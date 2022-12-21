# Issue 5433: [with patch, needs review] LaTeX fixes

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-03-04 02:15:25

Assignee: jhpalmieri

The attached patch fixes some `_latex_` methods: things like "{\rm blah}" have been changed to "\mathrm{blah}", and things like "\mbox{\bf blah}" have been changed to "\mathbf{blah}".


---

Attachment

Oh, right, it also does something else: it changes the `_latex_file_` function in sage/misc/latex.py: I changed the default arguments, added documentation, and removed the "brk" argument since I really couldn't see the point: setting brk equal to 2 would change `\begin{document} blah` to `\b eg in {d oc um en t} bl ah`.  Why?

As far as changing the default values, we made many of the same changes in the `view` function a while ago: see #3145.

I made corresponding changes to the png function in that file.


---

Comment by rbeezer created at 2009-03-16 04:56:31

Replying to [comment:1 jhpalmieri]:

Hi John,

Working on a review.  Looks good and all tests passed.

There was a time when TeX would choke on long input (more than 256 characters?) so maybe that explains the use of "brk"?  But I think those days are behind us, so it is probably safe to drop it.

Two suggestions:

1.  In the docstring for `_latex_file_()` it is not real clear that the `sep` argument is for decoration rather than function.  Maybe additional explanation like:  "for example, `sep='\\hrule'`", would make it clearer that this is not a LaTeX requirement like "$$" (and it also needs an escaped backslash for any TeX commands).  (Which I now see is discussed in #3145.)

2.  Are all the "empty" `\pagestyle` and `\thispagestyle` really needed?  There is one present in the header, but then two show up between each object's latex representation.  They don't seem to be hurting anything, but maybe now would be a good time to have them go away, perhaps along with a `\n` or two.

Rob


---

Comment by jhpalmieri created at 2009-03-16 17:28:41

Replying to [comment:2 rbeezer]:

Hi Rob,

Thanks for your comments. I'm attaching a new patch (to be applied on top of the other one) addressing them, plus a bit more:

I've expanded the docstring for `_latex_file` considerably, including comments about sep, and I've removed a bunch of the `\pagestyle` (etc.) commands.

I also changed the default spacing in the LaTeX file: it used to be 

```
title (centered)
\vfill
object
\vfill
```

and I've changed it to

```
title (centered)
\vspace{40mm}
object
```

I think this looks better, but we can change it back if you disagree.

It used to be that if `tiny=False`, then the file contained "\\small", and I've deleted this.

Finally, `view` and `_latex_file` had options to pass on to xdvi: 'expert' and 'zoom'.  These were not used anywhere in the code, and in fact I don't see how you even could pass them as arguments to xdvi, given the changes in #3137.  So I've deleted those options.

  John


---

Attachment

apply on top of other patch


---

Comment by rbeezer created at 2009-03-17 03:00:19

Replying to [comment:3 jhpalmieri]:

Hi John,

Looks great - lots of good documentation and code clean-up, plus much more readable LaTeX source being produced by `_latex_file_()`, in addition to the typeset result being improved.

latex.py passed tests and performs as advertised.  `view()` works at command line through xdvi or in the notebook.

And that's the most entertaining docstring I've seen yet.  ;-)

Positive review.  Apply both patches in the order attached here.

Rob


---

Comment by mabshoff created at 2009-03-25 07:52:36

Resolution: fixed


---

Comment by mabshoff created at 2009-03-25 07:52:36

Merged both patches in Sage 3.4.1.alpha0.

Cheers,

Michael
