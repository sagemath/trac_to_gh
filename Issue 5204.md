# Issue 5204: [with new patch, positive review] simon_two_descent -- bug in the interface when number field has variable name 'x'

archive/issues_005204.json:
```json
{
    "body": "Assignee: @williamstein\n\n1. A basic bug in the wrapper, which is probably easy to fix:\n\n```\nsage: E = EllipticCurve('8320e1').change_ring(QuadraticField(-191,'x'))\nsage: E.simon_two_descent()\nTraceback (most recent call last):\n...\n---> 98     ans = sage_eval(v, {'Mod': _gp_mod, 'y': K.gen(0)})\nNameError: name 'ans' is not defined\n```\n\nThe problem is my choice of 'x' as generator name for the number field.  The fix is to always change the variable of the base number field to 'a' before feeding anything to pari.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5204\n\n",
    "closed_at": "2009-03-24T23:16:07Z",
    "created_at": "2009-02-08T05:37:04Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with new patch, positive review] simon_two_descent -- bug in the interface when number field has variable name 'x'",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5204",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

1. A basic bug in the wrapper, which is probably easy to fix:

```
sage: E = EllipticCurve('8320e1').change_ring(QuadraticField(-191,'x'))
sage: E.simon_two_descent()
Traceback (most recent call last):
...
---> 98     ans = sage_eval(v, {'Mod': _gp_mod, 'y': K.gen(0)})
NameError: name 'ans' is not defined
```

The problem is my choice of 'x' as generator name for the number field.  The fix is to always change the variable of the base number field to 'a' before feeding anything to pari.


Issue created by migration from https://trac.sagemath.org/ticket/5204





---

archive/issue_comments_039794.json:
```json
{
    "body": "Attachment [trac_5204.patch](tarball://root/attachments/some-uuid/ticket5204/trac_5204.patch) by @rlmill created at 2009-02-10 20:49:24",
    "created_at": "2009-02-10T20:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5204#issuecomment-39794",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_5204.patch](tarball://root/attachments/some-uuid/ticket5204/trac_5204.patch) by @rlmill created at 2009-02-10 20:49:24



---

archive/issue_comments_039795.json:
```json
{
    "body": "Apply after previous",
    "created_at": "2009-02-15T17:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5204#issuecomment-39795",
    "user": "https://github.com/JohnCremona"
}
```

Apply after previous



---

archive/issue_comments_039796.json:
```json
{
    "body": "Attachment [trac_5204-a.patch](tarball://root/attachments/some-uuid/ticket5204/trac_5204-a.patch) by @JohnCremona created at 2009-02-15 17:40:22\n\nReview:  I can only deduce that rlm did not actually test this!\n\n```\nsage -t  \"devel/sage-5204/sage/schemes/elliptic_curves/gp_simon.py\"\n**********************************************************************\nFile \"/home/john/sage-3.3.rc0/devel/sage-5204/sage/schemes/elliptic_curves/gp_simon.py\", line 54:\n    sage: sage.schemes.elliptic_curves.gp_simon.simon_two_descent(E)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/john/sage-3.3.rc0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/john/sage-3.3.rc0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/john/sage-3.3.rc0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[4]>\", line 1, in <module>\n        sage.schemes.elliptic_curves.gp_simon.simon_two_descent(E)###line 54:\n    sage: sage.schemes.elliptic_curves.gp_simon.simon_two_descent(E)\n      File \"/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/gp_simon.py\", line 69, in simon_two_descent\n        K = E.base_ring().change_names('a')\n    AttributeError: 'RationalField' object has no attribute 'change_names'\n**********************************************************************\nFile \"/home/john/sage-3.3.rc0/devel/sage-5204/sage/schemes/elliptic_curves/gp_simon.py\", line 56:\n    sage: E.simon_two_descent()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/john/sage-3.3.rc0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/john/sage-3.3.rc0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/john/sage-3.3.rc0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[5]>\", line 1, in <module>\n        E.simon_two_descent()###line 56:\n    sage: E.simon_two_descent()\n      File \"/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py\", line 1202, in simon_two_descent\n        maxprob=maxprob, limbigprime=limbigprime)\n      File \"/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/gp_simon.py\", line 69, in simon_two_descent\n        K = E.base_ring().change_names('a')\n    AttributeError: 'RationalField' object has no attribute 'change_names'\n**********************************************************************\n1 items had failures:\n   2 of   8 in __main__.example_2\n```\n\nI have added a second patch (apply after the first one) which checks that K is not QQ before changing names!\n\nIf either rlm or was could review my patch then this can go forward.",
    "created_at": "2009-02-15T17:40:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5204#issuecomment-39796",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_5204-a.patch](tarball://root/attachments/some-uuid/ticket5204/trac_5204-a.patch) by @JohnCremona created at 2009-02-15 17:40:22

Review:  I can only deduce that rlm did not actually test this!

```
sage -t  "devel/sage-5204/sage/schemes/elliptic_curves/gp_simon.py"
**********************************************************************
File "/home/john/sage-3.3.rc0/devel/sage-5204/sage/schemes/elliptic_curves/gp_simon.py", line 54:
    sage: sage.schemes.elliptic_curves.gp_simon.simon_two_descent(E)
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-3.3.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-3.3.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-3.3.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[4]>", line 1, in <module>
        sage.schemes.elliptic_curves.gp_simon.simon_two_descent(E)###line 54:
    sage: sage.schemes.elliptic_curves.gp_simon.simon_two_descent(E)
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/gp_simon.py", line 69, in simon_two_descent
        K = E.base_ring().change_names('a')
    AttributeError: 'RationalField' object has no attribute 'change_names'
**********************************************************************
File "/home/john/sage-3.3.rc0/devel/sage-5204/sage/schemes/elliptic_curves/gp_simon.py", line 56:
    sage: E.simon_two_descent()
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-3.3.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-3.3.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-3.3.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[5]>", line 1, in <module>
        E.simon_two_descent()###line 56:
    sage: E.simon_two_descent()
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 1202, in simon_two_descent
        maxprob=maxprob, limbigprime=limbigprime)
      File "/home/john/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/gp_simon.py", line 69, in simon_two_descent
        K = E.base_ring().change_names('a')
    AttributeError: 'RationalField' object has no attribute 'change_names'
**********************************************************************
1 items had failures:
   2 of   8 in __main__.example_2
```

I have added a second patch (apply after the first one) which checks that K is not QQ before changing names!

If either rlm or was could review my patch then this can go forward.



---

archive/issue_comments_039797.json:
```json
{
    "body": "+1",
    "created_at": "2009-02-16T17:49:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5204#issuecomment-39797",
    "user": "https://github.com/rlmill"
}
```

+1



---

archive/issue_comments_039798.json:
```json
{
    "body": "These two patches cause the following doctest failure:\n\n```\nsage -t -long devel/sage/sage/schemes/elliptic_curves/ell_number_field.py\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.rc3/devel/sage-main/sage/schemes/elliptic_curves/ell_number_field.py\", line 9:\n    sage: E.simon_two_descent()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-3.3.rc3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.3.rc3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.3.rc3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[5]>\", line 1, in <module>\n        E.simon_two_descent()###line 9:\n    sage: E.simon_two_descent()\n      File \"/scratch/mabshoff/sage-3.3.rc3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_number_field.py\", line 176, in simon_two_descent\n        maxprob=maxprob, limbigprime=limbigprime)\n      File \"/scratch/mabshoff/sage-3.3.rc3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/gp_simon.py\", line 74, in simon_two_descent\n        E = E.change_ring(K)\n      File \"/scratch/mabshoff/sage-3.3.rc3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py\", line 826, in change_ring\n        return constructor.EllipticCurve(R, [R(a) for a in self.ainvs()])\n      File \"parent.pyx\", line 276, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3653)\n      File \"coerce_maps.pyx\", line 76, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:2793)\n      File \"coerce_maps.pyx\", line 71, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2700)\n      File \"/scratch/mabshoff/sage-3.3.rc3/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 831, in _element_constructor_\n        return self._coerce_from_other_number_field(x)\n      File \"/scratch/mabshoff/sage-3.3.rc3/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 3735, in _coerce_from_other_number_field\n        raise TypeError, \"Cannot coerce element into this number field\"\n    TypeError: Cannot coerce element into this number field\n**********************************************************************\n```",
    "created_at": "2009-02-20T07:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5204#issuecomment-39798",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

These two patches cause the following doctest failure:

```
sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_number_field.py
**********************************************************************
File "/scratch/mabshoff/sage-3.3.rc3/devel/sage-main/sage/schemes/elliptic_curves/ell_number_field.py", line 9:
    sage: E.simon_two_descent()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.3.rc3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.rc3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.rc3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[5]>", line 1, in <module>
        E.simon_two_descent()###line 9:
    sage: E.simon_two_descent()
      File "/scratch/mabshoff/sage-3.3.rc3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_number_field.py", line 176, in simon_two_descent
        maxprob=maxprob, limbigprime=limbigprime)
      File "/scratch/mabshoff/sage-3.3.rc3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/gp_simon.py", line 74, in simon_two_descent
        E = E.change_ring(K)
      File "/scratch/mabshoff/sage-3.3.rc3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py", line 826, in change_ring
        return constructor.EllipticCurve(R, [R(a) for a in self.ainvs()])
      File "parent.pyx", line 276, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3653)
      File "coerce_maps.pyx", line 76, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:2793)
      File "coerce_maps.pyx", line 71, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2700)
      File "/scratch/mabshoff/sage-3.3.rc3/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 831, in _element_constructor_
        return self._coerce_from_other_number_field(x)
      File "/scratch/mabshoff/sage-3.3.rc3/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 3735, in _coerce_from_other_number_field
        raise TypeError, "Cannot coerce element into this number field"
    TypeError: Cannot coerce element into this number field
**********************************************************************
```



---

archive/issue_comments_039799.json:
```json
{
    "body": "Rats.  I was certain I had tested that file.  I'll look into it when I can (unlikely before this evening GMT).  John",
    "created_at": "2009-02-20T08:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5204#issuecomment-39799",
    "user": "https://github.com/JohnCremona"
}
```

Rats.  I was certain I had tested that file.  I'll look into it when I can (unlikely before this evening GMT).  John



---

archive/issue_comments_039800.json:
```json
{
    "body": "Apply after previous two",
    "created_at": "2009-02-20T09:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5204#issuecomment-39800",
    "user": "https://github.com/JohnCremona"
}
```

Apply after previous two



---

archive/issue_comments_039801.json:
```json
{
    "body": "Attachment [trac_5204-b.patch](tarball://root/attachments/some-uuid/ticket5204/trac_5204-b.patch) by @JohnCremona created at 2009-02-20 09:55:02\n\nThe trouble is that after changing the name of the field's generator (in that example from 'i' to 'a') there is no coercion from the old field to the new one, even though they only differ i nthe name of the gen.\n\nThis could obviously be hacked, and I have done so, but it is not very elegant:   since E's field has changed you have to hack again to get the points found back on the original curve which has the original base field.\n\nI'm sure that there is a better coercion-based way of doing this.  But the tests now pass.  Apply new patch after the other two.",
    "created_at": "2009-02-20T09:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5204#issuecomment-39801",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_5204-b.patch](tarball://root/attachments/some-uuid/ticket5204/trac_5204-b.patch) by @JohnCremona created at 2009-02-20 09:55:02

The trouble is that after changing the name of the field's generator (in that example from 'i' to 'a') there is no coercion from the old field to the new one, even though they only differ i nthe name of the gen.

This could obviously be hacked, and I have done so, but it is not very elegant:   since E's field has changed you have to hack again to get the points found back on the original curve which has the original base field.

I'm sure that there is a better coercion-based way of doing this.  But the tests now pass.  Apply new patch after the other two.



---

archive/issue_comments_039802.json:
```json
{
    "body": "+1",
    "created_at": "2009-03-16T13:58:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5204#issuecomment-39802",
    "user": "https://github.com/rlmill"
}
```

+1



---

archive/issue_comments_039803.json:
```json
{
    "body": "The following example actually came up today:\n\n```\nsage: K.<b>=QuadraticField(43)\nsage: E=EllipticCurve([0,0,0,0,(-3697884*b - 24248647)])\nsage: E.simon_two_descent()\nNameError                                 Traceback (most recent call last)\n...\nNameError: name 'ans' is not defined\n```\n\nThis is after the patches are applied, so bad news.  I called the field generator 'b' since earlier I had called it 'a' and thought that might be the problem.\n\nIt turns out that it is a bug in simon's ell.gp:\n\n```\n             GP/PARI CALCULATOR Version 2.3.3 (released)\n      i686 running linux (ix86/GMP-4.2.1 kernel) 32-bit version\n       compiled: Mar 12 2009, gcc-4.1.2 20070115 (SUSE Linux)\n          (readline v5.2 enabled, extended help available)\n\n               Copyright (C) 2000-2006 The PARI Group\n\nPARI/GP is free software, covered by the GNU General Public\nLicense, and comes WITHOUT ANY WARRANTY WHATSOEVER.\n\nType ? for help, \\q to quit.\nType ?12 for how to get moral (and possibly technical) support.\n\nparisize = 4000000, primelimit = 500000\n? \\r ell.gp\n? K = bnfinit(y^2 - 43);\n? a = Mod(y,K.pol);\n? bnfellrank(K, [0,0,0,0,-3697884*a - 24248647]);\ncourbe elliptique : Y^2 = x^3 + Mod(-3697884*y - 24248647, y^2 - 43)\npoints triviaux sur la courbe = [[1, 1, 0]]\n  ***   array index (1) out of allowed range [none]:\n  ***   ...iv,r=nfsqrt(nf,norm(zc))[1];if(DEBUGLEVEL_ell\n                                    ^--------------------\n```\nI will check that it still happens with the latest pari/gp, and if so file a bug report with Denis Simon.",
    "created_at": "2009-03-19T16:54:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5204#issuecomment-39803",
    "user": "https://github.com/JohnCremona"
}
```

The following example actually came up today:

```
sage: K.<b>=QuadraticField(43)
sage: E=EllipticCurve([0,0,0,0,(-3697884*b - 24248647)])
sage: E.simon_two_descent()
NameError                                 Traceback (most recent call last)
...
NameError: name 'ans' is not defined
```

This is after the patches are applied, so bad news.  I called the field generator 'b' since earlier I had called it 'a' and thought that might be the problem.

It turns out that it is a bug in simon's ell.gp:

```
             GP/PARI CALCULATOR Version 2.3.3 (released)
      i686 running linux (ix86/GMP-4.2.1 kernel) 32-bit version
       compiled: Mar 12 2009, gcc-4.1.2 20070115 (SUSE Linux)
          (readline v5.2 enabled, extended help available)

               Copyright (C) 2000-2006 The PARI Group

PARI/GP is free software, covered by the GNU General Public
License, and comes WITHOUT ANY WARRANTY WHATSOEVER.

Type ? for help, \q to quit.
Type ?12 for how to get moral (and possibly technical) support.

parisize = 4000000, primelimit = 500000
? \r ell.gp
? K = bnfinit(y^2 - 43);
? a = Mod(y,K.pol);
? bnfellrank(K, [0,0,0,0,-3697884*a - 24248647]);
courbe elliptique : Y^2 = x^3 + Mod(-3697884*y - 24248647, y^2 - 43)
points triviaux sur la courbe = [[1, 1, 0]]
  ***   array index (1) out of allowed range [none]:
  ***   ...iv,r=nfsqrt(nf,norm(zc))[1];if(DEBUGLEVEL_ell
                                    ^--------------------
```
I will check that it still happens with the latest pari/gp, and if so file a bug report with Denis Simon.



---

archive/issue_comments_039804.json:
```json
{
    "body": "Denis Simon says:\n\n```\nDear John,\n\nOK, this is really a bug of ell.gp\n\nThe problem is that due to a low real precision, the sign\nof an algebraic number at some real embedding is misevaluated.\n\nFor a quick fix, you have to get into the function 'nfsqrt'\nand remove the small loop\nfor( i = 1, nf.r1,...\n\nThis is not a satisfactory solution, and I am looking for a better one.\nIn particular, I probably have to change the way I handle the real\nembeddings. For the moment, it is just something like\nsubst(algebraic_number,y,nf.roots[1])\n\nMaybe I have to do interval arithmetic...\n\nThank you for the report.\nDenis SIMON.\n```\nso that will have to wait until he fixes hos gp script.  This should probably be on a different ticket...",
    "created_at": "2009-03-23T19:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5204#issuecomment-39804",
    "user": "https://github.com/JohnCremona"
}
```

Denis Simon says:

```
Dear John,

OK, this is really a bug of ell.gp

The problem is that due to a low real precision, the sign
of an algebraic number at some real embedding is misevaluated.

For a quick fix, you have to get into the function 'nfsqrt'
and remove the small loop
for( i = 1, nf.r1,...

This is not a satisfactory solution, and I am looking for a better one.
In particular, I probably have to change the way I handle the real
embeddings. For the moment, it is just something like
subst(algebraic_number,y,nf.roots[1])

Maybe I have to do interval arithmetic...

Thank you for the report.
Denis SIMON.
```
so that will have to wait until he fixes hos gp script.  This should probably be on a different ticket...



---

archive/issue_events_012050.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-24T23:16:07Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5204",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5204#event-12050"
}
```



---

archive/issue_comments_039805.json:
```json
{
    "body": "Merged all three patches in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-24T23:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5204#issuecomment-39805",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three patches in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_events_012051.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-24T23:16:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5204",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5204#event-12051"
}
```



---

archive/issue_comments_039806.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-24T23:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5204#issuecomment-39806",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
