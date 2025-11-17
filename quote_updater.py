import random
import os

# Define the absolute path to the project directory
project_dir = os.path.dirname(os.path.abspath(__file__))

# Construct absolute paths for the files
quotes_file = os.path.join(project_dir, "quote.txt")
readme_file = os.path.join(project_dir, "README.md")

# Load quotes with UTF-8 encoding
with open(quotes_file, "r", encoding="utf-8") as file:
    quotes = file.readlines()

# Choose a random quote
quote = random.choice(quotes).strip()

# Read the README and remove the old quote section
with open(readme_file, "r", encoding="utf-8") as readme:
    content = readme.read()

# Find the start and end of the quote section
start_marker = "<!--QUOTE_START-->"
end_marker = "<!--QUOTE_END-->"
start_index = content.find(start_marker)
end_index = content.find(end_marker)

# Build the new content
if start_index != -1 and end_index != -1:
    before_quote = content[:start_index + len(start_marker)]
    after_quote = content[end_index:]
    new_content = f"{before_quote}\n> 📜 *{quote}*\n{after_quote}"
else:
    # If markers are not found, append the quote at the end
    new_content = content + f"\n{start_marker}\n> 📜 *{quote}*\n{end_marker}\n"

# Write the new quote section
with open(readme_file, "w", encoding="utf-8") as readme:
    readme.write(new_content)

print(f"Successfully updated README.md with a new quote: {quote}")
