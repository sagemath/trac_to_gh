# Issue 1083: Bug in degree 0 number fields; manifests itself in element.matrix(), .trace(), .norm(), etc

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2007-11-03 20:06:48

Assignee: was

Keywords: number fields matrix trace norm extension

The following is not correct:

sage: K.<a> = NumberField(ZZ['x'].0^2 + 2, 'a')
sage: L.<b> = K.extension(ZZ['x'].0 - a, 'b')
sage: L
Number Field in b with defining polynomial x - a over its base field
sage: L(a)
0

This is the root of the following bugs:

sage: a.trace(K)
sage: a.norm(K)
sage: a.matrix(K)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)
... (snipped) ...
/Users/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py in relativize(self, alpha, names)
   2902                     # self --> M that sends alpha to
   2903                     # the generator of the intermediate field.
-> 2904                     from_M = M.hom([self.gen()], self, check=True)
   2905                     M._set_structure(from_M, to_M)  # don't have to
   2906                                                     # worry about caching since relative number fields aren't cached.

/Users/ncalexan/Documents/School/MATH235/groebner/parent_gens.pyx in sage.structure.parent_gens.ParentWithGens.hom()

/Users/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/morphism.py in __call__(self, im_gen, base_hom, check)
    172         if check:
    173             im_gen = self.codomain()(im_gen)
--> 174         return self._from_im(im_gen, base_hom)
    175 
    176     def _coerce_impl(self, x):

/Users/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/morphism.py in _from_im(self, im_gen, base_hom)
    197         f = R([base_hom(x) for x in a.list()])
    198         b = f(im_gen)
--> 199         abs_hom = K.hom([b])
    200         return RelativeNumberFieldHomomorphism_from_abs(self, abs_hom)
    201 

/Users/ncalexan/Documents/School/MATH235/groebner/parent_gens.pyx in sage.structure.parent_gens.ParentWithGens.hom()

/Users/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/morphism.py in __call__(self, im_gens, check)
     30                 return self._coerce_impl(im_gens)
     31             except TypeError:
---> 32                 raise TypeError, "images do not define a valid homomorphism"
     33         
     34     def _coerce_impl(self, x):

<type 'exceptions.TypeError'>: images do not define a valid homomorphism


---

Comment by ncalexan created at 2007-11-03 20:09:13

Argh, that should be


```
sage: K.<a> = NumberField(ZZ['x'].0^2 + 2, 'a')
sage: L.<b> = K.extension(ZZ['x'].0 - a, 'b')
sage: L
Number Field in b with defining polynomial x - a over its base field
sage: L(a)
0
```



---

Comment by craigcitro created at 2008-01-21 11:55:58

Changing assignee from was to craigcitro.


---

Comment by craigcitro created at 2008-01-21 11:55:58

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-01-21 11:55:58

Man, this was a *bugger* to find. Here's the issue: at some point, we ask Pari to turn an absolute element into a relative element in a relative extension of degree n for us, and then we loop over the resulting polynomial from indices 0 to n-1 and add up some stuff. In the case that the relative extension is degree 1, Pari fails to do this correctly -- they don't reduce the polynomial below degree 1, which is what causes the trouble. The code proceeds to loop over just the 0th coefficient, which is just 0 in the example above. 

Interestingly, the problem here only occurs when you try to *print* your element -- you can create the element just fine, it's only when you try and print it that this zeroing occurs. (This was why I had so much trouble finding it.)

I have a fix for this, but I've also reported the bug to the Pari folks -- given that this doesn't seem terribly pressing, if they're going to fix it upstream, it seems like just waiting would be the best approach. If I don't hear anything from them in a few days, I'll post a patch.


---

Comment by craigcitro created at 2008-01-22 03:05:41

I just looked at the title of this, and noticed the 0 should be a 1.


---

Comment by ncalexan created at 2008-01-22 18:05:06

Good work, Craig Citro!  I spent hours tracking it as far as I did, too -- it was a strange bug, that's for sure.


---

Attachment

So I got a response from the pari team that the problem on their end is fixed in svn. However, given the fact that the Pari release cycle is slower than ours, I've added a workaround to Sage. Looking at the other tests Nick had above, I noticed that for any NumberFieldElement a, a.matrix(QQ) didn't work. I fixed this while I was there, and added a few doctests.


---

Comment by ncalexan created at 2008-01-27 04:27:12

Apply!  My only worry is that there is no reference, in the code, to the PARI bug, but maybe that is better?


---

Comment by mabshoff created at 2008-01-27 04:32:55

#1891 is the ticket to remove the work around once the fix is in upstream pari.


---

Comment by mabshoff created at 2008-01-27 05:14:26

Resolution: fixed


---

Comment by mabshoff created at 2008-01-27 05:14:26

Merged in Sage 2.10.1.rc1
