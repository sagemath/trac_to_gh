# Issue 5142: [with patch, needs review] speed up elementary_divisors for sparse integer matrices?

archive/issues_005142.json:
```json
{
    "body": "Assignee: was\n\nKeywords: sparse, elementary_divisors\n\nIt seems to me that if mat is a sparse integer matrix, then\n\n```\nmat.dense_matrix().elementary_divisors()\n```\n\nis much faster than \n\n```\nmat.elementary_divisors()\n```\n\nIs this correct?  I've checked this on certain families of matrices, but probably not extensively enough.\n\nIf so, we should change how elementary divisors for sparse integer matrices are computed.  I've patched this, pretty naively, by sticking a new method in matrix_integer_sparse.pyx which just contains the above code.  I would appreciate any comments or corrections.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5142\n\n",
    "created_at": "2009-01-30T22:30:51Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] speed up elementary_divisors for sparse integer matrices?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5142",
    "user": "jhpalmieri"
}
```
Assignee: was

Keywords: sparse, elementary_divisors

It seems to me that if mat is a sparse integer matrix, then

```
mat.dense_matrix().elementary_divisors()
```

is much faster than 

```
mat.elementary_divisors()
```

Is this correct?  I've checked this on certain families of matrices, but probably not extensively enough.

If so, we should change how elementary divisors for sparse integer matrices are computed.  I've patched this, pretty naively, by sticking a new method in matrix_integer_sparse.pyx which just contains the above code.  I would appreciate any comments or corrections.

Issue created by migration from https://trac.sagemath.org/ticket/5142





---

archive/issue_comments_039329.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-30T22:32:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5142#issuecomment-39329",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_039330.json:
```json
{
    "body": "This is a simple patch, but may raise complicated issues:\n\nHere's the situation, as I see it: the code for sparse matrices needs a lot of work, and the particular problem on this ticket is one symptom of this. Right now, if you call elementary_divisors on a sparse matrix, it will likely take a long time, and might even crash. The patch proposes a fix to this -- converting to a dense matrix first.  This will crash, too, for some matrices; I'm guessing that it will crash for strictly fewer matrices than elementary_divisors will.  Therefore this patch is not a terrible idea.\n\nIt is rather makeshift, though.  The *right* thing to do is to rewrite the sparse matrix code so that it works and is faster (and also less buggy -- see #5099, for instance).\n\nThis patch would be a temporary fix.  Is it a good idea to include this now, with the idea to fix it the right way later?  Or is it better to leave less than ideal code there now, first as an encouragement to fix it, and second so that we don't leave a patch like this in as a longterm solution?",
    "created_at": "2009-02-07T16:00:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5142#issuecomment-39330",
    "user": "jhpalmieri"
}
```

This is a simple patch, but may raise complicated issues:

Here's the situation, as I see it: the code for sparse matrices needs a lot of work, and the particular problem on this ticket is one symptom of this. Right now, if you call elementary_divisors on a sparse matrix, it will likely take a long time, and might even crash. The patch proposes a fix to this -- converting to a dense matrix first.  This will crash, too, for some matrices; I'm guessing that it will crash for strictly fewer matrices than elementary_divisors will.  Therefore this patch is not a terrible idea.

It is rather makeshift, though.  The *right* thing to do is to rewrite the sparse matrix code so that it works and is faster (and also less buggy -- see #5099, for instance).

This patch would be a temporary fix.  Is it a good idea to include this now, with the idea to fix it the right way later?  Or is it better to leave less than ideal code there now, first as an encouragement to fix it, and second so that we don't leave a patch like this in as a longterm solution?



---

archive/issue_comments_039331.json:
```json
{
    "body": "Another simple fix that ought to be in 3.3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-08T23:03:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5142#issuecomment-39331",
    "user": "mabshoff"
}
```

Another simple fix that ought to be in 3.3.

Cheers,

Michael



---

archive/issue_comments_039332.json:
```json
{
    "body": "Changing assignee from was to jhpalmieri.",
    "created_at": "2009-02-09T00:33:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5142#issuecomment-39332",
    "user": "jhpalmieri"
}
```

Changing assignee from was to jhpalmieri.



---

archive/issue_comments_039333.json:
```json
{
    "body": "Hi John,\n\nthis patch does not apply to my 3.3.rc0 merge tree. Please try to rebase it against 3.3.alpha6:\n\n```\nsage-3.3.rc0/devel/sage$ patch -p1 < trac_5142.patch \npatching file sage/matrix/matrix_integer_sparse.pyx\nHunk #1 FAILED at 296.\n1 out of 1 hunk FAILED -- saving rejects to file sage/matrix/matrix_integer_sparse.pyx.rej\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-02-09T12:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5142#issuecomment-39333",
    "user": "mabshoff"
}
```

Hi John,

this patch does not apply to my 3.3.rc0 merge tree. Please try to rebase it against 3.3.alpha6:

```
sage-3.3.rc0/devel/sage$ patch -p1 < trac_5142.patch 
patching file sage/matrix/matrix_integer_sparse.pyx
Hunk #1 FAILED at 296.
1 out of 1 hunk FAILED -- saving rejects to file sage/matrix/matrix_integer_sparse.pyx.rej
```


Cheers,

Michael



---

archive/issue_comments_039334.json:
```json
{
    "body": "Attachment\n\nrebased against 3.3.alpha6",
    "created_at": "2009-02-09T16:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5142#issuecomment-39334",
    "user": "jhpalmieri"
}
```

Attachment

rebased against 3.3.alpha6



---

archive/issue_comments_039335.json:
```json
{
    "body": "The new patch is just a rebase against 3.3.alpha6.",
    "created_at": "2009-02-09T16:45:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5142#issuecomment-39335",
    "user": "jhpalmieri"
}
```

The new patch is just a rebase against 3.3.alpha6.



---

archive/issue_comments_039336.json:
```json
{
    "body": "The patch looks good; I have three complaints regarding the docstring:\n\n* in the description of the algorithm 'pari', you presumably mean \"works robustly\", since \"works robustless\" doesn't mean anything\n* this is a one-line method, and it is pretty self-explanatory, so I don't think it needs a description of the implementation in the docstring\n* the OUTPUT description claims that the method returns a list of int's; this is not true, since the output is a list of Integer's\n\nI'll very happily give this a positive review once these issues are resolved.  This patch is a good idea and, as John points out, similar things should be done for other methods for sparse matrices (determinant is another example).  For the record, trying\n\n\n```\nsage: A = random_matrix(ZZ, 100, 100, sparse=True)\nsage: time e = A.elementary_divisors()\n```\n\n\nsimply fails with a mysterious TypeError in the current code, whereas with the patch applied it works in 1.44 seconds.",
    "created_at": "2009-02-10T13:08:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5142#issuecomment-39336",
    "user": "AlexGhitza"
}
```

The patch looks good; I have three complaints regarding the docstring:

* in the description of the algorithm 'pari', you presumably mean "works robustly", since "works robustless" doesn't mean anything
* this is a one-line method, and it is pretty self-explanatory, so I don't think it needs a description of the implementation in the docstring
* the OUTPUT description claims that the method returns a list of int's; this is not true, since the output is a list of Integer's

I'll very happily give this a positive review once these issues are resolved.  This patch is a good idea and, as John points out, similar things should be done for other methods for sparse matrices (determinant is another example).  For the record, trying


```
sage: A = random_matrix(ZZ, 100, 100, sparse=True)
sage: time e = A.elementary_divisors()
```


simply fails with a mysterious TypeError in the current code, whereas with the patch applied it works in 1.44 seconds.



---

archive/issue_comments_039337.json:
```json
{
    "body": "Attachment\n\nonly apply this patch",
    "created_at": "2009-02-10T18:00:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5142#issuecomment-39337",
    "user": "jhpalmieri"
}
```

Attachment

only apply this patch



---

archive/issue_comments_039338.json:
```json
{
    "body": "Thanks for the comments.  Here is a new patch which addresses them.\n\nIt also makes another change: my docstring for elementary_divisors was just copied from the docstring for the version in matrix_integer_dense, so since you pointed out the issues with my new docstring, I thought I should change that one, too.  I made one change to the old docstring in addition to the ones you suggested: I deleted the paragraph which suggests that we use linbox.  (We haven't used linbox for elementary_divisors for almost two years.)",
    "created_at": "2009-02-10T18:04:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5142#issuecomment-39338",
    "user": "jhpalmieri"
}
```

Thanks for the comments.  Here is a new patch which addresses them.

It also makes another change: my docstring for elementary_divisors was just copied from the docstring for the version in matrix_integer_dense, so since you pointed out the issues with my new docstring, I thought I should change that one, too.  I made one change to the old docstring in addition to the ones you suggested: I deleted the paragraph which suggests that we use linbox.  (We haven't used linbox for elementary_divisors for almost two years.)



---

archive/issue_comments_039339.json:
```json
{
    "body": "Good stuff.\n\nI'm upgrading this to a critical bug, due to the fact that it's not just a question of speed, but it also fails (see the example above).",
    "created_at": "2009-02-10T22:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5142#issuecomment-39339",
    "user": "AlexGhitza"
}
```

Good stuff.

I'm upgrading this to a critical bug, due to the fact that it's not just a question of speed, but it also fails (see the example above).



---

archive/issue_comments_039340.json:
```json
{
    "body": "Changing priority from minor to critical.",
    "created_at": "2009-02-10T22:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5142#issuecomment-39340",
    "user": "AlexGhitza"
}
```

Changing priority from minor to critical.



---

archive/issue_comments_039341.json:
```json
{
    "body": "Merged in Sage 3.3.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-11T04:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5142#issuecomment-39341",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc0.

Cheers,

Michael



---

archive/issue_comments_039342.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-11T04:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5142#issuecomment-39342",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039343.json:
```json
{
    "body": "As John pointed out in http://groups.google.com/group/sage-devel/t/312339a77bf58908: I merged 5142-rebased.patch instead of 5142-new.patch. So I reverted 5142-rebased.patch and merged 5142-new.patch in 3.3.rc1. Sorry for the screwup.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-11T22:16:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5142#issuecomment-39343",
    "user": "mabshoff"
}
```

As John pointed out in http://groups.google.com/group/sage-devel/t/312339a77bf58908: I merged 5142-rebased.patch instead of 5142-new.patch. So I reverted 5142-rebased.patch and merged 5142-new.patch in 3.3.rc1. Sorry for the screwup.

Cheers,

Michael
