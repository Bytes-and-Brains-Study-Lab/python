# Exercise: Basic Git and Github concepts

## Problem Statement (Simple)
This exercise simulates a real-world collaborative scenario using Git and GitHub, where you will work together to write 
a short Python program that generates a random story. 
Each one of you will take responsibility for a specific part of the story and practice Git and GitHub operations.

Check following files for this exercise:
- Main file to run the story (`git_exercise_1.py`)
- Abstract base class for story parts (`abc_story.py`)
- Sample 1st line of story (`story_part_1.py`)

## Instructions
1. Clone the Repository <br>
   `git clone <repository-url>`
2. Open the repository in your favorite IDE (PyCharm, VSCode, etc.)
3. Create new branch with your name/story part number <br>
   `git checkout -b <branch-name>`
4. Implement code in answers folder. I have created the first line of story (story_part_1.py) as an example.
5. Create a new file in the answers folder with the next part of the story.<br>
   `git add .` <br>
   `git commit -m "Your commit message"`
6. Push your changes to the remote repository <br>
   `git push origin <branch-name>`
7. Create a pull request on GitHub to merge your changes into the main branch
8. Let me know on whatsapp, I will review and merge the pull request. If story is not in sequence, I will ask you to make changes.
9. Repeat steps 3-8 for each part of the story.
10. To get the latest changes from the main branch, use the following commands: <br>
    `git checkout main` <br>
    `git pull origin main` <br>
    `git checkout <branch-name>` <br>
    `git merge main` <br>
11. If you face any issues, feel free to ask for help. Discuss how you want to divide the story among yourselves.
12. Test your code locally by running git_exercise_1.py before pushing to the remote repository.
13. Try both git command line as well as from GUI (PyCharm/VSCode) to get comfortable with both.
14. If you don't like the story beginning, feel free to change it. Just make sure the story flows well.
15. Have fun and enjoy the collaborative coding experience!