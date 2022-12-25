# Issue 6596: [with patch, needs review] Singular refactoring and Groebner Strategy objects

archive/issues_006596.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  polybori @burcin\n\nKeywords: singular\n\nThe attached patch factors out some commonly called code for dealing with libsingular to make it more accessible.\n\nAlso, the attached patch wraps Singular's Gr\u00f6bner strategy objects which allow much faster normal form computations.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6596\n\n",
    "created_at": "2009-07-23T07:57:04Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, needs review] Singular refactoring and Groebner Strategy objects",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6596",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  polybori @burcin

Keywords: singular

The attached patch factors out some commonly called code for dealing with libsingular to make it more accessible.

Also, the attached patch wraps Singular's Gröbner strategy objects which allow much faster normal form computations.


Issue created by migration from https://trac.sagemath.org/ticket/6596





---

archive/issue_comments_053893.json:
```json
{
    "body": "CCing Burcin, because this patch contains the first step of refactoring he wants.",
    "created_at": "2009-07-23T08:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6596#issuecomment-53893",
    "user": "https://github.com/malb"
}
```

CCing Burcin, because this patch contains the first step of refactoring he wants.



---

archive/issue_comments_053894.json:
```json
{
    "body": "Groebner Strategy in action\n\n\n```\nsage: P = PolynomialRing(QQ,6,'x')\nsage: I = sage.rings.ideal.Cyclic(P)\nsage: J = Ideal(I.groebner_basis())\nsage: J.ngens()\n45\n```\n\n\n\n```\nsage: f = P.random_element()\n```\n\n\nThe usual call to `kNF`:\n\n\n```\nsage: %timeit f.reduce(J.gens())\n1000 loops, best of 3: 1.11 ms per loop\n```\n\n\nUsing the `GroebnerStrategy` object.\n\n\n```\nsage: %timeit J.reduce(f)\n100000 loops, best of 3: 9.37 \u00b5s per loop\n```\n",
    "created_at": "2009-07-23T08:39:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6596#issuecomment-53894",
    "user": "https://github.com/malb"
}
```

Groebner Strategy in action


```
sage: P = PolynomialRing(QQ,6,'x')
sage: I = sage.rings.ideal.Cyclic(P)
sage: J = Ideal(I.groebner_basis())
sage: J.ngens()
45
```



```
sage: f = P.random_element()
```


The usual call to `kNF`:


```
sage: %timeit f.reduce(J.gens())
1000 loops, best of 3: 1.11 ms per loop
```


Using the `GroebnerStrategy` object.


```
sage: %timeit J.reduce(f)
100000 loops, best of 3: 9.37 µs per loop
```




---

archive/issue_comments_053895.json:
```json
{
    "body": "This patch requires Singular 3-1-0-4 which is available at\n\n  http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090723.spkg",
    "created_at": "2009-07-24T09:07:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6596#issuecomment-53895",
    "user": "https://github.com/malb"
}
```

This patch requires Singular 3-1-0-4 which is available at

  http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090723.spkg



---

archive/issue_comments_053896.json:
```json
{
    "body": "Doctests may fail on 32-bit system, #6628 contains the fix, sorry for the mixing.",
    "created_at": "2009-07-26T16:10:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6596#issuecomment-53896",
    "user": "https://github.com/malb"
}
```

Doctests may fail on 32-bit system, #6628 contains the fix, sorry for the mixing.



---

archive/issue_comments_053897.json:
```json
{
    "body": "Fixed doctests on 32-bit OSX.",
    "created_at": "2009-07-26T16:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6596#issuecomment-53897",
    "user": "https://github.com/malb"
}
```

Fixed doctests on 32-bit OSX.



---

archive/issue_comments_053898.json:
```json
{
    "body": "I am having trouble applying this patch on top of sage-4.1.1 + the latest spkg at #6476.  The issues occur in `multi_polynomial_libsingular.pyx`, and there is too much stuff going on for me to just rebase it myself...",
    "created_at": "2009-08-19T07:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6596#issuecomment-53898",
    "user": "https://github.com/aghitza"
}
```

I am having trouble applying this patch on top of sage-4.1.1 + the latest spkg at #6476.  The issues occur in `multi_polynomial_libsingular.pyx`, and there is too much stuff going on for me to just rebase it myself...



---

archive/issue_comments_053899.json:
```json
{
    "body": "Replying to [comment:3 malb]:\n> This patch requires Singular 3-1-0-4 which is available at\n> \n>   http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090723.spkg\n> \n\nNote that this is outdated, use \n\n  http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090818.spkg\n\ninstead.",
    "created_at": "2009-08-19T10:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6596#issuecomment-53899",
    "user": "https://github.com/malb"
}
```

Replying to [comment:3 malb]:
> This patch requires Singular 3-1-0-4 which is available at
> 
>   http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090723.spkg
> 

Note that this is outdated, use 

  http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090818.spkg

instead.



---

archive/issue_comments_053900.json:
```json
{
    "body": "Attachment [libsingular_refactoring.patch](tarball://root/attachments/some-uuid/ticket6596/libsingular_refactoring.patch) by @malb created at 2009-08-19 11:42:45\n\nshould apply cleanly against 4.1.1",
    "created_at": "2009-08-19T11:42:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6596#issuecomment-53900",
    "user": "https://github.com/malb"
}
```

Attachment [libsingular_refactoring.patch](tarball://root/attachments/some-uuid/ticket6596/libsingular_refactoring.patch) by @malb created at 2009-08-19 11:42:45

should apply cleanly against 4.1.1



---

archive/issue_comments_053901.json:
```json
{
    "body": "I rebased and updated the patch.",
    "created_at": "2009-08-19T11:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6596#issuecomment-53901",
    "user": "https://github.com/malb"
}
```

I rebased and updated the patch.



---

archive/issue_comments_053902.json:
```json
{
    "body": "Attachment [trac_6596-referee.patch](tarball://root/attachments/some-uuid/ticket6596/trac_6596-referee.patch) by @aghitza created at 2009-08-27 00:53:23\n\napply after the previous patch",
    "created_at": "2009-08-27T00:53:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6596#issuecomment-53902",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_6596-referee.patch](tarball://root/attachments/some-uuid/ticket6596/trac_6596-referee.patch) by @aghitza created at 2009-08-27 00:53:23

apply after the previous patch



---

archive/issue_comments_053903.json:
```json
{
    "body": "Looks good.  The attached patch fixes some minor docstring problems.",
    "created_at": "2009-08-27T00:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6596#issuecomment-53903",
    "user": "https://github.com/aghitza"
}
```

Looks good.  The attached patch fixes some minor docstring problems.



---

archive/issue_comments_053904.json:
```json
{
    "body": "Thanks, the referee patch looks good to me.",
    "created_at": "2009-08-27T09:34:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6596#issuecomment-53904",
    "user": "https://github.com/malb"
}
```

Thanks, the referee patch looks good to me.



---

archive/issue_comments_053905.json:
```json
{
    "body": "Merged both patches.",
    "created_at": "2009-09-03T05:34:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6596#issuecomment-53905",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged both patches.



---

archive/issue_comments_053906.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-03T05:34:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6596#issuecomment-53906",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_053907.json:
```json
{
    "body": "See #6872 for a follow-up to this ticket.",
    "created_at": "2009-09-03T05:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6596#issuecomment-53907",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

See #6872 for a follow-up to this ticket.
