# Issue 8053: graph editor minor bugs and improvements

archive/issues_008053.json:
```json
{
    "body": "Assignee: was\n\nCC:  mpatel\n\nThere was bug in the graph_editor which counted the release of a dragging move as a beginning of a double click. This should reduce the number of accidental node deletions.\n\nAlso added the following improvements.\n\n- there is one-step undo available.\n- a node dragged out of the iframe returns to its original position. Deletion is preformed only if mouse is released between the canvas and the iframe.\n- live sliders only shown when live is enabled.\n- live algorithm never pushes nodes out of bounds.\n\nNote that JSbeautifier.com moved some if else statements indents which is reflected in the patch (even though there was not actual code change in those parts).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8053\n\n",
    "created_at": "2010-01-25T07:03:57Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "title": "graph editor minor bugs and improvements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8053",
    "user": "rkirov"
}
```
Assignee: was

CC:  mpatel

There was bug in the graph_editor which counted the release of a dragging move as a beginning of a double click. This should reduce the number of accidental node deletions.

Also added the following improvements.

- there is one-step undo available.
- a node dragged out of the iframe returns to its original position. Deletion is preformed only if mouse is released between the canvas and the iframe.
- live sliders only shown when live is enabled.
- live algorithm never pushes nodes out of bounds.

Note that JSbeautifier.com moved some if else statements indents which is reflected in the patch (even though there was not actual code change in those parts).

Issue created by migration from https://trac.sagemath.org/ticket/8053





---

archive/issue_comments_070446.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-25T07:12:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8053#issuecomment-70446",
    "user": "rkirov"
}
```

Attachment



---

archive/issue_comments_070447.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-25T07:12:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8053#issuecomment-70447",
    "user": "rkirov"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070448.json:
```json
{
    "body": "The patch looks good.  The new features and fixes are great!\n\n* I recommend running `graph_editor.js` through [JSLint](http://www.jslint.com/) on its \"The Good Parts\" setting. (Feel free to set `white: true` at the top of the file, since the beautifier now takes care of that.).  It found:\n   * Missing `;` at the end of line 6.\n   * `removed_node` is not defined.  I suggest adding it to line 6.\n\n* Do people find it useful to turn off live mode but still be able to adjust the sliders?  I often do this to \"freeze\" movement while I make adjustments, but I'm definitely not a typical user.\n\n* Until they read the help text, users may expect the \"Undo\" button to undo the last *action*.  Can you extend its capability?  Or should we call it \"Undelete\" and restore a deleted edge, as well?",
    "created_at": "2010-01-31T11:17:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8053#issuecomment-70448",
    "user": "mpatel"
}
```

The patch looks good.  The new features and fixes are great!

* I recommend running `graph_editor.js` through [JSLint](http://www.jslint.com/) on its "The Good Parts" setting. (Feel free to set `white: true` at the top of the file, since the beautifier now takes care of that.).  It found:
   * Missing `;` at the end of line 6.
   * `removed_node` is not defined.  I suggest adding it to line 6.

* Do people find it useful to turn off live mode but still be able to adjust the sliders?  I often do this to "freeze" movement while I make adjustments, but I'm definitely not a typical user.

* Until they read the help text, users may expect the "Undo" button to undo the last *action*.  Can you extend its capability?  Or should we call it "Undelete" and restore a deleted edge, as well?



---

archive/issue_comments_070449.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-02T07:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8053#issuecomment-70449",
    "user": "rkirov"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_070450.json:
```json
{
    "body": "thanks, mitesh I will make a few more edits and submit a new patch.",
    "created_at": "2010-02-02T07:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8053#issuecomment-70450",
    "user": "rkirov"
}
```

thanks, mitesh I will make a few more edits and submit a new patch.



---

archive/issue_comments_070451.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-04-04T17:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8053#issuecomment-70451",
    "user": "rkirov"
}
```

Resolution: duplicate



---

archive/issue_comments_070452.json:
```json
{
    "body": "merged with ticket 8222",
    "created_at": "2010-04-04T17:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8053#issuecomment-70452",
    "user": "rkirov"
}
```

merged with ticket 8222
