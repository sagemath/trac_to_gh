# Issue 2915: bug in symbolic integration or "stupid bug in the sage/maxima interface"?

archive/issues_002915.json:
```json
{
    "body": "Assignee: @williamstein\n\nI tried the first integral inthe Axiom book in Sage and get a big boom!\n\n```\nsage: var('a,b')\nsage: integrate(1/(x^3 *(a+b*x)^(1/3)), x)\nTraceback (most recent call last):\n...\nTypeError: \nIs  a  \nComputation failed due to a bug in Maxima -- NOTE: Maxima had to be restarted.\n```\n\n\nTrying maxima interactively shows it is just prompting for\nwhether or not a is positive.  Specifying which makes this work fine:\n\n```\nsage: var('a,b')\nsage: assume(a>0)\nsage: integrate(1/(x^3 *(a+b*x)^(1/3)), x)\n2*b^2*arctan((2*(b*x + a)^(1/3) + a^(1/3))/(sqrt(3)*a^(1/3)))/(3*sqrt(3)*a^(7/3)) - b^2*log((b*x + a)^(2/3) + a^(1/3)*(b*x + a)^(1/3) + a^(2/3))/(9*a^(7/3)) + 2*b^2*log((b*x + a)^(1/3) - a^(1/3))/(9*a^(7/3)) + (4*b^2*(b*x + a)^(5/3) - 7*a*b^2*(b*x + a)^(2/3))/(6*a^2*(b*x + a)^2 - 12*a^3*(b*x + a) + 6*a^4)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2915\n\n",
    "created_at": "2008-04-14T05:27:46Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "bug in symbolic integration or \"stupid bug in the sage/maxima interface\"?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2915",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

I tried the first integral inthe Axiom book in Sage and get a big boom!

```
sage: var('a,b')
sage: integrate(1/(x^3 *(a+b*x)^(1/3)), x)
Traceback (most recent call last):
...
TypeError: 
Is  a  
Computation failed due to a bug in Maxima -- NOTE: Maxima had to be restarted.
```


Trying maxima interactively shows it is just prompting for
whether or not a is positive.  Specifying which makes this work fine:

```
sage: var('a,b')
sage: assume(a>0)
sage: integrate(1/(x^3 *(a+b*x)^(1/3)), x)
2*b^2*arctan((2*(b*x + a)^(1/3) + a^(1/3))/(sqrt(3)*a^(1/3)))/(3*sqrt(3)*a^(7/3)) - b^2*log((b*x + a)^(2/3) + a^(1/3)*(b*x + a)^(1/3) + a^(2/3))/(9*a^(7/3)) + 2*b^2*log((b*x + a)^(1/3) - a^(1/3))/(9*a^(7/3)) + (4*b^2*(b*x + a)^(5/3) - 7*a*b^2*(b*x + a)^(2/3))/(6*a^2*(b*x + a)^2 - 12*a^3*(b*x + a) + 6*a^4)
```


Issue created by migration from https://trac.sagemath.org/ticket/2915





---

archive/issue_comments_020038.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-14T20:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2915#issuecomment-20038",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020039.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2008-04-14T20:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2915#issuecomment-20039",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_020040.json:
```json
{
    "body": "Attachment [2915.patch](tarball://root/attachments/some-uuid/ticket2915/2915.patch) by @mwhansen created at 2008-04-14 20:44:53",
    "created_at": "2008-04-14T20:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2915#issuecomment-20040",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2915.patch](tarball://root/attachments/some-uuid/ticket2915/2915.patch) by @mwhansen created at 2008-04-14 20:44:53



---

archive/issue_comments_020041.json:
```json
{
    "body": "Attachment [sage-2915-followup.patch](tarball://root/attachments/some-uuid/ticket2915/sage-2915-followup.patch) by @williamstein created at 2008-04-14 23:56:00\n\nREFEREE REPORT:\n\n* Excellent!\n \n* I've reformatted the doctest a little and added computing the actual integral, since it's a good example to have in our system.",
    "created_at": "2008-04-14T23:56:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2915#issuecomment-20041",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2915-followup.patch](tarball://root/attachments/some-uuid/ticket2915/sage-2915-followup.patch) by @williamstein created at 2008-04-14 23:56:00

REFEREE REPORT:

* Excellent!
 
* I've reformatted the doctest a little and added computing the actual integral, since it's a good example to have in our system.



---

archive/issue_comments_020042.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-15T00:55:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2915#issuecomment-20042",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020043.json:
```json
{
    "body": "Merged both patches in Sage 3.0.alpha5",
    "created_at": "2008-04-15T00:55:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2915#issuecomment-20043",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.0.alpha5
