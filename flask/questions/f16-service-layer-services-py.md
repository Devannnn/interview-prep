Q. Explain each layer of a standard Flask app : route, model, service.

The route layer receives the input, parses it, call the service and returns the response. Its job is to receive an HTTP request and return an HTTP response.

The model layer defines the data shape: columns, types, constraints and relationships. It says what the data look like.

The service layer contains the business logic of the application. That's where you define what you can do with the data. It enforces rules like "a draft can move to submitted but not directly to approved".

When you don't have a separate service layer, the business logic goes into the routes and get duplicated. If you have different routes required the same logic, you have to write it several times. The service layer centralizes this logic.