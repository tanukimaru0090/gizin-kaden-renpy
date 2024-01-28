
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
# ただし、主人公は最初の時点で名前は判明していることとする。
# キャラクターの掛け合い時な}どにはキャラクターの名前とセリフを入れるが、地の文などは名前なしにする。
init 1 python:
    # ドットフォントで文字をフォーマットして返す
    def dot_mozi(text):
        return "{font=fonts/PixelMplus12-Regular.ttf}"+text+"{/font}"

init 2 python:
    # 名前:物部重人 性別:男 
    m = Character(name=dot_mozi("物部重人"),color="#0000FF")
    # 名前:ジェナ 性別:女
    g = Character(name=dot_mozi("???"),color="#FFFFFF")
    # 名前:電子レンジ 性別:男
    r = Character(name=dot_mozi("???"),color="#FF0000")
    # 

# init 3 python:
    
# init 4 python:  
    
# init 5 python:
    
# label ステートメント（文）はゲームの処理をまとめてラベル付けします。
# ラベル間の移動は jump ステートメントか call ステートメントを使います。


label prologue:
    # test 色々
    # $m(dot_mozi("おはよう"))

    # 冒頭
    $m(dot_mozi("休みの早朝、目が覚めたら家にある電化製品が無くなっていた。四畳半の一室に圧迫されていた冷蔵庫も洗濯機も、何もかもが綺麗に無くなっていた。"))
    $m(dot_mozi("男子高校生の一人暮らしにしては殺風景が過ぎる。"))

    $m(dot_mozi("存在するのはただ一つ、というより目の前の一人。"))
    # ジェナが正面に座っているスチルを表示
    $m(dot_mozi("銀髪ロングの美少女である。"))
    $m(dot_mozi("あまりにも現実感のない描写が、俺の視界に映り込んでいる。彼女は凛とした佇まいで、俺を瞬きもせずじっと見つめている。無表情だから軽く怖い。"))
    $m(dot_mozi("しかしなるほど把握した。これは夢だ。夢でしかない。夢以外に何があるのだ。そう思考した俺は、彼女とは別方向に倒れ込み二度寝を試みた。"))
    # ここで横になるときの効果音
    $g(dot_mozi("「おや。またおやすみになるのですか『マスター』」"))
    return    

label chapter1:
    return
label chapter2:
    return 
label chapter3:
    return 

# ゲームは start ラベルからスタートします。
label start:
    call prologue
    call chapter1
    call chapter2
    call chapter3
