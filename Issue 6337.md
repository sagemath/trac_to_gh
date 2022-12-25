# Issue 6337: bug in jorder form over symbolic ring

archive/issues_006337.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: version()\n'Sage Version 4.0.1, Release Date: 2009-06-06'\nsage: var('a d')\n(a, d)\nsage: A = matrix([[a,0],[1,d]])\nsage: A.eigenvalues()\n[d, a]\nsage: A.jordan_form()\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call\nlast)\n\n/home/bo198214/.sage/temp/darkdepth/6404/\n_home_bo198214__sage_init_sage_0.py in <module>()\n\n/usr/src/sage-4.0.1-linux-Debian_GNU_Linux_5.0_lenny-sse2-x86_64-Linux/\nlocal/lib/python2.5/site-packages/sage/matrix/matrix2.so in\nsage.matrix.matrix2.Matrix.jordan_form (sage/matrix/matrix2.c:27915)()\n\nRuntimeError: Some eigenvalue does not exist in Symbolic Ring.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6337\n\n",
    "created_at": "2009-06-16T16:58:27Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.9",
    "title": "bug in jorder form over symbolic ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6337",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
sage: version()
'Sage Version 4.0.1, Release Date: 2009-06-06'
sage: var('a d')
(a, d)
sage: A = matrix([[a,0],[1,d]])
sage: A.eigenvalues()
[d, a]
sage: A.jordan_form()
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call
last)

/home/bo198214/.sage/temp/darkdepth/6404/
_home_bo198214__sage_init_sage_0.py in <module>()

/usr/src/sage-4.0.1-linux-Debian_GNU_Linux_5.0_lenny-sse2-x86_64-Linux/
local/lib/python2.5/site-packages/sage/matrix/matrix2.so in
sage.matrix.matrix2.Matrix.jordan_form (sage/matrix/matrix2.c:27915)()

RuntimeError: Some eigenvalue does not exist in Symbolic Ring.
```


Issue created by migration from https://trac.sagemath.org/ticket/6337





---

archive/issue_comments_050478.json:
```json
{
    "body": "Things are failing early on, with the roots command.  E.g.:\n\nsage: var('a, d')\nsage: ((d - x)*(a - x)).roots()\n[(x, 1)]\n\nWhile the eigenvalues method works, it doesn't compute multiplicities, so I am not sure what the easiest fix is.",
    "created_at": "2009-06-16T17:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6337#issuecomment-50478",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Things are failing early on, with the roots command.  E.g.:

sage: var('a, d')
sage: ((d - x)*(a - x)).roots()
[(x, 1)]

While the eigenvalues method works, it doesn't compute multiplicities, so I am not sure what the easiest fix is.



---

archive/issue_comments_050479.json:
```json
{
    "body": "This one looks different now:\n\n```\nsage: sage: var('a d')\n(a, d)\nsage: sage: A = matrix([[a,0],[1,d]])\nsage: sage: A.eigenvalues()\n[d, a]\nsage: sage: A.jordan_form()\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n<ipython-input-8-708dc91119f4> in <module>()\n----> 1 A.jordan_form()\n\n/home/darij/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/matrix/matrix2.so in sage.matrix.matrix2.Matrix.jordan_form (sage/matrix/matrix2.c:44267)()\n\nValueError: Jordan normal form not implemented over inexact rings.\n```\n\n\nI agree that the symbolic ring is inexact, and that Jordan normal form requires exactness...",
    "created_at": "2013-06-22T23:04:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6337#issuecomment-50479",
    "user": "https://github.com/darijgr"
}
```

This one looks different now:

```
sage: sage: var('a d')
(a, d)
sage: sage: A = matrix([[a,0],[1,d]])
sage: sage: A.eigenvalues()
[d, a]
sage: sage: A.jordan_form()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-8-708dc91119f4> in <module>()
----> 1 A.jordan_form()

/home/darij/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/matrix/matrix2.so in sage.matrix.matrix2.Matrix.jordan_form (sage/matrix/matrix2.c:44267)()

ValueError: Jordan normal form not implemented over inexact rings.
```


I agree that the symbolic ring is inexact, and that Jordan normal form requires exactness...



---

archive/issue_events_014895.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6337#event-14895"
}
```



---

archive/issue_events_014896.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6337#event-14896"
}
```



