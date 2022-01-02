@echo off
if @%1 == @ goto usage
del *.zip
copy repo\zips\repository.peno64\*.zip
git add .
git commit  -m %1
git push -u origin master
goto done
:usage
echo %0 "commit message"
:done
