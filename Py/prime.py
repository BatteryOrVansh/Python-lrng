v = int(input('enter ur num: '))
c=False
if v!=1:

    for i in range(2,v+1):
        for j in range(2,i):
            
            if i%j==0:
                c=True
                break
            else:
                c=False
            
  
        if c==False:
            print(i)

else:
    print('enter above 1 cz 1 is neither prime nor  composite')
    