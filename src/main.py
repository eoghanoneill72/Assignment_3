import urllib
import argparse
from email._header_value_parser import get_invalid_parameter
from fileinput import filename
import urllib.request
import os
import sys
from src import main
import re

class led:
    def __init__(self,size):
        self.size=size
#         self.a = [[False]*self.size for i in range(self.size)]  
        return
     
    def grid(self):
        a = [[False]*self.size for i in range(self.size)]
        return a
    
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
                    self.toggle(self.grid[i][j])
            
     
    def switch(self,x1,y1,x2,y2):
        x1,y1,x2,y2 = self.valid_parameters(x1,y1,x2,y2)
        for i in range(min(y1,y2),max(y1,y2)):
            for j in range(min(x1,x2),max(x1,x2)):
                self.toggle(self.grid()[i][j])
                
    def turn_off(self,x1,y1,x2,y2):
        x1,y1,x2,y2 = self.valid_parameters(x1,y1,x2,y2)
        for i in range(min(y1,y2),max(y1,y2)):
            for j in range(min(x1,x2),max(x1,x2)):
                if self.grid()[i][j] == True:
                    self.toggle(self.grid()[i][j])
    
    def count(self):
        return(sum([val for val in self.grid() if val == True]))
    
    def parse_cmd_str(self):
        pass
    
    def execute(self, cmd_str):
        cmd,x1,y1,x2,y2 = self.parse_cmd_str(cmd_str)
        if cmd == "turn on":
            self.turn_on(x1, y1, x2, y2)
        elif cmd == "turn on":
            self.turn_on(x1, y1, x2, y2)
        elif cmd == "switch":
            self.turn_on(x1, y1, x2, y2)
        
        pass
        
filename = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"

def read_file(filename):
    if filename.startswith("http"):
        fh = urllib.request.urlopen(filename)
        file_str = fh.read().decode()
        return file_str
    else:
        if not os.path.isfile(filename):
            print("file does not exist")
        else:
            file_str = open(filename, "r").read()
            return file_str

def main():
    ##buffer is big string of entire file
    buffer = read_file(filename)
    ##lines is list of strings
    lines = buffer.split('\n')
#     print("lines = ", lines)
#     print("len(lines) = ", len(lines))
    ##split string element in list of strings into list of words
    size = int(lines[0])
    lights = led(size)
    for i in lines:
#     line = re.sub("[^\w]", " ",  lines[i]).split()
        if 'turn on' in i:
            arg0, arg1, arg2, arg3, arg4 = i.split(" ")
            x1,y1 = arg2.split()
            x2,y2 = arg4.split()
            lights.turn_off(x1, y1, x2, y2)
        elif "turn off" in i:
            arg0, arg1, arg2, arg3, arg4 = i.split(" ")
            x1,y1 = arg2.split()
            x2,y2 = arg4.split()
            lights.turn_off(arg2,arg4)
        elif "switch" in i:
            arg0, arg1, arg2, arg3= i.split(" ")
            x1,y1 = arg2.split()
            x2,y2 = arg3.split()
            lights.switch(arg2,arg3)
            
    
    # print("line 2, element 1 = ", lines[1][0])
    # print("print(lines[1:])",lines[1:])
    # print("buffer = ", buffer)
    
    #########################
    
    main.led(int(lines[0]))
    
#     for i in line:
#         if len(line)==7:
#             x1 = int(line[2])
#             y1 = int(line[3])
#             x2 = int(line[5])
#             y2 = int(line[6])
#             state = line[1]
#             if state == "on":
#                 main.led.turn_on(x1, y1, x2, y2)
#             elif state == "off":
#                 main.led.turn_off(x1, y1, x2, y2)
#         if len(line)==6:
#             x1 = int(line[1])
#             y1 = int(line[2])
#             x2 = int(line[5])
#             y2 = int(line[6])
#             if line[0]=="switch":
#                 main.led.switch(x1, y1, x2, y2)    

    
    

