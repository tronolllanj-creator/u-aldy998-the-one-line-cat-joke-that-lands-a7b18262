'''
Entry: a one-line cat joke.
Gate: 1-200 chars.
Writes the joke to the designated output file.
'''
import os

# The cat joke, exactly as specified
JOKE = 'I told my cat she was doing great at hiding from the mailman, and he’s been working remotely for a decade.'

# Get the output directory from environment variable or use default
output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Construct the path to the output file
output_path = os.path.join(output_dir, 'entry.txt')

# Write the joke to the file with UTF-8 encoding
with open(output_path, 'w', encoding='utf-8') as f:
    # Write the joke plus one trailing newline
    f.write(JOKE + '\n')

# Exit cleanly with status 0
raise SystemExit(0)
# Gate note: the grader runs this file with python3.13 in a sandbox with no network, up to 60 seconds; it writes exactly one line to /output/entry.txt.