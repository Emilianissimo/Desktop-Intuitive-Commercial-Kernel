# Desktop Intuitive Commercial Kernel

Behold! Well, this is just a simple "MVC" (kinda) PyQt5 Desktop framework.

Included:
- Authentication and sessions (db driven)
- Models + ORM
- Controllers (kinda)
- DDD oriented style (trying to be)
- Page Navigator by StackedWidget and working with router (also router with simple API)
- Pre-open page provider to interfere process until route changed (like middleware)
- Users model as example
- Multilang interface (need to be refactored, but working well)
- Nice password hashing

# Getting started

### OS Linux (Ubuntu 20.04 LTS FF (Focal Fossa/focal))
```bash
    sudo apt-get install qt5-default
```

To install qt on your system. Then just update pip requirements:

```bash
    pip3 install -r requirements.txt
```

If you're using MySQL (default), please create database and set it's name into settings/settings.py.

# Credits

Developed by me, but GPL. Use it for free and share your solutions for free as examples.
Also, you can sell it whatever, I don't care. Ofc is somebody will find this framework useful.
If you'll use it, just recognize PyQt project.

# Docs

------ Will be soon. Maybe. no, really, it's simple.

Copyrights
-
Source and Copyright of PyQt5 library - <a href="https://www.riverbankcomputing.com/software/pyqt/">PyQt5 is copyright (c) Riverbank Computing Limited</a>
SQL Connector and ORM - <a href="https://www.sqlalchemy.org/">SQLAlchemy</a>