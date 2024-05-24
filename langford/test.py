def x2y(a, b):
    return x_index[a-1]+b

sum = 0
length=3
list=[]
x_index=[]
for i in range(1, length+1):
    list.append([k for k in range(sum+1, sum+2*length-i)])
    x_index.append(sum)
    sum += 2*length-i-1
    print(f'sum:{sum}')
#    for j in range(1, 2*length-i):
#        print(f'i:{i},j:{j}')
list.append([i+1 for i in x_index]) # s_1
list.append([i+2 for i in x_index]) #s_2
for i in range(3, 2*length+1):
    tekitou=[x2y(j, i-j-1) for j in range(1, i-1) if j <= length]
    tekitou+=[x2y(j, i) for j in range(1, 2*length-i) if i<2*length-1]
#    tekitou=[[j, i-j-1] for j in range(1, i-1) if j <= length] + [[j,i] for j in range(1, 2*length-i) if i<2*length-1]
    list.append(tekitou)

print('end')