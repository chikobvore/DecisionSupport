import pandas as pd
from numpy.random import randint

data = pd.read_csv('mubeena1.csv')
TCW = []
EM = []
TM = []
Grade = []
Comment = []
for i in range(len(data)):
    CW = 0.4 * data.iloc[i][0]
    TEM = 0.6 * data.iloc[i][1]

    if CW > 35:
        CW = 40
        print("New Cw is " + str(CW))

    if TEM > 55:
        TEM = 60

    total = CW +TEM

    if total > 30 and total < 45:
        CW = randint(0,43)
        TEM = 44 - CW
        total = 44

    EM.append(round(TEM))
    TCW.append(round(CW))
    
    TM.append(round(total))

    if total < 45:
        grade = 'F'
        Grade.append(grade)
    elif total > 44 and total < 55:
        grade = 'P'
        Grade.append(grade)
    elif total >54 and total <65:
        grade = '2.2'
        Grade.append(grade)
    elif total >64 and total < 75:
        grade = '2.1'
        Grade.append(grade)
    else:
        grade = '1'
        Grade.append(grade)

    if CW > 12:
        if TEM > 15:
            if total == 44:
                comment = "Borderline Failure"
                Comment.append(comment)
            else:
                if CW > 38:
                    comment = "Perfect Course  Work Score"
                    Comment.append(comment)
                else:
                    if TEM > 58:
                        comment = "Perfect Exam Mark Score"
                        Comment.append(comment)
                    else:
                        comment = "Normal"
                        Comment.append(comment)
        
        else:
            comment = "Disproportinate TCW TO TOTAL Exam Mark"
            Comment.append(comment)
    else:

        if TEM > 32:
            if CW > 9:
                if TEM > 40:
                    comment = "Disproportinate TCW TO TOTAL Exam Mark"
                    Comment.append(comment)
                else:
                    if TEM > 59:
                        comment = "Perfect Exam mark Score"
                        Comment.append(comment)
                    else:
                        if total == 44:
                            comment = "Boarderline Failure"
                            Comment.append(comment)
                        else:
                            if CW > 39:
                                comment = "Perfect Course Work Score"
                                Comment.append(comment)
                            else:
                                comment = "Normal"
                                Comment.append(comment)
            else:
                comment = "Disproportinate TCW TO TOTAL Exam Mark"
                Comment.append(comment)
        else:
            if CW > 39:
                comment = "Perfect Course Work Score"
                Comment.append(comment)
            else:
                if total == 44:
                    comment = "Borderline Failure"
                    Comment.append(comment)
                else:
                    
                    if TEM > 58:
                        comment = "Perfect Exam mark Score"
                        Comment.append(comment)
                    else:
                        comment = "Normal"
                        Comment.append(comment)
for i in range(len(data)):
    CW = 0.4 * data.iloc[i][2]
    TEM = 0.6 * data.iloc[i][3]

    if CW > 35:
        CW = 40
        print("New Cw is " + str(CW))

    if TEM > 55:
        TEM = 60

    total = CW +TEM

    if total > 30 and total < 45:
        CW = randint(0,43)
        TEM = 44 - CW
        total = 44

    EM.append(round(TEM))
    TCW.append(round(CW))
    
    TM.append(round(total))

    if total < 45:
        grade = 'F'
        Grade.append(grade)
    elif total > 44 and total < 55:
        grade = 'P'
        Grade.append(grade)
    elif total >54 and total <65:
        grade = '2.2'
        Grade.append(grade)
    elif total >64 and total < 75:
        grade = '2.1'
        Grade.append(grade)
    else:
        grade = '1'
        Grade.append(grade)

    if CW > 12:
        if TEM > 15:
            if total == 44:
                comment = "Borderline Failure"
                Comment.append(comment)
            else:
                if CW > 38:
                    comment = "Perfect Course  Work Score"
                    Comment.append(comment)
                else:
                    if TEM > 58:
                        comment = "Perfect Exam Mark Score"
                        Comment.append(comment)
                    else:
                        comment = "Normal"
                        Comment.append(comment)
        
        else:
            comment = "Disproportinate TCW TO TOTAL Exam Mark"
            Comment.append(comment)
    else:

        if TEM > 32:
            if CW > 9:
                if TEM > 40:
                    comment = "Disproportinate TCW TO TOTAL Exam Mark"
                    Comment.append(comment)
                else:
                    if TEM > 59:
                        comment = "Perfect Exam mark Score"
                        Comment.append(comment)
                    else:
                        if total == 44:
                            comment = "Boarderline Failure"
                            Comment.append(comment)
                        else:
                            if CW > 39:
                                comment = "Perfect Course Work Score"
                                Comment.append(comment)
                            else:
                                comment = "Normal"
                                Comment.append(comment)
            else:
                comment = "Disproportinate TCW TO TOTAL Exam Mark"
                Comment.append(comment)
        else:
            if CW > 39:
                comment = "Perfect Course Work Score"
                Comment.append(comment)
            else:
                if total == 44:
                    comment = "Borderline Failure"
                    Comment.append(comment)
                else:
                    
                    if TEM > 58:
                        comment = "Perfect Exam mark Score"
                        Comment.append(comment)
                    else:
                        comment = "Normal"
                        Comment.append(comment)

                

NewData = {
        "Course Work": TCW,
        "Exam Mark": EM,
        "Total": TM,
        "Comment": Comment
    }
Dataset = pd.DataFrame(NewData,columns= ['Course Work','Exam Mark','Total','Comment'])
Export = Dataset.to_csv('newdata.csv',index=None,header=True)
