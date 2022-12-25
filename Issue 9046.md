# Issue 9046: missing documentation and bug in collect

archive/issues_009046.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @kcrisman\n\nthe documentation from `collect` does not say what this function\ndoes. It should be documented.\n\nAlso, if it does what its name suggests, i.e., collect terms with\nsame exponent in 's', the following example shows that it seems that\nthe user should call `expand` before, since terms in `x^3`\nare not properly collected:\n\n```\nsage: (x^2+(y-x^2)*(y+x)).collect(x)\n-(x + y - 1)*x^2 + x^3 - (x^2 - y)*x + y^2\nsage: (x^2+(y-x^2)*(y+x)).expand().collect(x)\n-(y - 1)*x^2 - x^3 + x*y + y^2\n```\n\n\nFinally this seems a bug (note the instances of `-x^2` and\n`x^2`):\n\n```\nvar('a b x y z')\nsage: p = -a*x^3 - a*x*y^2 + 2*b*x^2*y + 2*y^3 + x^2*z + y^2*z + x^2 + y^2 + a*x\nsage: p.collect(x)\n-a*x^3 + (2*b*y + z + 1)*x^2 - x^2 - (a*y^2 - a)*x + x^2 + 2*y^3 + y^2*z + y^2\n\nIssue created by migration from https://trac.sagemath.org/ticket/9046\n\n",
    "created_at": "2010-05-25T12:02:04Z",
    "labels": [
        "component: calculus",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "missing documentation and bug in collect",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9046",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: @burcin

CC:  @kcrisman

the documentation from `collect` does not say what this function
does. It should be documented.

Also, if it does what its name suggests, i.e., collect terms with
same exponent in 's', the following example shows that it seems that
the user should call `expand` before, since terms in `x^3`
are not properly collected:

```
sage: (x^2+(y-x^2)*(y+x)).collect(x)
-(x + y - 1)*x^2 + x^3 - (x^2 - y)*x + y^2
sage: (x^2+(y-x^2)*(y+x)).expand().collect(x)
-(y - 1)*x^2 - x^3 + x*y + y^2
```


Finally this seems a bug (note the instances of `-x^2` and
`x^2`):

```
var('a b x y z')
sage: p = -a*x^3 - a*x*y^2 + 2*b*x^2*y + 2*y^3 + x^2*z + y^2*z + x^2 + y^2 + a*x
sage: p.collect(x)
-a*x^3 + (2*b*y + z + 1)*x^2 - x^2 - (a*y^2 - a)*x + x^2 + 2*y^3 + y^2*z + y^2

Issue created by migration from https://trac.sagemath.org/ticket/9046





---

archive/issue_comments_083608.json:
```json
{
    "body": "Here is the same session using GiNaC directly via `ginsh`:\n\n\n```\n> t= -a*x^3 - a*x*y^2 + 2*b*x^2*y + 2*y^3 + x^2*z + y^2*z + x^2 + y^2 + a*x;\nx^2+2*y*b*x^2+y^2+y^2*z+a*x+2*y^3-a*x^3-y^2*a*x+z*x^2\n> t;\nx^2+2*y*b*x^2+y^2+y^2*z+a*x+2*y^3-a*x^3-y^2*a*x+z*x^2\n> collect(t, x);\n(1+2*y*b+z)*x^2+y^2+y^2*z+2*y^3-a*x^3-(y^2*a-a)*x\n> u = (x^2+(y-x^2)*(y+x));\nx^2-(y+x)*(x^2-y)\n> collect(u, x);\nx^3-(x^2-y)*x+y^2-(-1+y+x)*x^2\n```\n\n\nIt seems that one needs to call `expand()` explicitly before calling `collect()`. I think this should just be documented in the docstring.\n\nThe problem with `-x^2 + x^2` appearing in the output is probably a bug I introduced while playing with the ordering of the terms. I will take a look at it when I find a chance. It's likely to be later than a week though.",
    "created_at": "2010-05-26T11:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9046#issuecomment-83608",
    "user": "https://github.com/burcin"
}
```

