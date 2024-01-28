
# このファイルにはゲームのスクリプトを記述します。

# Ren'Py のスクリプトは、インデント（行頭の空白）によってブロック分けされています。
# インデントは Tab や Shift + Tab によって調整することができます。


init 1 python:
    # ドットフォントで文字をフォーマットして返す
    def dot_mozi(text):
        return "{font=fonts/PixelMplus12-Regular.ttf}"+text+"{/font}"
    def font_mozi(font_name,text):
        return "{font={}}".format(font_name)+text+"{/font}"
init 2 python:
    # キャラクター定義
    # 基本的にどのキャラクターの名前も不明だが、主人公は例外とする。
    # また、キャラ同士の掛け合いなどの際は名前とセリフ両方の表示をするが、地の文の際はなしにする。
    
    # 主人公の地の文
    m_z = Character(name=dot_mozi(""),color="#0000FF")
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

# プロローグ
label prologue:
    # test 色々
    # $m(dot_mozi("おはよう"))
    #with vpunch
    # 冒頭 
    $m(dot_mozi("休みの早朝、目が覚めたら家にある電化製品が無くなっていた。四畳半の一室に圧迫されていた冷蔵庫も洗濯機も、何もかもが綺麗に無くなっていた。"))
    
    $m(dot_mozi("男子高校生の一人暮らしにしては殺風景が過ぎる。")) 
    
    $m(dot_mozi("存在するのはただ一つ、というより目の前の一人。"))
    
    # ジェナが正面に座っているスチルを表示
    $m(dot_mozi("{size=+20}銀髪ロングの美少女である。{/size}"))
    
    $m(dot_mozi("あまりにも現実感のない描写が、俺の視界に映り込んでいる。彼女は凛とした佇まいで、俺を瞬きもせずじっと見つめている。無表情だから軽く怖い。"))
    
    $m(dot_mozi("しかしなるほど把握した。これは夢だ。夢でしかない。夢以外に何があるのだ。"))
    
    $m_z(dot_mozi("そう思考した俺は、彼女とは別方向に倒れ込み二度寝を試みた。"))
    # ここで横になるときの効果音
    
    $g(dot_mozi("「おや。またおやすみになるのですか『マスター』」"))
    
    $m_z(dot_mozi("儚げで美しい声が彼女から発せられた気がしたが、気のせいだ。夢なのだから。"))
    
    $m(dot_mozi("にしてもマスターっていう呼び方いいなぁ。アニメキャラみたいで。"))

    $g(dot_mozi("「ならば当機も、添い寝させていただきますね」"))
    
    $m(dot_mozi("一人称独特っ。"))
    
    $m_z(dot_mozi("それにしても何だか声が近く、しかも凄くいい匂いがより身近に感じられるような気がしたが、これも気のせいだ。夢は夢なのだから。"))

    $g(dot_mozi("「それではマスターが安眠できるように、子守唄……ではなく子守話でもしましょう」"))
    
    $m_z(dot_mozi("彼女の声があまりにも心地よく、何だか安心する。あぁこれがいわゆるバブみというやつなのだろう。年下かどうかは分からんが。だが悲しいかな、これも夢なのだ。"
    ))

    return    
# チャプター1(電子レンジ編)
label chapter1:
    return
# チャプター2()
label chapter2:
    return 
# チャプター3()
label chapter3:
    return 
# チャプター4()
label chapter4:
    return 
# チャプター5()
label chapter5:
    return 
# チャプター6()
label chapter6:
    return 

# ゲームは start ラベルからスタートします。
label start:
    call prologue
    call chapter1
    call chapter2
    call chapter3
    call chapter4
    call chapter5
    call chapter6
