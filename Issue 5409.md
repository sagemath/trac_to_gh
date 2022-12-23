# Issue 5409: rewrite quaternion algebras -- the current implementation isn't sufficiently good

archive/issues_005409.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  bober\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5409\n\n",
    "created_at": "2009-03-01T06:57:40Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "title": "rewrite quaternion algebras -- the current implementation isn't sufficiently good",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5409",
    "user": "was"
}
```
Assignee: tbd

CC:  bober



Issue created by migration from https://trac.sagemath.org/ticket/5409





---

archive/issue_comments_041805.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-03-01T07:56:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41805",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_041806.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-03-01T22:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41806",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_041807.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-03-02T08:35:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41807",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_041808.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-03-02T09:44:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41808",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_041809.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-03-02T09:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41809",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_041810.json:
```json
{
    "body": "Some issues doctesting against my 3.4.rc0 merge tree\n\n```\n\tsage -t  devel/sage/sage/quadratic_forms/special_values.py # 4 doctests failed\n\tsage -t  devel/sage/sage/quadratic_forms/quadratic_form__siegel_product.py # 8 doctests failed\n\tsage -t  devel/sage/sage/rings/ring.pyx # 1 doctests failed\n\tsage -t  devel/sage/sage/structure/sage_object.pyx # 1 doctests failed\n\tsage -t  devel/sage/sage/modular/dirichlet.py # 4 doctests failed\n\tsage -t  devel/sage/sage/quadratic_forms/quadratic_form__mass__Siegel_densities.py # 2 doctests failed\n\tsage -t  devel/sage/sage/quadratic_forms/quadratic_form__mass__Conway_Sloane_masses.py # 1 doctests failed\n\tsage -t  devel/sage/sage/interfaces/magma.py # 1 doctests failed\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T18:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41810",
    "user": "mabshoff"
}
```

Some issues doctesting against my 3.4.rc0 merge tree

```
	sage -t  devel/sage/sage/quadratic_forms/special_values.py # 4 doctests failed
	sage -t  devel/sage/sage/quadratic_forms/quadratic_form__siegel_product.py # 8 doctests failed
	sage -t  devel/sage/sage/rings/ring.pyx # 1 doctests failed
	sage -t  devel/sage/sage/structure/sage_object.pyx # 1 doctests failed
	sage -t  devel/sage/sage/modular/dirichlet.py # 4 doctests failed
	sage -t  devel/sage/sage/quadratic_forms/quadratic_form__mass__Siegel_densities.py # 2 doctests failed
	sage -t  devel/sage/sage/quadratic_forms/quadratic_form__mass__Conway_Sloane_masses.py # 1 doctests failed
	sage -t  devel/sage/sage/interfaces/magma.py # 1 doctests failed
```


Cheers,

Michael



---

archive/issue_comments_041811.json:
```json
{
    "body": "Replying to [comment:2 mabshoff]:\nI can fix all the doctest failures except\n\n```\n \tsage -t  devel/sage/sage/structure/sage_object.pyx # 1 doctests failed\n```\n\nwhich I don't know how to deal with.\n\nThe fix is two one-liners on top of part6\n\n```\ndiff -r 311c05f56282 sage/rings/arith.py\n--- a/sage/rings/arith.py       Mon Mar 02 04:52:16 2009 -0500\n+++ b/sage/rings/arith.py       Mon Mar 02 10:20:29 2009 -0800\n@@ -3964,6 +3964,7 @@\n     1, mod 4, and such that, at most, the only square dividing it is\n     4.\n     \"\"\"\n+    from sage.rings.all import Integer\n     D = Integer(D)\n     D = D.squarefree_part()\n     if D%4 == 1:\ndiff -r 311c05f56282 sage/rings/ring.pyx\n--- a/sage/rings/ring.pyx       Mon Mar 02 04:52:16 2009 -0500\n+++ b/sage/rings/ring.pyx       Mon Mar 02 10:20:29 2009 -0800\n@@ -735,7 +735,7 @@\n             sage: ZpCA(7).is_commutative()\n             True\n             sage: A = QuaternionAlgebra(QQ, -1, -3, names=('i','j','k')); A\n-            Quaternion algebra with generators (i, j, k) over Rational Field\n+            Quaternion Algebra (-1, -3) with base ring Rational Field\n             sage: A.is_commutative()\n             False\n         \"\"\"\n```\n",
    "created_at": "2009-03-02T18:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41811",
    "user": "tornaria"
}
```

Replying to [comment:2 mabshoff]:
I can fix all the doctest failures except

```
 	sage -t  devel/sage/sage/structure/sage_object.pyx # 1 doctests failed
