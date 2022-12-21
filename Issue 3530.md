# Issue 3530: [with patch, needs review] documentation for clib, cinclude pragmas

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-06-28 14:45:26

Assignee: malb

CC:  craigcitro wstein

Keywords: cython, documentation

Craig wrote off list:
> hey martin -- william tells me you created these pragmas for .spyx
> files. can you document them somewhere?

This patch documents the pragmas in the docstring. I also changed the behaviour of atlas() which now assumes that ATLAS is installed, since we ship it. mabshoff/wstein please check if my assumption is correct e.g. on OSX.


---

Attachment


---

Comment by malb created at 2008-07-02 20:47:18

Craig can you review my patch?


---

Comment by craigcitro created at 2008-07-02 22:16:33

I'm on it.


---

Comment by craigcitro created at 2008-07-04 23:52:51

This looks great. I've already updated the note on `wiki.sagemath.org` to include a reference to this docstring for more info. 

I also don't know the answer to Martin's question about ATLAS -- mabshoff or wstein, do you want to answer that?


---

Comment by mabshoff created at 2008-07-05 22:37:41

The patch will break some functionality since SAGE_CBLAS is no longer checked. I also tend to think that on OSX the whole BLAS function has not worked and will not ever work as is, so I would recommend splitting that part off to another ticket and dealing with it there. I can merge the "good" part and open another ticket for the "bad" part of the patch.

Cheers,

Michael


---

Comment by malb created at 2008-07-06 11:10:38

I'm all for splitting, so please go ahead. Actually, I don't think that this patch breaks anything it just reveals something that was broken for some time now.


---

Comment by mabshoff created at 2008-07-06 12:04:59

Since I agree with malb I will merge the patch as is and have opened #3563 to deal with the issue on OSX.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-06 18:16:10

Merged in Sage 3.0.4.alpha2


---

Comment by mabshoff created at 2008-07-06 18:16:10

Resolution: fixed


---

Attachment

Oops, somebody forgot to doctest on his install :)


---

Comment by craigcitro created at 2008-07-06 19:05:22

Looks good. *sheepishly*: I actually doctested it this time. :)
