# Issue 3945: sage -gdb doesn't work under OS X 10.5

archive/issues_003945.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  mhansen\n\nIt's very annoying that \"sage -gdb\" doesn't work under OS X 10.5.\n\nHere's the temporary workaround I've been using when I need it:\n\n1. Comment this in sage/all.py:\n\n```\n# We have to set this here so urllib, etc. can detect it. \n#import sage.server.notebook.gnutls_socket_ssl\n#sage.server.notebook.gnutls_socket_ssl.require_SSL()\n```\n\n\n2. Type this:\n\n```\nsage -sh\ngdb python\n...\nr\n...\n>>> from sage.all import *\n```\n\n\nI'm not sure how to fix this problem.  Basically any importing of anything related to ipython or the ntoebook seems to halt gdb.  Maybe there is some option to gdb to make it ignore such signals. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3945\n\n",
    "created_at": "2008-08-24T18:47:11Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "sage -gdb doesn't work under OS X 10.5",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3945",
    "user": "was"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/3945





---

archive/issue_comments_028318.json:
```json
{
    "body": "sage -gdb has been working for me on OSX for a long time. Every once in a while it craps out, but the next run usually works. One thing that really annoys me are all the missing debug symbol messages at startup.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-24T21:13:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3945#issuecomment-28318",
    "user": "mabshoff"
}
```

sage -gdb has been working for me on OSX for a long time. Every once in a while it craps out, but the next run usually works. One thing that really annoys me are all the missing debug symbol messages at startup.

Cheers,

Michael



---

archive/issue_comments_028319.json:
```json
{
    "body": "Ok, I think I am now hitting the same problem. On sage.math:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3$ ./sage -gdb\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/local/bin/sage-gdb-pythonstartup\nGNU gdb 6.4.90-debian\nCopyright (C) 2006 Free Software Foundation, Inc.\nGDB is free software, covered by the GNU General Public License, and you are\nwelcome to change it and/or distribute copies of it under certain conditions.\nType \"show copying\" to see the conditions.\nThere is absolutely no warranty for GDB.  Type \"show warranty\" for details.\nThis GDB was configured as \"x86_64-linux-gnu\"...Using host libthread_db library \"/lib/libthread_db.so.1\".\n| SAGE Version 3.1.3.alpha2, Release Date: 2008-09-30                |\n| Type notebook() for the GUI, and license() for information.        |\n[Thread debugging using libthread_db enabled]\n[New Thread 46983635287904 (LWP 15466)]\nPython 2.5.2 (r252:60911, Sep 30 2008, 17:45:52) \n[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\n\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.1.3.alpha2, Release Date: 2008-09-30                |\n| Type notebook() for the GUI, and license() for information.        |\nProgram exited normally.\n(gdb) \n```\n\nBy best guess would be that this is ipython related, specifically in `local/bin/sage-gdb-pythonstartup` we have\n\n```\nfrom sage.all import *\nimport os, sys\nsys.argv = ['', '-rc', os.environ['IPYTHONRC'], \\\n                '-c', os.environ['SAGE_STARTUP_COMMAND'] + '; banner()']\nimport IPython\nIPython.Shell.IPShell().mainloop(sys_exit=1, banner='')\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-10-07T22:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3945#issuecomment-28319",
    "user": "mabshoff"
}
```

Ok, I think I am now hitting the same problem. On sage.math:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3$ ./sage -gdb
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

archive/issue_comments_028320.json:
```json
{
    "body": "The following patchlet gets us a Python prompt, but this is obviously not the real solution:\n\n```\ndiff -r cdf30964f1fe sage-gdb-pythonstartup\n--- a/sage-gdb-pythonstartup    Tue Sep 30 16:55:34 2008 -0700\n+++ b/sage-gdb-pythonstartup    Tue Oct 07 15:21:02 2008 -0700\n@@ -3,5 +3,5 @@\n sys.argv = ['', '-rc', os.environ['IPYTHONRC'], \\\n                 '-c', os.environ['SAGE_STARTUP_COMMAND'] + '; banner()']\n import IPython\n-IPython.Shell.IPShell().mainloop(sys_exit=1, banner='')\n+IPython.Shell.IPShell().mainloop(banner='')\n```\n\n\nMike Hansen added to the CC.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-07T22:26:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3945#issuecomment-28320",
    "user": "mabshoff"
}
```

The following patchlet gets us a Python prompt, but this is obviously not the real solution:

```
diff -r cdf30964f1fe sage-gdb-pythonstartup
--- a/sage-gdb-pythonstartup    Tue Sep 30 16:55:34 2008 -0700
+++ b/sage-gdb-pythonstartup    Tue Oct 07 15:21:02 2008 -0700
@@ -3,5 +3,5 @@
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

archive/issue_comments_028321.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-12T19:01:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3945#issuecomment-28321",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_028322.json:
```json
{
    "body": "Changing assignee from cwitty to mhansen.",
    "created_at": "2008-10-12T19:01:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3945#issuecomment-28322",
    "user": "mhansen"
}
```

Changing assignee from cwitty to mhansen.



---

archive/issue_comments_028323.json:
```json
{
    "body": "Attachment [trac_3945.patch](tarball://root/attachments/some-uuid/ticket3945/trac_3945.patch) by mhansen created at 2008-10-12 19:01:24",
    "created_at": "2008-10-12T19:01:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3945#issuecomment-28323",
    "user": "mhansen"
}
```

Attachment [trac_3945.patch](tarball://root/attachments/some-uuid/ticket3945/trac_3945.patch) by mhansen created at 2008-10-12 19:01:24



---

archive/issue_comments_028324.json:
```json
{
    "body": "Attachment [trac_3945-2.patch](tarball://root/attachments/some-uuid/ticket3945/trac_3945-2.patch) by mhansen created at 2008-10-12 20:12:57",
    "created_at": "2008-10-12T20:12:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3945#issuecomment-28324",
    "user": "mhansen"
}
```

Attachment [trac_3945-2.patch](tarball://root/attachments/some-uuid/ticket3945/trac_3945-2.patch) by mhansen created at 2008-10-12 20:12:57



---

archive/issue_comments_028325.json:
```json
{
    "body": "Positive review for both patches.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-12T20:23:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3945#issuecomment-28325",
    "user": "mabshoff"
}
```

Positive review for both patches.

Cheers,

Michael



---

archive/issue_comments_028326.json:
```json
{
    "body": "Merged in Sage 3.1.3.rc0",
    "created_at": "2008-10-12T20:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3945#issuecomment-28326",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.rc0



---

archive/issue_comments_028327.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-12T20:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3945#issuecomment-28327",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028328.json:
```json
{
    "body": "Attachment [trac_3945-3.patch](tarball://root/attachments/some-uuid/ticket3945/trac_3945-3.patch) by mhansen created at 2008-10-12 23:02:03",
    "created_at": "2008-10-12T23:02:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3945#issuecomment-28328",
    "user": "mhansen"
}
```

Attachment [trac_3945-3.patch](tarball://root/attachments/some-uuid/ticket3945/trac_3945-3.patch) by mhansen created at 2008-10-12 23:02:03
