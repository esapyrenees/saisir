
import sys
from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer
import ssl


def test(HandlerClass=SimpleHTTPRequestHandler,
         ServerClass=BaseHTTPServer.HTTPServer):

    protocol = "HTTP/1.0"
    host = ''
    port = 4443
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if ':' in arg:
            host, port = arg.split(':')
            port = int(port)
        else:
            try:
                port = int(sys.argv[1])
            except:
                host = sys.argv[1]

    server_address = (host, port)

    HandlerClass.protocol_version = protocol
    httpd = ServerClass(server_address, HandlerClass)

    # ssl
    httpd.socket = ssl.wrap_socket (httpd.socket, certfile='server.includesprivatekey.pem', server_side=True)
    sa = httpd.socket.getsockname()

    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()


if __name__ == "__main__":
    test()

