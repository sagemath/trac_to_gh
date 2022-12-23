# Issue 7863: Remove lint from auxiliary JS files

archive/issues_007863.json:
```json
{
    "body": "Assignee: was\n\nCC:  timdumol\n\n[JSLint](http://www.jslint.com/) on \"The Good Parts\" setting, applied to `sagenb/data/sage/js/*.js` but *not* `notebook_lib.js`.  The latter will have its own ticket.\n\nFor now, I've have not enabled [strict mode](http://ejohn.org/blog/ecmascript-5-strict-mode-json-and-more/), since most (all?) current browsers don't yet have it.\n\nGiven the overall current design of the notebook JS library --- use lots of global variables, etc. --- I haven't implemented *all* of JSLint's suggestions.  More generally:\n\n    \"If you're writing javascript code, [JSLint](http://www.jslint.com/) is a really fine piece of software, too. You don't have to follow its recommendations blindly, but understanding what it says about your code can greatly improve your skills.\" -- http://jsbeautifier.org/\n\nIssue created by migration from https://trac.sagemath.org/ticket/7863\n\n",
    "created_at": "2010-01-07T03:11:23Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "title": "Remove lint from auxiliary JS files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7863",
    "user": "mpatel"
}
```
Assignee: was

CC:  timdumol

[JSLint](http://www.jslint.com/) on "The Good Parts" setting, applied to `sagenb/data/sage/js/*.js` but *not* `notebook_lib.js`.  The latter will have its own ticket.

For now, I've have not enabled [strict mode](http://ejohn.org/blog/ecmascript-5-strict-mode-json-and-more/), since most (all?) current browsers don't yet have it.

Given the overall current design of the notebook JS library --- use lots of global variables, etc. --- I haven't implemented *all* of JSLint's suggestions.  More generally:

    "If you're writing javascript code, [JSLint](http://www.jslint.com/) is a really fine piece of software, too. You don't have to follow its recommendations blindly, but understanding what it says about your code can greatly improve your skills." -- http://jsbeautifier.org/

Issue created by migration from https://trac.sagemath.org/ticket/7863





---

archive/issue_comments_068167.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-07T03:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7863#issuecomment-68167",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068168.json:
```json
{
    "body": "Attachment\n\nDeclare vars in functions, etc., in aux JS files.  Depends on #7786.  sagenb repo.",
    "created_at": "2010-01-07T03:21:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7863#issuecomment-68168",
    "user": "mpatel"
}
```

Attachment

Declare vars in functions, etc., in aux JS files.  Depends on #7786.  sagenb repo.



---

archive/issue_comments_068169.json:
```json
{
    "body": "Attachment\n\nRebased vs. #7786 v11.  Replaces previous.",
    "created_at": "2010-01-08T17:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7863#issuecomment-68169",
    "user": "mpatel"
}
```

Attachment

Rebased vs. #7786 v11.  Replaces previous.



---

archive/issue_comments_068170.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T20:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7863#issuecomment-68170",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068171.json:
```json
{
    "body": "Looks good to me. Nice style changes.",
    "created_at": "2010-01-17T20:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7863#issuecomment-68171",
    "user": "timdumol"
}
```

Looks good to me. Nice style changes.



---

archive/issue_comments_068172.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T03:34:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7863#issuecomment-68172",
    "user": "timdumol"
}
```

Resolution: fixed
