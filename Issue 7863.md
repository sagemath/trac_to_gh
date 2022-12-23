# Issue 7863: Remove lint from auxiliary JS files

Issue created by migration from https://trac.sagemath.org/ticket/7863

Original creator: mpatel

Original creation time: 2010-01-07 03:11:23

Assignee: was

CC:  timdumol

[JSLint](http://www.jslint.com/) on "The Good Parts" setting, applied to `sagenb/data/sage/js/*.js` but _not_ `notebook_lib.js`.  The latter will have its own ticket.

For now, I've have not enabled [strict mode](http://ejohn.org/blog/ecmascript-5-strict-mode-json-and-more/), since most (all?) current browsers don't yet have it.

Given the overall current design of the notebook JS library --- use lots of global variables, etc. --- I haven't implemented _all_ of JSLint's suggestions.  More generally:

    "If you're writing javascript code, [JSLint](http://www.jslint.com/) is a really fine piece of software, too. You don't have to follow its recommendations blindly, but understanding what it says about your code can greatly improve your skills." -- http://jsbeautifier.org/


---

Comment by mpatel created at 2010-01-07 03:18:51

Changing status from new to needs_review.


---

Attachment

Declare vars in functions, etc., in aux JS files.  Depends on #7786.  sagenb repo.


---

Attachment

Rebased vs. #7786 v11.  Replaces previous.


---

Comment by timdumol created at 2010-01-17 20:02:34

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-01-17 20:02:34

Looks good to me. Nice style changes.


---

Comment by timdumol created at 2010-01-19 03:34:29

Resolution: fixed
