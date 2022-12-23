# Issue 3081: [with patch; needs review] Added support for Kloosterman sums

archive/issues_003081.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  ncalexan\n\nThis (nearly trivial patch) adds support for exact and numerical evaluation of \"twisted\" Kloosterman sums. This generalizes Gauss sums, Salie sums and normal Kloosterman sums. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3081\n\n",
    "created_at": "2008-05-02T15:05:31Z",
    "labels": [
        "Cygwin",
        "major",
        "enhancement"
    ],
    "title": "[with patch; needs review] Added support for Kloosterman sums",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3081",
    "user": "kkilger"
}
```
Assignee: mabshoff

CC:  ncalexan

This (nearly trivial patch) adds support for exact and numerical evaluation of "twisted" Kloosterman sums. This generalizes Gauss sums, Salie sums and normal Kloosterman sums. 


Issue created by migration from https://trac.sagemath.org/ticket/3081





---

archive/issue_comments_021244.json:
```json
{
    "body": "Changing assignee from mabshoff to was.",
    "created_at": "2008-05-02T15:10:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3081#issuecomment-21244",
    "user": "mabshoff"
}
```

Changing assignee from mabshoff to was.



---

archive/issue_comments_021245.json:
```json
{
    "body": "Hi Kilian,\n\nAside from the fact that this is a number theory ticket everything looks good. Hopefully somebody will review this patch shortly.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-02T15:10:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3081#issuecomment-21245",
    "user": "mabshoff"
}
```

Hi Kilian,

Aside from the fact that this is a number theory ticket everything looks good. Hopefully somebody will review this patch shortly.

Cheers,

Michael



---

archive/issue_comments_021246.json:
```json
{
    "body": "Changing component from Cygwin to number theory.",
    "created_at": "2008-05-02T15:10:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3081#issuecomment-21246",
    "user": "mabshoff"
}
```

Changing component from Cygwin to number theory.



---

archive/issue_comments_021247.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-05-02T15:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3081#issuecomment-21247",
    "user": "kkilger"
}
```

Attachment



---

archive/issue_comments_021248.json:
```json
{
    "body": "This sounds extremely cool!\nWhat is based on? I can't get it to apply on either 3.0 or 3.0.1.alpha1.",
    "created_at": "2008-05-02T15:23:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3081#issuecomment-21248",
    "user": "wdj"
}
```

This sounds extremely cool!
What is based on? I can't get it to apply on either 3.0 or 3.0.1.alpha1.



---

archive/issue_comments_021249.json:
```json
{
    "body": "QUESTION:\n\nYou've rewritten some of the functions to be more general, e.g., this\n\n```\n707\t \t            z *= zeta \n708\t \t            g += phi(c)*z \n```\n\nbecomes this:\n\n```\n763\t                z = zeta ** (a*e + b*(e**(-1))) \n764\t                g += phi(self.__call__(c))*z        \n```\n\n\nWhat impact does this have on performance in the original case of computing Gauss\nsums?  Is it slower or faster or the same?\n\nAlso, why use \n\n```\nself.__call__(c)\n```\n\ninstead of \n\n```\nself(c)\n```\n\n?",
    "created_at": "2008-05-02T15:27:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3081#issuecomment-21249",
    "user": "was"
}
```

QUESTION:

You've rewritten some of the functions to be more general, e.g., this

```
707	 	            z *= zeta 
708	 	            g += phi(c)*z 
```

becomes this:

```
763	                z = zeta ** (a*e + b*(e**(-1))) 
764	                g += phi(self.__call__(c))*z        
```


What impact does this have on performance in the original case of computing Gauss
sums?  Is it slower or faster or the same?

Also, why use 

```
self.__call__(c)
```

instead of 

```
self(c)
```

?



---

archive/issue_comments_021250.json:
```json
{
    "body": "It computes the modular inverse every time. So it should be somewhat slower as before. I read that there is an ongoing discussion between code duplication and speed ...  \n\nI wanted to use this to introduce Poincare series in SAGE (and compute their Fourier coefficients) but this is far to slow. I am planning to reimplement the numerical stuff in C/Cython next week (or this weekend). \n\nQuestion: Why are Dirichlet characters in modular/dirichlet.py? Is it for historical reasons?\n\nRegards,\nKilian.",
    "created_at": "2008-05-02T15:50:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3081#issuecomment-21250",
    "user": "kkilger"
}
```

It computes the modular inverse every time. So it should be somewhat slower as before. I read that there is an ongoing discussion between code duplication and speed ...  

I wanted to use this to introduce Poincare series in SAGE (and compute their Fourier coefficients) but this is far to slow. I am planning to reimplement the numerical stuff in C/Cython next week (or this weekend). 

Question: Why are Dirichlet characters in modular/dirichlet.py? Is it for historical reasons?

Regards,
Kilian.



---

