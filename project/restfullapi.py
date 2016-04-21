from bottle import route

@route('/<command>')
def ping(command=None):
  if command.lower() == "ping":
    return "pong!"
  else:
    return "Unknown command"

@route('/')
def main():
  return "Simple RESTfull API: curl -X GET $URL/ping"

