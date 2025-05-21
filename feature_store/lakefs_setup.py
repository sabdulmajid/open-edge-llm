from lakefs_client import LakeFSClient
from lakefs_client.models import RepositoryCreation, BranchCreation

lakefs = LakeFSClient(host='http://localhost:8000', username='lakefs', password='lakefs')

# Create repo and branch if not exist
def setup_repo(repo_name, branch_name):
    try:
        lakefs.repositories.create_repository(RepositoryCreation(repository_id=repo_name, storage_namespace=f's3://{repo_name}'))
    except Exception:
        pass
    try:
        lakefs.branches.create_branch(repo_name, BranchCreation(name=branch_name, source='main'))
    except Exception:
        pass

if __name__ == "__main__":
    setup_repo('openedge-corpora', 'dev')
