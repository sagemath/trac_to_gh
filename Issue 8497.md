# Issue 8497: bug in simplify_rational

archive/issues_008497.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  kcrisman burcin jason mhansen\n\nKeywords: simplify, radical, sqrt\n\nthe documentation of `simplify_radical` says:\n\n```\nsage: x.simplify_radical?\n...\n       Simplifies this symbolic expression, which can contain logs,\n       exponentials, and radicals, by converting it into a form which is\n       canonical over a large class of expressions and a given ordering of\n       variables\n```\n\nhowever if indeed it is able to recognize zero:\n\n```\nsage: a=1/(sqrt(5)+sqrt(2))-(sqrt(5)-sqrt(2))/3\nsage: a.simplify_radical()\n0\n```\n\nit does *not* return a canonical expression:\n\n```\nsage: a1=1/(sqrt(5)+sqrt(2))\nsage: a2=(sqrt(5)-sqrt(2))/3\nsage: a1.simplify_radical()\n1/(sqrt(2) + sqrt(5))\nsage: a2.simplify_radical()\n-1/3*sqrt(2) + 1/3*sqrt(5)\nsage: (a1-a2).simplify_radical()\n0\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8497\n\n",
    "created_at": "2010-03-11T10:33:15Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "bug in simplify_rational",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8497",
    "user": "zimmerma"
}
```
Assignee: burcin

CC:  kcrisman burcin jason mhansen

Keywords: simplify, radical, sqrt

the documentation of `simplify_radical` says:

```
sage: x.simplify_radical?
...
       Simplifies this symbolic expression, which can contain logs,
       exponentials, and radicals, by converting it into a form which is
       canonical over a large class of expressions and a given ordering of
       variables
```

however if indeed it is able to recognize zero:

```
sage: a=1/(sqrt(5)+sqrt(2))-(sqrt(5)-sqrt(2))/3
sage: a.simplify_radical()
0
```

it does *not* return a canonical expression:

```
sage: a1=1/(sqrt(5)+sqrt(2))
sage: a2=(sqrt(5)-sqrt(2))/3
sage: a1.simplify_radical()
1/(sqrt(2) + sqrt(5))
sage: a2.simplify_radical()
-1/3*sqrt(2) + 1/3*sqrt(5)
sage: (a1-a2).simplify_radical()
0
```


Issue created by migration from https://trac.sagemath.org/ticket/8497





---

archive/issue_comments_076683.json:
```json
{
    "body": "Note the original question posed to me was: how to multiply say 1/(1+sqrt(2)+sqrt(3)) by the\nconjugate expression?",
    "created_at": "2010-03-11T10:38:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76683",
    "user": "zimmerma"
}
```

Note the original question posed to me was: how to multiply say 1/(1+sqrt(2)+sqrt(3)) by the
conjugate expression?



---

archive/issue_comments_076684.json:
```json
{
    "body": "This is the full docstring from Maxima:\n\n\n```\nSimplifies expr, which can contain logs, exponentials, and radicals, by converting it into a form which is canonical over a large class of expressions and a given ordering of variables; that is, all functionally equivalent forms are mapped into a unique form. For a somewhat larger class of expressions, radcan produces a regular form. Two equivalent expressions in this class do not necessarily have the same appearance, but their difference can be simplified by radcan to zero.\n\n    For some expressions radcan is quite time consuming. This is the cost of exploring certain relationships among the components of the expression for simplifications based on factoring and partial-fraction expansions of exponents. \n```\n\n\nPerhaps we should include this",
    "created_at": "2010-03-11T17:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76684",
    "user": "mhansen"
}
```

This is the full docstring from Maxima:


```
Simplifies expr, which can contain logs, exponentials, and radicals, by converting it into a form which is canonical over a large class of expressions and a given ordering of variables; that is, all functionally equivalent forms are mapped into a unique form. For a somewhat larger class of expressions, radcan produces a regular form. Two equivalent expressions in this class do not necessarily have the same appearance, but their difference can be simplified by radcan to zero.

    For some expressions radcan is quite time consuming. This is the cost of exploring certain relationships among the components of the expression for simplifications based on factoring and partial-fraction expansions of exponents. 
```


