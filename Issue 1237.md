# Issue 1237: E.torsion_order() fails on curves with big coefficients !!

archive/issues_001237.json:
```json
{
    "body": "Assignee: @williamstein\n\nOn Nov 20, 2007 1:40 PM, Paul Zimmermann  wrote:\n>        William,\n> \n> sage told me to report you, thus I do:\n[... see below]\n\nFor the particular curve you're considering mwrank (via sage's rank command)\ncan compute the rank -- which is what you want -- in 0.5 seconds, so maybe\nyou can use .rank() instead?\n\n\n```\nid=24|\ne = EllipticCurve([0, 33076156654533652066609946884, 0,\n347897536144342179642120321790729023127716119338758604800,\n114112815436927429551902303280680424778815462104985764887003237028585178\\\n1352816640000])\n```\n\n\n\n```\nid=27|\ntime e.rank()\n///\n1\nCPU time: 0.00 s,  Wall time: 0.46 s\n```\n\n\nThat said, the fact that  e.torsion_order() fails is certainly a bug:\n\n\n```\nid=29|\ne.torsion_order()\n///\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/Users/was/sage_notebook/worksheets/admin/23/code/91.py\", line 4, in <module>\n...\n    self.__torsion_subgroup = rational_torsion.EllipticCurveTorsionSubgroup(self, flag)\n  File \"/Users/was/s/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/rational_torsion.py\", line 56, in __init__\n    self.__E.__pari_double_prec()\nAttributeError: 'EllipticCurve_rational_field' object has no attribute '_EllipticCurveTorsionSubgroup__pari_double_prec'\n```\n\n\n\n\n```\n\n> sage: d = 919681/88529281\n> sage: _ = magma.eval('K := Rationals()')\n> sage: _ = magma.eval('P<x,y,z>:=ProjectiveSpace(K,2)')\n> sage: def rank(d):\n> ....:        s='f := (x^2+y^2)*z^2-z^4-('\n> ....:    s=''.join([s, repr(d), ')*x^2*y^2;'])\n> ....:    magma.eval(s)\n> ....:    magma.eval('C:=Curve(P,f);')\n> ....:    E = magma('EllipticCurve(C,C![0,1,1])')\n> ....:    l = E.aInvariants()\n> ....:    EE = EllipticCurve(map(Integer,l))\n> ....:    return EE.simon_two_descent()[0]\n> ....:\n> sage: rank(d)\n> ---------------------------------------------------------------------------\n> <type 'exceptions.AttributeError'>        Traceback (most recent call last)\n> \n> /home/zimmerma/<ipython console> in <module>()\n> \n> /home/zimmerma/<ipython console> in rank(d)\n> \n> /usr/local/sage-2.8.12/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py in simon_two_descent(self, verbose, lim1, lim3, limtriv, maxprob, limbigprime)\n>     858             (8, 8)\n>     859         \"\"\"\n> --> 860         if self.torsion_order() % 2 == 0:\n>     861             raise ArithmeticError, \"curve must not have rational 2-torsion\\nThe *only* reason for this is that I haven't finished implementing the wrapper\\nin this case.  It wouldn't be too difficult.\\nPerhaps you could do it?!  Email me (wstein@gmail.com).\"\n>     862         F = self.integral_weierstrass_model()\n> \n> /usr/local/sage-2.8.12/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py in torsion_order(self)\n>    1743             return self.__torsion_order\n>    1744         except AttributeError:\n> -> 1745             self.__torsion_order = self.torsion_subgroup().order()\n>    1746             return self.__torsion_order\n>    1747\n> \n> /usr/local/sage-2.8.12/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py in torsion_subgroup(self, flag)\n>    1781             return self.__torsion_subgroup\n>    1782         except AttributeError:\n> -> 1783             self.__torsion_subgroup = rational_torsion.EllipticCurveTorsionSubgroup(self, flag)\n>    1784             return self.__torsion_subgroup\n>    1785\n> \n> /usr/local/sage-2.8.12/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/rational_torsion.py in __init__(self, E, flag)\n>      54                 G = self.__E.pari_curve().elltors(flag)\n>      55             except RuntimeError:\n> ---> 56                 self.__E.__pari_double_prec()\n>      57         if G is None:\n>      58             raise RuntimeError, \"Could not compute torsion subgroup\"\n> \n> <type 'exceptions.AttributeError'>: 'EllipticCurve_rational_field' object has no attribute '_EllipticCurveTorsionSubgroup__pari_double_prec'\n> \n> Paul\n> \n```\n\n\n\n-- \nWilliam Stein\nAssociate Professor of Mathematics\nUniversity of Washington\nhttp://wstein.org\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1237\n\n",
    "created_at": "2007-11-21T17:25:16Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "E.torsion_order() fails on curves with big coefficients !!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1237",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

On Nov 20, 2007 1:40 PM, Paul Zimmermann  wrote:
>        William,
> 
> sage told me to report you, thus I do:
[... see below]

For the particular curve you're considering mwrank (via sage's rank command)
can compute the rank -- which is what you want -- in 0.5 seconds, so maybe
you can use .rank() instead?


```
id=24|
e = EllipticCurve([0, 33076156654533652066609946884, 0,
347897536144342179642120321790729023127716119338758604800,
114112815436927429551902303280680424778815462104985764887003237028585178\
1352816640000])
```



```
id=27|
time e.rank()
///
1
CPU time: 0.00 s,  Wall time: 0.46 s
```


That said, the fact that  e.torsion_order() fails is certainly a bug:


