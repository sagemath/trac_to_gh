# Issue 1752: sage make install bug

Issue created by migration from Trac.

Original creator: pgrinber

Original creation time: 2008-01-10 22:14:38

Assignee: cwitty

When calling 

```
DESTDIR=$sagedir make install
```

the following library files will be created with 555 permissions. When causes problems when trying to strip those files. To change that, deliver the files with 755 permissions.

$sagedir/sage/local/lib/libhistory.so.*
$sagedir/sage/local/lib/libreadline.so.*


---

Comment by mabshoff created at 2008-01-10 22:26:39

Hi Paul,

you should assign a milestone for each ticket you open. The next milestone is usually a good default. Same for #1753.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-11 19:00:53

Changing assignee from cwitty to mabshoff.


---

Comment by mabshoff created at 2008-01-11 19:00:53

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-01-11 19:00:53

The updated spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha2/readline-5.2.p0.spkg

fixes the issue.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-11 19:17:49

It looks like the issue itself is in the original readline install process. I will investigate this.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-11 19:21:01

Merged in Sage 2.10.alpha2.


---

Comment by mabshoff created at 2008-01-11 19:21:01

Resolution: fixed
