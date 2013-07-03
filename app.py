from flask import Flask, render_template
from config import get_service
import json
import time

import sys
sys.path.append('gen_py')

from datetime import datetime
from healthservice import HealthCheckService
from healthservice.ttypes import *
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

app = Flask(__name__)
app.config["DEBUG"] = True


############################# Calls ################################


@app.route('/check_service/<service>')
def check_service(service):
  info = get_service(service)
  try:
    transport = TSocket.TSocket(info["host"], info["port"])
    transport.setTimeout(3000)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = HealthCheckService.Client(protocol)
    transport.open()
  except:
    print "cannot connect to the learning service"
  client.healthCheck()
  transport.close()
  t = time.time()
  return json.dumps({"message": service + " service is up", "timestamp":t})


########################### running the app ########################


@app.route("/")
def hello():
  return render_template('index.html')

if __name__ == "__main__":
  app.run()
