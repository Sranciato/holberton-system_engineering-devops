# change config file lines

file_line {
  ensure => present,
  path   => '/etc/ssh/ssh_config'
  line   => '\tPasswordAuthentication no'
}
file_line {
  ensure => present,
  path => '/etc/ssh/ssh_config'
  line => '\tIdentityFile ~/.ssh/holberton'
}