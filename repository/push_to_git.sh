#!/bin/bash

# Change to your project directory
cd /Users/quangpham/Documents/my_project_aug_2023/main_project

# Add and commit changes
git add .
git commit -m "Automated commit on $(date +'%Y-%m-%d %H:%M:%S')"

# Push to the remote repository
git push origin main # Replace 'main' with your branch name if different