# Issue 8617: Add galrep by Drew Sutherland to Sage

archive/issues_008617.json:
```json
{
    "body": "Assignee: davidloeffler\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8617\n\n",
    "created_at": "2010-03-27T23:25:24Z",
    "labels": [
        "number fields",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Add galrep by Drew Sutherland to Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8617",
    "user": "was"
}
```
Assignee: davidloeffler



Issue created by migration from https://trac.sagemath.org/ticket/8617





---

archive/issue_comments_078085.json:
```json
{
    "body": "Attachment [trac_8617.patch](tarball://root/attachments/some-uuid/ticket8617/trac_8617.patch) by was created at 2010-03-27 23:25:55",
    "created_at": "2010-03-27T23:25:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-78085",
    "user": "was"
}
```

Attachment [trac_8617.patch](tarball://root/attachments/some-uuid/ticket8617/trac_8617.patch) by was created at 2010-03-27 23:25:55



---

archive/issue_comments_078086.json:
```json
{
    "body": "Attachment [galrep_gl2data.dat](tarball://root/attachments/some-uuid/ticket8617/galrep_gl2data.dat) by was created at 2010-03-27 23:26:31",
    "created_at": "2010-03-27T23:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-78086",
    "user": "was"
}
```

Attachment [galrep_gl2data.dat](tarball://root/attachments/some-uuid/ticket8617/galrep_gl2data.dat) by was created at 2010-03-27 23:26:31



---

archive/issue_comments_078087.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-27T23:27:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-78087",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078088.json:
```json
{
    "body": "This looks malformed -- there is no galrep.c code included in the patch (that I can see).",
    "created_at": "2010-03-30T22:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-78088",
    "user": "ncalexan"
}
```

This looks malformed -- there is no galrep.c code included in the patch (that I can see).



---

archive/issue_comments_078089.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-27T23:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-78089",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_078090.json:
```json
{
    "body": "Attachment [trac_8617-part2.patch](tarball://root/attachments/some-uuid/ticket8617/trac_8617-part2.patch) by rlm created at 2010-05-27 23:12:50\n\nI will review this ticket, as long as someone else makes the necessary changes to the extcode spkg to include the `galrep_*.dat` files in the appropriate manner.",
    "created_at": "2010-05-27T23:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-78090",
    "user": "rlm"
}
```

Attachment [trac_8617-part2.patch](tarball://root/attachments/some-uuid/ticket8617/trac_8617-part2.patch) by rlm created at 2010-05-27 23:12:50

I will review this ticket, as long as someone else makes the necessary changes to the extcode spkg to include the `galrep_*.dat` files in the appropriate manner.



---

archive/issue_comments_078091.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-15T20:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-78091",
    "user": "rlm"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078092.json:
```json
{
    "body": "Attachment [trac_8617-part3.patch](tarball://root/attachments/some-uuid/ticket8617/trac_8617-part3.patch) by rlm created at 2010-06-17 17:04:06\n\nPS - I don't think this is quite the right way to update extcode... I didn't realize I had done 'alpha0' --> 'alpha1'. I suppose the release manager would just add the \"galrep\" directory to the data/extcode directory, which would then be included in the new extcode spkg automatically by the dist script (Is this correct?)",
    "created_at": "2010-06-17T17:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-78092",
    "user": "rlm"
}
```

Attachment [trac_8617-part3.patch](tarball://root/attachments/some-uuid/ticket8617/trac_8617-part3.patch) by rlm created at 2010-06-17 17:04:06

PS - I don't think this is quite the right way to update extcode... I didn't realize I had done 'alpha0' --> 'alpha1'. I suppose the release manager would just add the "galrep" directory to the data/extcode directory, which would then be included in the new extcode spkg automatically by the dist script (Is this correct?)



---

archive/issue_comments_078093.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-24T20:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-78093",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078094.json:
```json
{
    "body": "Since I'm doing release management for sage-4.5, I can just merge the files here the right way, and since I haven't actually contributed anything, I feel as if I can give it a positive review as is.",
    "created_at": "2010-06-24T20:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-78094",
    "user": "rlm"
}
```

Since I'm doing release management for sage-4.5, I can just merge the files here the right way, and since I haven't actually contributed anything, I feel as if I can give it a positive review as is.



---

archive/issue_comments_078095.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-06T03:27:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-78095",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_078096.json:
```json
{
    "body": "I'm reverting this ticket, as it causes several weird problems: see #9445 and #9490.",
    "created_at": "2010-07-13T16:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-78096",
    "user": "rlm"
}
```

I'm reverting this ticket, as it causes several weird problems: see #9445 and #9490.



---

archive/issue_comments_078097.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-07-13T16:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-78097",
    "user": "rlm"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_078098.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-07-13T16:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-78098",
    "user": "rlm"
}
```

Changing status from closed to new.



---

archive/issue_comments_078099.json:
```json
{
    "body": "Removed `$SAGE_ROOT/data/extcode/galrep`, as well as the relevant lines from `module_list.py`, `sage/libs/all.py`, `setup.py` and deleted `sage/libs/galrep`.\n\n:-(",
    "created_at": "2010-07-13T16:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-78099",
    "user": "rlm"
}
```

Removed `$SAGE_ROOT/data/extcode/galrep`, as well as the relevant lines from `module_list.py`, `sage/libs/all.py`, `setup.py` and deleted `sage/libs/galrep`.

:-(



---

archive/issue_comments_078100.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-07-13T16:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-78100",
    "user": "rlm"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_078101.json:
```json
{
    "body": "Note - I plan to include this in PSAGE: http://code.google.com/p/purplesage/issues/detail?id=10",
    "created_at": "2010-11-17T02:09:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-78101",
    "user": "was"
}
```

Note - I plan to include this in PSAGE: http://code.google.com/p/purplesage/issues/detail?id=10
