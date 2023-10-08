import os



x="""<h1>Click the Button to Run Script</h1>

<button id="refreshButton">Refresh</button>

  <script>
    document.getElementById('refreshButton').addEventListener('click', function() {
      // Trigger the GitHub Actions workflow by making an API request
      fetch('/.github/workflows/run_python_script.yml', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          ref: 'main',  // Specify the branch to trigger the workflow
        }),
      })
        .then(response => {
          if (response.ok) {
            alert('Script triggered.');
          } else {
            alert('Failed to trigger the script.');
          }
        })
        .catch(error => {
          console.error('Error:', error);
          alert('An error occurred while running the script. Please try again later.');
        });
    });
  </script>"""


# Get the path to the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the filename (index.html)
html_filename = "index.html"

# Combine the script's directory and filename to create the full file path
html_file_path = os.path.join(script_directory, html_filename)

print(f"Current Directory: {script_directory}")
print(f"HTML File Path: {html_file_path}")

# Create an HTML file for output
with open(html_file_path, "w") as html_file:
    # Write the HTML header
    html_file.write("<html>\n\n<head>\n</head>\n\n<body>\n\n")
    html_file.write(f'{x}\n')
    html_file.write("</body>\n</html>\n")
html_file.close()
print(f"HTML file '{html_filename}' generated successfully.")
