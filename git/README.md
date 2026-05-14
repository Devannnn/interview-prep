# Git — interview questions

## Table of contents

- [1. What is the difference between Git and GitHub?](#1-what-is-the-difference-between-git-and-github)
- [2. What is a remote repository?](#2-what-is-a-remote-repository)
- [3. What does `origin` mean in Git?](#3-what-does-origin-mean-in-git)
- [4. What is a commit?](#4-what-is-a-commit)
- [5. What is a branch?](#5-what-is-a-branch)
- [6. What is `HEAD` in Git?](#6-what-is-head-in-git)
- [7. What is `.gitignore` used for?](#7-what-is-gitignore-used-for)
- [8. What is the difference between staged, unstaged, and untracked files?](#8-what-is-the-difference-between-staged-unstaged-and-untracked-files)
- [9. What does `git status` show?](#9-what-does-git-status-show)
- [10. What does `git diff` show?](#10-what-does-git-diff-show)
- [11. What is the difference between `git fetch` and `git pull`?](#11-what-is-the-difference-between-git-fetch-and-git-pull)
- [12. What is a pull request or merge request?](#12-what-is-a-pull-request-or-merge-request)
- [13. What is `git stash` used for?](#13-what-is-git-stash-used-for)
- [14. How do you undo local changes?](#14-how-do-you-undo-local-changes)
- [15. What is a merge conflict and how do you resolve it?](#15-what-is-a-merge-conflict-and-how-do-you-resolve-it)
- [16. What is the difference between `git merge` and `git rebase`?](#16-what-is-the-difference-between-git-merge-and-git-rebase)
- [17. What is the difference between `git reset` and `git revert`?](#17-what-is-the-difference-between-git-reset-and-git-revert)
- [18. How do you undo a commit that has already been pushed?](#18-how-do-you-undo-a-commit-that-has-already-been-pushed)

---

#### 1. What is the difference between Git and GitHub?

<details>
<summary>Reveal answer</summary>

Git is a distributed version control system (VCS) that runs locally and tracks history and branches.

Microsoft's GitHub is a platform to host your Git repositories. It's built on top of Git and adds collaboration features such as pull requests, code review, and issues. 

There are similar platforms to GitHub also using Git - such as GitLab and Bitbucket. They also host Git repos and add their own workflows.

</details>

---

#### 2. What is a remote repository?

<details>
<summary>Reveal answer</summary>

A remote repository is a version of a Git repository hosted somewhere outside your local machine, often on a platform such as GitHub, GitLab, or Bitbucket.

It allows you to avoid relying only on your local repository to store the project. More importantly, it enables collaboration, because several developers can each have their own local copy connected to the same remote repository.

</details>

---

#### 3. What does `origin` mean in Git?

<details>
<summary>Reveal answer</summary>

`origin` is the default name Git gives to the remote repository when you clone a project.

</details>

---

#### 4. What is a commit?

<details>
<summary>Reveal answer</summary>

A commit is a snapshot of changes made to a repository at a specific point in time. It bundles the changes staged locally and associates them with a message and a hash. A commit also points to its parent commit, creating the commit history - which is the evolution of the repo over time. It shows what the repo looks like after your staged changes.

</details>

---

#### 5. What is a branch?

<details>
<summary>Reveal answer</summary>

A branch is an independent sequence of commits. You use it to isolate work - for instance, you would create a new branch to develop a new feature. It allows you to change the code without impacting the original branch - until the feature is ready to be merged into the main branch. At low level, a branch is merely a pointer to a commit, that advances with each new commit.

</details>

---

#### 6. What is `HEAD` in Git?

<details>
<summary>Reveal answer</summary>

`HEAD` is a pointer to the latest commit of the current branch.

</details>

---

#### 7. What is `.gitignore` used for?

<details>
<summary>Reveal answer</summary>

`.gitignore` is a file used to tell git to never includes certain files to the staging area. It's used to prevent some files from ever being pushed to the remote repository. It's meant for files that should only stays local such as `.env` file, local databases or in general, anything private.

</details>

---

#### 8. What is the difference between staged, unstaged, and untracked files?

<details>
<summary>Reveal answer</summary>

These are possible states for files in a Git repository.

An untracked file is a file Git does not currently track. It is present in the working directory, but it has not been added to the staging area, so it will not be included in the next commit.

An unstaged file is a tracked file that has been modified, but whose latest changes have not been added to the staging area. It means the next commit will not contain those changes yet.

A staged file is a file whose changes have been added to the staging area. It means those changes are ready to be included in the next commit.

</details>

---

#### 9. What does `git status` show?

<details>
<summary>Reveal answer</summary>

`git status` shows the current state of the working directory and staging area.

It tells you which changes are staged for the next commit, which tracked files have unstaged changes, and which files are untracked. It also shows branch information, such as the current branch and whether it is ahead of or behind its remote branch.

</details>

---

#### 10. What does `git diff` show?

<details>
<summary>Reveal answer</summary>

`git diff` shows the unstaged changes in tracked files.

</details>

---

#### 11. What is the difference between `git fetch` and `git pull`?

<details>
<summary>Reveal answer</summary>

`git fetch` retrieves new commits and updates from the remote repository, but it does not change your current local branch or working directory.

`git pull` also retrieves new commits, but then immediately integrates them into your current branch.

</details>

---

#### 12. What is a pull request or merge request?

<details>
<summary>Reveal answer</summary>

A pull request (GitHub) or merge request (GitLab) is a request to merge one branch into another branch. 

A common usecase is creating a feature branch from `main`, developing a new feature, and then, once the feature is ready, opening a PR to merge those changes back into `main`.

A PR also provides a place for code review, discussion and automated checks before the changes are merged.
</details>

---

#### 13. What is `git stash` used for?

<details>
<summary>Reveal answer</summary>

`git stash` is used to temporarily put local changes on hold without committing them.

The changes disappear from the working directory, and the working directory is restored to the state of the latest commit. Later, the changes can be reapplied with `git stash apply` or `git stash pop`.

A useful nuance is that `git stash apply` keeps the stash in the stash list, while `git stash pop` reapplies it and removes it from the list.

</details>

---

#### 14. How do you undo local changes?

<details>
<summary>Reveal answer</summary>

It depends in which state are those changes : untracked, unstaged or staged.

For untracked changes, you can't undo them with git because they're by definition not tracked by git.

For unstaged changes, you can use `git restore <file>` to discard the changes and restore the file to the last committed version.

For stage changes, you can use `git restore --staged <file>` to remove them from the staging area and then use `git restore <file>`.

</details>

---

#### 15. What is a merge conflict and how do you resolve it?

<details>
<summary>Reveal answer</summary>
A merge conflict happens when Git tries to combine changes from two branches but cannot decide automatically how to apply them.

This often happens when both branches modified the same lines of a file, or when one branch deleted or renamed something that the other branch changed. In that situation, Git stops the merge and asks you to resolve the conflict manually.

To resolve it, you go through each conflicted file, decide which changes should be kept, edit the file to the final version, then stage the resolved files and complete the merge.
</details>

---

#### 16. What is the difference between `git merge` and `git rebase`?

<details>
<summary>Reveal answer</summary>

`git merge` combines the history of two branches. It usually creates a merge commit that has both branches as parents, which preserves the fact that the work happened on separate branches.

`git rebase` moves the commits from one branch and replays them on top of another branch. This creates a more linear history, as if the branch had been started from the latest commit of the target branch.

</details>

---

#### 17. What is the difference between `git reset` and `git revert`?

<details>
<summary>Reveal answer</summary>

`git reset` moves the current branch pointer back to a previous commit. Depending on the mode, it can also affect the staging area and working directory. It rewrites history, so it is mostly used for local commits that have not been shared.

`git revert` creates a new commit that undoes the changes introduced by a previous commit. It does not rewrite history, so it is safer for commits that have already been pushed or shared with others.

</details>

---

#### 18. How do you undo a commit that has already been pushed?

<details>
<summary>Reveal answer</summary>

To undo a commit that has already been pushed, you usually use `git revert <commit-hash>`.

This creates a new commit that applies the opposite of the original commit. It is safer than `git reset` for pushed commits because it preserves the shared history instead of rewriting it.

You could also use git reset + force push to delete a commit that has already been pushed. However, this is dangerous because it rewrites the shared history whereas `git revert` preserves it. If you are working with collaborators, you usually avoid to rewrite shared history except with team agreement.

</details>

