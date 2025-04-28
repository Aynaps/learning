# Learning

# How To Clone this repository
Click the green Clone button on the main screen of the repository.

Select the SSH option and copy the url github gives. In your terminal
navigate to the `Code` directory and use the `git clone <url>` command
This will clone this repository on your machine and create a directory for you

Navigate to the new `learning` directory that git created for you

Example: 
```
    person@Desktop-123123$ ls
    learning ...
```
Use `cd` to move into the directory

Then use `code .` to open the code in VSCode


# Updating the repository
As you learn more material I will add more `lessons` directories for you to
test your knowledge but that means you need to update your repository on your local machine

You can update your local repository with the remote(this page) by doing the following:

Navigate to the root of the github project directory e.g. when you type `ls` you will see the `lessonsX` directories and the `README.md` file

Example: 
```
    person@Desktop-123123/learning git:(main)$ ls
    lesson1 README.md
```

Then just type `git pull` and hit enter and this will update your local repository with the remote repository
