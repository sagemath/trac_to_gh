# Issue 2710: bug -- !singular doesn't work anymore on OS X

archive/issues_002710.json:
```json
{
    "body": "Assignee: @williamstein\n\nOn OS X, `!singular` no longer works.  It works fine on Linux still. \n\n\n```\nLast login: Fri Mar 28 12:02:34 on ttys001\nD-69-91-159-150:~ was$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading SAGE library. Current Mercurial branch is: modabvar\n| SAGE Version 2.10.4, Release Date: 2008-03-16                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: !singular\ndyld: Library not loaded: libntl.dylib\n  Referenced from: /Users/was/build/sage-2.10.4/local/bin/Singular-3-0-4\n  Reason: image not found\n/Users/was/build/sage-2.10.4/local/bin/singular: line 2:   408 Trace/BPT trap          Singular-3-0-4 $*\nsage: \n```\n\n\nNote that singular.console() does work:\n\n```\nsage: singular.console()\n                     SINGULAR                             /  Development\n A Computer Algebra System for Polynomial Computations   /   version 3-0-4\n                                                       0<\n     by: G.-M. Greuel, G. Pfister, H. Schoenemann        \\   Nov 2007\nFB Mathematik der Universitaet, D-67653 Kaiserslautern    \\\n> Auf Wiedersehen.\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2710\n\n",
    "created_at": "2008-03-28T21:32:17Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "bug -- !singular doesn't work anymore on OS X",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2710",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

On OS X, `!singular` no longer works.  It works fine on Linux still. 


```
Last login: Fri Mar 28 12:02:34 on ttys001
D-69-91-159-150:~ was$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: modabvar
| SAGE Version 2.10.4, Release Date: 2008-03-16                      |
| Type notebook() for the GUI, and license() for information.        |
sage: !singular
dyld: Library not loaded: libntl.dylib
  Referenced from: /Users/was/build/sage-2.10.4/local/bin/Singular-3-0-4
  Reason: image not found
/Users/was/build/sage-2.10.4/local/bin/singular: line 2:   408 Trace/BPT trap          Singular-3-0-4 $*
sage: 
```


Note that singular.console() does work:

```
sage: singular.console()
                     SINGULAR                             /  Development
 A Computer Algebra System for Polynomial Computations   /   version 3-0-4
                                                       0<
     by: G.-M. Greuel, G. Pfister, H. Schoenemann        \   Nov 2007
FB Mathematik der Universitaet, D-67653 Kaiserslautern    \
> Auf Wiedersehen.
```



Issue created by migration from https://trac.sagemath.org/ticket/2710





---

archive/issue_comments_018652.json:
```json
{
    "body": "The link mode for NTL on OSX is more than odd:\n\n```\nbsd:sage-2.11.alpha1-32bit mabshoff$ otool -L local/bin/Singular-3-0-4\nlocal/bin/Singular-3-0-4:\n        /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 111.0.0)\n        libntl.dylib (compatibility version 0.0.0, current version 0.0.0)\n        /Users/mabshoff/sage-2.11.alpha1-32bit/local/lib/libgmp.3.dylib (compatibility version 8.0.0, current version 8.1.0)\n        /Users/mabshoff/sage-2.11.alpha1-32bit/local/lib/libreadline.5.2.dylib (compatibility version 5.0.0, current version 5.2.0)\n        /usr/lib/libncurses.5.4.dylib (compatibility version 5.4.0, current version 5.4.0)\n        /usr/lib/libstdc++.6.dylib (compatibility version 7.0.0, current version 7.4.0)\n        /usr/lib/libgcc_s.1.dylib (compatibility version 1.0.0, current version 1.0.0)\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-03-28T21:44:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2710#issuecomment-18652",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The link mode for NTL on OSX is more than odd:

```
bsd:sage-2.11.alpha1-32bit mabshoff$ otool -L local/bin/Singular-3-0-4
local/bin/Singular-3-0-4:
        /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 111.0.0)
        libntl.dylib (compatibility version 0.0.0, current version 0.0.0)
        /Users/mabshoff/sage-2.11.alpha1-32bit/local/lib/libgmp.3.dylib (compatibility version 8.0.0, current version 8.1.0)
        /Users/mabshoff/sage-2.11.alpha1-32bit/local/lib/libreadline.5.2.dylib (compatibility version 5.0.0, current version 5.2.0)
        /usr/lib/libncurses.5.4.dylib (compatibility version 5.4.0, current version 5.4.0)
        /usr/lib/libstdc++.6.dylib (compatibility version 7.0.0, current version 7.4.0)
        /usr/lib/libgcc_s.1.dylib (compatibility version 1.0.0, current version 1.0.0)
```


Cheers,

Michael



---

archive/issue_comments_018653.json:
```json
{
    "body": "This has been fixed for me:\n\n```\nbsd:sage-3.0.3.alpha1-32bit mabshoff$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.0.3.alpha1, Release Date: 2008-06-04                |\n| Type notebook() for the GUI, and license() for information.        |\nsage: !singular\n                     SINGULAR                             /  Development\n A Computer Algebra System for Polynomial Computations   /   version 3-0-4\n                                                       0<\n     by: G.-M. Greuel, G. Pfister, H. Schoenemann        \\   Nov 2007\nFB Mathematik der Universitaet, D-67653 Kaiserslautern    \\\n> Auf Wiedersehen.\nsage: \nExiting SAGE (CPU time 0m0.03s, Wall time 0m9.35s).\nbsd:sage-3.0.3.alpha1-32bit mabshoff$ \n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-06-26T06:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2710#issuecomment-18653",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This has been fixed for me:

```
bsd:sage-3.0.3.alpha1-32bit mabshoff$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.3.alpha1, Release Date: 2008-06-04                |
| Type notebook() for the GUI, and license() for information.        |
sage: !singular
                     SINGULAR                             /  Development
 A Computer Algebra System for Polynomial Computations   /   version 3-0-4
                                                       0<
     by: G.-M. Greuel, G. Pfister, H. Schoenemann        \   Nov 2007
FB Mathematik der Universitaet, D-67653 Kaiserslautern    \
> Auf Wiedersehen.
sage: 
Exiting SAGE (CPU time 0m0.03s, Wall time 0m9.35s).
bsd:sage-3.0.3.alpha1-32bit mabshoff$ 
```


Cheers,

Michael



---

archive/issue_events_002899.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-26T06:21:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2710",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2710#event-2899"
}
```



---

archive/issue_comments_018654.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-26T06:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2710#issuecomment-18654",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