```
id=29|
e.torsion_order()
///
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/was/sage_notebook/worksheets/admin/23/code/91.py", line 4, in <module>
...
    self.__torsion_subgroup = rational_torsion.EllipticCurveTorsionSubgroup(self, flag)
  File "/Users/was/s/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/rational_torsion.py", line 56, in __init__
    self.__E.__pari_double_prec()
AttributeError: 'EllipticCurve_rational_field' object has no attribute '_EllipticCurveTorsionSubgroup__pari_double_prec'
```




```

> sage: d = 919681/88529281
> sage: _ = magma.eval('K := Rationals()')
> sage: _ = magma.eval('P<x,y,z>:=ProjectiveSpace(K,2)')
> sage: def rank(d):
> ....:        s='f := (x^2+y^2)*z^2-z^4-('
> ....:    s=''.join([s, repr(d), ')*x^2*y^2;'])
> ....:    magma.eval(s)
> ....:    magma.eval('C:=Curve(P,f);')
> ....:    E = magma('EllipticCurve(C,C![0,1,1])')
> ....:    l = E.aInvariants()
> ....:    EE = EllipticCurve(map(Integer,l))
> ....:    return EE.simon_two_descent()[0]
> ....:
> sage: rank(d)
> ---------------------------------------------------------------------------
> <type 'exceptions.AttributeError'>        Traceback (most recent call last)
> 
> /home/zimmerma/<ipython console> in <module>()
> 
> /home/zimmerma/<ipython console> in rank(d)
> 
> /usr/local/sage-2.8.12/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py in simon_two_descent(self, verbose, lim1, lim3, limtriv, maxprob, limbigprime)
>     858             (8, 8)
>     859         """
> --> 860         if self.torsion_order() % 2 == 0:
>     861             raise ArithmeticError, "curve must not have rational 2-torsion\nThe *only* reason for this is that I haven't finished implementing the wrapper\nin this case.  It wouldn't be too difficult.\nPerhaps you could do it?!  Email me (wstein@gmail.com)."
>     862         F = self.integral_weierstrass_model()
> 
> /usr/local/sage-2.8.12/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py in torsion_order(self)
>    1743             return self.__torsion_order
>    1744         except AttributeError:
> -> 1745             self.__torsion_order = self.torsion_subgroup().order()
>    1746             return self.__torsion_order
>    1747
> 
> /usr/local/sage-2.8.12/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py in torsion_subgroup(self, flag)
>    1781             return self.__torsion_subgroup
>    1782         except AttributeError:
> -> 1783             self.__torsion_subgroup = rational_torsion.EllipticCurveTorsionSubgroup(self, flag)
>    1784             return self.__torsion_subgroup
>    1785
> 
> /usr/local/sage-2.8.12/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/rational_torsion.py in __init__(self, E, flag)
>      54                 G = self.__E.pari_curve().elltors(flag)
>      55             except RuntimeError:
> ---> 56                 self.__E.__pari_double_prec()
>      57         if G is None:
>      58             raise RuntimeError, "Could not compute torsion subgroup"
> 
> <type 'exceptions.AttributeError'>: 'EllipticCurve_rational_field' object has no attribute '_EllipticCurveTorsionSubgroup__pari_double_prec'
> 
> Paul
> 
```



-- 
William Stein
Associate Professor of Mathematics
University of Washington
http://wstein.org


Issue created by migration from https://trac.sagemath.org/ticket/1237





---

archive/issue_comments_007709.json:
```json
{
    "body": "Fix",
    "created_at": "2007-11-21T22:13:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1237#issuecomment-7709",
    "user": "https://github.com/roed314"
}
```

Fix



---

archive/issue_comments_007710.json:
```json
{
    "body": "Changing assignee from @williamstein to @roed314.",
    "created_at": "2007-11-21T22:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1237#issuecomment-7710",
    "user": "https://github.com/roed314"
}
```

Changing assignee from @williamstein to @roed314.



---

archive/issue_comments_007711.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-21T22:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1237#issuecomment-7711",
    "user": "https://github.com/roed314"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007712.json:
```json
{
    "body": "Attachment [trac1237.patch](tarball://root/attachments/some-uuid/ticket1237/trac1237.patch) by @roed314 created at 2007-11-21 22:14:39",
    "created_at": "2007-11-21T22:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1237#issuecomment-7712",
    "user": "https://github.com/roed314"
}
```

Attachment [trac1237.patch](tarball://root/attachments/some-uuid/ticket1237/trac1237.patch) by @roed314 created at 2007-11-21 22:14:39



---

archive/issue_comments_007713.json:
```json
{
    "body": "Attachment [trac-1237-part2.patch](tarball://root/attachments/some-uuid/ticket1237/trac-1237-part2.patch) by @williamstein created at 2007-12-15 11:39:47\n\nthis touches up a bunch of the docs.",
    "created_at": "2007-12-15T11:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1237#issuecomment-7713",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1237-part2.patch](tarball://root/attachments/some-uuid/ticket1237/trac-1237-part2.patch) by @williamstein created at 2007-12-15 11:39:47

this touches up a bunch of the docs.



---

archive/issue_comments_007714.json:
```json
{
    "body": "I give this a positive review.",
    "created_at": "2007-12-15T11:40:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1237#issuecomment-7714",
    "user": "https://github.com/williamstein"
}
```

I give this a positive review.



---

archive/issue_comments_007715.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T11:51:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1237#issuecomment-7715",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007716.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T11:51:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1237#issuecomment-7716",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc0.
