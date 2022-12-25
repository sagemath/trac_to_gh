# Issue 7339: Fix notebook interaction and cell focus bugs

archive/issues_007339.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @jasongrout @williamstein\n\nPlease see [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/e89f816b32f9fd81) for the report.\n\n*Possibly* relevant recent tickets include #7238 and #7254.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7339\n\n",
    "created_at": "2009-10-28T19:42:33Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "title": "Fix notebook interaction and cell focus bugs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7339",
    "user": "https://github.com/qed777"
}
```
Assignee: boothby

CC:  @jasongrout @williamstein

Please see [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/e89f816b32f9fd81) for the report.

*Possibly* relevant recent tickets include #7238 and #7254.

Issue created by migration from https://trac.sagemath.org/ticket/7339





---

archive/issue_comments_061304.json:
```json
{
    "body": "The [report](http://groups.google.com/group/sage-notebook/browse_thread/thread/e89f816b32f9fd81):\n\n```\nIn Firefox 3.5.3 on Ubuntu 9.04, I opened up the \"Play: Epidemic\nModeling\" worksheet that is published at the top of the list on sagenb.org\nand evaluated the interact (the second cell down the page or so).  I\nchanged the R0 slider a few times.  Each time I changed the slider, the\ninteract updated and focus jumped to the top of the preceding cell,\nwhich was annoying.\n\nThen I changed the R0 slider once more and it's been hanging there for a\nwhile.  The green line on the side indicates that the interact is being\nupdated.\n\nI tried to restart the worksheet from the menu at the top, but when I\nselect \"Restart\", the combo box closes with the \"Restart\" option\nselected and nothing appears to happen.  When I selected the \"Restart\"\noption, this error appeared in the Firebug console:\n\nD is null\ncell_set_not_evaluated()main.js (line 831)\nset_all_cells_to_be_not_evaluated()main.js (line 1243)\nrestart_sage()main.js (line 1244)\neval()4 (line 1)\ngo_option()main.js (line 436)\nfunction onchange(event) { go_option(this); }(change )3 (line 2)\n\n(831 out of range 2)\n\nI saw this error multiple times yesterday too on different worksheets,\nalong with this problem of the restart option not working.\n\nI restarted the browser, and the focus-jumping problem does not happen\nanymore.  However, I was able to evaluate the interact, change a few\nsliders, and get the error above again when selecting the \"Restart\nworksheet\" option from the menu at the top of the worksheet.\n\nI hope that helps track down the problem.\n\nJason \n```\n",
    "created_at": "2009-10-28T19:46:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7339#issuecomment-61304",
    "user": "https://github.com/qed777"
}
```

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

archive/issue_comments_061305.json:
```json
{
    "body": "Fix interact cell focus \"bug\" and worksheet restart bug.",
    "created_at": "2009-10-29T06:45:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7339#issuecomment-61305",
    "user": "https://github.com/qed777"
}
```

Fix interact cell focus "bug" and worksheet restart bug.



---

archive/issue_comments_061306.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-29T07:06:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7339#issuecomment-61306",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061307.json:
```json
{
    "body": "Attachment [trac_7339-sagenb_cell_bugs.patch](tarball://root/attachments/some-uuid/ticket7339/trac_7339-sagenb_cell_bugs.patch) by @qed777 created at 2009-10-29 07:06:18\n\nPlease let me know if either problem remains, or if another obtains.\n\nBy the way, I've made a few changes that would be suggested by [JSLint](http://www.jslint.com/).  Currently, JSLint quits with the message\n\n```\nLint at line 193 character 20: Too many errors. (4% scanned).\n```\n\nAlthough some of the checks may seem pedantic, I think we should aim for a nearly [1] lint-free notebook library per JSLint's \"The Good Parts\" mode ([Crockford video](http://www.youtube.com/watch?v=hQVTIJBZook)).  The short-term pain may reveal and resolve many [potential] problems [2].\n\n[1] We'll need to \"Tolerate `eval`\", but possibly only in `eval_script_tags`.\n\n\n[2] For Python, see [PyChecker](http://pychecker.sourceforge.net/), [PyFlakes](http://divmod.org/trac/wiki/DivmodPyflakes), and [Pylint](http://www.logilab.org/project/pylint).",
    "created_at": "2009-10-29T07:06:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7339#issuecomment-61307",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7339-sagenb_cell_bugs.patch](tarball://root/attachments/some-uuid/ticket7339/trac_7339-sagenb_cell_bugs.patch) by @qed777 created at 2009-10-29 07:06:18

Please let me know if either problem remains, or if another obtains.

By the way, I've made a few changes that would be suggested by [JSLint](http://www.jslint.com/).  Currently, JSLint quits with the message

```
Lint at line 193 character 20: Too many errors. (4% scanned).
```

Although some of the checks may seem pedantic, I think we should aim for a nearly [1] lint-free notebook library per JSLint's "The Good Parts" mode ([Crockford video](http://www.youtube.com/watch?v=hQVTIJBZook)).  The short-term pain may reveal and resolve many [potential] problems [2].

[1] We'll need to "Tolerate `eval`", but possibly only in `eval_script_tags`.


[2] For Python, see [PyChecker](http://pychecker.sourceforge.net/), [PyFlakes](http://divmod.org/trac/wiki/DivmodPyflakes), and [Pylint](http://www.logilab.org/project/pylint).



---

archive/issue_comments_061308.json:
```json
{
    "body": "Attachment [trac_7339-sagenb_cell_bugs_v2.patch](tarball://root/attachments/some-uuid/ticket7339/trac_7339-sagenb_cell_bugs_v2.patch) by @qed777 created at 2009-10-31 08:50:47\n\nRebased vs. #7309, #7310, #7332.  Apply only this patch.",
    "created_at": "2009-10-31T08:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7339#issuecomment-61308",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7339-sagenb_cell_bugs_v2.patch](tarball://root/attachments/some-uuid/ticket7339/trac_7339-sagenb_cell_bugs_v2.patch) by @qed777 created at 2009-10-31 08:50:47

Rebased vs. #7309, #7310, #7332.  Apply only this patch.



---

archive/issue_comments_061309.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-12T00:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7339#issuecomment-61309",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061310.json:
```json
{
    "body": "Very nice!   This is awesome (both fixing the original problem + the JSLint updates).\n\nPositive review and merged into sagenb-0.4.3",
    "created_at": "2009-11-12T00:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7339#issuecomment-61310",
    "user": "https://github.com/williamstein"
}
```

Very nice!   This is awesome (both fixing the original problem + the JSLint updates).

Positive review and merged into sagenb-0.4.3



---

archive/issue_comments_061311.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-12T00:17:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7339#issuecomment-61311",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_017369.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-11-12T00:17:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7339",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7339#event-17369"
}
```
