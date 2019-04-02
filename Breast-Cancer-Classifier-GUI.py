import tkinter as tk
from tkinter import ttk
import pypyodbc
import pandas as pd
import pickle
from sklearn import preprocessing,neighbors,svm
from sklearn.model_selection import train_test_split
import numpy as np
from tkinter import messagebox as mbox
from tkintertable.Tables import TableCanvas
from tkintertable.TableModels import TableModel

conn = pypyodbc.connect("Driver={SQL Server Native Client 10.0};"
                        "Server=LAPTOP-77C7OI12;"
                        "Database=Breast Cancer;"
                        "uid=sa;pwd=1234")
root = tk.Tk()
root.title('Breast Cancer Classifier - Database')
root.geometry('1000x600')
'''
def train():

    df = pd.read_sql_query('Select * from [dbo].[breast_cancer_data]',conn)
    df.fillna(0,inplace=True)
    df.drop(['id number'],1,inplace = True)
    X = np.array(df.drop(['class'],1))
    y = np.array(df['class'])
    X_train, X_test,y_train, y_test = train_test_split(X,y,test_size = 0.2)

    clf = svm.SVC(probability=True)
    clf.fit(X_train,y_train)
    with open('bcancer.pickle','wb') as f:
        pickle.dump(clf,f)
'''
def test():
    pickle_in = open('bcancer.pickle','rb')
    clf = pickle.load(pickle_in)   
    i1 = e2.get()
    i2 = e3.get()
    i3 = e4.get()
    i4 = e5.get()
    i5 = e6.get()
    i6 = e7.get()
    i7 = e8.get()
    i8 = e9.get()
    i9 = e10.get()
    test_arr = np.array([[i1,i2,i3,i4,i5,i6,i7,i8,i9]])
    result = clf.predict(test_arr)
    if(str(result[0]) == '4.0'):
        res = str(result[0]) + ' - Malignant' 
    else:
        res = str(result[0]) + ' - Benign'
    conf = clf.predict_proba(test_arr)
    con = max(list(conf[0])) * 100
    mbox.showinfo("Message","Class : "+str(res)+"\nConfidence : "+str(round(con,2))+" %")
    

def insert():
    i0 = e11.get()
    print(i0)
    i1 = e22.get()
    i2 = e33.get()
    i3 = e44.get()
    i4 = e55.get()
    i5 = e66.get()
    i6 = e77.get()
    i7 = e88.get()
    i8 = e99.get()
    i9 = e100.get()
    i10 = e111.get()
    cursor = conn.cursor()
    SQLCommand = ("INSERT INTO [dbo].[breast_cancer_data] VALUES (?,?,?,?,?,?,?,?,?,?,?)")
    values = [i0,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10]
    cursor.execute(SQLCommand,values)
    conn.commit()  
    mbox.showinfo("Message","1 Row Inserted Successfully")
    df = pd.read_sql_query("select id from [dbo].[breast_cancer_data]",con)
    valarr1 = []
    for i in df['id'].values:
        valarr1.append(i)
    eb12.config(values = valarr1)

    
def delete():
    i1 = e12.get()
    cur = conn.cursor()
    cur.execute("delete from [dbo].[breast_cancer_data] where id = "+str(i1)+";")
    conn.commit()
    cur.close()
    eb12.set(0)
    df = pd.read_sql_query("select id from [dbo].[breast_cancer_data]",conn)
    valarr2 = []
    for i in df['id'].values:
        valarr2.append(i)
    eb12.config(values = valarr2)
    
    mbox.showinfo("Message","1 Row Deleted Successfully")

def view():
    c = e13.get()
    df = pd.read_sql_query("select * from [dbo].[breast_cancer_data] where id = '"+str(c)+"';",conn)
    print(df.columns)
    ct = df['clump thickness']
    csize =df['uniformity of cell size']
    csh =df['uniformity of cell shape']
    ma =df['marginal adhesion']
    secs =df['single epithelial cell size']
    bn = df['bare nuclei  ']
    bc = df['bland chromatin']
    nn = df['normal nucleoli']
    m = df['mitoses ']
    cl = df['class'].values
    x1.config(text=ct[0])
    x2.config(text=csize[0])
    x3.config(text=csh[0])
    x4.config(text=ma[0])
    x5.config(text=secs[0])
    x6.config(text=bn[0])
    x7.config(text=bc[0])
    x8.config(text=nn[0])
    x9.config(text=m[0])
    x10.config(text=cl[0])
    

