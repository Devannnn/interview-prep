Q. How do `Mapped[...]` annotations and `mapped_column()` work together in SQLAlchemy 2.x style models? 

`Mapped[...]` is a Python type annotation which tells SQLAlchemy the type of the column and if it's required. It gives autocomplete and type checking in the editor.

`mapped_column()` is a method to declare the database-level constraints of a field. That's what the database actually enforces.