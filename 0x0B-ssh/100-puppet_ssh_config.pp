# Client Configuration file with Puppet
include stdlib
file_line { 'set_ssh_rsa__private_key':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
}

file_line { 'disable_psswd_authentication':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
}
