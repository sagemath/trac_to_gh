# Issue 5392: relative number field subfield method -- unclear documentation

archive/issues_005392.json:
```json
{
    "body": "Assignee: @loefflerd\n\nKeywords: sd51\n\nConsider\n\n```\nsage: R.<a> = NumberField(x^4 - 2*x^2 - 1)\nsage: S.<i> = R.extension(x^2 + 1)\nsage: S.subfield(a + i/a)\n```\n\nThe S.subfield method documentation says that it constructs QQ(alpha), but this is false, I think it constructs R(alpha). In the above example, S.subfield(a + i/a) returns a number field of degree 8 over Q, whereas a + i/a has degree 4 over QQ (the minimal polynomial is `x^4 - 4x^2 + 8`).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5392\n\n",
    "closed_at": "2013-07-31T12:53:02Z",
    "created_at": "2009-02-27T16:03:04Z",
    "labels": [
        "component: number fields",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.11",
    "title": "relative number field subfield method -- unclear documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5392",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: @loefflerd

Keywords: sd51

Consider

```
sage: R.<a> = NumberField(x^4 - 2*x^2 - 1)
sage: S.<i> = R.extension(x^2 + 1)
sage: S.subfield(a + i/a)
```

The S.subfield method documentation says that it constructs QQ(alpha), but this is false, I think it constructs R(alpha). In the above example, S.subfield(a + i/a) returns a number field of degree 8 over Q, whereas a + i/a has degree 4 over QQ (the minimal polynomial is `x^4 - 4x^2 + 8`).


Issue created by migration from https://trac.sagemath.org/ticket/5392





---

archive/issue_events_012567.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-27T16:17:16Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5392",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5392#event-12567"
}
```



---

archive/issue_comments_041439.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-20T20:32:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5392#issuecomment-41439",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_041440.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-20T20:32:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5392#issuecomment-41440",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_041441.json:
```json
{
    "body": "patch against sage 5.10",
    "created_at": "2013-07-23T13:23:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5392#issuecomment-41441",
    "user": "https://trac.sagemath.org/admin/accounts/users/ArgaezG"
}
```

patch against sage 5.10



---

archive/issue_comments_041442.json:
```json
{
    "body": "Attachment [trac_5392.patch](tarball://root/attachments/some-uuid/ticket5392/trac_5392.patch) by ArgaezG created at 2013-07-23 13:24:34",
    "created_at": "2013-07-23T13:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5392#issuecomment-41442",
    "user": "https://trac.sagemath.org/admin/accounts/users/ArgaezG"
}
```

Attachment [trac_5392.patch](tarball://root/attachments/some-uuid/ticket5392/trac_5392.patch) by ArgaezG created at 2013-07-23 13:24:34



---

archive/issue_comments_041443.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-07-23T13:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5392#issuecomment-41443",
    "user": "https://trac.sagemath.org/admin/accounts/users/ArgaezG"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_041444.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd51\".",
    "created_at": "2013-07-23T14:18:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5392#issuecomment-41444",
    "user": "https://trac.sagemath.org/admin/accounts/users/mkosters"
}
```

Changing keywords from "" to "sd51".



---

archive/issue_comments_041445.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-07-23T15:45:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5392#issuecomment-41445",
    "user": "https://trac.sagemath.org/admin/accounts/users/ArgaezG"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_041446.json:
```json
{
    "body": "I happy with changes suggested by Michiel, and he is happy with mine.",
    "created_at": "2013-07-23T15:45:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5392#issuecomment-41446",
    "user": "https://trac.sagemath.org/admin/accounts/users/ArgaezG"
}
```

I happy with changes suggested by Michiel, and he is happy with mine.



---

archive/issue_comments_041447.json:
```json
{
    "body": "Apply trac_5392_subfield_review.patch after trac_5392.patch\u200b",
    "created_at": "2013-07-23T18:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5392#issuecomment-41447",
    "user": "https://trac.sagemath.org/admin/accounts/users/mkosters"
}
```

Apply trac_5392_subfield_review.patch after trac_5392.patch​



---

archive/issue_comments_041448.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-07-24T07:31:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5392#issuecomment-41448",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_041449.json:
```json
{
    "body": "The reviewer patch needs a proper commit message, use `hg qrefresh -e` for this.",
    "created_at": "2013-07-24T07:31:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5392#issuecomment-41449",
    "user": "https://github.com/jdemeyer"
}
```

The reviewer patch needs a proper commit message, use `hg qrefresh -e` for this.



---

archive/issue_comments_041450.json:
```json
{
    "body": "Attachment [trac_5392_subfield_review.patch](tarball://root/attachments/some-uuid/ticket5392/trac_5392_subfield_review.patch) by mkosters created at 2013-07-24 07:59:40\n\n`@`jdemeyer: is it correct now?",
    "created_at": "2013-07-24T07:59:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5392#issuecomment-41450",
    "user": "https://trac.sagemath.org/admin/accounts/users/mkosters"
}
```

Attachment [trac_5392_subfield_review.patch](tarball://root/attachments/some-uuid/ticket5392/trac_5392_subfield_review.patch) by mkosters created at 2013-07-24 07:59:40

`@`jdemeyer: is it correct now?



---

archive/issue_comments_041451.json:
```json
{
    "body": "Replying to [comment:8 mkosters]:\n> `@`jdemeyer: is it correct now?\n\n\nIt has a proper commit message now. So assuming this is the same patch, I'll put this to positive review again.",
    "created_at": "2013-07-24T08:45:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5392#issuecomment-41451",
    "user": "https://github.com/mstreng"
}
```

Replying to [comment:8 mkosters]:
> `@`jdemeyer: is it correct now?


It has a proper commit message now. So assuming this is the same patch, I'll put this to positive review again.



---

archive/issue_comments_041452.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2013-07-24T08:45:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5392#issuecomment-41452",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_events_012568.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-07-31T12:53:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5392",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5392#event-12568"
}
```



---

archive/issue_comments_041453.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-07-31T12:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5392#issuecomment-41453",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
