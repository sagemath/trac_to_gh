# Issue 4834: Return eigenvectors as members of a "normal" space instead of as members of an eigenspace

archive/issues_004834.json:
```json
{
    "body": "Assignee: @jasongrout\n\nCC:  @robertwb\n\nFrom sage-support:\n\n```\n\n> It looks like eigenvectors are returned as the basis vectors of the\n> > eigenspace.  Should they be returned as just plain old vectors instead?\n\nYes, definitely.  Then we don't have create a whole bunch of different\nvector spaces for no reason too.\n\n -- William\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4834\n\n",
    "created_at": "2008-12-19T22:29:12Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Return eigenvectors as members of a \"normal\" space instead of as members of an eigenspace",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4834",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @jasongrout

CC:  @robertwb

From sage-support:

```

> It looks like eigenvectors are returned as the basis vectors of the
> > eigenspace.  Should they be returned as just plain old vectors instead?

Yes, definitely.  Then we don't have create a whole bunch of different
vector spaces for no reason too.

 -- William
```


Issue created by migration from https://trac.sagemath.org/ticket/4834





---

archive/issue_comments_036562.json:
```json
{
    "body": "Changing assignee from @williamstein to @jasongrout.",
    "created_at": "2009-10-16T18:05:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4834#issuecomment-36562",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @williamstein to @jasongrout.



---

archive/issue_comments_036563.json:
```json
{
    "body": "Attachment [trac_4834_bug_demo.sws](tarball://root/attachments/some-uuid/ticket4834/trac_4834_bug_demo.sws) by @rbeezer created at 2010-12-10 02:14:37\n\nAttached worksheet does a better job of illustrating the problem.  I plan to attack this at Bug Days if it is still open.\n\nCan we naturally coerce vectors from lower-dimensional subspaces into the obvious ambient vector space (the one with same degree, same ring or a common super-ring)?  That might be one other solution.",
    "created_at": "2010-12-10T02:14:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4834#issuecomment-36563",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_4834_bug_demo.sws](tarball://root/attachments/some-uuid/ticket4834/trac_4834_bug_demo.sws) by @rbeezer created at 2010-12-10 02:14:37

Attached worksheet does a better job of illustrating the problem.  I plan to attack this at Bug Days if it is still open.

Can we naturally coerce vectors from lower-dimensional subspaces into the obvious ambient vector space (the one with same degree, same ring or a common super-ring)?  That might be one other solution.



---

archive/issue_comments_036564.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-12-10T02:14:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4834#issuecomment-36564",
    "user": "https://github.com/rbeezer"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_036565.json:
```json
{
    "body": "I fiddled with this a bit, and thought I posted a patch.  I can help at the Bug Days with this, if it's still open.",
    "created_at": "2010-12-10T02:43:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4834#issuecomment-36565",
    "user": "https://github.com/jasongrout"
}
```

I fiddled with this a bit, and thought I posted a patch.  I can help at the Bug Days with this, if it's still open.



---

archive/issue_comments_036566.json:
```json
{
    "body": "Following looks to me like the essence of the complaint.  Eigenvectors are assigned to their eigenspaces, which I think is useful and informative, and not worth throwing away.  Simple operations seem to work properly, in that computations proceed and parents are assigned accordingly.\n\nHowever, when a symbolic element is introduced, then addition fails with incompatible parents.  It would seem that the vector over the rationals could get promoted to be over the symbolic ring?  Similar behavior occurs for an element of a number field.\n\n\n```\nsage: B=matrix([[1,2],[2,1]])\nsage: spec=B.eigenvectors_right()\nsage: v=spec[0][1][0]\nsage: z=spec[1][1][0]\nsage: v,z\n((1, 1), (1, -1))\nsage: v.parent()\nVector space of degree 2 and dimension 1 over Rational Field\nUser basis matrix:\n[1 1]\nsage: z.parent()\nVector space of degree 2 and dimension 1 over Rational Field\nUser basis matrix:\n[ 1 -1]\nsage: u=3*v\nsage: u.parent()\nVector space of degree 2 and dimension 1 over Rational Field\nUser basis matrix:\n[1 1]\nsage: w = v + z\nsage: w.parent()\nVector space of degree 2 and dimension 2 over Rational Field\nUser basis matrix:\n[ 1 -1]\n[ 1  1]\n\nsage: var('t')\nt\nsage: v + t*z\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/sage/sage-4.6.1.rc1/devel/sage-main/<ipython console> in <module>()\n\n/sage/sage-4.6.1.rc1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:7627)()\n\n/sage/sage-4.6.1.rc1/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6995)()\n\nTypeError: unsupported operand parent(s) for '+': 'Vector space of degree 2 and dimension 1 over Rational Field\nUser basis matrix:\n[1 1]' and 'Vector space of degree 2 and dimension 1 over Symbolic Ring\nUser basis matrix:\n[ 1 -1]'\n\nsage: R.<a>=QuadraticField(-5)\nsage: v + a*z\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/sage/sage-4.6.1.rc1/devel/sage-main/<ipython console> in <module>()\n\n/sage/sage-4.6.1.rc1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:7627)()\n\n/sage/sage-4.6.1.rc1/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6995)()\n\nTypeError: unsupported operand parent(s) for '+': 'Vector space of degree 2 and dimension 1 over Rational Field\nUser basis matrix:\n[1 1]' and 'Vector space of degree 2 and dimension 1 over Number Field in a with defining polynomial x^2 + 5\nUser basis matrix:\n[ 1 -1]'\n```",
    "created_at": "2011-01-11T21:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4834#issuecomment-36566",
    "user": "https://github.com/rbeezer"
}
```