```

which I don't know how to deal with.

The fix is two one-liners on top of part6

```
diff -r 311c05f56282 sage/rings/arith.py
--- a/sage/rings/arith.py       Mon Mar 02 04:52:16 2009 -0500
+++ b/sage/rings/arith.py       Mon Mar 02 10:20:29 2009 -0800
@@ -3964,6 +3964,7 @@
     1, mod 4, and such that, at most, the only square dividing it is
     4.
     """
+    from sage.rings.all import Integer
     D = Integer(D)
     D = D.squarefree_part()
     if D%4 == 1:
diff -r 311c05f56282 sage/rings/ring.pyx
--- a/sage/rings/ring.pyx       Mon Mar 02 04:52:16 2009 -0500
+++ b/sage/rings/ring.pyx       Mon Mar 02 10:20:29 2009 -0800
@@ -735,7 +735,7 @@
             sage: ZpCA(7).is_commutative()
             True
             sage: A = QuaternionAlgebra(QQ, -1, -3, names=('i','j','k')); A
-            Quaternion algebra with generators (i, j, k) over Rational Field
+            Quaternion Algebra (-1, -3) with base ring Rational Field
             sage: A.is_commutative()
             False
         """
```




---

archive/issue_comments_041812.json:
```json
{
    "body": "Attachment\n\nreview patch -- fix doctests except for pickle jar",
    "created_at": "2009-03-02T18:29:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41812",
    "user": "tornaria"
}
```

Attachment

review patch -- fix doctests except for pickle jar



---

archive/issue_comments_041813.json:
```json
{
    "body": "Caching of quaternion algebras seems to be broken:\n\n```\nsage: QuaternionAlgebra(GF(5)(2),GF(5)(3))\nQuaternion Algebra (2, 3) with base ring Finite Field of size 5\nsage: QuaternionAlgebra(2,3)\nQuaternion Algebra (2, 3) with base ring Finite Field of size 5\n```\n\n\nThe second time we should have constructed\n\n```\nQuaternion Algebra (2, 3) with base ring Rational Field\n```\n",
    "created_at": "2009-03-02T19:00:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41813",
    "user": "tornaria"
}
```

Caching of quaternion algebras seems to be broken:

```
sage: QuaternionAlgebra(GF(5)(2),GF(5)(3))
Quaternion Algebra (2, 3) with base ring Finite Field of size 5
sage: QuaternionAlgebra(2,3)
Quaternion Algebra (2, 3) with base ring Finite Field of size 5
```


The second time we should have constructed

```
Quaternion Algebra (2, 3) with base ring Rational Field
```




---

archive/issue_comments_041814.json:
```json
{
    "body": "Attachment\n\nfix caching",
    "created_at": "2009-03-02T19:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41814",
    "user": "was"
}
```

Attachment

fix caching



---

archive/issue_comments_041815.json:
```json
{
    "body": "Found a couple of issues with vector_space():\na. I didn't find a way to map vectors between the quaternion algebra and the vector space\nb. neither the norm or the inner_product in the vector space seem to match the norm in the quaternion algebra\n\n```\nsage: Q1 = QuaternionAlgebra(2,3)\n(reverse-i-search)`V1': V1\nKeyboardInterrupt\nsage: V1 = Q1.vector_space()\nsage: q = Q1([1,2,3,4])\nsage: v = V1(q)\n...\nTypeError: can't initialize vector from nonzero non-list\nsage: v = V1([1,2,3,4])\nsage: Q1(v)\n...\nTypeError: Unable to coerce (1, 2, 3, 4) (<type 'sage.modules.vector_rational_dense.Vector_rational_dense'>) to Rational\nsage: q.norm()\n62\nsage: v.norm()\nsqrt(30)\nsage: v.inner_product(v)\n124\n```\n",
    "created_at": "2009-03-02T20:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41815",
    "user": "tornaria"
}
```

Found a couple of issues with vector_space():
a. I didn't find a way to map vectors between the quaternion algebra and the vector space
b. neither the norm or the inner_product in the vector space seem to match the norm in the quaternion algebra

```
sage: Q1 = QuaternionAlgebra(2,3)
(reverse-i-search)`V1': V1
KeyboardInterrupt
sage: V1 = Q1.vector_space()
sage: q = Q1([1,2,3,4])
sage: v = V1(q)
...
TypeError: can't initialize vector from nonzero non-list
sage: v = V1([1,2,3,4])
sage: Q1(v)
...
TypeError: Unable to coerce (1, 2, 3, 4) (<type 'sage.modules.vector_rational_dense.Vector_rational_dense'>) to Rational
sage: q.norm()
62
sage: v.norm()
sqrt(30)
sage: v.inner_product(v)
124
```




