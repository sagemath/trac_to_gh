# Issue 6017: Provide methods for graphs to set options for latex printing

Issue created by migration from https://trac.sagemath.org/ticket/6017

Original creator: rbeezer

Original creation time: 2009-05-11 04:34:50

Assignee: rbeezer

CC:  fidelbarrera

Using the tkz-graph package in latex allows for a variety of customizations in the output.  So methods will allow a graph to set and carry options that can be used by the latex() method.

1.  make set_latex_option(), get_latex_option(), clear_latex_option()  as new methods for a graph

2.  Add a dictionary to a graph that contains the values of these options.

3.  So the latex() method can query the dictionary and act accordingly.

See #5975



---

Comment by rbeezer created at 2009-05-20 15:30:01

The proposed changes have been incorporated into #5975, so this is obsolete.


---

Comment by mabshoff created at 2009-05-20 16:49:52

No, this is not obsolete and this is not how we do things around here ;).

Comment on the other ticket that it also fixes this ticket. Then both of them will be closed and credited when the other ticket has been merged.

Cheers,

Michael


---

Comment by rbeezer created at 2009-05-20 17:57:26

Replying to [comment:2 mabshoff]:
> No, this is not obsolete and this is not how we do things around here ;).

Understood.  It was a severely flawed attempt to save you some work.  ;-)


---

Comment by ncalexan created at 2009-06-13 23:29:07

Resolution: fixed


---

Comment by ncalexan created at 2009-06-13 23:29:07

This is addressed in #5975, merged in 4.0.2.alpha0.
