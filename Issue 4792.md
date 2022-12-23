# Issue 4792: Sage 3.2.1+valgrind is completely broken

archive/issues_004792.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  mhansen\n\nNotice the following:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: P.<x,y>=ZZ[]\nsage: \nExiting SAGE (CPU time 0m0.08s, Wall time 0m4.42s).\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2$ ./sage -valgrind\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2/local/bin/sage-ipython\nLog file is /home/mabshoff/.sage/valgrind/sage-memcheck.%p\nUsing default flags:\n--leak-resolution=high --leak-check=full --show-reachable=yes \n--log-file=/home/mabshoff/.sage/valgrind/sage-memcheck.%p --leak-check=full \n--num-callers=25 --suppressions=/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2/local/lib/valgrind/sage.supp\nPython 2.5.2 (r252:60911, Dec 13 2008, 22:51:49) \n[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\nsage: P.<x,y>=ZZ[]\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\n     P.<x,y>=ZZ[]\n       ^\nSyntaxError: invalid syntax\n| Sage Version 3.2.2.alpha2, Release Date: 2008-12-13                |\n| Type notebook() for the GUI, and license() for information.        |\n| Sage Version 3.2.2.alpha2, Release Date: 2008-12-13                |\n| Type notebook() for the GUI, and license() for information.        |\nsage: \n```\n\n\nI would blame the IPython fixes, but I have zero evidence so far.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4792\n\n",
    "created_at": "2008-12-14T07:37:17Z",
    "labels": [
        "packages: standard",
        "critical",
        "bug"
    ],
    "title": "Sage 3.2.1+valgrind is completely broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4792",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  mhansen

Notice the following:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: P.<x,y>=ZZ[]
sage: 
Exiting SAGE (CPU time 0m0.08s, Wall time 0m4.42s).
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2$ ./sage -valgrind
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

Issue created by migration from https://trac.sagemath.org/ticket/4792





---

archive/issue_comments_036318.json:
```json
{
    "body": "The same applies to Sage+gdb. Note:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2$ ./sage -gdb\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2/local/bin/sage-ipython\nGNU gdb 6.4.90-debian\nCopyright (C) 2006 Free Software Foundation, Inc.\nGDB is free software, covered by the GNU General Public License, and you are\nwelcome to change it and/or distribute copies of it under certain conditions.\nType \"show copying\" to see the conditions.\nThere is absolutely no warranty for GDB.  Type \"show warranty\" for details.\nThis GDB was configured as \"x86_64-linux-gnu\"...Using host libthread_db library \"/lib/libthread_db.so.1\".\n| Sage Version 3.2.2.alpha2, Release Date: 2008-12-13                |\n| Type notebook() for the GUI, and license() for information.        |\n[Thread debugging using libthread_db enabled]\n[New Thread 47877213499232 (LWP 27640)]\nPython 2.5.2 (r252:60911, Dec 13 2008, 22:51:49) \n[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\nsage: r\nNo previous input matching `` found.\nsage: P.<x,z>=ZZ[]\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\n     P.<x,z>=ZZ[]\n       ^\nSyntaxError: invalid syntax\n\nsage: \n\nProgram exited normally.\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: P.<x,z>=ZZ[]\nsage: \nExiting SAGE (CPU time 0m0.07s, Wall time 0m4.16s).\n```\n\n| Sage Version 3.2.2.alpha2, Release Date: 2008-12-13                |\n| Type notebook() for the GUI, and license() for information.        |\nCheers,\n\nMichael",
    "created_at": "2008-12-14T10:11:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4792#issuecomment-36318",
    "user": "mabshoff"
}
```

The same applies to Sage+gdb. Note:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2$ ./sage -gdb
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
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2$ ./sage
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

archive/issue_comments_036319.json:
```json
{
    "body": "Ok, here is some more info: The problem stems from the way we change initialization of ipython:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.rc0$ ./sage -gdb\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/local/bin/sage-ipython\nGNU gdb 6.4.90-debian\nCopyright (C) 2006 Free Software Foundation, Inc.\nGDB is free software, covered by the GNU General Public License, and you are\nwelcome to change it and/or distribute copies of it under certain conditions.\nType \"show copying\" to see the conditions.\nThere is absolutely no warranty for GDB.  Type \"show warranty\" for details.\nThis GDB was configured as \"x86_64-linux-gnu\"...Using host libthread_db library \"/lib/libthread_db.so.1\".\n| Sage Version 3.2.2.alpha2, Release Date: 2008-12-13                |\n| Type notebook() for the GUI, and license() for information.        |\n[Thread debugging using libthread_db enabled]\n[New Thread 47781974642528 (LWP 32617)]\nPython 2.5.2 (r252:60911, Dec 13 2008, 09:57:26) \n[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\nsage: import sage.misc.misc\nsage: from sage.misc.interpreter import preparser, _ip\nsage: preparser(True)\nsage: import sage.all_cmdline\nsage: sage.all_cmdline._init_cmdline(globals())\nsage: _ip.ex('from sage.all import Integer, RealNumber')\nsage: from sage.misc.interpreter import attached_files\nsage: _ip.ex('from sage.all_cmdline import *')\nsage: P.<x,y>=ZZ[]\nsage: \nExiting SAGE (CPU time 0m0.98s, Wall time 2m13.59s).\n```\n\nThe above steps are from ipy_profile_sage.py in local/bin.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-14T14:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4792#issuecomment-36319",
    "user": "mabshoff"
}
```

Ok, here is some more info: The problem stems from the way we change initialization of ipython:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.rc0$ ./sage -gdb
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

archive/issue_comments_036320.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-12-14T15:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4792#issuecomment-36320",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_036321.json:
```json
{
    "body": "Changing assignee from mabshoff to mhansen.",
    "created_at": "2008-12-14T15:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4792#issuecomment-36321",
    "user": "mhansen"
}
```

Changing assignee from mabshoff to mhansen.



---

archive/issue_comments_036322.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-14T15:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4792#issuecomment-36322",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036323.json:
```json
{
    "body": "Thanks Mike, positive review. I was getting close myself, but you beat me to it :)\n\nCheers,\n\nMichael",
    "created_at": "2008-12-14T15:42:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4792#issuecomment-36323",
    "user": "mabshoff"
}
```

Thanks Mike, positive review. I was getting close myself, but you beat me to it :)

Cheers,

Michael



---

archive/issue_comments_036324.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-14T16:11:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4792#issuecomment-36324",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036325.json:
```json
{
    "body": "Merged in Sage 3.2.2.rc0",
    "created_at": "2008-12-14T16:11:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4792#issuecomment-36325",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.rc0
