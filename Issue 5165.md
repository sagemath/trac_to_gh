# Issue 5165: make padded_list use prec by default

archive/issues_005165.json:
```json
{
    "body": "Assignee: @aghitza\n\nConsider this situation:\n\n```\nsage: f = ModularForms(28,2).q_expansion_basis()[-1]\nsage: f\nq^7 + O(q^20)\n```\n\nAt this point, I would like to be able to do f.padded_list() and have this take f.prec() as default parameter.  It's not a big deal, but it would be more convenient than having to type f.padded_list(f.prec()).  There might be other situations (power series in general, for instance?) where this change could also be made.\n\nI'll have a patch up for this soon.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5165\n\n",
    "created_at": "2009-02-03T05:59:54Z",
    "labels": [
        "component: modular forms",
        "trivial"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "make padded_list use prec by default",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5165",
    "user": "https://github.com/aghitza"
}
```
Assignee: @aghitza

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

archive/issue_comments_039503.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-03T10:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5165#issuecomment-39503",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_039504.json:
```json
{
    "body": "In fact, `padded_list` is actually inherited from power series.\n\nSee the attached patch.",
    "created_at": "2010-01-03T10:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5165#issuecomment-39504",
    "user": "https://github.com/aghitza"
}
```

In fact, `padded_list` is actually inherited from power series.

See the attached patch.



---

archive/issue_comments_039505.json:
```json
{
    "body": "Attachment [trac_5165.patch](tarball://root/attachments/some-uuid/ticket5165/trac_5165.patch) by @aghitza created at 2010-01-03 10:20:37",
    "created_at": "2010-01-03T10:20:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5165#issuecomment-39505",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_5165.patch](tarball://root/attachments/some-uuid/ticket5165/trac_5165.patch) by @aghitza created at 2010-01-03 10:20:37



---

archive/issue_comments_039506.json:
```json
{
    "body": "Looks fine to me.",
    "created_at": "2010-04-05T14:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5165#issuecomment-39506",
    "user": "https://github.com/loefflerd"
}
```

Looks fine to me.



---

archive/issue_comments_039507.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-05T14:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5165#issuecomment-39507",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_039508.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T05:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5165#issuecomment-39508",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_events_011960.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-15T05:19:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5165",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5165#event-11960"
}
```



---

archive/issue_comments_039509.json:
```json
{
    "body": "Merged in 4.4.alpha0.",
    "created_at": "2010-04-15T05:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5165#issuecomment-39509",
    "user": "https://github.com/jhpalmieri"
}
```

Merged in 4.4.alpha0.



---

archive/issue_comments_039510.json:
```json
{
    "body": "(The change in the description was accidental.)",
    "created_at": "2010-04-15T06:05:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5165#issuecomment-39510",
    "user": "https://github.com/jhpalmieri"
}
```

(The change in the description was accidental.)
