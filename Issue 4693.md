# Issue 4693: [with patch, needs review] cleanup work in sage/functions/piecewise.py

Issue created by migration from https://trac.sagemath.org/ticket/4693

Original creator: mhansen

Original creation time: 2008-12-04 10:06:23

Assignee: wdj

After looking at #4690, I realized that a lot could be done to "update" piecewise.py.  This includes not explicitly using Maxima where we don't need to in order to take advantage of pynac in the future.


---

Comment by wdj created at 2008-12-04 12:26:03

I'll review this today I hope. I've read through the code. It is mostly a much more elegant rewrite of the code I wrote long ago. Maybe 85% is just using clever Python constructions I should have thought about but didn't for some reason. The rest of it uses the more modern machinery of SR classes which wasn't available when the module was first written. At first read, it looks like a really excellent patch - thanks very much Mike for this (my students and I literally use this every semester).   
I need to do some testing though and need to read the file itself (and not just the diff) to check for possible docstring problems.


---

Comment by mabshoff created at 2008-12-04 12:28:41

Thanks David. I can doctest this patch shortly and will then let you know if there are any doctest problems. Also note #4690 which already has a positive review.

Cheers,

Michael


---

Attachment

I cannot apply this patch. I've tried various things (adding the 4690 patch first, not adding it, using different Sage releases, ...). As I said, I read through it and it looks very good. I wanted to read through the docstring descriptions to see if they still made sense. (For example, from the diff file, it seemed as though the docstring description for laplace needed a small rewording.) I also was hoping Mike added himself to the AUTHOR list at the top of the file. Since the diff doesn't contain that info and I can't apply the patch, I can't tell. 
Still these are very minor issues that can be taken care of later and should not prevent this from going into Sage. So, I give this a positive review, pending doctesting. Thanks again, Mike!


---

Comment by mabshoff created at 2008-12-04 15:01:31

This applies without any problem to Sage 3.2.1 and my current 3.2.2.alpha0 merge tree. I am also quite certain that this patch applies against 3.2 since piecewise.py hasn't been touched in a while.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-04 15:36:38

Resolution: fixed


---

Comment by mabshoff created at 2008-12-04 15:36:38

Merged in Sage 3.2.2.alpha0


---

Comment by mabshoff created at 2008-12-05 07:14:06

One more thing: I know we added doctests, but the slow down seems larger than it should be:

3.2.1:

```
sage -t -long "devel/sage/sage/functions/piecewise.py"      
	 [87.8 s]
}}} 
vs. 3.2.2.alpha0
{{{
sage -t -long "devel/sage/sage/functions/piecewise.py"      
	 [145.3 s]
}}}
It might be the cleanup for plotting, but I have not investigated.

Cheers,

Michael
