# Issue 5791: Allow custom packages to be injected or %latex and the Sage latex mode

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-04-15 06:55:56

Assignee: cwitty

See http://groups.google.com/group/sage-devel/browse_thread/thread/39f1d0e71eae2453 for the discussion: It would be great of one could add packages that are automatically included when running LaTeX, i.e. for commutative diagrams.

Cheers,

Michael


---

Comment by jhpalmieri created at 2009-04-24 20:02:36

Changing status from new to assigned.


---

Comment by jhpalmieri created at 2009-04-24 20:02:36

Here's an attempt at this.  To use it:

```
sage: latex.add_macro('\\newcommand{\\foo}{bar}')
```

and then a %latex cell with \\foo in it will be processed correctly, as will %jsmath and %html cells.  Also,

```
sage: latex.add_to_preamble('\\usepackage{blah}')
```

will do what it says; it should only have an effect on %latex cells.

(In this patch, "macros" are things which are processed by latex and jsmath, while the "preamble" is only passed to latex.  For both categories, you can add to the current string with latex.add_macro or latex.add_preamble, or you can replace it with latex.extra_macros or latex.extra_preamble.)

Some pictures are [here](http://sage.math.washington.edu/home/palmieri/misc/foobar.png) and [here](http://sage.math.washington.edu/home/palmieri/misc/ext.png).

Anyway, please test it out; the patch is against 3.4.2.alpha0.


---

Comment by jhpalmieri created at 2009-04-24 20:02:36

Changing assignee from cwitty to jhpalmieri.


---

Attachment

Passes tests on misc/latex.py and misc/latex_macros.py in 3.4.2.alpha0, and works as advertised at command-line and in notebook.

PDF version of documentation builds fine also.  Another great addition to Sage-LaTeX integration.

So this is ready to go - positive review.


---

Comment by mabshoff created at 2009-04-30 04:09:13

Merged in Sage 3.4.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 04:09:13

Resolution: fixed
