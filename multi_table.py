def mult(num):
    li=[]
    for i in range(num):
        li_num=[]
        for j in range(i+1):
            li_num.append((i+1)*(j+1))
        li.append(li_num)
    return li
print(mult(4))# result=[[1], [2, 4], [3, 6, 9], [4, 8, 12, 16]]
