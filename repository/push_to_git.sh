#!/bin/bash

# Define the path to your project directory
project_dir="/Users/quangpham/Documents/my_project_aug_2023/project_code/main_project"

# Change to the project directory
cd "$project_dir" || exit

# Add and commit changes
git add .
git commit -m "Automated commit on $(date +'%Y-%m-%d %H:%M:%S')"
git config --global user.name "binamite"
git config --global user.email pham29239@gmail.com

# Set the remote URL to the price_comparison_website repository
git remote set-url origin 'https://github.com/binamite/price_comparison_website.git'

# Pull the latest changes from the remote "project" branch
git pull --rebase origin main
# Push your changes to the remote "project" branch
git push -f origin main