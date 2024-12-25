import sys
import os
import markdown

def display_message():
    print('How to Use: python3 file-converter.py markdown <input_file> <output_file>')
    print('You can convert a .md file to new .html file by using the command above.')
    sys.exit(1)

if len(sys.argv) < 4:
    display_message()

elif sys.argv[1] != 'markdown':
    display_message()

else:
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    input_extention = os.path.splitext(input_file)[1]
    output_extention = os.path.splitext(output_file)[1]

    if input_extention != '.md':
        print('Your input file should be a markdown file. Please try again.')
        sys.exit(1)

    if output_extention != '.html':
        output_file = output_file + '.html'

    with open(input_file, 'r') as f:
        markdown_contents = f.read()
        html_contents = markdown.markdown(markdown_contents, extensions=['tables', 'extra'])

    with open(output_file, 'w') as f:
        f.write(html_contents)

print(f"Converted {input_file} to {output_file} successfully.")

sys.exit(0)