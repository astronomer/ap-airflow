import functools
import os
from airflow.plugins_manager import AirflowPlugin
from astronomer.certified.blueprint import ACThemeBlueprint
from astronomer.seed_log_template import seed_log_template

class AstronomerCertifiedPlugin(AirflowPlugin):

    name = "astronomer_certified_extensions"

    flask_blueprints = [ACThemeBlueprint()]

    @staticmethod
    def add_before_call(mod_or_cls, target, pre_fn):
        fn = getattr(mod_or_cls, target)

        @functools.wraps(fn)
        def run_before(*args, **kwargs):
            pre_fn()
            fn(*args, **kwargs)

        setattr(mod_or_cls, target, run_before)

    @classmethod
    def on_load(cls, *args, **kwargs):
        # Borrowed concept from version_check plugin.
        # Seed the log template table before synchronizing the template
        version = os.environ.get("ASTRONOMER_CERTIFIED_VERSION", "Unknown")

        import airflow.utils.db
        cls.add_before_call(
        airflow.utils.db, 'synchronize_log_template',
        seed_log_template
        )
