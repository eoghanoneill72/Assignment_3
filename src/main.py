import random

n = 10
a = [[True]*n for i in range(n)]
# b = [False]*n*n

# total = 0
# for e in a:
#     if e == True:
#         total+=(sum(e))
# print(total)
 
 

b = [True if random.random() < 0.5 else False for _ in range(10)]
print("b is", b)

# compute the sum (only counts elements which are True)
def count():
    print(sum(b))


# b = [val for val in a if val == True]
print("b is: ",b)

# for val in a:
#     print(val)
    
print(b.count(True))

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
    return x1,y1,y2,y2

# def switch(a):
#     valid_parameters(x1, y1, x2, y2)
#     x = max(x1,x2)
#     y = max(y1,y2)
#     [not i for i in range a]
    
def toggle(a):
    a = not a 
    return a 
 
def switch(x1,y1,x2,y2):
    for i in range(min(y1,y2),max(y1,y2)):
        for j in range(min(x1,x2),max(x1,x2)):
            toggle(a[i][j])

def create_grid(n):
    [[True]*n*n]
    
print(create_grid(6))