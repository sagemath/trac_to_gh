# Issue 4914: convert sage.groups.* docstrings to Sphinx

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-01-01 22:52:03

Assignee: tba




---

Attachment


---

Comment by wdj created at 2009-01-02 11:53:15

(1) This does not implement the docstring changes in
http://trac.sagemath.org/sage_trac/ticket/3749

(2) The only conversion problem is see is 

* in abelian_group:


```
 	129	- [C2] ----, A course in computational algebraic number theory, 
 	130	  Springer, 1996. [R] J. Rotman, An introduction to the theory of 
 	131	  groups, 4th ed, Springer, 1995. 
 	132	 
```

should be


```
 	129	- [C2] ----, A course in computational algebraic number theory, 
 	130	  Springer, 1996. 
        131       [R] J. Rotman, An introduction to the theory of 
 	132	  groups, 4th ed, Springer, 1995. 
 	133
```

	 
(3) What is the purpose of linear.py?? (Open a separate trac ticket?)


---

Comment by mhansen created at 2009-01-02 20:23:40

Regarding (1), those changes haven't been merged into Sage.

I'll post a patch for (2).

For (3), I think all of the linear groups stuff was there before they got moved out into their own files.


---

Attachment


---

Comment by mabshoff created at 2009-01-02 20:34:54

Replying to [comment:3 mhansen]:
> Regarding (1), those changes haven't been merged into Sage.

Yes, anything not in Sage will likely need to be rebased. The fast that the ReST conversion is coming has been known for *many weeks* and was mentioned numerous times on sage-devel.

Cheers,

Michael


---

Comment by mhansen created at 2009-01-02 20:38:19

That being said, I'll make a signup list for people who would like new files converted over / patches to be rebased to help ease the transition.


---

Comment by mabshoff created at 2009-01-02 20:40:48

Replying to [comment:5 mhansen]:
> That being said, I'll make a signup list for people who would like new files converted over / patches to be rebased to help ease the transition.

Absolutely, but given the wide publicity this received no one can reading sage-devel can claim to be surprised by this. And this shows exactly why people need to be behind their patches to get them reviewed so that they don't bitrot.

Cheers,

Michael


---

Comment by wdj created at 2009-01-02 20:48:16

Re: http://trac.sagemath.org/sage_trac/ticket/3749

It was my fault. I posted the patch following the referee's suggestions but simply forgot to relabel the ticket "needs review".


---

Attachment

latex-fix-4914.patch is a one-character change that's necessary to allow generation of the PDF docs.  Note that this is not in any way a review of the original patch; I haven't even looked at it.


---

Comment by wdj created at 2009-01-24 16:40:04

For the purpose of review, could you post somewhere the output of the html and/or pdf after all the patches are applied, please?


---

Comment by mhansen created at 2009-01-25 02:58:27

You can find them

http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/html/en/reference/

and 

http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/pdf/en/reference/


---

Comment by mhansen created at 2009-01-25 02:58:27

Changing status from new to assigned.


---

Comment by mhansen created at 2009-01-25 02:58:27

Changing assignee from tba to mhansen.


---

Comment by wdj created at 2009-01-25 04:19:54

Thank you.

Looks good to me!


---

Attachment

Merged in Sage 3.4.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-24 18:47:00

Resolution: fixed
