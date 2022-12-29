"""A library for generating images using OpenAI."""

import openai

# build a function that takes a prompt and returns a generated image
openai.api_key = "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"

def generate_image(text, size="1024x1024"):
    """Generate an image using OpenAI's API."""
    response = openai.Image.create(
        prompt=text,
        n=1,
        size=size,
    )
    image_url = response["data"][0]["url"]
    return image_url
