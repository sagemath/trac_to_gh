# Issue 6237: repeated roots with roots(CDF, multiplicities=False)

archive/issues_006237.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: roots CDF multiplicities\n\n```\nsage: pari('v')\nv\nsage: pari('u')\nu\nsage: u = QQ['u'].0\nsage: v = QQ['u']['v'].0\nsage: f = v^3 - u^7 + 2*u^3*v\nsage: f.discriminant()\n-27*u^14 - 32*u^9\nsage: f.discriminant().roots(CDF, multiplicities=False)\n\n[-1.03456371594,\n 0,\n 0,\n 0,\n 0,\n 0,\n 0,\n 0,\n 0,\n 0,\n -0.31969776999 - 0.983928563571*I,\n -0.31969776999 + 0.983928563571*I,\n 0.836979627962 - 0.608101294789*I,\n 0.836979627962 + 0.608101294789*I]\n```\n\nNote the repetition of 0.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6237\n\n",
    "created_at": "2009-06-06T22:30:12Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "repeated roots with roots(CDF, multiplicities=False)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6237",
    "user": "https://github.com/ncalexan"
}
```
Assignee: somebody

Keywords: roots CDF multiplicities

```
sage: pari('v')
v
sage: pari('u')
u
sage: u = QQ['u'].0
sage: v = QQ['u']['v'].0
sage: f = v^3 - u^7 + 2*u^3*v
sage: f.discriminant()
-27*u^14 - 32*u^9
sage: f.discriminant().roots(CDF, multiplicities=False)

[-1.03456371594,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 -0.31969776999 - 0.983928563571*I,
 -0.31969776999 + 0.983928563571*I,
 0.836979627962 - 0.608101294789*I,
 0.836979627962 + 0.608101294789*I]
```

Note the repetition of 0.

Issue created by migration from https://trac.sagemath.org/ticket/6237





---

archive/issue_comments_049724.json:
```json
{
    "body": "And if you run it with just `roots(CDF)` you get nine different occurrences of (0, 1), i.e. root 0 with multiplicity 1.\n\nThe attached patch fixes this.",
    "created_at": "2010-01-02T04:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6237#issuecomment-49724",
    "user": "https://github.com/aghitza"
}
```

And if you run it with just `roots(CDF)` you get nine different occurrences of (0, 1), i.e. root 0 with multiplicity 1.

The attached patch fixes this.



---

archive/issue_comments_049725.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-02T04:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6237#issuecomment-49725",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_049726.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-01-04T15:37:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6237#issuecomment-49726",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_049727.json:
```json
{
    "body": "This is fine overall, assuming the answer to the following question is yes.\n\n```\n            if output_complex:\n                rts = sort_complex_numbers_for_display([L(root) for root in ext_rts])\n            else:\n                rts = [L(root.real()) for root in ext_rts if root.imag() == 0]\n```\nThe first list gives a canonical ordering, so using \n\n```\n                rts_mult.append((rt, mult))\n                j += mult\n```\nis okay, it won't append the same thing twice.  Is that also true for the second list?  I couldn't come up with an example that breaks it, but that just means I don't know much about how polynomials are represented internally.  At any rate, it should probably be ordered, just to be on the safe side, if you use that way of finding multiplicities.  Does Pari not compute multiplicities for this?  Maxima's implementation does, though perhaps it doesn't do arbitrary precision.  I assume numpy definitely doesn't do multiplicities.",
    "created_at": "2010-01-04T15:37:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6237#issuecomment-49727",
    "user": "https://github.com/kcrisman"
}
```

This is fine overall, assuming the answer to the following question is yes.

```
            if output_complex:
                rts = sort_complex_numbers_for_display([L(root) for root in ext_rts])
            else:
                rts = [L(root.real()) for root in ext_rts if root.imag() == 0]
```
The first list gives a canonical ordering, so using 

```
                rts_mult.append((rt, mult))
                j += mult
```
is okay, it won't append the same thing twice.  Is that also true for the second list?  I couldn't come up with an example that breaks it, but that just means I don't know much about how polynomials are represented internally.  At any rate, it should probably be ordered, just to be on the safe side, if you use that way of finding multiplicities.  Does Pari not compute multiplicities for this?  Maxima's implementation does, though perhaps it doesn't do arbitrary precision.  I assume numpy definitely doesn't do multiplicities.



---

archive/issue_comments_049728.json:
```json
{
    "body": "Thanks for catching this.\n\nFrom Pari's documentation for the function we're using:\n\n```\npolroots(pol,{flag = 0})\n\ncomplex roots of the polynomial pol, given as a column vector where each root is repeated according to its multiplicity. [...]\n\nThe algorithm used is a modification of A.Sch\u00a8nhage's root-finding algorithm, due to and implemented by X.Gourdon. Barring bugs, it is guaranteed to converge and to give the roots to the required accuracy.\n```\n\nThere is no mention of the roots being sorted.  I guess I could read the source code and find out, but I like you suggestion of sorting the Pari output anyway -- just in case they change the behaviour in the future.\n\nAlso from the above snippet, Pari indeed does not give the multiplicities, it just repeats each root the correct number of times.\n\nI will replace the patch soon.",
    "created_at": "2010-01-04T23:20:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6237#issuecomment-49728",
    "user": "https://github.com/aghitza"
}
```

Thanks for catching this.

From Pari's documentation for the function we're using:

```
polroots(pol,{flag = 0})

complex roots of the polynomial pol, given as a column vector where each root is repeated according to its multiplicity. [...]

