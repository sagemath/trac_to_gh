# Issue 4175: [with patch, needs review] cpdef arithmatic functions

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-09-23 07:17:14

Assignee: somebody

Rather than the `_xxx_, _xxx_c, _xxx_c_impl` stuff we have now. 


---

Attachment

This gets rid of a lot of cruft and hundreds of lines of unneeded code now that we have cpdef functions (as well as hundreds of lines of ever .c function that cimports Element). 

All tests pass with sage -testall.


---

Comment by mhansen created at 2008-09-23 22:08:13

I've looked over this code, and it looks good to me.  This is definitely way better than what we had before.  mabshoff, do you want to see if applies to your current tree / passes tests?


---

Comment by mabshoff created at 2008-09-23 22:49:55

The patch goes into my current merge tree with slight offsets here and there and I am building and testing now, but that will be a while. Before I import it: Are any of the coercion changes impacted by this patch, i.e. do the rebased patches still apply with this patch applied? Or should we wait to merge the coercion tickets first and then apply this patch?

Cheers,

Michael


---

Comment by robertwb created at 2008-09-23 22:54:01

They should be fairly orthogonal--I tried to keep them that way.

The Dickman's function patch you just merged will need the _impl_c methods renamed though.


---

Comment by mabshoff created at 2008-09-23 22:59:43

Replying to [comment:4 robertwb]:
> They should be fairly orthogonal--I tried to keep them that way.

Good, let's hope for the best.

> The Dickman's function patch you just merged will need the _impl_c methods renamed though. 

Can you throw a patch on top for that function then? Should doctests and build pass I will merge this patch and the Diekman fix now.

Cheers,

Michael


---

Attachment


---

Comment by robertwb created at 2008-09-23 23:08:38

OK, there's the patch. Yes, all doctests should pass.


---

Comment by mabshoff created at 2008-09-24 00:12:32

Merged both patches in Sage 3.1.3.alpha1. All doctests pass with the two patches applied.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-24 00:12:32

Resolution: fixed
