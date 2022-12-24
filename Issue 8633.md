# Issue 8633: remove more instances of 'texttt' from jsmath output

archive/issues_008633.json:
```json
{
    "body": "Assignee: tbd\n\nTry this in the notebook with the \"Typeset\" box checked:\n\n```\nrandom_matrix(ZZ, 5, 5).eigenvalues()\n```\n\nYou will see a box saying \"Unknown control sequence '\\texttt'\".  The attached patch fixes this by replacing \"\\texttt\" with \"\\hbox\" before processing the LaTeX string with jsMath.\n\nThis was reported on [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/b35dc4f890f48677?tvc=2).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8633\n\n",
    "created_at": "2010-03-30T17:40:22Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "remove more instances of 'texttt' from jsmath output",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8633",
    "user": "jhpalmieri"
}
```
Assignee: tbd

Try this in the notebook with the "Typeset" box checked:

```
random_matrix(ZZ, 5, 5).eigenvalues()
```

You will see a box saying "Unknown control sequence '\texttt'".  The attached patch fixes this by replacing "\texttt" with "\hbox" before processing the LaTeX string with jsMath.

This was reported on [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/b35dc4f890f48677?tvc=2).

Issue created by migration from https://trac.sagemath.org/ticket/8633





---

archive/issue_comments_078297.json:
```json
{
    "body": "Attachment [trac_8633-texttt.patch](tarball://root/attachments/some-uuid/ticket8633/trac_8633-texttt.patch) by novoselt created at 2010-04-01 01:47:20\n\nWorks for me (I had another case of \\texttt - thank you for providing such a timely patch!) and for the given code.\n\nIs it ready for review? The patch does not add any doctests, but I am not sure if it is possible to test such an issue in doctests. At least it does not break any existing ones.",
    "created_at": "2010-04-01T01:47:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8633#issuecomment-78297",
    "user": "novoselt"
}
```

Attachment [trac_8633-texttt.patch](tarball://root/attachments/some-uuid/ticket8633/trac_8633-texttt.patch) by novoselt created at 2010-04-01 01:47:20

Works for me (I had another case of \texttt - thank you for providing such a timely patch!) and for the given code.

Is it ready for review? The patch does not add any doctests, but I am not sure if it is possible to test such an issue in doctests. At least it does not break any existing ones.



---

archive/issue_comments_078298.json:
```json
{
    "body": "Yes, it's ready for review.",
    "created_at": "2010-04-01T01:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8633#issuecomment-78298",
    "user": "jhpalmieri"
}
```

Yes, it's ready for review.



---

archive/issue_comments_078299.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-01T01:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8633#issuecomment-78299",
    "user": "jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078300.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-01T02:12:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8633#issuecomment-78300",
    "user": "novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078301.json:
```json
{
    "body": "Merged \"trac_8633-texttt.patch\" in 4.4.alpha0.",
    "created_at": "2010-04-16T18:54:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8633#issuecomment-78301",
    "user": "jhpalmieri"
}
```

Merged "trac_8633-texttt.patch" in 4.4.alpha0.



---

archive/issue_comments_078302.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:54:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8633#issuecomment-78302",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_078303.json:
```json
{
    "body": "I get the same problem on 4.4.2 with\n\n\n```\nhtml.table([random_matrix(ZZ, 5, 5).eigenvalues()])\n```\n\n\neven though the example in this ticket does work.",
    "created_at": "2010-09-22T02:35:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8633#issuecomment-78303",
    "user": "jason"
}
```

I get the same problem on 4.4.2 with


```
html.table([random_matrix(ZZ, 5, 5).eigenvalues()])
```


even though the example in this ticket does work.



---

archive/issue_comments_078304.json:
```json
{
    "body": "I think that the two calls to `latex` in sage/misc/html.py need to be changed from\n\n```\nlatex(XXX)\n```\n\nto \n\n```\nlatex(XXX).replace('\\\\texttt','\\\\hbox')\n```\n\nOpen another ticket, cc me, and post a patch.",
    "created_at": "2010-09-22T03:18:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8633#issuecomment-78304",
    "user": "jhpalmieri"
}
```

I think that the two calls to `latex` in sage/misc/html.py need to be changed from

```
latex(XXX)
```

to 

```
latex(XXX).replace('\\texttt','\\hbox')
```

Open another ticket, cc me, and post a patch.



---

archive/issue_comments_078305.json:
```json
{
    "body": "(Oh, and add a doctest in the patch.)",
    "created_at": "2010-09-22T03:19:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8633#issuecomment-78305",
    "user": "jhpalmieri"
}
```

(Oh, and add a doctest in the patch.)
