# Issue 2712: Add 'scalar_part()' and other methods for quaternion elements

Issue created by migration from https://trac.sagemath.org/ticket/2712

Original creator: justin

Original creation time: 2008-03-28 21:39:20

Assignee: mabshoff

Following John Cremona's suggestion, I've added 'scalar_part()", 'pure_part()', and 'is_pure()' for quaternions.

The method 'is_scalar()' is already implemented, so in a sense, this completes the picture.  This was spurred on by a request on the support list (from Chris Godsil).

The implementation assumes characteristic not 2, which is OK since it's implicitly or explicitly assumed throughout the quaternion code.

I think the terms 'scalar' and 'pure', for a value in the base ring and having trace 0 (and being non-zero), respectively, is fairly standard.





---

Comment by justin created at 2008-03-28 21:43:23

Adding patch.  The patch includes doctests, and the file passes the "-t" test.  The resulting file has 57% coverage (I did not add tests where there were none).

The patch is against a clean 2.10.4 tree.


---

Attachment

Patch implementing the element methods described above.


---

Comment by mhansen created at 2008-03-29 00:00:45

Looks good to me.


---

Comment by mabshoff created at 2008-03-29 00:11:49

Changing component from Cygwin to misc.


---

Comment by mabshoff created at 2008-03-29 00:11:49

Changing assignee from mabshoff to cwitty.


---

Comment by mabshoff created at 2008-03-29 00:11:49

Not sure about the component - feel free to reclassify.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-29 00:44:53

Merged in Sage 2.11.alpha2


---

Comment by mabshoff created at 2008-03-29 00:44:53

Resolution: fixed
