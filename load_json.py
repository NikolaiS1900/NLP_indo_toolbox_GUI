import json

def load_json(json_file_path):
    """Load the JSON file and return the dictionary."""
    try:
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        print(f"Error: The file {json_file_path} was not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: The file {json_file_path} is not a valid JSON file.")
        return {}
