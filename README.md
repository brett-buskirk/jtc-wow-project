# <div align="center">Returned Citizen Journey</div> #
## <div align="center">JTC WOW Project</div> ##
***
Returned Citizen Journey (RC Journey) is a MVP (minimal viable product) website built within Django, a Python web framework, that can create, read, update, and delete user data dynamically (CRUD) which will serve as a safe space for justice-impacted individuals who are returning back into society to share their experiences, make new connections, and find inspiration as they start their new journeys.
***
### <div align="center">Table of Contents</div> ###
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
### <div align="center">Developers</div> ###
- Brett Buskirk<br>
  Git Hub: https://github.com/brett-buskirk
- Kayla Ousley<br>
  Git Hub: https://github.com/KaOus22
- Joe Bollinger<br>
  Git Hub: https://github.com/joe-bollinger
- Rakesh Perani<br>
  Git Hub: https://github.com/RakeshPerani
***
### <div align="center">Installation/Technology Requirements</div> ###
RC Journey requires [Python](https://www.python.org/) v3.9+  and [Django](https://www.djangoproject.com/) to run.
***
### <div align="center">Usage</div> ###
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

##### On Windows: #####
Windows Powershell users:

```
<name-of-your-directory>/Scripts/activate.bat  or  <name-of-your-directory>/Scripts/activate.ps1
```
##### Bash users: #####
```
source <name-of-your-directory>/Scripts/activate
```
##### On Unix or MacOS: #####

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
### <div align="center">Navigating RC Journey</div> ###
#### The Landing Page is the first page of RC Journey where users can login or register. ####
![landing](https://user-images.githubusercontent.com/66227043/147306576-44e6a498-3dce-4499-8dd4-6dc9da002823.png)
#### Login Screen: ####
![login](https://user-images.githubusercontent.com/66227043/147307168-a0255bf8-471d-4fca-9f94-07c56d2ee7d7.png)
#### Register as a new user screen: ####
![register](https://user-images.githubusercontent.com/66227043/147307370-6db93844-d3b8-4a39-9094-8ad75257c8d6.png)
#### The Dashboard page is the next page the user goes to after logging in or registering as a new user. The user has the option of navigating to Forums, Listings, editing their profile, or logging out through the implementation of four buttons. ####
![dashboard](https://user-images.githubusercontent.com/66227043/147307597-f6732cf8-d090-4ac4-a250-5f0b7695bdd8.png)
#### The Forum page is where a user can create a post with tags, search through posts, and see what others have posted. Each users name is linked to their personal profile page. ####
![forum1](https://user-images.githubusercontent.com/66227043/147308135-ea1ec5f6-0011-4073-9dab-0f34411a8d08.png)
![forum2](https://user-images.githubusercontent.com/66227043/147308140-bafb09eb-69bc-4dc2-b09f-b3b7faaecbcc.png)
#### The Listings page displays all of the Returned Citizens profile pictures, bios, and the date they joined the site. The profile names are all linked to each users profile page. ####
![listings](https://user-images.githubusercontent.com/66227043/147308413-597b9fb6-389e-4a56-adf5-4d579082355d.png)
#### The Profile page can be accessed directly through the navigation bar icon, Edit Profile page, or by clicking on their name in the Forum Page or Listings page. The delete functionality is implemented on this page to allow users to delete any of their posts. ####
![profile](https://user-images.githubusercontent.com/66227043/147308776-64f0ac84-a886-4432-b1ca-996bbf287df7.png)
#### The Edit Profile page allows the user to create, update, and change their profile's bio and picture. ####
![edit-profile](https://user-images.githubusercontent.com/66227043/147309531-0a1dfc77-506f-4616-a196-78b3e45fa06b.png)
***
## <div align="center">Contributing</div>
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. 
All changes will be considered but may not be integrated.

Please make sure to update tests as appropriate.
***
### License
[MIT](https://choosealicense.com/licenses/mit/)
***
Copyright (c) 12/23/2021 Brett Buskirk, Rakesh Perani, Kayla Ousley, and Joe Bollinger
