from github import Github
import pygit2

# using username and password establish connection to github
g = Github('tkeerthi30@gmail.com', 'Candy@3027')
org = g.get_organization('BCBS')

#create the new repository
repo = org.create_repo("Pygit2", description = "New Project Initiation" )

#create some new files in the repo
repo.create_file("/README.md", "init commit", readmeText)

#Clone the newly created repo
repoClone = pygit2.clone_repository(repo.git_url, '/home/ec2-user/Pygit')

#put the files in the repository here

#Commit it
repoClone.remotes.set_url("origin", repo.clone_url)
index = repoClone.index
index.add_all()
index.write()
author = pygit2.Signature("Keerthi", "tkeerthi30@gmail.com")
commiter = pygit2.Signature("Keerthi", "tkeerthi30@gmail.com")
tree = index.write_tree()
oid = repoClone.create_commit('refs/heads/master', author, commiter, "init commit",tree,[repoClone.head.get_object().hex])
remote = repoClone.remotes["origin"]
credentials = pygit2.UserPass('tkeerthi30@gmail.com', 'Candy@3027')
remote.credentials = credentials

callbacks=pygit2.RemoteCallbacks(credentials=credentials)

remote.push(['refs/heads/master'],callbacks=callbacks)




curl https://bootstrap.pypa.io/get-pip.py -o 
get-pip.py
python get-pip.py
git config --list --show-origin
git config --global user.name "keerthi"
git config --global user.email xxx@example.com
pip install xxx --disable-pip-version-check
sudo yum list | grep python3

https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/

sudo apt install python3-pip


Step1: install git (sudo apt-get instll git)
step 2: Python 3 Installation (https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/)
step 3: INstall pip ( sudo apt install python3-pip)
Step 4: INstall pygit2 (sudo pip3 install pygit2)
Step 5: Run Script (python3 script.py)
