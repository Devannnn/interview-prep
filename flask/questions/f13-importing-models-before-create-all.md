Q. How SQLAlchemy knows which tables to create in the database ? 

SQLAlchemy creates the tables in the database when the method `db.create_all()` is executed. But how does it know which tables to create ? `db.create_all()` create a table for all the models classes that have been registered in SQLAlchemy's metadata and a model class is registered whenever it's imported. So in order to have a table created for each of your model, you just have to make sure that those models are imported before running `db.create_all()`.
