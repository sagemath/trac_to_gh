# Issue 1721: Introduse SYSTEM_ATLAS to skip tuning of ATLAS

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-01-08 10:52:38

Assignee: mabshoff

Since many people complain about the ATLAS build in case they end up with a system without pre-tuned CPUs add this end-variable to skip over the ATLAS build.

Cheers,

Michael


---

Comment by zimmerma created at 2008-01-09 23:08:29

The following patch should solve the problem of Pentium Ms which are misrecognized as CoreDuo:

```
$ pwd
/tmp/atlas-3.8.p6/src/ATLAS/CONFIG/src/backend
$ diff -u archinfo_x86.c.orig archinfo_x86.c
--- archinfo_x86.c.orig 2008-01-09 23:43:59.000000000 +0100
+++ archinfo_x86.c      2008-01-09 23:44:11.000000000 +0100
`@``@` -281,6 +281,7 `@``@`
       case  9:
       case 13:
          iret = IntPM;
+        break;
       case 14:
          iret = IntCoreDuo;
          break;
```

This should also solve (partly) #1547.


---

Comment by zimmerma created at 2008-01-09 23:13:14

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-01-10 05:06:37

Hello Paul,

this is really an orthogonal issue, so I took your patch and made it #1740.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-10 18:42:28

Removed [with patch] since Paul's patch is unrelated to this issue.

Cheers,

Michael


---

Comment by pdenapo created at 2008-01-19 21:08:52

This is an important thing to do, building ATLAS takes too much time!


---

Comment by jkantor created at 2008-01-20 01:09:01

I add an optional SAGE_ATLAS_LIB keyword, which should be a directory containing
libatlas.so, liblapack.so, libcblas.so, libatlas.so

http://sage.math.washington.edu/home/jkantor/spkgs/atlas-3.8.p8.spkg


---

Comment by mabshoff created at 2008-01-22 06:53:57

The script that did link the libraries failed to link the headers. The spkg at #1787 will fix that.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-22 07:11:05

Merged in Sage 2.10.1.alpha1


---

Comment by mabshoff created at 2008-01-22 07:11:05

Resolution: fixed
