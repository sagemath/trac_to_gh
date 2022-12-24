# Issue 3704: diagonal_matrix does not accept vectors

archive/issues_003704.json:
```json
{
    "body": "Assignee: was\n\nSo I think this is a bug \n\n```\nsage: w=vector(RR,[1,2,3])\nsage: d=diagonal_matrix(w)\nUnboundLocalError: local variable 'v' referenced before assignment\n```\n\nThe following fails as well\n\n```\nsage: d=diagonal_matrix(RR,w) \n```\n\nthe only thing that works is \n\n```\nsage: d=diagonal_matrix(RR,list(w))\n```\n\nA stupid but easy fix is to try to turn any argument to diagonal_matrix into a list before bailing out (its in matrix/constructor.py), but there should probably be logic actually expecting vectors and analyzing the parents?\n\nIssue created by migration from https://trac.sagemath.org/ticket/3704\n\n",
    "created_at": "2008-07-22T04:35:52Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "diagonal_matrix does not accept vectors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3704",
    "user": "jkantor"
}
```
Assignee: was

So I think this is a bug 

```
sage: w=vector(RR,[1,2,3])
sage: d=diagonal_matrix(w)
UnboundLocalError: local variable 'v' referenced before assignment
```

The following fails as well

```
sage: d=diagonal_matrix(RR,w) 
```

the only thing that works is 

```
sage: d=diagonal_matrix(RR,list(w))
```

A stupid but easy fix is to try to turn any argument to diagonal_matrix into a list before bailing out (its in matrix/constructor.py), but there should probably be logic actually expecting vectors and analyzing the parents?

Issue created by migration from https://trac.sagemath.org/ticket/3704





---

archive/issue_comments_026269.json:
```json
{
    "body": "Would it be easy as taking the argument to diagonal_matrix and sending it through Sequence?\n\n```\nsage: v=vector(QQ,[1,2,3/4])\nsage: v\n(1, 2, 3/4)\nsage: b=diagonal_matrix(Sequence(v)); b\n\n[  1   0   0]\n[  0   2   0]\n[  0   0 3/4]\nsage: b.parent()\nFull MatrixSpace of 3 by 3 dense matrices over Rational Field\n```\n",
    "created_at": "2008-07-22T14:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26269",
    "user": "jason"
}
```

Would it be easy as taking the argument to diagonal_matrix and sending it through Sequence?

```
sage: v=vector(QQ,[1,2,3/4])
sage: v
(1, 2, 3/4)
sage: b=diagonal_matrix(Sequence(v)); b

[  1   0   0]
[  0   2   0]
[  0   0 3/4]
sage: b.parent()
Full MatrixSpace of 3 by 3 dense matrices over Rational Field
```




---