tabControl = ttk.Notebook(root)          
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Test')
tabControl.add(tab2, text='Insert')
tabControl.add(tab3, text='Delete')
tabControl.add(tab4, text='View')
tabControl.pack(fill="both",expand=1)  


vals = [1,2,3,4,5,6,7,8,9,10]
lt = tk.Label(tab1,text = 'Enter Data to Detect Type',font = ('Helvetica',16) )
l2 = tk.Label(tab1,text = 'Clump Thickness :  ')
l3 = tk.Label(tab1,text = 'Uniformity of Cell Size :  ')
l4 = tk.Label(tab1,text = 'Uniformity of Cell Shape :  ')
l5 = tk.Label(tab1,text = 'Marginal Adhesion :  ')
l6 = tk.Label(tab1,text = 'Single Epithelial Cell Size :  ')
l7 = tk.Label(tab1,text = 'Bare Nuclei :  ')
l8 = tk.Label(tab1,text = 'Bland Chromatin :  ')
l9 = tk.Label(tab1,text = 'Normal Nucleoli :  ')
l10 = tk.Label(tab1,text = 'Mitoses :  ')
#Mitoses
e2 = tk.IntVar()
eb2 = ttk.Combobox(tab1,textvariable = e2,values=vals)
e3 = tk.IntVar()
eb3 = ttk.Combobox(tab1,textvariable = e3,values=vals)
e4 = tk.IntVar()
eb4 = ttk.Combobox(tab1,textvariable = e4,values=vals)
e5 = tk.IntVar()
eb5 = ttk.Combobox(tab1,textvariable = e5,values=vals)
e6 = tk.IntVar()
eb6 = ttk.Combobox(tab1,textvariable = e6,values=vals)
e7 = tk.IntVar()
eb7 = ttk.Combobox(tab1,textvariable = e7,values=vals)
e8 = tk.IntVar()
eb8 = ttk.Combobox(tab1,textvariable = e8,values=vals)
e9 = tk.IntVar()
eb9 = ttk.Combobox(tab1,textvariable = e9,values=vals)
e10 = tk.IntVar()
eb10 = ttk.Combobox(tab1,textvariable = e10,values=vals)

b1 = tk.Button(tab1,text = 'Test',width='18',bg='gray',fg='white',relief='flat',command = test)

lt.grid(row = 0,column = 0,padx = 8,pady = 8)


l2.grid(row = 1,column = 0,padx=15,pady = 8,sticky='w')
l3.grid(row = 2,column = 0,padx=15,pady = 8,sticky='w')
l4.grid(row = 3,column = 0,padx=15,pady = 8,sticky='w')
l5.grid(row = 4,column = 0,padx=15,pady = 8,sticky='w')
l6.grid(row = 5,column = 0,padx=15,pady = 8,sticky='w')
l7.grid(row = 6,column = 0,padx=15,pady = 8,sticky='w')
l8.grid(row = 7,column = 0,padx=15,pady = 8,sticky='w')
l9.grid(row = 8,column = 0,padx=15,pady = 8,sticky='w')
l10.grid(row = 9,column = 0,padx=15,pady = 8,sticky='w')

eb2.grid(row = 1,column = 1,padx=8,pady = 8)
eb3.grid(row = 2,column = 1,padx=8,pady = 8)
eb4.grid(row = 3,column = 1,padx=8,pady = 8)
eb5.grid(row = 4,column = 1,padx=8,pady = 8)
eb6.grid(row = 5,column = 1,padx=8,pady = 8)
eb7.grid(row = 6,column = 1,padx=8,pady = 8)
eb8.grid(row = 7,column = 1,padx=8,pady = 8)
eb9.grid(row = 8,column = 1,padx=8,pady = 8)
eb10.grid(row = 9,column = 1,padx=8,pady = 8)

b1.grid(row = 10,column = 1,padx=8,pady = 8)


#####tab2#####

