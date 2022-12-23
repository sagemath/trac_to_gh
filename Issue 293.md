# Issue 293: nasty memory leak in FAST_SEQ_UNSAFE macro

Issue created by migration from https://trac.sagemath.org/ticket/293

Original creator: dmharvey

Original creation time: 2007-02-24 16:43:20

Assignee: somebody

CC:  dmharvey@math.harvard.edu

It appears that `FAST_SEQ_UNSAFE` creates a new reference to the list but never releases it.

It might be because `PySequence_Fast` returns a new reference, but `PySequence_Fast_ITEMS` doesn't release it.

See also

http://docs.python.org/api/sequence.html



---

Comment by robertwb created at 2007-08-19 00:51:29

Replying to [comment:1 was]:

Now that we have fast list indexing, there should be very few instances where we need to use this macro...


---

Comment by was created at 2007-08-19 01:42:08

Confirmed.  This is a *major* memory leak

```
[18:35] <william> indeed!
[18:35] <william> david harvey is totally right about that memory leak!
[18:35] <william> Try the following two distinct blocks of code, where m = get_memory_usage
[18:35] <william> print m()
[18:35] <william> n = random_matrix(RR, 200) 
[18:35] <william> n.set_immutable()
[18:35] <william> hash(n)
[18:35] <william> del n
[18:35] <william> m()
[18:35] <william>   -- and --
[18:35] <william> print m()
[18:35] <william> n = random_matrix(RR, 200) 
[18:35] <william> n.set_immutable()
[18:35] <william> del n
[18:35] <william> m()
[18:36] <william> The first leaks about 3MB every time.  The second doesn't leak at all.
[18:36] <robertwb> ouch
[18:36] <robertwb> yes, it's a new reference (though it may or may not be a new object)


print m()
n = random_matrix(RR, 200) 
n.set_immutable()
hash(n)
del n
m()
```



---

Comment by was created at 2007-08-19 01:42:08

Changing priority from major to blocker.


---

Comment by was created at 2007-08-19 01:47:34

Changing assignee from somebody to robertwb.


---

Comment by robertwb created at 2007-08-19 07:53:34

patch to remove all uses of FAST_SEQ_UNSAFE


---

Attachment


---

Comment by robertwb created at 2007-08-19 07:54:24

Resolution: fixed
