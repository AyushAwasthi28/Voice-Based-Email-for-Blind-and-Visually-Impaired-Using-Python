import speech_recognition as sr
import pyttsx3
import easyimap
import smtplib
from email.message import EmailMessage

# Set up the voice engine
engine = pyttsx3.init()

# Set up the email connection
imap_server = 'imap.gmail.com'
imap_username = 'voicemailforblindproject@gmail.com'
imap_password = 'vvxiqwoyfowrctfr'
imap_passkey = '0305'

# Connect to the Gmail server using easyimap
mailbox = easyimap.connect(imap_server, imap_username, imap_password)

# Function to send an email
def send_email():
    # Prompt the user to enter the email recipient, subject, and message
    
    recipient = 'ayushawasthi914@gmail.com'
    engine.say('You said:')
    engine.say(recipient)
    str = 'Please say the email subject'
    print(str)
    engine.say(str)
    engine.runAndWait()
    subject = get_voice_input()
    engine.say('You said:')
    engine.say(subject)
    str = 'Please say the email message'
    print(str)
    engine.say(str)
    engine.runAndWait()
    message = get_voice_input()
    str = 'You have spoken the message:'
    print(str)
    engine.say(str)
    engine.say(message)

    # Set up the email message
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = 'voicemailforblindproject@gmail.com'
    msg['To'] = recipient

    # Send the email using smtplib
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('voicemailforblindproject@gmail.com', 'vvxiqwoyfowrctfr')
        smtp.send_message(msg)

    engine.say('Email sent successfully')
    engine.runAndWait()

# Function to read emails
def read_emails():
    # Get the list of emails from the mailbox
    emails = mailbox.unseen()

    # Read out the subject and sender of each email
    for i, email in enumerate(emails):
        engine.say('Email number ' + str(i+1))
        engine.runAndWait()
        engine.say('From ' + email.from_addr)
        engine.runAndWait()
        engine.say('Subject ' + email.title)
        engine.runAndWait()

# Function to exit the program
def exit_program():
    engine.say('Exiting the program')
    engine.runAndWait()
    quit()

# Function to get voice input
def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        # Convert the voice input to text using SpeechRecognition
        text = r.recognize_google(audio)
        return text
    except:
        # If there is an error, prompt the user to repeat their input
        str = 'Sorry, I could not understand your input. Please repeat your command.'
        print(str)
        engine.say(str)
        engine.runAndWait()
        return get_voice_input()

# Main program loop
while True:
    str = "Welcome to voice controlled email service for the Blind and Visually Impaired"
    print(str)
    engine.say(str)
    str = 'Speak SEND to Send email   Speak READ to Read Inbox   Speak EXIT to Exit'
    print(str)
    engine.say(str)
    engine.runAndWait()
    command = get_voice_input().upper()
    
    if command == 'SEND':
        send_email()
    elif command == 'READ':
        read_emails()
    elif command == 'EXIT':
        exit_program()
    else:
        str = 'Sorry, I did not understand your command. '
        engine.say(str)
        engine.runAndWait()
