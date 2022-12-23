# Issue 169: slice assignment not implemented for PARI C library interface

archive/issues_000169.json:
```json
{
    "body": "Assignee: was\n\n\n```\nFrom \"Luislang\" \n\nFollowing session says it all.\n \n--------------------------------------------------------\n--------------------------------------------------------\n \nsage: s=pari.vector(2,[0,0])\nsage: s[:1]\n _2 = [0]\nsage: s[:1]=[1]\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<console>\", line 1, in ?\n  File \"gen.pyx\", line 417, in gen.gen.__setitem__\nIndexError: index (slice(0, 1, None)) must be between 0 and 1\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/169\n\n",
    "created_at": "2006-11-15T15:44:35Z",
    "labels": [
        "interfaces",
        "minor",
        "enhancement"
    ],
    "title": "slice assignment not implemented for PARI C library interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/169",
    "user": "was"
}
```
Assignee: was


```
From "Luislang" 

Following session says it all.
 
--------------------------------------------------------
--------------------------------------------------------
 
sage: s=pari.vector(2,[0,0])
sage: s[:1]
 _2 = [0]
sage: s[:1]=[1]
------------------------------------------------------------
Traceback (most recent call last):
  File "<console>", line 1, in ?
  File "gen.pyx", line 417, in gen.gen.__setitem__
IndexError: index (slice(0, 1, None)) must be between 0 and 1
```


Issue created by migration from https://trac.sagemath.org/ticket/169





---

archive/issue_comments_000754.json:
```json
{
    "body": "\n```\n \nI'm not understanding your question. Lists are mutable:\nsage: L = [0,0]\nsage: L[:1] = [1]\nsage: L\n [1, 0]\npari vectors apparently are not. Are you saying they should be?\nOr is it that you don't like the error message?\n \nThe problem is simply that I only implemented __setitem__ in\nthe case of an integer input.  He wants a more general __setitem__\nto be implemented also for PARI vectors, which are mutable:\nsage: s=pari.vector(2,[0,0])\nsage: s[0] = 5\nsage: s\n[5, 0]\n \nI think the problem is that I didn't realize \"s[slice] = blah\"\nwas a standard Python idiom, so I didn't implement support for\nit for the PARI C-library interface.\n \n }}}",
    "created_at": "2006-11-15T15:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-754",
    "user": "was"
}
```


```
 
I'm not understanding your question. Lists are mutable:
sage: L = [0,0]
sage: L[:1] = [1]
sage: L
 [1, 0]
pari vectors apparently are not. Are you saying they should be?
Or is it that you don't like the error message?
 
The problem is simply that I only implemented __setitem__ in
the case of an integer input.  He wants a more general __setitem__
to be implemented also for PARI vectors, which are mutable:
sage: s=pari.vector(2,[0,0])
sage: s[0] = 5
sage: s
[5, 0]
 
I think the problem is that I didn't realize "s[slice] = blah"
was a standard Python idiom, so I didn't implement support for
it for the PARI C-library interface.
 
 }}}



---

archive/issue_comments_000755.json:
```json
{
    "body": "So William, would still consider this worth fixing? Sage 2.8.2-rc3 still has this issue roughly 18months later :(\n\n```\nsage: s=pari.vector(2,[0,0])\nsage: sage: s[:1]\n[0]\nsage: s[:1]=[1]\n---------------------------------------------------------------------------\n<type 'exceptions.IndexError'>            Traceback (most recent call last)\n\n/tmp/Work2/sage-2.8.1/sage-2.8.2.rc3/<ipython console> in <module>()\n\n/tmp/Work2/sage-2.8.1/sage-2.8.2.rc3/gen.pyx in gen.gen.__setitem__()\n\n<type 'exceptions.IndexError'>: index (slice(None, 1, None)) must be between 0 and 1\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-08-23T12:34:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-755",
    "user": "mabshoff"
}
```

So William, would still consider this worth fixing? Sage 2.8.2-rc3 still has this issue roughly 18months later :(

```
sage: s=pari.vector(2,[0,0])
sage: sage: s[:1]
[0]
sage: s[:1]=[1]
---------------------------------------------------------------------------
<type 'exceptions.IndexError'>            Traceback (most recent call last)

