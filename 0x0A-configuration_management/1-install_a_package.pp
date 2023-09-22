# Installing flask from pip3 using Puppet

package {'flask':
    ensure   => '2.1.0', # Flask's version
    provider => 'pip3', # Package manager
}