lt1 = tk.Label(tab2,text = 'Enter Data to Insert in Database ',font = ('Helvetica',16) )
l11 = tk.Label(tab2,text = 'ID Number :  ')
l22 = tk.Label(tab2,text = 'Clump Thickness :  ')
l33 = tk.Label(tab2,text = 'Uniformity of Cell Size :  ')
l44 = tk.Label(tab2,text = 'Uniformity of Cell Shape :  ')
l55 = tk.Label(tab2,text = 'Marginal Adhesion :  ')
l66 = tk.Label(tab2,text = 'Single Epithelial Cell Size :  ')
l77 = tk.Label(tab2,text = 'Bare Nuclei :  ')
l88 = tk.Label(tab2,text = 'Bland Chromatin :  ')
l99 = tk.Label(tab2,text = 'Normal Nucleoli :  ')
l100 = tk.Label(tab2,text = 'Mitoses :  ')
l111 = tk.Label(tab2,text = 'Class :  ')
#Mitoses
e11 = tk.DoubleVar()
eb11 = ttk.Entry(tab2,textvariable = e11,width = 22)
e22 = tk.IntVar()
eb22 = ttk.Combobox(tab2,textvariable = e22,values=vals)
e33 = tk.IntVar()
eb33 = ttk.Combobox(tab2,textvariable = e33,values=vals)
e44 = tk.IntVar()
eb44 = ttk.Combobox(tab2,textvariable = e44,values=vals)
e55 = tk.IntVar()
eb55 = ttk.Combobox(tab2,textvariable = e55,values=vals)
e66 = tk.IntVar()
eb66 = ttk.Combobox(tab2,textvariable = e66,values=vals)
e77 = tk.IntVar()
eb77 = ttk.Combobox(tab2,textvariable = e77,values=vals)
e88 = tk.IntVar()
eb88 = ttk.Combobox(tab2,textvariable = e88,values=vals)
e99 = tk.IntVar()
eb99 = ttk.Combobox(tab2,textvariable = e99,values=vals)
e100 = tk.IntVar()
eb100 = ttk.Combobox(tab2,textvariable = e100,values=vals)
e111 = tk.IntVar()
eb111 = ttk.Combobox(tab2,textvariable = e111,values=[2,4])

b11 = tk.Button(tab2,text = 'Insert',width='18',bg='gray',fg='white',relief='flat',command = insert)

lt1.grid(row = 0,column = 0,padx = 8,pady = 8)

l11.grid(row = 1,column = 0,padx=15,pady = 8,sticky='w')
l22.grid(row = 2,column = 0,padx=15,pady = 8,sticky='w')
l33.grid(row = 3,column = 0,padx=15,pady = 8,sticky='w')
l44.grid(row = 4,column = 0,padx=15,pady = 8,sticky='w')
l55.grid(row = 5,column = 0,padx=15,pady = 8,sticky='w')
l66.grid(row = 6,column = 0,padx=15,pady = 8,sticky='w')
l77.grid(row = 7,column = 0,padx=15,pady = 8,sticky='w')
l88.grid(row = 8,column = 0,padx=15,pady = 8,sticky='w')
l99.grid(row = 9,column = 0,padx=15,pady = 8,sticky='w')
l100.grid(row = 10,column = 0,padx=15,pady = 8,sticky='w')
l111.grid(row = 11,column = 0,padx=15,pady = 8,sticky='w')

eb11.grid(row = 1,column = 1,padx=8,pady = 8)
eb22.grid(row = 2,column = 1,padx=8,pady = 8)
eb33.grid(row = 3,column = 1,padx=8,pady = 8)
eb44.grid(row = 4,column = 1,padx=8,pady = 8)
eb55.grid(row = 5,column = 1,padx=8,pady = 8)
eb66.grid(row = 6,column = 1,padx=8,pady = 8)
eb77.grid(row = 7,column = 1,padx=8,pady = 8)
eb88.grid(row = 8,column = 1,padx=8,pady = 8)
eb99.grid(row = 9,column = 1,padx=8,pady = 8)
eb100.grid(row = 10,column = 1,padx=8,pady = 8)
eb111.grid(row = 11,column = 1,padx=8,pady = 8)
b11.grid(row = 12,column = 1,padx=8,pady = 8)


####Tab3###


df = pd.read_sql_query("select id from [dbo].[breast_cancer_data]",conn)
valarr = []
for i in df['id'].values:
    valarr.append(i)
   
