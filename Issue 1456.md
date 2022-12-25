# Issue 1456: gaussian_binomial bug

archive/issues_001456.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nThere are some problems with the function gaussian_binomial\nin sage 2.8.14. The help string contains a typo:\n\n binom{n}{k}_q = frac{(1-q<sup>m)(1-q</sup>{m-1})... (1-q^{m-r+1})}\n{(1-q)(1-q^2)... (1-q^r)}.\n\nThe typo is that m and r on the RHS should match n and k on the LHS.\n\nI feel that to be useful gaussian_binomial(n,k,q) should work if n\nand k are integers and 0<=k<=n, no matter what q is. At the moment,\nthe function requires q to be an integer but there will be\napplications if q is an indeterminate.  Moreover if q = 1 this\nshould give the ordinary binomial coefficient but the current\nimplementation fails due to division by zero.\n\nPerhaps the following is one way to improve the\nfunction would be as follows. Then it gives the\ncorrect behavior when q is an indeterminate or q=1.\n\nWhy does the original function use misc.prod instead\nof prod?\n\nDaniel Bump\n\n\n```\ndef gaussian_binomial(n,k,q):\n   r\"\"\"\n   Return the gaussian binomial\n   $$\n      \\binom{n}{k}_q = \\frac{(1-q^n)(1-q^{n-1})\\cdots (1-q^{n-k+1})}\n                            {(1-q)(1-q^2)\\cdots (1-q^k)}.\n   $$\n\n   EXAMPLES:\n       sage: gaussian_binomial(5,1,2)\n       31\n\n   AUTHOR: David Joyner and William Stein\n   \"\"\"\n\n   R.<x>=QQ[]\n\n   n = prod([1 - x**i for i in range((n-k+1),n+1)])\n   d = prod([1 - x**i for i in range(1,k+1)])\n\n   return (n / d).subs(x = q)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1456\n\n",
    "created_at": "2007-12-11T01:07:28Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "gaussian_binomial bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1456",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: @mwhansen

CC:  sage-combinat

There are some problems with the function gaussian_binomial
in sage 2.8.14. The help string contains a typo:

 binom{n}{k}_q = frac{(1-q<sup>m)(1-q</sup>{m-1})... (1-q^{m-r+1})}
{(1-q)(1-q^2)... (1-q^r)}.

The typo is that m and r on the RHS should match n and k on the LHS.

I feel that to be useful gaussian_binomial(n,k,q) should work if n
and k are integers and 0<=k<=n, no matter what q is. At the moment,
the function requires q to be an integer but there will be
applications if q is an indeterminate.  Moreover if q = 1 this
should give the ordinary binomial coefficient but the current
implementation fails due to division by zero.

Perhaps the following is one way to improve the
function would be as follows. Then it gives the
correct behavior when q is an indeterminate or q=1.

Why does the original function use misc.prod instead
of prod?

Daniel Bump


```
def gaussian_binomial(n,k,q):
   r"""
   Return the gaussian binomial
   $$
      \binom{n}{k}_q = \frac{(1-q^n)(1-q^{n-1})\cdots (1-q^{n-k+1})}
                            {(1-q)(1-q^2)\cdots (1-q^k)}.
   $$

   EXAMPLES:
       sage: gaussian_binomial(5,1,2)
       31

   AUTHOR: David Joyner and William Stein
   """

   R.<x>=QQ[]

   n = prod([1 - x**i for i in range((n-k+1),n+1)])
   d = prod([1 - x**i for i in range(1,k+1)])

   return (n / d).subs(x = q)
```



Issue created by migration from https://trac.sagemath.org/ticket/1456





---

archive/issue_comments_009359.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-23T21:28:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1456#issuecomment-9359",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009360.json:
```json
{
    "body": "Attachment [1456.patch](tarball://root/attachments/some-uuid/ticket1456/1456.patch) by @mwhansen created at 2008-01-23 21:30:00",
    "created_at": "2008-01-23T21:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1456#issuecomment-9360",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1456.patch](tarball://root/attachments/some-uuid/ticket1456/1456.patch) by @mwhansen created at 2008-01-23 21:30:00



---

archive/issue_comments_009361.json:
```json
{
    "body": "Looks good; doctests pass.",
    "created_at": "2008-01-27T01:41:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1456#issuecomment-9361",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Looks good; doctests pass.



---

archive/issue_comments_009362.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc1",
    "created_at": "2008-01-27T01:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1456#issuecomment-9362",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.rc1



---

archive/issue_comments_009363.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-27T01:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1456#issuecomment-9363",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001607.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-27T01:55:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1456",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1456#event-1607"
}
```
