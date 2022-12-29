"""Library with OpenAI API solutions - comment to code generation

"""

import openai

# build a function that converts a comment into code in any language
def generate_code(text, language):
    """This submits a comment to the OpenAI API to create code in any languag

    Example:
        language = '# Python3'
        text = f"Calculate the mean distance between an array of points"
        generate_code(text, language)

    """
    #openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = "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"
    prompt = f"## {language}\n\n{text}"

    result = openai.Completion.create(
        prompt=prompt,
        temperature=0,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        model="davinci-codex",
    )["choices"][0]["text"].strip(" \n")
    return result
