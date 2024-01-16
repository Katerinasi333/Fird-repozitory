x=float(input())
y=float(input())
def IsPointInArea(x, y):
    return (y>=-x and y>=2*x+2 and (x+1)**2+(y-1)**2<=4) or (y<=-x and y<=2*x+2 and (x+1)**2+(y-1)**2>=4)
    
if IsPointInArea(x, y):
     print ("YES")
else:
     print("NO")