"""
Example script for validating the efficacy of click-refiner general purpose CLICK accuracy improvement for AI vision models

When I presented the goal and screenshot below to gpt4v and asked where to click, it responded (x: 50%, y: 39%).

Let's see if we can refine this~!
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")
client.base_url = os.getenv("OPENAI_API_BASE_URL", client.base_url)

# 0,0 is top left corner
objective = "Find the price of bitcoin" #  given the current state of my computer (see screenshot)"
previous_action = ""
proposed_click_x = 50
proposed_click_y = 39
description = "Click: Google Search field" # aka target
reason = "This will allow me to search for a banana"
screenshot = "screenshots/screenshot.png"
number_of_iterations = 1

VISION_PROMPT = f"""
Given the screenshot and goal: "{objective}"

Where should I click to "{description}"? Why? "{reason}"

Please provide the x, y coordinates as a fraction out of 100%
"""