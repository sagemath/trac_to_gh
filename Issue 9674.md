# Issue 9674: Please revert sage/crypto/mq/sbox.py [11673:11b2f556827a:12294:d7533ae4895e]

archive/issues_009674.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  malb\n\nRevision sage/crypto/mq/sbox.py [11673:11b2f556827a:12294:d7533ae4895e] (explacing log_b() by exact_log()) causes the following problems:\n\n* difference_distribution_matrix() (in crypto/mq/sbox.py) crashes when an n-to-m bit S-box does not contain the element 2<sup>m-1</sup> (the wrong calculation of m results in an array index going out of bounds).\n\n* the statement length != int(length) is never executed, because exact_log() always outputs an integer\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9674\n\n",
    "created_at": "2010-08-03T12:17:53Z",
    "labels": [
        "cryptography",
        "major",
        "bug"
    ],
    "title": "Please revert sage/crypto/mq/sbox.py [11673:11b2f556827a:12294:d7533ae4895e]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9674",
    "user": "nmouha"
}
```
Assignee: mhansen

CC:  malb

Revision sage/crypto/mq/sbox.py [11673:11b2f556827a:12294:d7533ae4895e] (explacing log_b() by exact_log()) causes the following problems:

* difference_distribution_matrix() (in crypto/mq/sbox.py) crashes when an n-to-m bit S-box does not contain the element 2<sup>m-1</sup> (the wrong calculation of m results in an array index going out of bounds).

* the statement length != int(length) is never executed, because exact_log() always outputs an integer


Issue created by migration from https://trac.sagemath.org/ticket/9674





---

archive/issue_comments_094001.json:
```json
{
    "body": "Does ticket #9366 fix your problem?",
    "created_at": "2010-08-07T13:01:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9674#issuecomment-94001",
    "user": "ylchapuy"
}
```

Does ticket #9366 fix your problem?



---

archive/issue_comments_094002.json:
```json
{
    "body": "Replying to [comment:1 ylchapuy]:\n> Does ticket #9366 fix your problem?\n\nThank you for looking into this. You patch fixes the second bullet point. But the main problem is this line: \"self.n = ZZ(max(S)+1).exact_log(2)\".\n\nTry this, and see what happens:\nS = mq.SBox(5,6,0,3,4,2,1,2);\nS.difference_distribution_matrix();",
    "created_at": "2010-08-07T23:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9674#issuecomment-94002",
    "user": "nmouha"
}
```

Replying to [comment:1 ylchapuy]:
> Does ticket #9366 fix your problem?

Thank you for looking into this. You patch fixes the second bullet point. But the main problem is this line: "self.n = ZZ(max(S)+1).exact_log(2)".

Try this, and see what happens:
S = mq.SBox(5,6,0,3,4,2,1,2);
S.difference_distribution_matrix();



---

archive/issue_comments_094003.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-08T08:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9674#issuecomment-94003",
    "user": "ylchapuy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_094004.json:
```json
{
    "body": "You might review the following patch replacing `exact_log` with `nbits`.",
    "created_at": "2010-08-08T08:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9674#issuecomment-94004",
    "user": "ylchapuy"
}
```

You might review the following patch replacing `exact_log` with `nbits`.



---

archive/issue_comments_094005.json:
```json
{
    "body": "Your proposed patch fixes the problem. I also think it's a cleaner solution than reversing the patch by mhansen. Thanks for your time.",
    "created_at": "2010-08-08T11:08:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9674#issuecomment-94005",
    "user": "nmouha"
}
```

Your proposed patch fixes the problem. I also think it's a cleaner solution than reversing the patch by mhansen. Thanks for your time.



---

archive/issue_comments_094006.json:
```json
{
    "body": "If you are satisfied with the patch, and checked that all the doctests are still ok, then the procedure is to check the action \"positive review\" (bottom of the ticket page if you are logged in) and add yourself to the reviewers.\nThis allows the release manager to consider the merging of this ticket in the next release.",
    "created_at": "2010-08-09T18:33:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9674#issuecomment-94006",
    "user": "ylchapuy"
}
```

If you are satisfied with the patch, and checked that all the doctests are still ok, then the procedure is to check the action "positive review" (bottom of the ticket page if you are logged in) and add yourself to the reviewers.
This allows the release manager to consider the merging of this ticket in the next release.



---

archive/issue_comments_094007.json:
```json
{
    "body": "Maybe Martin will be interrested in reviewing this...",
    "created_at": "2010-08-13T12:29:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9674#issuecomment-94007",
    "user": "ylchapuy"
}
```

Maybe Martin will be interrested in reviewing this...



---

archive/issue_comments_094008.json:
```json
{
    "body": "Patch looks good, doctests pass.",
    "created_at": "2010-08-14T12:58:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9674#issuecomment-94008",
    "user": "malb"
}
```

Patch looks good, doctests pass.



---

archive/issue_comments_094009.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-14T12:58:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9674#issuecomment-94009",
    "user": "malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094010.json:
```json
{
    "body": "Please put the ticket number in the first line of the patch commit string.",
    "created_at": "2010-08-15T09:01:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9674#issuecomment-94010",
    "user": "mpatel"
}
```

Please put the ticket number in the first line of the patch commit string.



---

archive/issue_comments_094011.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-08-15T09:01:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9674#issuecomment-94011",
    "user": "mpatel"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_094012.json:
```json
{
    "body": "Attachment [trac9674_fix_Sbox_init.patch](tarball://root/attachments/some-uuid/ticket9674/trac9674_fix_Sbox_init.patch) by ylchapuy created at 2010-08-15 11:22:30",
    "created_at": "2010-08-15T11:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9674#issuecomment-94012",
    "user": "ylchapuy"
}
```

Attachment [trac9674_fix_Sbox_init.patch](tarball://root/attachments/some-uuid/ticket9674/trac9674_fix_Sbox_init.patch) by ylchapuy created at 2010-08-15 11:22:30



---

archive/issue_comments_094013.json:
```json
{
    "body": "Done, I put it back as positive review directly, I hope it's ok.",
    "created_at": "2010-08-15T11:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9674#issuecomment-94013",
    "user": "ylchapuy"
}
```

Done, I put it back as positive review directly, I hope it's ok.



---

archive/issue_comments_094014.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-08-15T11:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9674#issuecomment-94014",
    "user": "ylchapuy"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_094015.json:
```json
{
    "body": "Sure.  Thanks!",
    "created_at": "2010-08-15T21:18:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9674#issuecomment-94015",
    "user": "mpatel"
}
```

Sure.  Thanks!



---

archive/issue_comments_094016.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T11:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9674#issuecomment-94016",
    "user": "mpatel"
}
```

Resolution: fixed
