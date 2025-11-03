from openai import OpenAI, AuthenticationError

client = OpenAI()  # Use your actual API key here

instruction = """THROW AN EXCEPTION IF THE API KEY FAILS TO GET AUTHENTICATED"""

try:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": "What is OpenAI?"
            }
        ]
    )
    # Print the response content
    print(response['choices'][0]['message']['content'])

except AuthenticationError as e:
    # Handle authentication errors here
    print(f"AuthenticationError: {e}")
except Exception as e:
    # Handle other possible errors
    print(f"An error occurred: {e}")
