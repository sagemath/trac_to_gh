# Issue 9841: groebner basis bug

archive/issues_009841.json:
```json
{
    "body": "Assignee: @malb\n\nThe following code fails\n\n\n```\nset_random_seed(0)\nR=PolynomialRing(GF(2), 10, \"x\", \"lex\")\nL0 = [R.random_element() for i in range(10)]\nS = BooleanPolynomialRing(20, \"y\", \"lex\")\nSu = [S.gen(10+i) for i in range(10)]\nh = R.hom(Su)\nL1 = [h(L0[9]) +S.gen(9)] + \n     [h(L0[i])+S.gen(i)+S.gen(i+1) for i in range(8)] +\n     [S.gen(i)+S(GF(2).random_element()) for i in range(10,20)]\nI = ideal(L1)\nG0 = I.interreduced_basis()\nG0 == ideal(G0).groebner_basis()\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/<ipython console> in <module>()\n\n/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/sage/rings/polynomial/pbori.so in sage.rings.polynomial.pbori.BooleanPolynomialIdeal.groebner_basis (sage/rings/polynomial/pbori.cpp:25421)()\n\n/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/gbcore.pyc in wrapper(I, **kwds)\n    186                    \n    187                    (I,state)=pre(**dict([(k,v) for (k,v) in locals().iteritems() if k in pre_args]))\n--> 188             I=f(I,**kwds)\n    189             if option_set:\n    190                 if post:\n\n/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/gbcore.pyc in wrapper(I, **kwds)\n    186                    \n    187                    (I,state)=pre(**dict([(k,v) for (k,v) in locals().iteritems() if k in pre_args]))\n--> 188             I=f(I,**kwds)\n    189             if option_set:\n    190                 if post:\n\n/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/gbcore.pyc in __call__(self, *args, **kwds)\n    138         if heuristic:\n    139             complete_dict=self.heuristicFunction(complete_dict)\n--> 140         return self.f(**complete_dict)\n    141     def __init__(self,f,heuristic_function):\n    142         (self.argnames,self.varargs,self.varopts,self.defaults)=getargspec(f)\n\n/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/gbcore.pyc in wrapper(I, **kwds)\n    186                    \n    187                    (I,state)=pre(**dict([(k,v) for (k,v) in locals().iteritems() if k in pre_args]))\n--> 188             I=f(I,**kwds)\n    189             if option_set:\n    190                 if post:\n\n/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/gbcore.pyc in __call__(self, *args, **kwds)\n    138         if heuristic:\n    139             complete_dict=self.heuristicFunction(complete_dict)\n--> 140         return self.f(**complete_dict)\n    141     def __init__(self,f,heuristic_function):\n    142         (self.argnames,self.varargs,self.varopts,self.defaults)=getargspec(f)\n\n/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/gbcore.pyc in wrapper(I, **kwds)\n    186                    \n    187                    (I,state)=pre(**dict([(k,v) for (k,v) in locals().iteritems() if k in pre_args]))\n--> 188             I=f(I,**kwds)\n    189             if option_set:\n    190                 if post:\n\n/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/gbcore.pyc in wrapper(I, **kwds)\n    186                    \n    187                    (I,state)=pre(**dict([(k,v) for (k,v) in locals().iteritems() if k in pre_args]))\n--> 188             I=f(I,**kwds)\n    189             if option_set:\n    190                 if post:\n\n/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/gbcore.pyc in wrapper(I, **kwds)\n    186                    \n    187                    (I,state)=pre(**dict([(k,v) for (k,v) in locals().iteritems() if k in pre_args]))\n--> 188             I=f(I,**kwds)\n    189             if option_set:\n    190                 if post:\n\n/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/gbcore.pyc in wrapper(I, **kwds)\n    186                    \n    187                    (I,state)=pre(**dict([(k,v) for (k,v) in locals().iteritems() if k in pre_args]))\n--> 188             I=f(I,**kwds)\n    189             if option_set:\n    190                 if post:\n\n/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/gbcore.pyc in wrapper(I, **kwds)\n    185                        print \"preprocessing for option:\", option\n    186                    \n--> 187                    (I,state)=pre(**dict([(k,v) for (k,v) in locals().iteritems() if k in pre_args]))\n    188             I=f(I,**kwds)\n    189             if option_set:\n\n/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/gbcore.pyc in llfirst_pre(I, prot)\n    223     \n    224 def llfirst_pre(I,prot):\n--> 225     (eliminated,llnf, I)=eliminate(I,on_the_fly=False,prot=prot)\n    226     return (I,eliminated)\n    227 \n\n/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/ll.pyc in eliminate(polys, on_the_fly, prot, reduction_function, optimized)\n    105         reduction_function=reduction_function,\n    106         reduce_ll_system=(not on_the_fly),\n--> 107         prot=prot)\n    108   else:\n    109       reductors=ll_encode(linear_leads,reduce=(not on_the_fly),prot=prot)\n\n/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/ll.pyc in eliminate_ll_ranked(ll_system, to_reduce, reduction_function, reduce_ll_system, prot)\n    153       from_ring.set()\n    154       \n--> 155   map_from_vec=construct_map_by_indices(to_ring, map_from_indices)\n    156   map_back_vec=construct_map_by_indices(from_ring, map_back_indices)\n    157   def map_from(p):\n\n/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/ll.pyc in construct_map_by_indices(to_ring, idx_mapping)\n    121   v=BoolePolynomialVector(to_ring.n_variables()*[to_ring.zero()])\n    122   for (from_idx, to_idx) in idx_mapping.iteritems():\n--> 123       v[from_idx]=to_ring.var(to_idx)\n    124   return v\n    125 \n\n/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/sage/rings/polynomial/pbori.so in sage.rings.polynomial.pbori.BooleanPolynomialVector.__setitem__ (sage/rings/polynomial/pbori.cpp:29608)()\n\n/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/sage/rings/polynomial/pbori.so in sage.rings.polynomial.pbori.BooleanPolynomialRing.__call__ (sage/rings/polynomial/pbori.cpp:7107)()\n\n/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/sage/structure/parent_old.so in sage.structure.parent_old.Parent._coerce_c (sage/structure/parent_old.c:3561)()\n\n/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/sage/rings/polynomial/pbori.so in sage.rings.polynomial.pbori.BooleanPolynomialRing._coerce_c_impl (sage/rings/polynomial/pbori.cpp:6209)()\n\nValueError: cannot coerce polynomial y2 to Boolean PolynomialRing in y5, y7, y8, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16, y17, y18, y19: name y0 not defined\nsage: \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9842\n\n",
    "created_at": "2010-08-30T19:39:26Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "title": "groebner basis bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9841",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```
Assignee: @malb

The following code fails


```
set_random_seed(0)
R=PolynomialRing(GF(2), 10, "x", "lex")
L0 = [R.random_element() for i in range(10)]
S = BooleanPolynomialRing(20, "y", "lex")
Su = [S.gen(10+i) for i in range(10)]
h = R.hom(Su)
L1 = [h(L0[9]) +S.gen(9)] + 
     [h(L0[i])+S.gen(i)+S.gen(i+1) for i in range(8)] +
     [S.gen(i)+S(GF(2).random_element()) for i in range(10,20)]
I = ideal(L1)
G0 = I.interreduced_basis()
G0 == ideal(G0).groebner_basis()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/<ipython console> in <module>()

/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/sage/rings/polynomial/pbori.so in sage.rings.polynomial.pbori.BooleanPolynomialIdeal.groebner_basis (sage/rings/polynomial/pbori.cpp:25421)()

/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/gbcore.pyc in wrapper(I, **kwds)
    186                    
    187                    (I,state)=pre(**dict([(k,v) for (k,v) in locals().iteritems() if k in pre_args]))
--> 188             I=f(I,**kwds)
    189             if option_set:
    190                 if post:

/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/gbcore.pyc in wrapper(I, **kwds)
    186                    
    187                    (I,state)=pre(**dict([(k,v) for (k,v) in locals().iteritems() if k in pre_args]))
--> 188             I=f(I,**kwds)
    189             if option_set:
    190                 if post:

/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/gbcore.pyc in __call__(self, *args, **kwds)
    138         if heuristic:
    139             complete_dict=self.heuristicFunction(complete_dict)
--> 140         return self.f(**complete_dict)
    141     def __init__(self,f,heuristic_function):
    142         (self.argnames,self.varargs,self.varopts,self.defaults)=getargspec(f)

/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/gbcore.pyc in wrapper(I, **kwds)
    186                    
    187                    (I,state)=pre(**dict([(k,v) for (k,v) in locals().iteritems() if k in pre_args]))
--> 188             I=f(I,**kwds)
    189             if option_set:
    190                 if post:

/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/gbcore.pyc in __call__(self, *args, **kwds)
    138         if heuristic:
    139             complete_dict=self.heuristicFunction(complete_dict)
--> 140         return self.f(**complete_dict)
    141     def __init__(self,f,heuristic_function):
    142         (self.argnames,self.varargs,self.varopts,self.defaults)=getargspec(f)

/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/gbcore.pyc in wrapper(I, **kwds)
    186                    
    187                    (I,state)=pre(**dict([(k,v) for (k,v) in locals().iteritems() if k in pre_args]))
--> 188             I=f(I,**kwds)
    189             if option_set:
    190                 if post:

/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/gbcore.pyc in wrapper(I, **kwds)
    186                    
    187                    (I,state)=pre(**dict([(k,v) for (k,v) in locals().iteritems() if k in pre_args]))
--> 188             I=f(I,**kwds)
    189             if option_set:
    190                 if post:

/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/gbcore.pyc in wrapper(I, **kwds)
    186                    
    187                    (I,state)=pre(**dict([(k,v) for (k,v) in locals().iteritems() if k in pre_args]))
--> 188             I=f(I,**kwds)
    189             if option_set:
    190                 if post:

/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/gbcore.pyc in wrapper(I, **kwds)
    186                    
    187                    (I,state)=pre(**dict([(k,v) for (k,v) in locals().iteritems() if k in pre_args]))
--> 188             I=f(I,**kwds)
    189             if option_set:
    190                 if post:

/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/gbcore.pyc in wrapper(I, **kwds)
    185                        print "preprocessing for option:", option
    186                    
--> 187                    (I,state)=pre(**dict([(k,v) for (k,v) in locals().iteritems() if k in pre_args]))
    188             I=f(I,**kwds)
    189             if option_set:

/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/gbcore.pyc in llfirst_pre(I, prot)
    223     
    224 def llfirst_pre(I,prot):
--> 225     (eliminated,llnf, I)=eliminate(I,on_the_fly=False,prot=prot)
    226     return (I,eliminated)
    227 

/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/ll.pyc in eliminate(polys, on_the_fly, prot, reduction_function, optimized)
    105         reduction_function=reduction_function,
    106         reduce_ll_system=(not on_the_fly),
--> 107         prot=prot)
    108   else:
    109       reductors=ll_encode(linear_leads,reduce=(not on_the_fly),prot=prot)

/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/ll.pyc in eliminate_ll_ranked(ll_system, to_reduce, reduction_function, reduce_ll_system, prot)
    153       from_ring.set()
    154       
--> 155   map_from_vec=construct_map_by_indices(to_ring, map_from_indices)
    156   map_back_vec=construct_map_by_indices(from_ring, map_back_indices)
    157   def map_from(p):

/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/polybori/ll.pyc in construct_map_by_indices(to_ring, idx_mapping)
    121   v=BoolePolynomialVector(to_ring.n_variables()*[to_ring.zero()])
    122   for (from_idx, to_idx) in idx_mapping.iteritems():
--> 123       v[from_idx]=to_ring.var(to_idx)
    124   return v
    125 

/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/sage/rings/polynomial/pbori.so in sage.rings.polynomial.pbori.BooleanPolynomialVector.__setitem__ (sage/rings/polynomial/pbori.cpp:29608)()

/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/sage/rings/polynomial/pbori.so in sage.rings.polynomial.pbori.BooleanPolynomialRing.__call__ (sage/rings/polynomial/pbori.cpp:7107)()

/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/sage/structure/parent_old.so in sage.structure.parent_old.Parent._coerce_c (sage/structure/parent_old.c:3561)()

/home/mariah/sage/sage-4.5.2-x86_64-Linux-core2-fc/local/lib/python2.6/site-packages/sage/rings/polynomial/pbori.so in sage.rings.polynomial.pbori.BooleanPolynomialRing._coerce_c_impl (sage/rings/polynomial/pbori.cpp:6209)()

ValueError: cannot coerce polynomial y2 to Boolean PolynomialRing in y5, y7, y8, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16, y17, y18, y19: name y0 not defined
sage: 
```


Issue created by migration from https://trac.sagemath.org/ticket/9842





---

archive/issue_comments_096971.json:
```json
{
    "body": "I just ran this code on sage 4.6 on both a linux machine (sage.math) and my machine, which is MAC OS 10.6 64 bit. And it seems to be working fine.",
    "created_at": "2011-01-08T01:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9841#issuecomment-96971",
    "user": "https://trac.sagemath.org/admin/accounts/users/gagansekhon"
}
```

I just ran this code on sage 4.6 on both a linux machine (sage.math) and my machine, which is MAC OS 10.6 64 bit. And it seems to be working fine.



---

archive/issue_comments_096972.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-08T01:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9841#issuecomment-96972",
    "user": "https://trac.sagemath.org/admin/accounts/users/gagansekhon"
}
```

Resolution: fixed



---

archive/issue_events_009967.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/gagansekhon",
    "created_at": "2011-01-08T01:12:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9841",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9841#event-9967"
}
```



