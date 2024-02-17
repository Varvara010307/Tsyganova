a=10
b=5
c=0.5
for i in range (11):
    for j in range (21):
        for k in range(201):
            h=i*a+j*b+k*c
            x=i+j+k
            if (h<=100)and x==100:
                print(f'быков={i} коров={j} телят={k} ')