archive/issue_comments_026270.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2008-07-22T16:37:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26270",
    "user": "jason"
}
```

Changing priority from minor to major.



---

archive/issue_comments_026271.json:
```json
{
    "body": "The attached patch is a complete rewrite of diagonal_matrix which now does the following:\n\n1. If the first argument is a ring, pop it off the argument list\n2. If the next thing can be made into a Sequence, do so and use those elements as the diagonal elements.  If the next thing cannot be made into a sequence, then take the remainder of the argument list and use those things as the diagonal elements.\n3. Prepend the ring if one was specified and send everything to the matrix() function.\n\nThis changes the syntax slightly; in order to get a matrix of a specific size, you need to pass an nrows and/or ncols option.  But it is very nice in that it allows diagonal_matrix(1,2,3) or, as mentioned in this ticket, diagonal_matrix(v) where v is a vector.\n\nAll doctests in sage/matrix/* pass and all doctests elsewhere that I found using diagonal_matrix also pass.",
    "created_at": "2008-07-22T16:37:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26271",
    "user": "jason"
}
```

The attached patch is a complete rewrite of diagonal_matrix which now does the following:

1. If the first argument is a ring, pop it off the argument list
2. If the next thing can be made into a Sequence, do so and use those elements as the diagonal elements.  If the next thing cannot be made into a sequence, then take the remainder of the argument list and use those things as the diagonal elements.
3. Prepend the ring if one was specified and send everything to the matrix() function.

This changes the syntax slightly; in order to get a matrix of a specific size, you need to pass an nrows and/or ncols option.  But it is very nice in that it allows diagonal_matrix(1,2,3) or, as mentioned in this ticket, diagonal_matrix(v) where v is a vector.

All doctests in sage/matrix/* pass and all doctests elsewhere that I found using diagonal_matrix also pass.



---

archive/issue_comments_026272.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-07-22T16:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26272",
    "user": "jason"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_026273.json:
```json
{
    "body": "I guess it really is a defect, as pointed about above; there is a bug that is fixed.",
    "created_at": "2008-07-22T16:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26273",
    "user": "jason"
}
```

I guess it really is a defect, as pointed about above; there is a bug that is fixed.



---

archive/issue_comments_026274.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2008-07-22T16:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26274",
    "user": "jason"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_026275.json:
```json
{
    "body": "I generally like this patch, and it provides useful functionality.\n\nI applied th patch to 3.0.4 with no problem and all tests in\nsage/matrix pass.\n\nTwo things seemed strange to me:\n\n1. I cannot see a reason for the provided facility for padding\n    with zeros when nrows is given explicitly.  I just cannot think of\n    a time when anyone would need this!\n\n2. The example  diagonal_matrix(GF(2),GF(5))  is really crazy.\n    [It returns a diagonal matrix of size 5 and entries 0,1,0,1,0,\n    using a list of the elements of GF(5) coerced into GF(2)!]\n\n    This is surely a weird side-effect rather than a useful example.\n    the same result would come from diagonal_matrix(GF(2),range(5))\n    which is a little more sane.\n\nThat last example would not even work if it were not possible to\ncoerce from GF(5) to GF(2).  And I really think that should not be\npossible.  Does it still happen in the \"new coercion model\", I wonder?",
    "created_at": "2008-07-29T01:58:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26275",
    "user": "cremona"
}
```

I generally like this patch, and it provides useful functionality.

I applied th patch to 3.0.4 with no problem and all tests in
sage/matrix pass.

Two things seemed strange to me:

1. I cannot see a reason for the provided facility for padding
    with zeros when nrows is given explicitly.  I just cannot think of
    a time when anyone would need this!

2. The example  diagonal_matrix(GF(2),GF(5))  is really crazy.
    [It returns a diagonal matrix of size 5 and entries 0,1,0,1,0,
    using a list of the elements of GF(5) coerced into GF(2)!]

    This is surely a weird side-effect rather than a useful example.
    the same result would come from diagonal_matrix(GF(2),range(5))
    which is a little more sane.

That last example would not even work if it were not possible to
coerce from GF(5) to GF(2).  And I really think that should not be
possible.  Does it still happen in the "new coercion model", I wonder?



---

archive/issue_comments_026276.json:
```json
{
    "body": "The patch looks mostly good, but I heartily agree with points (1) and (2). Also, the following gives an undesired result: \n\n\n```\nsage: diagonal_matrix(x^3+3, x+1)\n```\n\n\nIf a ring is specified, it is converted even if there is no coercion. This allows stuff like\n\n\n```\nsage: matrix(GF(101), 2, [1, 1/2, 1/3, 1/4])\n[ 1 51]\n[34 76]\n```\n\n\ndespite there being no coercion QQ -> GF(101).",
    "created_at": "2008-07-29T08:41:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26276",
    "user": "robertwb"
}
```

The patch looks mostly good, but I heartily agree with points (1) and (2). Also, the following gives an undesired result: 


```
sage: diagonal_matrix(x^3+3, x+1)
```


If a ring is specified, it is converted even if there is no coercion. This allows stuff like


```
sage: matrix(GF(101), 2, [1, 1/2, 1/3, 1/4])
[ 1 51]
[34 76]
```


despite there being no coercion QQ -> GF(101).



---

archive/issue_comments_026277.json:
```json
{
    "body": "The patch looks mostly good, but I heartily agree with points (1) and (2). Also, the following gives an undesired result: \n\n\n```\nsage: diagonal_matrix(x^3+3, x+1)\n```\n\n\nIf a ring is specified, it is converted even if there is no coercion. This allows stuff like\n\n\n```\nsage: matrix(GF(101), 2, [1, 1/2, 1/3, 1/4])\n[ 1 51]\n[34 76]\n```\n\n\ndespite there being no coercion QQ -> GF(101).",
    "created_at": "2008-07-29T08:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26277",
    "user": "robertwb"
}
```

The patch looks mostly good, but I heartily agree with points (1) and (2). Also, the following gives an undesired result: 


```
sage: diagonal_matrix(x^3+3, x+1)
```


If a ring is specified, it is converted even if there is no coercion. This allows stuff like


```
sage: matrix(GF(101), 2, [1, 1/2, 1/3, 1/4])
[ 1 51]
[34 76]
```


despite there being no coercion QQ -> GF(101).



---

archive/issue_comments_026278.json:
```json
{
    "body": "Thanks for the feedback!  I'm at a conference now, so I won't have time to address point 2 for a few days.  However, to address point 1: the previous version of diagonal_matrix allowed for the rows to be specified and padded with zeros.  I was providing an example which showed how to achieve this effect.  Basically, I'm also showing that behavior is like the matrix() command (to which I am just blindly passing all keyword arguments, except for some special behavior about the sparse keyword).  So: the behavior is a result of the behavior of matrix() and shows how to achieve a former behavior of diagonal_matrix.  Whether or not it is actually useful is another issue: if anyone did use this feature, though, it might be nice to have an example of how to do it with the new diagonal_matrix.\n\nI also agree that coercion should play a role, as pointed out in point 2.  I'll look at that early next week, hopefully.\n\nThanks again!",
    "created_at": "2008-07-30T09:33:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26278",
    "user": "jason"
}
```

Thanks for the feedback!  I'm at a conference now, so I won't have time to address point 2 for a few days.  However, to address point 1: the previous version of diagonal_matrix allowed for the rows to be specified and padded with zeros.  I was providing an example which showed how to achieve this effect.  Basically, I'm also showing that behavior is like the matrix() command (to which I am just blindly passing all keyword arguments, except for some special behavior about the sparse keyword).  So: the behavior is a result of the behavior of matrix() and shows how to achieve a former behavior of diagonal_matrix.  Whether or not it is actually useful is another issue: if anyone did use this feature, though, it might be nice to have an example of how to do it with the new diagonal_matrix.

I also agree that coercion should play a role, as pointed out in point 2.  I'll look at that early next week, hopefully.

Thanks again!



---

archive/issue_comments_026279.json:
```json
{
    "body": "Okay, with the example: \n\n```\nsage: matrix(GF(101), 2, [1, 1/2, 1/3, 1/4])\n[ 1 51]\n[34 76]\n```\n\nthat comes from `GF(101)(1/2)` giving 51, etc.  I just hand it off to the matrix() constructor, which in turn hands the job off to the MatrixSpace constructor.\n\nAs to another point, I get:\n\n```\nsage: diagonal_matrix(x^3+3, x+1)\n\n[x^3 + 3       0]\n[      0   x + 1]\n```\n\nso with x being a symbolic variable, things work fine.\n\nHowever, if we have an iterable object, then things are not so good.  In that case, the patch tries to construct a Sequence object from the iterable object, which is where you get your weird results.\n\nI'm changing the patch so that if a list or tuple is passed in, then it tries to construct Sequence object from that list or tuple.  Note that this is only for backwards-compatibility, so we can still pass a list into diagonal_matrix and have it return what it used to return.",
    "created_at": "2008-08-02T14:41:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26279",
    "user": "jason"
}
```

Okay, with the example: 

```
sage: matrix(GF(101), 2, [1, 1/2, 1/3, 1/4])
[ 1 51]
[34 76]
```

that comes from `GF(101)(1/2)` giving 51, etc.  I just hand it off to the matrix() constructor, which in turn hands the job off to the MatrixSpace constructor.

As to another point, I get:

```
sage: diagonal_matrix(x^3+3, x+1)

