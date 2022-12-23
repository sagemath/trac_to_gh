# Issue 1280: make Permutation(range(10)).random() fast instead of dog slow.

Issue created by migration from https://trac.sagemath.org/ticket/1280

Original creator: was

Original creation time: 2007-11-26 09:09:42

Assignee: mhansen

CC:  sage-combinat


```
[01:06am] williamstein: mhansen -- I wonder if you could make this faster?
[01:06am] williamstein: p = Permutations(range(9)); p
[01:06am] williamstein: time p.random()
[01:06am] williamstein: 5 seconds.
[01:06am] williamstein: Maybe I'm being naive.
[01:06am] williamstein: for 10 it takes forever.
[01:06am] mhansen: Heh, yeah -- I definitely could 
[01:07am] williamstein: Since p = Permutations(10); time p.random() is instant.
[01:07am] williamstein: I was trying to permute the rows of a matrix and thought your combinatorics stuff would be really nice to use
[01:07am] mhansen: Yep, I just need to override the default random.  There
[01:07am] williamstein: and it was trivial to figure out how to use it for that, but since I wanted 0-based I used range(10), which made it insanely slow.
[01:08am] mhansen: 's all sorts of these things that'd be super-easy for an undergrad to do.
```



---

Attachment


---

Comment by mhansen created at 2007-11-26 10:24:27

Changing status from new to assigned.


---

Comment by cwitty created at 2007-11-27 05:31:16

I skimmed the patch, and nothing jumped out as being wrong.  Also, I applied the patch and doctested the changed file, and tests passed.  (I did not do testall.)

In short, looks good to me.


---

Comment by mabshoff created at 2007-12-01 16:16:53

Resolution: fixed


---

Comment by mabshoff created at 2007-12-01 16:16:53

Merged in 2.8.15.alpha1.