---

archive/issue_comments_096973.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2011-01-08T02:08:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9841#issuecomment-96973",
    "user": "https://trac.sagemath.org/admin/accounts/users/gagansekhon"
}
```

Changing status from closed to needs_work.



---

archive/issue_events_009968.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/gagansekhon",
    "created_at": "2011-01-08T02:08:40Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/9841",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9841#event-9968"
}
```



---

archive/issue_comments_096974.json:
```json
{
    "body": "Replying to [comment:2 gagansekhon]:\nI didn't know stating resolved would close the ticket. I just email Jeroen to close the ticket instead since he is the release manger.",
    "created_at": "2011-01-08T02:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9841#issuecomment-96974",
    "user": "https://trac.sagemath.org/admin/accounts/users/gagansekhon"
}
```

Replying to [comment:2 gagansekhon]:
I didn't know stating resolved would close the ticket. I just email Jeroen to close the ticket instead since he is the release manger.



---

archive/issue_events_009969.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-08T05:11:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9841",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9841#event-9969"
}
```



---

archive/issue_comments_096975.json:
```json
{
    "body": "Resolution changed from fixed to worksforme",
    "created_at": "2011-01-08T05:11:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9841#issuecomment-96975",
    "user": "https://github.com/jdemeyer"
}
```

Resolution changed from fixed to worksforme



---

archive/issue_comments_096976.json:
```json
{
    "body": "Fixed in sage-4.6, probably because of the Singular update.",
    "created_at": "2011-01-08T05:11:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9841#issuecomment-96976",
    "user": "https://github.com/jdemeyer"
}
```

Fixed in sage-4.6, probably because of the Singular update.



---

archive/issue_comments_096977.json:
```json
{
    "body": "This would have possibly involved PolyBori (not singular), or something involving coercion that doesn't involve external libraries (?).",
    "created_at": "2011-01-08T19:08:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9841#issuecomment-96977",
    "user": "https://github.com/williamstein"
}
```

This would have possibly involved PolyBori (not singular), or something involving coercion that doesn't involve external libraries (?).
