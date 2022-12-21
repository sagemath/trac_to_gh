# Issue 3122: after make install, sage tries to write in /usr/local

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2008-05-07 12:46:05

Assignee: cwitty

I compiled sage-3.0 on the machines of my lab, and installed it under /usr/local/sage-3.0 with make install DESTDIR=/usr/local/sage-3.0.
I am the Unix owner of the files under /usr/local/sage-3.0. When I run sage myself, it is ok. However, when other people in my lab run it, they get:

```
< bissogae`@`hector:~$ sage
< ----------------------------------------------------------------------
< | SAGE Version 3.0, Release Date: 2008-04-23                         |
< | Type notebook() for the GUI, and license() for information.        |
< ----------------------------------------------------------------------
< Traceback (most recent call last):
<   File "/usr/local/sage-3.0/sage/local/bin/sage-location", line 66, in <module>
<     t, R = install_moved()
<   File "/usr/local/sage-3.0/sage/local/bin/sage-location", line 11, in install_moved
<     O = open(location_file,'w')
< IOError: [Errno 13] Permission denied: '/usr/local/sage-3.0/sage/local/lib/sage-current-location.txt'
<
< sage:
```

I'm not sure it is ok that SAGE writes in /usr/local...


---

Comment by mabshoff created at 2008-05-07 12:51:07

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-05-07 12:51:07

Changing priority from minor to blocker.


---

Comment by mabshoff created at 2008-05-07 12:51:07

Hi Paul,

I am curious if you started Sage after running "make install". Starting Sage once after running the make install is needed so that the pyc files are recreated. After that Sage should not need to have write access to anything outside `~/.sage`. So I consider this a blocker. We must make the deployment of Sage as simple as possible and this includes having Sage in multi user environments.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-07 12:51:07

Changing assignee from cwitty to mabshoff.


---

Comment by malb created at 2008-08-16 23:48:21

It seems the touching /usr/local is caused by the "Sage moved" script, so I assume that the best "fix" is to print a better error message?


---

Comment by mabshoff created at 2008-09-15 04:49:02

I agree this issue seems closely related to #1830. So fixing this issue will also likely solve that ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-01 08:44:39

This patch is to the main makefile and is a classic patch, i.e. no hg here


---

Attachment

The hopefully final patch for 3.2.1.rc1 :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-01 08:54:34

Resolution: fixed


---

Comment by mabshoff created at 2008-12-01 08:54:34

Merged in Sage 3.2.1.rc1


---

Comment by mabshoff created at 2008-12-01 09:30:24

Looking at the problem again it seems that there might be another problem here. Several possibilities

 * other people ran sage before Paul did, hence sage-location was executed. We fixed that bug
 * somebody else has mounted the directory with sage in a different location than Paul in which case sage_location will cause the above error. There is nothing we can do in that case since the pyc files have to be recreated

Paul: If this is still a problem please let us know and open a new ticket with specific steps to reproduce and plenty of information.

Cheers,

Michael
