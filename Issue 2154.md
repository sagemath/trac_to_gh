# Issue 2154: Infinite memory allocation bug in PermutationGroupElement

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2008-02-14 01:09:40

Assignee: joyner

Run the following code in a virtual machine with a smallish bound on its memory.  Or it will crash your machine.  (it took me 2 reboots to isolate the problem...)


```
PermutationGroup(2)
PermutationGroupElement([1,1],S,check=False)
```



---

Comment by boothby created at 2008-02-14 01:12:46

Changing assignee from joyner to robertwb.


---

Comment by mabshoff created at 2008-02-14 10:01:30

GAP is involved here, so the issue might not be in Sage itself.

Cheers,

Michael


---

Attachment

It looks like the problem here was actually infinite loops, but it now checks to make sure it always gets a valid permutation (even if check=False is set).


---

Comment by mabshoff created at 2008-02-26 01:44:13


```
[02:01] <mabshoff> craigcitro: can you look at #2154 ? It looks good, 
but I would like a second opinion.
[02:11] <craigcitro> mabshoff: sure, it looks good to me.
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-02-26 01:44:57

Resolution: fixed


---

Comment by mabshoff created at 2008-02-26 01:44:57

Merged in Sage 2.10.3.alpha0
