from flask import Flask
import socket
app=Flask(_name_)
@app.route("/home")
def lwhome():
     hostname=socket.gethostname()
     IPAddr=socket.gethostbyname(hostname)
     
     return f"welocme to lw,my hostname : {hostname} <br /> my ip: {IPAddr}"

app.run(host="0.0.0.0",port=5000)