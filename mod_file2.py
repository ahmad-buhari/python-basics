with open('log.txt','r+') as f:
    
    line1 = int(f.readline())
    line2 = int(f.readline())
    multi = line1 + line2
    #f.write('\n')
    f.write(str(multi))
    #print(multi)
    
