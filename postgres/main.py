import argparse
import logging
from databricks.sdk import WorkspaceClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
parser = argparse.ArgumentParser(description="Run Databricks WorkspaceClient with a profile.")
parser.add_argument('--profile', type=str, required=True, help='Databricks profile name')
parser.add_argument('--instance', type=str, required=True, help='Databricks Postgres instance name')

args = parser.parse_args()
w = WorkspaceClient(profile=args.profile)
logger.info(f"Using profile: {args.profile}")

db = w.database.get_database_instance(args.instance)
logger.info(db.uid)
logger.info(db.capacity)
