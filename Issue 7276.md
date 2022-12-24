# Issue 7276: Fix PPC issues in totallyreal_rel.py

archive/issues_007276.json:
```json
{
    "body": "Assignee: davidloeffler\n\nCC:  georgsweber was\n\nKeywords: PPC, powerpc, lattice\n\nFrom #7112: I don't think this ended up getting officially logged on trac elsewhere.\n\n\n```\nsage -t -long devel/sage/sage/rings/number_field/totallyreal_rel.py\n```\n\nwill still fail however, there is a deeper problem lurking in that one point of a certain lattice sitting in a certain rectangle is missed in the computations on a PPC platform --- but that would be another ticket. Let the doctest fail for the time being, the enhancements by the patch(es) for this ticket here are needed anyway, I guess.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7276\n\n",
    "created_at": "2009-10-23T23:40:35Z",
    "labels": [
        "number fields",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "Fix PPC issues in totallyreal_rel.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7276",
    "user": "kcrisman"
}
```
Assignee: davidloeffler

CC:  georgsweber was

Keywords: PPC, powerpc, lattice

From #7112: I don't think this ended up getting officially logged on trac elsewhere.


```
sage -t -long devel/sage/sage/rings/number_field/totallyreal_rel.py
```

will still fail however, there is a deeper problem lurking in that one point of a certain lattice sitting in a certain rectangle is missed in the computations on a PPC platform --- but that would be another ticket. Let the doctest fail for the time being, the enhancements by the patch(es) for this ticket here are needed anyway, I guess.



Issue created by migration from https://trac.sagemath.org/ticket/7276





---

archive/issue_comments_060547.json:
```json
{
    "body": "Here is the code for integral_elements_in_box line by line, up to the first place where PPC differs from Intel:\n\n```\nsage: K.<alpha> = NumberField(x^2-2)\nsage: d = K.degree()\nsage: Z_F = K.maximal_order()\nsage: Foo = K.real_embeddings()\nsage: B = K.reduced_basis()\nsage: import numpy\nsage: import numpy.linalg\nsage: L = numpy.array([ [v(b) for b in B] for v in Foo])\nsage: Linv = numpy.linalg.inv(L)\nsage: C = [[0,5],[0,5]]\nsage: Vi = [[C[0][0]],[C[0][1]]]\nsage: \nsage: Linv\n\narray([[ 0.5       ,  0.5       ],\n       [-0.35355339,  0.35355339]])\nsage: for i in range(1,d):\n....:     Vi = sum([ [v + [C[i][0]], v + [C[i][1]]] for v in Vi], [])\n....:     \nsage: Vi\n[[0, 0], [0, 5], [5, 0], [5, 5]]\nsage: V = numpy.matrix(Linv)*(numpy.matrix(Vi).transpose())\nsage: V\n\nmatrix([[  0.00000000e+00,   2.50000000e+00,   2.50000000e+00,\n           5.00000000e+00],\n        [  0.00000000e+00,   1.76776695e+00,  -1.76776695e+00,\n           5.55111512e-17]])\n```\n\nIn particular, the matrices Linv and Vi, even in their numpy versions, are still the same.  Essentially, on PPC (at least G4) the computation -0.35355339*5+0.35355339*5 is not (quite) zero, but on Intel it is.  On Intel we get the same stuff but with just 0., 2.5, etc - and the last entry is 0., no hint of the 5.55e-17.  \n\nAnyway, this leads to the following error (since we are depending on the ceil of zero to be zero, but the ceil of 5.55e-17 is 1):\n\n```\nsage: while j < 2**d:\n    for i in range(d):\n        if V[i,j] < V[i,j+1]:\n            V[i,j] = math.floor(V[i,j])\n            V[i,j+1] = math.ceil(V[i,j+1])\n        else:\n            V[i,j] = math.ceil(V[i,j])\n            V[i,j+1] = math.floor(V[i,j+1])\n    j +=2\n....:         \nsage: V\n\nmatrix([[ 0.,  3.,  2.,  5.],\n        [ 0.,  2., -2.,  1.]])\n```\n\nWhere Intel correctly gives 0. in the last entry.\n\nJust so that it's clear that PPC is the issue:\n\n```\nsage: matrix(Linv)*matrix(Vi).transpose()\n\n[              0.0               2.5               2.5               5.0]\n[              0.0     1.76776695297    -1.76776695297 5.55111512313e-17]\n```\n\nSlightly more digits, but same problem.  I can in fact do the computation completely in Sage (which I assume doesn't call numpy for matrix multiplication?) and get the same.  Note however that Sage CAN multiply correctly, as can Numpy:\n\n```\nsage: -0.35355339*5+0.35355339*5\n0.000000000000000\nsage: numpy.int(5)*numpy.float(-0.35355339)+numpy.int(5)*numpy.float(0.35355339)\n0.0\n```\n\nSo somehow it has to do with our matrix multiplication algorithm and how it works on PPC.  Perhaps there are other nasty bugs lurking as yet unseen.  Any thoughts?",
    "created_at": "2009-10-28T14:59:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7276#issuecomment-60547",
    "user": "kcrisman"
}
```

