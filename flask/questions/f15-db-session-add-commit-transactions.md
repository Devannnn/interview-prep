Q. What is the difference between `db.session.add()` and `db.session.commit()`? Why do we have this two-step process ?

`add` put an operation to the staging area - it means it'll be included in the next transaction - the commit. You can stage several operations before committing. Once you added all the operations, you call commit. This persists those operations in the database.

This two-step process allows to have an atomic transaction. This mean that all the operations are considered as a single transaction - either all succeed or none. If something fails, none of the staged changes are written to the database. That way, the database is never left in a half-written state which would make it inconsistent.