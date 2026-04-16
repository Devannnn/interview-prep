Q. What is the application context and why do we need it?

The application context is a temporary runtime scope that tells Flask which app is currently active.

Anywhere where the code needs to be aware of the app's configuration - for example when working with a database - we need to specify which app we are talking about. This is done using `with app.app_context():`. It literaly means, 'in this section, the code is aware of the app's configuration'.

There is one place where we don't need to specify the application context and that's the routes. Flask automatically pushes the application context before the route functions run. But anywhere else, we do need to specify the context.

Why is there an application context ? Why not activate the configuration once and keep it open instead of constantly activating it / tearing it down ?

In a single-app scenario, you could do that and it would work. However, Flask was designed to support multiple apps running on the same Python process. For instance, an admin app and a public app. The context is how Flask knows which app a given piece of code is working with right now.

Also, once the context is torn down, all the database sessions are closed and the temporary state gets wiped. So this constant activate/tear down context allows to clean resource and create a fresh context each time.