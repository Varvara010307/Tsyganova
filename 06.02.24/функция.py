def equation(a,b):
    x1,y1=map(float, a.split(';'))
    x2, y2 = map(float, b.split(';'))
    k=(y2-y1)/(x2-x1)
    b=y1-k*x1
    print(f"{k} {b}")

equation("2;3", "5;1")