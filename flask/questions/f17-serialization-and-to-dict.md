Q. Why can you not pass a SQLAlchemy model instance directly to `jsonify()` ?

When creating an API, you want to return objects as a response. However, an in-memory object like a Python class is not something you can directly sends over the network. First, you have to convert the object into a format that can be transmitted. In practice, it often means to turn the object into a JSON.

That's what`jsonify()` is for : a method that serialize Python objects into a JSON.

However, `jsonify()` only knows how to serialize basic types - dicts, strings, numbers, boolean, etc. For a more complex object like a SQLAlchemy model instance - with internal state, database session references, etc - there's no universal way to turn that into JSON automatically.

To solve this, the solution is to first convert the instance into a serializable type like a dict. That's why you define the method `to_dict()`. Then, you give this dictionary to `jsonify()` which is able to turn it into a JSON.

Why do we do this ?

The thing is, serialization is not a limitation, it's actually intentional. You want to have to define clearly what should be included in the dictionary that represent your model instance. For example, you might have some fields that you don't want to expose into the API - like an internal ID or a password. Or, you might have other fields that needs to be processed before being exposed like a timestamp that should be displayed in a specific format. You want to control what leaves your application. That's the serialization step.