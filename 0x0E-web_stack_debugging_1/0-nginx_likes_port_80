#!/usr/bin/env bash
# debugging nginx port 80
# How I solved it: delete the existing ../sites-enabled/default and replace it with a copy of
# ../sites-available/default. You do that by creating a symbolic link. 
# NB: The flag -s creates a symbolic link, -f deletes the existing file and replaces it
sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
sudo service nginx restart
