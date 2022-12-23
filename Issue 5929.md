# Issue 5929: switch from clisp to ecl

Issue created by migration from https://trac.sagemath.org/ticket/5929

Original creator: was

Original creation time: 2009-04-29 01:50:33

Assignee: mabshoff

Replace clisp by ECL in Sage.  Need for the Solaris port.


---

Comment by tornaria created at 2009-05-11 03:31:05

fix for assumption hang with ecl


---

Attachment

fix (workaround) for out of sync hang which timeouts a doctest


---

Attachment

Comment for attachment:trac_5929-fix_assumption_hang.patch:

For #5929: fix hang in maxima/ecl due to assumption questions

When maxima asks a question, current code sends CTRL-C
twice to break, then raises an exception. This used to work with
clisp, but for ecl it actually hangs. A test case is given by


```
var("Ax,Bx,By")
t = -Ax*sin(sqrt(Ax^2)/2)/(sqrt(Ax^2)*sqrt(By^2 + Bx^2))
limit(t, Ax=0)
```


It turns out that it is possible to "break" from the question by just
sending ";" by itself to maxima. The current patch changes to this
method of escaping. It works with clisp or ecl.


---

Comment by tornaria created at 2009-05-11 03:36:29

Comment for attachment:trac_5929-fix_outofsync_hang.patch:

For #5929: fix timeout in maxima/ecl due to out-of-synch condition

This is triggered by the following doctest

```
sage: maxima._sendstr('1/1'*500)
sage: maxima('2+2')
```

In fact, the first line is missing a semicolon, so maxima is stuck out
of synch; the synchronization code is run for the second line, and
after a timeout, it tries to break by sending a ctrl-c (this happens
in Expect._interrupt()), but ctrl-c is broken with ecl, so this hangs.

The current fix adds an explicit semicolon to the synchronization
code. This fixes the timeout in the above doctest. The hang is still
latent, because there seems to be no way to interrupt maxima/ecl.


---

Comment by mabshoff created at 2009-05-11 07:33:27

I am splitting this off the ecl and maxima spkgs.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-11 07:33:27

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-05-12 06:11:11

Changing assignee from mabshoff to tornaria.


---

Comment by mabshoff created at 2009-05-12 06:11:11

Changing status from assigned to new.


---

Comment by mabshoff created at 2009-05-12 06:11:11

Ok, I am removing the ecl doctest fix since the two patches posted by Gonzalo fix this problem, too. So to keep credit and review simple I am giving this a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-12 06:34:51

Merged both patches in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-12 06:34:51

Resolution: fixed