/tmp/Work2/sage-2.8.1/sage-2.8.2.rc3/<ipython console> in <module>()

/tmp/Work2/sage-2.8.1/sage-2.8.2.rc3/gen.pyx in gen.gen.__setitem__()

<type 'exceptions.IndexError'>: index (slice(None, 1, None)) must be between 0 and 1
```


Cheers,

Michael



---

archive/issue_comments_000756.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-14T05:27:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-756",
    "user": "craigcitro"
}
```

Resolution: fixed



---

archive/issue_comments_000757.json:
```json
{
    "body": "Actually, this is already fixed:\n\n\n```\nsage: s=pari.vector(2,[0,0])\nsage: s[:1]\n[0]\nsage: s[:1]=[1]\nTrue\n```\n\n\nThe `__getslice__` function is also already doctested, so no need to add more. I'm closing this as fixed.",
    "created_at": "2008-11-14T05:27:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-757",
    "user": "craigcitro"
}
```

Actually, this is already fixed:


```
sage: s=pari.vector(2,[0,0])
sage: s[:1]
[0]
sage: s[:1]=[1]
True
```


The `__getslice__` function is also already doctested, so no need to add more. I'm closing this as fixed.



---

archive/issue_comments_000758.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-11-14T05:33:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-758",
    "user": "craigcitro"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_000759.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-11-14T05:33:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-759",
    "user": "craigcitro"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_000760.json:
```json
{
    "body": "Sorry, I can't read. I didn't notice that it was `__setslice__` that we were talking about.",
    "created_at": "2008-11-14T05:33:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-760",
    "user": "craigcitro"
}
```

Sorry, I can't read. I didn't notice that it was `__setslice__` that we were talking about.



---

archive/issue_comments_000761.json:
```json
{
    "body": "Changing status from reopened to new.",
    "created_at": "2008-11-14T05:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-761",
    "user": "mabshoff"
}
```

Changing status from reopened to new.



---

archive/issue_comments_000762.json:
```json
{
    "body": "Changing assignee from was to craigcitro.",
    "created_at": "2008-11-14T05:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-762",
    "user": "mabshoff"
}
```

Changing assignee from was to craigcitro.



---

archive/issue_comments_000763.json:
```json
{
    "body": "Indeed:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.rc1$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| Sage Version 3.2.rc0, Release Date: 2008-11-10                     |\n| Type notebook() for the GUI, and license() for information.        |\nsage: s=pari.vector(2,[0,0])\nsage: s[:1]\n[0]\nsage: s[:1]=[1]\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/scratch/mabshoff/release-cycle/sage-3.2.rc1/<ipython console> in <module>()\n\n/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen.gen.__setitem__ (sage/libs/pari/gen.c:6394)()\n\nTypeError: int() argument must be a string or a number, not 'slice'\nsage: \n```\n",
    "created_at": "2008-11-14T05:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-763",
    "user": "mabshoff"
}
```

Indeed:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.rc1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.2.rc0, Release Date: 2008-11-10                     |
| Type notebook() for the GUI, and license() for information.        |
sage: s=pari.vector(2,[0,0])
sage: s[:1]
[0]
sage: s[:1]=[1]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/scratch/mabshoff/release-cycle/sage-3.2.rc1/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen.gen.__setitem__ (sage/libs/pari/gen.c:6394)()

TypeError: int() argument must be a string or a number, not 'slice'
sage: 
```




---

archive/issue_comments_000764.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-14T06:42:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-764",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_000765.json:
```json
{
    "body": "Okay, in exchange for being an idiot at reading, I went ahead and fixed this. Attached patch should do the trick.",
    "created_at": "2008-11-14T06:42:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-765",
    "user": "craigcitro"
}
```

Okay, in exchange for being an idiot at reading, I went ahead and fixed this. Attached patch should do the trick.



---

