# Issue 2584: printing bug with show()

archive/issues_002584.json:
```json
{
    "body": "Assignee: jason\n\nThis causes a bug when printing:\n\n\n```\nshow([Matrix(ZZ,3,range(9)), Matrix(ZZ,3,range(9))])\n```\n\n\nNotice the extra \",\". A list of one element doesn't have the same problem.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2584\n\n",
    "created_at": "2008-03-18T11:51:35Z",
    "labels": [
        "graphics",
        "minor",
        "bug"
    ],
    "title": "printing bug with show()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2584",
    "user": "craigcitro"
}
```
Assignee: jason

This causes a bug when printing:


```
show([Matrix(ZZ,3,range(9)), Matrix(ZZ,3,range(9))])
```


Notice the extra ",". A list of one element doesn't have the same problem.

Issue created by migration from https://trac.sagemath.org/ticket/2584





---

archive/issue_comments_017683.json:
```json
{
    "body": "The bug is in the latex function:\n\n\n```\nsage: latex([Matrix(ZZ,3,range(9)), Matrix(ZZ,3,range(9))])\n\\begin{array}{l}[\\left(\\begin{array}{rrr}\n0 & 1 & 2 \\\\\n3 & 4 & 5 \\\\\n6 & 7 & 8\n\\end{array}\\right),\\\\\n\\left(\\begin{array}{rrr}\n0 & 1 & 2 \\\\\n3 & 4 & 5 \\\\\n6 & 7 & 8\n\\end{array}\\right)],\\\\\n\\end{array}\n```\n",
    "created_at": "2008-03-18T17:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2584#issuecomment-17683",
    "user": "jason"
}
```

The bug is in the latex function:


```
sage: latex([Matrix(ZZ,3,range(9)), Matrix(ZZ,3,range(9))])
\begin{array}{l}[\left(\begin{array}{rrr}
0 & 1 & 2 \\
3 & 4 & 5 \\
6 & 7 & 8
\end{array}\right),\\
\left(\begin{array}{rrr}
0 & 1 & 2 \\
3 & 4 & 5 \\
6 & 7 & 8
\end{array}\right)],\\
\end{array}
```




---

archive/issue_comments_017684.json:
```json
{
    "body": "Actually, the bug is in the list_function in latex.py in the case where the list string is too long.  I'll post a patch momentarily.",
    "created_at": "2008-03-18T18:42:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2584#issuecomment-17684",
    "user": "jason"
}
```

Actually, the bug is in the list_function in latex.py in the case where the list string is too long.  I'll post a patch momentarily.



---

archive/issue_comments_017685.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-18T18:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2584#issuecomment-17685",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_017686.json:
```json
{
    "body": "I believe the above patch works, but I'm still building 2.10.4, so I haven't tested it yet.",
    "created_at": "2008-03-18T18:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2584#issuecomment-17686",
    "user": "jason"
}
```

I believe the above patch works, but I'm still building 2.10.4, so I haven't tested it yet.



---

archive/issue_comments_017687.json:
```json
{
    "body": "The patch fixes the problem.",
    "created_at": "2008-03-18T20:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2584#issuecomment-17687",
    "user": "jason"
}
```

The patch fixes the problem.



---

archive/issue_comments_017688.json:
```json
{
    "body": "Replying to [comment:4 jason]:\n> The patch fixes the problem.\n\nWhile the patch looks like the fix to this problem shouldn't we also add a doctest that verifies that the bug has been fixed? Not to be pedantic ... well, I am :=)\n\nGreat job Jason.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-18T20:44:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2584#issuecomment-17688",
    "user": "mabshoff"
}
```

Replying to [comment:4 jason]:
> The patch fixes the problem.

While the patch looks like the fix to this problem shouldn't we also add a doctest that verifies that the bug has been fixed? Not to be pedantic ... well, I am :=)

Great job Jason.

Cheers,

Michael



---

archive/issue_comments_017689.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-18T22:53:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2584#issuecomment-17689",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_017690.json:
```json
{
    "body": "I added some doctests; only the last patch should be applied. Positive review from me.",
    "created_at": "2008-03-18T22:54:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2584#issuecomment-17690",
    "user": "mhansen"
}
```

I added some doctests; only the last patch should be applied. Positive review from me.



---

archive/issue_comments_017691.json:
```json
{
    "body": "Merged 2584.patch in Sage 2.11.alpha0 - thanks Mike for the doctest.",
    "created_at": "2008-03-19T00:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2584#issuecomment-17691",
    "user": "mabshoff"
}
```

Merged 2584.patch in Sage 2.11.alpha0 - thanks Mike for the doctest.



---

archive/issue_comments_017692.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-19T00:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2584#issuecomment-17692",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017693.json:
```json
{
    "body": "Thanks, Mike for adding the doctests.  The reason I didn't add doctests to test this fix was that the bug was only manifest in the notebook (in EMBEDDED_MODE).  However, I should have gone ahead and added doctests for the basic functionality anyway, even if they didn't test that the bug in question is fixed, just to get the doctest score up and do my part towards the 3.0 goals :)",
    "created_at": "2008-03-19T00:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2584#issuecomment-17693",
    "user": "jason"
}
```

Thanks, Mike for adding the doctests.  The reason I didn't add doctests to test this fix was that the bug was only manifest in the notebook (in EMBEDDED_MODE).  However, I should have gone ahead and added doctests for the basic functionality anyway, even if they didn't test that the bug in question is fixed, just to get the doctest score up and do my part towards the 3.0 goals :)



---

archive/issue_comments_017694.json:
```json
{
    "body": "Changing priority from minor to trivial.",
    "created_at": "2008-03-19T00:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2584#issuecomment-17694",
    "user": "jason"
}
```

Changing priority from minor to trivial.
