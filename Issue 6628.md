# Issue 6628: [with patch, needs review] Singular functions via libSingular

archive/issues_006628.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @burcin\n\nKeywords: singular, libsingular, commutative algebra\n\nThe attached patch implements the following:\n\n\n```\nsage: P = PolynomialRing(GF(127),10,'x')\nsage: I = Ideal(P.random_element() for _ in range(3000))\nsage: from sage.libs.singular.function import singular_function, lib\nsage: groebner = singular_function('groebner')\nsage: %time groebner(I)\nCPU times: user 0.07 s, sys: 0.00 s, total: 0.08 s\nWall time: 0.08 s\n[1]\n```\n\n\nFor comparison, the Singular pexpect interface needs almost two seconds for the same task (due to string parsing on both ends, IPC, etc.)\n\n\n```\nsage: %time I.groebner_basis()\nCPU times: user 0.96 s, sys: 0.24 s, total: 1.21 s\nWall time: 1.92 s\n[1]\n```\n\n\nThis patch requires an updated Singular SPKG (see below).\n\nIssue created by migration from https://trac.sagemath.org/ticket/6628\n\n",
    "created_at": "2009-07-26T13:59:05Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, needs review] Singular functions via libSingular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6628",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @burcin

Keywords: singular, libsingular, commutative algebra

The attached patch implements the following:


```
sage: P = PolynomialRing(GF(127),10,'x')
sage: I = Ideal(P.random_element() for _ in range(3000))
sage: from sage.libs.singular.function import singular_function, lib
sage: groebner = singular_function('groebner')
sage: %time groebner(I)
CPU times: user 0.07 s, sys: 0.00 s, total: 0.08 s
Wall time: 0.08 s
[1]
```


For comparison, the Singular pexpect interface needs almost two seconds for the same task (due to string parsing on both ends, IPC, etc.)


```
sage: %time I.groebner_basis()
CPU times: user 0.96 s, sys: 0.24 s, total: 1.21 s
Wall time: 1.92 s
[1]
```


This patch requires an updated Singular SPKG (see below).

Issue created by migration from https://trac.sagemath.org/ticket/6628





---

archive/issue_comments_054191.json:
```json
{
    "body": "* This patch depends on #6596\n  * The updated SPKG is available at http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090723.spkg",
    "created_at": "2009-07-26T14:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6628#issuecomment-54191",
    "user": "https://github.com/malb"
}
```

* This patch depends on #6596
  * The updated SPKG is available at http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090723.spkg



---

archive/issue_comments_054192.json:
```json
{
    "body": "Burcin, I just replaced the patch to fix a doctest failure.",
    "created_at": "2009-07-26T15:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6628#issuecomment-54192",
    "user": "https://github.com/malb"
}
```

Burcin, I just replaced the patch to fix a doctest failure.



---

archive/issue_comments_054193.json:
```json
{
    "body": "Btw. this also works now:\n\n\n```\nsage: from sage.libs.singular.function import singular_function, lib\nsage: groebner = singular_function('groebner')\nsage: groebner?\nType:           SingularLibraryFunction\nBase Class:     <type 'sage.libs.singular.function.SingularLibraryFunction'>\nString Form:    groebner (singular function)\nNamespace:      Interactive\nFile:           /usr/local/sage-4.1/local/lib/python2.6/site-packages/sage/libs/singular/function.so\nDocstring:\n\n    groebner\n    --------\n\n    Procedure from library `standard.lib' (*note standard_lib::).\n\n    *Syntax:*\n         `groebner (' ideal_expression `)'\n         `groebner (' module_expression `)'\n         `groebner (' ideal_expression`,' int_expression `)'\n         `groebner (' module_expression`,' int_expression `)'\n...\n```\n",
    "created_at": "2009-07-26T15:26:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6628#issuecomment-54193",
    "user": "https://github.com/malb"
}
```

Btw. this also works now:


```
sage: from sage.libs.singular.function import singular_function, lib
sage: groebner = singular_function('groebner')
sage: groebner?
Type:           SingularLibraryFunction
Base Class:     <type 'sage.libs.singular.function.SingularLibraryFunction'>
String Form:    groebner (singular function)
Namespace:      Interactive
File:           /usr/local/sage-4.1/local/lib/python2.6/site-packages/sage/libs/singular/function.so
Docstring:

    groebner
    --------

    Procedure from library `standard.lib' (*note standard_lib::).

    *Syntax:*
         `groebner (' ideal_expression `)'
         `groebner (' module_expression `)'
         `groebner (' ideal_expression`,' int_expression `)'
         `groebner (' module_expression`,' int_expression `)'