lt2 = tk.Label(tab3,text = 'Select ID to Delete Data ',font = ('Helvetica',16) )
l12 = tk.Label(tab3,text = 'ID Number :  ')
b12 = tk.Button(tab3,text = 'Delete',width='18',bg='gray',fg='white',relief='flat',command = delete)

e12 = tk.DoubleVar()
eb12 = ttk.Combobox(tab3,textvariable = e12,values=valarr)
lt2.grid(row = 0,column = 0,padx = 8,pady = 8)
l12.grid(row = 1,column = 0,padx=15,pady = 8,sticky='w')
eb12.grid(row = 1,column = 1,padx=8,pady = 8)
b12.grid(row = 2,column = 1,padx=8,pady = 8)



####tab4####

lt3 = tk.Label(tab4,text = 'Select ID to view data : ',font = ('Helvetica',16) )
l14 = tk.Label(tab4,text = 'ID Number :  ')
l24 = tk.Label(tab4,text = 'Clump Thickness :  ')
l34 = tk.Label(tab4,text = 'Uniformity of Cell Size :  ')
l44 = tk.Label(tab4,text = 'Uniformity of Cell Shape :  ')
l54 = tk.Label(tab4,text = 'Marginal Adhesion :  ')
l64 = tk.Label(tab4,text = 'Single Epithelial Cell Size :  ')
l74 = tk.Label(tab4,text = 'Bare Nuclei :  ')
l84 = tk.Label(tab4,text = 'Bland Chromatin :  ')
l94 = tk.Label(tab4,text = 'Normal Nucleoli :  ')
l104 = tk.Label(tab4,text = 'Mitoses :  ')
l114 = tk.Label(tab4,text = 'Class :  ')
x1 = tk.Label(tab4,text='')
x2 = tk.Label(tab4,text='')
x3 = tk.Label(tab4,text='')
x4 = tk.Label(tab4,text='')
x5 = tk.Label(tab4,text='')
x6 = tk.Label(tab4,text='')
x7 = tk.Label(tab4,text='')
x8 = tk.Label(tab4,text='')
x9 = tk.Label(tab4,text='')
x10 = tk.Label(tab4,text='')

b13 = tk.Button(tab4,text = 'View',width='18',bg='gray',fg='white',relief='flat',command = view)
e13 = tk.StringVar()
eb13 = ttk.Combobox(tab4,textvariable = e13,values=valarr)

lt3.grid(row = 0,column = 0,padx = 8,pady = 8)
l14.grid(row = 1,column = 0,padx=15,pady = 8,sticky='w')
l24.grid(row = 2,column = 0,padx=15,pady = 8,sticky='w')
l34.grid(row = 3,column = 0,padx=15,pady = 8,sticky='w')
l44.grid(row = 4,column = 0,padx=15,pady = 8,sticky='w')
l54.grid(row = 5,column = 0,padx=15,pady = 8,sticky='w')
l64.grid(row = 6,column = 0,padx=15,pady = 8,sticky='w')
l74.grid(row = 7,column = 0,padx=15,pady = 8,sticky='w')
l84.grid(row = 8,column = 0,padx=15,pady = 8,sticky='w')
l94.grid(row = 9,column = 0,padx=15,pady = 8,sticky='w')
l104.grid(row = 10,column = 0,padx=15,pady = 8,sticky='w')
l114.grid(row = 11,column = 0,padx=15,pady = 8,sticky='w')
x1.grid(row = 2,column = 1,padx=15,pady = 8,sticky='w')
x2.grid(row = 3,column = 1,padx=15,pady = 8,sticky='w')
x3.grid(row = 4,column = 1,padx=15,pady = 8,sticky='w')
x4.grid(row = 5,column = 1,padx=15,pady = 8,sticky='w')
x5.grid(row = 6,column = 1,padx=15,pady = 8,sticky='w')
x6.grid(row = 7,column = 1,padx=15,pady = 8,sticky='w')
x7.grid(row = 8,column = 1,padx=15,pady = 8,sticky='w')
x8.grid(row = 9,column = 1,padx=15,pady = 8,sticky='w')
x9.grid(row = 10,column = 1,padx=15,pady = 8,sticky='w')
x10.grid(row = 11,column = 1,padx=15,pady = 8,sticky='w')
eb13.grid(row = 1,column = 1,padx=8,pady = 8)
b13.grid(row = 1,column = 2,padx=8,pady = 8)

root.mainloop()
