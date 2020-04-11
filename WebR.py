import requests
import Esentiale

class WebR:
    debug = False
    printerName = "WebR"

    def __init__(self, prox=""):
        self.myproxy = ""
        self.session = requests.Session()
        self.session.verify = False
        self.session.wtrust_env = False

    def set_proxy(self, prox):
        case = prox.count(":")
        if (case == 1):
            self.myproxy = {
                "https": "https://{}@{}/".format(":", prox),
                "http": "http://{}@{}/".format(":", prox)
            }
        elif (case == 3):
            sp = prox.split(":")
            self.myproxy = {
                "https": "https://{}:{}@{}:{}/".format(sp[2], sp[3], sp[0], sp[1]),
                "http": "http://{}:{}@{}:{}/".format(sp[2], sp[3], sp[0], sp[1])
            }
        else:
            self.myproxy = {
                "https": "",
                "http": ""
            }
        self.printX("Proxy case " + str(case) + ": " + str(self.myproxy))

    def GET(self, url, headers):
        self.printX("GET: " + url)
        try:
            response = self.session.get(url, headers=headers, proxies=self.myproxy)
        except Exception as e:
            self.printX("GET ERROR:" + str(e))
            return "error"
        return response.text

    def POST(self, url, postData, headers):
        self.printX("POST: " + url)
        try:
            response = self.session.post(url, postData, headers=headers, proxies=self.myproxy)
        except Exception as e:
            self.printX("POST ERROR:" + str(e))
            return "error"
        return response.text

    def save_cookies(self, identif):
        Esentiale.save_to_file(str(self.session.cookies), identif)
        self.printX("Cookies saved: " + str(self.session.cookies))

    def load_cookies(self, identif):
        mycook=Esentiale.get_from_file(identif)
        mycook_lst=str(mycook).replace('>, <',"~~").replace("[<", "~~").replace('>]',"~~").split('~~')
        lst={}
        for i in range(1,len(mycook_lst)-1):
            sp=str(mycook_lst[i]).replace("="," ").split(" ")
            lst[sp[1]] = sp[2]
        self.session.cookies.update(lst)
        self.printX("Cookies loaded: " + str(lst))

    def printX(self, txt):
        if self.debug:
            print("[", self.printerName, "]  ", txt)
