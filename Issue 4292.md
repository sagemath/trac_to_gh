# Issue 4292: [with patch; needs trivial review] graphics_array -- stupid bug introduced by somebody cleaning up the code

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-10-15 11:11:36

Assignee: was

If you do

```
   graphics_array([This is the Trac macro *plot* that was inherited from the migration called with arguments (sin))](https://trac.sagemath.org/wiki/WikiMacros#plot-macro)).show(axes=False)
```

the axes still get shown!  This horrendously sucks, e.g. ,for my talk today, and this was not a problem in Sage a few months ago. 

Fortunately, it's a trivial 1-line fix, which I've attached.


---

Attachment

This seems fixed in 3.1.3.final. Which version did you use?

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-15 15:29:41

I checked the source and the patch still applies, but it seems that the doctest posted does not test that particular code path, so I would suggest that the patch should be applied anyway.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-15 16:21:03

Replying to [comment:2 mabshoff]:
> I checked the source and the patch still applies, but it seems that the doctest posted does not test that particular code path, so I would suggest that the patch should be applied anyway.
> 
> Cheers,
> 
> Michael

Ok, after testing it with the command line version it becomes clear that the bug remains unfixed and that William's fix is the correct one. In the end I learned something about the plotting code :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-15 16:21:50

Merged in Sage 3.1.4.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-15 16:21:50

Resolution: fixed
