from http.server import BaseHTTPRequestHandler, HTTPServer
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
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes("{'message': 'OK'}", "utf-8"))  # Тело ответа

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