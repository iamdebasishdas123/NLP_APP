from tkinter import *
from db import Database
from tkinter import messagebox
from my_api import api
class NLPAPP:
    def __init__(self):
        
        self.dbo=Database()
        self.apio=api()
        self.root=Tk()
        self.root.title("NLPAPP")
        self.root.iconbitmap('resource/favicon.ico')
        self.root.geometry('450x500')
        self.root.configure(bg='#34495E')
        
        self.login_gui()
        
        self.root.mainloop()
        
    def login_gui(self):
        
        self.clear()
        
        heading=Label(self.root,text='NLP APP',bg='#34495E',fg='green')
        heading.pack(pady=(30,30))
        heading.configure(font=('Verdana',24,'bold'))
        
        lebel1=Label(self.root,text='enter email')
        lebel1.pack(pady=(10,10))
        
        self.email_input= Entry(self.root)
        self.email_input.pack(pady=(10,20),ipady=3)
        
        lebel2=Label(self.root,text='password')
        lebel2.pack(pady=(10,10))
        
        self.password_input= Entry(self.root,show='*')
        self.password_input.pack(pady=(10,20),ipady=3)
        
        login_btn=Button(self.root,text='Login',width=7,height=2,command=self.perfrom_login)
        login_btn.pack(pady=(10,10))
        
        lebel3=Label(self.root,text='Not a member?')
        lebel3.pack(pady=(20,10))
        
        register_btn=Button(self.root,text='Register Now',width=10,height=2,command=self.register_gui)
        register_btn.pack(pady=(20,10))
        
    def register_gui(self):
        #clear the gui 
        
        self.clear()
        
        heading=Label(self.root,text='NLP APP',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('Verdana',24,'bold'))
        
        #name 
        
        self.name_input=Label(self.root,text='Enter Your name')
        self.name_input.pack(pady=(10,10))
        
        #enter name
        
        self.name_input= Entry(self.root)
        self.name_input.pack(pady=(10,20),ipady=3)
        
        #email
        
        lebel1=Label(self.root,text='enter email')
        lebel1.pack(pady=(10,10))
        
        #enter email
        
        self.email_input= Entry(self.root)
        self.email_input.pack(pady=(10,20),ipady=3)
        
        #password
        
        lebel2=Label(self.root,text='password')
        lebel2.pack(pady=(10,10))
        
        #enter password
        
        self.password_input= Entry(self.root)
        self.password_input.pack(pady=(10,20),ipady=3)
        
        #Register button
        
        register1_btn=Button(self.root,text='Register',command=self.perfrom_registration)
        register1_btn.pack(pady=(10,10))
        
        #already a member
        
        member=Label(self.root,text='Already a member!')
        member.pack(pady=(20,10))
        
        #login button
        
        login_btn=Button(self.root,text='login Now',width=10,height=2,command=self.login_gui)
        login_btn.pack(pady=(20,10))
        
          
        
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
     
            
    #perfrom registration 
       
    def perfrom_registration(self):
        name=self.name_input.get()
        email=self.email_input.get()
        password=self.password_input.get()
        recive=self.dbo.add_data(name , email , password)
        
        if recive :
            messagebox.showinfo('success','registration successfully')
        else:
            messagebox.showerror('error is here','email exits! \n You can Log in Now')
        
    def perfrom_login(self):
        email=self.email_input.get()
        password=self.password_input.get()
        
        recive=self.dbo.search(email,password)
        
        if recive:
            messagebox.showinfo("success","Login successfully")
            self.home_gui()
        else:
            messagebox.showerror('error','Incorrect email / password')
        
    def home_gui(self):
        
        self.clear()
        
        heading=Label(self.root,text='Menu to Request',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('Verdana',24,'bold'))
        
        sentiment_btn=Button(self.root,text='Sentiment Analysis',height=4,width=20,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10,10))
        
        ner_btn=Button(self.root,text='Name Entity Recognition',height=4,width=20,command=self.ner_gui)
        ner_btn.pack(pady=(10,10))
        
        abuse_btn=Button(self.root,text='abuse Prediction',height=4,width=20,command=self.abuse_gui)
        abuse_btn.pack(pady=(10,10))
        
        
        logout_btn=Button(self.root,text='LOG OUT',height=2,width=8,command=self.login_gui)
        logout_btn.pack(pady=(10,10))
        
        
    def sentiment_gui(self):
        self.clear()
        
        heading=Label(self.root,text='Sentiment Analysis',bg='#34495E',fg='black')
        heading.pack(pady=(30,30))
        heading.configure(font=('Verdana',24,'bold'))
        
        
        lebel1=Label(self.root,text='Write text',bg='#34495E',fg='black')
        lebel1.pack(pady=(30,30))
        heading.configure(font=('Verdana',24,'bold'))
        
        self.sentiment_input= Entry(self.root,width=50)
        self.sentiment_input.pack(pady=(10,20),ipady=3)
        
        sentiment_btn=Button(self.root,text='sentiment Analysis',height=4,width=20,command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10,10))
        
        self.sentiment_result=Label(self.root,text='',bg='#34495E',fg='black')
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.configure(font=('Verdana',24,'bold'))
        
        goback_btn=Button(self.root,text='Back to Menu',height=4,width=10,command=self.home_gui)
        goback_btn.pack(pady=(10,10))
        
    def ner_gui(self):
        
        self.clear()
        
        heading=Label(self.root,text='Name Entity Recognition',bg='#34495E',fg='red')
        heading.pack(pady=(30,30))
        heading.configure(font=('Verdana',24,'bold'))
        
        
        lebel1=Label(self.root,text='Write text',bg='#34495E',fg='black')
        lebel1.pack(pady=(30,30))
        heading.configure(font=('Verdana',24,'bold'))
        
        self.ner_input= Entry(self.root,width=50)
        self.ner_input.pack(pady=(10,20),ipady=3)
        
        ner_btn=Button(self.root,text='NER button',height=4,width=20,command=self.do_ner_analysis)
        ner_btn.pack(pady=(10,10))
        
        self.ner_result=Label(self.root,text='',bg='#34495E',fg='black')
        self.ner_result.pack(pady=(10,10))
        self.ner_result.configure(font=('Verdana',15,'bold'))
        
        goback_btn=Button(self.root,text='Back to Menu',height=4,width=20,command=self.home_gui)
        goback_btn.pack(pady=(10,10))
        
    def abuse_gui(self):
        self.clear()
        
        heading=Label(self.root,text='abuse Prediction',bg='#34495E',fg='red')
        heading.pack(pady=(30,30))
        heading.configure(font=('Verdana',24,'bold'))
        
        
        lebel1=Label(self.root,text='Write text',bg='#34495E',fg='black')
        lebel1.pack(pady=(30,30))
        heading.configure(font=('Verdana',24,'bold'))
        
        self.abuse_input= Entry(self.root,width=50)
        self.abuse_input.pack(pady=(10,20),ipady=3)
        
        abuse_btn=Button(self.root,text='abuse button',height=4,width=20,command=self.do_abuse_analysis)
        abuse_btn.pack(pady=(10,10))
        
        self.abuse_result=Label(self.root,text='',bg='#34495E',fg='black')
        self.abuse_result.pack(pady=(10,10))
        self.abuse_result.configure(font=('Verdana',15,'bold'))
        
        goback_btn=Button(self.root,text='Back to Menu',height=2,width=8,command=self.home_gui)
        goback_btn.pack(pady=(10,10))
        
        
    def do_sentiment_analysis(self):
        text=self.sentiment_input.get()
        result=self.apio.sentiment_analysis(text)
        
        txt=''
        for i in result['sentiment']:
            txt=txt+i+'-.'+str(result['sentiment'][i])+'\n'
            
        self.sentiment_result['text']=txt
        
    def do_ner_analysis(self):
        text=[self.ner_input.get()]
        result=self.apio.ner_analysis(text)
            
        self.ner_result['text']=result
        
    def do_abuse_analysis(self):
        text = [self.abuse_input.get()]
        result = self.apio.abuse_analysis(text)
        self.abuse_result['text']=result
    
        


        
nlp=NLPAPP()