from flask import Flask

app = Flask(__name__)

@app.route("/")
async def route():
    return "<h1>Check <a href='https://github.com/SPARKBRO/Auto-delete-bot'>AutoDelete</a></h1>"

if __name__ == "__main__":     
   app.run()
