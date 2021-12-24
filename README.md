# Returned Citizen Journey #

## JTC WOW Project ##

---

Returned Citizen Journey (RC Journey) is a MVP (minimal viable product) website built within Django, a Python web framework, that can create, read, update, and delete user data dynamically (CRUD) which will serve as a safe space for justice-impacted individuals who are returning back into society to share their experiences, make new connections, and find inspiration as they start their new journeys.

---

- [Returned Citizen Journey](#returned-citizen-journey)
  - [JTC WOW Project](#jtc-wow-project)
  - [Developers](#developers)
  - [Requirements](#requirements)
  - [Usage](#usage)
    - [On Windows](#on-windows)
    - [Bash Users](#bash-users)
    - [On Unix or MacOS](#on-unix-or-macos)
  - [Navigating RC Journey](#navigating-rc-journey)
    - [The Landing Page](#the-landing-page)
    - [The Login Page](#the-login-page)
    - [The Register Page](#the-register-page)
    - [The Dashboard Page](#the-dashboard-page)
    - [The Forum Page](#the-forum-page)
    - [The Listings Page](#the-listings-page)
    - [The Profile Page](#the-profile-page)
    - [The Edit Profile Page](#the-edit-profile-page)
  - [Contributing](#contributing)
  - [License](#license)
  
---

## Developers ##

- [Brett Buskirk](https://github.com/brett-buskirk)
- [Kayla Ousley](https://github.com/KaOus22)
- [Joe Bollinger](https://github.com/joe-bollinger)
- [Rakesh Perani](https://github.com/RakeshPerani)

---

## Requirements ##

RC Journey requires [Python](https://www.python.org/) v3.9+  and [Django](https://www.djangoproject.com/) to run.

---

## Usage ##

To run RC Journey, you will have to clone the project and run a virtual environment. After cloning the project, navigate to the project's root directory and run the following:

```bash
    python -m venv venv
```

Now, run the virtual environment:

### On Windows ###

Windows Powershell users:

```bash
    venv/Scripts/activate.bat  or  venv/Scripts/activate.ps1
```

### Bash Users ###

```bash
    source venv/Scripts/activate
```

### On Unix or MacOS ###

```bash
    source venv/bin/activate
```

The requirements.txt file will specify all the installed Python packages in the environment. Let's use a pip command to generate this:

```bash
    pip install -r requirements.txt
```

Start your virtual environment and run the RC Journey app from the directory with manage.py in it:

```bash
    cd rcjourney
    python manage.py runserver
```

Now open a browser tab and navigate to [localhost:8000](http://localhost:8000)

---

## Navigating RC Journey ##

### The Landing Page ###

This is the first page of RC Journey, where users can choose to login or register an account.

![landing](https://user-images.githubusercontent.com/66227043/147306576-44e6a498-3dce-4499-8dd4-6dc9da002823.png)

### The Login Page ###

![login](https://user-images.githubusercontent.com/66227043/147307168-a0255bf8-471d-4fca-9f94-07c56d2ee7d7.png)

### The Register Page ###

![register](https://user-images.githubusercontent.com/66227043/147307370-6db93844-d3b8-4a39-9094-8ad75257c8d6.png)

### The Dashboard Page ###

This is the next page the user goes to after logging in or registering as a new user. The user has the option of navigating to Forums, Listings, editing their profile, or logging out through the implementation of four buttons

![dashboard](https://user-images.githubusercontent.com/66227043/147307597-f6732cf8-d090-4ac4-a250-5f0b7695bdd8.png)

### The Forum Page ###

This is where a user can create a post with tags, search through posts, and see what others have posted. Each users name is linked to their personal profile page.

![forum1](https://user-images.githubusercontent.com/66227043/147308135-ea1ec5f6-0011-4073-9dab-0f34411a8d08.png)
![forum2](https://user-images.githubusercontent.com/66227043/147308140-bafb09eb-69bc-4dc2-b09f-b3b7faaecbcc.png)

### The Listings Page ###

This page displays all of the Returned Citizens profile pictures, bios, and the date they joined the site. The profile names are all linked to each users profile page.

![listings](https://user-images.githubusercontent.com/66227043/147308413-597b9fb6-389e-4a56-adf5-4d579082355d.png)

### The Profile Page ###

This page can be accessed directly through the navigation bar icon, Edit Profile page, or by clicking on their name in the Forum Page or Listings page. The delete functionality is implemented on this page to allow users to delete any of their posts.

![profile](https://user-images.githubusercontent.com/66227043/147308776-64f0ac84-a886-4432-b1ca-996bbf287df7.png)

### The Edit Profile Page ###

This page allows the user to create, update, and change their profile's bio and picture.

![edit-profile](https://user-images.githubusercontent.com/66227043/147309531-0a1dfc77-506f-4616-a196-78b3e45fa06b.png)

---

## Contributing ##

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

All changes will be considered but may not be integrated.

Please make sure to update tests as appropriate.

---

## License ##

[MIT](https://choosealicense.com/licenses/mit/)

---

Copyright (c) 12/23/2021 Brett Buskirk, Rakesh Perani, Kayla Ousley, and Joe Bollinger
