# Issue 2710: bug -- !singular doesn't work anymore on OS X

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-03-28 21:32:17

Assignee: was

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




---

Comment by mabshoff created at 2008-03-28 21:44:11

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

Comment by mabshoff created at 2008-06-26 06:21:19

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

Comment by mabshoff created at 2008-06-26 06:21:19

Resolution: fixed
