import time

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

def int_mul(x_str,y_str):

    if len(x_str)<2 or len(y_str)<2:
        return int(x_str)*int(y_str)
    else:
        halfx = int(len(x_str)/2)
        halfy = int(len(y_str)/2)
        a = x_str[:halfx]
        b = x_str[halfx:]
        c = y_str[:halfy]
        d = y_str[halfy:]
        x1 = int_mul(a,c)
        x2 = int_mul(b,d)
        len_b = len(b)
        len_d = len(d)
        if len_b == len_d:
            x3 = int_mul(str(int(a)+int(b)),str(int(c)+int(d)))
            x4 = x3 - x2 - x1
            return x1*10**(2*len_b)+x2+x4*10**(len_b)
        else:
            x3 = int_mul(a,d)
            x4 = int_mul(b,c)
            return x1*10**(len_b+len_d)+x2+x3*10**len_b+x4*10**len_d

start = time.clock()
print(int_mul(str(x),str(y)))
elapsed = (time.clock() - start)
print('Time used:'+str(elapsed)+'s')

start = time.clock()
print(x*y)
elapsed = (time.clock() - start)
print('Time used:'+str(elapsed)+'s')
