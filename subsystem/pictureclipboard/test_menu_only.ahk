; メニュー表示テスト専用
#NoEnv
#SingleInstance Force

; シンプルなメニューテスト
^!s::
    MsgBox, 64, Test, Ctrl+Alt+S pressed! Creating menu...
    
    Menu, TestMenu, Add
    Menu, TestMenu, DeleteAll
    
    Menu, TestMenu, Add, Test Item 1, TestHandler
    Menu, TestMenu, Add, Test Item 2, TestHandler
    Menu, TestMenu, Add, Test Item 3, TestHandler
    
    Menu, TestMenu, Show
return

TestHandler:
    MsgBox, 64, Menu Test, You selected: %A_ThisMenuItem%
return

; 基本動作確認
^!t::
    MsgBox, 64, Key Test, Ctrl+Alt+T works!
return

MsgBox, 64, Menu Test Tool, 
(
Menu Test Started!

Tests:
Ctrl+Alt+T : Basic key test
Ctrl+Alt+S : Menu display test

If Ctrl+Alt+S shows "pressed!" but no menu appears,
there might be a menu system issue.
)