#!/usr/bin/env bash

# Add migrations
python manage.py migrate

# Add a door for an external commands
exec python manage.py $@
