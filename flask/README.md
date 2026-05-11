# Flask — interview questions

## Table of contents

- [1. What does passing __name__ to Flask() do, and why does it matter?](#1-what-does-passing-name-to-flask-do-and-why-does-it-matter)
- [2. What does app.run() do, why shouldn't you use it in production, and what do you use instead?](#2-what-does-apprun-do-why-shouldnt-you-use-it-in-production-and-what-do-you-use-instead)
- [3. How does routing work in Flask?](#3-how-does-routing-work-in-flask)
- [4. How do you handle JSON data in Flask?](#4-how-do-you-handle-json-data-in-flask)
- [5. How does Flask expose query-string parameters ?](#5-how-does-flask-expose-query-string-parameters)
- [6. What is the `instance/` folder for ?](#6-what-is-the-instance-folder-for)
- [7. How do you configure CORS with Flask ?](#7-how-do-you-configure-cors-with-flask)
- [8. How do you handle HTTP errors in a Flask API?](#8-how-do-you-handle-http-errors-in-a-flask-api)
- [9. How do you validate data received by an API?](#9-how-do-you-validate-data-received-by-an-api)
- [10. What is a Flask blueprint and why use it?](#10-what-is-a-flask-blueprint-and-why-use-it)
- [11. How do you structure a REST API for a document system?](#11-how-do-you-structure-a-rest-api-for-a-document-system)
- [12. What's the factory pattern ? Give an example of use with Flask.](#12-whats-the-factory-pattern-give-an-example-of-use-with-flask)
- [13. What is the difference between `db.session.add()` and `db.session.commit()`? Why do we have this two-step process ?](#13-what-is-the-difference-between-dbsessionadd-and-dbsessioncommit-why-do-we-have-this-two-step-process)
- [14. How SQLAlchemy knows which tables to create in the database ?](#14-how-sqlalchemy-knows-which-tables-to-create-in-the-database)
- [15. How do you link the Flask application with the database ? Why in that order ?](#15-how-do-you-link-the-flask-application-with-the-database-why-in-that-order)
- [16. What is the application context and why do we need it?](#16-what-is-the-application-context-and-why-do-we-need-it)
- [17. Why does Flask-SQLAlchemy use a two-step pattern (create a module-level `db`, then call `db.init_app(app)` inside the app factory) instead of tying the extension to a single global app at import time? What problems does that solve for imports and configuration?](#17-why-does-flask-sqlalchemy-use-a-two-step-pattern-create-a-module-level-db-then-call-dbinit-appapp-inside-the-app-factory-instead-of-tying-the-extension-to-a-single-global-app-at-import-time-what-problems-does-that-solve-for-imports-and-configuration)
- [18. Why can you not pass a SQLAlchemy model instance directly to `jsonify()` ?](#18-why-can-you-not-pass-a-sqlalchemy-model-instance-directly-to-jsonify)
- [19. What's `app.test_client()` for in Flask ?](#19-whats-apptest-client-for-in-flask)
- [20. Explain each layer of a standard Flask app : route, model, service.](#20-explain-each-layer-of-a-standard-flask-app-route-model-service)
- [21. How do `Mapped[...]` annotations and `mapped_column()` work together in SQLAlchemy 2.x style models?](#21-how-do-mapped-annotations-and-mapped-column-work-together-in-sqlalchemy-2x-style-models)

---

#### 1. What does passing __name__ to Flask() do, and why does it matter?

<details>
<summary>Reveal answer</summary>

When creating the Flask app using the constructor Flask, you need to pass the current file name (arg __name__). It tells Flask which Python module the app belongs to. Flask then uses this module to find the directory on disk and uses it as the base path to find the templates and static folders.

</details>

---

#### 2. What does app.run() do, why shouldn't you use it in production, and what do you use instead?

<details>
<summary>Reveal answer</summary>

It runs the Flask app on a development server. The development server used by Flask is Werkzeug.

It shouldn't be used in production because it doesn't have the security and the performance of a real server. Werkzeug is a single-threaded server which means it handles one request at a time and was built only for development purposes.

For production, you use a WSGI server like Gunicorn.

</details>

---

#### 3. How does routing work in Flask?

<details>
<summary>Reveal answer</summary>

In Flask, routing is how you connect a URL path to a Python function. It's done through the decorator `@app.route(url, methods=...)`. When a request comes in, Flask matches it against its registered routes and call the corresponding view function.

</details>

---

#### 4. How do you handle JSON data in Flask?

<details>
<summary>Reveal answer</summary>

Inside the view functions, Flask automatically provides the request context and the app context. It means that to access the request body, you use the object `request` from Flask. This object comes with the method `get_json()` which allows to retrieve the JSON data as a Python dictionary. What you usually do then, is to validate the data using an expected schema and a library like pydantic. Then, you process the data and returns a json response using `jsonify()`.

</details>

---

#### 5. How does Flask expose query-string parameters ?

<details>
<summary>Reveal answer</summary>

In a Flask's route, you can access to query-string parameters using the object `request.args`. It returns a dictionary where the keys/values represent the parameters.

One caveat: it returns all parameters as strings regardless of what was sent. It means that `GET /records?instrument_id=3` gives "3" and must be explicitly cast.

</details>

---

#### 6. What is the `instance/` folder for ?

<details>
<summary>Reveal answer</summary>

The instance folder is where the application put all the files that are specific to an environment like databases, secrets, local config. All 

It's separated from the source code because those files are local and never committed. For instance, different developers might have different dev databases and you don't want them to conflict.

IMPORTANT: When using a relative SQLite URI like `sqlite:///project.db`, Flask-SQLAlchemy resolves it to this instance folder.

</details>

---

#### 7. How do you configure CORS with Flask ?

<details>
<summary>Reveal answer</summary>

In Flask, it would be :
```
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["https://frontend.example.com"])
```

This tells the browser that requests from ``https://frontend.example.com`` are allowed to read the responses from the API.

</details>

---

#### 8. How do you handle HTTP errors in a Flask API?

<details>
<summary>Reveal answer</summary>

In a Flask API, you can handle HTTP errors by registering a global error handler with the decorator `@app.errorhandler(HTTPException)`. It allows you to map all HTTPException errors bubbling up from the application to a dedicated Python function. Then, for an HTTP error, you generally want to preserve the HTTP status code, log useful information for debugging and return a consistence error response in the body.

</details>

---

#### 9. How do you validate data received by an API?

<details>
<summary>Reveal answer</summary>

You validate data received by an API against a predefined schema which defines the expected fields, types and constraints. You can use a library such as Pydantic. It will parse the input, validate it, apply some conversions or defaults values when possible and returns an error otherwise. 

</details>

---

#### 10. What is a Flask blueprint and why use it?

<details>
<summary>Reveal answer</summary>

A Flask blueprint is a way to group related routes and logic into a separate module. The idea is to split your api into several smaller parts, each with a specific purpose. These blueprints are then registered into the main API with a URL prefix and Flask includes their routes in the application routing table. 

You use blueprints to split an API by feature or domain. It makes the code more and maintainable, clearly delimitate the different parts of your API and keep files small instead of having one giant file with all the routes.

</details>

---

#### 11. What's the factory pattern ? Give an example of use with Flask.

<details>
<summary>Reveal answer</summary>

The factory pattern consists in putting all the logic to create the application inside a function. Another way would be to write this logic directly in the file and create the app at module level. 

But the issue with this method is that it becomes difficult to test the app and to run it with a different configuration. Also, any file that imports the module triggers the app creation as a side effect which can lead to circular import chain.

The factory pattern solves it. It allows to control when and how the application is created. It makes it easy to use a different configurations for development, production and testing. That's a convention to use this pattern for a Flask project.

</details>

---

#### 12. What is the difference between `db.session.add()` and `db.session.commit()`? Why do we have this two-step process ?

<details>
<summary>Reveal answer</summary>

`add` put an operation to the staging area - it means it'll be included in the next transaction - the commit. You can stage several operations before committing. Once you added all the operations, you call commit. This persists those operations in the database.

This two-step process allows to have an atomic transaction. This mean that all the operations are considered as a single transaction - either all succeed or none. If something fails, none of the staged changes are written to the database. That way, the database is never left in a half-written state which would make it inconsistent.

</details>

---

#### 13. How SQLAlchemy knows which tables to create in the database ?

<details>
<summary>Reveal answer</summary>

SQLAlchemy creates the tables in the database when the method `db.create_all()` is executed. But how does it know which tables to create ? `db.create_all()` create a table for all the models classes that have been registered in SQLAlchemy's metadata and a model class is registered whenever it's imported. So in order to have a table created for each of your model, you just have to make sure that those models are imported before running `db.create_all()`.

</details>

---

#### 14. How do you link the Flask application with the database ? Why in that order ?

<details>
<summary>Reveal answer</summary>

Flask stays small and generic
The Flask class is not supposed to know about SQLAlchemy (or every other extension). If binding were app-driven, core Flask would need hooks or methods for each library. Instead, each extension implements “attach me to this app” on the extension object.

The extension owns the wiring
SQLAlchemy.init_app(app) is where the library:

reads app.config (e.g. SQLALCHEMY_*),
registers teardowns, CLI, etc.,
stores itself on app.extensions['sqlalchemy'] (in current versions).
That logic lives in Flask-SQLAlchemy, so it belongs on db, not on Flask.

Application factory pattern
You often create db = SQLAlchemy() before any Flask instance exists, then in create_app() you call db.init_app(app). The db object is the long-lived “extension”; apps can be created, swapped, or tested with the same db stub.

So conceptually: db is the component that knows how to integrate with Flask; app is just the target you pass in.

</details>

---

#### 15. What is the application context and why do we need it?

<details>
<summary>Reveal answer</summary>

The application context is a temporary runtime scope that tells Flask which app is currently active.

Anywhere where the code needs to be aware of the app's configuration - for example when working with a database - we need to specify which app we are talking about. This is done using `with app.app_context():`. It literaly means, 'in this section, the code is aware of the app's configuration'.

There is one place where we don't need to specify the application context and that's the routes. Flask automatically pushes the application context before the route functions run. But anywhere else, we do need to specify the context.

Why is there an application context ? Why not activate the configuration once and keep it open instead of constantly activating it / tearing it down ?

In a single-app scenario, you could do that and it would work. However, Flask was designed to support multiple apps running on the same Python process. For instance, an admin app and a public app. The context is how Flask knows which app a given piece of code is working with right now.

Also, once the context is torn down, all the database sessions are closed and the temporary state gets wiped. So this constant activate/tear down context allows to clean resource and create a fresh context each time.

</details>

---

#### 16. Why does Flask-SQLAlchemy use a two-step pattern (create a module-level `db`, then call `db.init_app(app)` inside the app factory) instead of tying the extension to a single global app at import time? What problems does that solve for imports and configuration?

<details>
<summary>Reveal answer</summary>

Creating a model requires the `db` object so we have to be able to import it. However, if we were creating the database object and initialize it in the app factory, we wouldn't be able to import it.

So the solution is to use a two-step pattern. First, we create the object `db = SQLAlchemy()` which is an empty shell not associated to any app. Then, the method `db.init_app(app)` inside the factory binds the database with a specific app's configuration.

Apart fixing the import problems, that's what makes it possible to use different configuration : at factory call time, the database knows which configuration to use.

</details>

---

#### 17. Why can you not pass a SQLAlchemy model instance directly to `jsonify()` ?

<details>
<summary>Reveal answer</summary>

When creating an API, you want to return objects as a response. However, an in-memory object like a Python class is not something you can directly sends over the network. First, you have to convert the object into a format that can be transmitted. In practice, it often means to turn the object into a JSON.

That's what`jsonify()` is for : a method that serialize Python objects into a JSON.

However, `jsonify()` only knows how to serialize basic types - dicts, strings, numbers, boolean, etc. For a more complex object like a SQLAlchemy model instance - with internal state, database session references, etc - there's no universal way to turn that into JSON automatically.

To solve this, the solution is to first convert the instance into a serializable type like a dict. That's why you define the method `to_dict()`. Then, you give this dictionary to `jsonify()` which is able to turn it into a JSON.

Why do we do this ?

The thing is, serialization is not a limitation, it's actually intentional. You want to have to define clearly what should be included in the dictionary that represent your model instance. For example, you might have some fields that you don't want to expose into the API - like an internal ID or a password. Or, you might have other fields that needs to be processed before being exposed like a timestamp that should be displayed in a specific format. You want to control what leaves your application. That's the serialization step.

</details>

---

#### 18. What's `app.test_client()` for in Flask ?

<details>
<summary>Reveal answer</summary>

`app.test_client` is a Flask method which return an object to simulate HTTP requests. This test client sends requests directly to the app without any server involved. It's used with fixtures to simulate client requests and assert that the API's response is correct. 

This feature allows to run test in isolation - thanks to the test client and its fixtures, each test receives a fresh state.

That's the standard way to test automatically application routes and allow to avoid running the application on a server and perform requests manually.

</details>

---

#### 19. Explain each layer of a standard Flask app : route, model, service.

<details>
<summary>Reveal answer</summary>

The route layer receives the input, parses it, call the service and returns the response. Its job is to receive an HTTP request and return an HTTP response.

The model layer defines the data shape: columns, types, constraints and relationships. It says what the data look like.

The service layer contains the business logic of the application. That's where you define what you can do with the data. It enforces rules like "a draft can move to submitted but not directly to approved".

When you don't have a separate service layer, the business logic goes into the routes and get duplicated. If you have different routes required the same logic, you have to write it several times. The service layer centralizes this logic.

</details>

---

#### 20. How do `Mapped[...]` annotations and `mapped_column()` work together in SQLAlchemy 2.x style models?

<details>
<summary>Reveal answer</summary>

`Mapped[...]` is a Python type annotation which tells SQLAlchemy the type of the column and if it's required. It gives autocomplete and type checking in the editor.

`mapped_column()` is a method to declare the database-level constraints of a field. That's what the database actually enforces.

</details>

---
