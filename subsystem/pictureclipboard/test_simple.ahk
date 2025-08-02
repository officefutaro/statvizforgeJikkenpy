; 簡易テスト版
#NoEnv
#SingleInstance Force

; テスト用ホットキー
#+t::
    MsgBox, 64, Test, AutoHotkey is working!
return

; WSLテスト
#+w::
    RunWait, wsl.exe -d Ubuntu -- echo "WSL Test OK", Result, Hide
    MsgBox, 64, WSL Test, WSL command executed
return