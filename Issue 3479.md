# Issue 3479: [with patch, needs review] update dsage portion of tut.tex

Issue created by migration from Trac.

Original creator: yi

Original creation time: 2008-06-19 22:29:22

Assignee: tba

This patch provides 2 more examples on how to use the distributed map() function in dsage as well as the `@`parallel decorator.

To get the tutorial to build correctly I needed to remove all the temporary files and run the 'build_pdf' script twice to generate the index. 

This patch depends on #3467 and the `@`parallel decorator patches going in.


---

Comment by yi created at 2008-06-19 22:30:08

Patch for doc/tut/tut.tex


---

Attachment

Yi, does your patch apply with #3347 applied?


---

Comment by mhansen created at 2008-06-19 22:37:37

Changing keywords from "" to "editor_mhansen".


---

Comment by jhpalmieri created at 2008-08-13 19:13:22

The patch fails against the current version of the tutorial.

When applied manually, the patch seems okay, and passes all doctests. A few comments:

In example 3, item 5, I would suggest changing `$f$` to `\code{f`}, for the sake of better latex to html conversion.

In example 4, the verbatim block looks odd, especially in the live version of the tutorial.

If you fix at least example 3, and produce a patch against the current tutorial, I'll give it a positive review.

(In general, I find the style of using numbered instructions, as in all of the dsage examples, at odds with the style of the rest of the tutorial.  It would be nice if this were rewritten, but that can wait for a separate trac item and patch.)


---

Comment by jhpalmieri created at 2008-08-13 21:00:33

By the way, what does "% (fold)" mean?  This only appears in the dsage part of the tutorial, and I don't know what role it plays.


---

Comment by mhansen created at 2009-01-24 09:56:43

Changing status from new to assigned.


---

Comment by mhansen created at 2009-01-24 09:56:43

Changing assignee from tba to mhansen.


---

Comment by mhansen created at 2009-01-24 09:56:43

I addressed the referee's comment and added this to the Sphinx version of the tutorial.


---

Comment by mabshoff created at 2009-02-24 17:54:50

Merged in Sage 3.4.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-24 17:54:50

Resolution: fixed
