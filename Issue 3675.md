# Issue 3675: upgrade to valgrind 3.3.1

Issue created by migration from https://trac.sagemath.org/ticket/3675

Original creator: rlm

Original creation time: 2008-07-18 20:03:58

Assignee: mabshoff


```
[12:50pm] rlm: __Pyx_ImportType?
[12:51pm] rlm: sound familiar? i'm valgrinding, and this
seems to be many of 13,030 loss records...
[12:51pm] mabshoff: Yes.
[12:51pm] mabshoff: It is Cython dictionaries and I plan
to suppress them in the future.
...
[12:52pm] mabshoff: Can you make a ticket for it? I also
want to upgrade the optional valgrind.spkg to 3.3.1 and
also change some of the default options, i.e. no more
--follow-children
```


Another suggestion- an optional python spkg which has valgrind-friendly compile options set, perhaps even just a replacement `spkg-install` which uses the standard spkg.


---

Comment by mabshoff created at 2008-09-15 10:52:32

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-09-15 10:52:32

The updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc4/valgrind_3.3.1.spkg

Cheers,

Michael


---

Comment by rlm created at 2008-09-15 10:57:17

Suppression good!


---

Comment by mabshoff created at 2008-09-15 11:28:48

Merged in the optional spkg repo in Sage 3.1.2.rc4.


---

Comment by mabshoff created at 2008-09-15 11:28:48

Resolution: fixed