Here is the code for integral_elements_in_box line by line, up to the first place where PPC differs from Intel:

```
sage: K.<alpha> = NumberField(x^2-2)
sage: d = K.degree()
sage: Z_F = K.maximal_order()
sage: Foo = K.real_embeddings()
sage: B = K.reduced_basis()
sage: import numpy
sage: import numpy.linalg
sage: L = numpy.array([ [v(b) for b in B] for v in Foo])
sage: Linv = numpy.linalg.inv(L)
sage: C = [[0,5],[0,5]]
sage: Vi = [[C[0][0]],[C[0][1]]]
sage: 
sage: Linv

array([[ 0.5       ,  0.5       ],
       [-0.35355339,  0.35355339]])
sage: for i in range(1,d):
....:     Vi = sum([ [v + [C[i][0]], v + [C[i][1]]] for v in Vi], [])
....:     
sage: Vi
[[0, 0], [0, 5], [5, 0], [5, 5]]
sage: V = numpy.matrix(Linv)*(numpy.matrix(Vi).transpose())
sage: V

matrix([[  0.00000000e+00,   2.50000000e+00,   2.50000000e+00,
           5.00000000e+00],
        [  0.00000000e+00,   1.76776695e+00,  -1.76776695e+00,
           5.55111512e-17]])
```

In particular, the matrices Linv and Vi, even in their numpy versions, are still the same.  Essentially, on PPC (at least G4) the computation -0.35355339*5+0.35355339*5 is not (quite) zero, but on Intel it is.  On Intel we get the same stuff but with just 0., 2.5, etc - and the last entry is 0., no hint of the 5.55e-17.  

Anyway, this leads to the following error (since we are depending on the ceil of zero to be zero, but the ceil of 5.55e-17 is 1):

```
sage: while j < 2**d:
    for i in range(d):
        if V[i,j] < V[i,j+1]:
            V[i,j] = math.floor(V[i,j])
            V[i,j+1] = math.ceil(V[i,j+1])
        else:
            V[i,j] = math.ceil(V[i,j])
            V[i,j+1] = math.floor(V[i,j+1])
    j +=2
....:         
sage: V

matrix([[ 0.,  3.,  2.,  5.],
        [ 0.,  2., -2.,  1.]])
```

Where Intel correctly gives 0. in the last entry.

Just so that it's clear that PPC is the issue:

```
sage: matrix(Linv)*matrix(Vi).transpose()

[              0.0               2.5               2.5               5.0]
[              0.0     1.76776695297    -1.76776695297 5.55111512313e-17]
```

