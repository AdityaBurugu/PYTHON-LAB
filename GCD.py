def gcd(a,b):
     fa=[]
     for i in range(1,a+1):
          if (a%i)==0:
              fa.append(i)
     fb=[]
     for j in range(1,b+1):
          if (b%j)==0:
              fb.append(j)
     cf=[]
     for f in fa:
          if f in fb:
              cf.append(f)
     return(cf[-1])