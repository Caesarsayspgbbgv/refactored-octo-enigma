from flask import Flask
app=Flask(__name__)

@app.route("/")
def home():
  return "麻豆传媒映画"

if __name__=="__main__":
  app.run()