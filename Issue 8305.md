# Issue 8305: Improve documentation of Monsky-Washnitzer code

archive/issues_008305.json:
```json
{
    "body": "Assignee: cremona\n\nCC:  jpflori\n\nKeywords: Monsky-Washnitzer, elliptic curves, hyperelliptic curves\n\nThe code in schemes/elliptic_curves/monsky_washnitzer.py largely dates from a time (early 2007) before Sage documentation and doctesting standards had been codified. As a result, its coverage is terrible (26 of 107).\n\nIt may also be worth a mild refactor: since it now applies more generally to hyperelliptic curves, it probably should be under schemes/hyperelliptic_curves.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8305\n\n",
    "created_at": "2010-02-19T03:34:22Z",
    "labels": [
        "elliptic curves",
        "major",
        "bug"
    ],
    "title": "Improve documentation of Monsky-Washnitzer code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8305",
    "user": "kedlaya"
}
```
Assignee: cremona

CC:  jpflori

Keywords: Monsky-Washnitzer, elliptic curves, hyperelliptic curves

The code in schemes/elliptic_curves/monsky_washnitzer.py largely dates from a time (early 2007) before Sage documentation and doctesting standards had been codified. As a result, its coverage is terrible (26 of 107).

It may also be worth a mild refactor: since it now applies more generally to hyperelliptic curves, it probably should be under schemes/hyperelliptic_curves.

Issue created by migration from https://trac.sagemath.org/ticket/8305





---

archive/issue_comments_073584.json:
```json
{
    "body": "The patch at #7926 brings coverage up to 50% (though I didn't make it to documenting the really interesting stuff).",
    "created_at": "2010-02-20T08:54:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8305#issuecomment-73584",
    "user": "robertwb"
}
```

The patch at #7926 brings coverage up to 50% (though I didn't make it to documenting the really interesting stuff).



---

archive/issue_comments_073585.json:
```json
{
    "body": "OK, so this ticket should stay on ice until someone (e.g., me) has a chance to review #7926. Besides the documentation, there is also the issue of moving the MW code from elliptic to hyperelliptic where it belongs.",
    "created_at": "2010-02-20T14:57:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8305#issuecomment-73585",
    "user": "kedlaya"
}
```

OK, so this ticket should stay on ice until someone (e.g., me) has a chance to review #7926. Besides the documentation, there is also the issue of moving the MW code from elliptic to hyperelliptic where it belongs.



---

archive/issue_comments_073586.json:
```json
{
    "body": "Changing assignee from cremona to kedlaya.",
    "created_at": "2010-02-20T14:57:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8305#issuecomment-73586",
    "user": "kedlaya"
}
```

Changing assignee from cremona to kedlaya.



---

archive/issue_comments_073587.json:
```json
{
    "body": "Attachment [trac_8305_monsky_doc.patch](tarball://root/attachments/some-uuid/ticket8305/trac_8305_monsky_doc.patch) by chapoton created at 2013-07-09 09:35:24\n\nfirst patch, with coverage reaching 67%",
    "created_at": "2013-07-09T09:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8305#issuecomment-73587",
    "user": "chapoton"
}
```

Attachment [trac_8305_monsky_doc.patch](tarball://root/attachments/some-uuid/ticket8305/trac_8305_monsky_doc.patch) by chapoton created at 2013-07-09 09:35:24

first patch, with coverage reaching 67%



---

archive/issue_comments_073588.json:
```json
{
    "body": "after some more work, coverage is almost 77%",
    "created_at": "2013-08-23T16:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8305#issuecomment-73588",
    "user": "chapoton"
}
```

after some more work, coverage is almost 77%



---

archive/issue_comments_073589.json:
```json
{
    "body": "after some more work, coverage is now 83%",
    "created_at": "2013-10-01T19:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8305#issuecomment-73589",
    "user": "chapoton"
}
```

after some more work, coverage is now 83%



---

archive/issue_comments_073590.json:
```json
{
    "body": "Attachment [trac_8305_monsky_doc_step2.patch](tarball://root/attachments/some-uuid/ticket8305/trac_8305_monsky_doc_step2.patch) by chapoton created at 2013-10-14 19:33:14",
    "created_at": "2013-10-14T19:33:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8305#issuecomment-73590",
    "user": "chapoton"
}
```

Attachment [trac_8305_monsky_doc_step2.patch](tarball://root/attachments/some-uuid/ticket8305/trac_8305_monsky_doc_step2.patch) by chapoton created at 2013-10-14 19:33:14



---

archive/issue_comments_073591.json:
```json
{
    "body": "after some more work, coverage is now 85%",
    "created_at": "2013-10-14T19:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8305#issuecomment-73591",
    "user": "chapoton"
}
```

after some more work, coverage is now 85%



---

archive/issue_comments_073592.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-01-05T13:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8305#issuecomment-73592",
    "user": "chapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073593.json:
```json
{
    "body": "maybe this can be considered as a good first step towards 100% ?\n----\nNew commits:",
    "created_at": "2014-01-05T13:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8305#issuecomment-73593",
    "user": "chapoton"
}
```

maybe this can be considered as a good first step towards 100% ?
----
New commits:



---

archive/issue_comments_073594.json:
```json
{
    "body": "An excellent step, yes! Good work.\n\nI've spun off tickets #15645 and #15646 to track the remaining issues on this ticket (100% coverage and refactoring).",
    "created_at": "2014-01-07T23:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8305#issuecomment-73594",
    "user": "kedlaya"
}
```

An excellent step, yes! Good work.

I've spun off tickets #15645 and #15646 to track the remaining issues on this ticket (100% coverage and refactoring).



---

archive/issue_comments_073595.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-01-07T23:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8305#issuecomment-73595",
    "user": "kedlaya"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073596.json:
```json
{
    "body": "Fill in the reviewer name...",
    "created_at": "2014-01-09T06:43:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8305#issuecomment-73596",
    "user": "vbraun"
}
```

Fill in the reviewer name...



---

archive/issue_comments_073597.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-01-10T07:29:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8305#issuecomment-73597",
    "user": "vbraun"
}
```

Resolution: fixed
