oper=[]
N=int(input('How many coins do you want to withdraw from ATM? '))
nn=int(N)
#print(N,type(N))

def nine(N):
    for n in range(15):
        if (9**n)<=N and (9**(n+1))>N:
            return 9**n
            '''global A
            A=N-9**n
            #print(A)
            return A'''
        '''else:
            return 0'''
def six(A):
    #print(A,type(A))
    for m in range(20):
        if (6**m)<=A and (6**(m+1))>A:
            return 6**m
nnn=nn
if nn<=100000:
    try:
        while nn<=100000:
            x,y=nine(nn),six(nn)
            #print(x,type(x))
            #print(y,type(y))
            maxxy=max(x,y)
            oper.append(maxxy)
            nn=nn-maxxy
    except:
        print("")
    finally:
        rem=nnn-sum(oper)
        #print(rem)
        #oper.append(rem)
        print('Take out coins in this manner: ',oper)
        nopr=len(oper)+rem
        print('No. of operations you will need to perform to take out %d coins from ATM is: '%nnn,nopr)
elif nn>100000:
    print("Sorry, because of Technical error in ATM machine, you will be able to withdraw cash below 100000 in a day!!")
