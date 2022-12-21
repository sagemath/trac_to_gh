# Issue 6124: Bug in galois_group of a p-adic field extension

Issue created by migration from Trac.

Original creator: jlefebvre

Original creation time: 2009-05-24 14:41:03

Assignee: was

Keywords: p-adic

A bug in the implementation of p-adic groups.

sage: K.<a> = Qp(2).extension(x^3 + x^2+1)
sage: K.galois_group()
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

/Users/jeromelefebvre/.sage/temp/Jerome.local/23278/_Users_jeromelefebvre__sage_init_sage_0.py in <module>()

/Applications/sage/local/lib/python2.5/site-packages/sage/rings/padics/unramified_extension_generic.pyc in galois_group(self)
     96         ## doing this.
     97         ##
---> 98         from sage.groups.perm_gps.permgroup import CyclicPermutationGroup
     99         return CyclicPermutationGroup(self.modulus().degree())
    100 

ImportError: cannot import name CyclicPermutationGroup


While, CyclicPermutationGroup does work fine on my machine.
sage: G=CyclicPermutationGroup(2)
sage: G.list()
[(), (1,2)]


---

Comment by AlexGhitza created at 2009-05-25 01:53:41

Changing assignee from was to roed.


---

Comment by AlexGhitza created at 2009-05-25 01:53:41

Changing component from number theory to padics.


---

Comment by AlexGhitza created at 2009-05-25 01:53:41

Note that in sage-4.0.rc0, there is no `galois_group` method for an extension of `Qp`:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: K.<a> = Qp(2).extension(x^3 + x^2+1)
sage: K.g    # tried to tab-complete here:
K.gcd                   K.gens                  K.get_action            K.get_action_impl       K.ground_ring_of_tower  
K.gen                   K.gens_dict             K.get_action_c          K.ground_ring           
```



---

Comment by jlefebvre created at 2009-06-11 15:01:40

Same thing for Sage 4.0.1. It would be cool if there was some galois group computations, but that's an other issue.
So, it looks like this trac should be closed.
Thanks for looking into it.


---

Comment by roed created at 2011-11-09 03:21:09

Changing status from new to needs_review.


---

Comment by roed created at 2011-11-09 03:21:09

This ticket should be closed.


---

Comment by roed created at 2011-11-19 04:25:52

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-11-26 13:05:13

Resolution: invalid