---

archive/issue_comments_041816.json:
```json
{
    "body": "Attachment\n\nWe didn't do quat alg from discriminants for number fields yet.   I'm going to also get rid of \"norm\" and \"trace\" and just have \"reduced_norm\" and \"reduced_trace\" since even Gonzalo clearly got confused by having both and an alias.",
    "created_at": "2009-03-04T04:46:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41816",
    "user": "was"
}
```

Attachment

We didn't do quat alg from discriminants for number fields yet.   I'm going to also get rid of "norm" and "trace" and just have "reduced_norm" and "reduced_trace" since even Gonzalo clearly got confused by having both and an alias.



---

archive/issue_comments_041817.json:
```json
{
    "body": "get rid of \"norm\" and \"trace\" -- this confused gonzalo; now have only reduced norm and trace!",
    "created_at": "2009-03-04T07:17:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41817",
    "user": "was"
}
```

get rid of "norm" and "trace" -- this confused gonzalo; now have only reduced norm and trace!



---

archive/issue_comments_041818.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-03-04T08:23:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41818",
    "user": "bober"
}
```

Attachment



---

archive/issue_comments_041819.json:
```json
{
    "body": "Bug fixes and doctests",
    "created_at": "2009-03-04T19:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41819",
    "user": "jvoight"
}
```

Bug fixes and doctests



---

archive/issue_comments_041820.json:
```json
{
    "body": "Attachment\n\nI got it to patch correctly against 3.4.rc0.  I found some bugs and added a few doctests.  Partial positive review.  JV",
    "created_at": "2009-03-04T19:56:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41820",
    "user": "jvoight"
}
```

Attachment

I got it to patch correctly against 3.4.rc0.  I found some bugs and added a few doctests.  Partial positive review.  JV



---

archive/issue_comments_041821.json:
```json
{
    "body": "I found a few issues with jvoight's referee patch, which I'm noting here:\n\n* In inner_product_matrix the docs say: \"The standard basis 1, i, j, k is orthogonal, so this matrix is just the diagonal matrix with diagonal entries 1, a, b, a*b.\"  In the code, though, it's 2,2*a,2*b,2*a*b.  \n\n* Line 475 is:\n\n\"and j*i=-i*j.  K is a field not of characteristic and a,b are nonzero elements of K\"\n\nbut it should say \"and j*i=-i*j.  K is a field not of characteristic 2 and a,b are nonzero elements of K\"  (the missing 2).\n\nOtherwise the referee patch from jvoight looks very very good!",
    "created_at": "2009-03-04T20:35:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41821",
    "user": "was"
}
```

I found a few issues with jvoight's referee patch, which I'm noting here:

* In inner_product_matrix the docs say: "The standard basis 1, i, j, k is orthogonal, so this matrix is just the diagonal matrix with diagonal entries 1, a, b, a*b."  In the code, though, it's 2,2*a,2*b,2*a*b.  

* Line 475 is:

"and j*i=-i*j.  K is a field not of characteristic and a,b are nonzero elements of K"

but it should say "and j*i=-i*j.  K is a field not of characteristic 2 and a,b are nonzero elements of K"  (the missing 2).

Otherwise the referee patch from jvoight looks very very good!



---

archive/issue_comments_041822.json:
```json
{
    "body": "Great, so then this gets a positive review from me, too.  I tried a few things out and the multiplication, and this last doctest might be useful (to test cpdef RingElement _mul_), but maybe there's enough already.\n\n\n```\n            sage: K.<x> = QQ[]\n            sage: Q_ab = QuaternionAlgebra(Frac(K), 17, -3)\n            sage: Q = QuaternionAlgebra(17, -3)\n            sage: for t in xrange(100):\n            sage:     v1 = [ZZ.random_element() for i in range(4)]\n            sage:     v2 = [ZZ.random_element() for i in range(4)]\n            sage:     if list(Q(v1)*Q(v2)) <> list(Q_ab(v1)*Q_ab(v2)):\n            sage:         print \"Multiplication is inconsistent\", v1, v2\n```\n",
    "created_at": "2009-03-05T00:17:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41822",
    "user": "jvoight"
}
```

Great, so then this gets a positive review from me, too.  I tried a few things out and the multiplication, and this last doctest might be useful (to test cpdef RingElement _mul_), but maybe there's enough already.


```
            sage: K.<x> = QQ[]
            sage: Q_ab = QuaternionAlgebra(Frac(K), 17, -3)
            sage: Q = QuaternionAlgebra(17, -3)
            sage: for t in xrange(100):
            sage:     v1 = [ZZ.random_element() for i in range(4)]
            sage:     v2 = [ZZ.random_element() for i in range(4)]
            sage:     if list(Q(v1)*Q(v2)) <> list(Q_ab(v1)*Q_ab(v2)):
            sage:         print "Multiplication is inconsistent", v1, v2
