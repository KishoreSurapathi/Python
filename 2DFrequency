inputarr=[10,0,3,4,5,3,5,6,7,5,3,5,2,5,3,2,1,10,14,16,22,11,13,9,3,0]
mainlst=[]
len1=len(inputarr)
flag = 1
j=1
lastelem=0

while(flag == 1):
    flag = 0
    for i in range(len1-1):
        if(inputarr[i] > inputarr[i+1]):
            temp = inputarr[i+1]
            inputarr[i+1] = inputarr[i]
            inputarr[i] = temp
            flag = 1
print(inputarr)

for i in range(len1-1):
    if(inputarr[i] == inputarr[i+1]):
        j = j+1
        lastelem=0
    else:
        lst=[inputarr[i],j]
        j = 1
        lastelem=1
        mainlst.append(lst)

if(lastelem==1):
    lst=[inputarr[len1-1],1]
    mainlst.append(lst)
print(mainlst)

flag = 1
len2=len(mainlst)
while(flag == 1):
    flag = 0
    for i in range(len2-1):
        if mainlst[i+1][1] > mainlst[i][1]:
            temp = mainlst[i+1]
            mainlst[i + 1] = mainlst[i]
            mainlst[i] = temp
            flag = 1
        elif mainlst[i+1][1] == mainlst[i][1]:
            if mainlst[i][0] > mainlst[i+1][0]:
                temp = mainlst[i]
                mainlst[i] = mainlst[i+1]
                mainlst[i+1] = temp
                flag = 1
print(mainlst)
