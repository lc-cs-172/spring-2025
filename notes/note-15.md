# CS2 Spring 2025 Note 15

## Git

### Configuration

Before you start using Git, it is a good idea to configure the system with the
commands below:

```
git config --global user.name "Your Name"
git config --global user.email "yourname@yourdomain.edu"
```

This step is only needed once per platform on which you work.

### Common actions

Here is a short summary of possible Git actions, how to perform perform them
with Visual Studio Code, and how to perform them as a command typed in a
terminal.  Note that I'm showing only one way to perform these actions, but
generally there are multiple approaches to the same result.

With respect to source control, Visual Studio Code has two important areas to
keep in mind.  One, the "Source Control" icon, shown below, typically located in
the left margin.

![Visual Studio Code's Source Control icon](Source-Control-icon.png)

The number displayed with the icon will vary with the number of changes that
have been made in your copy of the repository.  In my case, there were 17 such
changes.

The second area that I will call "current branch," shown below, is typically
located at the bottom of the window.

![Visual Studio Code's current branch display](current-branch.png)

Both of those areas are clickable.

Action | Visual Studio Code | Command line
-|-|-
Status | Source Control > (Staged) Changes | `git status`
Logs | Source Control > Source Control Graph | `git log --oneline`
Change branch | Current branch > Select a branch | `git checkout branchname`
Create a new branch | Current branch > Create new branch ... | `git checkout -b branchname`
Stage a file in current branch | Source Control > Changes > + | `git add filename`
Unstage a file in current branch | Source Control > Staged Changes > − | `git restore --staged filename`
Discard all changes in a file | Source Control > Changes > − | `git restore filename`
Commit staged files to current branch | Source Control > Commit | `git commit -m 'commit message'`
Pull new commits from the parent repository | Source Control > Source Control Graph > Pull icon | `git pull`

Two important notes:

1. Pull only when you are on the "main" branch and only when there are no staged
files and no modified files (marked with the letter "M").  If it is not the
case, park those changes in a branch or restore the original files first.

2. The "current branch" area will change to reflect the branch on which you
are currently.

When you make a commit with Visual Studio Code, you will be asked to type a
commit message.  When you are done, save the changes to the commit message and
close the associated tab (all lines in the commit message starting with the
pound sign (`#`) will be ignored).  While Visual Studio Code is waiting for you
to finish editing the commit message, the "Commit" button will be grayed out.
