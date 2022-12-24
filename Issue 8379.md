# Issue 8379: add arithmetic for Boolean functions

archive/issues_008379.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  malb\n\nwe define:\n\n* `~` : returns the complement Boolean function\n* `+`,`*` : corresponds to the same op. on the ANFs\n* `|` : concatenate the truth tables ( used for various constructions, e.g. http://eprint.iacr.org/2009/134.pdf )\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8379\n\n",
    "created_at": "2010-02-26T13:21:45Z",
    "labels": [
        "cryptography",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "add arithmetic for Boolean functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8379",
    "user": "ylchapuy"
}
```
Assignee: mvngu

CC:  malb

we define:

* `~` : returns the complement Boolean function
* `+`,`*` : corresponds to the same op. on the ANFs
* `|` : concatenate the truth tables ( used for various constructions, e.g. http://eprint.iacr.org/2009/134.pdf )


Issue created by migration from https://trac.sagemath.org/ticket/8379





---

archive/issue_comments_074920.json:
```json
{
    "body": "Attachment [trac_8379.patch](tarball://root/attachments/some-uuid/ticket8379/trac_8379.patch) by ylchapuy created at 2010-02-26 13:22:52",
    "created_at": "2010-02-26T13:22:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8379#issuecomment-74920",
    "user": "ylchapuy"
}
```

Attachment [trac_8379.patch](tarball://root/attachments/some-uuid/ticket8379/trac_8379.patch) by ylchapuy created at 2010-02-26 13:22:52



---

archive/issue_comments_074921.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-26T13:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8379#issuecomment-74921",
    "user": "ylchapuy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074922.json:
```json
{
    "body": "The provided patch also correct a bug in the computation of the algebraic immunity.",
    "created_at": "2010-02-26T13:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8379#issuecomment-74922",
    "user": "ylchapuy"
}
```

The provided patch also correct a bug in the computation of the algebraic immunity.



---

archive/issue_comments_074923.json:
```json
{
    "body": "The patch looks good (I'll run doctests once my update is done) but we usually do not implement `__iadd__` and `__imul__` since objects in Sage are generally supposed to be immutable. There are some exceptions like matrices where this wouldn't make any sense.",
    "created_at": "2010-04-05T16:35:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8379#issuecomment-74923",
    "user": "malb"
}
```

The patch looks good (I'll run doctests once my update is done) but we usually do not implement `__iadd__` and `__imul__` since objects in Sage are generally supposed to be immutable. There are some exceptions like matrices where this wouldn't make any sense.



---

archive/issue_comments_074924.json:
```json
{
    "body": "Doctests pass. Thust for a positive review from me all that's needed would be to either remove `__iadd__` or to give a justification why this class should be an exception.",
    "created_at": "2010-04-05T18:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8379#issuecomment-74924",
    "user": "malb"
}
```

Doctests pass. Thust for a positive review from me all that's needed would be to either remove `__iadd__` or to give a justification why this class should be an exception.



---

archive/issue_comments_074925.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-04-28T20:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8379#issuecomment-74925",
    "user": "wdj"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_074926.json:
```json
{
    "body": "ylchapuy?",
    "created_at": "2010-04-28T20:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8379#issuecomment-74926",
    "user": "wdj"
}
```

ylchapuy?



---

archive/issue_comments_074927.json:
```json
{
    "body": "Attachment [trac_8379_v2.patch](tarball://root/attachments/some-uuid/ticket8379/trac_8379_v2.patch) by ylchapuy created at 2010-05-04 12:53:12\n\napply only this one",
    "created_at": "2010-05-04T12:53:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8379#issuecomment-74927",
    "user": "ylchapuy"
}
```

Attachment [trac_8379_v2.patch](tarball://root/attachments/some-uuid/ticket8379/trac_8379_v2.patch) by ylchapuy created at 2010-05-04 12:53:12

apply only this one



---

archive/issue_comments_074928.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-05-04T12:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8379#issuecomment-74928",
    "user": "ylchapuy"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_074929.json:
```json
{
    "body": "Patch updated. I removed the inplace versions `__iadd__` and `__imul__`.\n\nApply only the last patch.\n\n(and sorry for the delay, I'm quite busy those days...)",
    "created_at": "2010-05-04T12:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8379#issuecomment-74929",
    "user": "ylchapuy"
}
```

Patch updated. I removed the inplace versions `__iadd__` and `__imul__`.

Apply only the last patch.

(and sorry for the delay, I'm quite busy those days...)



---

archive/issue_comments_074930.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-02T20:58:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8379#issuecomment-74930",
    "user": "malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074931.json:
```json
{
    "body": "Patch looks good, applies cleanly, doctests pass on sage.math",
    "created_at": "2010-06-02T20:58:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8379#issuecomment-74931",
    "user": "malb"
}
```

Patch looks good, applies cleanly, doctests pass on sage.math



---

archive/issue_comments_074932.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T08:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8379#issuecomment-74932",
    "user": "mhansen"
}
```

Resolution: fixed