archive/issue_comments_021251.json:
```json
{
    "body": "P.S.: ... oh. I will change self.__call__(c) to self(c). I have to get used to python ;-).",
    "created_at": "2008-05-02T15:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3081#issuecomment-21251",
    "user": "kkilger"
}
```

P.S.: ... oh. I will change self.__call__(c) to self(c). I have to get used to python ;-).



---

archive/issue_comments_021252.json:
```json
{
    "body": "P.P.S: It should be based on 3.0 ...",
    "created_at": "2008-05-02T15:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3081#issuecomment-21252",
    "user": "kkilger"
}
```

P.P.S: It should be based on 3.0 ...



---

archive/issue_comments_021253.json:
```json
{
    "body": "> Question: Why are Dirichlet characters in modular/dirichlet.py? Is it for historical reasons?\n\nYep, Historical reasons.  Where would you want to put it.\n\n> It computes the modular inverse every time. So it should be somewhat \n> slower as before. I read that there is an ongoing discussion between \n> code duplication and speed ...\n\nWorrisome, but like you say below it is too slow in the first place. \n\n> I wanted to use this to introduce Poincare series in SAGE (and compute their \n> Fourier coefficients) but this is far to slow. I am planning to reimplement \n> the numerical stuff in C/Cython next week (or this weekend). \n\nExcellent!\n\n -- William",
    "created_at": "2008-05-02T16:08:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3081#issuecomment-21253",
    "user": "was"
}
```

> Question: Why are Dirichlet characters in modular/dirichlet.py? Is it for historical reasons?

Yep, Historical reasons.  Where would you want to put it.

> It computes the modular inverse every time. So it should be somewhat 
> slower as before. I read that there is an ongoing discussion between 
> code duplication and speed ...

Worrisome, but like you say below it is too slow in the first place. 

> I wanted to use this to introduce Poincare series in SAGE (and compute their 
> Fourier coefficients) but this is far to slow. I am planning to reimplement 
> the numerical stuff in C/Cython next week (or this weekend). 

Excellent!

 -- William



---

archive/issue_comments_021254.json:
```json
{
    "body": "> Yep, Historical reasons. Where would you want to put it.\n\nAre there some other character groups implemented? Perhaps it should go to the dual groups?\n\nAnother question:\n\nIf I compute for example the Kloosterman sum K(2,4,13) in Magma it returns:\n2*zeta_13^10 + 2*zeta_13^9 + 2*zeta_13^7 + 2*zeta_13^6 + 2*zeta_13^4 + 2*zeta_13^3\n\nIf I compute it with SAGE it returns:\n2*zeta156^40 - 2*zeta156^34 + 2*zeta156^28 - 2*zeta156^24 + 2*zeta156^18 - 2*zeta156^14 - 2*zeta156^12 + 2*zeta156^8 - 2*zeta156^2 - 2\n\nThis is the same number but it is much more reduced in MAGMA. The corresponding MAGMA code is:\n\n> Kloosterman := func< u, v, n |\n>     &+[z^(IntegerRing() ! (u*x+v*x^-1)) : x in F | IsUnit(x) ]\n>         where z is RootOfUnity(n, CyclotomicField(n))\n>         where F is ResidueClassRing(n) >;\n\nKilian.",
    "created_at": "2008-05-02T17:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3081#issuecomment-21254",
    "user": "kkilger"
}
```

> Yep, Historical reasons. Where would you want to put it.

Are there some other character groups implemented? Perhaps it should go to the dual groups?

Another question:

If I compute for example the Kloosterman sum K(2,4,13) in Magma it returns:
2*zeta_13^10 + 2*zeta_13^9 + 2*zeta_13^7 + 2*zeta_13^6 + 2*zeta_13^4 + 2*zeta_13^3

If I compute it with SAGE it returns:
2*zeta156^40 - 2*zeta156^34 + 2*zeta156^28 - 2*zeta156^24 + 2*zeta156^18 - 2*zeta156^14 - 2*zeta156^12 + 2*zeta156^8 - 2*zeta156^2 - 2

This is the same number but it is much more reduced in MAGMA. The corresponding MAGMA code is:

> Kloosterman := func< u, v, n |
>     &+[z^(IntegerRing() ! (u*x+v*x^-1)) : x in F | IsUnit(x) ]
>         where z is RootOfUnity(n, CyclotomicField(n))
>         where F is ResidueClassRing(n) >;

Kilian.



---

archive/issue_comments_021255.json:
```json
{
    "body": "Again ... I forgot the code block\n\nMagma-Number:\n\n\n```\n2*zeta_13^10 + 2*zeta_13^9 + 2*zeta_13^7 + 2*zeta_13^6 + 2*zeta_13^4 + 2*zeta_13^3\n```\n\n\nSAGE-Number:\n\n```\n2*zeta156^40 - 2*zeta156^34 + 2*zeta156^28 - 2*zeta156^24 + 2*zeta156^18 - 2*zeta156^14 - 2*zeta156^12 + 2*zeta156^8 - 2*zeta156^2 - 2\n```\n\n\nMagma-Code:\n\n```\n>  Kloosterman := func< u, v, n |\n>      &+[z^(IntegerRing() ! (u*x+v*x^-1)) : x in F | IsUnit(x) ]\n>          where z is RootOfUnity(n, CyclotomicField(n))\n>          where F is ResidueClassRing(n) >;\n```\n",
    "created_at": "2008-05-02T17:28:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3081#issuecomment-21255",
    "user": "kkilger"
}
```

