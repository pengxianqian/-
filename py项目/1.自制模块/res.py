import re
class Re:
    def __init__(self):
        self.pattern = None
    
    def match(self,x,y):
        self.pattern = re.compile(x)
        if self.pattern.search(str(y)):
            print('匹配')
        else :
            print('不匹配')
            
    def day(self,mouth):    
        self.match(r'^((0?[1-9])|((1|2)[0-9])|30|31)$',mouth)
    
    def email(self,email):
        self.match(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$',email)  
    
    def mobile_number(self,number):
        self.match(r'^(13[0-9]|14[0-9]|15[0-9]|166|17[0-9]|18[0-9]|19[0-9]|19[8|9])\d{8}$',number) 
        
    def id_card_number(self,number):
        self.match(r'^((\d{18})|([0-9x]{18})|([0-9X]{18}))$',number)       
        
if __name__ == '__main__':
    r = Re()
    r.day(12)
    r.email('123456@qq.com')
    r.mobile_number(19561783812)   
    r.id_card_number(411525200606079656)     