...
```




---

archive/issue_comments_054194.json:
```json
{
    "body": "Hi!\nIt looks very promosing.\nHowever, I have difficulties to apply the patch.\nUsing sage-4.1.0 and the updated singular spkg:\n\nI tried it with and without the refactoring patch, also using a fresh installation:\n\n```\nsage -hg import ~/Downloads/libsingular_functions.patch \napplying /Users/michael/Downloads/libsingular_functions.patch\npatching file module_list.py\nHunk #1 FAILED at 441\n1 out of 1 hunks FAILED -- saving rejects to file module_list.py.rej\nunable to find 'sage/libs/singular/polynomial.pyx' for patching\n1 out of 1 hunks FAILED -- saving rejects to file sage/libs/singular/polynomial.pyx.rej\npatching file sage/libs/singular/singular-cdefs.pxi\nHunk #3 FAILED at 207\nHunk #4 succeeded at 215 with fuzz 2 (offset -43 lines).\nHunk #7 FAILED at 853\n2 out of 7 hunks FAILED -- saving rejects to file sage/libs/singular/singular-cdefs.pxi.rej\npatching file sage/libs/singular/singular.pxd\nHunk #1 FAILED at 0\nHunk #2 FAILED at 26\n2 out of 2 hunks FAILED -- saving rejects to file sage/libs/singular/singular.pxd.rej\npatching file sage/libs/singular/singular.pyx\nHunk #1 FAILED at 24\nHunk #2 succeeded at 514 with fuzz 2 (offset -15 lines).\nHunk #3 FAILED at 593\n2 out of 3 hunks FAILED -- saving rejects to file sage/libs/singular/singular.pyx.rej\npatching file sage/rings/polynomial/multi_polynomial_libsingular.pyx\nHunk #1 FAILED at 1906\nHunk #2 FAILED at 2019\n2 out of 2 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_libsingular.pyx.rej\n```\n\nMichael",
    "created_at": "2009-07-27T07:48:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6628#issuecomment-54194",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

Hi!
It looks very promosing.
However, I have difficulties to apply the patch.
Using sage-4.1.0 and the updated singular spkg:

I tried it with and without the refactoring patch, also using a fresh installation:

```
sage -hg import ~/Downloads/libsingular_functions.patch 
applying /Users/michael/Downloads/libsingular_functions.patch
patching file module_list.py
Hunk #1 FAILED at 441
1 out of 1 hunks FAILED -- saving rejects to file module_list.py.rej
unable to find 'sage/libs/singular/polynomial.pyx' for patching
1 out of 1 hunks FAILED -- saving rejects to file sage/libs/singular/polynomial.pyx.rej
patching file sage/libs/singular/singular-cdefs.pxi
Hunk #3 FAILED at 207
Hunk #4 succeeded at 215 with fuzz 2 (offset -43 lines).
Hunk #7 FAILED at 853
2 out of 7 hunks FAILED -- saving rejects to file sage/libs/singular/singular-cdefs.pxi.rej
patching file sage/libs/singular/singular.pxd
Hunk #1 FAILED at 0
Hunk #2 FAILED at 26
2 out of 2 hunks FAILED -- saving rejects to file sage/libs/singular/singular.pxd.rej
patching file sage/libs/singular/singular.pyx
Hunk #1 FAILED at 24
Hunk #2 succeeded at 514 with fuzz 2 (offset -15 lines).
Hunk #3 FAILED at 593
2 out of 3 hunks FAILED -- saving rejects to file sage/libs/singular/singular.pyx.rej
patching file sage/rings/polynomial/multi_polynomial_libsingular.pyx
Hunk #1 FAILED at 1906
Hunk #2 FAILED at 2019
2 out of 2 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_libsingular.pyx.rej
```

Michael



---

archive/issue_comments_054195.json:
```json
{
    "body": "Hi Michael, this is strange, here is what works for me\n\n* I installed the new Singular SPKG\n* `hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6596/libsingular_refactoring.patch`\n* `hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6628/libsingular_functions.patch`\n* `sage -b`\n\nI have no failed hunks etc. with that.",
    "created_at": "2009-07-27T15:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6628#issuecomment-54195",
    "user": "https://github.com/malb"
}
```

Hi Michael, this is strange, here is what works for me

* I installed the new Singular SPKG
* `hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6596/libsingular_refactoring.patch`
* `hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6628/libsingular_functions.patch`
* `sage -b`

I have no failed hunks etc. with that.



---

archive/issue_comments_054196.json:
```json
{
    "body": "I am happy with the refactoring of my code :-).\nI played with it and I like it.\nFrom the Singular side, this nontrivial patch looks fine.",
    "created_at": "2009-07-27T15:50:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6628#issuecomment-54196",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

I am happy with the refactoring of my code :-).
I played with it and I like it.
From the Singular side, this nontrivial patch looks fine.



---

archive/issue_comments_054197.json:
```json
{
    "body": "Here some different timings with even better factor: opposite kind of example: very tiny input, output and almost nothing to compute, replaces some\nsingular interpreter call via pexpect with libsingular kernel function call\n\n\n```python\nfrom sage.libs.singular import function as sf\nintersect=sf.SingularKernelFunction(\"intersect\")\nsage: P.<x,y,z>=QQ[]\nsage: j=P.ideal(x,z)\nsage: i=P.ideal(x,y)\nsage: timeit(\"z=i.intersection(j)\")\n125 loops, best of 3: 5.12 ms per loop\nsage: timeit(\"z=intersect(i,j)\")\n625 loops, best of 3: 60.9 \u00b5s per loop\n\n```\n",
    "created_at": "2009-07-29T07:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6628#issuecomment-54197",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

Here some different timings with even better factor: opposite kind of example: very tiny input, output and almost nothing to compute, replaces some
singular interpreter call via pexpect with libsingular kernel function call


```python
from sage.libs.singular import function as sf
intersect=sf.SingularKernelFunction("intersect")
sage: P.<x,y,z>=QQ[]
sage: j=P.ideal(x,z)
sage: i=P.ideal(x,y)
sage: timeit("z=i.intersection(j)")
125 loops, best of 3: 5.12 ms per loop
sage: timeit("z=intersect(i,j)")
625 loops, best of 3: 60.9 µs per loop

```




---

archive/issue_comments_054198.json:
```json
{
    "body": "It seems this patch makes docbuild choke because\n\n\n```\ngroebner\n--------\n```\n\n\nis contained in one docstring.",
    "created_at": "2009-08-04T11:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6628#issuecomment-54198",
    "user": "https://github.com/malb"
}
```

It seems this patch makes docbuild choke because


```
groebner
--------
```


is contained in one docstring.



---

archive/issue_comments_054199.json:
```json
{
    "body": "fixed in updated patch.",
    "created_at": "2009-08-04T11:32:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6628#issuecomment-54199",
    "user": "https://github.com/malb"
}
```

fixed in updated patch.



---

archive/issue_comments_054200.json:
```json
{
    "body": "On IRC:\n\n```\n[13:02] <mvngu> malb: The package singular-3-1-0-4-20090723.spkg compiles OK on t2!\n```\n",
    "created_at": "2009-08-04T12:55:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6628#issuecomment-54200",
    "user": "https://github.com/malb"
}
```

On IRC:

```
[13:02] <mvngu> malb: The package singular-3-1-0-4-20090723.spkg compiles OK on t2!
```




---

archive/issue_comments_054201.json:
```json
{
    "body": "Attachment [libsingular_functions.patch](tarball://root/attachments/some-uuid/ticket6628/libsingular_functions.patch) by @malb created at 2009-08-19 11:56:08\n\nfixing docstring issue",
    "created_at": "2009-08-19T11:56:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6628#issuecomment-54201",
    "user": "https://github.com/malb"
}
```

Attachment [libsingular_functions.patch](tarball://root/attachments/some-uuid/ticket6628/libsingular_functions.patch) by @malb created at 2009-08-19 11:56:08

fixing docstring issue



---

archive/issue_comments_054202.json:
```json
{
    "body": "Attachment [trac_6628-referee.patch](tarball://root/attachments/some-uuid/ticket6628/trac_6628-referee.patch) by @aghitza created at 2009-08-20 11:05:08\n\napply after the previous patch",
    "created_at": "2009-08-20T11:05:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6628#issuecomment-54202",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_6628-referee.patch](tarball://root/attachments/some-uuid/ticket6628/trac_6628-referee.patch) by @aghitza created at 2009-08-20 11:05:08

apply after the previous patch



---

archive/issue_comments_054203.json:
```json
{
    "body": "This stuff is great!  I've attached a small referee patch that fixes some very minor typos.\n\nI will note that line 280 of `singular-cdefs.pxi` is not entirely confidence-inspiring, but I believe the best way to test and refine this stuff is to get it into Sage and start using it a lot.\n\nNote to the release manager: as pointed out above, one must first merge the new Singular spkg, and the patch(es) at #6596.",
    "created_at": "2009-08-20T11:10:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6628#issuecomment-54203",
    "user": "https://github.com/aghitza"
}
```

This stuff is great!  I've attached a small referee patch that fixes some very minor typos.

I will note that line 280 of `singular-cdefs.pxi` is not entirely confidence-inspiring, but I believe the best way to test and refine this stuff is to get it into Sage and start using it a lot.

Note to the release manager: as pointed out above, one must first merge the new Singular spkg, and the patch(es) at #6596.



---

archive/issue_comments_054204.json:
```json
{
    "body": "The referee patch looks good. I think the next step would be to port stuff in `multi_polynomial_ideal.py` to use this new stuff and see what happens.",
    "created_at": "2009-08-20T11:23:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6628#issuecomment-54204",
    "user": "https://github.com/malb"
}
```

The referee patch looks good. I think the next step would be to port stuff in `multi_polynomial_ideal.py` to use this new stuff and see what happens.



---

archive/issue_comments_054205.json:
```json
{
    "body": "Replying to [comment:13 malb]:\n> The referee patch looks good. I think the next step would be to port stuff in `multi_polynomial_ideal.py` to use this new stuff and see what happens.\n\nIndeed.  I'm expecting awesomeness (more Singular functionality readily exposed in Sage), speed, and the occasional bug fix.\n\nI'll try to have a look at #6596 soon, but it's a bit bigger, and it will probably take a few days.",
    "created_at": "2009-08-20T11:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6628#issuecomment-54205",
    "user": "https://github.com/aghitza"
}
```

Replying to [comment:13 malb]:
> The referee patch looks good. I think the next step would be to port stuff in `multi_polynomial_ideal.py` to use this new stuff and see what happens.

Indeed.  I'm expecting awesomeness (more Singular functionality readily exposed in Sage), speed, and the occasional bug fix.

I'll try to have a look at #6596 soon, but it's a bit bigger, and it will probably take a few days.



---

archive/issue_comments_054206.json:
```json
{
    "body": "regarding 280:\nI was a little bit confused, as I thought it would be the same type in idrec and sleftv.\nBut it's indeed void* in sleftv, so the code is correct, but the comment is wrong.\nNothing dangerous, you can remove the warning.\nMichael",
    "created_at": "2009-08-20T12:34:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6628#issuecomment-54206",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

regarding 280:
I was a little bit confused, as I thought it would be the same type in idrec and sleftv.
But it's indeed void* in sleftv, so the code is correct, but the comment is wrong.
Nothing dangerous, you can remove the warning.
Michael



---

archive/issue_comments_054207.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-03T06:09:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6628#issuecomment-54207",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_015644.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-03T06:09:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6628",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6628#event-15644"
}
```



---

archive/issue_comments_054208.json:
```json
{
    "body": "Merged both patches.",
    "created_at": "2009-09-03T06:09:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6628#issuecomment-54208",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged both patches.