Slightly more digits, but same problem.  I can in fact do the computation completely in Sage (which I assume doesn't call numpy for matrix multiplication?) and get the same.  Note however that Sage CAN multiply correctly, as can Numpy:

```
sage: -0.35355339*5+0.35355339*5
0.000000000000000
sage: numpy.int(5)*numpy.float(-0.35355339)+numpy.int(5)*numpy.float(0.35355339)
0.0
```

So somehow it has to do with our matrix multiplication algorithm and how it works on PPC.  Perhaps there are other nasty bugs lurking as yet unseen.  Any thoughts?



---

archive/issue_comments_060548.json:
```json
{
    "body": "The file \"devel/sage/sage/rings/number_field/totallyreal_rel.py\" has five functions, and only three of these have doctests. The problem in this ticket is with one these, which is an internal function not used elsewhere. From what I guess from the code, it is meant to be called with \"inexact\" bounds --- see the use of \"eps_global\".\n\nSo we might \"heal\" this internal function by using some kind of interval technique --- but the price could be high, i.e. slowing down the algorithm where this internal function is intended to be used.\n\nI rather propose to heal the doctest by giving bounds [-0.1, 5.1] ... instead of [0, 5] ..., which most probably is far closer to the actual intended usage than the current doctest.",
    "created_at": "2009-10-28T22:54:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7276#issuecomment-60548",
    "user": "GeorgSWeber"
}
```

The file "devel/sage/sage/rings/number_field/totallyreal_rel.py" has five functions, and only three of these have doctests. The problem in this ticket is with one these, which is an internal function not used elsewhere. From what I guess from the code, it is meant to be called with "inexact" bounds --- see the use of "eps_global".

So we might "heal" this internal function by using some kind of interval technique --- but the price could be high, i.e. slowing down the algorithm where this internal function is intended to be used.

I rather propose to heal the doctest by giving bounds [-0.1, 5.1] ... instead of [0, 5] ..., which most probably is far closer to the actual intended usage than the current doctest.



---

archive/issue_comments_060549.json:
```json
{
    "body": "Just for the record, can you clarify where that is called in integral_elements_in_box?   Especially since Linv and Vi are the same on PPC and Intel, but not the matrix multiplication, which is what integral_elements_in_box uses?   \n\nHowever, if you can explain that, I agree that (assuming the inexact bounds is correct) fixing the doctest in this way is okay.\n\nOr are you saying that there is more than one problem?  The documentation for one of the other functions does note platform-dependence, so certainly the author knew this.  You might want to email him as well, unfortunately I am not a number field expert so can't identify it further.",
    "created_at": "2009-10-29T14:35:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7276#issuecomment-60549",
    "user": "kcrisman"
}
```

Just for the record, can you clarify where that is called in integral_elements_in_box?   Especially since Linv and Vi are the same on PPC and Intel, but not the matrix multiplication, which is what integral_elements_in_box uses?   

However, if you can explain that, I agree that (assuming the inexact bounds is correct) fixing the doctest in this way is okay.

Or are you saying that there is more than one problem?  The documentation for one of the other functions does note platform-dependence, so certainly the author knew this.  You might want to email him as well, unfortunately I am not a number field expert so can't identify it further.



---

archive/issue_comments_060550.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-11-06T15:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7276#issuecomment-60550",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_060551.json:
```json
{
    "body": "This is also broken on Itanium.  This *MUST* get fixed -- so I'm promoting this to blocker.  We either remove offending code or fix the bug. \n\n```\nsage -t  \"devel/sage/sage/rings/number_field/totallyreal_rel.py\"\n**********************************************************************\nFile \"/home/wstein/screen/cleo/build/sage-4.2/devel/sage/sage/rings/number_field/totallyreal_rel.py\", line 48:\n    sage: sorted([str(a) for a in v])\nExpected:\n    ['-alpha + 2', '-alpha + 3', '0', '1', '2', '3', '4', '5', 'alpha + 2', 'alpha + 3']\nGot:\n    ['-alpha + 2', '-alpha + 3', '0', '1', '2', '3', '4', 'alpha + 2', 'alpha + 3']\n**********************************************************************\n1 items had failures:\n   1 of   8 in __main__.example_1\n```\n",
    "created_at": "2009-11-06T15:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7276#issuecomment-60551",
    "user": "was"
}
```

This is also broken on Itanium.  This *MUST* get fixed -- so I'm promoting this to blocker.  We either remove offending code or fix the bug. 

```
sage -t  "devel/sage/sage/rings/number_field/totallyreal_rel.py"
**********************************************************************
File "/home/wstein/screen/cleo/build/sage-4.2/devel/sage/sage/rings/number_field/totallyreal_rel.py", line 48:
    sage: sorted([str(a) for a in v])
Expected:
    ['-alpha + 2', '-alpha + 3', '0', '1', '2', '3', '4', '5', 'alpha + 2', 'alpha + 3']
