@echo off

set fn=%1
set public_private=%2
cd /d %~dp0

If "%1"=="" (
    echo "create <folder_name> <public/private>"
) else (
    python create.py %fn% %public_private%
)
