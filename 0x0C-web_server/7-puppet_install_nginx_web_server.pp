# Script to install nginx using puppet

package {'nginx':
  ensure => 'present',
}

exec {'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,

}

exec {'Hello':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec {'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/blog.ehoneahobed.com\/;\\n\\t}/" /etc/nginx/sites-available/default':
  provider => shell,
}

exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}