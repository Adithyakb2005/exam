for i in range(1,5):
    for j in range(1,i+1):
        print(chr(64+j),end='\t')
    for j in range(-1,0,-1):
        print(chr(64+j),end='\t')
    print()