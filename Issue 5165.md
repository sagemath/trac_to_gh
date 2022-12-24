# Issue 5165: make padded_list use prec by default

archive/issues_005165.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nConsider this situation:\n\n\n```\nsage: f = ModularForms(28,2).q_expansion_basis()[-1]\nsage: f\nq^7 + O(q^20)\n```\n\n\nAt this point, I would like to be able to do f.padded_list() and have this take f.prec() as default parameter.  It's not a big deal, but it would be more convenient than having to type f.padded_list(f.prec()).  There might be other situations (power series in general, for instance?) where this change could also be made.\n\nI'll have a patch up for this soon.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5165\n\n",
    "created_at": "2009-02-03T05:59:54Z",
    "labels": [
        "modular forms",
        "trivial",
        "enhancement"
    ],
    "title": "make padded_list use prec by default",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5165",
    "user": "AlexGhitza"
}
```
Assignee: AlexGhitza

Consider this situation:


```
sage: f = ModularForms(28,2).q_expansion_basis()[-1]
sage: f
q^7 + O(q^20)
```


At this point, I would like to be able to do f.padded_list() and have this take f.prec() as default parameter.  It's not a big deal, but it would be more convenient than having to type f.padded_list(f.prec()).  There might be other situations (power series in general, for instance?) where this change could also be made.

I'll have a patch up for this soon.

Issue created by migration from https://trac.sagemath.org/ticket/5165





---

archive/issue_comments_039579.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-03T10:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5165#issuecomment-39579",
    "user": "AlexGhitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_039580.json:
```json
{
    "body": "In fact, `padded_list` is actually inherited from power series.\n\nSee the attached patch.",
    "created_at": "2010-01-03T10:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5165#issuecomment-39580",
    "user": "AlexGhitza"
}
```

In fact, `padded_list` is actually inherited from power series.

See the attached patch.



---

archive/issue_comments_039581.json:
```json
{
    "body": "Attachment [trac_5165.patch](tarball://root/attachments/some-uuid/ticket5165/trac_5165.patch) by AlexGhitza created at 2010-01-03 10:20:37",
    "created_at": "2010-01-03T10:20:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5165#issuecomment-39581",
    "user": "AlexGhitza"
}
```

Attachment [trac_5165.patch](tarball://root/attachments/some-uuid/ticket5165/trac_5165.patch) by AlexGhitza created at 2010-01-03 10:20:37



---

archive/issue_comments_039582.json:
```json
{
    "body": "Looks fine to me.",
    "created_at": "2010-04-05T14:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5165#issuecomment-39582",
    "user": "davidloeffler"
}
```

Looks fine to me.



---

archive/issue_comments_039583.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-05T14:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5165#issuecomment-39583",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_039584.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T05:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5165#issuecomment-39584",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_039585.json:
```json
{
    "body": "Merged in 4.4.alpha0.",
    "created_at": "2010-04-15T05:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5165#issuecomment-39585",
    "user": "jhpalmieri"
}
```

Merged in 4.4.alpha0.



---

archive/issue_comments_039586.json:
```json
{
    "body": "(The change in the description was accidental.)",
    "created_at": "2010-04-15T06:05:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5165#issuecomment-39586",
    "user": "jhpalmieri"
}
```

(The change in the description was accidental.)
