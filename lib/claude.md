# 概要
## ライブラリの目的
- 個人開発で行うGUIベースのアプリケーションを作っている。  
- Pythonは機械学習に強いが、実験計画法など統計計算によわい。 
- その弱い部分は自作ライブラリで計算させる
- このフォルダはその自作ライブラリのフォルダである。

## ライブラリ名
全体のライブラリ名はjikkenpy(JikkenPy)とする。  

# 機能
jikkenpy.designs : 実験計画法のデザインを行うライブラリ。
jikkenpy.designs.generator() : doegnerator classを返す。
例：
L8exp = jikkenpy.designs.generator("L8")
doegenerator classの機能
1. 因子名の割り付け（含む交互作用）
1. 分散分析
1. SN比の計算
jikkenpy.designs.generator()   


