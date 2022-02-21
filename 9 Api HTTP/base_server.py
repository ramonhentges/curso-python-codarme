from http.server import HTTPServer, BaseHTTPRequestHandler
from usuario import Usuario
from usuario_html_model import head, title, table_head, table_body

userA = Usuario('Ramon', 'ram@gmail.com', '12345678')
userB = Usuario('Fernanda', 'fer@gmail.com', '12345952')
userC = Usuario('Chirulipa', 'xis@gmail.com', '12125678')
userD = Usuario('Mister', 'mister@gmail.com', '1963245678')

users = [userA, userB, userC, userD]


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/usuarios":
            # Enviar o status code da resposta: self.send_reponse(status_code)
            self.send_response(200)
            # Enviar cabeçalhos: self.send_header(nome, valor)
            self.send_header('content-type', 'text/html; charset=utf-8')
            # Finalizar cabeçalhos: self.end_headers()
            self.end_headers()
            # Escrever dados para o "socket" (wfile): self.wfile.write(data)
            html = f"""
                    <html>
                        {head}
                        {title}
                        <table>
                            {table_head}
                            {table_body(users)}
                        </table>
                    </html>
                    """
            self.wfile.write(html.encode())


server = HTTPServer(('localhost', 8000), SimpleHandler)
server.serve_forever()
