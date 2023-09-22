# A manifest that kills a process named killmenow

exec {'killmenow':
    command => '/usr/bin/pkill -f "killmenow"', # Killing process using pkill
}   
