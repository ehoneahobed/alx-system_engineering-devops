#!/usr/bin/env bash
#Configure your Nginx server to have a custom 404 page that contains the string

sudo apt-get update
sudo apt-get install -y nginx

# code to redirect a specific endpoint (eg: redirect /redirect_me to https://blog.ehoneahobed.com)
echo "Hello World!" | sudo tee /var/www/html/index.html
string_for_replacement="server_name _;\n\trewrite ^\/redirect_me https:\/\/www.blog.ehoneahobed.com permanent;"
sudo sed -i "s/server_name _;/$string_for_replacement/" /etc/nginx/sites-enabled/default

# code to create error page and add a redirect for error 404
echo "Ceci n'est pas une page" | sudo tee /var/www/html/404.html
string_for_replacement="listen 80 default_server;\n\terror_page 404 \/404.html;\n\tlocation = \/404.html {\n\t\troot \/var\/www\/html;\n\t\tinternal;\n\t}"
sudo sed -i "s/listen 80 default_server;/$string_for_replacement/" /etc/nginx/sites-enabled/default

# restart the server
sudo service nginx restart
