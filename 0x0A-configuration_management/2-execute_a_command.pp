# A manifest that kills a process named killmenow

exec {'kill_a_process':
    command => '/usr/bin/pkill -f "killmenow"', # Killing process using pkill
}   