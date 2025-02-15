# -*- coding: utf-8 -*-
"""motivation_bot_vhacks

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jYyYEnPi1x8HQPP4I41gDqqqxrBGTDNk
"""

!pip install openai

import openai
import json

class Mind:

  def __init__(self):
    self.confidence = 0

  def setConf(self):
    print("My Confidence")
    self.confidence = input()

  def affirm(self):
    openai.api_key = 'enter-api-here'

    feeling = input("How do you see yourself today? ")

    def store_conversation(conversation_history, filename = 'conversation_history.json'):
      with open(filename, 'w') as f:
        json.dump(conversation_history, f)

    def get_customized_response(user_input):
     # prompt = f"The input you are given is of someone logging their skin condtion. This includes symptoms, sleep that night,hydration that day, diet that day, and sun exposure that day. Provide a comprehensive summary of what each of those fields means and how they can improve their skin through each field"

      response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "The input given" + user_input + "is how someone is feeling about their skin and self that day. They also gave their confidence that day out of 10 " +self.confidence + "Give them affirmations, motivations, and make them feel better about themselves. Make it specific to them and their needs"},
        {"role": "user","content": user_input}# System message to set context
          # User's input
    ],
       # prompt = prompt,
        max_tokens = 1000,
        temperature = 0.7
      )

      return response.choices[0].message.content.strip()

    def chat_with_single_prompt(feeling):
      conversation_history = [
          {"role": "system", "content": "The input given" + feeling + "is how someone is feeling about their skin and self that day. They also gave their confidence that day out of 10 " +self.confidence + "Give them affirmations, motivations, and make them feel better about themselves. Make it specific to them and their needs"
          }
          #{"role": "user","content": user_input}

      ]

      user_input = feeling

      assistant_response = get_customized_response(user_input)
      conversation_history.append({"role": "user", "content": user_input})
      conversation_history.append({"role": "assistant", "content": assistant_response})

      store_conversation(conversation_history)
      print()
      print(assistant_response)

    chat_with_single_prompt(feeling)

mind  = Mind()
mind.setConf()
mind.affirm()