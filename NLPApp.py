from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API
class NLPApp:

    def __init__(self):

        self.dbo = Database()

        self.root = Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap('Resources/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#34495E')
        self.api = API()

        self.login_gui()

        self.root.mainloop()

    def login_gui(self):
        self.clear()
        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label1 = Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=40)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root, text='Enter password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=40,show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_button = Button(self.root,text='Login',width=15,height=2,command=self.perform_login)
        login_button.pack(pady=(10,10))

        redirect_button = Button(self.root, text='Not a member ?? Register Now !', width=25, height=2,command=self.register_gui)
        redirect_button.pack(pady=(10, 10))


    def register_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter Name')
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=40)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=40)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=40, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_button = Button(self.root, text='Register', width=15, height=2,command=self.perform_registration)
        register_button.pack(pady=(10, 10))

        redirect_button = Button(self.root, text='Already a member ?? login now!', width=25, height=2,command=self.login_gui)
        redirect_button.pack(pady=(10, 10))

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()


    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo('success','registration successfull,you can login now!')
        else:
            messagebox.showinfo('Error','Email already exists')
    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.search(email,password)

        if response:
            messagebox.showinfo('success','login successfull')
            self.home_gui()
        else:
            messagebox.showerror('error','incorrect email / password')


    def home_gui(self):

        self.clear()

        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        sentiment_button = Button(self.root, text='Sentiment Analysis', width=25, height=4,command=self.sentiment_gui)
        sentiment_button.pack(pady=(10, 10))

        ner_button = Button(self.root, text='Named Entity Recognition', width=25, height=4,command=self.ner)
        ner_button.pack(pady=(10, 10))

        emotion_button = Button(self.root, text='Emotion Prediction', width=25, height=4,command=self.emotion_prediction)
        emotion_button.pack(pady=(10, 10))

        logout_button = Button(self.root, text='Logout', width=25, height=4,command=self.login_gui)
        logout_button.pack(pady=(10, 10))



    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading = Label(self.root, text='Sentiment Analysis', bg='#34495E', fg='white')
        heading.pack(pady=(10, 20))
        heading.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=40)
        self.sentiment_input.pack(pady=(5, 10), ipady=4)

        sentiment_button = Button(self.root, text='Analysis sentiment', width=16, height=3, command=self.do_senti)
        sentiment_button.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='',bg='#34495E',fg='white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana',16))

        goback_button = Button(self.root, text='Go back', width=25, height=4, command=self.home_gui)
        goback_button.pack(pady=(10, 10))

    def do_senti(self):
        text = self.sentiment_input.get()
        final = self.api.for_senti(text)
        self.sentiment_result['text'] = final


    def emotion_prediction(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading = Label(self.root, text='Emotion Prediction', bg='#34495E', fg='white')
        heading.pack(pady=(10, 20))
        heading.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.ep_input = Entry(self.root, width=40)
        self.ep_input.pack(pady=(5, 10), ipady=4)

        ep_button = Button(self.root, text='Analyze', width=12, height=1, command=self.do_ep)
        ep_button.pack(pady=(10, 10))

        self.ep_result = Label(self.root, text='',bg='#34495E',fg='white')
        self.ep_result.pack(pady=(10, 10))
        self.ep_result.configure(font=('verdana',16))

        goback_button = Button(self.root, text='Go back', width=25, height=4, command=self.home_gui)
        goback_button.pack(pady=(10, 10))

    def do_ep(self):
        text = self.ep_input.get()
        final = self.api.emotions(text)
        self.ep_result['text'] = final



    def ner(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading = Label(self.root, text='Named Entity Recognition', bg='#34495E', fg='white')
        heading.pack(pady=(10, 20))
        heading.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.ner_input = Entry(self.root, width=40)
        self.ner_input.pack(pady=(5, 10), ipady=4)

        ep_button = Button(self.root, text='Analyze', width=12, height=1, command=self.do_ner)
        ep_button.pack(pady=(10, 10))

        self.ner_result = Label(self.root, text='',bg='#34495E',fg='white')
        self.ner_result.pack(pady=(10, 10))
        self.ner_result.configure(font=('verdana',16))

        goback_button = Button(self.root, text='Go back', width=25, height=4, command=self.home_gui)
        goback_button.pack(pady=(10, 10))

    def do_ner(self):
        text = self.ner_input.get()
        final = self.api.ner(text)
        self.ner_result['text'] = final





nlp = NLPApp()