# Issue 9064: remove p-adic matrix directory

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-05-27 08:20:44

Assignee: jason, was

There's a single file in matrix/padics and it is an empty __init__.py.

Says David Roe: "Yeah, oversight.  At some point I was planning on working on p-adic matrices, and I guess the __init__.py file got put in then.  Since I'm not going to work on it anytime soon, it can safely be removed."


---

Comment by was created at 2010-08-11 18:07:33

Changing status from new to needs_review.


---

Comment by was created at 2010-08-11 18:07:33

Since the file is empty, I can't do think of any way to actually do this with HG.  It seems impossible.  

```
flat:matrix wstein$ hg rm  padics
removing padics/__init__.py
flat:matrix wstein$ 
flat:matrix wstein$ 
flat:matrix wstein$ hg ci
flat:matrix wstein$ hg export ip
abort: unknown revision 'ip'!
flat:matrix wstein$ hg export tip
# HG changeset patch
# User William Stein <wstein`@`gmail.com>
# Date 1281549848 25200
# Node ID 029114d1f8a76cbd4d88b2a9a28fecadac170205
# Parent  5b338f2e484f2065d3d30d47bc204d6e9ed13d12
trac 9064 -- remove p-adic matrix directory
```

(see nothing!)

So there is no patch to post, and I take David Roe's statement (above) as a positive review.

So to the release manager merging this, just do the following:


```
cd SAGE_ROOT/devel/sage/sage/matrix
sage -hg rm  padics
sage -hg ci
```


and checkin the resulting empty patch.    Unfortunately, this won't do anything for people doing "sage -upgrade".  Anyway, it's an empty directory so whatever happens is pretty harmless.


---

Comment by was created at 2010-08-11 18:07:39

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-31 01:50:49

Remove matrix/padics.


---

Attachment

Replying to [comment:1 was]:
> So there is no patch to post, and I take David Roe's statement (above) as a positive review.

I've attached a patch made with the Mercurial queues extension.


---

Comment by mpatel created at 2010-08-31 03:20:20

Resolution: fixed