Again ... I forgot the code block

Magma-Number:


```
2*zeta_13^10 + 2*zeta_13^9 + 2*zeta_13^7 + 2*zeta_13^6 + 2*zeta_13^4 + 2*zeta_13^3
```


SAGE-Number:

```
2*zeta156^40 - 2*zeta156^34 + 2*zeta156^28 - 2*zeta156^24 + 2*zeta156^18 - 2*zeta156^14 - 2*zeta156^12 + 2*zeta156^8 - 2*zeta156^2 - 2
```


Magma-Code:

```
>  Kloosterman := func< u, v, n |
>      &+[z^(IntegerRing() ! (u*x+v*x^-1)) : x in F | IsUnit(x) ]
>          where z is RootOfUnity(n, CyclotomicField(n))
>          where F is ResidueClassRing(n) >;
```




---

archive/issue_comments_021256.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_craigcitro\".",
    "created_at": "2008-06-15T21:40:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3081#issuecomment-21256",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_craigcitro".



---

archive/issue_comments_021257.json:
```json
{
    "body": "Nick,\n\nanything going on here?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-25T00:18:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3081#issuecomment-21257",
    "user": "mabshoff"
}
```

Nick,

anything going on here?

Cheers,

Michael



---

archive/issue_comments_021258.json:
```json
{
    "body": "From Nick:\n\n```\nI seem to remember thinking this code was mildly flawed (easily fixed) and not fast.  But please pass it on to someone more tuned in.\n```\n",
    "created_at": "2008-10-30T18:07:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3081#issuecomment-21258",
    "user": "was"
}
```

From Nick:

```
I seem to remember thinking this code was mildly flawed (easily fixed) and not fast.  But please pass it on to someone more tuned in.
```




---

archive/issue_comments_021259.json:
```json
{
    "body": "REFEREE REPORT:\n\nThis patch needs work.  Just totally delete the first part of the patch that\nreplaces lines 636-652 by nothing and calls kloosterman_sum, since kloosterman_sum is much slower.  Just leave the code like it used to be.\n\nOtherwise, i think the code is good to have included in sage.    In particular, the issue the author raises about the representation of a certain output and a root of unity is interesting, but not something to stop this patch from going in.\n\nSo I think with some very obvious simple work, this can easily be included.  Just delete the part that will slow down the gauss_sum.",
    "created_at": "2008-11-28T04:39:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3081#issuecomment-21259",
    "user": "was"
}
```

REFEREE REPORT:

This patch needs work.  Just totally delete the first part of the patch that
replaces lines 636-652 by nothing and calls kloosterman_sum, since kloosterman_sum is much slower.  Just leave the code like it used to be.

Otherwise, i think the code is good to have included in sage.    In particular, the issue the author raises about the representation of a certain output and a root of unity is interesting, but not something to stop this patch from going in.

So I think with some very obvious simple work, this can easily be included.  Just delete the part that will slow down the gauss_sum.



---

archive/issue_comments_021260.json:
```json
{
    "body": "Attachment\n\nRepaired patch",
    "created_at": "2009-04-11T14:22:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3081#issuecomment-21260",
    "user": "kkilger"
}
```

Attachment

Repaired patch



---

archive/issue_comments_021261.json:
```json
{
    "body": "Sorry ... a bit late but what comes late is better than everything what comes never :-)",
    "created_at": "2009-04-11T14:25:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3081#issuecomment-21261",
    "user": "kkilger"
}
```

Sorry ... a bit late but what comes late is better than everything what comes never :-)



---

archive/issue_comments_021262.json:
```json
{
    "body": "Just changing the title so this gets noticed.",
    "created_at": "2009-04-11T15:55:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3081#issuecomment-21262",
    "user": "craigcitro"
}
```

Just changing the title so this gets noticed.



---

archive/issue_comments_021263.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-12T20:53:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3081#issuecomment-21263",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021264.json:
```json
{
    "body": "Merged kloosterman.patch in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-12T20:53:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3081#issuecomment-21264",
    "user": "mabshoff"
}
```

Merged kloosterman.patch in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_comments_021265.json:
```json
{
    "body": "I just notices that this patch uses tabs instead of spaces. In Sage we do not use tabs but spaces, so please adjust your editor.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T08:20:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3081#issuecomment-21265",
    "user": "mabshoff"
}
```

I just notices that this patch uses tabs instead of spaces. In Sage we do not use tabs but spaces, so please adjust your editor.

Cheers,

Michael
