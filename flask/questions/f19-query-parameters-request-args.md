Q. How does Flask expose query-string parameters ? 

In a Flask's route, you can access to query-string parameters using the object `request.args`. It returns a dictionary where the keys/values represent the parameters.

One caveat: it returns all parameters as strings regardless of what was sent. It means that `GET /records?instrument_id=3` gives "3" and must be explicitly cast.