```




---

archive/issue_comments_041823.json:
```json
{
    "body": "If I read this correctly the last two suggestions by William still need to be fixed in John's patch. \n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2009-03-10T16:57:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41823",
    "user": "mabshoff"
}
```

If I read this correctly the last two suggestions by William still need to be fixed in John's patch. 

Thoughts?

Cheers,

Michael



---

archive/issue_comments_041824.json:
```json
{
    "body": "Besides the known pickle issue John's patch breaks two more doctests:\n\n```\nsage -t -long devel/sage/sage/structure/sage_object.pyx # 1 doctests failed\nsage -t -long devel/sage/sage/algebras/quaternion_algebra.py # 8 doctests failed\nsage -t -long devel/sage/sage/algebras/quaternion_algebra_element.pyx # 1 doctests failed\n```\n\nIn detail:\n\n```\nsage -t -long \"devel/sage/sage/algebras/quaternion_algebra_element.pyx\"\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.rc2/devel/sage/sage/algebras/quaternion_algebra_element.pyx\", line 322:\n    sage: 1/Q(0)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-3.4.rc2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.4.rc2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.4.rc2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_11[6]>\", line 1, in <module>\n        Integer(1)/Q(Integer(0))###line 322:\n    sage: 1/Q(0)\n      File \"element.pyx\", line 1238, in sage.structure.element.RingElement.__div__ (sage/structure/element.c:9116)\n      File \"coerce.pyx\", line 712, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:5438)\n      File \"element.pyx\", line 1236, in sage.structure.element.RingElement.__div__ (sage/structure/element.c:9099)\n      File \"quaternion_algebra_element.pyx\", line 362, in sage.algebras.quaternion_algebra_element.QuaternionAlgebraElement_abstract._div_ (sage/algebras/quaternion_algebra_element.cpp:5726)\n      File \"quaternion_algebra_element.pyx\", line 346, in sage.algebras.quaternion_algebra_element.QuaternionAlgebraElement_abstract.__invert__ (sage/algebras/quaternion_algebra_element.cpp:5660)\n      File \"rational.pyx\", line 1445, in sage.rings.rational.Rational.__invert__ (sage/rings/rational.c:10565)\n    ZeroDivisionError: rational division by zero\n**********************************************************************\n```\n\nand\n\n```\nsage -t -long \"devel/sage/sage/algebras/quaternion_algebra.py\"\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.rc2/devel/sage/sage/algebras/quaternion_algebra.py\", line 89:\n    sage: QuaternionAlgebra(0,0)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-3.4.rc2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.4.rc2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.4.rc2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[7]>\", line 1, in <module>\n        QuaternionAlgebra(Integer(0),Integer(0))###line 89:\n    sage: QuaternionAlgebra(0,0)\n      File \"/scratch/mabshoff/sage-3.4.rc2/local/lib/python2.5/site-packages/sage/algebras/quaternion_algebra.py\", line 175, in QuaternionAlgebra\n        raise ValueError, \"a and b must be nonzero\"\n    ValueError: a and b must be nonzero\n**********************************************************************\n<SNIP>\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-03-10T18:01:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41824",
    "user": "mabshoff"
}
```

Besides the known pickle issue John's patch breaks two more doctests:

```
sage -t -long devel/sage/sage/structure/sage_object.pyx # 1 doctests failed
sage -t -long devel/sage/sage/algebras/quaternion_algebra.py # 8 doctests failed
sage -t -long devel/sage/sage/algebras/quaternion_algebra_element.pyx # 1 doctests failed
```

In detail:

```
sage -t -long "devel/sage/sage/algebras/quaternion_algebra_element.pyx"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.rc2/devel/sage/sage/algebras/quaternion_algebra_element.pyx", line 322:
    sage: 1/Q(0)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.4.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_11[6]>", line 1, in <module>
        Integer(1)/Q(Integer(0))###line 322:
    sage: 1/Q(0)
      File "element.pyx", line 1238, in sage.structure.element.RingElement.__div__ (sage/structure/element.c:9116)
      File "coerce.pyx", line 712, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:5438)
      File "element.pyx", line 1236, in sage.structure.element.RingElement.__div__ (sage/structure/element.c:9099)
      File "quaternion_algebra_element.pyx", line 362, in sage.algebras.quaternion_algebra_element.QuaternionAlgebraElement_abstract._div_ (sage/algebras/quaternion_algebra_element.cpp:5726)
      File "quaternion_algebra_element.pyx", line 346, in sage.algebras.quaternion_algebra_element.QuaternionAlgebraElement_abstract.__invert__ (sage/algebras/quaternion_algebra_element.cpp:5660)
      File "rational.pyx", line 1445, in sage.rings.rational.Rational.__invert__ (sage/rings/rational.c:10565)
    ZeroDivisionError: rational division by zero
