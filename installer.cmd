@ECHO OFF
:A
echo Enter Do you have all the pip modules installed ?
set/p "pass= say y/n :"
if NOT %pass%== n goto B
pip install os-sys
pip install PyMySQL
pip install stdiomask
pip install passlib
pip install cryptography
pip install color-it

@ECHO OFF
:B
echo Enter Do you have MySQL and Python 3 ?
set/p "pass= say y/n :"
if NOT %pass%== y goto Fail
1_python-3.8.6.exe
2_python-3.9.1-amd64.exe
3_mysql-installer-web-community-8.0.22.0.msi
4_mysql-connector-python-8.0.23-windows-x86-32bit.msi

echo Successfull
goto End
:Fail
echo Ok exiting....... 
timeout /t 10
:End
