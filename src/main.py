import urllib.request
import argparse
from email._header_value_parser import get_invalid_parameter



class led:
    def __init__(self,size):
        self.size=size
          
    def set_up(self):
        return[[False]*self.size for i in range(self.size)]
    
    def valid_parameters(self,x1,y1,x2,y2):
        if x1 > self.size:
            x1 = self.size
        if x2 > self.size:
            x2 = self.size
        if y1 > self.size:
            y1 = self.size
        if y2 > self.size:
            y2 = self.size
        if x1 < 0:
            x1 = 0
        if x2 < 0:
            x2 = 0
        if y1 < 0:
            y1 = 0
        if y2 < 0:
            y2 = 0
        return x1,y1,x2,y2
    
    def toggle(self,e):
        return not e
        
            
    def turn_on(self,x1,y1,x2,y2):
#         x1 = self.valid_parameter(x1)
        x1,y1,x2,y2 = self.valid_parameters(x1,y1,x2,y2)
        for i in range(min(y1,y2),max(y1,y2)):
            for j in range(min(x1,x2),max(x1,x2)):
                if a[i][j] == False:
                    self.toggle(a[i][j])
            
     
    def switch(self,x1,y1,x2,y2):
        x1,y1,x2,y2 = self.valid_parameters(x1,y1,x2,y2)
        for i in range(min(y1,y2),max(y1,y2)):
            for j in range(min(x1,x2),max(x1,x2)):
                self.toggle(a[i][j])
                
    def turn_off(self,x1,y1,x2,y2):
        x1,y1,x2,y2 = self.valid_parameters(x1,y1,x2,y2)
        for i in range(min(y1,y2),max(y1,y2)):
            for j in range(min(x1,x2),max(x1,x2)):
                if a[i][j] == True:
                    self.toggle(a[i][j])
    
    def count(self):
        print(sum([val for val in a if val == True]))


a = led(5)
c = a.set_up()
print(c)
print("before toggle",c[0][1])
c[0][1] = a.toggle(c[0][1])
print("after toggle",c[0][1])

# filename = "data/data.txt"
# with open(filename) as f:
#     for line in f.readlines():
#         # process line        
#         values = line.strip().split()
#         if len(values)==1:
#             led.set_up(int(values[0]))
#         if len(values)==7:
#             x1 = int(values[2])
#             y1 = int(values[3])
#             x2 = int(values[5])
#             y2 = int(values[6])
#             state = values[1]
#             if state == "on":
#                 led.turn_on(x1, y1, x2, y2)
#             elif state == "off":
#                 led.turn_off(x1, y1, x2, y2)
#         if len(values)==6:
#             x1 = int(values[1])
#             y1 = int(values[2])
#             x2 = int(values[5])
#             y2 = int(values[6])
#             if values[0]=="switch":
#                 led.switch(x1, y1, x2, y2)
#             
# parser = argparse.ArgumentParser()
# parser.add_argument('--input', help='input help')
# args = parser.parse_args()
# 
# filename = args.input


k = led(200)

a,b,c,d = 5000,-100,9000,5
e,f,g,h = k.valid_parameters(a,b,c,d)

print(e,f,g,h)

