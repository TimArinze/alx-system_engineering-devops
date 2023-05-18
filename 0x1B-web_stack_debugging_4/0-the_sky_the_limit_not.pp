# fix nginx server of slow performance

exec { 'fixing nginx':
  command => 'sed -i s//usr/share/nginx/html//var/www/html/g /etc/nginx/sites-available/default',
  path    => '/usr/local/bin/:/bin/'
}

# restarting nginx
exec { 'nginx restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
