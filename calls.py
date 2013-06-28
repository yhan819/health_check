import sys
sys.path.append('gen_py')

from datetime import datetime
from healthservice import HealthCheckService
from healthservice.ttypes import *
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from flask import Flask
import app
from app import app
import json


