Q. What's the factory pattern ? Give an example of use with Flask.

The factory pattern consists in putting all the logic to create the application inside a function. Another way would be to write this logic directly in the file and create the app at module level. 

But the issue with this method is that it becomes difficult to test the app and to run it with a different configuration. Also, any file that imports the module triggers the app creation as a side effect which can lead to circular import chain.

The factory pattern solves it. It allows to control when and how the application is created. It makes it easy to use a different configurations for development, production and testing. That's a convention to use this pattern for a Flask project.