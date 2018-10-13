import linecache

#using this top commands "top  -n1 | awk -vtime="$(date +%m-%d-%Y-%T)" 'NR<7{print;next}NR==7{printf("Time\t\t\t\t%s\n",$0)}NR>8{printf("%s\t%s\n",time,$0)}' >>/mnt/sda1/top.log"
#bash on the router

#check string if he matches to list and return ok
def ch(t):
    list = ['10%idle', '9%idle', '8%idle', '7%idle', '6%idle', '5%idle', '4%idle', '3%idle', '2%idle', '1%idle',
            '0%idle']
    for i in list:
        # print (t)
        if t == i:
            t = 'ok'
            pass
    return t
#print the idle + 15 line after + space
def lineprint(h):
    file2.write('\n')
    file2.write(keep)
    for n in range(1,16):
        y = h+n
        x3 = linecache.getline(r"C:\tmp\top.log", y)
        #print (keep)
        #print (x3)
        file2.write(x3)


#output file
file2 = open('testfile5.txt','w')
#read top file
file = open(r"C:\tmp\top.log", 'r')
count = 0
#read line by line (not load full file)
for line in file:
    #count line
    count += 1
    keep = line
    #remove space on specific location
    x = (line[33:42].replace(" ", ""))
    mo = (ch(x))
    if mo == 'ok':
       print (count ,mo,x)
       lineprint(count)
       pass

file2.close()