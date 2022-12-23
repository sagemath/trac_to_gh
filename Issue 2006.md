# Issue 2006: crap -- gap contains a binary

Issue created by migration from https://trac.sagemath.org/ticket/2006

Original creator: was

Original creation time: 2008-01-31 23:16:28

Assignee: mabshoff

Gap contains this binary.  It should be deleted:

```
sage-2.10.1.rc3/spkg/standard/gap-4.4.10.p1/src/pkg/guava3.1/src/leonconv
```






---

Comment by wdj created at 2008-01-31 23:18:45

Is there a way that this can be compiled during installation? The instructions are at
http://sage.math.washington.edu/home/wdj/guava/


---

Comment by mabshoff created at 2008-01-31 23:23:25

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-01-31 23:23:25

Gap contains this binary.  It should be deleted:

```
sage-2.10.1.rc3/spkg/standard/gap-4.4.10.p1/src/pkg/guava3.1/src/leonconv
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-01-31 23:24:10

Replying to [comment:1 wdj]:
> Is there a way that this can be compiled during installation? The instructions are at
> http://sage.math.washington.edu/home/wdj/guava/

I remember somebody (rlm?) mentioning that it leaked like a sieve. Am I mistaken?

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-01 02:00:21

Resolution: fixed


---

Comment by mabshoff created at 2008-02-01 02:00:21

Merged in Sage 2.10.1.rc4
