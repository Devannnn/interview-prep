Q. What does app.run() do, why shouldn't you use it in production, and what do you use instead?

It runs the Flask app on a development server. The development server used by Flask is Werkzeug.

It shouldn't be used in production because it doesn't have the security and the performance of a real server. Werkzeug is a single-threaded server which means it handles one request at a time and was built only for development purposes.

For production, you use a WSGI server like Gunicorn.