The algorithm used is a modification of A.Sch¨nhage's root-finding algorithm, due to and implemented by X.Gourdon. Barring bugs, it is guaranteed to converge and to give the roots to the required accuracy.
```

There is no mention of the roots being sorted.  I guess I could read the source code and find out, but I like you suggestion of sorting the Pari output anyway -- just in case they change the behaviour in the future.

Also from the above snippet, Pari indeed does not give the multiplicities, it just repeats each root the correct number of times.

I will replace the patch soon.



---

archive/issue_comments_049729.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-01-04T23:20:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6237#issuecomment-49729",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_049730.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-04T23:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6237#issuecomment-49730",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_049731.json:
```json
{
    "body": "Attachment [trac_6237.patch](tarball://root/attachments/some-uuid/ticket6237/trac_6237.patch) by @aghitza created at 2010-01-04 23:56:23\n\nOK, the revised patch is up.",
    "created_at": "2010-01-04T23:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6237#issuecomment-49731",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_6237.patch](tarball://root/attachments/some-uuid/ticket6237/trac_6237.patch) by @aghitza created at 2010-01-04 23:56:23

OK, the revised patch is up.



---

archive/issue_comments_049732.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-05T04:03:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6237#issuecomment-49732",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_049733.json:
```json
{
    "body": "Looks good.  Passes relevant tests.\n\nI did find something else weird, perhaps just my install is somehow corrupt... Did you try the original thing from the description as well?  It seems to be broken at the calculation of the discriminant both before and after the patch.  I get an error message about PariError(8).  However, this does not appear on sage.math, so I assume something weird happened in my local install.  But I thought I'd mention it in case you find it.\n\nAnyway, positive review!",
    "created_at": "2010-01-05T04:03:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6237#issuecomment-49733",
    "user": "https://github.com/kcrisman"
}
```

Looks good.  Passes relevant tests.

I did find something else weird, perhaps just my install is somehow corrupt... Did you try the original thing from the description as well?  It seems to be broken at the calculation of the discriminant both before and after the patch.  I get an error message about PariError(8).  However, this does not appear on sage.math, so I assume something weird happened in my local install.  But I thought I'd mention it in case you find it.

Anyway, positive review!



---

archive/issue_comments_049734.json:
```json
{
    "body": "Did you try the whole thing, including `pari('v')` and `pari('u')` ?\n\nIt seems to work for me.  Of course, if I had written the example I would have tried something like\n\n```\nsage: R.<u> = QQ[]\nsage: S.<v> = R[]\nsage: f = v^3 - u^7 + 2*u^3*v\nsage: f.discriminant()\n```\n\nThis does indeed fail with a `PariError(8)`.  And this is apparently documented in the docstring for `discriminant`.  It's a shame that it doesn't work out of the box.  In fact, I would even like something like the following to work:\n\n```\nsage: R.<u, v> = QQ[]\nsage: f = v^3 - u^7 + 2*u^3*v\nsage: f.discriminant(v)\n```\n\nAnyway, it's beyond the scope of this ticket.  I might open an enhancement ticket about it.",
    "created_at": "2010-01-05T06:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6237#issuecomment-49734",
    "user": "https://github.com/aghitza"
}
```

Did you try the whole thing, including `pari('v')` and `pari('u')` ?

It seems to work for me.  Of course, if I had written the example I would have tried something like

```
sage: R.<u> = QQ[]
sage: S.<v> = R[]
sage: f = v^3 - u^7 + 2*u^3*v
sage: f.discriminant()
```

This does indeed fail with a `PariError(8)`.  And this is apparently documented in the docstring for `discriminant`.  It's a shame that it doesn't work out of the box.  In fact, I would even like something like the following to work:

```
sage: R.<u, v> = QQ[]
sage: f = v^3 - u^7 + 2*u^3*v
sage: f.discriminant(v)
```

Anyway, it's beyond the scope of this ticket.  I might open an enhancement ticket about it.



---

archive/issue_comments_049735.json:
```json
{
    "body": "Replying to [comment:6 AlexGhitza]:\n> Did you try the whole thing, including `pari('v')` and `pari('u')` ?\nYes.  Again, oddly enough, the same thing did work when I tried it on sage.math, so it must be highly sensitive to something, though not sure what - maybe I had typed in something earlier that made it work/not work.\n> \n> It seems to work for me.  Of course, if I had written the example I would have tried something like\n> \n> \n> ```\n> sage: R.<u> = QQ[]\n> sage: S.<v> = R[]\n> sage: f = v^3 - u^7 + 2*u^3*v\n> sage: f.discriminant()\n> ```\n> \n> This does indeed fail with a `PariError(8)`.  And this is apparently documented in the docstring for `discriminant`.  \nHuh.  Well, glad to know it.\n> Anyway, it's beyond the scope of this ticket.  I might open an enhancement ticket about it.\n\nGo for it, though I won't be able to help on it.",
    "created_at": "2010-01-05T13:36:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6237#issuecomment-49735",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:6 AlexGhitza]:
> Did you try the whole thing, including `pari('v')` and `pari('u')` ?
Yes.  Again, oddly enough, the same thing did work when I tried it on sage.math, so it must be highly sensitive to something, though not sure what - maybe I had typed in something earlier that made it work/not work.
> 
> It seems to work for me.  Of course, if I had written the example I would have tried something like
> 
> 
> ```
> sage: R.<u> = QQ[]
> sage: S.<v> = R[]
> sage: f = v^3 - u^7 + 2*u^3*v
> sage: f.discriminant()
> ```
> 
> This does indeed fail with a `PariError(8)`.  And this is apparently documented in the docstring for `discriminant`.  
Huh.  Well, glad to know it.
> Anyway, it's beyond the scope of this ticket.  I might open an enhancement ticket about it.

Go for it, though I won't be able to help on it.



---

archive/issue_events_014614.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-13T08:29:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6237",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6237#event-14614"
}
```



---

archive/issue_comments_049736.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T08:29:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6237#issuecomment-49736",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