archive/issue_comments_000766.json:
```json
{
    "body": "First, __setslice__ is deprecated: http://www.python.org/doc/2.5.2/ref/sequence-methods.html\n\nInstead, check for a slice object in the __setitem__ function.\n\nAlso, the slice could have a step as well:\n\n\n```\nsage: a=[1,2,3,4,5,6,7,8,9]\nsage: a[2:8:2]\n[3, 5, 7]\n```\n",
    "created_at": "2008-11-14T15:24:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-766",
    "user": "jason"
}
```

First, __setslice__ is deprecated: http://www.python.org/doc/2.5.2/ref/sequence-methods.html

Instead, check for a slice object in the __setitem__ function.

Also, the slice could have a step as well:


```
sage: a=[1,2,3,4,5,6,7,8,9]
sage: a[2:8:2]
[3, 5, 7]
```




---

archive/issue_comments_000767.json:
```json
{
    "body": "I should add: Thanks so much for doing this long-standing feature request!  You rock!",
    "created_at": "2008-11-14T15:26:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-767",
    "user": "jason"
}
```

I should add: Thanks so much for doing this long-standing feature request!  You rock!



---

archive/issue_comments_000768.json:
```json
{
    "body": "Ah, cool. I had no idea that `__setslice__` was deprecated. I'll clean this up today or tomorrow.",
    "created_at": "2008-11-14T17:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-768",
    "user": "craigcitro"
}
```

Ah, cool. I had no idea that `__setslice__` was deprecated. I'll clean this up today or tomorrow.



---

archive/issue_comments_000769.json:
```json
{
    "body": "new and improved patch",
    "created_at": "2008-11-19T11:22:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-769",
    "user": "craigcitro"
}
```

new and improved patch



---

archive/issue_comments_000770.json:
```json
{
    "body": "Attachment\n\nNew patch, with lots of added functionality. (I read what all you can do with the `step` parameter to slice.",
    "created_at": "2008-11-19T11:23:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-770",
    "user": "craigcitro"
}
```

Attachment

