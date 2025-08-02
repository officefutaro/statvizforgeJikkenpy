; 修正版シンプルテスト
#NoEnv
#SingleInstance Force
SendMode Input
SetWorkingDir %A_ScriptDir%

; F12キーでテスト
F12::
    MsgBox, 64, Test, F12 key pressed manually!
return

; Ctrl+J でテスト
^j::
    MsgBox, 64, Test, Ctrl+J pressed manually!
return

; 起動完了メッセージ（キーイベントではない）
Sleep, 100
MsgBox, 64, Startup, Fixed Simple Test Ready!`n`nPress F12 or Ctrl+J to test