# ---- Homework 1 + 2 Review---
# 3.1 Vocab Review
# Define or describe the following phrases and commands as comments:
# 1. Git vs. GitHub
# Git is a control system that tracks changes to files and code locally.
# GitHub is a platform for sharing Git repositories remotely.

# 2. Terminal vs. Command Line
# The terminal is the program that lets you interact with your computer using text commands.
# The command line is the actual interface inside the terminal where you type commands.

# 3. Local vs. Remote Repository
# A local repository is stored on your personal computer.
# A remote repository is stored online

# 4. Version Control
# A system that records changes to files over time so you can track revisions

# 5. Staging Area
# A temporary space where changes are made before committing them to the Git repository

# 6. git add
# Adds new changes to the staging area to prepare them for a commit
# 7. git commit
# Saves staged changes to the repository and creates a permanent version history
 
# 8. git push
# Uploads local commits from your computer to a remote repository

# 9. git status
# Shows the current state of your repository

# 10. git pull
# Downloads changes from a remote repository 

# 11. pwd
# Prints your current working directory

# 12. ls
# Lists all files in current directory

# 13. cd
# Moves you to a different directory

# 14. nano
# Opens a python text editor in your terminal

# 15. touch
# Creates a new empty file

# 16. mv
# Moves files and directories 
# 17. rm
# Removes/deletes files or directories permanently 

# 18. cat
# Displays the contents of a file directly in the terminal 

# 3.2 A Directory Tree
# Questions:
# • You have been plopped into Judy’s directory system. What command will tell you what your current working directory is?
# pwd

# • The terminal responds by saying you are in ∼/python decal/judy decal. What command will list all the files in your current working directory?
# ls

# • Oh no! Brianna just sent out an announcement saying that there was a typo in homework.py. You will need to pull the brianna repo repository to find the updated file. What command(s)
# will let you move to the correct repository and pull the latest changes?
# cd ../brianna_repo
# git pull

# • How would you move this new homework.py to the homework/ folder in your personal repository?
# mv homework.py ../bella/homework/

# • How would you move yourself to the same repository as homework.py?
# cd ../bella/homework/
# • You want to see the contents of homework.py in your terminal, how would you do this?
# cat homework.py

# • Great job! You just finished the homework for this week. What command(s) allow you to save the changes and push from your local repository to your remote repository?
# git add homework.py
# git commit -m ""
# git push

# • Oh no! Git gave you the following error. What commands should you call to resolve this error and push your homework properly? What does the error mean? (i.e. what did “Judy" do wrong when trying to push?)
# git pull origin main --rebase
# git push
# Judy's local repository was behind the remote one

# • What absolute path will allow you to move to Recents/?
# cd ~/Recent

# 4 Homework 3 Review
# 4.1 Data Types

def checkDataType(value):
    return type(value).__name__
# print(checkDataType(3.14))

# 4.2 Conditonals 


def evenOrOdd(num):
      if num % 2 == 0:
        return 'Even'
      else:
           return 'Odd'
# print(evenOrOdd(6))

# 5 Loops
def sumWithLoop(numbers):
    total = 0
    for n in numbers:
        total += n
    return total
# print(sumWithLoop([1, 2, 3, 4, 5]))

# 6 Homework 4 review 

# 6.1 Lists

def duplicateList(lst):
    duplicated = []
    for item in lst:
          duplicated.append(item)
          duplicated.append(item)
    return duplicated
# print(duplicateList(['a','b','c','c','b','c','d']))

# 6.2 Debugging
# colon is missing 
def square(num):
    return num * num

print(sumWithLoop([1, 5, 6, 2, 4, 2]))