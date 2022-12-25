# Issue 7863: Remove lint from auxiliary JS files

archive/issues_007863.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @TimDumol\n\n[JSLint](http://www.jslint.com/) on \"The Good Parts\" setting, applied to `sagenb/data/sage/js/*.js` but *not* `notebook_lib.js`.  The latter will have its own ticket.\n\nFor now, I've have not enabled [strict mode](http://ejohn.org/blog/ecmascript-5-strict-mode-json-and-more/), since most (all?) current browsers don't yet have it.\n\nGiven the overall current design of the notebook JS library --- use lots of global variables, etc. --- I haven't implemented *all* of JSLint's suggestions.  More generally:\n\n    \"If you're writing javascript code, [JSLint](http://www.jslint.com/) is a really fine piece of software, too. You don't have to follow its recommendations blindly, but understanding what it says about your code can greatly improve your skills.\" -- http://jsbeautifier.org/\n\nIssue created by migration from https://trac.sagemath.org/ticket/7863\n\n",
    "created_at": "2010-01-07T03:11:23Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Remove lint from auxiliary JS files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7863",
    "user": "https://github.com/qed777"
}
```
Assignee: @williamstein

CC:  @TimDumol

[JSLint](http://www.jslint.com/) on "The Good Parts" setting, applied to `sagenb/data/sage/js/*.js` but *not* `notebook_lib.js`.  The latter will have its own ticket.

For now, I've have not enabled [strict mode](http://ejohn.org/blog/ecmascript-5-strict-mode-json-and-more/), since most (all?) current browsers don't yet have it.

Given the overall current design of the notebook JS library --- use lots of global variables, etc. --- I haven't implemented *all* of JSLint's suggestions.  More generally:

    "If you're writing javascript code, [JSLint](http://www.jslint.com/) is a really fine piece of software, too. You don't have to follow its recommendations blindly, but understanding what it says about your code can greatly improve your skills." -- http://jsbeautifier.org/

Issue created by migration from https://trac.sagemath.org/ticket/7863





---

archive/issue_comments_068050.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-07T03:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7863#issuecomment-68050",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068051.json:
```json
{
    "body": "Attachment [trac_7863-declare_vars_aux_js.patch](tarball://root/attachments/some-uuid/ticket7863/trac_7863-declare_vars_aux_js.patch) by @qed777 created at 2010-01-07 03:21:17\n\nDeclare vars in functions, etc., in aux JS files.  Depends on #7786.  sagenb repo.",
    "created_at": "2010-01-07T03:21:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7863#issuecomment-68051",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7863-declare_vars_aux_js.patch](tarball://root/attachments/some-uuid/ticket7863/trac_7863-declare_vars_aux_js.patch) by @qed777 created at 2010-01-07 03:21:17

Declare vars in functions, etc., in aux JS files.  Depends on #7786.  sagenb repo.



---

archive/issue_comments_068052.json:
```json
{
    "body": "Attachment [trac_7863-declare_vars_aux_js_v2.patch](tarball://root/attachments/some-uuid/ticket7863/trac_7863-declare_vars_aux_js_v2.patch) by @qed777 created at 2010-01-08 17:17:01\n\nRebased vs. #7786 v11.  Replaces previous.",
    "created_at": "2010-01-08T17:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7863#issuecomment-68052",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7863-declare_vars_aux_js_v2.patch](tarball://root/attachments/some-uuid/ticket7863/trac_7863-declare_vars_aux_js_v2.patch) by @qed777 created at 2010-01-08 17:17:01

Rebased vs. #7786 v11.  Replaces previous.



---

archive/issue_comments_068053.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T20:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7863#issuecomment-68053",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068054.json:
```json
{
    "body": "Looks good to me. Nice style changes.",
    "created_at": "2010-01-17T20:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7863#issuecomment-68054",
    "user": "https://github.com/TimDumol"
}
```

Looks good to me. Nice style changes.



---

archive/issue_events_008078.json:
```json
{
    "actor": "https://github.com/TimDumol",
    "created_at": "2010-01-19T03:34:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7863",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7863#event-8078"
}
```



---

archive/issue_comments_068055.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T03:34:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7863#issuecomment-68055",
    "user": "https://github.com/TimDumol"
}
```

Resolution: fixed
