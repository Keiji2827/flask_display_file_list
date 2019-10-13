from flask import Flask, render_template, request, redirect, url_for
import subprocess
app = Flask(__name__)

def command_ls():
    flist = subprocess.check_output(["ls","-l"])
    # splitだと最終行の空文字列が残る
    flist = flist.decode("utf-8").splitlines()
    #del flist[0]
    flist.pop(0)
    return flist

def command_ls_back():
    flist = subprocess.check_output(["ls","-l","../"])
    # splitだと最終行の空文字列が残る
    flist = flist.decode("utf-8").splitlines()
    #del flist[0]
    flist.pop(0)
    return flist

@app.route('/')
def display_file_list():
    flist1 = command_ls()
    flist2 = command_ls_back()
    return render_template("index.html", flist1 = flist1, flist2 = flist2, title="index")

# 不使用
@app.route("/post", methods=["GET","POST"])
def post():
    title="next"

    if request.method == "POST":
        #name = request.form["name"]
        return render_template("index.html", message="次のページ", flist = ["a"], title=title)
    else :
        return redirect(url_for("index.html", flist=flist))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
