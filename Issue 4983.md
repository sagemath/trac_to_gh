# Issue 4983: replace subdivisions attribute for matrices with a function

archive/issues_004983.json:
```json
{
    "body": "Assignee: @williamstein\n\nI do not like this:\n\n```\nsage: sage: a = matrix(ZZ,4,[1, 0, 0, 0, 0, 1, 0, 0, 1, -1, 1, 0, 1, -1, 1, 2])\nsage: sage: b=a.jordan_form()\nsage: b.subdivisions\n([0, 1, 3, 4], [0, 1, 3, 4])\nsage: b.subdivisions = 10\nsage: b.subdivisions\n10\n```\n\nNotice that you can make the subdivisions nonsense because it can be changed.\nAlso, of course,\n\n```\nsage: b.subdivisions?\n...     The Integer class represents arbitrary precision\n        integers.  It derives from the Element class, so\n[other useless stuff]\n```\n\n\nI don't like that at all either.  I wish that subdivisions were a method with a proper docstring, doctests, etc., and that variable were hidden.\n\n\nThen one would do:\n\n```\n   sage: b.subdivisions?\n   useful stuff (and also it would be in the reference manual)\nand\n   sage: b.subdivisions()\n   ([0, 1, 3, 4], [0, 1, 3, 4])\n```\n\n---\n\n**Depends on:**\n1. #10974\n\n**Apply:**\n1. [attachment:trac_4983-subdivisions-rebased.patch]\n\nIssue created by migration from https://trac.sagemath.org/ticket/4983\n\n",
    "closed_at": "2011-04-05T11:59:51Z",
    "created_at": "2009-01-16T00:30:50Z",
    "labels": [
        "component: linear algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "replace subdivisions attribute for matrices with a function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4983",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

I do not like this:

```
sage: sage: a = matrix(ZZ,4,[1, 0, 0, 0, 0, 1, 0, 0, 1, -1, 1, 0, 1, -1, 1, 2])
sage: sage: b=a.jordan_form()
sage: b.subdivisions
([0, 1, 3, 4], [0, 1, 3, 4])
sage: b.subdivisions = 10
sage: b.subdivisions
10
```

Notice that you can make the subdivisions nonsense because it can be changed.
Also, of course,

```
sage: b.subdivisions?
...     The Integer class represents arbitrary precision
        integers.  It derives from the Element class, so
[other useless stuff]
```


I don't like that at all either.  I wish that subdivisions were a method with a proper docstring, doctests, etc., and that variable were hidden.


Then one would do:

```
   sage: b.subdivisions?
   useful stuff (and also it would be in the reference manual)
and
   sage: b.subdivisions()
   ([0, 1, 3, 4], [0, 1, 3, 4])
```

---

**Depends on:**
1. #10974

**Apply:**
1. [attachment:trac_4983-subdivisions-rebased.patch]

Issue created by migration from https://trac.sagemath.org/ticket/4983





---

archive/issue_comments_037916.json:
```json
{
    "body": "The method is \n\n```\nsage: b.get_subdivisions()\n([1, 3], [1, 3])\n```\n\nbut this should probably be changed to have an attribute _subdivisions and a method subdivisions() for consistency.",
    "created_at": "2009-01-16T00:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37916",
    "user": "https://github.com/robertwb"
}
```

The method is 

```
sage: b.get_subdivisions()
([1, 3], [1, 3])
```

but this should probably be changed to have an attribute _subdivisions and a method subdivisions() for consistency.



---

archive/issue_comments_037917.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:45:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37917",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_037918.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-03-21T20:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37918",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_037919.json:
```json
{
    "body": "Here's patch.  This keeps `get_subdivisions` as a synonym for `subdivisions`.",
    "created_at": "2011-03-21T20:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37919",
    "user": "https://github.com/jhpalmieri"
}
```

Here's patch.  This keeps `get_subdivisions` as a synonym for `subdivisions`.



---

archive/issue_comments_037920.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2011-03-21T20:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37920",
    "user": "https://github.com/jhpalmieri"
}
```

Changing priority from major to minor.



---

