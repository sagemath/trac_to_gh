# Issue 3635: If m is a matrix, then m.plot() should call matrix_plot

archive/issues_003635.json:
```json
{
    "body": "Assignee: was\n\nCurrently this just puts the text description on an empty set of axes.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3635\n\n",
    "created_at": "2008-07-10T20:41:22Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "If m is a matrix, then m.plot() should call matrix_plot",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3635",
    "user": "jason"
}
```
Assignee: was

Currently this just puts the text description on an empty set of axes.

Issue created by migration from https://trac.sagemath.org/ticket/3635





---

archive/issue_comments_025710.json:
```json
{
    "body": "Attachment\n\nThe attached patch implements the requested behavior. Jason, do you want to review it?",
    "created_at": "2008-08-18T21:17:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3635#issuecomment-25710",
    "user": "malb"
}
```

Attachment

The attached patch implements the requested behavior. Jason, do you want to review it?



---

archive/issue_comments_025711.json:
```json
{
    "body": "Whoever reviews it and/or malb should note that the patches to #3853 would imply the call to MatrixPlotFactory is superfluous (though something may still have to be imported), but of course that patch has not yet been merged either.",
    "created_at": "2008-08-20T01:35:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3635#issuecomment-25711",
    "user": "kcrisman"
}
```

Whoever reviews it and/or malb should note that the patches to #3853 would imply the call to MatrixPlotFactory is superfluous (though something may still have to be imported), but of course that patch has not yet been merged either.



---

archive/issue_comments_025712.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-08-27T14:44:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3635#issuecomment-25712",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_025713.json:
```json
{
    "body": "Apply the rebased patch *AFTER* the first patch.  Sorry, I should have used a better word that rebased.\n\nWorks great. Positive review.",
    "created_at": "2008-08-27T14:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3635#issuecomment-25713",
    "user": "jason"
}
```

Apply the rebased patch *AFTER* the first patch.  Sorry, I should have used a better word that rebased.

Works great. Positive review.



---

archive/issue_comments_025714.json:
```json
{
    "body": "Doctests in matrix/matrix2.pyx pass after both patches have been applied.",
    "created_at": "2008-08-27T14:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3635#issuecomment-25714",
    "user": "jason"
}
```

Doctests in matrix/matrix2.pyx pass after both patches have been applied.



---

archive/issue_comments_025715.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-27T22:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3635#issuecomment-25715",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025716.json:
```json
{
    "body": "Merged both patches in Sage 3.1.2.alpha2",
    "created_at": "2008-08-27T22:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3635#issuecomment-25716",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.1.2.alpha2
