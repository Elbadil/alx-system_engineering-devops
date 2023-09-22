# Creating a file in the directory /tmp

file {'/tmp/school':
    ensure  => file, # Ensures it's a regular file
    content => 'I love Puppet', # Content of the file
    owner   => 'www-data', # File's owner
    group   => 'www-data', # File's group owner
    mode    => '0744', # File's permissions
}
