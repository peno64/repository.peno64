del /s pe.cfg
del /s *.bak
del /s repo\zips
del /s leia\zips
del /s matrix\zips
python _repo_generator.py
del *.zip
copy repo\zips\repository.peno64\*.zip
