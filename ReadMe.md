# In-*Silico* Restriction Digest Tool

This simple program determines restriction cut sites for popular digests and returns peptides with their associated weight (in Da),
and lengths. The program allows users to filter peptide results for length, weight, and also accounts for the amount missed cleavages. Based on the ExPASy's PeptideMass software tool.

## Installation
This program runs on python 2.7 or above. Mac OS X, Sierra has python 2.7 already installed. I suggest using python 2.7 instead of 
python 3, because most extensions of flask aren't stable with the latest versions of python. A beginner tutorial of the installation of
python can be found [here](https://wiki.python.org/moin/BeginnersGuide/Download). 

### Virtual environment for development
In order to avoid compatability issues between different libraries for different projects, it is important to use a virtual environment.

Run the following command on the command prompt/terminal:
```
pip install virtualenv
```
Add sudo before pip on Linux/Mac OS. This will install the virtual environment under the C:/pythonX/scripts path, where X is the version 
of your python. If on windows, log in as administrator. On ubuntu:
```
sudo apt-get install python-virtualenv
```
Once installed, create a directory for your project, and run:
```
virtualenv venv
```
This sets up an virtual environment folder in your project directory. From there you can activate the virtual environment.

For Linux/Mac OS:
```
venv/bin/activate
```

For Windows:
```
venv\scripts\activate
```

Install Flask in this environment using the following command:
```
pip install Flask
```
After obtaining this repository, execute:
```
python digest.py
```
This runs the program that allows you to access the front page through any internet browser (chrome, firefox, safari, etc.).

## Future directions for this project
- Fixing the input form for protein sequences, to be case in sensitive.
- Adding FASTA file upload capability.
- Convert functionality of the program to classes and methods.
- Add more restriction enzymes to this program.
- Improve aesthetic of HTML and CSS of home page.
- Add this program to be hosted on web server.

## Contact Information

If there are any questions about this project, feel free to contact me:
Email - wongak626@gmail.com
