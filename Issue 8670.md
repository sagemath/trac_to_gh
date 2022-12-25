# Issue 8670: Provide projections methods for word paths

archive/issues_008670.json:
```json
{
    "body": "Assignee: @seblabbe\n\nCC:  abmasse @videlec @robertwb tjolivet tmonteil\n\nNice mathematical objects can be obtained when projecting appropriately a discrete path (Rauzy fractals for instance).\n\nThis patch introduces 3 projection functions for word path. It also adds 1 function to `WordMorphism` and 2 matrix rotation functions to `sage/plot/plot3d/transforms.pyx`.\n\nThe first 1000 points of the Rauzy fractal :\n\n\n```\n    sage: s = WordMorphism('1->12,2->13,3->1')\n    sage: D = s.fixed_point('1')\n    sage: v = s.pisot_vector()\n    sage: P = WordPaths('123',[(1,0,0),(0,1,0),(0,0,1)])\n    sage: w = P(D[:1000])\n    sage: w.projected_plot(v)\n```\n\n\nSee more examples in doctests.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8670\n\n",
    "created_at": "2010-04-11T12:10:06Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "Provide projections methods for word paths",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8670",
    "user": "https://github.com/seblabbe"
}
```
Assignee: @seblabbe

CC:  abmasse @videlec @robertwb tjolivet tmonteil

Nice mathematical objects can be obtained when projecting appropriately a discrete path (Rauzy fractals for instance).

This patch introduces 3 projection functions for word path. It also adds 1 function to `WordMorphism` and 2 matrix rotation functions to `sage/plot/plot3d/transforms.pyx`.

The first 1000 points of the Rauzy fractal :


```
    sage: s = WordMorphism('1->12,2->13,3->1')
    sage: D = s.fixed_point('1')
    sage: v = s.pisot_vector()
    sage: P = WordPaths('123',[(1,0,0),(0,1,0),(0,0,1)])
    sage: w = P(D[:1000])
    sage: w.projected_plot(v)
```


See more examples in doctests.

Issue created by migration from https://trac.sagemath.org/ticket/8670





---

archive/issue_comments_078760.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-11T13:08:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8670#issuecomment-78760",
    "user": "https://github.com/seblabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078761.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-13T11:44:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8670#issuecomment-78761",
    "user": "https://github.com/seblabbe"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_078762.json:
```json
{
    "body": "There are some limit case problems :\n\n\n```\nsage: from sage.plot.plot3d.transform import *\nsage: rotate_vector_on_axis((1,0,0), 0)\nTraceback (most recent call last):\n...\nZeroDivisionError: Rational division by zero\n```\n\n\nWill post a new patch soon.",
    "created_at": "2010-04-13T11:44:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8670#issuecomment-78762",
    "user": "https://github.com/seblabbe"
}
```

There are some limit case problems :


```
sage: from sage.plot.plot3d.transform import *
sage: rotate_vector_on_axis((1,0,0), 0)
Traceback (most recent call last):
...
ZeroDivisionError: Rational division by zero
```


Will post a new patch soon.



---

archive/issue_comments_078763.json:
```json
{
    "body": "I fixed the above problem in the updated patch. Needs review!\n\nSince I am adding two functions to the file `sage/plot/plot3d/transform.pyx`, I am also adding Robert Bradshaw in cc of this ticket. He might have some comments to share.",
    "created_at": "2010-04-18T19:39:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8670#issuecomment-78763",
    "user": "https://github.com/seblabbe"
}
```

I fixed the above problem in the updated patch. Needs review!

Since I am adding two functions to the file `sage/plot/plot3d/transform.pyx`, I am also adding Robert Bradshaw in cc of this ticket. He might have some comments to share.



---

archive/issue_comments_078764.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-18T19:39:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8670#issuecomment-78764",
    "user": "https://github.com/seblabbe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078765.json:
```json
{
    "body": "Does not depend on any known patch. Applies on 4.3.4.",
    "created_at": "2010-04-27T15:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8670#issuecomment-78765",
    "user": "https://github.com/seblabbe"
}
```

Does not depend on any known patch. Applies on 4.3.4.



---

