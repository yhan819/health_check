from flask import Flask, render_template
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

'''
#localhost and port
host = "localhost"
learning_port = 5678
email_port = 11111 #has no access to email service locally
'''
# real host and port
host = "50.17.210.180"
learning_port = 5001
email_port = 5567 #fake port number. should fail


############################# Calls ################################


@app.route('/check_learning_service')
def check_learning_service():
  try:
    transport = TSocket.TSocket(host, learning_port)
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
  return json.dumps({"message":"learning service is up", "timestamp":t})


@app.route('/check_email_service')
def check_email_service():
  try:
    transport = TSocket.TSocket(host, email_port)
    transport.setTimeout(3000)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = HealthCheckService.Client(protocol)
    transport.open()
  except:
    print "cannot connect to the email service"
  client.healthCheck()
  transport.close()
  t = time.time()
  return json.dumps({"message": "email service is up", "timestamp":t})


########################### running the app ########################

@app.route("/")
def hello():
  return render_template('index.html')

if __name__ == "__main__":
  app.run()
