# Issue 8053: graph editor minor bugs and improvements

Issue created by migration from https://trac.sagemath.org/ticket/8053

Original creator: rkirov

Original creation time: 2010-01-25 07:03:57

Assignee: was

CC:  mpatel

There was bug in the graph_editor which counted the release of a dragging move as a beginning of a double click. This should reduce the number of accidental node deletions.

Also added the following improvements.

- there is one-step undo available.
- a node dragged out of the iframe returns to its original position. Deletion is preformed only if mouse is released between the canvas and the iframe.
- live sliders only shown when live is enabled.
- live algorithm never pushes nodes out of bounds.

Note that JSbeautifier.com moved some if else statements indents which is reflected in the patch (even though there was not actual code change in those parts).


---

Attachment


---

Comment by rkirov created at 2010-01-25 07:12:40

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-01-31 11:17:54

The patch looks good.  The new features and fixes are great!

 * I recommend running `graph_editor.js` through [JSLint](http://www.jslint.com/) on its "The Good Parts" setting. (Feel free to set `white: true` at the top of the file, since the beautifier now takes care of that.).  It found:
    * Missing `;` at the end of line 6.
    * `removed_node` is not defined.  I suggest adding it to line 6.

 * Do people find it useful to turn off live mode but still be able to adjust the sliders?  I often do this to "freeze" movement while I make adjustments, but I'm definitely not a typical user.

 * Until they read the help text, users may expect the "Undo" button to undo the last _action_.  Can you extend its capability?  Or should we call it "Undelete" and restore a deleted edge, as well?


---

Comment by rkirov created at 2010-02-02 07:12:34

Changing status from needs_review to needs_work.


---

Comment by rkirov created at 2010-02-02 07:12:34

thanks, mitesh I will make a few more edits and submit a new patch.


---

Comment by rkirov created at 2010-04-04 17:18:33

Resolution: duplicate


---

Comment by rkirov created at 2010-04-04 17:18:33

merged with ticket 8222
