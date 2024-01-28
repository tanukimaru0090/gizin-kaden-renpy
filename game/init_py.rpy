init 1 python:
    # ドットフォントで文字をフォーマットして返す
    def dot_mozi(text):
        return "{font=fonts/PixelMplus12-Regular.ttf}"+text+"{/font}"
    def font_mozi(font_path,text):
        return "{font={}}".format(font_path)+text+"{/font}"
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
    

