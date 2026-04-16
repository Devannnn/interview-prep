Q. What is the `instance/` folder for ?

The instance folder is where the application put all the files that are specific to an environment like databases, secrets, local config. All 

It's separated from the source code because those files are local and never committed. For instance, different developers might have different dev databases and you don't want them to conflict.

IMPORTANT: When using a relative SQLite URI like `sqlite:///project.db`, Flask-SQLAlchemy resolves it to this instance folder.