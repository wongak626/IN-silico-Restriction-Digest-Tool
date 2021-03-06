# In-*Silico* Restriction Digest Tool

This simple program determines restriction cut sites on user inputted protein sequeqnces for many different restriction enzymes and returns digested peptides with their associated weight (in Da),and lengths (in amino acids). The program allows users to filter peptide results for length, weight, and also accounts for the amount of missed cleavages. Based on the ExPASy's PeptideMass software tool.

## Installation
This program runs on python 2.7 or above (https://wiki.python.org/moin/BeginnersGuide/Download). This program also uses the Flask micro-webframework, and will need to be run in an virtual environment.

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
After obtaining this repository, go into the project directory and execute:
```
python digest.py
```
This inititates the program, and allows you to access the front page through any internet browser (chrome, firefox, safari, etc.).

## Deployment
This web application has not been successfully deployed.

## Testing
Currently, users are only allowed to copy and paste AA sequences into a webform for this project. I have included a sample AA sequence in the form of a fasta file to be used as a test case for this project: ALPHA_CRYSTALLIN.fasta.

## Future directions for this project
- Adding FASTA file upload capability.
- Convert functionality of the program to classes and methods.
- Add more restriction enzymes to this program.
- Improve aesthetic of HTML and CSS of home page.
- Add this program to be hosted on web server.
- Add quality check/ form validators

## Contact Information

Feel free to contact me:
Email - wongak626@gmail.com
