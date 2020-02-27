#Change the ulimit that causes too many open files
exec { 'handle ulimit':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => "sudo sed -i 's/15/10000/g' /etc/default/nginx"; sudo service nginx restart,
}
