html_file = open("index.html", "w")

html_content = """
<html>
  <head>
    <title>My First HTML File</title>
  </head>
  <body>
    <h1>Hello, World!</h1>
    <h1>Aniket Here!</h1>
    <p>This is my first HTML file created using Python.</p>
  </body>
</html>
"""

html_file.write(html_content)
html_file.close()
