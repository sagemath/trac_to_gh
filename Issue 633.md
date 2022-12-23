# Issue 633: spkg-[install|check] should verify that SAGE_LOCAL is defined

Issue created by migration from https://trac.sagemath.org/ticket/633

Original creator: mabshoff

Original creation time: 2007-09-10 03:42:39

Assignee: mabshoff

Keywords: spkg-install, spkg-check

When building spkgs manually by invoking spkg-install on the shell I oftern do not have sage-env sourced. Consequently odd things happen:

```
[mabshoff@m940 mpfr-2.2.1.p1]$ ./spkg-install
./spkg-install: line 16: [: =: unary operator expected
```

We ought to verify that at least SAGE_LOCAL is non-empty. If it is empty print a warning message and exit.

To fix this we need to touch every spkg-install in the tree which is more that 75 scripts. So while we are at it we should also add spkg-check scripts to each spkg while we are at it.

Cheers,

Michael


---

Comment by mabshoff created at 2007-10-18 13:33:20

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-01-26 10:24:42

I suggest adding the following to the top of all spkg-install and spkg-check scripts:

```
if [ "$SAGE_LOCAL" = "" ]; then
   echo "SAGE_LOCAL undefined ... exiting";
   exit 1
fi
```


Cheers,

Michael


---

Comment by was created at 2008-01-27 13:33:01

Wouldn't it be useful to also give a hint about what the user should do, e.g., something like:


```
if [ "$SAGE_LOCAL" = "" ]; then
   echo "SAGE_LOCAL undefined ... exiting";
   echo "Maybe run 'sage -sh'?"
   exit 1
fi
```



---

Comment by mabshoff created at 2008-07-31 03:23:37

Resolution: fixed


---

Comment by mabshoff created at 2008-07-31 03:23:37

I have been adding the above code snippet to every spkg that I have touched in the last couple month and I assume all of them have been fixed. If there is any more specific spkg with issue it should be dealt with at its own ticket.

Cheers,

Michael
