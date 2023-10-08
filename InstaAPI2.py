import os



x="""<h1>Click the Button to Run Script</h1>"""


html_filename="index.html"

# Create an HTML file for output
with open(html_filename, "w") as html_file:
    # Write the HTML header
    html_file.write("<html>\n\n<head>\n</head>\n\n<body>\n\n")
    html_file.write(f'{x}\n')
    html_file.write("</body>\n</html>\n")
html_file.close()
print(f"HTML file '{html_filename}' generated successfully.")
