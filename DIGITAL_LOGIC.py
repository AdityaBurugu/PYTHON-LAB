def half_adder(a, b):
    s = a ^ b
    c = a * b
    return s, c

def full_adder(a, b, c):
    s = a ^ b ^ c
    co = ((a * b) | (b * c) | (c * a))
    return s, co

def full_adder_using_half_adder(a,b,c):
    sum1 , carry1 = half_adder(a, b)
    sum, carry2 = half_adder(sum1, c)
    carry = carry1 or carry2
    return sum , carry

def Parallel_Adder_Vallidity_Check(a,b):
    if len(a)==len(b):
        for i in range(len(a)):
            if a[i]=="0" or a[i]=="1":
                if b[i]=="0" or b[i]=="1":
                    return True
                return False
            return False
    else:
        return False

def parallel_adder(a, b):
    c=0
    s_arr=[]
    for i in range(1,len(a)+1):
        p = int(a[i-1]) ^ int(b[i-1])
        g = int(a[i-1]) & int(b[i-1])
        s = p ^ c
        s_arr.append(s)
        co = (p & c) | g
        c=co
    return s_arr,co

run = True
while run:
    a = int(input("Enter a value [1-bit Data]:"))
    if (a > 1 or a < 0):
        print("ERROR")
        break
    b = int(input("Enter b value [1-bit Data]:"))
    if (b > 1 or b < 0):
        print("ERROR")
        break
    c = int(input("Enter c value [1-bit Data]:"))
    if (c > 1 or c < 0):
        print("ERROR")
        break
########################################################################
    d = int(input("Enter d value [Integer Data]:"))
    bd = bin(d)[2:]
    bd = bd[::-1]
    e = int(input("Enter e value [Integer Data]:"))
    be = bin(e)[2:]
    be = be[::-1]

    maxl = max(d.bit_length(), e.bit_length())
    minl = min(d.bit_length(), e.bit_length())

    rz = maxl - minl

    if min(d, e) == d:
        bd = bd + "0" * rz
    if min(d, e) == e:
        be = be + "0" * rz

    print("AND", a & b)
    print("OR", a | b)
    print("NOT", int(not(a)))
    print("E-XOR", a ^ b)
    print("Ex-NOR", int(not(a ^ b)))
    print("NAND", int(not(a & b)))
    print("NOR", int(not(a | b)))

    s, co = half_adder(a, b)
    print(f'''Half Adder: Sum:{s} Carry:{co}''')

    s, co = full_adder(a, b, c)
    print(f'''Full Adder: Sum:{s} Carry:{co}''')

    s, co = full_adder_using_half_adder(a, b, c)
    print(f'''Full Adder using Half Adder: Sum:{s} Carry:{co}''')

    if Parallel_Adder_Vallidity_Check(bd, be):
        s, co = parallel_adder(bd, be)
        f = s[::-1].copy()
        f.insert(0, co)
        fs = ''.join(str(x) for x in f)
        print("A:", d, "B:", e, "A+B:", d + e)
        print("Parallel Adder: Carry:", co, "Sum:", *s[::-1], "Final Val:", *fs, "Decimal Equivalent:", int(fs, 2))
    else:
        print("PARALLEL ADDER ERROR")
        break