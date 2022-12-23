# Issue 5618: Cyclotomic field elements are not convert to Gap correctly.

Issue created by migration from https://trac.sagemath.org/ticket/5618

Original creator: saliola

Original creation time: 2009-03-26 19:40:53

Assignee: tbd

CC:  joyner

Although this works:

```
sage: K = CyclotomicField(3)
sage: z = K.an_element(); z
zeta3
sage: gap(z)
zeta3
```

the resulting gap element doesn't have the correct properties:

```
sage: K(gap.E(3)) == z  # Good!
True
sage: gap(K(gap.E(3))) == gap.E(3)  # Bad!
False
```


This causes the following problem with group characters.

```
sage: H = AlternatingGroup(4)
sage: g = H.list()[1]
sage: K = H.subgroup([g])
sage: z = CyclotomicField(3).an_element(); z
sage: c = K.character([1,z,z**2])
...
RuntimeError: Gap produced error output
Error, no 1st choice method found for `CONDUCTOR' on 1 arguments
```

Note: the above works if one takes z = gap.E(3).


---

Comment by SimonKing created at 2010-07-03 11:12:01

Here is some problem analysis:

```
sage: K = CyclotomicField(3)
sage: z = K.an_element(); z
zeta3
sage: gap(z)
zeta3
sage: K(gap(z))
zeta3
sage: gap.E(3)
E(3)
sage: gap.E(3) == gap(z)
False
sage: K(gap.E(3)) == K(gap(z)) == z
True
```


So, apparently GAP treats "the same" elements of a cyclotomic field differently if they have different names. But this isn't particularly surprising, since the two cyclotomic fields seem to have a totaly different representation in GAP:

```
sage: ZFgap = gap('CyclotomicField(3)')
sage: Kgap = gap(K)
sage: Kgap
<algebraic extension over the Rationals of degree 2>
sage: ZFgap
CF(3)
sage: ZFgap.GeneratorsOfField()
[ E(3) ]
sage: Kgap.GeneratorsOfField()
[ zeta3 ]
```


Note that comparison of the two field in the GAP interface results in an error:


```
sage: Kgap == ZFgap
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (47, 0))

---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/home/king/<ipython console> in <module>()

/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__richcmp__ (sage/structure/element.c:7061)()

/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element._richcmp (sage/structure/element.c:6943)()

/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __cmp__(self, other)
   1527                                  other.name())) == P._true_symbol():
   1528             return 0
-> 1529         elif P.eval("%s %s %s"%(self.name(), P._lessthan_symbol(), other.name())) == P._true_symbol():
   1530             return -1
   1531         elif P.eval("%s %s %s"%(self.name(), P._greaterthan_symbol(), other.name())) == P._true_symbol():

/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/interfaces/gap.pyc in eval(self, x, newlines, strip, **kwds)
    478             input_line += ';'
    479
--> 480         result = Expect.eval(self, input_line, **kwds)
    481
    482         if not newlines:

/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in eval(self, code, strip, synchronize, locals, **kwds)
    981         try:
    982             with gc_disabled():
--> 983                 return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
    984         except KeyboardInterrupt:
    985             # DO NOT CATCH KeyboardInterrupt, as it is being caught

/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/interfaces/gap.pyc in _eval_line(self, line, allow_use_file, wait_for_prompt)
    720                         return ''
    721                 else:
--> 722                     raise RuntimeError, message
    723
    724         except KeyboardInterrupt:

RuntimeError: Gap produced error output
Error, no 1st choice method found for `LT' on 2 arguments

   executing $sage2 < $sage8;
```


But GAP indeed considers the two fields to be different:

```
sage: gap.eval(Kgap.name() + ' = ' + ZFgap.name())
'false'
```


So, what does all this mean?

 1. The `__cmp__` method of the GAP interface has a bug. An error raised by GAP when attempting "<" or ">" should be caught and then "=" should be tried.
 2. A GAP cyclotomic field is different from the GAP version of a Sage cyclotomic field. This is since the GAP version of a Sage cyclotomic field is a number field. It could be solved by providing a genuine `_gap_init_` method for Sage cyclotomic fields (currently, it is inherited from number fields).

