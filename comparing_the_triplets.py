# Func to find Triplets
def compareTriplets(a, b):
    c=0
    d=0
    for i in range (len(a)):
        if(a[i]>b[i]):      #Triplet condition
            c+=1
        elif(a[i]<b[i]):
            d+=1        
    print(c,d)
	
# To get Lists from the user
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
