

class utils():
    def common_header(self):
        Header = {
            "Content-Type": "application/json"
        }
        return Header

    def put_patch_del_header_basicauth(self,basic_auth_value):
        Header ={
            "Content-Type" : "application/json",
            "Authorization" :"Basic" + str(basic_auth_value)
        }
        return Header

    def put_patch_del_header_cookie(self, cookie_value):
        Header = {
            "Content-Type": "application/json",
            "Cookie" : "token=" + str(cookie_value)
        }
        return Header