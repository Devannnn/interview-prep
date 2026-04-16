Q. What does passing __name__ to Flask() do, and why does it matter?

When creating the Flask app using the constructor Flask, you need to pass the current file name (arg __name__). It tells Flask which Python module the app belongs to. Flask then uses this module to find the directory on disk and uses it as the base path to find the templates and static folders.