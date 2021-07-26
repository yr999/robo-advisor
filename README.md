# robo-advisor

This Python application automates the process of providing my clients with stock trading recommendations. It accepts one or more stock or cryptocurrency symbols as information inputs, then it requests real live historical trading data from the internet, and finally provides a recommendation as the whether or not the client should purchase the given stocks or cryptocurrencies. 

Prerequisites

Anaconda 3.7+
Python 3.7+
Pip
Installation

Fork this remote repository under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

cd ~GitHub/robo-advisor
You can also navigate to the directory by clicking "Repository" and "Open in Terminal" from GitHub Desktop upon dowloading the copy of the application.

Use Anaconda to create and activate a new virtual environment, perhaps called "stocks-env":

conda create -n stocks-env python=3.8
conda activate stocks-env
After activating the virtual environment, install package dependencies (see the "requirements.txt" file):

pip install -r requirements.txt
NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial cd step above).
Setup

In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username (then make sure to SAVE the ".env" file aftwards):

ALPHAVANTAGE_API_KEY="abc123"
NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the ".gitignore" file). This means we need to instruct each person who uses our code needs to create their own local ".env" file. 

The ".gitignore" file generated during the GitHub repo creation process should already do this, otherwise you can create your own ".gitignore" file and place inside the following contents:

#this is the ".gitignore" file

#ignore secret environment variable values in the ".env" file:
.env

Ensure to create .env file before creating .gitignore file.

Usage

Run the Python script:

python robo_advisor.py

# alternative module-style invocation (only required if importing from one file to another):
python -m robo_advisor.py
NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the pip command above to ensure that package has been installed into the virtual environment.