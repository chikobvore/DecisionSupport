import pandas as pd 
from numpy.random import randint
A1 = []
B1 = []
C1 = []
D1 = []
F1 = []
Total = []
Comment = []
for i in range(2000):
    A = randint(0,100)
    B = randint(0,100)
    C = randint(0,100)
    D = randint(0,100)
    F = randint(0,100)
    total = A + B + C + D + F
    A = round((A/total)*100)
    B = round((B/total)*100)
    C = round((C/total)*100)
    D = round((D/total)*100)
    F = round((F/total)*100)

    total = A + B + C + D + F


    Total.append(total)

    if F > 30:

        if D > 20:
            comment = "Low Grade Anomally"
            Comment.append(comment)
        else:
            x = D + F
            if x > 40:
                comment = "High Failure rate"
                Comment.append(comment)
            else:
                if A > 70:
                    comment = "TOO GOOD GRADES"
                    Comment.append(comment)
                else:
                    if A > 50:
                        A = 100
                        B = 0
                        C = 0
                        D = 0
                        F = 0
                    if B > 50:
                        B = 100
                        A = 0
                        C = 0
                        D = 0
                        F = 0
                    if C > 50:
                        C = 100
                        B = 0
                        A = 0
                        D = 0
                        F = 0
                    if D > 50:
                        D = 100
                        B = 0
                        C = 0
                        A = 0
                        F = 0
                    if F > 50:
                        F = 100
                        B = 0
                        C = 0
                        D = 0
                        A = 0
                    print(A)

                    if A ==100 or B == 100 or C == 100 or D == 100 or F == 100:
                        comment = "SAME GRADE"
                        Comment.append(comment)
                    else:
                        comment = "Fair Enough"
                        Comment.append(comment)
    else:
        if A > 30 and B > 20:
            comment = "TOO GOOD GRADES"
            Comment.append(comment)
        else:
            if A > 30 and B > 20 and C >10:
                comment = "TOO HIGH PASSRATE"
                Comment.append(comment)
            else:
                if A > 70:
                    comment = "TOO GOOD GRADES"
                    Comment.append(comment)
                else:
                    if A > 50:
                        A = 100
                        B = 0
                        C = 0
                        D = 0
                        F = 0
                    if B > 50:
                        B = 100
                        A = 0
                        C = 0
                        D = 0
                        F = 0
                    if C > 50:
                        C = 100
                        B = 0
                        A = 0
                        D = 0
                        F = 0
                    if D > 50:
                        D = 100
                        B = 0
                        C = 0
                        A = 0
                        F = 0
                    if F > 50:
                        F = 100
                        B = 0
                        C = 0
                        D = 0
                        A = 0
                    print(A)

                    if A ==100 or B == 100 or C == 100 or D == 100 or F == 100:
                        comment = "SAME GRADE"
                        Comment.append(comment)
                    else:
                        comment = "Fair Enough"
                        Comment.append(comment)
        
    A1.append(A)
    B1.append(B)
    C1.append(C)
    D1.append(D)
    F1.append(F)
 





newdata = {
    "1":A1,
    "2.1":B1,
    "2.2":C1,
    "P":D1,
    "F":F1,
    "Total": Total,
    "Remarks": Comment
}

Dataset = pd.DataFrame(newdata,columns= ['1','2.1','2.2','P','F','Total','Remarks'])
Export = Dataset.to_csv('D2.csv',index=None,header=True)