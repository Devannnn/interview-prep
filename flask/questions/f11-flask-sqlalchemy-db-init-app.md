Q. Why does Flask-SQLAlchemy use a two-step pattern (create a module-level `db`, then call `db.init_app(app)` inside the app factory) instead of tying the extension to a single global app at import time? What problems does that solve for imports and configuration?

Creating a model requires the `db` object so we have to be able to import it. However, if we were creating the database object and initialize it in the app factory, we wouldn't be able to import it.

So the solution is to use a two-step pattern. First, we create the object `db = SQLAlchemy()` which is an empty shell not associated to any app. Then, the method `db.init_app(app)` inside the factory binds the database with a specific app's configuration.

Apart fixing the import problems, that's what makes it possible to use different configuration : at factory call time, the database knows which configuration to use.