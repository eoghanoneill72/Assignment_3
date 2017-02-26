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
    e = not e
    return e
        
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

# def create_grid(n):
#     [[False]*n for j in range(n)]
#     b = create_grid(n)
#     return b
# 
# def grid(n):
#     return [[False for i in range(n)] for j in range(n)]
n = 5
a = set_up(n)

print(a)
print(a[1][1])
toggle(a[1][1])
print(a[1][1])
count()

