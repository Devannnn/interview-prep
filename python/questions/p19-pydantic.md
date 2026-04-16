Q. What's Pydantic ?

Pydantic is a Python library used to validate data against a schema. It's often used to check that data sent by a user before persisting it in the database.

The schema declares what the API accepts.

The model declares what the database stores.

Those two are separated because they can evolve independently - you might want to have fewer fields expose on the API that what you actually store into the database.