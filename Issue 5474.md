# Issue 5474: [with patch, needs review] delimiters for LaTeX representation of matrices

Issue created by migration from https://trac.sagemath.org/ticket/5474

Original creator: jhpalmieri

Original creation time: 2009-03-10 21:23:00

Assignee: jhpalmieri

There was a request on [sage-support](http://groups.google.com/group/sage-support/browse_frm/thread/f12feafb8e4285ce) for the option to change how matrices are displayed, from parentheses to square brackets.  William made this suggestion:

```
How about adding a function to matrix0.pyx that sets a global variable
in that file to the left and right delimiters for matrices?

sage.matrix.matrix0.set_latex_delimiters('[',']')

would set them.  That's minimally intrusive.  Later on somebody could
come up with some grand scheme for customizing latex output, but
please don't until there are a few more use cases. 
```

The attached patch implements "set_matrix_latex_delimiters". (I changed the name slightly.)



---

Attachment


---

Comment by jhpalmieri created at 2009-03-10 21:46:27

Here's a vector version, too.


---

Comment by was created at 2009-03-10 22:37:50

Frickin' awesome!   NIce!


---

Comment by mabshoff created at 2009-03-11 00:13:04

Merged both patches in Sage 3.4.final.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-11 00:13:04

Resolution: fixed


---

Comment by jason created at 2009-03-11 00:48:42

Thank you!  This has been a minor annoyance when using Sage in class, since we use different delimiters than Sage...


---

Comment by jhpalmieri created at 2009-03-11 01:08:07

Replying to [comment:4 jason]:
> Thank you!  This has been a minor annoyance when using Sage in class, since we use different delimiters than Sage...

You're welcome! I hope it works well for you.
