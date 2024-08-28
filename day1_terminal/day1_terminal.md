### **Day 1: Terminal Basics**

Walk through day, learning how to use the terminal, and how to use it in VSCode.

1. **Introduction to the Terminal**
   - **What is the Terminal?**
     - Brief explanation of the terminal as a text-based interface for interacting with the operating system.
   - **Opening the Terminal**
     - How to open the terminal on different operating systems (e.g., macOS, Linux).
   - **Basic Command Syntax**
     - Structure of a command: command, options, and arguments.
     - `command --option argument`
     - EX: `cp -r old_folder new_folder`

2. **Navigating the File System**
   - **pwd (Print Working Directory)**
     - Understanding the current location in the file system.
   - **ls (List)**
     - Listing files and directories in the current directory.
   - **cd (Change Directory)**
     - Moving between directories.
   - **mkdir (Make Directory)**
     - Creating new directories.
   - **Relative vs Absolute paths**
	   - Relative: `folder` vs `./folder` vs `~/folder` 
	   - Abs: `/Users/zackmawaldi/folder`


3. **File Operations**
   - **touch**
     - Creating an empty file.
   - **cat, head, tail**
     - Viewing file contents:
       - `cat`: Display the entire file.
       - `head`: Display the first few lines of a file.
       - `tail`: Display the last few lines of a file.
	       - `head` and `tail` with `-n` specifies number of lines:
	       - `head -n 20 notes.txt` displays top 20 lines of `notes.txt`
   - **cp, mv, rm**
     - Copying, moving, and deleting files:
       - `cp`: Copy files and directories.
       - `mv`: Move or rename files and directories.
       - `rm`: Remove files (with caution).
	       - Flag `-r` allows for `cp` and `rm` of folders

4. **Text Editing**
   - **Introduction to vim**
	   - Opening a file in vim. `vim file.txt`
	   - Basic navigation in vim (insert mode, normal mode).
	   - Saving (`:w`), exiting (`:q`), and save and exit in vim (`:wq`). Forceful action with `!` ex: `:q!`

5. **Piping and Redirection**
   - **Basic Piping (`|`)**
     - Combine commands using the pipe symbol to send the output of one command as input to another (e.g., `ls | grep "txt"` or `ls | wc -l`).
   - **Redirection (`>`, `>>`)**
     - Redirecting command output to a file:
       - `>`: Overwrite a file with the command output.
       - `>>`: Append command output to the end of a file.

6. **Scripting Basics**
   - **Introduction to Bash Scripting**
     - What is a bash script? How does it differ from typing commands manually?
   - **Creating a Simple Bash Script**
     - Create a basic bash script (`hello.sh`) to automate a sequence of commands.
     - Explain how to make a script executable (`chmod +x hello.sh`).
     - `#!/bin/bash`
   - **Running the Bash Script**
     - Execute the script from the terminal.



### **If time allows, if not let's do next class:**
- Download [VSCode](https://code.visualstudio.com)
- Download Miniconda (if not installed already)
```shell
# Downlaod miniconda installer:
wget -O ./miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Then run the installer:
bash ./miniconda.sh
```

We'll touch more on these downloads next class :)