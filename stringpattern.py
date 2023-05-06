def pattern(string, list=[]):
    """
    function to store each letter in pattern * into list
    """
    for i in range(len(string)):
        """
        for loop for running the loop for each char in a string
        """
        if(string[i]=="A"):
            A = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (col in [0,4] and row!=0) or (row in [0,2] and col in [1,2,3]):
                        A[row][col]="*"
            list.append(A)

        elif(string[i]=="B"):
            B = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (col in [0,4] and row not in [0,2,4]) or (row in [0,2,4] and col!=4):
                        B[row][col]="*"
            list.append(B)
        
        elif(string[i]=="C"):
            C = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (col == 0 and row not in [0,4])or(row in [0,4] and col != 0):
                        C[row][col]="*"
            list.append(C)

        elif(string[i]=="D"):
            D = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (col==0)or(row in [0,4] and col!=4)or(col==4 and row not in [0,4]):
                        D[row][col]="*"
            list.append(D)

        elif(string[i]=="E"):
            E = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (row in [0,2,4] and col!=0) or (col==0 and row not in [0,4]):
                        E[row][col]="*"
            list.append(E)

        elif(string[i]=="F"):
            F = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (col==0 or row in [0,2]):
                        F[row][col]="*"
            list.append(F)

        elif(string[i]=="G"):
            G = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (col==0 and row not in [0,4]) or (row in [0,4] and col!=0) or (col>1 and row==2) or (row>1 and col==4):
                        G[row][col]="*"
            list.append(G)

        elif(string[i]=="H"):
            H = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (col in [0,4]) or (row==2):
                        H[row][col]="*"
            list.append(H)

        elif(string[i]=="I"):
            I = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (row in [0,4]) or (col==2):
                        I[row][col]="*"
            list.append(I)

        elif(string[i]=="J"):
            J = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (row==0)or(col==2)or(row>2 and col==0)or(row==4 and col==1):
                        J[row][col]="*"
            list.append(J)

        elif(string[i]=="K"):
            K = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (col==0)or(row-col==1)or(row+col==3):
                        K[row][col]="*"
            list.append(K)

        elif(string[i]=="L"):
            L = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (col==0)or(row==4 and col!=4):
                        L[row][col]="*"
            list.append(L)

        elif(string[i]=="M"):
            M = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (col in [0,4])or(row==1 and col in [1,3])or(col==2 and row==2):
                        M[row][col]="*"
            list.append(M)

        elif(string[i]=="N"):
            N = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (col in [0,4])or(col==row):
                        N[row][col]="*"
            list.append(N)

        elif(string[i]=="O"):
            O = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (col in [0,4] and row not in [0,4]) or (row in [0,4] and col not in [0,4]):
                        O[row][col]="*"
            list.append(O)

        elif(string[i]=="P"):
            P = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (col==0)or(row in [0,2] and col!=4)or(col==4 and row==1):
                        P[row][col]="*"
            list.append(P)

        elif(string[i]=="Q"):
            Q = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if(col==0 and row not in [0,4]) or (row==0 and col not in [0,4]) or (col==4 and row in range(1,3)) or (row==4 and col in range(1,3)) or (row==3 and col==3) or (row==4 and col==4):
                        Q[row][col]="*"
            list.append(Q)

        elif(string[i]=="R"):
            R = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (col==0)or(row in [0,2] and col!=4)or(col==4 and row in [1,4])or(row==3 and col==3):
                        R[row][col]="*"
            list.append(R)

        elif(string[i]=="S"):
            S = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (row in [0,2,4]) or(col==0 and row<3)or(col==4 and row>2):
                        S[row][col]="*"
            list.append(S)

        elif(string[i]=="T"):
            T = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (row==0)or(col==2):
                        T[row][col]="*"
            list.append(T)

        elif(string[i]=="U"):
            U = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (col in [0,4] and row!=4)or(row==4 and col not in [0,4]):
                        U[row][col]="*"
            list.append(U)

        elif(string[i]=="V"):
            V = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (col in [0,4] and row<3)or(col in [1,3] and row==3)or(col==2 and row==4):
                        V[row][col]="*"
            list.append(V)

        elif(string[i]=="W"):
            W = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (col in [0,4])or(col in [1,3] and row==3)or(col==2 and row==2):
                        W[row][col]="*"
            list.append(W)

        elif(string[i]=="X"):
            X = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (row==col)or(row+col==4):
                        X[row][col]="*"
            list.append(X)

        elif(string[i]=="Y"):
            Y = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if ((row==col or col+row==4) and row<3)or(col==2 and row>1):
                        Y[row][col]="*"
            list.append(Y)

        elif(string[i]=="Z"):
            Z = [[" "for col in range(5)]for row in range(5)]
            for row in range(5):
                for col in range(5):
                    if (row in [0,4])or(col+row==4):
                        Z[row][col]="*"
            list.append(Z)


        else:
            pass


string = input("Enter a name : ")
string = string.upper()

list=[]

pattern(string,list)


for i in range(5):
    for j in range(len(list)):
        for k in range(5):
            print(list[j][i][k], end=" ")
        print(" ",end=" ")
    print()
