Q. How do you link the Flask application with the database ? Why in that order ?

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