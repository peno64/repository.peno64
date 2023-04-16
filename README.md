# Cloning this repository

After making a local clone with the command \
git clone url \
Also the submodules must be cloned. This must be done with the command: \
git submodule update --init --recursive

# Updating addons in this repository

The root folder is the folder where the python script _repo_generator.py is located and subfolder repo exists. \
There are two cases:
- An addon is updated
- An addon is added

### An addon is updated

The addon sources are in folder repo. However that are in fact submodules. Make the needed changes to the addon in its own repository and don't forget to increment the version number in addon.xml \
When that is done and put in github, update the addon in folder repo via the git command \
git pull \
Possibly a message is given that no branch wasn't chosen yet. In that case give first the git command\
git checkout master \
Go in folder repo into the folder of the addon before executing above git command.

### An addon is added

The addon sources are in folder repo. However that are in fact submodules. First create a new repository for the addon and when that it done, create it as submodule in folder repo with the command: \
git submodule add &lt;url&gt; \
With url the url of the new addon. \
Since a new addon is added to the repo, the repo must also update. \
To force that, goto folder repo/repository.peno64. Edit addon.xml and increase the version number. \
Edit in the root file index.html and change the version numbers here also. Note that this must be done two times.

### After the changes are made to the addon/repo

Remove folder zips in folders repo. \
Run python script _repo_generator.py \
Remove file repository.peno64-x.y.zip in the root folder. \
Copy zip file repo/zips/repository.peno64/repository.peno64-x.y.zip to the root folder. \
This is also done by the batch file gen.bat

### Upload the changes to github
git add . \
git commit -m "comment" \
git push -u origin master

This is also done by the batch file upload.bat

