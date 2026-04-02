# How do you configure CORS with Flask ?

In Flask, it would be :
```
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["https://frontend.example.com"])
```

This tells the browser that requests from ``https://frontend.example.com`` are allowed to read the responses from the API.
