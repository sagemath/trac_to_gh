# Issue 3594: lisp -- impossible to run command line!

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-07 22:38:17

Assignee: mabshoff

The upgrade of clisp to 2.46 seriously broke something 


```
age`@`modular:~/build/sage-3.0.4.alpha2$ ./sage -lisp
/home2/sage/build/sage-3.0.4.alpha2/local/bin/clisp.bin: /home2/sage/build/sage-3.0.4.alpha2/local/lib/clisp/base/lisp.run: Nosuch file or directory
sage`@`modular:~/build/sage-3.0.4.alpha2$ ./sage -clisp
/home2/sage/build/sage-3.0.4.alpha2/local/bin/clisp.bin: /home2/sage/build/sage-3.0.4.alpha2/local/lib/clisp/base/lisp.run: Nosuch file or directory
sage`@`modular:~/build/sage-3.0.4.alpha2$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.4.alpha2, Release Date: 2008-07-06                |
| Type notebook() for the GUI, and license() for information.        |
sage: !clisp
/home2/sage/build/sage-3.0.4.alpha2/local/bin/clisp.bin: /home2/sage/build/sage-3.0.4.alpha2/local/lib/clisp/base/lisp.run: Nosuch file or director]
```



---

Comment by mabshoff created at 2008-07-07 22:54:17

clisp.run has moved to a different place. Updated spkg coming up. Sigh.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-07 22:54:23

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-07-07 23:22:42

An updated spkg is at 

http://sage.math.washington.edu/home/mabshoff/clisp-2.46.p1.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-07 23:30:00

It now actually works:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.0.4.rc0-$ ./sage -clisp
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
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.0.4.rc0-$ ./sage -lisp
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

Comment by was created at 2008-07-08 00:00:58

Resolution: fixed


---

Comment by mabshoff created at 2008-07-08 00:05:26

Merged in Sage 3.0.4.rc0
