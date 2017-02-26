import urllib.request
import argparse


def set_up(n):
    return[[False]*n for i in range(n)]

def valid_parameters(x1,y1,x2,y2):
    if x1 > n:
        x1 = n
    if x2 > n:
        x2 = n
    if y1 > n:
        y1 = n
    if y2 > n:
        y2 = n
    if x1 < 0:
        x1 = 0
    if x2 < 0:
        x2 = 0
    if y1 < 0:
        y1 = 0
    if y2 < 0:
        y2 = 0
    return x1,y1,x2,y2

def toggle(e):
    return not bool(e)
    
        
def turn_on(x1,y1,x2,y2):
    valid_parameters(x1,y1,x2,y2)
    for i in range(min(y1,y2),max(y1,y2)):
        for j in range(min(x1,x2),max(x1,x2)):
            if a[i][j] == False:
                toggle(a[i][j])
        
 
def switch(x1,y1,x2,y2):
    valid_parameters(x1,y1,x2,y2)
    for i in range(min(y1,y2),max(y1,y2)):
        for j in range(min(x1,x2),max(x1,x2)):
            toggle(a[i][j])
            
def turn_off(x1,y1,x2,y2):
    valid_parameters(x1,y1,x2,y2)
    for i in range(min(y1,y2),max(y1,y2)):
        for j in range(min(x1,x2),max(x1,x2)):
            if a[i][j] == True:
                toggle(a[i][j])

def count():
    print(sum([val for val in a if val == True]))

n = 5
a = set_up(n)

print(a)
print("before toggle",a[0][1])
toggle(a[0][1])
print("after toggle",a[0][1])
count()

filename = "data/data.txt"
with open(filename) as f:
    for line in f.readlines():
        # process line        
        values = line.strip().split()
        if len(values)==1:
            set_up(int(values[0]))
        if len(values)==7:
            x1 = int(values[2])
            y1 = int(values[3])
            x2 = int(values[5])
            y2 = int(values[6])
            state = values[1]
            if state == "on":
                turn_on(x1, y1, x2, y2)
            elif state == "off":
                turn_off(x1, y1, x2, y2)
        if len(values)==6:
            x1 = int(values[1])
            y1 = int(values[2])
            x2 = int(values[5])
            y2 = int(values[6])
            if values[0]=="switch":
                switch(x1, y1, x2, y2)
            
parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input help')
args = parser.parse_args()

filename = args.input




