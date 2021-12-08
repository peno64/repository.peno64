# Updating addons in this repository

The root folder is the folder where the python script _repo_generator.py is located, subfolders - and repo exist.\
There are two cases:\
- An adddon is updated
- An addon is added

### An adddon is updated

The addon sources are in folder repo. Make the needed changes to the addon and don't forget to increment the version number in addon.xml

### An adddon is added

The addon sources are in folder repo. Put the addon there in its folder.\
Since a new addon is added to the repo, the repo must also update.\
To force that, goto folder -/repository.peno64. Edit addon.xml and increase the version number.

### After the changes are made to the addon/repo

Remove folders zips in folders - and repo\
Run python script _repo_generator.py\
Remove file repository.peno64-x.y.zip in the root folder.\
Copy zip file -/zips/repository.peno64/repository.peno64-x.y.zip to the root folder.\
If the version number of -/repository.peno64/addon.xml has changed, edit index.html and change it here also. Note that this must be done two times.

### Upload the changes to github
git add .\
git commit -m "comment"\
git push -u origin master\
