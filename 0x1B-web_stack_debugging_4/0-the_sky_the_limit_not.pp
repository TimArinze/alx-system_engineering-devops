# fix nginx server of slow performance

exec { 'fixing nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# restarting nginx
exec { 'nginx restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
