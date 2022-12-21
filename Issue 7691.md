# Issue 7691: Expect interfaces should not timeout

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-15 19:46:14

Assignee: was

Long, long ago I randomly decided that the pexpect interfaces (to maxima, gp, etc.) should timeout if the subprocess takes more than 30 seconds to startup.  This is completely arbitrary, and really makes no sense, especially since randomly loaded systems (especially heavy NFS load) can easily and reasonably increase the startup time to > 30 seconds.  

Let's change it so that there is *no* timeout.  If you type

```
 sage: gp('2+2')
```

then Sage should simply wait until gp starts, no matter how long that takes.   That's just like typing 

```
 bash$ gp
```

on the command line and the command line not killing gp because it takes > 30 seconds to start.

This will also sort out many doctest issues on highly loaded machines. 


---

Comment by was created at 2009-12-15 21:41:05

Changing status from new to needs_review.


---

Comment by was created at 2009-12-15 21:41:05

Here is the patch:

    http://sage.math.washington.edu/home/wstein/patches/trac_7691.patch


---

Comment by mhansen created at 2009-12-16 02:28:54

Resolution: fixed


---

Attachment