[x^3 + 3       0]
[      0   x + 1]
```

so with x being a symbolic variable, things work fine.

However, if we have an iterable object, then things are not so good.  In that case, the patch tries to construct a Sequence object from the iterable object, which is where you get your weird results.

I'm changing the patch so that if a list or tuple is passed in, then it tries to construct Sequence object from that list or tuple.  Note that this is only for backwards-compatibility, so we can still pass a list into diagonal_matrix and have it return what it used to return.



---

archive/issue_comments_026280.json:
```json
{
    "body": "Attachment [trac-3704-diagonal_matrix.patch](tarball://root/attachments/some-uuid/ticket3704/trac-3704-diagonal_matrix.patch) by jason created at 2008-08-02 17:18:46\n\nOkay, new patch is up which should take of the issues in my previous post.",
    "created_at": "2008-08-02T17:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26280",
    "user": "jason"
}
```

Attachment [trac-3704-diagonal_matrix.patch](tarball://root/attachments/some-uuid/ticket3704/trac-3704-diagonal_matrix.patch) by jason created at 2008-08-02 17:18:46

Okay, new patch is up which should take of the issues in my previous post.



---

archive/issue_comments_026281.json:
```json
{
    "body": "I successfully applied the patch to 3.1.alpha0 and all seems to work as advertised.  All tests in sage.matrix pass.  Publish!",
    "created_at": "2008-08-09T16:34:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26281",
    "user": "cremona"
}
```

I successfully applied the patch to 3.1.alpha0 and all seems to work as advertised.  All tests in sage.matrix pass.  Publish!



---

archive/issue_comments_026282.json:
```json
{
    "body": "Patches at #2577 seem to do something very close to this patch, so someone ought to sort out if there are any differences that could be resolved into one unified patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-11T00:43:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26282",
    "user": "mabshoff"
}
```

Patches at #2577 seem to do something very close to this patch, so someone ought to sort out if there are any differences that could be resolved into one unified patch.

Cheers,

Michael



---

archive/issue_comments_026283.json:
```json
{
    "body": "I looked at the patch at #2577 and like the patch here better.  I can't see any extra functionality in #2577 that I would want to merge to this patch, but I'm open to suggestions.",
    "created_at": "2008-08-15T23:38:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26283",
    "user": "jason"
}
```

I looked at the patch at #2577 and like the patch here better.  I can't see any extra functionality in #2577 that I would want to merge to this patch, but I'm open to suggestions.



---

archive/issue_comments_026284.json:
```json
{
    "body": "Attachment [trac-3704-diagonal_matrix-2.patch](tarball://root/attachments/some-uuid/ticket3704/trac-3704-diagonal_matrix-2.patch) by jason created at 2008-08-16 00:07:27\n\nI just added a patch, to be applied on top of the first patch, which does two things:\n\n1. Makes a trivial simplification in the code\n\n2. Adds a doctest illustrating the sparse keyword.",
    "created_at": "2008-08-16T00:07:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26284",
    "user": "jason"
}
```

Attachment [trac-3704-diagonal_matrix-2.patch](tarball://root/attachments/some-uuid/ticket3704/trac-3704-diagonal_matrix-2.patch) by jason created at 2008-08-16 00:07:27

I just added a patch, to be applied on top of the first patch, which does two things:

1. Makes a trivial simplification in the code

2. Adds a doctest illustrating the sparse keyword.



---

archive/issue_comments_026285.json:
```json
{
    "body": "Hmm, can we sort out this mess, i.e. what to do about #2577? The consensus seems to be to merge theses patches and close #2577?\n\nAn final positive review will also be good since Jason did add a second patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-02T11:26:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26285",
    "user": "mabshoff"
}
```

Hmm, can we sort out this mess, i.e. what to do about #2577? The consensus seems to be to merge theses patches and close #2577?

An final positive review will also be good since Jason did add a second patch.

Cheers,

Michael



---

archive/issue_comments_026286.json:
```json
{
    "body": "Attachment [trac-3704-diagonal_matrix-3.patch](tarball://root/attachments/some-uuid/ticket3704/trac-3704-diagonal_matrix-3.patch) by cremona created at 2008-09-02 12:00:11",
    "created_at": "2008-09-02T12:00:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26286",
    "user": "cremona"
}
```

Attachment [trac-3704-diagonal_matrix-3.patch](tarball://root/attachments/some-uuid/ticket3704/trac-3704-diagonal_matrix-3.patch) by cremona created at 2008-09-02 12:00:11



---

archive/issue_comments_026287.json:
```json
{
    "body": "Let's agree to kill #2577 since it does nothing which these patches do not do, and these are now a lot better.\n\nI applied both patches to 3.1.2.alpha3 with no problems.  All the above examples now work and give sensible answers.  They are not all included as doctests though.\n\nI hit a doctest error in sage/matrix/matrix_integer_dense_hnf.py:\n\n```\nsage -t  devel/sage/sage/matrix/matrix_integer_dense_hnf.py **********************************************************************\nFile \"/home/john/sage-3.1.2.alpha3/tmp/matrix_integer_dense_hnf.py\", line 132:\n    sage: m = diagonal_matrix(ZZ, 68, [2]*66 + [1,1])\nException raised:\n    Traceback (most recent call last):\n      File \"/home/john/sage-3.1.2.alpha3/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[17]>\", line 1, in <module>\n        m = diagonal_matrix(ZZ, Integer(68), [Integer(2)]*Integer(66) + [Integer(1),Integer(1)])###line 132:\n    sage: m = diagonal_matrix(ZZ, 68, [2]*66 + [1,1])\n      File \"/home/john/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/matrix/constructor.py\", line 736, in diagonal_matrix\n        return matrix(*args, **kwds)\n      File \"/home/john/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/matrix/constructor.py\", line 524, in matrix\n        entries, entry_ring = prepare_dict(args[0])\n      File \"/home/john/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/matrix/constructor.py\", line 619, in prepare_dict\n        entries, ring = prepare(X)\n      File \"/home/john/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/matrix/constructor.py\", line 613, in prepare\n        raise TypeError, \"unable to find a common ring for all elements\"\n    TypeError: unable to find a common ring for all elements\n```\n\nThis is trivial to fix, and I added a trivial patch which fixes it.\n\nConclusion:  kill #2577 and merge this one (all three patches).  I assume mabshoff can take on the responsibility of reviewing the final mini-patch!",
    "created_at": "2008-09-02T12:01:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26287",
    "user": "cremona"
}
```

Let's agree to kill #2577 since it does nothing which these patches do not do, and these are now a lot better.

I applied both patches to 3.1.2.alpha3 with no problems.  All the above examples now work and give sensible answers.  They are not all included as doctests though.

I hit a doctest error in sage/matrix/matrix_integer_dense_hnf.py:

```
sage -t  devel/sage/sage/matrix/matrix_integer_dense_hnf.py **********************************************************************
File "/home/john/sage-3.1.2.alpha3/tmp/matrix_integer_dense_hnf.py", line 132:
    sage: m = diagonal_matrix(ZZ, 68, [2]*66 + [1,1])
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-3.1.2.alpha3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[17]>", line 1, in <module>
        m = diagonal_matrix(ZZ, Integer(68), [Integer(2)]*Integer(66) + [Integer(1),Integer(1)])###line 132:
    sage: m = diagonal_matrix(ZZ, 68, [2]*66 + [1,1])
      File "/home/john/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/matrix/constructor.py", line 736, in diagonal_matrix
        return matrix(*args, **kwds)
      File "/home/john/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/matrix/constructor.py", line 524, in matrix
        entries, entry_ring = prepare_dict(args[0])
      File "/home/john/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/matrix/constructor.py", line 619, in prepare_dict
        entries, ring = prepare(X)
      File "/home/john/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/matrix/constructor.py", line 613, in prepare
        raise TypeError, "unable to find a common ring for all elements"
    TypeError: unable to find a common ring for all elements
