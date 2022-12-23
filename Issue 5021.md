# Issue 5021: [with patch, needs review] add some jsMath extensions

Issue created by migration from https://trac.sagemath.org/ticket/5021

Original creator: jhpalmieri

Original creation time: 2009-01-19 06:02:31

Assignee: boothby

Keywords: jsMath

In the spirit of the patch for #4945, this patch adds several jsMath extensions so that some new LaTeX commands will be available: it adds `moreArrows` which implements \xrightarrow among other things, and it adds `AMSmath`, which implements a handful of commands from the amsmath LaTeX package.

This patch also adds a few lines of documentation which give links to the jsMath pages for these extensions.  See those web pages for complete lists of all of the LaTeX commands made available by these packages.

(I'm adding this because I want to contribute some Sage code which uses \xrightarrow, but other people might find these useful as well.)




---

Attachment

Looks good.  I tested a command from each package and it seemed to work great.  Positive review.


---

Comment by mabshoff created at 2009-01-28 18:04:33

Resolution: fixed


---

Comment by mabshoff created at 2009-01-28 18:04:33

Moved in Sage 3.3.alpha3.

Cheers,

Michael
