# Issue 385: implement at for symbolics

archive/issues_000385.json:
```json
{
    "body": "Assignee: was\n\nCC:  jason burcin was mhansen\n\n\n```\nOn 6/7/07, Randy LeVeque <rjl@amath.washington.edu> wrote:\n> By the way, I'm just trying to figure out how sage does Taylor series.\n> Maybe you can pass this on to whoever the best person is to chat with about\n> this...\n> \n> In maple I can do things like\n> \n> > mtaylor(u(x+h,t+k),[h,k],3);\n>                                                                      2\n> u(x, t) + D[1](u)(x, t) h + D[2](u)(x, t) k + 1/2 D[1, 1](u)(x, t) h\n> \n>                                                      2\n>       + h D[1, 2](u)(x, t) k + 1/2 D[2, 2](u)(x, t) k\n> \n> \n> which is very convenient for numerical analysis when computing truncation\n> errors of finite difference methods (h and k are mesh widths in space and\n> time).  In sage a general expansion of this sort doesn't seem possible even\n> in a single variable, e.g.,\n> \n> sage: taylor(u(x+h),h,0,4)\n> x + h\n> \n> Apparently an undefined function like u(x) is taken to be the identity map?\n\nTo define a formal function, do u = function('u').  Then\n\nsage: u = function('u')\nsage: u(x + h)\nu(x + h)\nsage: diff(u(x+h), x)\ndiff(u(x + h), x, 1)\n\nTo get the Taylor expansion you would do this:\n\nsage: taylor(u(x+h),h,0,4)\n\n-- however -- this currently doesn't work in SAGE since we hadn't considered\ndoing this yet.   What happens is Maxima does the computation and outputs\nthe following expression:\n\n'u(x)+(?%at('diff('u(x+h),h,1),h=0))*h+(?%at('diff('u(x+h),h,2),h=0))*h^2/2+(?%at('diff('u(x+h),h,3),h=0))*h^3/6+(?%at('diff('u(x+h),h,4),h=0))*h^4/24\n\nSAGE doesn't know yet how to parse the \"at\" function, so you get\nan error -- it will have to be added.   [Note that I don't necessarily consider\nmaxima the ultimate underlying engine for SAGE's symbolic computation\ncapabilities -- but it does provide a very quick way for SAGE to have\na powerful symbolic system for which a lot of subtle bugs have\nalready been fixed (over the last 40 years of Maxima development). ]\n\nDefinitely point out lots of things like this in your talk at SD4!\n\n -- William\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/385\n\n",
    "created_at": "2007-06-07T18:51:34Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "implement at for symbolics",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/385",
    "user": "was"
}
```
Assignee: was

CC:  jason burcin was mhansen


```
On 6/7/07, Randy LeVeque <rjl@amath.washington.edu> wrote:
> By the way, I'm just trying to figure out how sage does Taylor series.
> Maybe you can pass this on to whoever the best person is to chat with about
> this...
> 
> In maple I can do things like
> 
> > mtaylor(u(x+h,t+k),[h,k],3);
>                                                                      2
> u(x, t) + D[1](u)(x, t) h + D[2](u)(x, t) k + 1/2 D[1, 1](u)(x, t) h
> 
>                                                      2
>       + h D[1, 2](u)(x, t) k + 1/2 D[2, 2](u)(x, t) k
> 
> 
> which is very convenient for numerical analysis when computing truncation
> errors of finite difference methods (h and k are mesh widths in space and
> time).  In sage a general expansion of this sort doesn't seem possible even
> in a single variable, e.g.,
> 
> sage: taylor(u(x+h),h,0,4)
> x + h
> 
> Apparently an undefined function like u(x) is taken to be the identity map?

To define a formal function, do u = function('u').  Then

sage: u = function('u')
sage: u(x + h)
u(x + h)
sage: diff(u(x+h), x)
diff(u(x + h), x, 1)

To get the Taylor expansion you would do this:

sage: taylor(u(x+h),h,0,4)

-- however -- this currently doesn't work in SAGE since we hadn't considered
doing this yet.   What happens is Maxima does the computation and outputs
the following expression:

'u(x)+(?%at('diff('u(x+h),h,1),h=0))*h+(?%at('diff('u(x+h),h,2),h=0))*h^2/2+(?%at('diff('u(x+h),h,3),h=0))*h^3/6+(?%at('diff('u(x+h),h,4),h=0))*h^4/24

SAGE doesn't know yet how to parse the "at" function, so you get
an error -- it will have to be added.   [Note that I don't necessarily consider
maxima the ultimate underlying engine for SAGE's symbolic computation
capabilities -- but it does provide a very quick way for SAGE to have
a powerful symbolic system for which a lot of subtle bugs have
already been fixed (over the last 40 years of Maxima development). ]

Definitely point out lots of things like this in your talk at SD4!

 -- William
```


Issue created by migration from https://trac.sagemath.org/ticket/385





---

archive/issue_comments_001883.json:
```json
{
    "body": "Changing assignee from was to gfurnish.",
    "created_at": "2008-03-16T20:12:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/385#issuecomment-1883",
    "user": "gfurnish"
}
```

Changing assignee from was to gfurnish.



---

archive/issue_comments_001884.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-16T20:12:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/385#issuecomment-1884",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_001885.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:20:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/385#issuecomment-1885",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_001886.json:
```json
{
    "body": "This would also resolve #3914.",
    "created_at": "2009-09-28T20:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/385#issuecomment-1886",
    "user": "kcrisman"
}
```

This would also resolve #3914.



---

archive/issue_comments_001887.json:
```json
{
    "body": "Try this patch.  It should do the trick.  Notice that I do not make it a normal symbolic function like in functions/other.py or something, because it's only for use here for now.  If necessary, I could do that, though - it's a nice second way to do things instead of .subs(), so I could also import it globally if appropriate.  I put in doctests for this, #3914, and a direct call.",
    "created_at": "2009-10-09T16:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/385#issuecomment-1887",
    "user": "kcrisman"
}
```

Try this patch.  It should do the trick.  Notice that I do not make it a normal symbolic function like in functions/other.py or something, because it's only for use here for now.  If necessary, I could do that, though - it's a nice second way to do things instead of .subs(), so I could also import it globally if appropriate.  I put in doctests for this, #3914, and a direct call.



---

archive/issue_comments_001888.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-09T16:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/385#issuecomment-1888",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_001889.json:
```json
{
    "body": "Attachment 'trac_385-at-evaluate.patch' not found :(",
    "created_at": "2009-10-10T23:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/385#issuecomment-1889",
    "user": "robert.marik"
}
```

Attachment 'trac_385-at-evaluate.patch' not found :(



---

archive/issue_comments_001890.json:
```json
{
    "body": "Based on 4.1.2.alpha4",
    "created_at": "2009-10-12T16:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/385#issuecomment-1890",
    "user": "kcrisman"
}
```

Based on 4.1.2.alpha4



---

archive/issue_comments_001891.json:
```json
{
    "body": "Attachment [trac_385-at-evaluate.patch](tarball://root/attachments/some-uuid/ticket385/trac_385-at-evaluate.patch) by kcrisman created at 2009-10-12 16:49:04\n\nReplying to [comment:6 robert.marik]:\n> Attachment 'trac_385-at-evaluate.patch' not found :(\n\nIt must have gotten lost somewhere during the latest Trac outage.   This should work now.",
    "created_at": "2009-10-12T16:49:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/385#issuecomment-1891",
    "user": "kcrisman"
}
```

Attachment [trac_385-at-evaluate.patch](tarball://root/attachments/some-uuid/ticket385/trac_385-at-evaluate.patch) by kcrisman created at 2009-10-12 16:49:04

Replying to [comment:6 robert.marik]:
> Attachment 'trac_385-at-evaluate.patch' not found :(

It must have gotten lost somewhere during the latest Trac outage.   This should work now.



---

archive/issue_comments_001892.json:
```json
{
    "body": "Passes sage -testall and does what it claims. Adds some very very useful functionality.",
    "created_at": "2009-10-24T20:07:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/385#issuecomment-1892",
    "user": "wdj"
}
```

Passes sage -testall and does what it claims. Adds some very very useful functionality.



---

archive/issue_comments_001893.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-24T20:07:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/385#issuecomment-1893",
    "user": "wdj"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_001894.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-31T16:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/385#issuecomment-1894",
    "user": "mhansen"
}
```

Resolution: fixed
