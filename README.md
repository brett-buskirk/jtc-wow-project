# <div align="center">Returned Citizen Journey</div>
## <div align="center">JTC WOW Project</div>
***
Returned Citizen Journey (RC Journey) is a website built within Django, a Python web framework, that can create, read, update, and delete user data dynamically (CRUD) which will serve as a forum for justice-impacted individuals who are returning back into society to share their experiences, make new connections, and find inspiration as they start their new journeys.
***
### <div align="center">Table of Contents</div>
- Developers
- Installation/Technology Requirements
    - Python ver. 3.9.7 or later
    - Django
- Usage
    - Create and Run Virtual Environment
    - Install Django and Create 'requirements.txt' file
    - Run the RC Journey website in the virtual environment
- Navigating RC Journey
    - Landing page
    - Register as user
    - Dashboard
    - Forum
    - Listings
    - Edit Profile
- License
- Links
***
### <div align="center">Developers</div>
- Brett Buskirk<br>
  Git Hub: https://github.com/brett-buskirk
- Kayla Ousley<br>
  Git Hub: https://github.com/KaOus22
- Joe Bollinger<br>
  Git Hub: https://github.com/joe-bollinger
- Rakesh Perani<br>
  Git Hub: https://github.com/RakeshPerani
***
### <div align="center">Installation/Technology Requirements</div>
RC Journey requires [Python](https://www.python.org/) v3.9+  and [Django](https://www.djangoproject.com/) to run.
***
### <div align="center">Usage</div>
- To run RC Journey, you will have to create a directory where you will run a virtual environment. The files for running the virtual environment will be saved in this directory:
```
mkdir <name-of-your-directory>
cd <name-of-your-directory>
```

Inside `<name-of-your-directory>` run the following:
```
python -m venv <name-of-your-virtual-environment>
```
Now, run the virtual environment:

##### On Windows:
Windows Powershell users:

```
<name-of-your-directory>/Scripts/activate.bat  or  <name-of-your-directory>/Scripts/activate.ps1
```
##### Bash users:
```
source <name-of-your-directory>/Scripts/activate
```
##### On Unix or MacOS:

```
source <name-of-your-directory>/bin/activate
```

- Install Django and create a `requirements.txt` file :
```
pip install django
```
The requirements.txt file will specify all the installed Python packages in the environment. Let's use a pip command to generate this:
```
pip freeze > requirements.txt
```

- Start your virtual environment and run the RC Journey app from the directory with manage.py in it:
```
python manage.py runserver (and follow/click on the link: http://127.0.0.1:8000/)
```
***
### <div align="center">Navigating RC Journey</div>
