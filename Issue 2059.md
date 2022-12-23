# Issue 2059: bug in polybori -- lexLmDeg -- no such attribute

archive/issues_002059.json:
```json
{
    "body": "Assignee: malb\n\nCC:  burcin\n\nHi,\n\nI finally decided to play with PolyBoRi and found a bug in the Sage wrapper of it in about 20 seconds flat.  See below.  This is \n\n\n```\nsage: B.<x,y,z> = BooleanPolynomialRing(3)\nsage: B.ideal([x,y])\nIdeal (x, y) of Boolean PolynomialRing in x, y, z\nsage: B.ideal([x,y])^3\nIdeal (x, x*y, x*y, x*y, x*y, x*y, x*y, y) of Boolean PolynomialRing in x, y, z\nsage: B.ideal([x,y])^20\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/Users/was/<ipython console> in <module>()\n\n/Users/was/element.pyx in sage.structure.element.MonoidElement.__pow__()\n\n/Users/was/element.pyx in sage.structure.element.generic_power_c()\n\n/Users/was/element.pyx in sage.structure.element.Element.__richcmp__()\n\n/Users/was/element.pyx in sage.structure.element.Element._richcmp()\n\n/Users/was/s/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in __cmp__(self, other)\n    235         #    return c\n    236         l = self.groebner_basis()\n--> 237         r = other.groebner_basis()\n    238         return cmp(r,l)\n    239 \n\n/Users/was/pbori.pyx in sage.rings.polynomial.pbori.BooleanPolynomialIdeal.groebner_basis()\n\n/Users/was/s/local/share/polybori/pyroot/polybori/gbcore.py in __call__(self, *args, **kwds)\n    134         if heuristic:\n    135             complete_dict=self.heuristicFunction(complete_dict)\n--> 136         return self.f(**complete_dict)\n    137     def __init__(self,f,heuristic_function):\n    138         \n\n/Users/was/s/local/share/polybori/pyroot/polybori/gbcore.py in wrapper(I, **kwds)\n    184                        (I,state)=pre(I,option_set)\n    185                \n--> 186             res=f(I,**kwds)\n    187             if option_set:\n    188                 if post:\n\n/Users/was/s/local/share/polybori/pyroot/polybori/gbcore.py in wrapper(I, **kwds)\n    184                        (I,state)=pre(I,option_set)\n    185                \n--> 186             res=f(I,**kwds)\n    187             if option_set:\n    188                 if post:\n\n/Users/was/s/local/share/polybori/pyroot/polybori/gbcore.py in wrapper(I, **kwds)\n    184                        (I,state)=pre(I,option_set)\n    185                \n--> 186             res=f(I,**kwds)\n    187             if option_set:\n    188                 if post:\n\n/Users/was/s/local/share/polybori/pyroot/polybori/gbcore.py in wrapper(I, **kwds)\n    180                        print \"preprocessing for option:\", option\n    181                    if not pass_option_set:\n--> 182                        (I,state)=pre(I)\n    183                    else:\n    184                        (I,state)=pre(I,option_set)\n\n/Users/was/s/local/share/polybori/pyroot/polybori/gbcore.py in llfirst_pre(I)\n    216     \n    217 def llfirst_pre(I):\n--> 218     (eliminated,llnf, I)=eliminate(I,on_the_fly=False)\n    219     return (I,eliminated)\n    220 \n\n/Users/was/s/local/share/polybori/pyroot/polybori/ll.py in eliminate(polys, on_the_fly)\n     69       reductors=ll_encode(linear_leads)\n     70   else:\n---> 71       reductors=llredsb_Cudd_style(linear_leads)\n     72       reductors=BooleSet(reductors.set())\n     73   if on_the_fly:\n\n/Users/was/s/local/share/polybori/pyroot/polybori/ll.py in llredsb_Cudd_style(polys)\n      9   assert len(set([p.lexLead() for p in linear_lead]))==len(polys)\n     10   assert len([p for p in polys if p.constant()])==0\n---> 11   assert len([p for p in polys if p.lexLmDeg()==1])==len(polys)\n     12   assert len(set([p.navigation().value() for p in polys]))==len(polys)\n     13   counter=0\n\n<type 'exceptions.AttributeError'>: 'sage.rings.polynomial.pbori.BooleanPolynomial' object has no attribute 'lexLmDeg'\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2059\n\n",
    "created_at": "2008-02-05T17:11:53Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "bug in polybori -- lexLmDeg -- no such attribute",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2059",
    "user": "was"
}
```
Assignee: malb

CC:  burcin

Hi,

I finally decided to play with PolyBoRi and found a bug in the Sage wrapper of it in about 20 seconds flat.  See below.  This is 


```
sage: B.<x,y,z> = BooleanPolynomialRing(3)
sage: B.ideal([x,y])
Ideal (x, y) of Boolean PolynomialRing in x, y, z
sage: B.ideal([x,y])^3
Ideal (x, x*y, x*y, x*y, x*y, x*y, x*y, y) of Boolean PolynomialRing in x, y, z
sage: B.ideal([x,y])^20
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/element.pyx in sage.structure.element.MonoidElement.__pow__()