Following looks to me like the essence of the complaint.  Eigenvectors are assigned to their eigenspaces, which I think is useful and informative, and not worth throwing away.  Simple operations seem to work properly, in that computations proceed and parents are assigned accordingly.

However, when a symbolic element is introduced, then addition fails with incompatible parents.  It would seem that the vector over the rationals could get promoted to be over the symbolic ring?  Similar behavior occurs for an element of a number field.


```
sage: B=matrix([[1,2],[2,1]])
sage: spec=B.eigenvectors_right()
sage: v=spec[0][1][0]
sage: z=spec[1][1][0]
sage: v,z
((1, 1), (1, -1))
sage: v.parent()
Vector space of degree 2 and dimension 1 over Rational Field
User basis matrix:
[1 1]
sage: z.parent()
Vector space of degree 2 and dimension 1 over Rational Field
User basis matrix:
[ 1 -1]
sage: u=3*v
sage: u.parent()
Vector space of degree 2 and dimension 1 over Rational Field
User basis matrix:
[1 1]
sage: w = v + z
sage: w.parent()
Vector space of degree 2 and dimension 2 over Rational Field
User basis matrix:
[ 1 -1]
[ 1  1]

sage: var('t')
t
sage: v + t*z
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/sage/sage-4.6.1.rc1/devel/sage-main/<ipython console> in <module>()

/sage/sage-4.6.1.rc1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:7627)()

/sage/sage-4.6.1.rc1/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6995)()

TypeError: unsupported operand parent(s) for '+': 'Vector space of degree 2 and dimension 1 over Rational Field
User basis matrix:
[1 1]' and 'Vector space of degree 2 and dimension 1 over Symbolic Ring
User basis matrix:
[ 1 -1]'

sage: R.<a>=QuadraticField(-5)
sage: v + a*z
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/sage/sage-4.6.1.rc1/devel/sage-main/<ipython console> in <module>()

/sage/sage-4.6.1.rc1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:7627)()

/sage/sage-4.6.1.rc1/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6995)()

TypeError: unsupported operand parent(s) for '+': 'Vector space of degree 2 and dimension 1 over Rational Field
User basis matrix:
[1 1]' and 'Vector space of degree 2 and dimension 1 over Number Field in a with defining polynomial x^2 + 5
User basis matrix:
[ 1 -1]'
```



---

archive/issue_comments_036567.json:
```json
{
    "body": "I spent some time trying to see where to add this to the coercion system, but it was beyond me. I could probably review a fix.",
    "created_at": "2011-01-12T18:03:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4834#issuecomment-36567",
    "user": "https://github.com/rbeezer"
}
```

I spent some time trying to see where to add this to the coercion system, but it was beyond me. I could probably review a fix.



---

archive/issue_comments_036568.json:
```json
{
    "body": "A workaround is to begin with symbolic matrices, which are now amenable to eigenvector computations (albeit slowly).  See #6934, #10346 (coming soon to an official release).  Then results (eigenvectors) are symbolic for starters, so they play nicely with a symbolic expression like the variable t.\n\n```\nsage: B=matrix(SR, [[1,2],[2,1]])\nsage: spec=B.eigenvectors_left()\nsage: spec\n[(3, [(1, 1)], 1), (-1, [(1, -1)], 1)]\nsage: v = spec[0][1][0]\nsage: z = spec[1][1][0]\nsage: z.parent()\nVector space of dimension 2 over Symbolic Ring\nsage: var('t')\nt\nsage: v + t*z\n(t + 1, -t + 1)\n```\n\nBut I think an addition to the coercion system is still the best long-term solution, since these symbolic eigenvalue computations are not real robust.",
    "created_at": "2011-01-22T21:43:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4834#issuecomment-36568",
    "user": "https://github.com/rbeezer"
}
```

A workaround is to begin with symbolic matrices, which are now amenable to eigenvector computations (albeit slowly).  See #6934, #10346 (coming soon to an official release).  Then results (eigenvectors) are symbolic for starters, so they play nicely with a symbolic expression like the variable t.

```
sage: B=matrix(SR, [[1,2],[2,1]])
sage: spec=B.eigenvectors_left()
sage: spec
[(3, [(1, 1)], 1), (-1, [(1, -1)], 1)]
sage: v = spec[0][1][0]
sage: z = spec[1][1][0]
sage: z.parent()
Vector space of dimension 2 over Symbolic Ring
sage: var('t')
t
sage: v + t*z
(t + 1, -t + 1)
```

But I think an addition to the coercion system is still the best long-term solution, since these symbolic eigenvalue computations are not real robust.



---

archive/issue_events_011096.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4834",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4834#event-11096"
}
```



---

archive/issue_events_011097.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4834",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4834#event-11097"
}
```



---

archive/issue_events_011098.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4834",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4834#event-11098"
}
```



---

archive/issue_events_011099.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4834",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4834#event-11099"
}
```



---

archive/issue_events_011100.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4834",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4834#event-11100"
}
```



---

archive/issue_events_011101.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4834",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4834#event-11101"
}
```



---

archive/issue_events_011102.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4834",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4834#event-11102"
}
```
