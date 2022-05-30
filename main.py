import tweepy
from decouple import config
import random
from PIL import Image, ImageDraw, ImageFont

API_KEY = config('API_KEY')
API_SECRET = config('API_SECRET')

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(config('ACCESS_TOKEN'), config('ACCESS_TOKEN_SECRET'))
api = tweepy.API(auth)

# this will likely be some sort of input
tweet_id = 1531352393673318401

status = api.get_status(tweet_id, tweet_mode='extended')

def create_outer():
    image_width = 1080
    image_height = 1080
    background_color_options = ["0047AB", "7f0000", "228B22", "FFC0CB"]

    # select random background color
    background_color = "#" + random.choice(background_color_options)
    
    image = Image.new("RGB", (image_height, image_width), background_color)
    image.save(f'outer_square.png', "PNG")


def create_inner():

    image_width = 800
    image_height = 800
    text_color = (0, 0, 0)
    backround_color = (255, 255, 255)

    # generate image with background
    image = Image.new("RGB", (image_height, image_width), backround_color)
    image_editable = ImageDraw.Draw(image)

    tweet_font = ImageFont.truetype('fonts/Arial.ttf', size=20)
    w_tweet_text, h_tweet_text = image_editable.textsize(status.full_text, font=tweet_font)
    image_editable.text(((image_width-w_tweet_text)/2, ((image_height-h_tweet_text)/2)), status.full_text, font=tweet_font, fill=text_color)

    image.save(f'inner_square.png', "PNG")


def place_outer():
    outer_image = Image.open('outer_square.png')
    inner_image = Image.open('inner_square.png')

    outer_image.paste(inner_image, (int((1080-800)/2), int((1080-800)/2)))

    outer_image.save(f'output.png', "PNG")


if __name__ == '__main__':
    create_outer()
    create_inner()
    place_outer()