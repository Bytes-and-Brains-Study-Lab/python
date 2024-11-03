# Learn Git fundamentals

## Introduction
[Git](https://en.wikipedia.org/wiki/Git) is a free and open-source distributed version control system, originally created by Linus Torvalds(creator of Linux) in 2005
- Version control, also known as source control, is the practice of tracking and managing changes to software code
- VCS(Version control systems) are software tools that help software teams manage changes to source code over time
- Git is a distributed version control system, which means that the entire codebase and its full history are available on every developer's computer
- Git is a command-line tool, but there are also graphical user interfaces available for Git (eg: Inside Pycharm/IntelliJ etc)

#### Git Basics
- **Workflow**
  ![Image](https://cdn-media-1.freecodecamp.org/images/1*iL2J8k4ygQlg3xriKGimbQ.png)
  - First 3 boxes are hosted on your local machine
  - Last box (Remote Repo) hosts the project on internet, team members can push/pull changes to/from this repo
  - Examples of remote repos: github.com (free/enterprise), gitlab.com (free/enterprise), bitbucket.org (free/enterprise), Azure Devops (enterprise) 
  ![Image](https://images.javatpoint.com/tutorial/git/images/git-remote.png)
- **Branching and merging**
  ![Image](https://www.nobledesktop.com/image/gitresources/git-branches-merge.png)
  - Helps team members work concurrently
  - Individuals working on their own can benefit from the ability to work on independent streams of changes
  - Branches can be created for releases, features, bug fixes, hot fixes, experiments, prototypes, documentation, configuration etc
  - As best practice, branches should be short-lived
  - Merging is the process of integrating changes from one branch into another
  - Conflicts can occur during merging, which needs to be resolved manually
  - Merging can be done by Pull Requests, which is a code review process
- **Traceability**
  - Being able to trace each change made to the software, contains a complete long-term change history of every file
  - This allows you to go back in time and see what a file looked like at any point in time and recover older versions
  - Identify who made the changes and possibly WHY

## Exercise
- [Sign-up](https://github.com/signup?source=form-home-signup)
- [Install](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Install Pycharm Community](https://www.jetbrains.com/pycharm/download/)
- Clone this repository 
  - If you are on windows use equivalient commands (ask ChatGPT)
  - In command prompt / terminal
  - `cd [~/Documents/code/python/learn]`
  - `git clone https://github.com/Bytes-and-Brains-Study-Lab/python`
  - Optional: rename folder as `Bytes-and-Brains-Study-Lab`
  - Open folder in Pycharm
  - Follow instructions in [video](https://youtu.be/6-VYUYWsnYA)
    - Create a new branch with your name or any other name and not question-3 as shown in video
    - Create access token for push to remote repo - refer [link](https://docs.catalyst.zoho.com/en/tutorials/githubbot/java/generate-personal-access-token/)