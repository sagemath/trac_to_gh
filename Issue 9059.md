# Issue 9059: some shortcuts for "is_H-free" tests

archive/issues_009059.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nSome useful tests :\n\n* is_even_hole_free\n* is_odd_hole_free\n* is_odd_antihole_free\n\nMay be worth a dedicated function... :-)\n\nNathann\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9059\n\n",
    "created_at": "2010-05-26T22:34:40Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "some shortcuts for \"is_H-free\" tests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9059",
    "user": "@nathanncohen"
}
```
Assignee: jason, ncohen, rlm

Some useful tests :

* is_even_hole_free
* is_odd_hole_free
* is_odd_antihole_free

May be worth a dedicated function... :-)

Nathann


Issue created by migration from https://trac.sagemath.org/ticket/9059





---

archive/issue_comments_084054.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-06T11:01:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9059#issuecomment-84054",
    "user": "@nathanncohen"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_084055.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-13T16:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9059#issuecomment-84055",
    "user": "@nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084056.json:
```json
{
    "body": "Well, as odd_antihole_free is just g.complement().is_odd_hole_free, let this patch just define the first two :-)\n\nNathann",
    "created_at": "2010-06-13T16:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9059#issuecomment-84056",
    "user": "@nathanncohen"
}
```

Well, as odd_antihole_free is just g.complement().is_odd_hole_free, let this patch just define the first two :-)

Nathann



---

archive/issue_comments_084057.json:
```json
{
    "body": "Attachment [trac_9059.patch](tarball://root/attachments/some-uuid/ticket9059/trac_9059.patch) by @rlmill created at 2010-06-21 20:45:44\n\nLooks good to me.",
    "created_at": "2010-06-21T20:45:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9059#issuecomment-84057",
    "user": "@rlmill"
}
```

Attachment [trac_9059.patch](tarball://root/attachments/some-uuid/ticket9059/trac_9059.patch) by @rlmill created at 2010-06-21 20:45:44

Looks good to me.



---

archive/issue_comments_084058.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-21T20:45:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9059#issuecomment-84058",
    "user": "@rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084059.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-29T16:46:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9059#issuecomment-84059",
    "user": "@rlmill"
}
```

Resolution: fixed
