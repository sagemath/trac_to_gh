# Issue 327: add perl 5.8 dependency for sage

Issue created by migration from https://trac.sagemath.org/ticket/327

Original creator: was

Original creation time: 2007-03-21 22:38:11

Assignee: was

In sage base check of prerequisites should also check for perl 5.8.  According to Kevin 
Buzzard, building maxima using perl 5.6 fails with this error, but upgrading to perl 5.8
resolves the problem:

```
"Unknown open() mode '<:crlf' at ./build_index.pl line 25".
```



---

Comment by mabshoff created at 2007-08-24 13:02:08

This will also applies to the optional PolyMakes.spkg once we update to release 2.3 - see ticket #297


---

Comment by jhpalmieri created at 2010-03-09 07:00:06

I think we do this now.  See line 5825 in prereq-0.7/configure.  Perhaps we can close this ticket?


---

Comment by drkirkby created at 2010-06-09 20:31:23

Yes, it can be closed. The configure script is generated from this bit of code I wrote in configure.ac


```
# The stats program R 2.9.2 needs perl 5.8.0 or later.
# If anything needs a later version, then this should be updated.
AC_PATH_PROG([PERL],[perl])
AX_PROG_PERL_VERSION([5.8.0],[],[AC_MSG_ERROR([Sorry, your version of perl is too old]) ])
```


The 'AC_MSG_ERROR' will cause the build to terminate at that point. 

Dave


---

Comment by drkirkby created at 2010-06-09 22:04:25

Resolution: fixed
