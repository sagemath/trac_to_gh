# Issue 2435: Fix memory leak from #1337 workaround

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-03-09 05:32:17

Assignee: mabshoff

CC:  gfurnish

The workaround for the double free in #1337 causes memory leaks if the integer pool is full


---

Comment by mabshoff created at 2008-03-10 07:01:49

Changing priority from critical to blocker.


---

Comment by mabshoff created at 2008-03-10 07:01:49

This actually causes massive memory leaks. I tried enlarging the mempool to 1024*1024 elements, but that seems like a rather crude band aid any may have performance implications.

Robert - can you have a look if you can fix this?

Cheers,

Michael


---

Comment by robertwb created at 2008-03-10 17:51:25

I should have some time to look at this tonight. I you were busy working on 1337 and wanted to jump in but had a pile of things I couldn't put off this weekend. 

Could one or both of you post a comment here bringing things up to date with what you figured out with #1337, I've read the patch but have to admit it's not very informative on what exactly is going on. 

In justification of the integer pool--the main performance gain is because integers are ephemeral objects, so even a pool of 100 integers is a huge gain as most of the time you have new/delete/new/delete/new/delete...


---

Comment by robertwb created at 2008-03-11 10:52:28

Line 3209 of integer.pyx


```
ONE = Integer(1)
```


It has refcount 2 when one quits. It gets overwritten in two dictionaries one dictionary, then two separate dictionaries that refer to it get deleted. 

Any easy fix is to cdef it or incref it, but that isn't what the real problem is.


---

Comment by robertwb created at 2008-03-11 11:20:14

OK, this is due to some voodoo that Python does trying to clean up after itself. `_PyImport_Fini` gets called twice at the end, which tried to deallocate the (copy of) the module's dictionary. Somehow, after the first deallocation, it is still hanging around for a second round of deallocation. But the integer `ONE` does not have a high enough refcount (after all, it's only in two dictionaries) to be deallocated 3 times. 

I suspect we're running into this problem here because of some circular import issue that prevents it from being completely cleaned up the first time around.


---

Comment by robertwb created at 2008-03-11 11:32:58

Here is a fix--it doesn't crash any more for me (filling up the pool, whatever) or leak memory. 

Interestingly enough, David Roe increfs `ONE` in his `_val_unit` function (integer.pyx:1749) for no apparent reason. Hmm...


---

Comment by was created at 2008-03-11 15:41:39

Resolution: fixed


---

Attachment


---

Comment by mabshoff created at 2008-03-11 19:27:33

Nice catch Robert. Looking at the patch I can only say "D'oh" since it is so obvious. But hindsight is always 20/20 - congratulations nonetheless.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-11 20:31:51

Merged in Sage 2.10.3.final


---

Comment by robertwb created at 2008-03-12 00:43:35

Some more info: the extra Py_INCREF is not needed if `ONE` is created after the dummy integer (even if it's before the fast `tp_*` functions are hooked in).
