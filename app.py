from flask import Flask, render_template
import json

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

############################# Calls ################################


@app.route('/test')
def test():
  client.healthCheck()
  return json.dumps({"message":"testing"})




########################### running the app ########################

@app.route("/")
def hello():
  return render_template('index.html')

if __name__ == "__main__":
  local = "localhost"
  local_port = "5678"
  real_host = "50.17.210.180"
  real_port = "5001"
  try:
    transport = TSocket.TSocket(real_host, real_port)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = HealthCheckService.Client(protocol)
    transport.open()
    app.run()
    transport.close()
  except:
    print "one of the server is not running"
