# Issue 7339: Fix notebook interaction and cell focus bugs

Issue created by migration from https://trac.sagemath.org/ticket/7339

Original creator: mpatel

Original creation time: 2009-10-28 19:42:33

Assignee: boothby

CC:  jason was

Please see [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/e89f816b32f9fd81) for the report.

_Possibly_ relevant recent tickets include #7238 and #7254.


---

Comment by mpatel created at 2009-10-28 19:46:15

The [report](http://groups.google.com/group/sage-notebook/browse_thread/thread/e89f816b32f9fd81):

```
In Firefox 3.5.3 on Ubuntu 9.04, I opened up the "Play: Epidemic
Modeling" worksheet that is published at the top of the list on sagenb.org
and evaluated the interact (the second cell down the page or so).  I
changed the R0 slider a few times.  Each time I changed the slider, the
interact updated and focus jumped to the top of the preceding cell,
which was annoying.

Then I changed the R0 slider once more and it's been hanging there for a
while.  The green line on the side indicates that the interact is being
updated.

I tried to restart the worksheet from the menu at the top, but when I
select "Restart", the combo box closes with the "Restart" option
selected and nothing appears to happen.  When I selected the "Restart"
option, this error appeared in the Firebug console:

D is null
cell_set_not_evaluated()main.js (line 831)
set_all_cells_to_be_not_evaluated()main.js (line 1243)
restart_sage()main.js (line 1244)
eval()4 (line 1)
go_option()main.js (line 436)
function onchange(event) { go_option(this); }(change )3 (line 2)

(831 out of range 2)

I saw this error multiple times yesterday too on different worksheets,
along with this problem of the restart option not working.

I restarted the browser, and the focus-jumping problem does not happen
anymore.  However, I was able to evaluate the interact, change a few
sliders, and get the error above again when selecting the "Restart
worksheet" option from the menu at the top of the worksheet.

I hope that helps track down the problem.

Jason 
```



---

Comment by mpatel created at 2009-10-29 06:45:42

Fix interact cell focus "bug" and worksheet restart bug.


---

Comment by mpatel created at 2009-10-29 07:06:18

Changing status from new to needs_review.


---

Attachment

Please let me know if either problem remains, or if another obtains.

By the way, I've made a few changes that would be suggested by [JSLint](http://www.jslint.com/).  Currently, JSLint quits with the message

```
Lint at line 193 character 20: Too many errors. (4% scanned).
```

Although some of the checks may seem pedantic, I think we should aim for a nearly [1] lint-free notebook library per JSLint's "The Good Parts" mode ([Crockford video](http://www.youtube.com/watch?v=hQVTIJBZook)).  The short-term pain may reveal and resolve many [potential] problems [2].

[1] We'll need to "Tolerate `eval`", but possibly only in `eval_script_tags`.


[2] For Python, see [PyChecker](http://pychecker.sourceforge.net/), [PyFlakes](http://divmod.org/trac/wiki/DivmodPyflakes), and [Pylint](http://www.logilab.org/project/pylint).


---

Attachment

Rebased vs. #7309, #7310, #7332.  Apply only this patch.


---

Comment by was created at 2009-11-12 00:17:34

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-11-12 00:17:34

Very nice!   This is awesome (both fixing the original problem + the JSLint updates).

Positive review and merged into sagenb-0.4.3


---

Comment by was created at 2009-11-12 00:17:59

Resolution: fixed