Here is the same session using GiNaC directly via `ginsh`:


```
> t= -a*x^3 - a*x*y^2 + 2*b*x^2*y + 2*y^3 + x^2*z + y^2*z + x^2 + y^2 + a*x;
x^2+2*y*b*x^2+y^2+y^2*z+a*x+2*y^3-a*x^3-y^2*a*x+z*x^2
> t;
x^2+2*y*b*x^2+y^2+y^2*z+a*x+2*y^3-a*x^3-y^2*a*x+z*x^2
> collect(t, x);
(1+2*y*b+z)*x^2+y^2+y^2*z+2*y^3-a*x^3-(y^2*a-a)*x
> u = (x^2+(y-x^2)*(y+x));
x^2-(y+x)*(x^2-y)
> collect(u, x);
x^3-(x^2-y)*x+y^2-(-1+y+x)*x^2
```


It seems that one needs to call `expand()` explicitly before calling `collect()`. I think this should just be documented in the docstring.

The problem with `-x^2 + x^2` appearing in the output is probably a bug I introduced while playing with the ordering of the terms. I will take a look at it when I find a chance. It's likely to be later than a week though.



---

archive/issue_comments_083609.json:
```json
{
    "body": "Changing keywords from \"\" to \"pynac\".",
    "created_at": "2010-05-26T11:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9046#issuecomment-83609",
    "user": "https://github.com/burcin"
}
```

Changing keywords from "" to "pynac".



---

archive/issue_comments_083610.json:
```json
{
    "body": "Changing priority from critical to minor.",
    "created_at": "2011-03-16T15:32:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9046#issuecomment-83610",
    "user": "https://github.com/kcrisman"
}
```

Changing priority from critical to minor.



---

archive/issue_comments_083611.json:
```json
{
    "body": "This is not critical.",
    "created_at": "2011-03-16T15:32:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9046#issuecomment-83611",
    "user": "https://github.com/kcrisman"
}
```

This is not critical.



---

archive/issue_comments_083612.json:
```json
{
    "body": "Changing component from calculus to symbolics.",
    "created_at": "2012-07-07T02:52:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9046#issuecomment-83612",
    "user": "https://github.com/kcrisman"
}
```

Changing component from calculus to symbolics.



---

archive/issue_comments_083613.json:
```json
{
    "body": "It turns out that #11839 was opened and did the first part of this ticket, including documenting the `expand()` issue.\n\nHowever, the bug remains, so I'll just change this ticket to be about it.",
    "created_at": "2012-07-07T02:52:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9046#issuecomment-83613",
    "user": "https://github.com/kcrisman"
}
```

It turns out that #11839 was opened and did the first part of this ticket, including documenting the `expand()` issue.

However, the bug remains, so I'll just change this ticket to be about it.



---

archive/issue_comments_083614.json:
```json
{
    "body": "With the new description, this is probably a duplicate of #9880. I will check if the pynac changes for that ticket fix this one.",
    "created_at": "2012-07-07T07:22:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9046#issuecomment-83614",
    "user": "https://github.com/burcin"
}
```

With the new description, this is probably a duplicate of #9880. I will check if the pynac changes for that ticket fix this one.



---

archive/issue_comments_083615.json:
```json
{
    "body": "bug still present in Sage 5.0.\n\nPaul",
    "created_at": "2012-07-09T12:50:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9046#issuecomment-83615",
    "user": "https://github.com/zimmermann6"
}
```

bug still present in Sage 5.0.

Paul



---

