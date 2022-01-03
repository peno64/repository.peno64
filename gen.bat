@echo off
del /s /q pe.cfg
del /s /q *.bak
del /s /q repo\zips
del /s /q leia\zips
del /s /q matrix\zips
python _repo_generator.py
del /q *.zip
copy repo\zips\repository.peno64\*.zip
