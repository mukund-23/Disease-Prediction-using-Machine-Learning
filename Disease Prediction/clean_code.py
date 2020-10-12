from tkinter import *
import numpy as np
import pandas as pd
import sqlite3
import random
import string
from tkinter import messagebox as mb
# from gui_stuff import *


# ------------------------------------------------------------------------------------------------------

l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']
OPTIONS = sorted(l1)

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

l2=[]
for x in range(0,len(l1)):
    l2.append(0)

# TESTING DATA df -------------------------------------------------------------------------------------
df=pd.read_csv("Training.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

# print(df.head())

X= df[l1]

y = df[["prognosis"]]
np.ravel(y)
# print(y)

# TRAINING DATA tr --------------------------------------------------------------------------------
tr=pd.read_csv("Testing.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)

user_ID = ''

def DecisionTree():
    from sklearn import tree

    clf3 = tree.DecisionTreeClassifier()   # empty model of the decision tree
    clf3 = clf3.fit(X,y)

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=clf3.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        # print (k,)
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf3.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break
            

    if (h=='yes'):
        t1.delete("1.0", END)
        t1.insert(END, disease[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")
    


def randomforest():
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit(X,np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=clf4.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t2.delete("1.0", END)
        t2.insert(END, disease[a])
    else:
        t2.delete("1.0", END)
        t2.insert(END, "Not Found")


def NaiveBayes():
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb=gnb.fit(X,np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")

var=0
# gui_stuff------------------------------------------------------------------------------------
def NewPatient():
    global var
    var=1
    wl.destroy()
    btn1.destroy()
    btn2.destroy()
    fm.destroy()
    
def Patient():
    conn = sqlite3.connect('project.db')
    cursorObject = conn.cursor()
    global user_ID
    user_ID = user_entry.get()
    uPass = password_entry.get()
    user_ID = user_ID.strip()
    try:
        cursorObject.execute('''select * from credential where userID=?;''',(user_ID))
        cred_data = cursorObject.fetchall()[0]
    except:
        cred_data = None
        mb.showerror('Credentials','Wrong Credentials')
        
    global var
    if cred_data != None and uPass == cred_data[1]:
        var=2
        wl.destroy()
        btn1.destroy()
        btn2.destroy()
        fm.destroy()
    else:
        mb.showerror('Credentials','Wrong Credentials')
    
def Save():
    
    conn = sqlite3.connect('project.db')
    cursorObject = conn.cursor()
    pName = NameEn.get()
    #print(pName)
    cursorObject.execute('''select max(PID)from patient''')
    PID = cursorObject.fetchone()[0]
    if PID == None:
        PID=1
    else:
        PID+=1
    #print(PID)
    Sym1 = Symptom1.get()
    Sym2 = Symptom2.get()
    Sym3 = Symptom3.get()
    Sym4 = Symptom4.get()
    Sym5 = Symptom5.get()
    DT=t1.get("1.0", END)
    RF=t2.get("1.0",END)
    NB=t3.get("1.0",END)
    
    
    conn.execute("INSERT INTO Patient(PID, Name)VALUES(?,?);",(PID, pName))
    conn.execute("INSERT INTO PatientSymptom(PID,symptom1,symptom2,symptom3,symptom4,symptom5)VALUES(?,?,?,?,?,?);",(PID,Sym1,Sym2,Sym3,Sym4,Sym5))#,decisiontree,randomforest,naivebayes,ActualDisease)VALUES(?,?,?,?,?,?,?,?,?,?,?);",(PID,pName,Sym1,Sym2,Sym3,Sym4,Sym5,DT,RF,NB,"N/A"))
    conn.execute("INSERT INTO Prediction(PID,decisiontree,randomforest,naivebayes)VALUES(?,?,?,?);",(PID,DT,RF,NB))
    conn.execute("INSERT INTO ActualDisease(PID,Actualdisease)VALUES(?,?);",(PID,"NA"))
    lettersAndDigits = string.ascii_letters + string.digits
    passw = ''.join((random.choice(lettersAndDigits) for i in range(8)))
    conn.execute("INSERT INTO credential(userID,password,designation)VALUES(?,?,?);",(PID,passw,'Patient'))
    conn.commit()
    conn.close()
    mb.showinfo("Patient ID & Password","Your PatientId is %d \n password is '%s'" %(PID,passw))
    
def AllPatient():
    conn = sqlite3.connect('project.db')
    cursorObject = conn.cursor()
    uID = user_entry.get()
    uPass = password_entry.get()
    uID = uID.strip()
    try:
        print(uID)
        cursorObject.execute('''select * from credential where userID=?''',(uID, ))
        cred_data = cursorObject.fetchall()[0]
        print(cred_data)
        if cred_data != None and uPass == cred_data[1] and cred_data[2] == "Doctor":    
            global var
            var=3
            fm.destroy()
        elif cred_data[2] != 'Doctor':
            mb.showerror("Authentication Error","You are not authorised")
    except:
        cred_data = None
        mb.showerror('Credentials','Wrong Credentials')
    
    conn.close()
    
def PatientDetails():
    search = tpid.get()
    print(search)
    if str(search).isnumeric()!= True :
        mb.showerror("Invalid PID", "PID contains only numeric value")
    else:
        conn = sqlite3.connect('project.db')
        cursorObject = conn.cursor()
        cursorObject.execute("select * from patient where PID=?;",(search))
        d = cursorObject.fetchone()
        print(d)
        if d == None:
            mb.showinfo("Unavailable", "Entered Patient Id is not present")
        else:
            pidl.destroy()
            tpid.destroy()
            pdet.destroy()
            
            fname = "PatientDetails.png"
            logo_image = PhotoImage(file=fname)
            # get the width and height of the image
            w = logo_image.width()
            h = logo_image.height()
            #f.geometry("%dx%d+50+30" % (w, h))
            # size the window so the image will fill it 
            #root.geometry("%dx%d+50+30" % (w, h))
            detl = Canvas(root,width=w, height=h,bg="#390697")
            detl.place(x=500,y=100)
            detl.create_image(2,2, image=logo_image, anchor='nw')
            
            
            detail00 = Label(detl,text="Patient Id")
            detail00.grid(row=0,column=0,padx=5,pady=5)
            detail01 = Label(detl)
            detail01.grid(row=0, column=1,padx=5,pady=5)
            detail01.configure(text=str(search))
            
            d=list(d)
            detail10 = Label(detl,text="Patient Name")
            detail10.grid(row=1,column=0,padx=5,pady=5)
            detail11 = Label(detl)
            detail11.grid(row=1, column=1,padx=5,pady=5)
            detail11.configure(text=d[1])
            
            detail20 = Label(detl,text="Symptom1")
            detail20.grid(row=2,column=0,padx=5,pady=5)
            detail21 = Label(detl)
            detail21.grid(row=2, column=1,padx=5,pady=5)
            detail21.configure(text=d[2])
            
            detail30 = Label(detl,text="Symptom2")
            detail30.grid(row=3,column=0,padx=5,pady=5)
            detail31 = Label(detl)
            detail31.grid(row=3, column=1,padx=5,pady=5)
            detail31.configure(text=d[3])
            
            detail40 = Label(detl,text="Symptom3")
            detail40.grid(row=4,column=0,padx=5,pady=5)
            detail41 = Label(detl)
            detail41.grid(row=4, column=1,padx=5,pady=5)
            detail41.configure(text=d[4])
            
            detail50 = Label(detl,text="Symptom4")
            detail50.grid(row=5,column=0,padx=5,pady=5)
            detail51 = Label(detl)
            detail51.grid(row=5, column=1,padx=5,pady=5)
            detail51.configure(text=d[5])
            
            detail60 = Label(detl,text="Symptom5")
            detail60.grid(row=6,column=0,padx=5,pady=5)
            detail61 = Label(detl)
            detail61.grid(row=6, column=1,padx=5,pady=5)
            detail61.configure(text=d[6])
            
            detail70 = Label(detl,text="Decision Tree")
            detail70.grid(row=7,column=0,padx=5,pady=5)
            detail71 = Label(detl)
            detail71.grid(row=7, column=1,padx=5,pady=5)
            detail71.configure(text=d[7][0:-2])
            
            detail80 = Label(detl,text="Random Forest")
            detail80.grid(row=8,column=0,padx=5,pady=5)
            detail81 = Label(detl)
            detail81.grid(row=8, column=1,padx=5,pady=5)
            detail81.configure(text=d[8][0:-2])
            
            detail90 = Label(detl,text="Naive Bayes")
            detail90.grid(row=9,column=0,padx=5,pady=5)
            detail91 = Label(detl)
            detail91.grid(row=9, column=1,padx=5,pady=5)
            detail91.configure(text=d[9][0:-2])
            
    
    
    
                 
fm = Tk()
fm.configure(background='sky blue')
fm.title("Prediction System")

wid = fm.winfo_screenwidth()

    
# pick a .gif image file you have in the working directory
#fname = "bg1.png"
fname = "allPatient.png"
bg_image = PhotoImage(file=fname)
# get the width and height of the image
w = bg_image.width()
h = bg_image.height()

hei=h
fm.geometry("%dx%d+50+30" % (w, h))
# size the window so the image will fill it
#root.geometry("%dx%d+50+30" % (w, h))
root = Canvas(fm,width=w, height=h)
root.place(x=0,y=0)
root.create_image(0, 0, image=bg_image, anchor='nw')
    
wl = Label(root, text="Disease Prediction using Machine Learning", bg="#aa33ff", fg="white")
wl.config(font=("Elephant", 30),anchor=CENTER)
wl.place(x= ("%d")%((wid/2)-300),y=10)


b_pos=(wid/4)-30

user_label = Label(root,text="User Id")
user_label.place(x=(2*b_pos)-100,y=(hei/3))

user_entry = Entry(root)
user_entry.place(x=(2*b_pos)+50,y=(hei/3))

password_label = Label(root,text="Password")
password_label.place(x=(2*b_pos)-100,y=(hei/3)+50)

password_entry = Entry(root,show='*')
password_entry.place(x=(2*b_pos)+50,y=(hei/3)+50)

btn1 = Button(root, text="New Patient",command=NewPatient,bg="#aaff00")
btn1.place(x=b_pos, y = (hei/2))
        
btn2 = Button(root, text="Existing Patient",command=Patient,bg="#aaff00")
btn2.place(x=(2*b_pos), y = (hei/2))

btn2 = Button(root, text="Patient Details",command=AllPatient,bg="#aaff00")
btn2.place(x=(3*b_pos), y = (hei/2))

fm.mainloop()

f = Tk()
f.configure(background='sky blue')


if var==1:
    f.title("New Patient")
    fname = "bg1.png"
    bg_image = PhotoImage(file=fname)
    # get the width and height of the image
    w = bg_image.width()
    h = bg_image.height()
    f.geometry("%dx%d+50+30" % (w+150, h))
    # size the window so the image will fill it 
    #root.geometry("%dx%d+50+30" % (w, h))
    root = Canvas(f,width=w+50, height=h+30)
    root.place(x=100,y=20)
    root.create_image(0, 0, image=bg_image, anchor='nw')
    # Heading
    w2 = Label(root, justify=LEFT, text="Disease Prediction using Machine Learning", fg="white", bg="sky blue")
    w2.config(font=("Elephant", 30))
    w2.grid(row=0,column=1,columnspan=2,pady=5 )
    
    fname = "RedCross.png"
    logo_image = PhotoImage(file=fname)
    # get the width and height of the image
    w = logo_image.width()
    h = logo_image.height()
    #f.geometry("%dx%d+50+30" % (w, h))
    # size the window so the image will fill it 
    #root.geometry("%dx%d+50+30" % (w, h))
    logo = Canvas(root,width=w, height=h)
    logo.grid(row=1,column=1,sticky='ne',pady=10)#place(x=2,y=2)
    logo.create_image(0,0, image=logo_image, anchor='nw')
        

    # labels 
    NameLb = Label(root, text="Name of the Patient", fg="yellow", bg="black")
    NameLb.grid(row=6, column=1, pady=15)#, sticky=E)
    
    
    S1Lb = Label(root, text="Symptom 1", fg="yellow", bg="black")
    S1Lb.grid(row=7, column=1, pady=10)#, sticky=E)
        
    S2Lb = Label(root, text="Symptom 2", fg="yellow", bg="black")    
    S2Lb.grid(row=8, column=1, pady=10)#, sticky=E)
    
    S3Lb = Label(root, text="Symptom 3", fg="yellow", bg="black")
    S3Lb.grid(row=9, column=1, pady=10)#, sticky=E)
    
    S4Lb = Label(root, text="Symptom 4", fg="yellow", bg="black")
    S4Lb.grid(row=10, column=1, pady=10)#, sticky=E)
    
    S5Lb = Label(root, text="Symptom 5", fg="yellow", bg="black")
    S5Lb.grid(row=11, column=1, pady=10)#, sticky=E)
    
    #entry variables
    Symptom1 = StringVar(root)
    Symptom1.set(None)
    Symptom2 = StringVar(root)
    Symptom2.set(None)
    Symptom3 = StringVar(root)
    Symptom3.set(None)
    Symptom4 = StringVar(root)
    Symptom4.set(None)
    Symptom5 = StringVar(root)
    Symptom5.set(None)
    Name = StringVar(root)
        
    # entries
    OPTIONS = sorted(l1)
    NameEn = Entry(root, textvariable=Name,width=30)
    NameEn.grid(row=6, column=2, sticky=W,columnspan=2)
    
    S1En = OptionMenu(root, Symptom1,*OPTIONS)
    S1En.grid(row=7, column=2, sticky=W,columnspan=2)
    
    S2En = OptionMenu(root, Symptom2,*OPTIONS)
    S2En.grid(row=8, column=2, sticky=W,columnspan=2)
    
    S3En = OptionMenu(root, Symptom3,*OPTIONS)
    S3En.grid(row=9, column=2, sticky=W,columnspan=2)
    
    S4En = OptionMenu(root, Symptom4,*OPTIONS)
    S4En.grid(row=10, column=2, sticky=W,columnspan=2)
    
    S5En = OptionMenu(root, Symptom5,*OPTIONS)
    S5En.grid(row=11, column=2, sticky=W,columnspan=2)
        
    
    
    
    dst = Button(root, text="DecisionTree", command=DecisionTree,bg="#0000ff",fg="#0000ff")
    dst.grid(row=12, column=0,padx=10,pady=50)
    
    rnf = Button(root, text="Randomforest", command=randomforest,bg="#0000ff",fg="#0000ff")
    rnf.grid(row=12, column=1,padx=10,columnspan=2)
    
    lr = Button(root, text="NaiveBayes", command=NaiveBayes,bg="#0000ff",fg="#0000ff")
    lr.grid(row=12, column=3,padx=10)
    
    #textfileds
    t1 = Text(root, height=1, width=40,fg="black")
    t1.grid(row=13, column=0, padx=5,pady=5)
    
    t2 = Text(root, height=1, width=40,fg="black")
    t2.grid(row=13, column=1 , padx=5,columnspan=2)
    
    t3 = Text(root, height=1, width=40,fg="black")
    t3.grid(row=13, column=3 , padx=5)
    
    saveButton = Button(root, text= "Save",command=Save)
    saveButton.grid(row=14,column=1,columnspan=2)
    
    f.mainloop()
    

elif var==2:
    f.title("Patient Details")
    # pick a .gif image file you have in the working directory
    fname = "bg1.png"
    bg_image = PhotoImage(file=fname)
    # get the width and height of the image
    w = bg_image.width()
    h = bg_image.height()
    f.geometry("%dx%d+50+30" % (w, h))
    
    # size the window so the image will fill it
    #root.geometry("%dx%d+50+30" % (w, h))
    root = Canvas(f,width=w, height=h)
    root.place(x=0,y=0)
    root.create_image(0, 0, image=bg_image, anchor='nw')
    
    wl = Label(root, text="Disease Prediction using Machine Learning", bg="#aa33ff", fg="white")
    wl.config(font=("Elephant", 30))
    wl.place(x= 350,y=10)
    
    fname = "PatientDetails.png"
    logo_image = PhotoImage(file=fname)
    # get the width and height of the image
    w1 = logo_image.width()
    h1 = logo_image.height()
    
    detl = Canvas(root,width=w1, height=h1,bg="#390697")
    detl.place(x=500,y=200)
    detl.create_image(2,2, image=logo_image, anchor='nw')
    
    conn = sqlite3.connect('project.db')
    cursorObject = conn.cursor()
    cursorObject.execute("select * from patient Natural Join PatientSymptom Natural Join Prediction where PID = ?",(user_ID, ))
    d = cursorObject.fetchone()
    
            
    detail00 = Label(detl,text="Patient Id")
    detail00.grid(row=0,column=0,padx=5,pady=5)
    detail01 = Label(detl)
    detail01.grid(row=0, column=1,padx=5,pady=5)
    detail01.configure(text=d[0])
            
    d=list(d)
    detail10 = Label(detl,text="Patient Name")
    detail10.grid(row=1,column=0,padx=5,pady=5)
    detail11 = Label(detl)
    detail11.grid(row=1, column=1,padx=5,pady=5)
    detail11.configure(text=d[1])
            
    detail20 = Label(detl,text="Symptom1")
    detail20.grid(row=2,column=0,padx=5,pady=5)
    detail21 = Label(detl)
    detail21.grid(row=2, column=1,padx=5,pady=5)        
    detail21.configure(text=d[2])
            
    detail30 = Label(detl,text="Symptom2")
    detail30.grid(row=3,column=0,padx=5,pady=5)
    detail31 = Label(detl)
    detail31.grid(row=3, column=1,padx=5,pady=5)
    detail31.configure(text=d[3])
    
    detail40 = Label(detl,text="Symptom3")
    detail40.grid(row=4,column=0,padx=5,pady=5)
    detail41 = Label(detl)
    detail41.grid(row=4, column=1,padx=5,pady=5)
    detail41.configure(text=d[4])
    
    detail50 = Label(detl,text="Symptom4")
    detail50.grid(row=5,column=0,padx=5,pady=5)
    detail51 = Label(detl)
    detail51.grid(row=5, column=1,padx=5,pady=5)
    detail51.configure(text=d[5])
    
    detail60 = Label(detl,text="Symptom5")
    detail60.grid(row=6,column=0,padx=5,pady=5)
    detail61 = Label(detl)
    detail61.grid(row=6, column=1,padx=5,pady=5)
    detail61.configure(text=d[6])
    
    detail70 = Label(detl,text="Decision Tree")
    detail70.grid(row=7,column=0,padx=5,pady=5)
    detail71 = Label(detl)
    detail71.grid(row=7, column=1,padx=5,pady=5)
    detail71.configure(text=d[7][0:-2])
    
    detail80 = Label(detl,text="Random Forest")
    detail80.grid(row=8,column=0,padx=5,pady=5)
    detail81 = Label(detl)
    detail81.grid(row=8, column=1,padx=5,pady=5)
    detail81.configure(text=d[8][0:-2])
    
    detail90 = Label(detl,text="Naive Bayes")
    detail90.grid(row=9,column=0,padx=5,pady=5)
    detail91 = Label(detl)
    detail91.grid(row=9, column=1,padx=5,pady=5)
    detail91.configure(text=d[9][0:-2])
    
    conn.close()
    f.mainloop()
    
elif var==3:
    f.title("All Patient Details")
    # pick a .gif image file you have in the working directory
    fname = "allPatient.png"
    bg_image = PhotoImage(file=fname)
    # get the width and height of the image
    w = bg_image.width()
    h = bg_image.height()
    f.geometry("%dx%d+50+30" % (w, h))
    
    root = Canvas(f,width=w, height=w)
    root.place(x=0,y=0)
    root.create_image(0, 0, image=bg_image, anchor='nw')
    
    w1 = Label(root, justify=LEFT, text="Disease Prediction using Machine Learning", fg="white", bg="sky blue")
    w1.config(font=("Elephant", 30))
    w1.grid(row=0,column=1,columnspan=9,pady=5 )
    
    lb1 = Label(root, text= "Patient Id", fg="white", bg="#390697")
    lb1.grid(row=1,column=0,padx=5,pady=5)
    
    lb2 = Label(root, text= "Patient Name", fg="white", bg="#390697")
    lb2.grid(row=1,column=1,padx=5,pady=5)
    
    lb3 = Label(root, text= "Symptom_1", fg="white", bg="#390697")
    lb3.grid(row=1,column=2,padx=5,pady=5)
    
    lb4 = Label(root, text= "Symptom_2", fg="white", bg="#390697")
    lb4.grid(row=1,column=3,padx=5,pady=5)
    
    lb5 = Label(root, text= "Symptom_3", fg="white", bg="#390697")
    lb5.grid(row=1,column=4,padx=5,pady=5)
    
    lb6 = Label(root, text= "Symptom_4", fg="white", bg="#390697")
    lb6.grid(row=1,column=5,padx=5,pady=5)
    
    lb7 = Label(root, text= "Symptom_5", fg="white", bg="#390697")
    lb7.grid(row=1,column=6,padx=5,pady=5)
    
    lb8 = Label(root, text= "DecisionTree", fg="white", bg="#390697")
    lb8.grid(row=1,column=7,padx=5,pady=5)
    
    lb9 = Label(root, text= "RandomForest", fg="white", bg="#390697")
    lb9.grid(row=1,column=8,padx=5,pady=5)
    
    lb10 = Label(root, text= "NaiveBayes", fg="white", bg="#390697")
    lb10.grid(row=1,column=9,padx=5,pady=5)
    
    lb11 = Label(root, text= "Actual Disease", fg="white", bg="#390697")
    lb11.grid(row=1,column=10,padx=5,pady=5)
    
    conn = sqlite3.connect('project.db')
    cursorObject = conn.cursor()
    cursorObject.execute('''select * from patient Natural Join PatientSymptom Natural Join Prediction Natural Join ActualDisease order by PID''')
    PDet = cursorObject.fetchall()
    
    
    cursorObject.execute('''select count(PID)from patient''')
    maxP = cursorObject.fetchone()[0]
    
    
    PDet = list(PDet)
    
    list(PDet[0])
    
    for i in  range(2,maxP+2):
        
        m=list(PDet[i-2])
        print(i)
        
        lb1 = Label(root, fg="white", bg="#390697")
        lb1.grid(row=i,column=0,padx=5,pady=5)
        lb1.configure(text=m[0])
    
        lb2 = Label(root, fg="white", bg="#390697")
        lb2.grid(row=i,column=1,padx=5,pady=5)
        lb2.configure(text=m[1])
    
        lb3 = Label(root, fg="white", bg="#390697")
        lb3.grid(row=i,column=2,padx=5,pady=5)
        lb3.configure(text=m[2])
        
        lb4 = Label(root, fg="white", bg="#390697")
        lb4.grid(row=i,column=3,padx=5,pady=5)
        lb4.configure(text=m[3])
        
        lb5 = Label(root, fg="white", bg="#390697")
        lb5.grid(row=i,column=4,padx=5,pady=5)
        lb5.configure(text=m[4])
        
        lb6 = Label(root, fg="white", bg="#390697")
        lb6.grid(row=i,column=5,padx=5,pady=5)
        lb6.configure(text=m[5])
        
        lb7 = Label(root, fg="white", bg="#390697")
        lb7.grid(row=i,column=6,padx=5,pady=5)
        lb7.configure(text=m[6])
        
        lb8 = Label(root, fg="white", bg="#390697")
        lb8.grid(row=i,column=7,padx=5,pady=5)
        lb8.configure(text=m[7][0:-2])
        
        lb9 = Label(root, fg="white", bg="#390697")
        lb9.grid(row=i,column=8,padx=5,pady=5)
        lb9.configure(text=m[8][0:-2])
        
        lb10 = Label(root, fg="white", bg="#390697")
        lb10.grid(row=i,column=9,padx=5,pady=5)
        lb10.configure(text=m[9][0:-2])
        
        lb11 = Label(root, fg="white", bg="#390697")
        lb11.grid(row=i,column=10,padx=5,pady=5)
        lb11.configure(text=m[10])
        
        
    f.mainloop()
    