#Automate typo from .phpp to .php
exec { 'handle typo':
  command   => '/bin/sed -i \'137s/\.phpp/\.php/\' /var/www/html/wp-settings.php'
}
