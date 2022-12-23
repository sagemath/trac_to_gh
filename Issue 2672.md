# Issue 2672: Fix OSX 10.5 detection code - it fails for the currect OSX 10.5.2

Issue created by migration from https://trac.sagemath.org/ticket/2672

Original creator: mabshoff

Original creation time: 2008-03-26 07:31:30

Assignee: mabshoff

The latest OSX 10.5.2 identifies itself as 

```
$ uname -a
Darwin zippo 9.2.2 Darwin Kernel Version 9.2.2: Tue Mar  4 21:17:34
PST 2008; root:xnu-1228.4.31~1/RELEASE_I386 i386
```

This makes the following detection code fail:

```
$ uname -r | sed s/9\.[0-9]\.0/9\.0\.0/
9.2.2
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-03-26 07:34:39

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-03-26 11:38:28

We currently use the following code:

```
if [ `uname` = "Darwin" -a `uname -r | sed s/9\.[0-9]\.0/9\.0\.0/` = "9.0.0" ]; then
    echo "OSX 10.5."
fi
```

It needs to be

```
if [ `uname` = "Darwin" -a `uname -r | sed s/9\.[0-9]\.[0-9]/9\.0\.0/` = "9.0.0" ]; then
    echo "OSX 10.5."
fi
```

This will break once OSX 10.5.10 rolls around, so we might want to do something more clever.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-28 19:29:33

The above construct is used in three spkgs:

 * clisp-2.41.p12
 * gmp-4.2.1.p12
 * python-2.5.1.p13

Fixed spkgs coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-28 20:19:31

Update spkgs:

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/alpha2/clisp-2.41.p13.spkg
http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/alpha2/gmp-4.2.1.p13.spkg
http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/alpha2/python-2.5.1.p14.spkg

Build tested on Linux, test on OSX coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-28 20:43:03

The above three spkgs also build fine on OSX 10.5.1. I don't have access to a 10.5.2 test box, but they should now work since I manually tested the changed to the sed script.

Cheers,

Michael


---

Comment by gfurnish created at 2008-03-28 21:45:00

These build correctly.


---

Comment by mabshoff created at 2008-03-28 21:54:24

Merged in Sage 2.11.alpha2


---

Comment by mabshoff created at 2008-03-28 21:54:24

Resolution: fixed
