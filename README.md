# <div align="center">Returned Citizen Journey</div>
## <div align="center">JTC WOW Project</div>

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
  pip install -r requirements.txt
```

Now move into the `rcjourney` directory and start the server:

```bash
  cd rcjourney
  python manage.py runserver
```

---

## Database Concerns ##

The database is not tracked by version control. Instead we can dump local data into an SQL file that can then be committed and shared across the team. This frees up each individual member to utilize test data when building. Once were ready to deploy, we can use one set of data to be exported to all the applications.

To dump the database, use the following commands:

```bash
  python manage.py dbshell
  sqlite> .output db.dump.sql
  sqlite> .dump
  sqlite> .exit
```

To create and import the data, we must first remove the existing `db.sqlite3` if any, then run the following commands:

```bash
  python manage.py dbshell
  sqlite> .read db.dump.sql
```
