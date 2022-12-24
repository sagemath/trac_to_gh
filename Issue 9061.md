# Issue 9061: Fix broken inequalities in add_constraint method

archive/issues_009061.json:
```json
{
    "body": "Assignee: jason, jkantor\n\nCC:  mvngu abmasse\n\nInequalities using <= and >= still do not work properly... :-/\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9061\n\n",
    "created_at": "2010-05-26T22:38:38Z",
    "labels": [
        "numerical",
        "major",
        "bug"
    ],
    "title": "Fix broken inequalities in add_constraint method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9061",
    "user": "ncohen"
}
```
Assignee: jason, jkantor

CC:  mvngu abmasse

Inequalities using <= and >= still do not work properly... :-/

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/9061





---

archive/issue_comments_084061.json:
```json
{
    "body": "Can you try `sage.misc.misc.balanced_sum`?  It seems to get about the same speedup for me as you indicate.\n\n\n```\np = MixedIntegerLinearProgram()\nv = p.new_variable()\n%timeit sage.misc.misc.balanced_sum([v[i] for i in xrange(900)])\n```\n",
    "created_at": "2010-05-28T00:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9061#issuecomment-84061",
    "user": "jason"
}
```

Can you try `sage.misc.misc.balanced_sum`?  It seems to get about the same speedup for me as you indicate.


```
p = MixedIntegerLinearProgram()
v = p.new_variable()
%timeit sage.misc.misc.balanced_sum([v[i] for i in xrange(900)])
```




---

archive/issue_comments_084062.json:
```json
{
    "body": "For me, the balanced_sum function gives these timings:\n\n\n```\nsage: p = MixedIntegerLinearProgram()\nsage: v = p.new_variable()\nsage: sage: %timeit sum([v[i] for i in xrange(900)])\n5 loops, best of 3: 1.48 s per loop\nsage: p = MixedIntegerLinearProgram()\nsage: v = p.new_variable()\nsage: %timeit sage.misc.misc.balanced_sum([v[i] for i in xrange(900)])\n25 loops, best of 3: 28.2 ms per loop\n```\n\n\nSo I guess your function still wins (which isn't much of a surprise).",
    "created_at": "2010-05-28T02:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9061#issuecomment-84062",
    "user": "jason"
}
```

For me, the balanced_sum function gives these timings:


```
sage: p = MixedIntegerLinearProgram()
sage: v = p.new_variable()
sage: sage: %timeit sum([v[i] for i in xrange(900)])
5 loops, best of 3: 1.48 s per loop
sage: p = MixedIntegerLinearProgram()
sage: v = p.new_variable()
sage: %timeit sage.misc.misc.balanced_sum([v[i] for i in xrange(900)])
25 loops, best of 3: 28.2 ms per loop
```


So I guess your function still wins (which isn't much of a surprise).



---

archive/issue_comments_084063.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-15T17:00:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9061#issuecomment-84063",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084064.json:
```json
{
    "body": "This patch defines the function sage.numerical.mip.Sum and updates the LP functions to have them use it !\n\nNathann",
    "created_at": "2010-06-15T17:00:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9061#issuecomment-84064",
    "user": "ncohen"
}
```

This patch defines the function sage.numerical.mip.Sum and updates the LP functions to have them use it !

Nathann



---

archive/issue_comments_084065.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-01T11:20:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9061#issuecomment-84065",
    "user": "ncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_084066.json:
```json
{
    "body": "Rebased ! :-)\n\nNathann",
    "created_at": "2010-07-01T11:20:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9061#issuecomment-84066",
    "user": "ncohen"
}
```

Rebased ! :-)

Nathann



---

archive/issue_comments_084067.json:
```json
{
    "body": "Attachment [trac_9061.patch](tarball://root/attachments/some-uuid/ticket9061/trac_9061.patch) by abmasse created at 2010-07-05 13:19:17\n\nHello, Nathann!\n\nDid you rebase it on sage-4.4.3? It seems so because it doesn't apply on sage-4.4.4. Since it touches many parts of the code, I don't know what would be the best strategy to make sure it is correctly based and it does not raise any problem with other patches.\n\nHaving looked at the code, it will probably be a fast review, as soon as I have checked for the improved efficiency.",
    "created_at": "2010-07-05T13:19:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9061#issuecomment-84067",
    "user": "abmasse"
}
```

Attachment [trac_9061.patch](tarball://root/attachments/some-uuid/ticket9061/trac_9061.patch) by abmasse created at 2010-07-05 13:19:17

Hello, Nathann!

Did you rebase it on sage-4.4.3? It seems so because it doesn't apply on sage-4.4.4. Since it touches many parts of the code, I don't know what would be the best strategy to make sure it is correctly based and it does not raise any problem with other patches.

Having looked at the code, it will probably be a fast review, as soon as I have checked for the improved efficiency.



---

archive/issue_comments_084068.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-07-06T08:20:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9061#issuecomment-84068",
    "user": "rlm"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_084069.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-06T08:20:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9061#issuecomment-84069",
    "user": "rlm"
}
```

Resolution: fixed