archive/issue_comments_078766.json:
```json
{
    "body": "Attachment [trac_8670-word-path-projection-sl.patch](tarball://root/attachments/some-uuid/ticket8670/trac_8670-word-path-projection-sl.patch) by @saliola created at 2010-06-23 16:04:26\n\n1. Your definition of Pisot eigenvector is ambiguous.\n\n```\nReturns the left eigenvector of the incidence matrix associated\nto the largest eigenvalue (in absolute value).\n```\n\nIt is possible that there are multiple eigenvalues with the same absolute value:\n\n```\nsage: mu = WordMorphism('a->c,b->c,c->ab')\nsage: m = matrix(mu); m\n[0 0 1]\n[0 0 1]\n[1 1 0]\nsage: m.eigenvalues()\n[0, -1.414213562373095?, 1.414213562373095?]\n```\n\nIt is not clear which eigenvector gets returned here.\n\nAlso, there may be more than one eigenvector associated to your \"maximal\" eigenvalue, and your method only returns one eigenvector:\n\n```\nsage: mu = WordMorphism('a->a,b->b,c->abc')\nsage: mu.pisot_eigenvector_left()\n(1, -1, 0)\nsage: m = matrix(mu); m\n[1 0 1]\n[0 1 1]\n[0 0 1]\nsage: m.eigenspaces_left()\n[\n(1, Vector space of degree 3 and dimension 2 over Rational Field\nUser basis matrix:\n[ 1 -1  0]\n[ 0  0  1])\n]\n```\n\n\n2. The method `directive_vector` should include a definition of what the directive vector is.\n\n3. In your functions `rotate_ith_to_zero` and `rotate_vector_on_axis`, you first construct the matrix and then coerce it into the ring specified by the user. Why is this preferable to doing the computations directly in the ring? What about making this an option `compute_in_ring=False`? I think all you need to do is add the following line at the beginning:\n\n```\nif compute_in_ring is True:\n    v = vector(ring, v)\n```\n",
    "created_at": "2010-06-23T16:04:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8670#issuecomment-78766",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_8670-word-path-projection-sl.patch](tarball://root/attachments/some-uuid/ticket8670/trac_8670-word-path-projection-sl.patch) by @saliola created at 2010-06-23 16:04:26

1. Your definition of Pisot eigenvector is ambiguous.

```
Returns the left eigenvector of the incidence matrix associated
to the largest eigenvalue (in absolute value).
```

It is possible that there are multiple eigenvalues with the same absolute value:

```
sage: mu = WordMorphism('a->c,b->c,c->ab')
sage: m = matrix(mu); m
[0 0 1]
[0 0 1]
[1 1 0]
sage: m.eigenvalues()
[0, -1.414213562373095?, 1.414213562373095?]
```

It is not clear which eigenvector gets returned here.

Also, there may be more than one eigenvector associated to your "maximal" eigenvalue, and your method only returns one eigenvector:

```
sage: mu = WordMorphism('a->a,b->b,c->abc')
sage: mu.pisot_eigenvector_left()
(1, -1, 0)
sage: m = matrix(mu); m
[1 0 1]
[0 1 1]
[0 0 1]
sage: m.eigenspaces_left()
[
(1, Vector space of degree 3 and dimension 2 over Rational Field
User basis matrix:
[ 1 -1  0]
[ 0  0  1])
]
```


2. The method `directive_vector` should include a definition of what the directive vector is.

3. In your functions `rotate_ith_to_zero` and `rotate_vector_on_axis`, you first construct the matrix and then coerce it into the ring specified by the user. Why is this preferable to doing the computations directly in the ring? What about making this an option `compute_in_ring=False`? I think all you need to do is add the following line at the beginning:

```
if compute_in_ring is True:
    v = vector(ring, v)
