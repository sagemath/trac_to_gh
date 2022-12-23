# Issue 1013: Matrix_real_double_dense overrides parent numpy() method with less-functional version

archive/issues_001013.json:
```json
{
    "body": "Assignee: was\n\nMatrix_real_double_dense and Matrix_complex_double_dense both define a numpy() method that turns the matrix into the appropriate kind of numpy matrix.  However, Matrix defines a numpy() method that takes an optional type argument, to say what kind of matrix to produce.  The specialized classes should also take this optional type argument, and fall back to the slow method defined by Matrix if the type is not 'd' or 'D', respectively.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1013\n\n",
    "created_at": "2007-10-27T22:40:12Z",
    "labels": [
        "linear algebra",
        "minor",
        "enhancement"
    ],
    "title": "Matrix_real_double_dense overrides parent numpy() method with less-functional version",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1013",
    "user": "cwitty"
}
```
Assignee: was

Matrix_real_double_dense and Matrix_complex_double_dense both define a numpy() method that turns the matrix into the appropriate kind of numpy matrix.  However, Matrix defines a numpy() method that takes an optional type argument, to say what kind of matrix to produce.  The specialized classes should also take this optional type argument, and fall back to the slow method defined by Matrix if the type is not 'd' or 'D', respectively.

Issue created by migration from https://trac.sagemath.org/ticket/1013





---

archive/issue_comments_006202.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-14T05:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6202",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006203.json:
```json
{
    "body": "Changing assignee from was to jason.",
    "created_at": "2008-11-14T05:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6203",
    "user": "jason"
}
```

Changing assignee from was to jason.



---

archive/issue_comments_006204.json:
```json
{
    "body": "This should be a modification of Matrix_double_dense now.",
    "created_at": "2008-11-14T05:09:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6204",
    "user": "jason"
}
```

This should be a modification of Matrix_double_dense now.



---

archive/issue_comments_006205.json:
```json
{
    "body": "Jason,\n\ndid you already fix this in some other patch or is this still open?\n\nCheers,\n\nMichael",
    "created_at": "2009-02-09T08:36:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6205",
    "user": "mabshoff"
}
```

Jason,

did you already fix this in some other patch or is this still open?

Cheers,

Michael



---

archive/issue_comments_006206.json:
```json
{
    "body": "No, I haven't fixed it.  It's one of those low-hanging, one-line fixes, though.",
    "created_at": "2009-02-09T13:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6206",
    "user": "jason"
}
```

No, I haven't fixed it.  It's one of those low-hanging, one-line fixes, though.



---

archive/issue_comments_006207.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-08-26T20:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6207",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_006208.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-26T20:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6208",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_006209.json:
```json
{
    "body": "Attachment\n\nSame patch as before but with trailing whitespace removed",
    "created_at": "2012-03-14T15:30:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6209",
    "user": "davidloeffler"
}
```

Attachment

Same patch as before but with trailing whitespace removed



---

archive/issue_comments_006210.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-14T15:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6210",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_006211.json:
```json
{
    "body": "Apply trac_1013-whitespace_removed.patch\n\nLooks good and doctests pass. I'm frankly amazed that this patch has survived for so long without bitrotting.",
    "created_at": "2012-03-14T15:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6211",
    "user": "davidloeffler"
}
```

Apply trac_1013-whitespace_removed.patch

Looks good and doctests pass. I'm frankly amazed that this patch has survived for so long without bitrotting.



---

archive/issue_comments_006212.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-03-23T16:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6212",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_006213.json:
```json
{
    "body": "This needs to be rebased to sage-5.0.beta9:\n\n```\napplying trac_1013-whitespace_removed.patch\npatching file sage/matrix/matrix_double_dense.pyx\nHunk #1 succeeded at 3268 with fuzz 2 (offset 1875 lines).\n```\n",
    "created_at": "2012-03-23T16:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6213",
    "user": "jdemeyer"
}
```

This needs to be rebased to sage-5.0.beta9:

```
applying trac_1013-whitespace_removed.patch
patching file sage/matrix/matrix_double_dense.pyx
Hunk #1 succeeded at 3268 with fuzz 2 (offset 1875 lines).
```




---

archive/issue_comments_006214.json:
```json
{
    "body": "Rebase to 5.0.beta10",
    "created_at": "2012-03-25T13:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6214",
    "user": "davidloeffler"
}
```

Rebase to 5.0.beta10



---

archive/issue_comments_006215.json:
```json
{
    "body": "Attachment\n\nApply trac_1013-rebase.patch\n\nHere's the rebase. Since I didn't actually do anything, just hg import / qpush / refresh / export, I think it's valid for me just to restate the positive review.",
    "created_at": "2012-03-25T13:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6215",
    "user": "davidloeffler"
}
```

Attachment

Apply trac_1013-rebase.patch

Here's the rebase. Since I didn't actually do anything, just hg import / qpush / refresh / export, I think it's valid for me just to restate the positive review.



---

archive/issue_comments_006216.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-03-25T13:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6216",
    "user": "davidloeffler"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_006217.json:
```json
{
    "body": "Replying to [comment:8 davidloeffler]:\n> Apply trac_1013-rebase.patch\n> \n> Here's the rebase. Since I didn't actually do anything, just hg import / qpush / refresh / export, I think it's valid for me just to restate the positive review.\n...provided you did a sanity check that the patch was applied correctly.  1875 lines of offset certainly should raise your eyebrows.",
    "created_at": "2012-03-26T13:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6217",
    "user": "jdemeyer"
}
```

Replying to [comment:8 davidloeffler]:
> Apply trac_1013-rebase.patch
> 
> Here's the rebase. Since I didn't actually do anything, just hg import / qpush / refresh / export, I think it's valid for me just to restate the positive review.
...provided you did a sanity check that the patch was applied correctly.  1875 lines of offset certainly should raise your eyebrows.



---

archive/issue_comments_006218.json:
```json
{
    "body": "Replying to [comment:9 jdemeyer]:\n> Replying to [comment:8 davidloeffler]:\n> > Apply trac_1013-rebase.patch\n> > \n> > Here's the rebase. Since I didn't actually do anything, just hg import / qpush / refresh / export, I think it's valid for me just to restate the positive review.\n> ...provided you did a sanity check that the patch was applied correctly.  1875 lines of offset certainly should raise your eyebrows.\n\nIt did, and I did, and it was fine. :-)",
    "created_at": "2012-03-26T13:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6218",
    "user": "davidloeffler"
}
```

Replying to [comment:9 jdemeyer]:
> Replying to [comment:8 davidloeffler]:
> > Apply trac_1013-rebase.patch
> > 
> > Here's the rebase. Since I didn't actually do anything, just hg import / qpush / refresh / export, I think it's valid for me just to restate the positive review.
> ...provided you did a sanity check that the patch was applied correctly.  1875 lines of offset certainly should raise your eyebrows.

It did, and I did, and it was fine. :-)



---

archive/issue_comments_006219.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-03-28T10:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6219",
    "user": "jdemeyer"
}
```

Resolution: fixed
