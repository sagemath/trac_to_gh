# Issue 3594: lisp -- impossible to run command line!

archive/issues_003594.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe upgrade of clisp to 2.46 seriously broke something \n\n\n```\nage@modular:~/build/sage-3.0.4.alpha2$ ./sage -lisp\n/home2/sage/build/sage-3.0.4.alpha2/local/bin/clisp.bin: /home2/sage/build/sage-3.0.4.alpha2/local/lib/clisp/base/lisp.run: Nosuch file or directory\nsage@modular:~/build/sage-3.0.4.alpha2$ ./sage -clisp\n/home2/sage/build/sage-3.0.4.alpha2/local/bin/clisp.bin: /home2/sage/build/sage-3.0.4.alpha2/local/lib/clisp/base/lisp.run: Nosuch file or directory\nsage@modular:~/build/sage-3.0.4.alpha2$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.0.4.alpha2, Release Date: 2008-07-06                |\n| Type notebook() for the GUI, and license() for information.        |\nsage: !clisp\n/home2/sage/build/sage-3.0.4.alpha2/local/bin/clisp.bin: /home2/sage/build/sage-3.0.4.alpha2/local/lib/clisp/base/lisp.run: Nosuch file or director]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3594\n\n",
    "created_at": "2008-07-07T22:38:17Z",
    "labels": [
        "packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "lisp -- impossible to run command line!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3594",
    "user": "@williamstein"
}
```
Assignee: mabshoff

The upgrade of clisp to 2.46 seriously broke something 


```
age@modular:~/build/sage-3.0.4.alpha2$ ./sage -lisp
/home2/sage/build/sage-3.0.4.alpha2/local/bin/clisp.bin: /home2/sage/build/sage-3.0.4.alpha2/local/lib/clisp/base/lisp.run: Nosuch file or directory
sage@modular:~/build/sage-3.0.4.alpha2$ ./sage -clisp
/home2/sage/build/sage-3.0.4.alpha2/local/bin/clisp.bin: /home2/sage/build/sage-3.0.4.alpha2/local/lib/clisp/base/lisp.run: Nosuch file or directory
sage@modular:~/build/sage-3.0.4.alpha2$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.4.alpha2, Release Date: 2008-07-06                |
| Type notebook() for the GUI, and license() for information.        |
sage: !clisp
/home2/sage/build/sage-3.0.4.alpha2/local/bin/clisp.bin: /home2/sage/build/sage-3.0.4.alpha2/local/lib/clisp/base/lisp.run: Nosuch file or director]
```


Issue created by migration from https://trac.sagemath.org/ticket/3594





---

archive/issue_comments_025401.json:
```json
{
    "body": "clisp.run has moved to a different place. Updated spkg coming up. Sigh.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-07T22:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3594#issuecomment-25401",
    "user": "mabshoff"
}
```

clisp.run has moved to a different place. Updated spkg coming up. Sigh.

Cheers,

Michael



---

archive/issue_comments_025402.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-07T22:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3594#issuecomment-25402",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025403.json:
```json
{
    "body": "An updated spkg is at \n\nhttp://sage.math.washington.edu/home/mabshoff/clisp-2.46.p1.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-07-07T23:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3594#issuecomment-25403",
    "user": "mabshoff"
}
```

An updated spkg is at 

http://sage.math.washington.edu/home/mabshoff/clisp-2.46.p1.spkg

Cheers,

Michael



---

