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

The addon sources are in folder repo. Make the needed changes to the addon and don't forget to increment the version number in addon.xml

### An addon is added

The addon sources are in folder repo. Put the new addon there. \
Since a new addon is added to the repo, the repo must also update. \
To force that, goto folder repo/repository.peno64. Edit addon.xml and increase the version number. \
Edit in the root file index.html and change the version numbers here also. Note that this must be done two times.

### After the changes are made to the addon/repo

Remove folder zips in folders repo. \
Run python script _repo_generator.py \
Remove file repository.peno64-x.y.zip in the root folder. \
Copy zip file repo/zips/repository.peno64/repository.peno64-x.y.zip to the root folder.

### Upload the changes to github
git add . \
git commit -m "comment" \
git push -u origin master
