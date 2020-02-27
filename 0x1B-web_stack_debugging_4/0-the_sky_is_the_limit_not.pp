#Change the ulimit that causes too many open files
exec { 'handle ulimit':
  command => sudo /bin/sed -i 's/15/5000/' /etc/default/nginx; sudo /usr/bin/service nginx restart
}
