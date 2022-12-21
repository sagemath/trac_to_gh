# Issue 3212: Improving rescaling of matrices

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2008-05-15 16:31:37

Assignee: was

Currently, rescale_row and rescale_col don't allow you to rescale by something mathematically right but outside the current matrix base ring.  Discussion from sage-devel follows.

> Under the current scaling code, this happens: 
> sage: N.rescale_col(2,i/2) 
> --------------------------------------------------------------------------- 
> <type 'exceptions.TypeError'>             Traceback (most recent call 
> last) 
> <snip> 
> <type 'exceptions.TypeError'>: unable to convert I/2 to a rational 


Yep, this is orthogonal.  You're just suggesting that scale_row 
be improved. 
> What I am wondering is whether throwing an exception of TypeError 
> under the current code should be replaced by a try statement first 
> attempting N.changering(??) . The problem is I have no idea what to 
> use for ??, because unfortunately i/2 lives in Symbolic Ring, not in 
> CC, so I can't just put in ??=parent(i/2). 


The Sequence constructor is the canonical answer to this question. 
Given any list v of Sage object it will find a canonical place to put 
them all: 
sage: v = [3, I/2] 
sage: w = Sequence(v) 
sage: w 
[3, I/2] 
sage: w.universe() 
Symbolic Ring


---

Comment by kcrisman created at 2008-05-16 05:21:54

This is a first try at a patch improving documentation and removing the problem.


---

Attachment

I should point out that the above patch does not yet work.  It DOES remove the TypeError problem, but doesn't actually give the correct new matrix.


---

Comment by kcrisman created at 2008-05-16 05:23:22

Changing status from new to assigned.


---

Comment by kcrisman created at 2008-05-16 05:23:22

Changing assignee from was to kcrisman.


---

Attachment

Patch for allowing row mult by non-ring elements


---

Comment by kcrisman created at 2008-05-18 03:39:21

The patch 8869 replaces patch 8867.  

It allows multiplication of rows/columns of matrices by elements of extensions of the base rings, at the cost of (only in those cases) returning a copy, not changing the original.  

This also adds extra examples and documentation, as well as a set_col_to_multiple_of_col attribute to match set_row_to_multiple_of_row .


---

Comment by robertwb created at 2008-05-18 06:04:04

It should probably always return a matrix (for consistency), even when copying is not required.


---

Comment by kcrisman created at 2008-05-20 01:50:09

I have to remove my test function, and also want feedback on Robert's comment.


---

Comment by kcrisman created at 2008-06-06 03:06:27

Improves documentation and error messages and adds alternate methods for rescaling of matrices


---

Attachment

Use only rescaling.patch.


---

Comment by robertwb created at 2008-06-06 16:36:29

Works well for me. The only comments I have are 

- (nitpicky) with_rescale_row -> with_rescaled_row (sounds better to me)

- Do not just print out an error message, actually raise a TypeError (with an explanatory error message, though preferably without line breaks at 58 characters).


---

Attachment

Use only rescale.patch.  This is hopefully the final version.


---

Comment by robertwb created at 2008-06-07 00:09:53

Thanks. Works great.


---

Comment by mabshoff created at 2008-06-09 06:45:54

Merged rescale.patch in Sage 3.0.3.alpha2


---

Comment by mabshoff created at 2008-06-09 06:45:54

Resolution: fixed
