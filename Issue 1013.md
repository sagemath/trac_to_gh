# Issue 1013: Matrix_real_double_dense overrides parent numpy() method with less-functional version

archive/issues_001013.json:
```json
{
    "body": "Assignee: @williamstein\n\nMatrix_real_double_dense and Matrix_complex_double_dense both define a numpy() method that turns the matrix into the appropriate kind of numpy matrix.  However, Matrix defines a numpy() method that takes an optional type argument, to say what kind of matrix to produce.  The specialized classes should also take this optional type argument, and fall back to the slow method defined by Matrix if the type is not 'd' or 'D', respectively.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1013\n\n",
    "created_at": "2007-10-27T22:40:12Z",
    "labels": [
        "component: linear algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "Matrix_real_double_dense overrides parent numpy() method with less-functional version",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1013",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

Matrix_real_double_dense and Matrix_complex_double_dense both define a numpy() method that turns the matrix into the appropriate kind of numpy matrix.  However, Matrix defines a numpy() method that takes an optional type argument, to say what kind of matrix to produce.  The specialized classes should also take this optional type argument, and fall back to the slow method defined by Matrix if the type is not 'd' or 'D', respectively.

Issue created by migration from https://trac.sagemath.org/ticket/1013





---

archive/issue_comments_006182.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-14T05:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6182",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006183.json:
```json
{
    "body": "Changing assignee from @williamstein to @jasongrout.",
    "created_at": "2008-11-14T05:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6183",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @williamstein to @jasongrout.



---

archive/issue_comments_006184.json:
```json
{
    "body": "This should be a modification of Matrix_double_dense now.",
    "created_at": "2008-11-14T05:09:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6184",
    "user": "https://github.com/jasongrout"
}
```

This should be a modification of Matrix_double_dense now.



---

archive/issue_comments_006185.json:
```json
{
    "body": "Jason,\n\ndid you already fix this in some other patch or is this still open?\n\nCheers,\n\nMichael",
    "created_at": "2009-02-09T08:36:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6185",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Jason,

did you already fix this in some other patch or is this still open?

Cheers,

Michael



---

archive/issue_comments_006186.json:
```json
{
    "body": "No, I haven't fixed it.  It's one of those low-hanging, one-line fixes, though.",
    "created_at": "2009-02-09T13:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6186",
    "user": "https://github.com/jasongrout"
}
```

No, I haven't fixed it.  It's one of those low-hanging, one-line fixes, though.



---

archive/issue_comments_006187.json:
```json
{
    "body": "Attachment [trac_1013.patch](tarball://root/attachments/some-uuid/ticket1013/trac_1013.patch) by @mwhansen created at 2010-08-26 20:11:50",
    "created_at": "2010-08-26T20:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6187",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_1013.patch](tarball://root/attachments/some-uuid/ticket1013/trac_1013.patch) by @mwhansen created at 2010-08-26 20:11:50



---

archive/issue_comments_006188.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-26T20:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6188",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_006189.json:
```json
{
    "body": "Attachment [trac_1013-whitespace_removed.patch](tarball://root/attachments/some-uuid/ticket1013/trac_1013-whitespace_removed.patch) by @loefflerd created at 2012-03-14 15:30:59\n\nSame patch as before but with trailing whitespace removed",
    "created_at": "2012-03-14T15:30:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6189",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_1013-whitespace_removed.patch](tarball://root/attachments/some-uuid/ticket1013/trac_1013-whitespace_removed.patch) by @loefflerd created at 2012-03-14 15:30:59

Same patch as before but with trailing whitespace removed



---

archive/issue_comments_006190.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-14T15:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6190",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_006191.json:
```json
{
    "body": "Apply trac_1013-whitespace_removed.patch\n\nLooks good and doctests pass. I'm frankly amazed that this patch has survived for so long without bitrotting.",
    "created_at": "2012-03-14T15:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6191",
    "user": "https://github.com/loefflerd"
}
```

Apply trac_1013-whitespace_removed.patch

Looks good and doctests pass. I'm frankly amazed that this patch has survived for so long without bitrotting.



---

archive/issue_comments_006192.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-03-23T16:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6192",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_006193.json:
```json
{
    "body": "This needs to be rebased to sage-5.0.beta9:\n\n```\napplying trac_1013-whitespace_removed.patch\npatching file sage/matrix/matrix_double_dense.pyx\nHunk #1 succeeded at 3268 with fuzz 2 (offset 1875 lines).\n```\n",
    "created_at": "2012-03-23T16:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6193",
    "user": "https://github.com/jdemeyer"
}
```

This needs to be rebased to sage-5.0.beta9:

```
applying trac_1013-whitespace_removed.patch
patching file sage/matrix/matrix_double_dense.pyx
Hunk #1 succeeded at 3268 with fuzz 2 (offset 1875 lines).
```




---

archive/issue_comments_006194.json:
```json
{
    "body": "Rebase to 5.0.beta10",
    "created_at": "2012-03-25T13:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6194",
    "user": "https://github.com/loefflerd"
}
```

Rebase to 5.0.beta10



---

archive/issue_comments_006195.json:
```json
{
    "body": "Attachment [trac_1013-rebase.patch](tarball://root/attachments/some-uuid/ticket1013/trac_1013-rebase.patch) by @loefflerd created at 2012-03-25 13:33:09\n\nApply trac_1013-rebase.patch\n\nHere's the rebase. Since I didn't actually do anything, just hg import / qpush / refresh / export, I think it's valid for me just to restate the positive review.",
    "created_at": "2012-03-25T13:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6195",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_1013-rebase.patch](tarball://root/attachments/some-uuid/ticket1013/trac_1013-rebase.patch) by @loefflerd created at 2012-03-25 13:33:09

Apply trac_1013-rebase.patch

Here's the rebase. Since I didn't actually do anything, just hg import / qpush / refresh / export, I think it's valid for me just to restate the positive review.



---

archive/issue_comments_006196.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-03-25T13:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6196",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_006197.json:
```json
{
    "body": "Replying to [comment:8 davidloeffler]:\n> Apply trac_1013-rebase.patch\n> \n> Here's the rebase. Since I didn't actually do anything, just hg import / qpush / refresh / export, I think it's valid for me just to restate the positive review.\n...provided you did a sanity check that the patch was applied correctly.  1875 lines of offset certainly should raise your eyebrows.",
    "created_at": "2012-03-26T13:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6197",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:8 davidloeffler]:
> Apply trac_1013-rebase.patch
> 
> Here's the rebase. Since I didn't actually do anything, just hg import / qpush / refresh / export, I think it's valid for me just to restate the positive review.
...provided you did a sanity check that the patch was applied correctly.  1875 lines of offset certainly should raise your eyebrows.



---

archive/issue_comments_006198.json:
```json
{
    "body": "Replying to [comment:9 jdemeyer]:\n> Replying to [comment:8 davidloeffler]:\n> > Apply trac_1013-rebase.patch\n> > \n> > Here's the rebase. Since I didn't actually do anything, just hg import / qpush / refresh / export, I think it's valid for me just to restate the positive review.\n> ...provided you did a sanity check that the patch was applied correctly.  1875 lines of offset certainly should raise your eyebrows.\n\nIt did, and I did, and it was fine. :-)",
    "created_at": "2012-03-26T13:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6198",
    "user": "https://github.com/loefflerd"
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

archive/issue_comments_006199.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-03-28T10:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1013#issuecomment-6199",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_001137.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2012-03-28T10:02:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1013",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1013#event-1137"
}
```
