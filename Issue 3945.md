# Issue 3945: sage -gdb doesn't work under OS X 10.5

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-08-24 18:47:11

Assignee: cwitty

CC:  mhansen

It's very annoying that "sage -gdb" doesn't work under OS X 10.5.

Here's the temporary workaround I've been using when I need it:

1. Comment this in sage/all.py:

```
# We have to set this here so urllib, etc. can detect it. 
#import sage.server.notebook.gnutls_socket_ssl
#sage.server.notebook.gnutls_socket_ssl.require_SSL()
```


2. Type this:

```
sage -sh
gdb python
...
r
...
>>> from sage.all import *
```


I'm not sure how to fix this problem.  Basically any importing of anything related to ipython or the ntoebook seems to halt gdb.  Maybe there is some option to gdb to make it ignore such signals. 



---

Comment by mabshoff created at 2008-08-24 21:13:33

sage -gdb has been working for me on OSX for a long time. Every once in a while it craps out, but the next run usually works. One thing that really annoys me are all the missing debug symbol messages at startup.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-07 22:21:20

Ok, I think I am now hitting the same problem. On sage.math:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3$ ./sage -gdb
----------------------------------------------------------------------
----------------------------------------------------------------------
/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/local/bin/sage-gdb-pythonstartup
GNU gdb 6.4.90-debian
Copyright (C) 2006 Free Software Foundation, Inc.
GDB is free software, covered by the GNU General Public License, and you are
welcome to change it and/or distribute copies of it under certain conditions.
Type "show copying" to see the conditions.
There is absolutely no warranty for GDB.  Type "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu"...Using host libthread_db library "/lib/libthread_db.so.1".
| SAGE Version 3.1.3.alpha2, Release Date: 2008-09-30                |
| Type notebook() for the GUI, and license() for information.        |
[Thread debugging using libthread_db enabled]
[New Thread 46983635287904 (LWP 15466)]
Python 2.5.2 (r252:60911, Sep 30 2008, 17:45:52) 
[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2
Type "help", "copyright", "credits" or "license" for more information.

----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.3.alpha2, Release Date: 2008-09-30                |
| Type notebook() for the GUI, and license() for information.        |
Program exited normally.
(gdb) 
```

By best guess would be that this is ipython related, specifically in `local/bin/sage-gdb-pythonstartup` we have

```
from sage.all import *
import os, sys
sys.argv = ['', '-rc', os.environ['IPYTHONRC'], \
                '-c', os.environ['SAGE_STARTUP_COMMAND'] + '; banner()']
import IPython
IPython.Shell.IPShell().mainloop(sys_exit=1, banner='')
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-10-07 22:26:04

The following patchlet gets us a Python prompt, but this is obviously not the real solution:

```
diff -r cdf30964f1fe sage-gdb-pythonstartup
--- a/sage-gdb-pythonstartup    Tue Sep 30 16:55:34 2008 -0700
+++ b/sage-gdb-pythonstartup    Tue Oct 07 15:21:02 2008 -0700
`@``@` -3,5 +3,5 `@``@`
 sys.argv = ['', '-rc', os.environ['IPYTHONRC'], \
                 '-c', os.environ['SAGE_STARTUP_COMMAND'] + '; banner()']
 import IPython
-IPython.Shell.IPShell().mainloop(sys_exit=1, banner='')
+IPython.Shell.IPShell().mainloop(banner='')
```


Mike Hansen added to the CC.

Cheers,

Michael


---

Comment by mhansen created at 2008-10-12 19:01:24

Changing status from new to assigned.


---

Comment by mhansen created at 2008-10-12 19:01:24

Changing assignee from cwitty to mhansen.


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2008-10-12 20:23:39

Positive review for both patches.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-12 20:25:00

Merged in Sage 3.1.3.rc0


---

Comment by mabshoff created at 2008-10-12 20:25:00

Resolution: fixed


---

Attachment