archive/issue_comments_037921.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-22T17:21:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37921",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_037922.json:
```json
{
    "body": "This looks real good.  Passes long tests.  I'm glad to see a \"get_\" go away.\n\nThis means I should mildly change #10974, so I'll go make the changes necessary there and have it depend on this.",
    "created_at": "2011-03-22T17:21:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37922",
    "user": "https://github.com/rbeezer"
}
```

This looks real good.  Passes long tests.  I'm glad to see a "get_" go away.

This means I should mildly change #10974, so I'll go make the changes necessary there and have it depend on this.



---

archive/issue_comments_037923.json:
```json
{
    "body": "This probably conflicts with #10847 too.",
    "created_at": "2011-03-22T22:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37923",
    "user": "https://github.com/jasongrout"
}
```

This probably conflicts with #10847 too.



---

archive/issue_comments_037924.json:
```json
{
    "body": "(where \"conflicts\" means that #10847 probably needs to be changed after this patch too.)",
    "created_at": "2011-03-22T22:31:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37924",
    "user": "https://github.com/jasongrout"
}
```

(where "conflicts" means that #10847 probably needs to be changed after this patch too.)



---

archive/issue_comments_037925.json:
```json
{
    "body": "It would be nice if a patch that has had positive review for over a week did not have to be rebased for a patch that has had positive review for seven hours.  Could this patch not be based on that instead?",
    "created_at": "2011-03-22T23:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37925",
    "user": "https://github.com/kcrisman"
}
```

It would be nice if a patch that has had positive review for over a week did not have to be rebased for a patch that has had positive review for seven hours.  Could this patch not be based on that instead?



---

archive/issue_comments_037926.json:
```json
{
    "body": "kcrisman: I just posted a fix for #10847.  (The issue was, the patches at #10847 used the attribute `matrix.subdivisions` instead of using the method `matrix.get_subdivisions()`.)",
    "created_at": "2011-03-23T00:20:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37926",
    "user": "https://github.com/jhpalmieri"
}
```

kcrisman: I just posted a fix for #10847.  (The issue was, the patches at #10847 used the attribute `matrix.subdivisions` instead of using the method `matrix.get_subdivisions()`.)



---

archive/issue_comments_037927.json:
```json
{
    "body": "Replying to [comment:8 jhpalmieri]:\n> kcrisman: I just posted a fix for #10847.  (The issue was, the patches at #10847 used the attribute `matrix.subdivisions` instead of using the method `matrix.get_subdivisions()`.)\n\nThanks, I appreciate it.  I was aware of the incompatibility, just didn't have time to take care of it myself the next few days.",
    "created_at": "2011-03-23T11:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37927",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:8 jhpalmieri]:
> kcrisman: I just posted a fix for #10847.  (The issue was, the patches at #10847 used the attribute `matrix.subdivisions` instead of using the method `matrix.get_subdivisions()`.)

Thanks, I appreciate it.  I was aware of the incompatibility, just didn't have time to take care of it myself the next few days.



---

archive/issue_comments_037928.json:
```json
{
    "body": "Attachment [trac_4983-subdivisions.patch](tarball://root/attachments/some-uuid/ticket4983/trac_4983-subdivisions.patch) by @jhpalmieri created at 2011-03-23 17:51:05",
    "created_at": "2011-03-23T17:51:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37928",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_4983-subdivisions.patch](tarball://root/attachments/some-uuid/ticket4983/trac_4983-subdivisions.patch) by @jhpalmieri created at 2011-03-23 17:51:05



---

archive/issue_comments_037929.json:
```json
{
    "body": "I just uploaded a new patch; the only difference is I added the comment\n\n```\n    # 'get_subdivisions' is kept for backwards compatibility: see #4983. \n```\nright before `get_subdivisions = subdivisions`.",
    "created_at": "2011-03-23T17:52:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37929",
    "user": "https://github.com/jhpalmieri"
}
```

I just uploaded a new patch; the only difference is I added the comment

```
    # 'get_subdivisions' is kept for backwards compatibility: see #4983. 
```
right before `get_subdivisions = subdivisions`.



---

archive/issue_comments_037930.json:
```json
{
    "body": "This patch conflicts with #10974.",
    "created_at": "2011-04-04T09:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37930",
    "user": "https://github.com/jdemeyer"
}
```

This patch conflicts with #10974.



---

archive/issue_comments_037931.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-04-04T09:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37931",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_037932.json:
```json
{
    "body": "Here's a patch rebased against #10974.  Does this need review or not?",
    "created_at": "2011-04-04T19:23:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37932",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a patch rebased against #10974.  Does this need review or not?



---

archive/issue_comments_037933.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-04T19:23:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37933",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_037934.json:
```json
{
    "body": "Attachment [trac_4983-subdivisions-rebased.patch](tarball://root/attachments/some-uuid/ticket4983/trac_4983-subdivisions-rebased.patch) by @jhpalmieri created at 2011-04-04 19:24:10",
    "created_at": "2011-04-04T19:24:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37934",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_4983-subdivisions-rebased.patch](tarball://root/attachments/some-uuid/ticket4983/trac_4983-subdivisions-rebased.patch) by @jhpalmieri created at 2011-04-04 19:24:10



---

archive/issue_comments_037935.json:
```json
{
    "body": "If it's literally a fairly trivial rebase and nothing changed in terms of testing, I think it would be okay to just post a diff of what had to be rebased (since the patch is fairly large) and set back to positive review.  If there are some actual nontrivial changes in the code then I guess someone would have to review it.",
    "created_at": "2011-04-04T19:47:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37935",
    "user": "https://github.com/kcrisman"
}
```

If it's literally a fairly trivial rebase and nothing changed in terms of testing, I think it would be okay to just post a diff of what had to be rebased (since the patch is fairly large) and set back to positive review.  If there are some actual nontrivial changes in the code then I guess someone would have to review it.



---

archive/issue_comments_037936.json:
```json
{
    "body": "Replying to [comment:12 jhpalmieri]:\n> Here's a patch rebased against #10974.  \n\n\nThanks, John.\n\n> Does this need review or not?\n\n\nNormally, I'd say \"not.\"  But I have two or three  other rebase tasks for later this afternoon, so I can give it a quick test then.\n\nRob",
    "created_at": "2011-04-04T19:49:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37936",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:12 jhpalmieri]:
> Here's a patch rebased against #10974.  


Thanks, John.

> Does this need review or not?


Normally, I'd say "not."  But I have two or three  other rebase tasks for later this afternoon, so I can give it a quick test then.

Rob



---

archive/issue_comments_037937.json:
```json
{
    "body": "I just rebased it, I didn't change anything else, but if Rob has time to run tests on it, that would be great.  (I've already done this, but it's good to double-check it.)",
    "created_at": "2011-04-04T19:56:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37937",
    "user": "https://github.com/jhpalmieri"
}
```

I just rebased it, I didn't change anything else, but if Rob has time to run tests on it, that would be great.  (I've already done this, but it's good to double-check it.)



---

archive/issue_comments_037938.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-04-04T20:16:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37938",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_037939.json:
```json
{
    "body": "Replying to [comment:14 kcrisman]:\n> I think it would be okay to [...] set back to positive review.\n\nDone.",
    "created_at": "2011-04-04T20:16:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37939",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:14 kcrisman]:
> I think it would be okay to [...] set back to positive review.

Done.



---

archive/issue_comments_037940.json:
```json
{
    "body": "Replying to [comment:16 jhpalmieri]:\n>  (I've already done this, but it's good to double-check it.)\n\n\nDouble-check shows everything is fine on 4.7.alpha3: applies, builds, passes long tests.\n\nThanks again, John, for sparing me the work on #10974.  As a bonus I upgraded the depends/apply block to Jeroen's new formatting.  ;-)",
    "created_at": "2011-04-04T23:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37940",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:16 jhpalmieri]:
>  (I've already done this, but it's good to double-check it.)


Double-check shows everything is fine on 4.7.alpha3: applies, builds, passes long tests.

Thanks again, John, for sparing me the work on #10974.  As a bonus I upgraded the depends/apply block to Jeroen's new formatting.  ;-)



---

archive/issue_comments_037941.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-04-05T11:59:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4983#issuecomment-37941",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_011533.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-04-05T11:59:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4983",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4983#event-11533"
}
```
