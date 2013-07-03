SERVICES = {
  "learning":{"host":"50.17.210.180", "port":5001}, #learning service
  "email":{"host":"50.17.210.180", "port":5567}, #email service (not connected)
}

def get_service(service):
  return SERVICES[service]
