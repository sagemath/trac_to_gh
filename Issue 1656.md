# Issue 1656: make SCons pick the same gcc as `which gcc`

Issue created by migration from https://trac.sagemath.org/ticket/1656

Original creator: mabshoff

Original creation time: 2008-01-02 17:01:49

Assignee: mabshoff

Kiran had some build failure with PolyBori because SCons seems to pick the newest gcc in $PATH instead of the first one. In his particular case the newest gcc was a 32 bit target on a 64 bit platform and things didn't go to well from there. See the discussion toward the end of 

http://groups.google.com/group/sage-support/browse_thread/thread/cdf2ae8087d5637e#

This affects PolyBori as well as sagelib as far as I can tell.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-02 17:02:02

Changing status from new to assigned.


---

Comment by kedlaya created at 2008-01-02 19:59:45

On my system, unless PATH is forced to be imported from the external environment, SCons somehow decides to try using the path:

```
/usr/local/bin:/opt/bin:/bin:/usr/bin
```

despite the fact that /opt/bin doesn't exist. (This has caused mischief in the past because I had an old version of gcc in /usr/local/bin and a current one in /usr/bin; in my PATH, /usr/bin comes first.) How is this generated?


---

Comment by mabshoff created at 2008-01-03 14:39:59

This ticket also relates to #1553.

Cheers,

Michael


---

Comment by gfurnish created at 2008-03-23 18:30:01

Changing assignee from mabshoff to gfurnish.


---

Comment by gfurnish created at 2008-03-23 18:30:01

Changing status from assigned to new.


---

Comment by gfurnish created at 2008-03-23 18:30:16

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-25 16:56:27

This has been fixed in PolyBoRi via a custom.py and has been fixed in SageLib for a long, long time.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-25 16:56:27

Resolution: fixed