Perhaps we should include this



---

archive/issue_comments_076685.json:
```json
{
    "body": "> Perhaps we should include this \n\nyes (unless of course upstream finds a way to get a real canonical form).\nAnd maybe adding an example showing the difference when checking for 0.",
    "created_at": "2010-03-11T19:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76685",
    "user": "zimmerma"
}
```

> Perhaps we should include this 

yes (unless of course upstream finds a way to get a real canonical form).
And maybe adding an example showing the difference when checking for 0.



---

archive/issue_comments_076686.json:
```json
{
    "body": "What is really going on here is that `simplify_radical` uses `radcan` under the hood, which treats things as symbolic expressions, not functions, and just chooses a branch - consistently, but arbitrarily.  At least I think that is what is going on here.  See [the Maxima list thread starting here](http://www.math.utexas.edu/pipermail/maxima/2011/026097.html).",
    "created_at": "2011-09-23T14:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76686",
    "user": "kcrisman"
}
```

What is really going on here is that `simplify_radical` uses `radcan` under the hood, which treats things as symbolic expressions, not functions, and just chooses a branch - consistently, but arbitrarily.  At least I think that is what is going on here.  See [the Maxima list thread starting here](http://www.math.utexas.edu/pipermail/maxima/2011/026097.html).



---

archive/issue_comments_076687.json:
```json
{
    "body": "then should we simply change the documentation, in saying that `simplify_radical` gives a\ncanonical expression for zero, but if a and b are two identical expressions, they might not\nbe \"simplified\" to the same expression?\n\nPaul",
    "created_at": "2011-09-23T14:57:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76687",
    "user": "zimmerma"
}
```

then should we simply change the documentation, in saying that `simplify_radical` gives a
canonical expression for zero, but if a and b are two identical expressions, they might not
be "simplified" to the same expression?

Paul



---

archive/issue_comments_076688.json:
```json
{
    "body": "You are correct.  I was just updating, though, at this point.  \n\nIt gets worse, because some expressions that are definitely not 1 will simplify to just 1, because that is the branch that was picked.  See [this ask.sagemath.org question](http://ask.sagemath.org/question/767/simplification-errors-in-simple-expressions), and Fateman's accurate response.",
    "created_at": "2011-09-23T14:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76688",
    "user": "kcrisman"
}
```

You are correct.  I was just updating, though, at this point.  

It gets worse, because some expressions that are definitely not 1 will simplify to just 1, because that is the branch that was picked.  See [this ask.sagemath.org question](http://ask.sagemath.org/question/767/simplification-errors-in-simple-expressions), and Fateman's accurate response.



---

archive/issue_comments_076689.json:
```json
{
    "body": "then I suggest to simply remove this function from Sage, unless there are ideas how to fix it.\n\nPaul",
    "created_at": "2011-09-23T15:05:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76689",
    "user": "zimmerma"
}
```

then I suggest to simply remove this function from Sage, unless there are ideas how to fix it.

Paul



---

archive/issue_comments_076690.json:
```json
{
    "body": "Well, in Fateman's eyes (and I would remind that he is an expert, if not THE expert, in this), the only bug is in users who treat these *expressions* as *functions*.  At least, that's how I interpret it.  So updating the documentation may be the better way.\n\nBut this shouldn't be a duologue; hopefully some others will have ideas.  Cc:ing a few others who have thought about at least one or two of these things, just in case they have thoughts at this time.  Otherwise it will sit - I simply don't have time to deal with it right now, because it needs to be part of a general overhaul of simplification if we don't just change documentation.",
    "created_at": "2011-09-23T15:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76690",
    "user": "kcrisman"
}
```

Well, in Fateman's eyes (and I would remind that he is an expert, if not THE expert, in this), the only bug is in users who treat these *expressions* as *functions*.  At least, that's how I interpret it.  So updating the documentation may be the better way.

But this shouldn't be a duologue; hopefully some others will have ideas.  Cc:ing a few others who have thought about at least one or two of these things, just in case they have thoughts at this time.  Otherwise it will sit - I simply don't have time to deal with it right now, because it needs to be part of a general overhaul of simplification if we don't just change documentation.



---

archive/issue_comments_076691.json:
```json
{
    "body": "I mean change documentation to give examples in prominent places, both in `simplify_radical` and `simplify_full`.",
    "created_at": "2011-09-23T15:20:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76691",
    "user": "kcrisman"
}
```

I mean change documentation to give examples in prominent places, both in `simplify_radical` and `simplify_full`.



---

archive/issue_comments_076692.json:
```json
{
    "body": "I believe we should at least add such examples to the documentation, to warn the user that in some\ncases no canonical form is returned.\n\nPaul",
    "created_at": "2011-09-24T07:21:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76692",
    "user": "zimmerma"
}
```

I believe we should at least add such examples to the documentation, to warn the user that in some
cases no canonical form is returned.

Paul



---

archive/issue_comments_076693.json:
```json
{
    "body": "Okay.  So whoever does this ticket will do that :)\n\n(Incidentally, mentioning that they *are* canonical, but in Fateman's sense of expressions, not in the way we would think of them as functions.)",
    "created_at": "2011-09-24T14:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76693",
    "user": "kcrisman"
}
```

Okay.  So whoever does this ticket will do that :)

(Incidentally, mentioning that they *are* canonical, but in Fateman's sense of expressions, not in the way we would think of them as functions.)



---

archive/issue_comments_076694.json:
```json
{
    "body": "Attachment [trac_8497.patch](tarball://root/attachments/some-uuid/ticket8497/trac_8497.patch) by zimmerma created at 2011-09-25 21:04:40",
    "created_at": "2011-09-25T21:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76694",
    "user": "zimmerma"
}
```

Attachment [trac_8497.patch](tarball://root/attachments/some-uuid/ticket8497/trac_8497.patch) by zimmerma created at 2011-09-25 21:04:40



---

archive/issue_comments_076695.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-09-25T21:06:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76695",
    "user": "zimmerma"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076696.json:
```json
{
    "body": "the attached patch implements what I suggest in comment [comment:11].\n\nPaul",
    "created_at": "2011-09-25T21:06:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76696",
    "user": "zimmerma"
}
```

the attached patch implements what I suggest in comment [comment:11].

Paul



---

archive/issue_comments_076697.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-10-07T09:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76697",
    "user": "burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076698.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2011-10-07T09:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76698",
    "user": "burcin"
}
```

Looks good to me.



---

archive/issue_comments_076699.json:
```json
{
    "body": "Fixed some formatting of the documentation, needs review.",
    "created_at": "2011-10-07T12:32:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76699",
    "user": "jdemeyer"
}
```

Fixed some formatting of the documentation, needs review.



---

archive/issue_comments_076700.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-10-07T12:32:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76700",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_076701.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-10-07T12:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76701",
    "user": "jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076702.json:
```json
{
    "body": "Fixed doc formatting, apply only this",
    "created_at": "2011-10-07T13:21:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76702",
    "user": "jdemeyer"
}
```

Fixed doc formatting, apply only this



---

archive/issue_comments_076703.json:
```json
{
    "body": "Attachment [8497_fix_doc.patch](tarball://root/attachments/some-uuid/ticket8497/8497_fix_doc.patch) by kcrisman created at 2011-10-07 16:52:47\n\nI feel that we should at least ask on the Maxima list about whether this is truly \"not canonical\".  My understanding is that Fateman would say it is canonical as an *expression*, not as a *function*.   If I'm the only one who feels this way, I'll let it slide.   But I figure we would want him to give us benefit of the doubt in our areas of expertise.",
    "created_at": "2011-10-07T16:52:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76703",
    "user": "kcrisman"
}
```

Attachment [8497_fix_doc.patch](tarball://root/attachments/some-uuid/ticket8497/8497_fix_doc.patch) by kcrisman created at 2011-10-07 16:52:47

I feel that we should at least ask on the Maxima list about whether this is truly "not canonical".  My understanding is that Fateman would say it is canonical as an *expression*, not as a *function*.   If I'm the only one who feels this way, I'll let it slide.   But I figure we would want him to give us benefit of the doubt in our areas of expertise.



---

archive/issue_comments_076704.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-10-07T16:52:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76704",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_076705.json:
```json
{
    "body": "For me, a \"canonical expression\" means that two mathematically identical expressions simplify to\nthe *exactly same* expression. Thus it is clearly not canonical. Feel free to ask on the Maxima\nlist, but this should not delay this ticket.\n\nPaul",
    "created_at": "2011-10-08T09:23:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76705",
    "user": "zimmerma"
}
```

For me, a "canonical expression" means that two mathematically identical expressions simplify to
the *exactly same* expression. Thus it is clearly not canonical. Feel free to ask on the Maxima
list, but this should not delay this ticket.

Paul



---

archive/issue_comments_076706.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-10-08T09:40:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76706",
    "user": "jdemeyer"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_076707.json:
```json
{
    "body": "Replying to [comment:18 zimmerma]:\n> this should not delay this ticket.\n\nI agree but somebody needs to review my reformatting of the documentation.",
    "created_at": "2011-10-08T09:40:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76707",
    "user": "jdemeyer"
}
```

Replying to [comment:18 zimmerma]:
> this should not delay this ticket.

I agree but somebody needs to review my reformatting of the documentation.



---

archive/issue_comments_076708.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-10-10T08:58:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76708",
    "user": "burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076709.json:
```json
{
    "body": "I am not well versed in ReST, but AFAICT, Jeroen's changes make sense.\n\nMaxima documentation on `radcan()` (below) is rather vague. Based on this text, we shouldn't make bold claims about canonical results in the Sage documentation. I am switching this back to positive review.\n\n\n```\nSimplifies expr, which can contain logs, exponentials, and radicals, by\nconverting it into a form which is canonical over a large class of expressions\nand a given ordering of variables; that is, all functionally equivalent forms\nare mapped into a unique form. For a somewhat larger class of expressions,\nradcan produces a regular form. Two equivalent expressions in this class do\nnot necessarily have the same appearance, but their difference can be\nsimplified by radcan to zero.\n\nFor some expressions radcan is quite time consuming. This is the cost of\nexploring certain relationships among the components of the expression for\nsimplifications based on factoring and partial-fraction expansions of\nexponents. \n```\n\n\nWe can open an enhancement ticket to clarify what \n* * a large class of expressions*\n* *functionally equivalent*\n* * regular form*\nmean in the text above, and how the ordering of the variables effect the final result. Ideally, we should have references to a description of the underlying algorithm as well.",
    "created_at": "2011-10-10T08:58:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76709",
    "user": "burcin"
}
```

I am not well versed in ReST, but AFAICT, Jeroen's changes make sense.

Maxima documentation on `radcan()` (below) is rather vague. Based on this text, we shouldn't make bold claims about canonical results in the Sage documentation. I am switching this back to positive review.


```
Simplifies expr, which can contain logs, exponentials, and radicals, by
converting it into a form which is canonical over a large class of expressions
and a given ordering of variables; that is, all functionally equivalent forms
are mapped into a unique form. For a somewhat larger class of expressions,
radcan produces a regular form. Two equivalent expressions in this class do
not necessarily have the same appearance, but their difference can be
simplified by radcan to zero.

For some expressions radcan is quite time consuming. This is the cost of
exploring certain relationships among the components of the expression for
simplifications based on factoring and partial-fraction expansions of
exponents. 
```


We can open an enhancement ticket to clarify what 
* * a large class of expressions*
* *functionally equivalent*
* * regular form*
mean in the text above, and how the ordering of the variables effect the final result. Ideally, we should have references to a description of the underlying algorithm as well.



---

archive/issue_comments_076710.json:
```json
{
    "body": "Okay, that's now #11912.",
    "created_at": "2011-10-10T12:46:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76710",
    "user": "kcrisman"
}
```

Okay, that's now #11912.



---

archive/issue_comments_076711.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-10-10T20:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8497#issuecomment-76711",
    "user": "jdemeyer"
}
```

Resolution: fixed