```

This is trivial to fix, and I added a trivial patch which fixes it.

Conclusion:  kill #2577 and merge this one (all three patches).  I assume mabshoff can take on the responsibility of reviewing the final mini-patch!



---

archive/issue_comments_026288.json:
```json
{
    "body": "Attachment [trac-3704-diagonal_matrix-4.patch](tarball://root/attachments/some-uuid/ticket3704/trac-3704-diagonal_matrix-4.patch) by cremona created at 2008-09-02 12:06:38\n\nPS Forgot to add that doctest: 4th patch does that too.",
    "created_at": "2008-09-02T12:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26288",
    "user": "cremona"
}
```

Attachment [trac-3704-diagonal_matrix-4.patch](tarball://root/attachments/some-uuid/ticket3704/trac-3704-diagonal_matrix-4.patch) by cremona created at 2008-09-02 12:06:38

PS Forgot to add that doctest: 4th patch does that too.



---

archive/issue_comments_026289.json:
```json
{
    "body": "Is there a reason that we got rid of this construction?\n\n\n```\n \t        4. matrix(ring, nrows, diagonal_entries, [sparse=True]): \n\t               matrix with given number of rows and flat list of entries  \n```\n\n\nIt should at least be deprecated first.",
    "created_at": "2008-09-02T23:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26289",
    "user": "mhansen"
}
```

Is there a reason that we got rid of this construction?


```
 	        4. matrix(ring, nrows, diagonal_entries, [sparse=True]): 
	               matrix with given number of rows and flat list of entries  
