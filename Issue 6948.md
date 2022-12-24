# Issue 6948: powers of exp are over simplified

archive/issues_006948.json:
```json
{
    "body": "Assignee: @burcin\n\nFrancois Maltey wrote on sage-support:\n\n\n```\nvar(\"a,b,c\")\nexp(a)^2 # returns exp(2a) is right\nexp(a)^(1/2) # returns exp (a/2) is wrong, with a=2*i*pi we get -1=1\nexp(a)^b # returns exp(a*b) is wrong\n```\n\n\nThe thread is here:\n\nhttp://groups.google.com/group/sage-support/browse_thread/thread/330a015bf640a4f3/0ddfdd5a4e021579\n\nIssue created by migration from https://trac.sagemath.org/ticket/6948\n\n",
    "created_at": "2009-09-17T13:48:17Z",
    "labels": [
        "symbolics",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "powers of exp are over simplified",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6948",
    "user": "@burcin"
}
```
Assignee: @burcin

Francois Maltey wrote on sage-support:


```
var("a,b,c")
exp(a)^2 # returns exp(2a) is right
exp(a)^(1/2) # returns exp (a/2) is wrong, with a=2*i*pi we get -1=1
exp(a)^b # returns exp(a*b) is wrong
```


The thread is here:

http://groups.google.com/group/sage-support/browse_thread/thread/330a015bf640a4f3/0ddfdd5a4e021579

Issue created by migration from https://trac.sagemath.org/ticket/6948





---

archive/issue_comments_057445.json:
```json
{
    "body": "Attachment [trac_6948-exp_power.patch](tarball://root/attachments/some-uuid/ticket6948/trac_6948-exp_power.patch) by @burcin created at 2009-09-19 15:05:32",
    "created_at": "2009-09-19T15:05:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6948#issuecomment-57445",
    "user": "@burcin"
}
```

Attachment [trac_6948-exp_power.patch](tarball://root/attachments/some-uuid/ticket6948/trac_6948-exp_power.patch) by @burcin created at 2009-09-19 15:05:32



---

archive/issue_comments_057446.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-19T15:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6948#issuecomment-57446",
    "user": "@burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_057447.json:
```json
{
    "body": "This is fixed in my pynac tree, attachment:trac_6948-exp_power.patch is the corresponding patch for Sage. I will release a pynac spkg with some more fixes and post instructions for review.",
    "created_at": "2009-09-19T15:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6948#issuecomment-57447",
    "user": "@burcin"
}
```

This is fixed in my pynac tree, attachment:trac_6948-exp_power.patch is the corresponding patch for Sage. I will release a pynac spkg with some more fixes and post instructions for review.



---

archive/issue_comments_057448.json:
```json
{
    "body": "New pynac package available at #6993.",
    "created_at": "2009-09-22T19:27:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6948#issuecomment-57448",
    "user": "@burcin"
}
```

New pynac package available at #6993.



---

archive/issue_comments_057449.json:
```json
{
    "body": "Nice, but does it actually fix the examples provided?  \n\n```\nsage: exp(a)^(1/2)\nsqrt(e^a)\n```\n\nI guess that's okay.  But\n\n```\nsage: exp(a)^(1/3)\ne^a^(1/3)\nsage: exp(a^(1/3))\ne^(a^(1/3))\n```\n\nI think there are missing parentheses in the first example, particularly because it's not typeset.   Even if that is a convention, which I'm not so sure of, the dictum is that it's better to be explicit.  \n\nI also get a doctest failure (not mentioned in the Pynac upgrade ticket) in product and quotient rule differentiation in calculus/tests.py, but it looks like that's the one in #6524, so it's properly speaking another issue, I guess.",
    "created_at": "2009-09-23T01:58:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6948#issuecomment-57449",
    "user": "@kcrisman"
}
```

Nice, but does it actually fix the examples provided?  

```
sage: exp(a)^(1/2)
sqrt(e^a)
```

I guess that's okay.  But

```
sage: exp(a)^(1/3)
e^a^(1/3)
sage: exp(a^(1/3))
e^(a^(1/3))
```

I think there are missing parentheses in the first example, particularly because it's not typeset.   Even if that is a convention, which I'm not so sure of, the dictum is that it's better to be explicit.  

I also get a doctest failure (not mentioned in the Pynac upgrade ticket) in product and quotient rule differentiation in calculus/tests.py, but it looks like that's the one in #6524, so it's properly speaking another issue, I guess.



---

archive/issue_comments_057450.json:
```json
{
    "body": "This package should fix this problem:\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.9.p0.spkg\n\nI'll attach a patch with some more doctests now.",
    "created_at": "2009-09-24T06:30:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6948#issuecomment-57450",
    "user": "@burcin"
}
```

This package should fix this problem:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.9.p0.spkg

I'll attach a patch with some more doctests now.



---

archive/issue_comments_057451.json:
```json
{
    "body": "Attachment [trac_6948-exp_power_print.patch](tarball://root/attachments/some-uuid/ticket6948/trac_6948-exp_power_print.patch) by @kcrisman created at 2009-09-24 13:32:06\n\nPositive review!",
    "created_at": "2009-09-24T13:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6948#issuecomment-57451",
    "user": "@kcrisman"
}
```

Attachment [trac_6948-exp_power_print.patch](tarball://root/attachments/some-uuid/ticket6948/trac_6948-exp_power_print.patch) by @kcrisman created at 2009-09-24 13:32:06

Positive review!



---

archive/issue_comments_057452.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-25T22:44:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6948#issuecomment-57452",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057453.json:
```json
{
    "body": "Merged both patches.",
    "created_at": "2009-09-25T22:44:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6948#issuecomment-57453",
    "user": "mvngu"
}
```

Merged both patches.



---

archive/issue_comments_057454.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6948#issuecomment-57454",
    "user": "mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