Got:
    ['-alpha + 2', '-alpha + 3', '0', '1', '2', '3', '4', 'alpha + 2', 'alpha + 3']
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_1
```




---

archive/issue_comments_060552.json:
```json
{
    "body": "William, can you try \n\n```\nsage: K.<alpha> = NumberField(x^2-2)\nsage: d = K.degree()\nsage: Z_F = K.maximal_order()\nsage: Foo = K.real_embeddings()\nsage: B = K.reduced_basis()\nsage: import numpy\nsage: import numpy.linalg\nsage: L = numpy.array([ [v(b) for b in B] for v in Foo])\nsage: Linv = numpy.linalg.inv(L)\nsage: C = [[0,5],[0,5]]\nsage: Vi = [[C[0][0]],[C[0][1]]]\nsage: Linv # should be array([[ 0.5       ,  0.5       ],       [-0.35355339,  0.35355339]])\nsage: for i in range(1,d):\n....:     Vi = sum([ [v + [C[i][0]], v + [C[i][1]]] for v in Vi], [])\n....:     \nsage: Vi # should be [[0, 0], [0, 5], [5, 0], [5, 5]]\nsage: V = numpy.matrix(Linv)*(numpy.matrix(Vi).transpose())\nsage: V # should be matrix([[  0.00000000e+00,   2.50000000e+00,   2.50000000e+00,           5.00000000e+00],        [  0.00000000e+00,   1.76776695e+00,  -1.76776695e+00,           0.00000000e+00]]) but isn't on PPC, last element is e-17\nsage: matrix(Linv)*matrix(Vi).transpose() # should be [              0.0               2.5               2.5               5.0] [              0.0     1.76776695297    -1.76776695297           0.0] but isn't on PPC\n```\n \non cleo to see if (one of the) problem(s) there is also in matrix multiplication on itanium?   Just to clarify, at least one problem is that ceil(0)=0 but ceil(epsilon)=1.",
    "created_at": "2009-11-06T15:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7276#issuecomment-60552",
    "user": "kcrisman"
}
```

William, can you try 

```
sage: K.<alpha> = NumberField(x^2-2)
sage: d = K.degree()
sage: Z_F = K.maximal_order()
sage: Foo = K.real_embeddings()
sage: B = K.reduced_basis()
sage: import numpy
sage: import numpy.linalg
sage: L = numpy.array([ [v(b) for b in B] for v in Foo])
sage: Linv = numpy.linalg.inv(L)
sage: C = [[0,5],[0,5]]
sage: Vi = [[C[0][0]],[C[0][1]]]
sage: Linv # should be array([[ 0.5       ,  0.5       ],       [-0.35355339,  0.35355339]])
sage: for i in range(1,d):
....:     Vi = sum([ [v + [C[i][0]], v + [C[i][1]]] for v in Vi], [])
....:     
sage: Vi # should be [[0, 0], [0, 5], [5, 0], [5, 5]]
sage: V = numpy.matrix(Linv)*(numpy.matrix(Vi).transpose())
sage: V # should be matrix([[  0.00000000e+00,   2.50000000e+00,   2.50000000e+00,           5.00000000e+00],        [  0.00000000e+00,   1.76776695e+00,  -1.76776695e+00,           0.00000000e+00]]) but isn't on PPC, last element is e-17
sage: matrix(Linv)*matrix(Vi).transpose() # should be [              0.0               2.5               2.5               5.0] [              0.0     1.76776695297    -1.76776695297           0.0] but isn't on PPC
```
 
on cleo to see if (one of the) problem(s) there is also in matrix multiplication on itanium?   Just to clarify, at least one problem is that ceil(0)=0 but ceil(epsilon)=1.



---

archive/issue_comments_060553.json:
```json
{
    "body": "The output on itanium (cleo) is exactly the same as on PPC above.  I.e., I get \"last element is e-17\".  \n\nSo is there a bug somewhere in the algorithm that assumes some floating point number is 0.0, but really it might just be epsilon sometimes, and this is revealed on PPC and Itanium. \n\nNOTE: Our PPC box is *big endian*.  Our Itanium is *little endian*.  So this is not just an endianess issue.",
    "created_at": "2009-11-10T05:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7276#issuecomment-60553",
    "user": "was"
}
```

The output on itanium (cleo) is exactly the same as on PPC above.  I.e., I get "last element is e-17".  

So is there a bug somewhere in the algorithm that assumes some floating point number is 0.0, but really it might just be epsilon sometimes, and this is revealed on PPC and Itanium. 

NOTE: Our PPC box is *big endian*.  Our Itanium is *little endian*.  So this is not just an endianess issue.



---

archive/issue_comments_060554.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-10T06:27:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7276#issuecomment-60554",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060555.json:
```json
{
    "body": "Attachment [trac_7276.patch](tarball://root/attachments/some-uuid/ticket7276/trac_7276.patch) by was created at 2009-11-10 06:27:25\n\nI have attached a patch that does what Georg suggested above.  I also added more doctests (i.e., a cubic example) to explain what the mysterius \"C\" is.   With this patch, doctests pass on ppc, itanium, and x86_64 now. \n\nI've also emailed John Voight asking him to get the docs of this file up to snuff.",
    "created_at": "2009-11-10T06:27:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7276#issuecomment-60555",
    "user": "was"
}
```

Attachment [trac_7276.patch](tarball://root/attachments/some-uuid/ticket7276/trac_7276.patch) by was created at 2009-11-10 06:27:25

I have attached a patch that does what Georg suggested above.  I also added more doctests (i.e., a cubic example) to explain what the mysterius "C" is.   With this patch, doctests pass on ppc, itanium, and x86_64 now. 

I've also emailed John Voight asking him to get the docs of this file up to snuff.



---

archive/issue_comments_060556.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-10T14:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7276#issuecomment-60556",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060557.json:
```json
{
    "body": "You're gonna love this... on Intel Mac 10.5:\n\n```\nnumber_field/totallyreal_rel.py\", line 76:\n    sage: sorted(v)\nExpected:\n    [-1/2*a + 2, 1/4*a^2 + 1/2*a, 0, 1, 2, 3, 4, -1/4*a^2 - 1/2*a + 5, 1/2*a + 3, -1/4*a^2 + 5]\nGot:\n    [-1/2*a + 2, 1/4*a^2 + 1/2*a, 0, 1, 2, 3, 4, 5, -1/4*a^2 - 1/2*a + 5, 1/2*a + 3, -1/4*a^2 + 5]\n```\n\nThis is from the cubic field example.\n\nAlso, probably it would be good to directly confirm that the original bugbear is fixed, at the end of the first doctest:\n\n```\nsage: C = [[0-eps,5+eps],[0-eps,5+eps]] \nsage: v = sage.rings.number_field.totallyreal_rel.integral_elements_in_box(K, C) \nsage: sorted(v) [-alpha + 2, -alpha + 3, 0, 1, 2, 3, 4, 5, alpha + 2, alpha + 3]\n```\n\n\nThe documentation clarifies things a lot, so +1 on that!",
    "created_at": "2009-11-10T14:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7276#issuecomment-60557",
    "user": "kcrisman"
}
```

You're gonna love this... on Intel Mac 10.5:

```
number_field/totallyreal_rel.py", line 76:
    sage: sorted(v)
