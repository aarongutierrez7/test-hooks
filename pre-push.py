#!/usr/bin/env python

import subprocess
import re
import sys

def run_git_command(command, repo_directory):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True, cwd=repo_directory)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        return None
    
def check_files_presence(diff_output):
    #pattern = r'(\S+)\s*\|'
    pattern = r'(\S+)\s*\|\s*(?!0)\d+'


    # Use re.findall to find all matches in the input string
    matches = re.findall(pattern, diff_output)

    # Remove leading/trailing spaces and append to the array
    file_names = [match.strip() for match in matches]

    return file_names

# Specify the repository directory
repo_dir = "C:/Users/aaron/Desktop/test-git"
mandatory_files = ["file1.txt", "file2.txt", "file3.txt"]


# Run the git diff command in the specified directory
git_command = ["git", "diff", "--stat", "--cached", "origin/master"]
command_output = run_git_command(git_command, repo_dir)
files_arr = check_files_presence(command_output)
print(files_arr)

for file_to_check in mandatory_files:
        if file_to_check not in files_arr:
            print('EXITING 1: Some files need to be modified')
            print(sys.exit(1))
print("EXITING 0: All OK")
print(sys.exit(0))



