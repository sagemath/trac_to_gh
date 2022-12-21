# Issue 6375: Run sage once as part of install process to generate sage-flags.txt

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2009-06-20 20:53:26

Assignee: tbd

When sage runs for the first time, it creates a file `sage-flags.txt` to keep track of what special instructions the CPU supports. Several people have run into trouble compiling and installing sage as root, and then running it as a normal user, because they don't have permission to create the file. Here's such a traceback:


```
Traceback (most recent call last):
  File "/usr/local/sage-4.0.2/local/bin/sage-location", line 174, in <module>
    t, R = install_moved()
  File "/usr/local/sage-4.0.2/local/bin/sage-location", line 18, in install_moved
    write_flags_file()
  File "/usr/local/sage-4.0.2/local/bin/sage-location", line 82, in write_flags_file
    open(flags_file,'w').write(get_flags_info())
IOError: [Errno 13] Permission denied: '/usr/local/sage-4.0.2/local/lib/sage-flags.txt'
```


It would seem sensible to run `local/bin/sage-starts` once during the install process to create this file.


---

Comment by jdemeyer created at 2012-04-02 15:46:37

Duplicate of #11926.


---

Comment by jdemeyer created at 2012-04-02 15:46:37

Resolution: duplicate