Expected:
    [-1/2*a + 2, 1/4*a^2 + 1/2*a, 0, 1, 2, 3, 4, -1/4*a^2 - 1/2*a + 5, 1/2*a + 3, -1/4*a^2 + 5]
Got:
    [-1/2*a + 2, 1/4*a^2 + 1/2*a, 0, 1, 2, 3, 4, 5, -1/4*a^2 - 1/2*a + 5, 1/2*a + 3, -1/4*a^2 + 5]
```

This is from the cubic field example.

Also, probably it would be good to directly confirm that the original bugbear is fixed, at the end of the first doctest:

```
sage: C = [[0-eps,5+eps],[0-eps,5+eps]] 
sage: v = sage.rings.number_field.totallyreal_rel.integral_elements_in_box(K, C) 
sage: sorted(v) [-alpha + 2, -alpha + 3, 0, 1, 2, 3, 4, 5, alpha + 2, alpha + 3]
```


The documentation clarifies things a lot, so +1 on that!



---

archive/issue_comments_060558.json:
```json
{
    "body": "But all tests pass on PPC ;-)",
    "created_at": "2009-11-10T14:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7276#issuecomment-60558",
    "user": "kcrisman"
}
```

But all tests pass on PPC ;-)



---

archive/issue_comments_060559.json:
```json
{
    "body": "apply instead the first patch from William",
    "created_at": "2009-11-10T20:10:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7276#issuecomment-60559",
    "user": "GeorgSWeber"
}
```

apply instead the first patch from William



---

archive/issue_comments_060560.json:
```json
{
    "body": "Attachment [trac_7276_v2.patch](tarball://root/attachments/some-uuid/ticket7276/trac_7276_v2.patch) by GeorgSWeber created at 2009-11-10 20:35:24\n\nGrmpf.\n\nThe new patch version 2 tried to address the issues. In the cubic field example, the \"5\" should be in, so I enlarged the epsilon. This works \"as is\" on MacIntel OS X 10.4.11.\n\nHowever, the patch version 2 does *not* work on MacPPC OS X 10.4.11, so this ticket has to stay \"needs work\".",
    "created_at": "2009-11-10T20:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7276#issuecomment-60560",
    "user": "GeorgSWeber"
}
```

Attachment [trac_7276_v2.patch](tarball://root/attachments/some-uuid/ticket7276/trac_7276_v2.patch) by GeorgSWeber created at 2009-11-10 20:35:24

Grmpf.

The new patch version 2 tried to address the issues. In the cubic field example, the "5" should be in, so I enlarged the epsilon. This works "as is" on MacIntel OS X 10.4.11.

However, the patch version 2 does *not* work on MacPPC OS X 10.4.11, so this ticket has to stay "needs work".



---

archive/issue_comments_060561.json:
```json
{
    "body": "ignore georg's patch above.  apply trac_7276.patch and this.",
    "created_at": "2009-11-11T16:43:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7276#issuecomment-60561",
    "user": "was"
}
```

ignore georg's patch above.  apply trac_7276.patch and this.



---

archive/issue_comments_060562.json:
```json
{
    "body": "Attachment [trac_7276-part2.patch](tarball://root/attachments/some-uuid/ticket7276/trac_7276-part2.patch) by was created at 2009-11-11 16:43:28",
    "created_at": "2009-11-11T16:43:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7276#issuecomment-60562",
    "user": "was"
}
```

Attachment [trac_7276-part2.patch](tarball://root/attachments/some-uuid/ticket7276/trac_7276-part2.patch) by was created at 2009-11-11 16:43:28



---

archive/issue_comments_060563.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-11T16:43:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7276#issuecomment-60563",
    "user": "was"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060564.json:
```json
{
    "body": "Remark from John Voight:\n\"...what a mess!  I'm so sorry.  (Next time, feel free to contact\nme earlier if there are issues with my code that I can be of help\nwith.)\n\nThe algorithm used is described in\n http://www.cems.uvm.edu/~voight/articles/ANTS144.pdf\nin Section 3.1 (page 9), \"Lattice points in boxes\".  There is\nabsolutely a rounding issue which I can see as failing miserably in\nlow precision.  Off the top of my head, one might be able to fix the\nissue by replacing a ceiling with a floor + 1, or even a ceiling +\n1--but even then, this assumes the precision loss is so constrained...\n\nI won't have a chance to work on the doctest until the weekend, but\nit's in my queue now.\n\nJV\"",
    "created_at": "2009-11-11T17:03:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7276#issuecomment-60564",
    "user": "was"
}
```

Remark from John Voight:
"...what a mess!  I'm so sorry.  (Next time, feel free to contact
me earlier if there are issues with my code that I can be of help
with.)

The algorithm used is described in
 http://www.cems.uvm.edu/~voight/articles/ANTS144.pdf
in Section 3.1 (page 9), "Lattice points in boxes".  There is
absolutely a rounding issue which I can see as failing miserably in
low precision.  Off the top of my head, one might be able to fix the
issue by replacing a ceiling with a floor + 1, or even a ceiling +
1--but even then, this assumes the precision loss is so constrained...

I won't have a chance to work on the doctest until the weekend, but
it's in my queue now.

JV"



---

archive/issue_comments_060565.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-11T20:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7276#issuecomment-60565",
    "user": "GeorgSWeber"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060566.json:
```json
{
    "body": "Tested positively on both MacIntel OS X 10.4 and MacPPC OS X 10.4 (apply the original patch and the \"part2\" patch, both from William; do ignore my \"v2\" patch).",
    "created_at": "2009-11-11T20:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7276#issuecomment-60566",
    "user": "GeorgSWeber"
}
```

Tested positively on both MacIntel OS X 10.4 and MacPPC OS X 10.4 (apply the original patch and the "part2" patch, both from William; do ignore my "v2" patch).



---

archive/issue_comments_060567.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-12T06:09:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7276#issuecomment-60567",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_060568.json:
```json
{
    "body": "See #7649 for a followup ticket.",
    "created_at": "2009-12-10T01:25:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7276#issuecomment-60568",
    "user": "was"
}
```

See #7649 for a followup ticket.