New patch, with lots of added functionality. (I read what all you can do with the `step` parameter to slice.



---

archive/issue_comments_000771.json:
```json
{
    "body": "Wow, that was a lot of work. Looks good to me.",
    "created_at": "2008-11-21T00:03:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-771",
    "user": "robertwb"
}
```

Wow, that was a lot of work. Looks good to me.



---

archive/issue_comments_000772.json:
```json
{
    "body": "Wow, robertwb is right; that was a lot of work.\n\nThanks for the generic normalize slice function.  Eventually, it would be great to move that to a more general utility function, maybe somewhere in sage/misc or something.  I can see it being very, very useful for other objects that need to implement slice notation (for example, matrices and vectors of other types).",
    "created_at": "2008-11-21T02:48:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-772",
    "user": "jason"
}
```

Wow, robertwb is right; that was a lot of work.

Thanks for the generic normalize slice function.  Eventually, it would be great to move that to a more general utility function, maybe somewhere in sage/misc or something.  I can see it being very, very useful for other objects that need to implement slice notation (for example, matrices and vectors of other types).



---

archive/issue_comments_000773.json:
```json
{
    "body": "Oops:\n\n```\n        sage -t -long devel/sage/sage/tests/book_stein_modform.py # 7 doctests failed\n        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_tate_curve.py # 47 doctests failed\n        sage -t -long devel/sage/sage/rings/number_field/number_field.py # 3 doctests failed\n        sage -t -long devel/sage/sage/rings/integer.pyx # 1 doctests failed\n        sage -t -long devel/sage/sage/modular/modform/tests.py # 2 doctests failed\n        sage -t -long devel/sage/sage/modular/modform/submodule.py # 1 doctests failed\n        sage -t -long devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 4 doctests failed\n        sage -t -long devel/sage/sage/modular/modform/hecke_operator_on_qexp.py # 11 doctests failed\n        sage -t -long devel/sage/sage/modular/modform/half_integral.py # 5 doctests failed\n        sage -t -long devel/sage/sage/modular/modform/space.py # 61 doctests failed\n        sage -t -long devel/sage/sage/modular/modform/ambient_g1.py # 1 doctests failed\n        sage -t -long devel/sage/sage/modular/modform/cuspidal_submodule.py # 6 doctests failed\n        sage -t -long devel/sage/sage/modular/modform/eisenstein_submodule.py # 12 doctests failed\n        sage -t -long devel/sage/sage/modular/modform/constructor.py # 6 doctests failed\n        sage -t -long devel/sage/sage/modular/modform/ambient_R.py # 1 doctests failed\n        sage -t -long devel/sage/sage/modular/modform/ambient.py # 12 doctests failed\n        sage -t -long devel/sage/sage/modular/modform/element.py # 49 doctests failed\n        sage -t -long devel/sage/sage/modular/hecke/module.py # 2 doctests failed\n        sage -t -long devel/sage/sage/modular/abvar/constructor.py # 2 doctests failed\n        sage -t -long devel/sage/sage/modular/abvar/abvar_newform.py # 11 doctests failed\n        sage -t -long devel/sage/sage/modular/abvar/morphism.py # 4 doctests failed\n        sage -t -long devel/sage/sage/modular/abvar/abvar_ambient_jacobian.py # 3 doctests failed\n        sage -t -long devel/sage/sage/modular/abvar/homspace.py # 32 doctests failed\n        sage -t -long devel/sage/sage/modular/abvar/abvar.py # 10 doctests failed\n        sage -t -long devel/sage/sage/libs/pari/gen.pyx # 1 doctests failed\n        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # 8 doctests failed\n```\n\nIs there a dependency I missed?\n\nCheers,\n\nMichael",
    "created_at": "2008-11-21T05:19:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-773",
    "user": "mabshoff"
}
```

Oops:

```
        sage -t -long devel/sage/sage/tests/book_stein_modform.py # 7 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_tate_curve.py # 47 doctests failed
        sage -t -long devel/sage/sage/rings/number_field/number_field.py # 3 doctests failed
        sage -t -long devel/sage/sage/rings/integer.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/modular/modform/tests.py # 2 doctests failed
        sage -t -long devel/sage/sage/modular/modform/submodule.py # 1 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 4 doctests failed
        sage -t -long devel/sage/sage/modular/modform/hecke_operator_on_qexp.py # 11 doctests failed
        sage -t -long devel/sage/sage/modular/modform/half_integral.py # 5 doctests failed
        sage -t -long devel/sage/sage/modular/modform/space.py # 61 doctests failed
        sage -t -long devel/sage/sage/modular/modform/ambient_g1.py # 1 doctests failed
        sage -t -long devel/sage/sage/modular/modform/cuspidal_submodule.py # 6 doctests failed
        sage -t -long devel/sage/sage/modular/modform/eisenstein_submodule.py # 12 doctests failed
        sage -t -long devel/sage/sage/modular/modform/constructor.py # 6 doctests failed
        sage -t -long devel/sage/sage/modular/modform/ambient_R.py # 1 doctests failed
        sage -t -long devel/sage/sage/modular/modform/ambient.py # 12 doctests failed
        sage -t -long devel/sage/sage/modular/modform/element.py # 49 doctests failed
        sage -t -long devel/sage/sage/modular/hecke/module.py # 2 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/constructor.py # 2 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/abvar_newform.py # 11 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/morphism.py # 4 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/abvar_ambient_jacobian.py # 3 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/homspace.py # 32 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/abvar.py # 10 doctests failed
        sage -t -long devel/sage/sage/libs/pari/gen.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # 8 doctests failed
```

Is there a dependency I missed?

Cheers,

Michael



---

archive/issue_comments_000774.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-11-21T05:32:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-774",
    "user": "craigcitro"
}
```

Attachment



---

archive/issue_comments_000775.json:
```json
{
    "body": "Yep, I forgot to handle the case of lists of length 0. Oops.\n\nAttached patch should fix everything.",
    "created_at": "2008-11-21T05:32:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-775",
    "user": "craigcitro"
}
```

Yep, I forgot to handle the case of lists of length 0. Oops.

