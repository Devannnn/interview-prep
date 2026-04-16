Q. What's SQLite ?

SQLite is a file-based relational database. It's convenient because unlike traditional database like MySQL, you don't need a separate server process nor installation.

That makes it the best choice if you need a fast way to persist data for local development.

However it lacks features needed in production like concurrent writing. That's why it's not recommended in production and is then replaced by a system like PostgreSQL.