It seems likely to me that after implementing 2., things will already work. But 1. should be fixed as well.


---

Comment by SimonKing created at 2010-07-04 18:30:49

Gap-representation of Cyclotomic Fields should be a Cyclotomic Field in Gap


---

Comment by SimonKing created at 2010-07-04 18:46:22

Changing status from new to needs_review.


---

Comment by SimonKing created at 2010-07-04 18:46:22

Changing keywords from "" to "gap interface cyclotomic field".


---

Attachment

I created the patch after the patches from #8909 and #9423 -- so, it is possible that the new patch actually depends on the two other tickets (but one of them already has a positive review).

With the patch, a cyclotomic field in Sage is represented as a cyclotomic field (and not as a number field) in GAP:

```
sage: Z = CyclotomicField(8)
sage: gap(Z)
CF(8)
sage: Z(gap(Z.0^2))
zeta8^2
```


The advantage is that the motivating example from the ticket description now works (and is used as a doctest):

```
sage: H = AlternatingGroup(4)
sage: g = H.list()[1]
sage: K = H.subgroup([g])
sage: z = CyclotomicField(3).an_element(); z
sage: c = K.character([1,z,z**2]); c
Character of Subgroup of AlternatingGroup(4) generated by [(2,3,4)]
sage: c(g^2); z^2
-zeta3 - 1
-zeta3 - 1
```


The disadvantage: While it is still possible to chose the name of a number field generator in GAP as in Sage

```
sage: K.<tau> = NumberField(x^2+x+1)
sage: gap(K)
<algebraic extension over the Rationals of degree 3>
sage: K.0
tau
sage: gap(K.0)
tau
```

it is now impossible to do the same for cyclotomic fields:

```
sage: L.<zeta> = CyclotomicField(3)
sage: L.0
zeta
sage: gap(L.0)
E(3)
```


By consequence, I had to fix a couple of doctests. All doctests pass, but I can not vouch for external code.


---

Comment by lftabera created at 2010-12-04 16:19:15

Changing status from needs_review to needs_work.


---

Comment by lftabera created at 2010-12-04 16:19:15

The patch simply converts sage Cyclotomic fields to gap cyclotomic fields instead of generic number fields. The disadvantage presented is just a limitation of gap, not sage.

The semantics of gap(CyclotomicField(n)) have changed!
DeprecationWarning would be too pedantic here. Current behaviour of sage is considered a bug and I cannot see any functionality loss. So the code is ok.

The doctests are relevant. However, this patch depends on #9423 and one doctest has disappeared in that patch. That doctest is relevant, because it shows the change in the code. So, I would add the output of:


```
sage: F=CyclotomicField(8)
sage: F.gen()
sage: F._gap_init_() # the following variable name $sage1 represents the F.base_ring() in gap and is somehow random
sage: f=gap(F)
sage: f.GeneratorsOfDivisionRing() 
```


in NumberField_cyclotomic._gap_init_()


---

Attachment

updated headers


---

Comment by lftabera created at 2010-12-29 14:30:47

additional doctest


---

Comment by lftabera created at 2010-12-29 14:34:16

Changing status from needs_work to needs_review.


---

Attachment

I give a positive review to Simon's patch. However, I have added some doctest in trac_5618_gap_for_cyclotomic_fields_doctest.patch that needs review. The doctest are in the unpatched code, but they have disappeared in the process. This patch put them back.

Apply:

trac_5618_gap_for_cyclotomic_fields.2.patch

trac_5618_gap_for_cyclotomic_fields_doctest.patch

Depends on: #9423


---

Comment by mhampton created at 2011-01-11 06:41:19

Should this be marked positive review then?


---

Comment by lftabera created at 2011-01-11 08:52:27

If you agreee with the doctest I wrote back in http://trac.sagemath.org/sage_trac/ticket/5618 yes, it should have a positive review.


---

Comment by davidloeffler created at 2011-01-19 16:08:42

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2011-01-19 16:08:42

The doctest looks fine to me. Let's get this in. (I'm not going to claim reviewer credit for this one -- I just verified that the doctest was the same as the one removed from #9423.)


---

Comment by jdemeyer created at 2011-01-25 08:13:50

Resolution: fixed
