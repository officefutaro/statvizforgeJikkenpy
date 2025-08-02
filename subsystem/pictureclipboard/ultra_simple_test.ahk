; 超シンプルテスト
#NoEnv
#SingleInstance Force

; F12キーでテスト（競合しにくい）
F12::
    MsgBox, F12 key works!
return

; Ctrl+J でテスト
^j::
    MsgBox, Ctrl+J works!
return

; 起動確認
MsgBox, Ultra Simple Test Started! Press F12 or Ctrl+J