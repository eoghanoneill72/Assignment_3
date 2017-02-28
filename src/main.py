import urllib.request
import os

class led:
    def __init__(self,size):
        self.size=size
        self.a = [[False]*self.size for i in range(self.size)]
    
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
        x1,y1,x2,y2 = self.valid_parameters(x1,y1,x2,y2)
        for i in range(min(y1,y2),max(y1,y2)):
            for j in range(min(x1,x2),max(x1,x2)):
                if self.a[i][j] == False:
                    self.toggle(self.a[i][j])
            
     
    def switch(self,x1,y1,x2,y2):
        x1,y1,x2,y2 = self.valid_parameters(x1,y1,x2,y2)
        for i in range(min(y1,y2),max(y1,y2)):
            for j in range(min(x1,x2),max(x1,x2)):
                self.toggle(self.a[i][j])
                
    def turn_off(self,x1,y1,x2,y2):
        x1,y1,x2,y2 = self.valid_parameters(x1,y1,x2,y2)
        for i in range(min(y1,y2),max(y1,y2)):
            for j in range(min(x1,x2),max(x1,x2)):
                if self.a[i][j] == True:
                    self.toggle(self.a[i][j])
    
    def count(self):
#         return(sum([val for val in self.a() if val == True]))
        tally=0
        for i in range(self.size):
            for j in range(self.size):
                if self.a[i][j] == True:
                    tally+=1
        return tally
     
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
    
    size = int(lines[0])
    
    lights = led(size)
    
    for line in lines:
        if 'turn on' in line:
            coord1, coord2 = line.split(" ")[2::2]
            x1,y1 = coord1.split(",")
            x1,y1 = int(x1),int(y1)
            x2,y2 = coord2.split(",")
            x2,y2 = int(x2),int(y2)
            lights.turn_off(x1, y1, x2, y2)
        elif "turn off" in line:
            coord1, coord2 = line.split(" ")[2::2]
            x1,y1 = coord1.split(",")
            x1,y1 = int(x1),int(y1)
            x2,y2 = coord2.split(",")
            x2,y2 = int(x2),int(y2)
            lights.turn_on(x1, y1, x2, y2)
        elif "switch" in line:
            coord1, coord2 = line.split(" ")[1::2]
            x1,y1 = coord1.split(",")
            x1,y1 = int(x1),int(y1)
            x2,y2 = coord2.split(",")
            x2,y2 = int(x2),int(y2)
            lights.switch(x1, y1, x2, y2)
        
    print(lights.count())
        
main()




    

    
    

