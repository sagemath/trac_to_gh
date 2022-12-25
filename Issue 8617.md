# Issue 8617: Add galrep by Drew Sutherland to Sage

archive/issues_008617.json:
```json
{
    "body": "Assignee: @loefflerd\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8617\n\n",
    "created_at": "2010-03-27T23:25:24Z",
    "labels": [
        "component: number fields"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Add galrep by Drew Sutherland to Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8617",
    "user": "https://github.com/williamstein"
}
```
Assignee: @loefflerd



Issue created by migration from https://trac.sagemath.org/ticket/8617





---

archive/issue_comments_077957.json:
```json
{
    "body": "Attachment [trac_8617.patch](tarball://root/attachments/some-uuid/ticket8617/trac_8617.patch) by @williamstein created at 2010-03-27 23:25:55",
    "created_at": "2010-03-27T23:25:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-77957",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_8617.patch](tarball://root/attachments/some-uuid/ticket8617/trac_8617.patch) by @williamstein created at 2010-03-27 23:25:55



---

archive/issue_comments_077958.json:
```json
{
    "body": "Attachment [galrep_gl2data.dat](tarball://root/attachments/some-uuid/ticket8617/galrep_gl2data.dat) by @williamstein created at 2010-03-27 23:26:31",
    "created_at": "2010-03-27T23:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-77958",
    "user": "https://github.com/williamstein"
}
```

Attachment [galrep_gl2data.dat](tarball://root/attachments/some-uuid/ticket8617/galrep_gl2data.dat) by @williamstein created at 2010-03-27 23:26:31



---

archive/issue_comments_077959.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-27T23:27:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-77959",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077960.json:
```json
{
    "body": "This looks malformed -- there is no galrep.c code included in the patch (that I can see).",
    "created_at": "2010-03-30T22:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-77960",
    "user": "https://github.com/ncalexan"
}
```

This looks malformed -- there is no galrep.c code included in the patch (that I can see).



---

archive/issue_comments_077961.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-27T23:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-77961",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_077962.json:
```json
{
    "body": "Attachment [trac_8617-part2.patch](tarball://root/attachments/some-uuid/ticket8617/trac_8617-part2.patch) by @rlmill created at 2010-05-27 23:12:50\n\nI will review this ticket, as long as someone else makes the necessary changes to the extcode spkg to include the `galrep_*.dat` files in the appropriate manner.",
    "created_at": "2010-05-27T23:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-77962",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_8617-part2.patch](tarball://root/attachments/some-uuid/ticket8617/trac_8617-part2.patch) by @rlmill created at 2010-05-27 23:12:50

I will review this ticket, as long as someone else makes the necessary changes to the extcode spkg to include the `galrep_*.dat` files in the appropriate manner.



---

archive/issue_comments_077963.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-15T20:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-77963",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_077964.json:
```json
{
    "body": "Attachment [trac_8617-part3.patch](tarball://root/attachments/some-uuid/ticket8617/trac_8617-part3.patch) by @rlmill created at 2010-06-17 17:04:06\n\nPS - I don't think this is quite the right way to update extcode... I didn't realize I had done 'alpha0' --> 'alpha1'. I suppose the release manager would just add the \"galrep\" directory to the data/extcode directory, which would then be included in the new extcode spkg automatically by the dist script (Is this correct?)",
    "created_at": "2010-06-17T17:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-77964",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_8617-part3.patch](tarball://root/attachments/some-uuid/ticket8617/trac_8617-part3.patch) by @rlmill created at 2010-06-17 17:04:06

PS - I don't think this is quite the right way to update extcode... I didn't realize I had done 'alpha0' --> 'alpha1'. I suppose the release manager would just add the "galrep" directory to the data/extcode directory, which would then be included in the new extcode spkg automatically by the dist script (Is this correct?)



---

archive/issue_comments_077965.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-24T20:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-77965",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077966.json:
```json
{
    "body": "Since I'm doing release management for sage-4.5, I can just merge the files here the right way, and since I haven't actually contributed anything, I feel as if I can give it a positive review as is.",
    "created_at": "2010-06-24T20:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-77966",
    "user": "https://github.com/rlmill"
}
```

Since I'm doing release management for sage-4.5, I can just merge the files here the right way, and since I haven't actually contributed anything, I feel as if I can give it a positive review as is.



---

archive/issue_comments_077967.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-06T03:27:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-77967",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_008787.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-07-06T03:27:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8617#event-8787"
}
```



---

archive/issue_comments_077968.json:
```json
{
    "body": "I'm reverting this ticket, as it causes several weird problems: see #9445 and #9490.",
    "created_at": "2010-07-13T16:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-77968",
    "user": "https://github.com/rlmill"
}
```

I'm reverting this ticket, as it causes several weird problems: see #9445 and #9490.



---

archive/issue_comments_077969.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-07-13T16:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-77969",
    "user": "https://github.com/rlmill"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_077970.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-07-13T16:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-77970",
    "user": "https://github.com/rlmill"
}
```

Changing status from closed to new.



---

archive/issue_events_008788.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-07-13T16:41:37Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8617#event-8788"
}
```



---

archive/issue_comments_077971.json:
```json
{
    "body": "Removed `$SAGE_ROOT/data/extcode/galrep`, as well as the relevant lines from `module_list.py`, `sage/libs/all.py`, `setup.py` and deleted `sage/libs/galrep`.\n\n:-(",
    "created_at": "2010-07-13T16:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-77971",
    "user": "https://github.com/rlmill"
}
```

Removed `$SAGE_ROOT/data/extcode/galrep`, as well as the relevant lines from `module_list.py`, `sage/libs/all.py`, `setup.py` and deleted `sage/libs/galrep`.

:-(



---

archive/issue_comments_077972.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-07-13T16:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-77972",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_077973.json:
```json
{
    "body": "Note - I plan to include this in PSAGE: http://code.google.com/p/purplesage/issues/detail?id=10",
    "created_at": "2010-11-17T02:09:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8617#issuecomment-77973",
    "user": "https://github.com/williamstein"
}
```

Note - I plan to include this in PSAGE: http://code.google.com/p/purplesage/issues/detail?id=10
