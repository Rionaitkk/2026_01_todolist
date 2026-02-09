# Webアプリ表示のツール、html表示のツール、入力データ受け取りのツール、画面遷移のツール
from flask import Flask, render_template, request, redirect


app = Flask(__name__)# おまじない

todo_list = []  # TODOリストを保存するためのリスト
done_list = []  # 完了リストを保存するためのリスト
@app.route("/")  # ルートURLにアクセスしたときの処理(アドレスの最後が/のとき下の関数を実行して)
def index():
    return render_template("index.html", todo_list=todo_list, done_list=done_list)  # index.htmlを表示し、todo_listを渡す（これでapp.pyもhtmlもtodo_listが使える）

@app.route("/add", methods=["POST"])  # /addにPOSTリクエストが来たときの処理
def add_todo():
    todo_item = request.form.get("todo_item")  # フォームから送信されたTODOアイテムを取得
    if todo_item:  # アイテムが空でない場合
        todo_list.append(todo_item)  # TODOリストに追加
    return redirect("/")  # redirect(/)で自動的にトップページに戻る

# 完了リスト
@app.route("/done/<int:index>")  # /done/<index>にアクセスしたときの処理
def mark_done(index):
    done_item = todo_list.pop(index)  # 指定されたインデックスのTODOアイテムをTODOリストから削除
    done_list.append(done_item)  # 完了リストに追加
    return redirect("/")  # トップページに戻る

@app.route('/delete/<int:index>') # /delete/<index>にアクセスしたときの処理
def delete_todo(index):
    todo_list.pop(index)  # 指定されたインデックスのTODOアイテムをTODOリストから削除
    return redirect("/")  # トップページに戻る

app.run(debug=True)  # デバッグモードでアプリを起動