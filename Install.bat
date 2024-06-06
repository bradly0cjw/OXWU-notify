@echo off
@REM :TNMENU
@REM cls
@REM color 3
@REM echo -------------------------------------------------------------------------
@REM echo - 地牛Wake UP!連動 Discord-Webhook-EEW (套件安裝)
@REM echo - By.Eric101201 , ChocoMing
@REM echo -
@REM echo - 1.開始安裝 Start Install                             
@REM echo - 0.離開 Exit      
@REM echo -------------------------------------------------------------------------

@REM set choice=
@REM set /p choice= 請輸入數字 :
@REM if '%choice%'=='1' goto ST
@REM if '%choice%'=='0' goto OEND
@REM echo "%choice%" is not vaild, try again
@REM goto TNMENU

@REM :ST
@REM cls
@REM echo - 安裝discord_webhook套件中。
@REM pip install discord_webhook
@REM echo - 安裝完成。
@REM echo - 安裝dotenv套件中。
@REM pip install python-dotenv
@REM echo - 安裝完成。
@REM echo - By.Eric101201 , ChocoMing
@REM timeout /t 5
@REM goto OEND

@REM :OEND
@REM color c
@REM cls
@REM echo -------------------------------------------------------------------------
@REM echo - 地牛Wake UP!連動 Discord-Webhook-EEW (套件安裝)
@REM echo - By.Eric101201 , ChocoMing
@REM echo -
@REM echo - 確定離開? Sure Leave?
@REM echo -
@REM echo - 1.取消 Cancel
@REM echo - 0.離開 Exit      
@REM echo -------------------------------------------------------------------------

@REM set choice=
@REM set /p choice= 請輸入數字 :
@REM if '%choice%'=='1' goto TNMENU
@REM if '%choice%'=='0' goto END
@REM echo "%choice%" is not vaild, try again
@REM goto OEND

@REM :END

pip install -r requirements.txt