Attached patch should fix everything.



---

archive/issue_comments_000776.json:
```json
{
    "body": "+1 on trac-169-pt2.patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-21T05:34:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-776",
    "user": "mabshoff"
}
```

+1 on trac-169-pt2.patch.

Cheers,

Michael



---

archive/issue_comments_000777.json:
```json
{
    "body": "I ran doctests on a couple of files as well as trying this out and looking at the code, but I guess there's nothing like a full sage -testall",
    "created_at": "2008-11-21T05:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-777",
    "user": "robertwb"
}
```

I ran doctests on a couple of files as well as trying this out and looking at the code, but I guess there's nothing like a full sage -testall



---

archive/issue_comments_000778.json:
```json
{
    "body": "Mhh, odd things happen on 64 bit I assume:\n\n```\nsage -t -long devel/sage/sage/libs/pari/gen.pyx             \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/libs/pari/gen.pyx\", line 2714:\n    sage: pari(2**50).length()\nExpected:\n    4             \nGot:\n    1\n**********************************************************************\n```\n\nI would guess this is a 32 vs. 64 bit issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-21T06:40:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-778",
    "user": "mabshoff"
}
```

Mhh, odd things happen on 64 bit I assume:

```
sage -t -long devel/sage/sage/libs/pari/gen.pyx             
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/libs/pari/gen.pyx", line 2714:
    sage: pari(2**50).length()
Expected:
    4             
Got:
    1
**********************************************************************
```

I would guess this is a 32 vs. 64 bit issue.

Cheers,

Michael



---

archive/issue_comments_000779.json:
```json
{
    "body": "\n```\n[10:22pm] mabshoff: craigcitro: One more think for #169 - looks like 32 vs. 64 bit maybe?\n[10:50pm] craigcitro: mabshoff: oops, i can't count.\n[10:50pm] craigcitro: i multiplied by 2 when i should have divided ...\n[10:50pm] craigcitro: the 4 should really be a 1\n[10:50pm] mabshoff: Don't tell me this fails on your box, too \n[10:51pm] mabshoff:\n[10:51pm] craigcitro: (it's already got cases for 32 vs 64 bit)\n[10:51pm] craigcitro: grin\n[10:51pm] mabshoff:\n[10:51pm] craigcitro: yeah, i was just being dumb.\n[10:51pm] mabshoff: Don't divide - craigcitro inside?\n[10:51pm] craigcitro: hahahahaha\n[10:51pm] mabshoff: Couldn't resist \n[10:51pm] craigcitro: should i make a new patch? or do you want to edit the patch?\n[10:51pm] mabshoff: I will edit the patch\n[10:51pm] craigcitro: k\n```\n",
    "created_at": "2008-11-21T06:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-779",
    "user": "mabshoff"
}
```


```
[10:22pm] mabshoff: craigcitro: One more think for #169 - looks like 32 vs. 64 bit maybe?
[10:50pm] craigcitro: mabshoff: oops, i can't count.
[10:50pm] craigcitro: i multiplied by 2 when i should have divided ...
[10:50pm] craigcitro: the 4 should really be a 1
[10:50pm] mabshoff: Don't tell me this fails on your box, too 
[10:51pm] mabshoff:
[10:51pm] craigcitro: (it's already got cases for 32 vs 64 bit)
[10:51pm] craigcitro: grin
[10:51pm] mabshoff:
[10:51pm] craigcitro: yeah, i was just being dumb.
[10:51pm] mabshoff: Don't divide - craigcitro inside?
[10:51pm] craigcitro: hahahahaha
[10:51pm] mabshoff: Couldn't resist 
[10:51pm] craigcitro: should i make a new patch? or do you want to edit the patch?
[10:51pm] mabshoff: I will edit the patch
[10:51pm] craigcitro: k
```




---

archive/issue_comments_000780.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-21T07:27:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-780",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_000781.json:
```json
{
    "body": "Merged both patches in Sage 3.2.1.alpha0",
    "created_at": "2008-11-21T07:27:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/169#issuecomment-781",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.2.1.alpha0
