import speech_recognition as sr
import pyttsx3
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import webbrowser
import urllib.parse
import re

df = pd.read_csv('D:\ML_PROJECT\Responsedata.csv')
# Extract the input and response values
X = df[['Input1', 'Input2', 'Input3']].values.tolist()
y = df['Response'].values.tolist()

# Train the decision tree model
model = DecisionTreeClassifier()
model.fit(X, y)

# Implement voice recognition system
r = sr.Recognizer()
active = True  # flag to indicate whether the voice assistant should be active or not
while active:
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source, timeout=4, phrase_time_limit=2)

    # Use the decision tree model to predict response
    try:
        query = r.recognize_google(audio)
        query = query.lower()
        print(f"You: {query}")

        # functions in which Response comes from dataset.............
        if 'hello' in query or 'hi' in query or 'hyy' in query or 'hai' in query or 'hy' in query:
            response = model.predict([[0, 0, 0]])
        elif 'how are you' in query or 'how you are' in query:
            response = model.predict([[0, 0, 1]])
        elif 'also good' in query or 'also fine' in query or 'fine' in query or 'am good' in query or 'awesome' in query or 'am fine' in query:
            response = model.predict([[0, 1, 0]])
        elif 'your name' in query or 'your name' in query or 'name' in query or "what's your name" in query:
            response = model.predict([[0, 1, 1]])
        elif 'what can you do' in query or 'can I ask' in query or 'can you do' in query:
            response = model.predict([[1, 0, 0]])
        elif 'tell me about yourself' in query or 'tell me about you' in query or 'your function' in query:
            response = model.predict([[1, 0, 1]])
        elif 'good morning' in query or 'morning' in query or 'gud morning' in query:
            response = model.predict([[1, 1, 0]])
        elif 'bye' in query or 'goodbye' in query or 'tata' in query or 'see you later' in query:
            response = model.predict([[1, 1, 1]])
            active = False

        # other functions.........
        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/')
            response = 'Opening Youtube'
            active = False  # set the flag to False to stop the voice assistant
        elif 'open google' in query or 'open browser' in query:
            webbrowser.open('https://www.google.com/')
            response = 'Opening Google'
            active = False
        elif 'play' in query and 'on youtube' in query or 'play' in query:
            song_name = query.split('play')[1].replace(
                'on youtube', '').strip()
            query_string = urllib.parse.urlencode({"search_query": song_name})
            html_content = urllib.request.urlopen(
                "http://www.youtube.com/results?" + query_string)
            search_results = re.findall(
                r'watch\?v=(\S{11})', html_content.read().decode())
            if len(search_results) > 0:
                video_id = search_results[0]
                webbrowser.open(f"https://www.youtube.com/watch?v={video_id}")
                response = f"Playing {song_name} on YouTube"
                active = False
            else:
                response = f"Sorry, I could not find any video for {song_name}"

        elif 'search' in query and 'on google' in query or 'search' in query and 'on browser' in query or 'search' in query:
            search_query = query.replace(
                'search', '').replace('on google', '').strip()
            query_string = urllib.parse.urlencode(
                {"search_query": search_query})
            webbrowser.open(f"https://www.google.com/search?q={query_string}")
            response = f"Searching for {search_query} on Google"
            active = False
        else:
            response = f'Sorry, I did not understand meaning of {query}'

        # Implement text-to-speech system to output response
        engine = pyttsx3.init()
        engine.say(response)
        engine.runAndWait()

        # Print the response as text
        print(f"Assistant: {response}")

    except sr.UnknownValueError:
        print("Sorry, I couldn't listen you, Please Speak again!!")
        response = 'Sorry, I could not listen you, Please Speak again!!'
        # Implement text-to-speech system to output response
        engine = pyttsx3.init()
        engine.say(response)
        engine.runAndWait()

    except sr.RequestError:
        print("Sorry, my speech service is currently down.")
