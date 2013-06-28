#!/bin/sh
thrift --gen py -out gen_py/ thrift/HealthCheckService.thrift
