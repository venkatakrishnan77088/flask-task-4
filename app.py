from flask import Flask,render_template,request
import requests
import sqlite3 as venkat


app=Flask(__name__)


@app.route("/add", methods=["POST","GET"])
def datadheep():
          #  dic=None
           # if request.form.get("number")!=None:
                dot=request.form.get("number")
                res=requests.get("https://api.mfapi.in/mf/"+str(dot))
                fund=res.json().get("meta").get("fund_house")
                nav = res.json().get("data")[0].get("nav")
                dic ={"id":dot,"fund":fund,"nav":nav}
                conn=venkat.connect("scheme.db")
                cur=conn.cursor()
                cur.execute("insert into fund (ID,FUND,NAV) values(?,?,?)",(dot,fund,nav))
                conn.commit()
                return render_template("index.html")
        
        
        
        
@app.route("/venkats",methods=["get","post"])
def venkats():
    return "<h1>venkat has good time</h1>"

if __name__=="__main__":
    app.run(debug=True)