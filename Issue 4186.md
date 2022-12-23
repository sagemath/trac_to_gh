# Issue 4186: [with patch, needs review] speed up default __call__

Issue created by migration from https://trac.sagemath.org/ticket/4186

Original creator: robertwb

Original creation time: 2008-09-24 08:41:15

Assignee: robertwb

As this is used everywhere, I added a couple more optimizations. Cython generates less then optimal code here too, which I will fix. 




---

Attachment

Looks good to me.


---

Comment by mabshoff created at 2008-09-24 10:04:03

Resolution: fixed


---

Comment by mabshoff created at 2008-09-24 10:04:03

Merged in Sage 3.1.3.alpha1. It does not get the speed down to the old value, but shaves about 40 seconds off, so I will take this improvement :)

Cheers,

Michael


---

Comment by robertwb created at 2008-09-24 16:41:15

Hmm... It was faster on the subset of that test that I ran. There's still improvements to be made though (like when the new Cython comes out it should shave at least that much off again).
