#Change the ulimit that causes too many open files
exec { 'handle ulimit':
  command => sudo /bin/sed -i 's/15/10000/' /etc/default/nginx; sudo /usr/sbin/service nginx restart
}
