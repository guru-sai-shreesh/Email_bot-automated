import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()

engine = pyttsx3.init()
engine.setProperty('rate', 180)
#engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha.premium')
#mac users can remove above commment for better experience

contact_list = {
    'myself': 'gojo.testing123@gmail.com',
    'guru sai': 'guru.sai.shreesh@gmail.com',
    'jennie': 'jennie@blackpink.com',
    'lisa': 'lisa@blackpink.com',
    'charan': 'charan123@gmail.com'
}

def talk(text):
    engine.say(text)
    engine.runAndWait()

def mike_out():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)#to connect to server
    server.starttls()#tells that it is an secure connection
    # Make sure to give app access in your Google account
    server.login('gojo.testing123@gmail.com', 'hellogojo')
    email = EmailMessage()
    email['From'] = 'gojo.testing123@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


def create_email():
    print("Receiver's names(you can say 'All' for all your contacts): ", end=' ')
    talk('To Whom you want to send this Email.')
    talk('you can send this to multiple people by connecting them with and!')
    l_names = mike_out()
    if l_names == 'quit':
        exit()
    names = l_names.split(' and ')
    for name in names:
        if name not in contact_list:
            names.remove(name)
    receivers=[]
    if len(names)==0:
        talk("sorry there are no similar email addresses in your contacts")
        talk("please try again later")
        exit()
    for name in names:
        receivers.append(contact_list[name])
    print("Receiver's Email adresses: \n", *receivers)
    print('Subject of this Email: ', end=' ')
    talk('What is the subject of this Email?')
    subject = mike_out()
    if subject == 'quit':
        exit()
    print('Text in your Email: ', end=' ')
    talk('Tell me the text in your Email?')
    message = mike_out()
    if message == 'quit':
        exit()
    for receiver in receivers:
        send_email(receiver, subject, message)
    print('Email sent successfully to', *names)
    talk('Your emails has been sent successfully')

    talk('Do you want to send another email?')
    send_more = mike_out()
    if send_more=='yes' or send_more=='yep':
        isnew_ornot()
def isnew_ornot():
    print("Say 'YES' if it is known contact else say 'NO': ")
    talk('Are you sending this email to a know contact?')
    opt = mike_out()
    if opt == 'yes':
        create_email()
    elif opt == 'no':
        talk('type the name and address of new contact!')
        name = input("Type name of new contact to add: ")
        email = input("Type Email address of new contact to add: ")
        contact_list[name] = email
        create_email()

talk('hello! I am samantha your email bot')
talk("you can exit at any point by saying 'quit'")
isnew_ornot()

