# Issue 9841: groebner basis bug

Issue created by migration from https://trac.sagemath.org/ticket/9842

Original creator: mariah

Original creation time: 2010-08-30 19:39:26

Assignee: malb

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



---

Comment by gagansekhon created at 2011-01-08 01:12:17

I just ran this code on sage 4.6 on both a linux machine (sage.math) and my machine, which is MAC OS 10.6 64 bit. And it seems to be working fine.


---

Comment by gagansekhon created at 2011-01-08 01:12:17

Resolution: fixed


---

Comment by gagansekhon created at 2011-01-08 02:08:40

Changing status from closed to needs_work.


---

Comment by gagansekhon created at 2011-01-08 02:09:54

Replying to [comment:2 gagansekhon]:
I didn't know stating resolved would close the ticket. I just email Jeroen to close the ticket instead since he is the release manger.


---

Comment by jdemeyer created at 2011-01-08 05:11:17

Resolution changed from fixed to worksforme


---

Comment by jdemeyer created at 2011-01-08 05:11:17

Fixed in sage-4.6, probably because of the Singular update.


---

Comment by was created at 2011-01-08 19:08:15

This would have possibly involved PolyBori (not singular), or something involving coercion that doesn't involve external libraries (?).
