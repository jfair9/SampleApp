from github import Github

# Authentication is defined via github.Auth
from github import Auth

repo = 'SampleApp'
owner = 'jfair9'
branch = 'develop'
contexts = ["Scan Dev1/checkov-app-dev1"]

# using an access token
auth = Auth.Token("")

# First create a Github instance:

# Public Web Github
g = Github(auth=auth)

repo = g.get_repo(owner + "/" + repo)
branch = repo.get_branch(branch)
current_checks = branch.get_required_status_checks()

current_contexts = current_checks.contexts

# branch.edit_required_status_checks(strict=True, contexts=current_contexts + contexts)
repo.create_file("test.txt", "test", "test", branch="test")
{'content': ContentFile(path="test.txt"), 'commit': Commit(sha="5b584cf6d32d960bb7bee8ce94f161d939aec377")}
# contents = repo.get_contents(".github/workflows")
# while contents:
#     file_content = contents.pop(0)
#     if file_content.type == "dir":
#         contents.extend(repo.get_contents(file_content.path))
#     else:
#         print(file_content.decoded_content.decode())