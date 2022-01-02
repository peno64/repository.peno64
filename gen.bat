del /s pe.cfg
del /s *.bak
python _repo_generator.py
del *.zip
copy repo\zips\repository.peno64\*.zip
