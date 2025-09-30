import os
import csv

from git import Repo
from dataclasses import dataclass

print("Would you like to Clone Repos (Y/N)?")
cloneRepoInput = input()

inputFile = open("./Input/VR_Project_List.txt")
lines = inputFile.readlines()

commitList = []

if(cloneRepoInput == "Y" or cloneRepoInput == "y"):

    print(f"Cloning {len(lines)} Repositories")
    for line in lines:
        line = line.replace("\n", "")
        currentRepoURL = line
        currentRepoName = currentRepoURL.split(".git")[0].split('/')[-1]
        print(f"Cloning {currentRepoName}...")
        try:
            Repo.clone_from(currentRepoURL, f"./Repos/{currentRepoName}/")
            print(f"Cloned {currentRepoName} Successfully")
        except:
            print(f"Error Cloning {currentRepoName}")

print("Analyzing Repositories")

for folder in next(os.walk('./Repos/'))[1]:
    print(f"Reading {folder}...")
    repo  = Repo(f"./Repos/{folder}")
    all_commits = list(repo.iter_commits(repo.active_branch))
    for commit in all_commits:

        print(f"Reading Commit {commit} in repo {folder}")

        if ("performance" in commit.message.lower() or
            "speed up" in commit.message.lower() or
            "accelerate" in commit.message.lower() or
            "fast" in commit.message.lower() or
            "slow" in commit.message.lower() or
            "latency" in commit.message.lower() or
            "contention" in commit.message.lower() or
            "optimize" in commit.message.lower() or
            "efficiency" in commit.message.lower()
            ):

            commitData = {"Repo":folder, "Message":commit.message, "Commit":commit}
            commitList.append(commitData)

with open('./Output/Result.csv', 'w') as f:
    fieldNames = ["Repo", "Message", "Commit"]
    writer = csv.DictWriter(f, fieldnames=fieldNames)
    writer.writeheader()
    writer.writerows(commitList)


