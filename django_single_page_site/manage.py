#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eng30.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


#TB Some comments about running manage.py:

# python manage.py migrate 
# create db

# While the web server is running, you won't see a new command-line prompt to enter additonal commands. 
#The terminal will accept new text but will not execute new commands. This is because the web server 
#continuously runs in order to listen for incoming requests.

# Django prepared a migration file for us that we now have to apply to our database. Type python manage.py migrate blog and the output should be as follows: