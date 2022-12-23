# Issue 3934: Eta product modular functions

Issue created by migration from https://trac.sagemath.org/ticket/3934

Original creator: davidloeffler

Original creation time: 2008-08-23 11:46:53

Assignee: davidloeffler

At the Heilbronn Institute workshop "Computations with Modular Forms", Ken McMurdy requested code for handling eta products on X_0(N). Theory background and wish-list here: http://maths.pratum.net/CMF/resources/McMurdyTalk.pdf.


---

Comment by davidloeffler created at 2008-08-23 11:56:07

Changing status from new to assigned.


---

Attachment

First version: patch against sage 3.1.1


---

Comment by cremona created at 2008-08-24 17:51:29

Patch applies fine to 3.1.1.  Doctests for the new file pass.

Problem:  doctesting all in sage/modular, some strange errors appear in modular/abvar to do with latex.  They went away when I deleted the line "... import latex" in the new file, which is not actually used anyway.

In the constructor, in checking Ligozat, you loop over divisors of N.  Would it not be faster to loop over the keys in the dict?  There is then no need to factor N, or to look at (however briefly) the divisors which are not in the dict.

There is something similar at line 146.  Instead of 

```
 eta_n = max([ (n/d).floor() for d in divisors(self.level()) if self.r(d) != 0])
```

you could write 

```
 eta_n = max([ (n/d).floor() for d in self.r().keys()]) 
```


If you really wanted to have the full list of divisors of the level around, you could compute it and cache the result in the constructor.

In the function r(d) you can just say

```
   return self._rdict.get(d,0)
```

since the get function on a dict returns the value if the key is there or a default value (here 0) if not.

That's all I have time for now: I got as far as line 235 (def basis_eta_products).


---

Comment by davidloeffler created at 2008-08-26 18:00:35

Thanks very much for the comments. Since that first version was written I have realised a much better way of fitting the code into Sage's object hierarchy; I will combine that with your suggestions and submit a new version.


---

Attachment


---

Comment by davidloeffler created at 2008-08-27 14:23:30

OK, here's a second attempt (patch to be installed on top of the first attempt). I've refactored it extensively, creating a new class EtaGroup which is the parent of eta product objects; changed it so it doesn't use divisors() unless it really has to; and added a new module-level function eta_poly_relations which finds polynomial relations between two eta products.


---

Comment by cremona created at 2008-08-27 14:50:23

Replying to [comment:5 davidloeffler]:
> OK, here's a second attempt (patch to be installed on top of the first attempt). I've refactored it extensively, creating a new class EtaGroup which is the parent of eta product objects; changed it so it doesn't use divisors() unless it really has to; and added a new module-level function eta_poly_relations which finds polynomial relations between two eta products.

Excellent -- I will review this right away.  John


---

Comment by cremona created at 2008-08-27 15:36:56

Apply after the previous two patches


---

Attachment

Review summary:  This is a great piece of work, especially after the second patch.  I have made a few changes, detailed below, which are in the 3rd patch.

    * I changed the type-checking of the level parameter so that it forces it to be a Sage integer.  This is a good idea since some integer methods would not work if the level was a Python integer, and it also allows you to say `EtaGroup_class(4/2)` should you ever want to.

    * docstring for EtaGroup_class.basis() had a spurious redundant INPUT line (N)

    * I added a little more type and value checking of parameters

    * In  eta_poly_relations there is a lot of output which cannot be turned off.   Why not include a parameter verbose, default False, and only print the output if it is True?  I put this in and changed the doctests accordingly.

    * I commented out the NotImplemented plot function, as it seemed pointless to have it!

Coverage test gives this:

```
 ./sage -coverage devel/sage-eta/sage/modular/etaproducts.py 

devel/sage-eta/sage/modular/etaproducts.py
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE devel/sage-eta/sage/modular/etaproducts.py: 74% (23 of 31)

Missing documentation:
	 * __init__(self, level)
	 * _repr_(self)
	 * __call__(self, dict)
	 * __init__(self, parent, rdict)
	 * __cmp__(self, other)
	 * __eq__(self, other)
	 * _short_repr(self)
	 * _eta_relations_helper(eta1, eta2, degree, qexp_terms, labels, verbose)


Possibly wrong (function name doesn't occur in doctests):
	 * _mul_(self, other)
	 * _div_(self, other)
	 * _repr_(self)
	 * _repr_(self)
```

I have never been sure about the loads(dumps) message.  Apart from that all functions which are not preceded by an underscore have docstrings and doctests, which is the main thing:  it would be better if they had a little documentation, but then you'll get the complaint that they should also have doctests.


Conclusion:  I am very happy with this, but it would be even better if someone who knows a lot more about eta products (such as Ken McMurdy) could put it through its paces.


---

Comment by mabshoff created at 2008-09-23 00:19:14

Ok, anything going on here? The patches here have been bitrotting for a while and it would be nice if someone wrote the missing doctests. In order to have the right report pick it up I am renaming it to "needs work".

Cheers,

Michael


---

Comment by cremona created at 2008-09-23 08:07:21

David,

If you are happy with the additions I made then we can get this accepted soon.  I have not yet tried applying the patches to 3.1.3.*.  John


---

Comment by davidloeffler created at 2008-09-23 09:33:37

I'm very happy with John's changes. I've sent a copy to Ken McMurdy for review; he said he'll reply by September 26th. I doubt that bit rot will be a problem with this one as it's a single new source file which is entirely self-contained.

I'll get to work on the missing doctests and post a new patch.

David


---

Attachment

I've added doctests for the underscore methods, and a loads(dumps()) test; sage -coverage now returns 100%.


---

Comment by cremona created at 2008-09-23 11:15:26

Excellent!  I just checked that the sequence of 4 patches applies cleanly to 3.1.3.alpha0, and all tests in sage/modular pass.

Let it roll: even if Ken McMurdy suggests changes and additions, why not merge this now?

I'll inform Lloyd, Gabor and Lassina about this once it is merged, since it sefinitely a success story coming out of their August workshop.


---

Comment by was created at 2008-10-23 16:18:03

Cremona gave this a positive review (above), so I'm changing the heading.


---

Comment by was created at 2008-10-23 16:18:21

I'm also changing this to target 3.2


---

Comment by mabshoff created at 2008-10-26 04:06:40

Merged all four patches in Sage 3.2.alpha1


---

Comment by mabshoff created at 2008-10-26 04:06:40

Resolution: fixed