/Users/was/element.pyx in sage.structure.element.generic_power_c()

/Users/was/element.pyx in sage.structure.element.Element.__richcmp__()

/Users/was/element.pyx in sage.structure.element.Element._richcmp()

/Users/was/s/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in __cmp__(self, other)
    235         #    return c
    236         l = self.groebner_basis()
--> 237         r = other.groebner_basis()
    238         return cmp(r,l)
    239 

/Users/was/pbori.pyx in sage.rings.polynomial.pbori.BooleanPolynomialIdeal.groebner_basis()

/Users/was/s/local/share/polybori/pyroot/polybori/gbcore.py in __call__(self, *args, **kwds)
    134         if heuristic:
    135             complete_dict=self.heuristicFunction(complete_dict)
--> 136         return self.f(**complete_dict)
    137     def __init__(self,f,heuristic_function):
    138         

/Users/was/s/local/share/polybori/pyroot/polybori/gbcore.py in wrapper(I, **kwds)
    184                        (I,state)=pre(I,option_set)
    185                
--> 186             res=f(I,**kwds)
    187             if option_set:
    188                 if post:

/Users/was/s/local/share/polybori/pyroot/polybori/gbcore.py in wrapper(I, **kwds)
    184                        (I,state)=pre(I,option_set)
    185                
--> 186             res=f(I,**kwds)
    187             if option_set:
    188                 if post:

/Users/was/s/local/share/polybori/pyroot/polybori/gbcore.py in wrapper(I, **kwds)
    184                        (I,state)=pre(I,option_set)
    185                
--> 186             res=f(I,**kwds)
    187             if option_set:
    188                 if post:

/Users/was/s/local/share/polybori/pyroot/polybori/gbcore.py in wrapper(I, **kwds)
    180                        print "preprocessing for option:", option
    181                    if not pass_option_set:
--> 182                        (I,state)=pre(I)
    183                    else:
    184                        (I,state)=pre(I,option_set)

/Users/was/s/local/share/polybori/pyroot/polybori/gbcore.py in llfirst_pre(I)
    216     
    217 def llfirst_pre(I):
--> 218     (eliminated,llnf, I)=eliminate(I,on_the_fly=False)
    219     return (I,eliminated)
    220 

/Users/was/s/local/share/polybori/pyroot/polybori/ll.py in eliminate(polys, on_the_fly)
     69       reductors=ll_encode(linear_leads)
     70   else:
---> 71       reductors=llredsb_Cudd_style(linear_leads)
     72       reductors=BooleSet(reductors.set())
     73   if on_the_fly:

/Users/was/s/local/share/polybori/pyroot/polybori/ll.py in llredsb_Cudd_style(polys)
      9   assert len(set([p.lexLead() for p in linear_lead]))==len(polys)
     10   assert len([p for p in polys if p.constant()])==0
---> 11   assert len([p for p in polys if p.lexLmDeg()==1])==len(polys)
     12   assert len(set([p.navigation().value() for p in polys]))==len(polys)
     13   counter=0

<type 'exceptions.AttributeError'>: 'sage.rings.polynomial.pbori.BooleanPolynomial' object has no attribute 'lexLmDeg'

