# Issue 3046: version option returning clone branch name

Issue created by migration from https://trac.sagemath.org/ticket/3046

Original creator: wdj

Original creation time: 2008-04-27 20:19:58

Assignee: was

The attached patch adds to version an option which returns the version and the branch clone name.
New behavior:
sage: version()
returns exactly the same thing it did before no change.
sage: version(True) # or replace "True" by anything except "0" or "False"
returns 
(Version, Branch name)
For example,

```
sage: version(1)

('SAGE Version 3.0, Release Date: 2008-04-22',
 'Mercurial clone branch: version')
```

in a Mercurial clone branch created using "sage -clone version".


---

Attachment


---

Comment by mabshoff created at 2008-05-11 11:08:06

Patch looks good to me. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-11 11:08:20

Resolution: fixed


---

Comment by mabshoff created at 2008-05-11 11:08:20

Merged in Sage 3.0.2.alpha0


---

Comment by was created at 2008-05-19 06:17:23

Changing status from closed to reopened.


---

Comment by was created at 2008-05-19 06:17:23

Very negative review because the patch adds this line:

```
	r"""nodoctest 
```



---

Comment by was created at 2008-05-19 06:17:23

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-05-19 06:28:33

Resolution: fixed


---

Comment by mabshoff created at 2008-05-19 06:28:33

I fixed this in the repo by removing "nodoctest". Doctests do pass now.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-19 06:32:19

this patch removes 'nodoctest' and make the doctests actually pass - my bad for the sloppy review
