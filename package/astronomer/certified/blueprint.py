import os
import airflow
from airflow.utils.log.logging_mixin import LoggingMixin
from packaging.version import Version

from flask import Blueprint

def transform_airflow_version(airflow_ver):

    parsed = Version(airflow_ver)

    ver = '.'.join(str(x) for x in parsed.release)

    if parsed.local:
        local = parsed._version.local[1]
        ver += '.post' + str(local)

    if parsed.is_devrelease:
        ver += '.dev' + str(parsed.dev)

    return ver

def get_versions():
    try:
        airflow_version = airflow.__version__
        airflow_upstream_version = airflow_version.split('.dev')[0].split('+astro')[0]
    except Exception:
        airflow_version = None
        airflow_upstream_version = None
    ac_version = os.environ.get("ASTRONOMER_CERTIFIED_VERSION", "Unknown")
    if 'astro' in ac_version:
        ac_version = transform_airflow_version(ac_version)
    return ac_version, airflow_upstream_version


class ACThemeBlueprint(Blueprint, LoggingMixin):

    original_base_template = None

    def __init__(self):

        super().__init__(
            "AstronomerCertifiedTheme",
            __name__,
            static_url_path='/astro',
            static_folder="static",
            template_folder=os.path.join(os.path.dirname(__file__), "templates"),
        )

    def new_template_vars(self):
        ac_version, airflow_upstream_version = get_versions()
        return {
            "original_base_template": self.original_base_template,
            'ac_version': ac_version,
            'airflow_upstream_version': airflow_upstream_version,
        }

    def register(self, app, *args, **kwargs):
        """
        Re-configure Flask to use our customized layout (that includes the call-home JS)
        Called by Flask when registering the blueprint to the app
        """

        # Don't run if we're not at appbuilder stage yet
        if not hasattr(app, "appbuilder"):
            return

        # Change documentation menu if needed
        app.appbuilder.add_link(
            name="Astronomer",
            label="Astronomer Docs",
            href='https://www.astronomer.io/docs',
            category="Astronomer",
        )
        app.appbuilder.add_link(
            name="Astronomer",
            label="Astronomer Registry",
            href='https://registry.astronomer.io',
            category="Astronomer",
        )
        app.appbuilder.add_link(
            name="Astronomer",
            label="Airflow Guides",
            href='https://www.astronomer.io/guides',
            category="Astronomer",
        )

        # Change base template if needed
        self.original_base_template = app.appbuilder.base_template
        if app.appbuilder.base_template in ["airflow/master.html", "airflow/main.html",  "astro-baselayout.html"]:
            app.appbuilder.base_template = "certified_base.html"
        else:
            self.log.warning(
                "Not replacing appbuilder.base_template, it didn't have the expected value. Update"
                " available messages will not be visible in UI"
            )

        # Let us inject variables into the Jinja context
        self.app_context_processor(self.new_template_vars)

        super().register(app, *args, **kwargs)
