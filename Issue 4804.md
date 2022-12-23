# Issue 4804: add latex output for ceiling, floor, and derivative functions

archive/issues_004804.json:
```json
{
    "body": "Assignee: burcin\n\nThis could look better:\n\n```\nsage: latex(ceil(x) + floor(x) + derivative(floor(x)))\n{{d}\\over{d\\,x}}\\,\\left \\lfloor x \\right \\rfloor + \\text{floor} \\left( x \\right) + \\text{ceil} \\left( x \\right)\n```\n\n\nNotice that floor and ceil do not have special latex support except strangely inside the derivative. Also, the derivative would be better written as a partial derivative, since that's what it is in Sage in general. \n\nAlso, this guy wrote to sage-support 3 or 4 times about this and was ignored:\n\n```\nDear all,\n\nI tried to reply my questions below to an existing thread (notation\nfor derivatives) but for some reason it didn't work. So I opened this\nnew one.\n\nI use the derivative function and want to get an output in latex\nstyle. At the moment the output looks quite good but imho it would be\nnicer if it uses the \"\\partial\" latex command. It is possible to\nimplement this? Further I use the floor and ceil functions. Would it\nbe possible to implement a latex output for these functions too?\n\nThanks,\nAndreas\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4804\n\n",
    "created_at": "2008-12-15T15:38:30Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "add latex output for ceiling, floor, and derivative functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4804",
    "user": "was"
}
```
Assignee: burcin

This could look better:

```
sage: latex(ceil(x) + floor(x) + derivative(floor(x)))
{{d}\over{d\,x}}\,\left \lfloor x \right \rfloor + \text{floor} \left( x \right) + \text{ceil} \left( x \right)
```


Notice that floor and ceil do not have special latex support except strangely inside the derivative. Also, the derivative would be better written as a partial derivative, since that's what it is in Sage in general. 

Also, this guy wrote to sage-support 3 or 4 times about this and was ignored:

```
Dear all,

I tried to reply my questions below to an existing thread (notation
for derivatives) but for some reason it didn't work. So I opened this
new one.

I use the derivative function and want to get an output in latex
style. At the moment the output looks quite good but imho it would be
nicer if it uses the "\partial" latex command. It is possible to
implement this? Further I use the floor and ceil functions. Would it
be possible to implement a latex output for these functions too?

Thanks,
Andreas
```


Issue created by migration from https://trac.sagemath.org/ticket/4804





---

archive/issue_comments_036412.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-15T18:14:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4804#issuecomment-36412",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036413.json:
```json
{
    "body": "Changing assignee from burcin to mhansen.",
    "created_at": "2008-12-15T18:14:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4804#issuecomment-36413",
    "user": "mhansen"
}
```

Changing assignee from burcin to mhansen.



---

archive/issue_comments_036414.json:
```json
{
    "body": "I don't agree with the positive review, since the change breaks the latex output for\nmaxima expressions:\n\n\n```\nsage: m = maxima('d/(d-2)')\nsage: latex(m)\n{{\\partial}\\over{d-2}}\n```\n\n\nCheers,\n\nWilfried",
    "created_at": "2008-12-16T10:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4804#issuecomment-36414",
    "user": "whuss"
}
```

I don't agree with the positive review, since the change breaks the latex output for
maxima expressions:


```
sage: m = maxima('d/(d-2)')
sage: latex(m)
{{\partial}\over{d-2}}
```


Cheers,

Wilfried



---

archive/issue_comments_036415.json:
```json
{
    "body": "Good catch. I've updated the patch to deal with this.",
    "created_at": "2008-12-16T11:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4804#issuecomment-36415",
    "user": "mhansen"
}
```

Good catch. I've updated the patch to deal with this.



---

archive/issue_comments_036416.json:
```json
{
    "body": "It is still not correct:\n\n\n```\nsage: m = maxima('2*diff(f(x), x)')\nsage: latex(m)\n2\\,\\left({{d}\\over{d\\,x}}\\,f\\left(x\\right)\\right)\n```\n\n\nThis should be changed in the maxima code, there\nit should be trivial. Trying to guess what part\nof the latex representation is a differential\nseems very error prone to me.\n\nCheers,\n\nWilfried",
    "created_at": "2008-12-16T13:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4804#issuecomment-36416",
    "user": "whuss"
}
```

It is still not correct:


```
sage: m = maxima('2*diff(f(x), x)')
sage: latex(m)
2\,\left({{d}\over{d\,x}}\,f\left(x\right)\right)
```


This should be changed in the maxima code, there
it should be trivial. Trying to guess what part
of the latex representation is a differential
seems very error prone to me.

Cheers,

Wilfried



---

archive/issue_comments_036417.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-12-16T14:53:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4804#issuecomment-36417",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_036418.json:
```json
{
    "body": "I put up a new plot which changes the tex code in maxima.  I'm not sure how to get rid of the \\it's but they're harmless.",
    "created_at": "2008-12-16T14:54:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4804#issuecomment-36418",
    "user": "mhansen"
}
```

I put up a new plot which changes the tex code in maxima.  I'm not sure how to get rid of the \it's but they're harmless.



---

archive/issue_comments_036419.json:
```json
{
    "body": "I will review this at some point today.",
    "created_at": "2008-12-29T20:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4804#issuecomment-36419",
    "user": "mhampton"
}
```

I will review this at some point today.



---

archive/issue_comments_036420.json:
```json
{
    "body": "This seems to work.  I'm not sure that I agree that partial derivatives look better, but I don't feel strongly about it.  It certainly is better for multivariate cases.",
    "created_at": "2008-12-29T21:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4804#issuecomment-36420",
    "user": "mhampton"
}
```

This seems to work.  I'm not sure that I agree that partial derivatives look better, but I don't feel strongly about it.  It certainly is better for multivariate cases.



---

archive/issue_comments_036421.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-12T01:21:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4804#issuecomment-36421",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha0



---

archive/issue_comments_036422.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-12T01:21:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4804#issuecomment-36422",
    "user": "mabshoff"
}
```

Resolution: fixed