```




---

archive/issue_comments_078767.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-23T16:04:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8670#issuecomment-78767",
    "user": "https://github.com/saliola"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_078768.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-15T21:00:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8670#issuecomment-78768",
    "user": "https://github.com/seblabbe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078769.json:
```json
{
    "body": "Needs review again!",
    "created_at": "2010-10-15T21:00:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8670#issuecomment-78769",
    "user": "https://github.com/seblabbe"
}
```

Needs review again!



---

archive/issue_comments_078770.json:
```json
{
    "body": "Attachment [trac_8670-review-sl.patch](tarball://root/attachments/some-uuid/ticket8670/trac_8670-review-sl.patch) by @seblabbe created at 2010-10-15 22:05:42\n\nApplies over the precedent patch",
    "created_at": "2010-10-15T22:05:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8670#issuecomment-78770",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac_8670-review-sl.patch](tarball://root/attachments/some-uuid/ticket8670/trac_8670-review-sl.patch) by @seblabbe created at 2010-10-15 22:05:42

Applies over the precedent patch



---

archive/issue_comments_078771.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-28T17:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8670#issuecomment-78771",
    "user": "https://trac.sagemath.org/admin/accounts/users/tjolivet"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_078772.json:
```json
{
    "body": "Hi,\n\nHere are a few remarks:\n\n(1) There is a doctest failure:\n\n  `File \"/home/timo/sage-4.6.1/devel/sage-trac_8670/sage/plot/plot3d/transform.pyx\", line 325:    sage: rotate_vector_on_axis(v, 0, ring=RealField(10)) * vExpected:    (5.5, 0.0020, 0.0020, 0.00)Got:    (5.5, 0.00098, 0.00098, 0.00)`\n\nThis should be fixed by using \"`...`\", and could be done for the other occurrences of printed floats.\n\n(2) I think that the rotations matrices should be in a file in sage/matrix/. I remember having looked for something like `rotate_arbitrary`, but I didn't find it because it was in plot3d/ and not in matrix/.\n\n(3) The documentation for `rotate_vector_on_axis` could be a little bit clearer (the description).\n\nOtherwise this is a nice and useful patch.",
    "created_at": "2011-01-28T17:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8670#issuecomment-78772",
    "user": "https://trac.sagemath.org/admin/accounts/users/tjolivet"
}
```

Hi,

Here are a few remarks:

(1) There is a doctest failure:

  `File "/home/timo/sage-4.6.1/devel/sage-trac_8670/sage/plot/plot3d/transform.pyx", line 325:    sage: rotate_vector_on_axis(v, 0, ring=RealField(10)) * vExpected:    (5.5, 0.0020, 0.0020, 0.00)Got:    (5.5, 0.00098, 0.00098, 0.00)`

This should be fixed by using "`...`", and could be done for the other occurrences of printed floats.

(2) I think that the rotations matrices should be in a file in sage/matrix/. I remember having looked for something like `rotate_arbitrary`, but I didn't find it because it was in plot3d/ and not in matrix/.

(3) The documentation for `rotate_vector_on_axis` could be a little bit clearer (the description).

Otherwise this is a nice and useful patch.



---

archive/issue_comments_078773.json:
```json
{
    "body": "Attachment [trac_8670_second_corrections-sl.patch](tarball://root/attachments/some-uuid/ticket8670/trac_8670_second_corrections-sl.patch) by @seblabbe created at 2011-01-29 13:24:26\n\nApplies over the precedent 2 patches",
    "created_at": "2011-01-29T13:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8670#issuecomment-78773",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac_8670_second_corrections-sl.patch](tarball://root/attachments/some-uuid/ticket8670/trac_8670_second_corrections-sl.patch) by @seblabbe created at 2011-01-29 13:24:26

Applies over the precedent 2 patches



---

archive/issue_comments_078774.json:
```json
{
    "body": "Thanks for the comments. I moved the two rotation matrix constructor to the file `sage/matrix/constructor.py`. I improved the docstrings and fixed the doctest failure (I was having the same).\n\nNeeds review.",
    "created_at": "2011-01-29T13:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8670#issuecomment-78774",
    "user": "https://github.com/seblabbe"
}
```

Thanks for the comments. I moved the two rotation matrix constructor to the file `sage/matrix/constructor.py`. I improved the docstrings and fixed the doctest failure (I was having the same).

Needs review.



---

archive/issue_comments_078775.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-29T13:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8670#issuecomment-78775",
    "user": "https://github.com/seblabbe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078776.json:
```json
{
    "body": "Attachment [trac_8670_folded-sl.patch](tarball://root/attachments/some-uuid/ticket8670/trac_8670_folded-sl.patch) by @seblabbe created at 2011-01-30 00:42:40\n\nApply only this one.",
    "created_at": "2011-01-30T00:42:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8670#issuecomment-78776",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac_8670_folded-sl.patch](tarball://root/attachments/some-uuid/ticket8670/trac_8670_folded-sl.patch) by @seblabbe created at 2011-01-30 00:42:40

Apply only this one.



---

archive/issue_comments_078777.json:
```json
{
    "body": "For the patchbot :\n\nApply trac_8670_folded-sl.patch",
    "created_at": "2011-01-30T00:43:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8670#issuecomment-78777",
    "user": "https://github.com/seblabbe"
}
```

For the patchbot :

Apply trac_8670_folded-sl.patch



---

archive/issue_comments_078778.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-02-07T12:36:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8670#issuecomment-78778",
    "user": "https://trac.sagemath.org/admin/accounts/users/tjolivet"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078779.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-03-17T19:22:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8670#issuecomment-78779",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
