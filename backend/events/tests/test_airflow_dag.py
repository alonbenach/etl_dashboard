import unittest
import os
from airflow.models.dagbag import DagBag


class TestDAGIntegrity(unittest.TestCase):
    def setUp(self):
        dag_folder = os.path.abspath("/app/dags")
        self.dagbag = DagBag(dag_folder=dag_folder, include_examples=False)

    def test_dag_imports_clean(self):
        """Ensure there are no import errors in any DAGs."""
        self.assertEqual(
            len(self.dagbag.import_errors),
            0,
            f"DAG import errors: {self.dagbag.import_errors}",
        )

    def test_daily_metrics_dag_exists(self):
        """Confirm daily_metrics_dag is present."""
        self.assertIn("daily_metrics_dag", self.dagbag.dags)

    def test_daily_metrics_dag_has_compute_task(self):
        """Check if compute_metrics task exists in the DAG."""
        dag = self.dagbag.dags.get("daily_metrics_dag")
        self.assertIsNotNone(dag, "DAG not found")
        self.assertIn("compute_metrics", dag.task_ids)
