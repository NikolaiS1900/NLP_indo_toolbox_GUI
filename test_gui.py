import os
from gooey import Gooey, GooeyParser

@Gooey(program_name="Text Processing Tool",
       program_description="Select options for text processing",
       default_size=(800, 600))
def main():
    parser = GooeyParser(description="Choose an action to perform")

    # Main action selection
    parser.add_argument('action', 
                        choices=['Process Text', 'Generate Report'],
                        help="Select the action to perform")

    # This will show checkboxes if 'Process Text' is selected
    group = parser.add_argument_group('Processing Options', 
                                       gooey_options={'show_if': {'action': 'Process Text'}})

    group.add_argument('--remove_punctuation', 
                       action='store_true', 
                       help="Remove punctuation from the text")
    group.add_argument('--convert_to_lower', 
                       action='store_true', 
                       help="Convert text to lower case")
    group.add_argument('--remove_numbers', 
                       action='store_true', 
                       help="Remove numbers from the text")

    # For demonstration purposes, we'll have another argument that does not depend on the action
    parser.add_argument('--output_file', 
                        help="Specify the output file name")

    args = parser.parse_args()

    print(f"Action: {args.action}")
    if args.action == 'Process Text':
        print(f"Remove Punctuation: {args.remove_punctuation}")
        print(f"Convert to Lower: {args.convert_to_lower}")
        print(f"Remove Numbers: {args.remove_numbers}")

    print(f"Output File: {args.output_file}")

if __name__ == "__main__":
    main()