```


Issue created by migration from https://trac.sagemath.org/ticket/2059





---

archive/issue_comments_013332.json:
```json
{
    "body": "Attachment\n\nthis fixes the attribute error but is not enough to make the calculation given above work",
    "created_at": "2008-02-05T17:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2059#issuecomment-13332",
    "user": "malb"
}
```

Attachment

this fixes the attribute error but is not enough to make the calculation given above work



---

archive/issue_comments_013333.json:
```json
{
    "body": "The attached patch `trac_2059_1.patch` fixes the attribute error, however now:\n\n\n```\nsage:  sage: B.<x,y,z> = BooleanPolynomialRing(3)\nsage:  sage: B.ideal([x,y])\nIdeal (x, y) of Boolean PolynomialRing in x, y, z\nsage:  sage: B.ideal([x,y])^3\nIdeal (x, x*y, x*y, x*y, x*y, x*y, x*y, y) of Boolean PolynomialRing in x, y, z\nsage:  B.ideal([x,y])^20\n...\n<type 'exceptions.AttributeError'>: 'list' object has no attribute 'minimalizeAndTailReduce'\n```\n\n\nBurcin, any idea?",
    "created_at": "2008-02-05T17:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2059#issuecomment-13333",
    "user": "malb"
}
```

The attached patch `trac_2059_1.patch` fixes the attribute error, however now:


```
sage:  sage: B.<x,y,z> = BooleanPolynomialRing(3)
sage:  sage: B.ideal([x,y])
Ideal (x, y) of Boolean PolynomialRing in x, y, z
sage:  sage: B.ideal([x,y])^3
Ideal (x, x*y, x*y, x*y, x*y, x*y, x*y, y) of Boolean PolynomialRing in x, y, z
sage:  B.ideal([x,y])^20
...
<type 'exceptions.AttributeError'>: 'list' object has no attribute 'minimalizeAndTailReduce'
```


Burcin, any idea?



---

archive/issue_comments_013334.json:
```json
{
    "body": "The problem seen after applying attachment:trac_2059_1.patch is a bug in `PolyBoRi` itself. Trying to compute the Groebner basis of an ideal generated by [x,y] causes the heuristic function to blow up with the same problem in the ipython shell that comes with `PolyBoRi.` I will report this upstream.",
    "created_at": "2008-02-06T11:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2059#issuecomment-13334",
    "user": "burcin"
}
```

The problem seen after applying attachment:trac_2059_1.patch is a bug in `PolyBoRi` itself. Trying to compute the Groebner basis of an ideal generated by [x,y] causes the heuristic function to blow up with the same problem in the ipython shell that comes with `PolyBoRi.` I will report this upstream.



---

archive/issue_comments_013335.json:
```json
{
    "body": "Changing assignee from malb to burcin.",
    "created_at": "2008-02-06T11:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2059#issuecomment-13335",
    "user": "burcin"
}
```

Changing assignee from malb to burcin.



---

archive/issue_comments_013336.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-06T11:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2059#issuecomment-13336",
    "user": "burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013337.json:
```json
{
    "body": "This seems to be fixed in PolyBoRi 0.3.1:\n\n```\nsage: B.<x,y,z> = BooleanPolynomialRing(3)\nsage: B.ideal([x,y])\nIdeal (x, y) of Boolean PolynomialRing in x, y, z\nsage: B.ideal([x,y])^3\nIdeal (x, x*y, x*y, x*y, x*y, x*y, x*y, y) of Boolean PolynomialRing in x, y, z\nsage: B.ideal([x,y])^20\nIdeal (x, y) of Boolean PolynomialRing in x, y, z\n```\n",
    "created_at": "2008-04-07T13:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2059#issuecomment-13337",
    "user": "malb"
}
```

This seems to be fixed in PolyBoRi 0.3.1:

```
sage: B.<x,y,z> = BooleanPolynomialRing(3)
sage: B.ideal([x,y])
Ideal (x, y) of Boolean PolynomialRing in x, y, z
sage: B.ideal([x,y])^3
Ideal (x, x*y, x*y, x*y, x*y, x*y, x*y, y) of Boolean PolynomialRing in x, y, z
sage: B.ideal([x,y])^20
Ideal (x, y) of Boolean PolynomialRing in x, y, z
```




---

archive/issue_comments_013338.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T13:41:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2059#issuecomment-13338",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013339.json:
```json
{
    "body": "Closed on recommendation of malb.",
    "created_at": "2008-04-07T13:41:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2059",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2059#issuecomment-13339",
    "user": "mabshoff"
}
```

Closed on recommendation of malb.
