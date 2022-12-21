# Issue 4792: Sage 3.2.1+valgrind is completely broken

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-12-14 07:37:17

Assignee: mabshoff

CC:  mhansen

Notice the following:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: P.<x,y>=ZZ[]
sage: 
Exiting SAGE (CPU time 0m0.08s, Wall time 0m4.42s).
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2$ ./sage -valgrind
----------------------------------------------------------------------
----------------------------------------------------------------------
/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2/local/bin/sage-ipython
Log file is /home/mabshoff/.sage/valgrind/sage-memcheck.%p
Using default flags:
--leak-resolution=high --leak-check=full --show-reachable=yes 
--log-file=/home/mabshoff/.sage/valgrind/sage-memcheck.%p --leak-check=full 
--num-callers=25 --suppressions=/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2/local/lib/valgrind/sage.supp
Python 2.5.2 (r252:60911, Dec 13 2008, 22:51:49) 
[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
sage: P.<x,y>=ZZ[]
------------------------------------------------------------
   File "<ipython console>", line 1
     P.<x,y>=ZZ[]
       ^
SyntaxError: invalid syntax
| Sage Version 3.2.2.alpha2, Release Date: 2008-12-13                |
| Type notebook() for the GUI, and license() for information.        |
| Sage Version 3.2.2.alpha2, Release Date: 2008-12-13                |
| Type notebook() for the GUI, and license() for information.        |
sage: 
```


I would blame the IPython fixes, but I have zero evidence so far.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-14 10:11:43

The same applies to Sage+gdb. Note:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2$ ./sage -gdb
----------------------------------------------------------------------
----------------------------------------------------------------------
/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2/local/bin/sage-ipython
GNU gdb 6.4.90-debian
Copyright (C) 2006 Free Software Foundation, Inc.
GDB is free software, covered by the GNU General Public License, and you are
welcome to change it and/or distribute copies of it under certain conditions.
Type "show copying" to see the conditions.
There is absolutely no warranty for GDB.  Type "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu"...Using host libthread_db library "/lib/libthread_db.so.1".
| Sage Version 3.2.2.alpha2, Release Date: 2008-12-13                |
| Type notebook() for the GUI, and license() for information.        |
[Thread debugging using libthread_db enabled]
[New Thread 47877213499232 (LWP 27640)]
Python 2.5.2 (r252:60911, Dec 13 2008, 22:51:49) 
[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
sage: r
No previous input matching `` found.
sage: P.<x,z>=ZZ[]
------------------------------------------------------------
   File "<ipython console>", line 1
     P.<x,z>=ZZ[]
       ^
SyntaxError: invalid syntax

sage: 

Program exited normally.
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: P.<x,z>=ZZ[]
sage: 
Exiting SAGE (CPU time 0m0.07s, Wall time 0m4.16s).
```

| Sage Version 3.2.2.alpha2, Release Date: 2008-12-13                |
| Type notebook() for the GUI, and license() for information.        |
Cheers,

Michael


---

Comment by mabshoff created at 2008-12-14 14:22:59

Ok, here is some more info: The problem stems from the way we change initialization of ipython:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.2.2.rc0$ ./sage -gdb
----------------------------------------------------------------------
----------------------------------------------------------------------
/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/local/bin/sage-ipython
GNU gdb 6.4.90-debian
Copyright (C) 2006 Free Software Foundation, Inc.
GDB is free software, covered by the GNU General Public License, and you are
welcome to change it and/or distribute copies of it under certain conditions.
Type "show copying" to see the conditions.
There is absolutely no warranty for GDB.  Type "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu"...Using host libthread_db library "/lib/libthread_db.so.1".
| Sage Version 3.2.2.alpha2, Release Date: 2008-12-13                |
| Type notebook() for the GUI, and license() for information.        |
[Thread debugging using libthread_db enabled]
[New Thread 47781974642528 (LWP 32617)]
Python 2.5.2 (r252:60911, Dec 13 2008, 09:57:26) 
[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
sage: import sage.misc.misc
sage: from sage.misc.interpreter import preparser, _ip
sage: preparser(True)
sage: import sage.all_cmdline
sage: sage.all_cmdline._init_cmdline(globals())
sage: _ip.ex('from sage.all import Integer, RealNumber')
sage: from sage.misc.interpreter import attached_files
sage: _ip.ex('from sage.all_cmdline import *')
sage: P.<x,y>=ZZ[]
sage: 
Exiting SAGE (CPU time 0m0.98s, Wall time 2m13.59s).
```

The above steps are from ipy_profile_sage.py in local/bin.

Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2008-12-14 15:10:59

Changing assignee from mabshoff to mhansen.


---

Comment by mhansen created at 2008-12-14 15:10:59

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-12-14 15:42:24

Thanks Mike, positive review. I was getting close myself, but you beat me to it :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-14 16:11:28

Resolution: fixed


---

Comment by mabshoff created at 2008-12-14 16:11:28

Merged in Sage 3.2.2.rc0
