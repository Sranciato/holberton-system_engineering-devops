# create a manifest that kills a process named killmenow
exec { '/killmenow' :
  command  => 'pkill killmenow',
  provider => 'shell',
  creates  => '/killmenow',
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
}