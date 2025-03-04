# -*- coding: utf-8 -*-
"""Skincare_tracker_chatbotfeature

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Gb8n9frqF9rWPRI0g07EDfvryqC4_O7k
"""

!pip install openai





import openai
import json

class Log:

  def __init__(self,symptoms, sleep, hyd, diet, sun ):
    self.symptoms = symptoms
    self.sleep = sleep
    self.hyd = hyd
    self.diet = diet
    self.sun = sun

  def editField(self, input):
    field = ""
    if field == "symptoms":
      self.symptoms = input
    if field == "sleep":
      self.sleep = input
    if field == "hyd":
      self.hyd = input
    if field == "diet":
      self.diet = input
    if field == "sun":
      self.sun = input
    return

  def getSymptoms(self):
      return self.symptoms
  def getSleep(self):
    return self.sleep
  def getHyd(self):
    return self.hyd
  def getDiet(self):
    return self.diet
  def getSun(self):
    return self.sun


class Main:

# Your OpenAI API key

# Function to interact with GPT-3

  def __init__(self):
    self.log = Log("","","","","")
    self.word = ""

  def createLog(self):
    print("What symptoms did you have today?")
    symptoms = input()
    print("How long did you sleep last night?")
    sleep = input()
    print("How much did you drink today?")
    hyd = input()
    print("What did you eat today?")
    diet = input()
    print("What sun exposure did you have today?")
    sun = input()
    self.log = Log(symptoms, sleep, hyd, diet, sun)

  def logInput(self):
    word = self.log.getSymptoms() + self.log.getSleep() + self.log.getHyd() + self.log.getDiet() + self.log.getSun()
    return word

  def summary(self):
#    openai.api_key = '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'

    def store_conversation(conversation_history, filename = 'conversation_history.json'):
      with open(filename, 'w') as f:
        json.dump(conversation_history, f)

    def get_customized_response(user_input):
     # prompt = f"The input you are given is of someone logging their skin condtion. This includes symptoms, sleep that night,hydration that day, diet that day, and sun exposure that day. Provide a comprehensive summary of what each of those fields means and how they can improve their skin through each field"

      response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "The input you are given is of someone logging their skin condtion. This includes symptoms"+self.log.getSymptoms()+", sleep that night" +self.log.getSleep()+", hydration that day" + self.log.getHyd()+" , diet that day" + self.log.getDiet()+" , and sun exposure that day" + self.log.getSun()+" . Provide a comprehensive summary of what each of those fields means and how they can improve their skin through each field. Be specific. It has to be related to the responses that gave. Answer as if you are talking to them'"},
        {"role": "user","content": user_input}# System message to set context
          # User's input
    ],
       # prompt = prompt,
        max_tokens = 1000,
        temperature = 0.7
      )

      return response.choices[0].message.content.strip()

    def chat_with_single_prompt():
      conversation_history = [
          {"role": "system", "content": "The input you are given is of someone logging their skin condtion. This includes symptoms, sleep that night," +
           "hydration that day, diet that day, and sun exposure that day. Provide a comprehensive summary of what each of those fields means and how they can improve their skin through each field. Be specific. It has to be related to the responses that gave"
          }
          #{"role": "user","content": user_input}

      ]

      user_input = self.word

      assistant_response = get_customized_response(user_input)
      conversation_history.append({"role": "user", "content": user_input})
      conversation_history.append({"role": "assistant", "content": assistant_response})

      store_conversation(conversation_history)
      print("Summary:", assistant_response)

    chat_with_single_prompt()



  def run(self):
    self.createLog()
    self.summary()

m = Main()
m.run()

# Start the chatbot