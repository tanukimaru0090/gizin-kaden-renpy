# このファイルにはゲームのスクリプトを記述します。
# Ren'Py のスクリプトは、インデント（行頭の空白）によってブロック分けされています。
# インデントは Tab や Shift + Tab によって調整することができます。
# ゲームは start ラベルからスタートします。

label start:
    call start_fade_out from _call_start_fade_out
    call prologue from _call_prologue
    call chapter1 from _call_chapter1
    call chapter2 from _call_chapter2
    call chapter3 from _call_chapter3
    call chapter4 from _call_chapter4
    call chapter5 from _call_chapter5
    call chapter6 from _call_chapter6
