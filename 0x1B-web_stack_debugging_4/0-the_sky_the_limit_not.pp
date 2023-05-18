# Increases the amount of traffic an Nginx server can handle

# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
  command  => 'sed -i s/15/4096/g /etc/default/nginx',
  provider => shell
}

#restart Nginx

exec { 'nginx-restart':
  command  => 'sudo service nginx restart',
  provider => shell
}
