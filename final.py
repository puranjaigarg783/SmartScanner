import json

def construct_json_from_file(file_path):
    """Constructs a JSON object from the text file."""
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Ensure there's at least one line
    if lines:
        first_line = lines[0].split()
        # Ensure the first line has at least one word
        if first_line:
            discreet_response = first_line[0]
            # Remove the first word from the first line for the explain key
            explain_text = ' '.join(first_line[1:])
            if len(lines) > 1:
                # Include the rest of the file in the explain key
                explain_text += '\n' + ''.join(lines[1:])
        else:
            raise ValueError("The first line of the file is empty.")
    else:
        raise ValueError("The file is empty.")

    # Constructing the JSON object
    json_data = {
        "discreet response": discreet_response,
        "explain": explain_text
    }
    return json_data

def main():
    # Replace 'your_text_file.txt' with your actual text file path
    file_path = 'oa_output.txt'
    try:
        json_data = construct_json_from_file(file_path)
        with open('final.json', 'w') as json_file:
          json.dump(json_data, json_file, indent=4)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

