"""
General purpose CLICK accuracy improvement for AI vision models
"""

from PIL import Image, ImageDraw, ImageFont, ImageGrab


# x axis 50%, y axis 39% -- 0,0 is top left corner
goal = "find out the price of bitcoin, given the current state of my computer (see screenshot)"
target = "click on google search bar"
proposed_click_x = 50
proposed_click_y = 39
screenshot = "screenshots/screenshot.png"
number_of_iterations = 1

#either goal or target likely needed, but not both
def refine_click(target, goal, proposed_click, screenshot, number_of_iterations):
    zoom_factor = 2
    zoom_location_x = proposed_click_x
    zoom_location_y = proposed_click_y
    required_offset = 50 / zoom_factor # 50% = 25% on each side?
    # handle edge cases
    if proposed_click_x  < required_offset/2:
        zoom_location_x = required_offset/2 # proposed_click_x becomes 25 if it was less than 25
    if proposed_click_x > 100 - required_offset/2:
        zoom_location_x = 100 - required_offset/2 # proposed_click_x becomes 75 if it was more than 75
    if proposed_click_y  < required_offset/2:
        zoom_location_y = required_offset/2 # proposed_click_y becomes 25 if it was less than 25
    if proposed_click_y > 100 - required_offset/2:
        zoom_location_y = 100 - required_offset/2 # proposed_click_y becomes 75 if it was more than 75
    # modify screenshot to keep the 25% on either axis around the zoom location
    screenshot 

from PIL import Image

def crop_image_around_center(input_path, output_path, x_center, y_center, percent_width, percent_height):
    with Image.open(input_path) as img:
        width, height = img.size
        crop_width = width * (percent_width / 100)
        crop_height = height * (percent_height / 100)

        center_x = width * x_center / 100
        center_y = height * y_center / 100

        left = max(center_x - crop_width / 2, 0)
        upper = max(center_y - crop_height / 2, 0)
        right = min(center_x + crop_width / 2, width)
        lower = min(center_y + crop_height / 2, height)

        cropped_img = img.crop((left, upper, right, lower))

        # Optionally, check the mode and convert to 'RGB' if 'RGBA' to avoid issues when saving as JPEG
        if cropped_img.mode == 'RGBA':
            cropped_img = cropped_img.convert('RGB')

        # Save or display the cropped image
        cropped_img.save(output_path)
        cropped_img.show()

# Example usage
input_image_path = 'screenshots/Screenshot 2024-05-15 at 11.52.02 PM.png'
output_image_path = 'screenshots/cropped_image.jpg'
crop_image_around_center(input_image_path, output_image_path, 50, 10, 50, 50)
