# change config file lines
file_line {
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}
file_line {
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
}
