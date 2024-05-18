"""
General purpose mouse click accuracy improvement for AI vision models

Given a goal, propsed mouse click, screenshot, and number of iterations
(1) Crop around the proposed click location
(2) Ask the model where to click
(3) Translate the zoomed click location to the unzoomed click location
(3) Repeat for x number of iterations
(6) Return the final unzoomed click location 
"""

from PIL import Image, ImageDraw, ImageFont, ImageGrab

# x axis 50%, y axis 39% -- 0,0 is top left corner
goal = "find out the price of bitcoin, given the current state of my computer (see screenshot)"
target = "click on google search bar"
proposed_click_x = 50
proposed_click_y = 39
screenshot = "screenshots/screenshot.png"
number_of_iterations = 1

#TODO: implement this function
def refine_click(target, goal, proposed_click, screenshot, number_of_iterations):
    pass

def crop_image_around_center(input_path, output_path, x_center, y_center, percent_width, percent_height):

    """
    Crop an image around a specified center point with a given width and height percentage.

    Args:
    input_path (str): Path to the input image file.
    output_path (str): Path to save the cropped image.
    x_center (float): X coordinate of the center point as a percentage of the image width (0-100).
    y_center (float): Y coordinate of the center point as a percentage of the image height (0-100).
    percent_width (float): Width of the cropped area as a percentage of the image width (0-100).
    percent_height (float): Height of the cropped area as a percentage of the image height (0-100).

    Example usage:
    input_image_path = 'screenshots/Screenshot 2024-05-15 at 11.52.02 PM.png'
    output_image_path = 'screenshots/cropped_image.jpg'
    crop_image_around_center(input_image_path, output_image_path, 50, 39, 50, 50)
    """

    with Image.open(input_path) as img:
        width, height = img.size
        crop_width = width * (percent_width / 100)
        crop_height = height * (percent_height / 100)

        center_x = width * (x_center / 100)
        center_y = height * (y_center / 100)

        left = center_x - crop_width / 2
        upper = center_y - crop_height / 2
        right = center_x + crop_width / 2
        lower = center_y + crop_height / 2

        if (left < 0) or (upper < 0) or (right > width) or (lower > height):
            raise ValueError('The crop dimensions exceed the original image boundaries')

        cropped_img = img.crop((left, upper, right, lower))

        # Check the mode and convert to 'RGB' if 'RGBA' to avoid issues when saving as JPEG
        if cropped_img.mode == 'RGBA':
            cropped_img = cropped_img.convert('RGB')

        # Save or display the cropped image
        cropped_img.save(output_path)
        cropped_img.show()