---

archive/issue_events_014897.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6337#event-14897"
}
```



---

archive/issue_events_014898.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6337#event-14898"
}
```



---

archive/issue_events_014899.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6337#event-14899"
}
```



---

archive/issue_events_014900.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6337#event-14900"
}
```



---

archive/issue_events_014901.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6337#event-14901"
}
```



---

archive/issue_comments_050480.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-07-31T13:51:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6337#issuecomment-50480",
    "user": "https://github.com/rwst"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050481.json:
```json
{
    "body": "Replying to [comment:3 darij]:\n> I agree that the symbolic ring is inexact, and that Jordan normal form requires exactness...\nSo this would be invalid now?",
    "created_at": "2015-07-31T13:51:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6337#issuecomment-50481",
    "user": "https://github.com/rwst"
}
```

Replying to [comment:3 darij]:
> I agree that the symbolic ring is inexact, and that Jordan normal form requires exactness...
So this would be invalid now?



---

archive/issue_events_014902.json:
```json
{
    "actor": "https://github.com/rwst",
    "created_at": "2015-07-31T13:51:37Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6337#event-14902"
}
```



---

archive/issue_events_014903.json:
```json
{
    "actor": "https://github.com/rwst",
    "created_at": "2015-07-31T13:51:37Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6337#event-14903"
}
```



---

archive/issue_comments_050482.json:
```json
{
    "body": "I think someone who understands symbolic better should weigh in.",
    "created_at": "2015-07-31T13:54:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6337#issuecomment-50482",
    "user": "https://github.com/darijgr"
}
```

I think someone who understands symbolic better should weigh in.



---

archive/issue_comments_050483.json:
```json
{
    "body": "Replying to [comment:1 mhampton]:\n> Things are failing early on, with the roots command.  E.g.:\n> \n> sage: var('a, d')\n> sage: ((d - x)*(a - x)).roots()\n> [(x, 1)]\n\nWhat is failing here? In order to get the expected answer you need of course to specify the variable\n\n```\nsage: var('a d')\n(a, d)\nsage:  ((d - x)*(a - x)).roots()\n[(x, 1)]\nsage:  ((d - x)*(a - x)).roots(x)\n[(d, 1), (a, 1)]\nsage:  ((d - x)**2).roots()\n[(x, 2)]\n```\n",
    "created_at": "2015-08-09T14:20:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6337#issuecomment-50483",
    "user": "https://github.com/videlec"
}
```

Replying to [comment:1 mhampton]:
> Things are failing early on, with the roots command.  E.g.:
> 
> sage: var('a, d')
> sage: ((d - x)*(a - x)).roots()
> [(x, 1)]

What is failing here? In order to get the expected answer you need of course to specify the variable

```
sage: var('a d')
(a, d)
sage:  ((d - x)*(a - x)).roots()
[(x, 1)]
sage:  ((d - x)*(a - x)).roots(x)
[(d, 1), (a, 1)]
sage:  ((d - x)**2).roots()
[(x, 2)]
```




---

archive/issue_events_014904.json:
```json
{
    "actor": "https://github.com/pjbruin",
    "created_at": "2015-08-31T18:13:28Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6337#event-14904"
}
```



---

archive/issue_events_014905.json:
```json
{
    "actor": "https://github.com/pjbruin",
    "created_at": "2015-08-31T18:13:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "milestone": "sage-6.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6337#event-14905"
}
```



---

archive/issue_comments_050484.json:
```json
{
    "body": "Here is a straightforward implementation of `jordan_form()` for symbolic matrices using Maxima.  Even though the \"symbolic ring\" is considered to be inexact, it still seems useful to have a working `jordan_form()` method for it.",
    "created_at": "2015-08-31T18:13:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6337#issuecomment-50484",
    "user": "https://github.com/pjbruin"
}
```

Here is a straightforward implementation of `jordan_form()` for symbolic matrices using Maxima.  Even though the "symbolic ring" is considered to be inexact, it still seems useful to have a working `jordan_form()` method for it.



---

archive/issue_comments_050485.json:
```json
{
    "body": "This looks fine to me.\n\n\nReplying to [comment:8 rws]:\n> Replying to [comment:3 darij]:\n> > I agree that the symbolic ring is inexact, and that Jordan normal form requires exactness...\n> So this would be invalid now?\nThe Jordan normal form does not require more \"exactness\" from the ring as do the eigenvalues which are already implemented for symbolic matrices (calling maxima). Hence I see no point in discussing whether or not we should offer a jordan_form method for symbolic matrices, it seems natural to do it as what is proposed here.\n\nJust one thing: to be consistent with what is returned over other coefficient domains, the Jordan form should display the subdivision of the block matrix.\n  {{{#!python\n  sage: a = matrix(QQ,3,[1,0,1,0,2,0,0,0,1])\n  sage: a.jordan_form()\n  [2|0 0]\n  [-+---]\n  [0|1 1]\n  [0|0 1]\n  }}}",
    "created_at": "2015-09-15T16:09:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6337#issuecomment-50485",
    "user": "https://github.com/ClementPernet"
}
```

This looks fine to me.


Replying to [comment:8 rws]:
> Replying to [comment:3 darij]:
> > I agree that the symbolic ring is inexact, and that Jordan normal form requires exactness...
> So this would be invalid now?
The Jordan normal form does not require more "exactness" from the ring as do the eigenvalues which are already implemented for symbolic matrices (calling maxima). Hence I see no point in discussing whether or not we should offer a jordan_form method for symbolic matrices, it seems natural to do it as what is proposed here.

Just one thing: to be consistent with what is returned over other coefficient domains, the Jordan form should display the subdivision of the block matrix.
  {{{#!python
  sage: a = matrix(QQ,3,[1,0,1,0,2,0,0,0,1])
  sage: a.jordan_form()
  [2|0 0]
  [-+---]
  [0|1 1]
  [0|0 1]
  }}}



---

archive/issue_comments_050486.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-09-15T16:09:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6337#issuecomment-50486",
    "user": "https://github.com/ClementPernet"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_050487.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-09-17T15:56:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6337#issuecomment-50487",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_050488.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-09-17T15:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6337#issuecomment-50488",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_050489.json:
```json
{
    "body": "Replying to [comment:12 cpernet]:\n> Just one thing: to be consistent with what is returned over other coefficient domains, the Jordan form should display the subdivision of the block matrix.\nThanks for noticing, I added this in the latest commit.",
    "created_at": "2015-09-17T15:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6337#issuecomment-50489",
    "user": "https://github.com/pjbruin"
}
```

Replying to [comment:12 cpernet]:
> Just one thing: to be consistent with what is returned over other coefficient domains, the Jordan form should display the subdivision of the block matrix.
Thanks for noticing, I added this in the latest commit.



---

archive/issue_comments_050490.json:
```json
{
    "body": "Thanks, this is all good to me.",
    "created_at": "2015-09-18T05:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6337#issuecomment-50490",
    "user": "https://github.com/ClementPernet"
}
```

Thanks, this is all good to me.



---

archive/issue_comments_050491.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-09-18T05:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6337#issuecomment-50491",
    "user": "https://github.com/ClementPernet"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050492.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2015-09-18T07:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6337#issuecomment-50492",
    "user": "https://github.com/vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_050493.json:
```json
{
    "body": "Reviewer name missing",
    "created_at": "2015-09-18T07:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6337#issuecomment-50493",
    "user": "https://github.com/vbraun"
}
```

Reviewer name missing



---

archive/issue_comments_050494.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2015-09-18T11:41:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6337#issuecomment-50494",
    "user": "https://github.com/ClementPernet"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_050495.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-09-18T19:10:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6337#issuecomment-50495",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_014906.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-09-18T19:10:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6337",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6337#event-14906"
}
```
