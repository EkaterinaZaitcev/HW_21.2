from http.server import BaseHTTPRequestHandler, HTTPServer
import os.path
import time

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200) # Отправка кода ответа
        self.send_header("Content-type", "text/html")
        """ Отправка типа данных, который будет передаваться"""
        self.end_headers()

        # чтение файла с кодом страницы "Контакты"
        with open(os.path.join(os.path.dirname(__file__), "pages", "contacts.html"), encoding="utf-8") as f:
            content = f.read()
        self.wfile.write(bytes(content, "utf-8"))

if __name__ == "__main__":

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
            """ Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов"""
            webServer.serve_forever()
    except KeyboardInterrupt:

        pass

    webServer.server_close()
    print("Server stopped.")