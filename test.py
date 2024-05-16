"""
Example script for validating the efficacy of click-refiner general purpose CLICK accuracy improvement for AIvision models
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")
client.base_url = os.getenv("OPENAI_API_BASE_URL", client.base_url)

"""
Goal: from the starting point of the screenshot in the screenshots folder, 
    what is the next best action to take with the goal of getting the price of bitcoin.

(1) Load the screenshot
(2) Use the model to predict the next best action
(3) Take the action
(4) Repeat until the goal is achieved

(note: multiple actions are out of scope of the click-refiner library, 
    so in this context an acceptable next best action is a single click,
    such as clicking in the browser navigation bar or the google search box)
"""

"""
When I presented this goal and the screenshot to gpt4 and asked for the next best action, 
it gave the following response: (x: 50%, y: 39%).

Let's see if we can refine this~!
"""