**********************************************************************
```

and

```
sage -t -long "devel/sage/sage/algebras/quaternion_algebra.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.rc2/devel/sage/sage/algebras/quaternion_algebra.py", line 89:
    sage: QuaternionAlgebra(0,0)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.4.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[7]>", line 1, in <module>
        QuaternionAlgebra(Integer(0),Integer(0))###line 89:
    sage: QuaternionAlgebra(0,0)
      File "/scratch/mabshoff/sage-3.4.rc2/local/lib/python2.5/site-packages/sage/algebras/quaternion_algebra.py", line 175, in QuaternionAlgebra
        raise ValueError, "a and b must be nonzero"
    ValueError: a and b must be nonzero
**********************************************************************
<SNIP>
```


Cheers,

Michael



---

archive/issue_comments_041825.json:
```json
{
    "body": "Ok, this fixes the first problem:\n\n```\ndiff -r c0c80b6d1261 sage/algebras/quaternion_algebra_element.pyx\n--- a/sage/algebras/quaternion_algebra_element.pyx      Wed Mar 04 11:54:38 2009 -0800\n+++ b/sage/algebras/quaternion_algebra_element.pyx      Tue Mar 10 11:51:54 2009 -0700\n@@ -320,6 +320,7 @@\n             sage: type(theta)\n             <type 'sage.algebras.quaternion_algebra_element.QuaternionAlgebraElement_rational_field'>\n             sage: 1/Q(0)\n+            Traceback (most recent call last):\n             ...\n             ZeroDivisionError: rational division by zero\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-03-10T18:52:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41825",
    "user": "mabshoff"
}
```

Ok, this fixes the first problem:

```
diff -r c0c80b6d1261 sage/algebras/quaternion_algebra_element.pyx
--- a/sage/algebras/quaternion_algebra_element.pyx      Wed Mar 04 11:54:38 2009 -0800
+++ b/sage/algebras/quaternion_algebra_element.pyx      Tue Mar 10 11:51:54 2009 -0700
@@ -320,6 +320,7 @@
             sage: type(theta)
             <type 'sage.algebras.quaternion_algebra_element.QuaternionAlgebraElement_rational_field'>
             sage: 1/Q(0)
+            Traceback (most recent call last):
             ...
             ZeroDivisionError: rational division by zero
```


Cheers,

Michael



---

archive/issue_comments_041826.json:
```json
{
    "body": "trac_5409-part12-reviewer.patch makes the doctest pass again. It is only a diff since I did not want to commit anything to that tree. Most of the changes are trivial. Mike Hansen also pointed out some of the fixes :)\n\nI am somehow under the impression John's patch was not the final one or somehow incomplete.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-10T19:14:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41826",
    "user": "mabshoff"
}
```

trac_5409-part12-reviewer.patch makes the doctest pass again. It is only a diff since I did not want to commit anything to that tree. Most of the changes are trivial. Mike Hansen also pointed out some of the fixes :)

I am somehow under the impression John's patch was not the final one or somehow incomplete.

Cheers,

Michael



---

archive/issue_comments_041827.json:
```json
{
    "body": "positive review (I fixed the other two small mistakes from John Voight's patch in Mabshoff's tree).",
    "created_at": "2009-03-10T19:41:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41827",
    "user": "was"
}
```

positive review (I fixed the other two small mistakes from John Voight's patch in Mabshoff's tree).



---

archive/issue_comments_041828.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-03-10T19:46:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41828",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_041829.json:
```json
{
    "body": "Merged 12 patches in Sage 3.4.final.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-10T19:52:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41829",
    "user": "mabshoff"
}
```

Merged 12 patches in Sage 3.4.final.

Cheers,

Michael



---

archive/issue_comments_041830.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-10T19:52:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5409#issuecomment-41830",
    "user": "mabshoff"
}
```

Resolution: fixed
