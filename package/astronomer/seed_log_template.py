import logging
from airflow.utils.session import provide_session

log = logging.getLogger(__name__)

@provide_session
def seed_log_template(*, session=None) -> None:
    """Add historical log_template record for ES log_id_template
    This only adds the historical values if the log_template table is empty -
    new install or initial upgrade to 2.3.0+.
    """

    from airflow.utils.db import reflect_tables
    from airflow.models.tasklog import LogTemplate

    def log_template_exists():
        metadata = reflect_tables([LogTemplate], session)
        log_template_table = metadata.tables.get(LogTemplate.__tablename__)
        return log_template_table is not None
    if not log_template_exists:
        log.info('Log template table does not exist (added in 2.3.0); skipping log template seeding.')
        return

    # The Astronomer chart overrode the default log_id_template to this
    log_id = "{dag_id}_{task_id}_{execution_date}_{try_number}"
    # While the log_filename_template was the default
    filename = "{{ ti.dag_id }}/{{ ti.task_id }}/{{ ts }}/{{ try_number }}.log"

    # We mistakenly seeded this in 2.3.0. We need to update it to the new format.
    old_log_id = "{dag_id}_{task_id}_{run_id}_{try_number}"

    updated = (
        session.query(LogTemplate)
        .filter(LogTemplate.elasticsearch_id == old_log_id)
        .update({LogTemplate.elasticsearch_id: log_id})
    )
    if updated or session.query(LogTemplate.id).first():
        return
    else:
        session.add(LogTemplate(filename=filename, elasticsearch_id=log_id))
