
# このファイルにはゲームのスクリプトを記述します。

# Ren'Py のスクリプトは、インデント（行頭の空白）によってブロック分けされています。
# インデントは Tab や Shift + Tab によって調整することができます。


# まず最初に、ゲームに使うキャラクター（台詞を表示するオブジェクト）を定義します。
# 一番目のパラメーターは、テキストウィンドウに表示されるキャラクターの名前です。
# color のパラメーターを追加すると、キャラクターの名前を色付けできます。

# キャラクター定義
# test
#define e = Character('Eileen', color="#c8ffc8")

# 最初はすべてのキャラクターの名前は不明のため、???とする。

init python:
    # 主人公(男) 名前:物部重人
    m = Character(name="???",color="#0000FF")
    # スマホ(女) 名前:ジェナ
    g = Character(name="???",color="#FFFFFF")
    # ヤンキー(男) 名前:電子レンジ
    r = Character(name="???",color="#FF0000")
    
        
        

# label ステートメント（文）はゲームの処理をまとめてラベル付けします。
# ラベル間の移動は jump ステートメントか call ステートメントを使います。


label prologue:
    return    



# ゲームは start ラベルからスタートします。
label start:
    scene bg room
    call prologue
