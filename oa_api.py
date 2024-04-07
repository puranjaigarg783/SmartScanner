import openai
import os
from dotenv import load_dotenv

# Replace "your_api_key" with your actual OpenAI API key
# Load environment variables from .env file
load_dotenv()

# Read the OpenAI API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")


def read_file(file_path):
    """Reads content from a file."""
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def write_file(file_path, content):
    """Writes content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)

def query_openai_chat(prompt):
    """Sends a prompt to OpenAI's chat model and returns the response."""
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Example model name, replace with your chat model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content'].strip()

def main():
    # Path to the input file
    input_file_path = "output.txt"
    # Path to the output file
    output_file_path = "oa_output.txt"
    
    # Read the prompt from the input file
    prompt = read_file(input_file_path)
    
    # Get the response from OpenAI's chat model
    response = query_openai_chat(prompt)
    
    # Write the response to the output file
    write_file(output_file_path, response)
    
    print("Response from OpenAI's chat model has been written to", output_file_path)

if __name__ == "__main__":
    main()

