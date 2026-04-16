Q. What do black and isort do, and why do they need to be configured together?

`black` is a code formatter which rewrite Python files to enforce a consistent style. `isort` is a tool which reorder the imports of each file.

The purpose of those tools is to delete any discussions on the formatting. They ensure every file looks the same, regardless of who wrote it.

They should be configured together because they can conflict. Especially, `black` has some opinions on how imports should look. `isort` has others opinions. Without coordination between the two tools, they would reformat the same lines differently. To solve this, `isort` should be configured with `profile = "black"`.