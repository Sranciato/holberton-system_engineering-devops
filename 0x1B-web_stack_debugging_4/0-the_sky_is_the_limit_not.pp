#Change the ulimit that causes too many open files
exec { 'handle ulimit':
  command => '/bin/sed -i \'s/15/1000/\' /etc/default/nginx'
}
exec { 'nginx restart':
  command => '/usr/bin/service nginx restart'
}
