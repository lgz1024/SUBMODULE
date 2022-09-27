@echo off
if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit
:begin

cd C:\D\my_world\out\production\my_world
java MainClass
rem @pause
 @exit rem 退出