archive/issue_comments_083616.json:
```json
{
    "body": "This is a duplicate of #9880. With [the Pynac patch queue](https://bitbucket.org/burcin/pynac-patches/src) and patches listed on #9880, I get:\n\n\n```\nsage: var('a b x y z')\n(a, b, x, y, z)\nsage: p = -a*x^3 - a*x*y^2 + 2*b*x^2*y + 2*y^3 + x^2*z + y^2*z + x^2 + y^2 + a>\nsage: p.collect(x)\n-a*x^3 + (2*b*y + z + 1)*x^2 + 2*y^3 + y^2*z - (a*y^2 - a)*x + y^2\n```\n\n\nWe should close this after adding it as a doctest to #9880.",
    "created_at": "2012-07-10T09:15:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9046#issuecomment-83616",
    "user": "https://github.com/burcin"
}
```

This is a duplicate of #9880. With [the Pynac patch queue](https://bitbucket.org/burcin/pynac-patches/src) and patches listed on #9880, I get:


```
sage: var('a b x y z')
(a, b, x, y, z)
sage: p = -a*x^3 - a*x*y^2 + 2*b*x^2*y + 2*y^3 + x^2*z + y^2*z + x^2 + y^2 + a>
sage: p.collect(x)
-a*x^3 + (2*b*y + z + 1)*x^2 + 2*y^3 + y^2*z - (a*y^2 - a)*x + y^2
```


We should close this after adding it as a doctest to #9880.



---

archive/issue_comments_083617.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-07-10T09:15:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9046#issuecomment-83617",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083618.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-07-27T13:00:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9046#issuecomment-83618",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083619.json:
```json
{
    "body": "Doctest is in attachment:trac_9880-doctest_for_9046.patch:ticket:9880. This can be closed now.",
    "created_at": "2012-07-27T13:00:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9046#issuecomment-83619",
    "user": "https://github.com/burcin"
}
```

Doctest is in attachment:trac_9880-doctest_for_9046.patch:ticket:9880. This can be closed now.



---

archive/issue_comments_083620.json:
```json
{
    "body": "Burcin,\n\nfirst the ticket number is wrong (13107 instead of 9046) then the input p was mangled\n(ends with `a>` instead of `a*x`).\n\nPaul",
    "created_at": "2012-07-27T13:13:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9046#issuecomment-83620",
    "user": "https://github.com/zimmermann6"
}
```

Burcin,

first the ticket number is wrong (13107 instead of 9046) then the input p was mangled
(ends with `a>` instead of `a*x`).

Paul



---

archive/issue_comments_083621.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-07-27T13:13:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9046#issuecomment-83621",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_083622.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-11-21T21:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9046#issuecomment-83622",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083623.json:
```json
{
    "body": "I replaced the patch attached to #9880:\n\nattachment:trac_9880-doctest_for_9046.patch:ticket:9880\n\nI hope I got it right this time. Sorry for the noise.",
    "created_at": "2012-11-21T21:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9046#issuecomment-83623",
    "user": "https://github.com/burcin"
}
```

I replaced the patch attached to #9880:

attachment:trac_9880-doctest_for_9046.patch:ticket:9880

I hope I got it right this time. Sorry for the noise.



---

archive/issue_comments_083624.json:
```json
{
    "body": "the patch is ok now. But since #9880 is not yet fixed, the doctest will fail. Thus we should wait for #9880 to review this one...\n\nPaul",
    "created_at": "2012-11-22T08:11:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9046#issuecomment-83624",
    "user": "https://github.com/zimmermann6"
}
```

the patch is ok now. But since #9880 is not yet fixed, the doctest will fail. Thus we should wait for #9880 to review this one...

Paul



---

archive/issue_comments_083625.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-18T19:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9046#issuecomment-83625",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083626.json:
```json
{
    "body": "That ticket has been merged, so I think this can be closed.",
    "created_at": "2013-06-18T19:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9046#issuecomment-83626",
    "user": "https://github.com/kcrisman"
}
```

That ticket has been merged, so I think this can be closed.



---

archive/issue_comments_083627.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-06-19T12:17:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9046#issuecomment-83627",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_009198.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-06-19T12:17:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9046",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9046#event-9198"
}
```
