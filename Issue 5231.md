# Issue 5231: [with patch, needs review] make relative number fields lazy

archive/issues_005231.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  was cc davidloeffler\n\nKeywords: relative number fields lazy pari\n\nThe attached patch makes relative number fields truly lazy, meaning that they don't require PARI's nf or bnf structures for the base field nor PARI's rnf structures for the extension.  This means that arithmetic can be done in huge extensions, ones for which there is no hope of finding units, class groups, etc.\n\nAlong the way I cleaned some conversions to PARI and fixed a bug relativizing absolute fields over QQ.  I also added many doctests.  I also tested this with #4779's randomized testing; passed with flying colors.\n\nThis patch cannot be allowed to bitrot, it's just to much work to understand this part of the code.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5231\n\n",
    "created_at": "2009-02-11T00:36:08Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] make relative number fields lazy",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5231",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

CC:  was cc davidloeffler

Keywords: relative number fields lazy pari

The attached patch makes relative number fields truly lazy, meaning that they don't require PARI's nf or bnf structures for the base field nor PARI's rnf structures for the extension.  This means that arithmetic can be done in huge extensions, ones for which there is no hope of finding units, class groups, etc.

Along the way I cleaned some conversions to PARI and fixed a bug relativizing absolute fields over QQ.  I also added many doctests.  I also tested this with #4779's randomized testing; passed with flying colors.

This patch cannot be allowed to bitrot, it's just to much work to understand this part of the code.

Issue created by migration from https://trac.sagemath.org/ticket/5231





---

archive/issue_comments_040015.json:
```json
{
    "body": "Attachment [trac_5231-lazy-relative-fields.patch](tarball://root/attachments/some-uuid/ticket5231/trac_5231-lazy-relative-fields.patch) by @ncalexan created at 2009-02-11 00:37:48",
    "created_at": "2009-02-11T00:37:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5231#issuecomment-40015",
    "user": "https://github.com/ncalexan"
}
```

Attachment [trac_5231-lazy-relative-fields.patch](tarball://root/attachments/some-uuid/ticket5231/trac_5231-lazy-relative-fields.patch) by @ncalexan created at 2009-02-11 00:37:48



---

archive/issue_comments_040016.json:
```json
{
    "body": "Nick,\n\nI hope to have some time to look at this (and hopefully review it) this evening (i.e. in about 6 hours).",
    "created_at": "2009-02-11T05:01:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5231#issuecomment-40016",
    "user": "https://github.com/aghitza"
}
```

Nick,

I hope to have some time to look at this (and hopefully review it) this evening (i.e. in about 6 hours).



---

archive/issue_comments_040017.json:
```json
{
    "body": "Attachment [trac_5231-lazy-relative-fields-updated.patch](tarball://root/attachments/some-uuid/ticket5231/trac_5231-lazy-relative-fields-updated.patch) by @ncalexan created at 2009-02-11 05:32:04",
    "created_at": "2009-02-11T05:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5231#issuecomment-40017",
    "user": "https://github.com/ncalexan"
}
```

Attachment [trac_5231-lazy-relative-fields-updated.patch](tarball://root/attachments/some-uuid/ticket5231/trac_5231-lazy-relative-fields-updated.patch) by @ncalexan created at 2009-02-11 05:32:04



---

archive/issue_comments_040018.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-11T06:05:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5231#issuecomment-40018",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040019.json:
```json
{
    "body": "Merged in Sage 3.3.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-11T06:05:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5231#issuecomment-40019",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.rc0.

Cheers,

Michael



---

archive/issue_events_005487.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-02-11T06:05:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5231",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5231#event-5487"
}
```
