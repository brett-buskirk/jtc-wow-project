# RC Journey #

This is the RC Journey project for the JTC WoW project.

---

## Cloning and Setting up the Project ##

First clone down the repo and then move into it with:

```bash
  cd jtc-wow-project
```

Next set up the virtual environment and load the dependencies with:

```bash
  python -m venv venv
  source venv/bin/activate
  pip install django
  pip freeze > requirements.txt
```

Now move into the `rcjourney` directory and start the server:

```bash
  cd rcjourney
  python manage.py runserver
```