archive/issue_comments_025404.json:
```json
{
    "body": "It now actually works:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.rc0-$ ./sage -clisp\n  i i i i i i i       ooooo    o        ooooooo   ooooo   ooooo\n  I I I I I I I      8     8   8           8     8     o  8    8\n  I  \\ `+' /  I      8         8           8     8        8    8\n   \\  `-+-'  /       8         8           8      ooooo   8oooo\n    `-__|__-'        8         8           8           8  8\n        |            8     o   8           8     o     8  8\n  ------+------       ooooo    8oooooo  ooo8ooo   ooooo   8\n\nWelcome to GNU CLISP 2.46 (2008-07-02) <http://clisp.cons.org/>\n\nCopyright (c) Bruno Haible, Michael Stoll 1992, 1993\nCopyright (c) Bruno Haible, Marcus Daniels 1994-1997\nCopyright (c) Bruno Haible, Pierpaolo Bernardi, Sam Steingold 1998\nCopyright (c) Bruno Haible, Sam Steingold 1999-2000\nCopyright (c) Sam Steingold, Bruno Haible 2001-2008\n\nType :h and hit Enter for context help.\n\n[1]> (quit)\nBye.\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.rc0-$ ./sage -lisp\n  i i i i i i i       ooooo    o        ooooooo   ooooo   ooooo\n  I I I I I I I      8     8   8           8     8     o  8    8\n  I  \\ `+' /  I      8         8           8     8        8    8\n   \\  `-+-'  /       8         8           8      ooooo   8oooo\n    `-__|__-'        8         8           8           8  8\n        |            8     o   8           8     o     8  8\n  ------+------       ooooo    8oooooo  ooo8ooo   ooooo   8\n\nWelcome to GNU CLISP 2.46 (2008-07-02) <http://clisp.cons.org/>\n\nCopyright (c) Bruno Haible, Michael Stoll 1992, 1993\nCopyright (c) Bruno Haible, Marcus Daniels 1994-1997\nCopyright (c) Bruno Haible, Pierpaolo Bernardi, Sam Steingold 1998\nCopyright (c) Bruno Haible, Sam Steingold 1999-2000\nCopyright (c) Sam Steingold, Bruno Haible 2001-2008\n\nType :h and hit Enter for context help.\n\n[1]> \nBye.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-07-07T23:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3594#issuecomment-25404",
    "user": "mabshoff"
}
```

It now actually works:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.rc0-$ ./sage -clisp
  i i i i i i i       ooooo    o        ooooooo   ooooo   ooooo
  I I I I I I I      8     8   8           8     8     o  8    8
  I  \ `+' /  I      8         8           8     8        8    8
   \  `-+-'  /       8         8           8      ooooo   8oooo
    `-__|__-'        8         8           8           8  8
        |            8     o   8           8     o     8  8
  ------+------       ooooo    8oooooo  ooo8ooo   ooooo   8

Welcome to GNU CLISP 2.46 (2008-07-02) <http://clisp.cons.org/>

Copyright (c) Bruno Haible, Michael Stoll 1992, 1993
Copyright (c) Bruno Haible, Marcus Daniels 1994-1997
Copyright (c) Bruno Haible, Pierpaolo Bernardi, Sam Steingold 1998
Copyright (c) Bruno Haible, Sam Steingold 1999-2000
Copyright (c) Sam Steingold, Bruno Haible 2001-2008

Type :h and hit Enter for context help.

[1]> (quit)
Bye.
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.rc0-$ ./sage -lisp
  i i i i i i i       ooooo    o        ooooooo   ooooo   ooooo
  I I I I I I I      8     8   8           8     8     o  8    8
  I  \ `+' /  I      8         8           8     8        8    8
   \  `-+-'  /       8         8           8      ooooo   8oooo
    `-__|__-'        8         8           8           8  8
        |            8     o   8           8     o     8  8
  ------+------       ooooo    8oooooo  ooo8ooo   ooooo   8

Welcome to GNU CLISP 2.46 (2008-07-02) <http://clisp.cons.org/>

Copyright (c) Bruno Haible, Michael Stoll 1992, 1993
Copyright (c) Bruno Haible, Marcus Daniels 1994-1997
Copyright (c) Bruno Haible, Pierpaolo Bernardi, Sam Steingold 1998
Copyright (c) Bruno Haible, Sam Steingold 1999-2000
Copyright (c) Sam Steingold, Bruno Haible 2001-2008

Type :h and hit Enter for context help.

[1]> 
Bye.
```


Cheers,

Michael



---

archive/issue_comments_025405.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-08T00:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3594#issuecomment-25405",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_025406.json:
```json
{
    "body": "Merged in Sage 3.0.4.rc0",
    "created_at": "2008-07-08T00:05:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3594#issuecomment-25406",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.rc0