```


It should at least be deprecated first.



---

archive/issue_comments_026290.json:
```json
{
    "body": "There was exactly one doctest which stopped working with that construction missing, and the fix was just to delete the nrows parameter.\n\nI don't have strong feelings about deprecating things like this.  I think the point of having nrows in there was so that diagonal_entries could be shorter than nrows and then would be padded out by zeroes.  I feel happier requiring the user to provide the whole list of diagonal entries, but if someone wants to put this construction back I don't mind either.",
    "created_at": "2008-09-03T08:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26290",
    "user": "cremona"
}
```

There was exactly one doctest which stopped working with that construction missing, and the fix was just to delete the nrows parameter.

I don't have strong feelings about deprecating things like this.  I think the point of having nrows in there was so that diagonal_entries could be shorter than nrows and then would be padded out by zeroes.  I feel happier requiring the user to provide the whole list of diagonal entries, but if someone wants to put this construction back I don't mind either.



---

archive/issue_comments_026291.json:
```json
{
    "body": "There was some extended discussion on sage-devel and the consensus is that the new non-list constructor will break if more than 255 elements are passed. So this needs work :)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-19T03:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26291",
    "user": "mabshoff"
}
```

There was some extended discussion on sage-devel and the consensus is that the new non-list constructor will break if more than 255 elements are passed. So this needs work :)

Cheers,

Michael



---

archive/issue_comments_026292.json:
```json
{
    "body": "I'm attaching a new patch which takes a much lower level approach to solving the problem. If a complete rewrite is really necessary, I propose we open a new ticket for it, since this ticket is just about constructing a diagonal matrix from a vector.",
    "created_at": "2009-01-23T12:40:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26292",
    "user": "rlm"
}
```

I'm attaching a new patch which takes a much lower level approach to solving the problem. If a complete rewrite is really necessary, I propose we open a new ticket for it, since this ticket is just about constructing a diagonal matrix from a vector.



---

archive/issue_comments_026293.json:
```json
{
    "body": "Attachment [trac-3704.patch](tarball://root/attachments/some-uuid/ticket3704/trac-3704.patch) by rlm created at 2009-01-23 12:41:09\n\nIndependent of the other patches found here.",
    "created_at": "2009-01-23T12:41:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26293",
    "user": "rlm"
}
```

Attachment [trac-3704.patch](tarball://root/attachments/some-uuid/ticket3704/trac-3704.patch) by rlm created at 2009-01-23 12:41:09

Independent of the other patches found here.



---

archive/issue_comments_026294.json:
```json
{
    "body": "Positive review for rlm's patch.  It fixes the problem mentioned in the ticket.  The new ticket rlm mentioned is #5110.",
    "created_at": "2009-01-27T03:55:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26294",
    "user": "jason"
}
```

Positive review for rlm's patch.  It fixes the problem mentioned in the ticket.  The new ticket rlm mentioned is #5110.



---

archive/issue_comments_026295.json:
```json
{
    "body": "(because of #5110, do not delete the other patches on this ticket.)",
    "created_at": "2009-01-27T03:55:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26295",
    "user": "jason"
}
```

(because of #5110, do not delete the other patches on this ticket.)



---

archive/issue_comments_026296.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T14:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26296",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026297.json:
```json
{
    "body": "Merged trac-3704.patch only in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T14:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3704#issuecomment-26297",
    "user": "mabshoff"
}
```

Merged trac-3704.patch only in Sage 3.3.alpha3.

Cheers,

Michael
