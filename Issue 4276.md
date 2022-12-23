# Issue 4276: [with patch, needs review] move number fields to new coercion, implement embeddings

Issue created by migration from https://trac.sagemath.org/ticket/4276

Original creator: robertwb

Original creation time: 2008-10-13 19:27:47

Assignee: robertwb

CC:  craigcitro was




---

Comment by robertwb created at 2008-10-13 21:29:53

I'll actually upload the patches when I'm on a stable enough connection to do so...


---

Attachment


---

Attachment


---

Attachment


---

Attachment

To help possible reviewers of what looks like very useful and good stuff, would it be possible to write a few words about what is going on here?

By the way, the second patch does not view properly whan I click on it.  I don't know why.


---

Comment by robertwb created at 2008-10-28 07:30:26

Yes, I explained this to some people at Sage Days 10, but it certainly could use some explanation here. 

These patches move coercion over to the new api, which is (hopefully) easier to understand and use as well as being faster. As part of this move, we also get the benefit of being able to specify embeddings at creation time, into RR or CC being the most common. (The embeddings into RR and CC are by default into "lazy" fields so the path can be followed to a field of any precision.) Cyclotomic fields and fields created with the "QuadraticField" command come with their standard embeddings. 

A field with an embedding can do arithmetic with its ambient field, and if two number fields have an embedding into a common field than elements can be moved from one to the other as well. Here is a brief example (though more can be found in the documentation): 


```
sage: L.<a> = QuadraticField(-3)
sage: a + 1.5
1.50000000000000 + 1.73205080756888*I
sage: a + 1.50000000000000000000000000000000000000
1.50000000000000000000000000000000000000 + 1.73205080756887729352744634150587236694*I
sage: K.<zeta> = CyclotomicField(12)
sage: K(a)
2*zeta^7 + 1

sage: L.<b> = NumberField(x^5-x+1, embedding=-1.1)
sage: b in RR
True
sage: RR(b)
-1.16730397826142
sage: RealField(200)(b)
-1.1673039782614186842560458998548421807205603715254890391401
sage: RealField(200)(b^2-5)
-3.6374014223350653758204435726195439793325331732024834332371
sage: RealField(200)(b^5-b+1)
0.00000000000000000000000000000000000000000000000000000000000
```


This also paves the path for more sophisticated arithmetic, like automatic compositums.


---

Comment by davidloeffler created at 2008-11-14 09:30:39

I downloaded these patches not so much in order to review them but because I wanted to see if they would conflict with any changes I might make in order to fix #4193. 

Anyway, they apply and build fine (eventually) under 3.1.4. Testing number_field/ passes except for a minor numerical noise issue:

```
**************************************************
File "/home/david/sage-current/tmp/number_field_morphisms.py", line 223:
    sage: closest_root(x^3-1, CDF.0)
Expected:
    -0.500000000000000 + 0.866025403784439*I
Got:
    -0.500000000000000 + 0.866025403784438*I
**********************************************************************
```


But I can't really do much to test the new functionality, since I'm not sure what it's supposed to do. You say above "here is a brief example (though more can be found in the documentation)" but I can't see any; all of the various number field constructors now accept an embedding parameter but there's no explanation or tests in the docstrings. Can we have a bit of demystification?


---

Comment by robertwb created at 2008-11-14 19:10:22

Thank you for taking a look at this. I really don't want these patches to bitrot. I will try to post another patch with more docstrings. 

Essentially, the embedding is a specified coercion into another field (typically RR or CC, though  embeddings to any other field can be specified). This should make what you're trying to do at #4193 trivial (or at least very easy). The embedding parameter specifies where the generator of the number field should land (the closest root being taken if the root is not exact). So by doing 


```
sage: L.<b> = NumberField(x^5-x+1, embedding=-1.1)
```


I am saying I want the number filed defined by `x^5-x+1` *with* the embedding into RR defined by sending the generator to the root (closest to) -1.1. You can test this by calling `RR(b)` or RR(some other element of K) and doing stuff like `b+1.5` whose result should be about 0.4.  Given two number fields K and L with embedding into (say) CC, one now gets for free morphisms between (subsets of) K and L.


---

Attachment

OK, I've attached some more documentation on embeddings. Also, since this is a coercion ticket, one of the main points of testing it is to make sure things still work like they used to.


---

Comment by davidloeffler created at 2008-11-16 07:19:05

Thanks for clarifying things there. Your new docstrings assert that cyclotomic fields all have their usual embeddings so coercion between them should work, but I'm slightly concerned by the following non-associativity of addition: 


``` 
sage: K5.<zeta5> = CyclotomicField(5)
sage: K7.<zeta7> = CyclotomicField(7)
sage: K35.<zeta35> = CyclotomicField(35)
sage: (-zeta35 + zeta7) + (zeta5 + zeta35)
zeta35^7 + zeta35^5
sage: -zeta35 + (zeta7 + zeta5) + zeta35
TypeError: unsupported operand parent(s) for '+': 'Cyclotomic Field of order 5 and degree 4' and 'Cyclotomic Field of order 7 and degree 6'
```


This problem is not in any way new, and existed before your patches; but shouldn't your patches fix it?


---

Comment by robertwb created at 2008-11-16 07:41:26

No, my patch does not automatically compute compositums, just coercions one direction or the other. This should be done, is on my (long) todo list, and of course is especially easy for cyclotomic fields, but this ticket is big enough already...

Note that Sage does not guarantee associativity of addition. Consider


```
sage: ZZ['t,x'].0 + ZZ['x'].0 + ZZ['t'].0
2*t + x
sage: ZZ['t,x'].0 + (ZZ['x'].0 + ZZ['t'].0)
Traceback (most recent call last):
...
TypeError: unsupported operand parent(s) for '+': 'Univariate Polynomial Ring in x over Integer Ring' and 'Univariate Polynomial Ring in t over Integer Ring'
```


This is because there is an ambiguous ordering of the variables if the rightmost addition is performed first. What should be true, however, is if both operations succeed then they should give equal answers.


---

Comment by ncalexan created at 2008-11-30 06:33:31

I am trying to referee this, but it's going to take some time.  I'm going to put it into my tree and try to move some of my code that does this by hand to the embedding architecture.  Email me in a month.

I have some questions and problems:

I really need to be able to specify embeddings after creation, because *tons* of functions create number fields (composite_fields, for example, or subfields) and I really don't want to specify all possible embeddings of the results...

First, why squarefree_part bounded?  This could be a separate patch.

Second, I can specify non-embeddings that seem to be ignored:


```
sage: K.<a> = NumberField(x^3+2, embedding=CC(-10).nth_root(3))
sage: K.coerce_embedding()

Generic morphism:
  From: Number Field in a with defining polynomial x^3 + 2
  To:   Complex Lazy Field
  Defn: a -> 0.6299605249474365? + 1.091123635971722?*I
sage: K.gen_embedding()^3
-2.00000000000000? + 0.?e-14*I
```


Finally, I am having lots of trouble creating non-default embeddings:


```
sage: K2.<a> = NumberField(x^2 + 2, 'a', embedding=RR(-sqrt(2)))
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/Users/ncalexan/.sage/temp/mero.local/25160/_Users_ncalexan__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in NumberField(polynomial, name, check, names, cache, embedding)
    369 
    370     if polynomial.degree() == 2:
--> 371         K = NumberField_quadratic(polynomial, name, check, embedding)
    372     else:
    373         K = NumberField_absolute(polynomial, name, None, check, embedding)

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in __init__(self, polynomial, name, check, embedding)
   6470             Number Field in a with defining polynomial x^2 - 4
   6471         """
-> 6472         NumberField_absolute.__init__(self, polynomial, name=name, check=check, embedding=embedding)
   6473         self._element_class = number_field_element_quadratic.NumberFieldElement_quadratic
   6474         c, b, a = [rational.Rational(t) for t in self.defining_polynomial().list()]

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in __init__(self, polynomial, name, latex_name, check, embedding)
   3649         NumberField_generic.__init__(self, polynomial, name, latex_name, check, embedding)
   3650         self._element_class = number_field_element.NumberFieldElement_absolute
-> 3651         self._zero_element = self(0)
   3652         self._one_element =  self(1)
   3653 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3665)()
    277 
    278 
--> 279 
    280 
    281 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.convert_map_from (sage/structure/parent.c:8640)()
   1000 
   1001 
-> 1002 
   1003 
   1004 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.discover_convert_map_from (sage/structure/parent.c:8771)()
   1007 
   1008 
-> 1009 
   1010 
   1011 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.coerce_map_from (sage/structure/parent.c:7653)()
    876 
    877 
--> 878 
    879 
    880 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.discover_coerce_map_from (sage/structure/parent.c:7956)()
    921 
    922 
--> 923 
    924 
    925 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent_old.so in sage.structure.parent_old.Parent._coerce_map_from_ (sage/structure/parent_old.c:6291)()
    576 
    577 
--> 578 
    579 
    580 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in _coerce_map_from_(self, K)
   6497             return number_field_element_quadratic.Q_to_quadratic_field_element(self)
   6498         else:
-> 6499             return NumberField_absolute._coerce_map_from_(self, K)
   6500 
   6501 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in _coerce_map_from_(self, R)
   1525         """
   1526         if R in [int, long, ZZ, QQ, self.base()]:
-> 1527             return self._generic_convert_map(R)
   1528         from sage.rings.number_field.order import is_NumberFieldOrder
   1529         if is_NumberFieldOrder(R) and R.number_field().has_coerce_map_from(self):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent_old.so in sage.structure.parent_old.Parent._generic_convert_map (sage/structure/parent_old.c:6841)()
    594 
    595 
--> 596 
    597 
    598 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent_old.so in sage.structure.parent_old.Parent._generic_convert_map (sage/structure/parent_old.c:6806)()
    602 
    603 
--> 604 
    605 
    606 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent._generic_convert_map (sage/structure/parent.c:6875)()
    747 
    748 
--> 749 
    750 
    751 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap.__init__ (sage/structure/coerce_maps.c:1931)()
     22 
     23 
---> 24 
     25 
     26 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/categories/map.so in sage.categories.map.Map.__init__ (sage/categories/map.c:1768)()
     39 
     40 
---> 41 
     42 
     43 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/categories/homset.pyc in Hom(X, Y, cat)
    151             
    152     ##_cache[key] = weakref.ref(H)
--> 153     _cache[(X, Y, cat)] = weakref.ref(H)
    154     
    155     return H

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in __cmp__(self, other)
   1639         else:
   1640             return cmp(self.coerce_embedding()(self.gen()),
-> 1641                        other.coerce_embedding()(other.gen()))
   1642 
   1643     def _ideal_class_(self):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/real_lazy.so in sage.rings.real_lazy.LazyBinop.__richcmp__ (sage/rings/real_lazy.c:7858)()
    868 
    869 
--> 870 
    871 
    872 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.Element._richcmp (sage/structure/element.c:5169)()
    530 
    531 
--> 532 
    533 
    534 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.Element._richcmp_c_impl (sage/structure/element.c:5400)()
    577 
    578 
--> 579 
    580 
    581 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/real_lazy.so in sage.rings.real_lazy.LazyFieldElement._cmp_c_impl (sage/rings/real_lazy.c:5445)()
    508 
    509 
--> 510 
    511 
    512 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/real_lazy.so in sage.rings.real_lazy.LazyFieldElement.approx (sage/rings/real_lazy.c:5880)()
    567 
    568 
--> 569 
    570 
    571 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/real_lazy.so in sage.rings.real_lazy.LazyBinop.eval (sage/rings/real_lazy.c:7427)()
    825 
    826 
--> 827 
    828 
    829 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/real_lazy.so in sage.rings.real_lazy.LazyBinop.eval (sage/rings/real_lazy.c:7439)()
    826 
    827 
--> 828 
    829 
    830 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/real_lazy.so in sage.rings.real_lazy.LazyAlgebraic.eval (sage/rings/real_lazy.c:10310)()
   1278 
   1279 
-> 1280 
   1281 
   1282 

IndexError: list index out of range
sage:
```



And even worse, non-embeddings. check the sign of sqrt(2) below)


```
sage: K1.<a> = NumberField(x^2 + 2, 'a', embedding=RR(sqrt(2)))
sage: K1.gen_embedding()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/Users/ncalexan/.sage/temp/mero.local/25160/_Users_ncalexan__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/IPython/Prompts.pyc in __call__(self, arg)
    549 
    550             # and now call a possibly user-defined print mechanism
--> 551             manipulated_val = self.display(arg)
    552             
    553             # user display hooks can change the variable to be stored in

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/IPython/Prompts.pyc in _display(self, arg)
    575             return IPython.generics.result_display(arg)
    576         except TryNext:            
--> 577             return self.shell.hooks.result_display(arg)
    578 
    579     # Assign the default display method:

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/IPython/hooks.pyc in __call__(self, *args, **kw)
    133             #print "prio",prio,"cmd",cmd #dbg
    134             try:
--> 135                 ret = cmd(*args, **kw)
    136                 return ret
    137             except ipapi.TryNext, exc:

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/IPython/hooks.pyc in result_display(self, arg)
    163     
    164     if self.rc.pprint:
--> 165         out = pformat(arg)
    166         if '\n' in out:
    167             # So that multi-line strings line up with the left column of

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python/pprint.pyc in pformat(self, object)
    109     def pformat(self, object):
    110         sio = _StringIO()
--> 111         self._format(object, sio, 0, 0, {}, 0)
    112         return sio.getvalue()
    113 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python/pprint.pyc in _format(self, object, stream, indent, allowance, context, level)
    127             self._readable = False
    128             return
--> 129         rep = self._repr(object, context, level - 1)
    130         typ = _type(object)
    131         sepLines = _len(rep) > (self._width - 1 - indent - allowance)

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python/pprint.pyc in _repr(self, object, context, level)
    193     def _repr(self, object, context, level):
    194         repr, readable, recursive = self.format(object, context.copy(),
--> 195                                                 self._depth, level)
    196         if not readable:
    197             self._readable = False

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python/pprint.pyc in format(self, object, context, maxlevels, level)
    205         and whether the object represents a recursive construct.
    206         """
--> 207         return _safe_repr(object, context, maxlevels, level)
    208 
    209 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python/pprint.pyc in _safe_repr(object, context, maxlevels, level)
    290         return format % _commajoin(components), readable, recursive
    291 
--> 292     rep = repr(object)
    293     return rep, (rep and not rep.startswith('<')), False
    294 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1090)()
     90 
     91 
---> 92 
     93 
     94 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/real_lazy.so in sage.rings.real_lazy.LazyFieldElement._repr_ (sage/rings/real_lazy.c:5833)()
    555 
    556 
--> 557 
    558 
    559 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/real_lazy.so in sage.rings.real_lazy.LazyFieldElement.approx (sage/rings/real_lazy.c:5880)()
    567 
    568 
--> 569 
    570 
    571 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/real_lazy.so in sage.rings.real_lazy.LazyBinop.eval (sage/rings/real_lazy.c:7427)()
    825 
    826 
--> 827 
    828 
    829 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/real_lazy.so in sage.rings.real_lazy.LazyBinop.eval (sage/rings/real_lazy.c:7439)()
    826 
    827 
--> 828 
    829 
    830 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/real_lazy.so in sage.rings.real_lazy.LazyAlgebraic.eval (sage/rings/real_lazy.c:10310)()
   1278 
   1279 
-> 1280 
   1281 
   1282 

IndexError: list index out of range
sage: 
```



---

Attachment

`4276-ncalexan.patch` applies to 3.2.1.alpha2 and aggregates all robertwb's patches.


---

Comment by davidloeffler created at 2008-12-01 14:29:00

Thanks very much, ncalexan, for taking over refereeing of this patch. I don't have the background to review something like this (my initial attempts above made me realise that) and I was worried that other more qualified people would now assume I had it under control.


---

Comment by robertwb created at 2008-12-02 12:29:29

> First, why squarefree_part bounded? This could be a separate patch.

Yes, in retrospect it could be. I moved that code out of the number field file, and while doing so decided to optimize it. 

> Second, I can specify non-embeddings that seem to be ignored:

I'm not sure what you're trying to show with your example. It picks the closest root (so one doesn't need to specify the root to an arbitrary precision). 

> Finally, I am having lots of trouble creating non-default embeddings:

`sage: K2.<a> = NumberField(x^2 + 2, 'a', embedding=RR(-sqrt(2)))`

I agree these tracebacks are bad, but it's having trouble deciding which of I*sqrt(2) or -I*sqrt(2) is closest to sqrt(2). I'll have it throw a more sensible error instead.


---

Attachment

Everything rebased against 3.2.1


---

Comment by robertwb created at 2008-12-02 13:01:35

I've rebased against 3.2.1. Still building, but I'm off to bed.


---

Comment by mabshoff created at 2008-12-02 15:47:22

With this patch and the one from #3623 applied I am seeing two doctest failures in 

```
sage -t -long devel/sage/sage/structure/coerce.pyx # 3 doctests failed
sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_number_field.py
```

The details are at #3623.

Cheers,

Michael


---

Comment by robertwb created at 2008-12-02 21:50:07

apply after the latest rebase


---

Attachment

The attached patch should address the issues.


---

Comment by mabshoff created at 2008-12-02 22:40:30

4276-nf-coerce-fixes.patch does also fix the doctest failure for me, so we finally have no more doctest failures with this and the two patches from #3623 applied.

Cheers,

Michael


---

Comment by ncalexan created at 2008-12-04 04:40:04

This code is good, it really is, but it's just not tested.  I don't have time right now to test it and I will be sans computer over the Christmas break.

I have to give this a negative review because I do not believe the embeddings work in anything more than the trivial situation: two absolute fields, compatible embeddings into CC.

On the other hand, I have no reservations about the coercion part of this patch.  Are we willing to accept almost certainly broken new functionality to have valuable infrastructure upgrades?


```
sage: L1 = NumberField(x^4 + 6*x^2 + 1, 'a', embedding=CC(5*I))
sage: NumberField(x^4 + 6*x^2 + 1, 'a', embedding=L1.gen())
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/ncalexan/.sage/temp/pv139196.reshsg.uci.edu/23733/_Users_ncalexan__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in NumberField(polynomial, name, check, names, cache, embedding)
    371         K = NumberField_quadratic(polynomial, name, check, embedding)
    372     else:
--> 373         K = NumberField_absolute(polynomial, name, None, check, embedding)
    374 
    375     if cache:

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in __init__(self, polynomial, name, latex_name, check, embedding)
   3655         NumberField_generic.__init__(self, polynomial, name, latex_name, check, embedding)
   3656         self._element_class = number_field_element.NumberFieldElement_absolute
-> 3657         self._zero_element = self(0)
   3658         self._one_element =  self(1)
   3659 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3665)()
    277 
    278 
--> 279 
    280 
    281 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.convert_map_from (sage/structure/parent.c:8640)()
   1000 
   1001 
-> 1002 
   1003 
   1004 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.discover_convert_map_from (sage/structure/parent.c:8771)()
   1007 
   1008 
-> 1009 
   1010 
   1011 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.coerce_map_from (sage/structure/parent.c:7653)()
    876 
    877 
--> 878 
    879 
    880 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.discover_coerce_map_from (sage/structure/parent.c:7956)()
    921 
    922 
--> 923 
    924 
    925 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent_old.so in sage.structure.parent_old.Parent._coerce_map_from_ (sage/structure/parent_old.c:6291)()
    576 
    577 
--> 578 
    579 
    580 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in _coerce_map_from_(self, R)
   1531         """
   1532         if R in [int, long, ZZ, QQ, self.base()]:
-> 1533             return self._generic_convert_map(R)
   1534         from sage.rings.number_field.order import is_NumberFieldOrder
   1535         if is_NumberFieldOrder(R) and R.number_field().has_coerce_map_from(self):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent_old.so in sage.structure.parent_old.Parent._generic_convert_map (sage/structure/parent_old.c:6841)()
    594 
    595 
--> 596 
    597 
    598 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent_old.so in sage.structure.parent_old.Parent._generic_convert_map (sage/structure/parent_old.c:6806)()
    602 
    603 
--> 604 
    605 
    606 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent._generic_convert_map (sage/structure/parent.c:6875)()
    747 
    748 
--> 749 
    750 
    751 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap.__init__ (sage/structure/coerce_maps.c:1931)()
     22 
     23 
---> 24 
     25 
     26 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/categories/map.so in sage.categories.map.Map.__init__ (sage/categories/map.c:1768)()
     39 
     40 
---> 41 
     42 
     43 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/categories/homset.pyc in Hom(X, Y, cat)
    151             
    152     ##_cache[key] = weakref.ref(H)
--> 153     _cache[(X, Y, cat)] = weakref.ref(H)
    154     
    155     return H

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in __cmp__(self, other)
   1645         else:
   1646             return cmp(self.coerce_embedding()(self.gen()),
-> 1647                        other.coerce_embedding()(other.gen()))
   1648 
   1649     def _ideal_class_(self):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/real_lazy.so in sage.rings.real_lazy.LazyBinop.__richcmp__ (sage/rings/real_lazy.c:7864)()
    868         
    869     def __richcmp__(left, right, int op):
--> 870         return (<Element>left)._richcmp(right, op)
    871 
    872     def __hash__(self):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.Element._richcmp (sage/structure/element.c:5167)()
    530 
    531 
--> 532 
    533 
    534 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.Element._richcmp_c_impl (sage/structure/element.c:5398)()
    577 
    578 
--> 579 
    580 
    581 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/real_lazy.so in sage.rings.real_lazy.LazyFieldElement._cmp_c_impl (sage/rings/real_lazy.c:5454)()
    508         except TypeError:
    509             pass
--> 510         left, right = self.approx(), other.approx()
    511         return cmp(left, right)
    512         

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/real_lazy.so in sage.rings.real_lazy.LazyFieldElement.approx (sage/rings/real_lazy.c:5886)()
    567             Complex Interval Field with 53 bits of precision
    568         """
--> 569         return self.eval(self._parent.interval_field())
    570     
    571     def _real_double_(self, R):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/real_lazy.so in sage.rings.real_lazy.LazyBinop.eval (sage/rings/real_lazy.c:7433)()
    825             '68'
    826         """
--> 827         left = self._left.eval(R)
    828         right = self._right.eval(R)
    829         if self._op is add:

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/real_lazy.so in sage.rings.real_lazy.LazyBinop.eval (sage/rings/real_lazy.c:7445)()
    826         """
    827         left = self._left.eval(R)
--> 828         right = self._right.eval(R)
    829         if self._op is add:
    830             return left + right

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/real_lazy.so in sage.rings.real_lazy.LazyAlgebraic.eval (sage/rings/real_lazy.c:10512)()
   1292                 roots = self._poly.roots(ring = AA if isinstance(self._parent, RealLazyField_class) else QQbar)
   1293                 best_root = roots[0][0]
-> 1294                 min_dist = abs(self._root_approx - best_root)
   1295                 for r, e in roots[1:]:
   1296                     dist = abs(self._root_approx - r)

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement.__sub__ (sage/structure/element.c:6075)()
    680 
    681 
--> 682 
    683 
    684 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:5808)()
    695 
    696 
--> 697 
    698 
    699 

TypeError: unsupported operand parent(s) for '-': 'Number Field in a with defining polynomial x^4 + 6*x^2 + 1' and 'Algebraic Field'
sage: NumberField(x^4 + 6*x^2 + 1, 'a').extension(x^4 + 111, embeding=2.5)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/ncalexan/.sage/temp/pv139196.reshsg.uci.edu/23733/_Users_ncalexan__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

TypeError: extension() got an unexpected keyword argument 'embeding'
```



---

Comment by ncalexan created at 2008-12-04 05:09:38

I see now that I typoed in the last stanza.  Try this instead:


```
sage: NumberField(x^4 + 6*x^2 + 1, 'a').extension(x^4 + 111, 'b', embedding=I*2.5).absolute_field().coerce_embedding()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/Users/ncalexan/.sage/temp/pv139196.reshsg.uci.edu/23733/_Users_ncalexan__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in extension(self, poly, name, names, check, embedding)
   2559         if name is None:
   2560             raise TypeError, "the variable name must be specified."
-> 2561         return NumberField_relative(self, poly, str(name), check=check, embedding=embedding)
   2562 
   2563     def factor(self, n):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in __init__(self, base, polynomial, name, latex_name, names, check, embedding)
   4577 
   4578         v[0] = self._gen_relative()
-> 4579         v = [self(x) for x in v]
   4580         self.__gens = tuple(v)
   4581         self._zero_element = self(0)

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3712)()
    282 
    283 
--> 284 
    285 
    286 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:2763)()
     74 
     75 
---> 76 
     77 
     78 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2675)()
     69 
     70 
---> 71 
     72 
     73 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in _element_constructor_(self, x)
   4848             elif P == self:
   4849                 return self._element_class(self, x.polynomial())
-> 4850             return self.__base_inclusion(self.base_field()(x))
   4851 
   4852         if not isinstance(x, (int, long, rational.Rational,

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in __base_inclusion(self, element)
   4920         # Convert to a SAGE polynomial, then to one in gen(), and return it
   4921         R = self.polynomial_ring()
-> 4922         return self(R(expr_x))
   4923 
   4924     def _fractional_ideal_class_(self):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3665)()
    277 
    278 
--> 279 
    280 
    281 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.convert_map_from (sage/structure/parent.c:8640)()
   1000 
   1001 
-> 1002 
   1003 
   1004 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.discover_convert_map_from (sage/structure/parent.c:8833)()
   1013 
   1014 
-> 1015 
   1016 
   1017 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.coerce_map_from (sage/structure/parent.c:7791)()
    838 
    839 
--> 840 
    841 
    842 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.coerce_map_from (sage/structure/parent.c:7522)()
    864 
    865 
--> 866 
    867 
    868 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in __cmp__(self, other)
   1645         else:
   1646             return cmp(self.coerce_embedding()(self.gen()),
-> 1647                        other.coerce_embedding()(other.gen()))
   1648 
   1649     def _ideal_class_(self):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/categories/map.so in sage.categories.map.Map.__call__ (sage/categories/map.c:2729)()
    122 
    123 
--> 124 
    125 
    126 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field_morphisms.so in sage.rings.number_field.number_field_morphisms.NumberFieldEmbedding._call_ (sage/rings/number_field/number_field_morphisms.c:1777)()
     66 
     67 
---> 68 
     69 
     70 

AttributeError: 'NoneType' object has no attribute 'polynomial'
```



---

Attachment

apply on top of the others


---

Comment by mabshoff created at 2008-12-04 07:47:49

Replying to [comment:18 ncalexan]:

Hi Nick,

> This code is good, it really is, but it's just not tested.  I don't have time right now to test it and I will be sans computer over the Christmas break.
> 
> I have to give this a negative review because I do not believe the embeddings work in anything more than the trivial situation: two absolute fields, compatible embeddings into CC.

Ok.
 
> On the other hand, I have no reservations about the coercion part of this patch.  Are we willing to accept almost certainly broken new functionality to have valuable infrastructure upgrades?

I would say the answer is to merge this as is and then open follow up tickets for the problems. Does #4692 address your current concern?

It looks like 3.2.2 will be longer than I have though, so getting this in now should give us the time needed to straighten this out before release.

Thoughts?

Cheers,

Michael


---

Comment by robertwb created at 2008-12-04 07:52:39

I think even the "most trivial" embeddings of absolute fields into CC will be very useful, and a step forward. As this is the first real use of embeddings in the coercion model, I worked on coercion and embeddings at the same time. 

I don't embeddings are "almost certainly broken", but keep trying to break it. Not doing everything one can hope for is acceptable to me, as long as it fails gracefully. And it doesn't break currently working code. 

And thanks again for taking the time to look at this and try it out, it's a huge patch.


---

Comment by cremona created at 2008-12-04 09:35:41

Provided that the doctests pass, that known issues have a ticket, and that the default behaviour (without specifying any embedding) still works as in the past, then we should not hold this back.
There are various things I want to implement for number fields and I would prefer to do so after this patch came in.

Like Nick, I do not have time to test this thoroughly, but someone needs to stick their neck out with a positive review!  As far as I can see Nick has done most one  this, and mabshoff at least has checked the doctests, which should be enough.


---

Comment by mabshoff created at 2008-12-06 18:54:10

For the record:

 * 4276-nf-coerce-all.patch
 * 4276-nf-coerce-fixes.patch
 * 4276-nf-coerce-fixes2.patch

are in Sage 3.2.2.alpha0 on probation since a formal review is still outstanding.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-09 01:31:16

Comment by Nick Alexander, but it ended up in the wrong box, so I am appending it here:

I'm not sure what is supposed to happen, but this probably isn't it.  AFAICT, these embeddings are *not* compatible.  Or they are only after some work, that makes the results at the end strange.

Please explain why this is correct if it is!


```
sage: F1 = NumberField(x^3 + 2, 'a', embedding=2)
sage: F1.coerce_embedding()

Generic morphism:
  From: Number Field in a with defining polynomial x^3 + 2
  To:   Real Lazy Field
  Defn: a -> -1.259921049894873?
sage: F2 = NumberField(x^3 + 2, 'a', embedding=CC.0)
sage: F2.coerce_embedding()

Generic morphism:
  From: Number Field in a with defining polynomial x^3 + 2
  To:   Complex Lazy Field
  Defn: a -> 0.6299605249474365? + 1.091123635971722?*I

sage: F1.gen() + F2.gen()
2*a
sage: (F1.gen() + F2.gen()).parent()
Number Field in a with defining polynomial x^3 + 2
sage: (F1.gen() + F2.gen()).parent().coerce_embedding()

Generic morphism:
  From: Number Field in a with defining polynomial x^3 + 2
  To:   Real Lazy Field
  Defn: a -> -1.259921049894873?
sage: CC(F1.gen())
-1.25992104989487
sage: CC(F1.gen()) + CC(F2.gen())
-0.629960524947436 + 1.09112363597172*I
sage: CC(F1.gen() + F2.gen())
-2.51984209978975
sage: CC(F2.gen() + F1.gen())
1.25992104989487 + 2.18224727194344*I
```



---

Comment by robertwb created at 2008-12-09 19:15:42

Yes, that is a bug. I wasn't considering all the roots in the ambient field, which I now see is necessary.


---

Comment by robertwb created at 2008-12-09 19:29:34

apply on top of fixes2


---

Attachment

OK, the issue found by Nick has been resolved.


---

Comment by mabshoff created at 2008-12-09 19:50:00

For the record: With 4276-nf-coerce-fixes3.patch applied on top of the other patches and my 3.2.2.alpha1 merge tree all doctests pass.

Cheers,

Michael


---

Comment by ncalexan created at 2008-12-10 02:54:42

I just discovered _populate_coercion_lists_(embedding=), and I am now a lot happier.  (Still not thrilled, because it caches aggressively and if you do any arithmetic before changing the embedding it might not take.)

This is what I want to be able to do:  (The composite fields call needs new code of mine, to be posted shortly.)


```
sage: Q1 = NumberField(x^3 + 2, 'a')
sage: Q2 = NumberField(x^3 + 3, 'a')
sage: Q3 = Q1.composite_fields(Q2)[0]
sage: Q3, Q1_into_Q3, Q2_into_Q3, _ = Q1.composite_fields(Q2, both_maps=True)[0]
sage: Q1._populate_coercion_lists_(embedding=Q1_into_Q3)
sage: Q2._populate_coercion_lists_(embedding=Q2_into_Q3)
sage: Q3(Q1.gen())
2/45*a0^7 + 7/45*a0^4 + 311/45*a0
sage: Q3(Q2.gen())
2/45*a0^7 + 7/45*a0^4 + 356/45*a0
sage: Q1.gen() + Q2.gen()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/ncalexan/Documents/School/cmvar/cm_field.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:5721)()
    647 
    648 
--> 649 
    650 
    651 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:5808)()
    695 
    696 
--> 697 
    698 
    699 

TypeError: unsupported operand parent(s) for '+': 'Number Field in a with defining polynomial x^3 + 2' and 'Number Field in a with defining polynomial x^3 + 3'
```


I also want to assert an embedding of L into CLF and have the coercion model discover that I can convert Q1 -> L -> CLF and Q2 -> L -> CLF.  Then we'll be getting somewhere.


---

Comment by mabshoff created at 2008-12-10 06:30:53

After a chat in IRC with Nick I have merged 4276-nf-coerce-fixes3.patch in Sage 3.2.2.alpha1

Cheers,

Michael


---

Comment by robertwb created at 2008-12-10 08:46:38

Nick, 

I'd like to see that happen too--but I can live with that type error for now. The caching is so that it doesn't need to apply the coercion logic every time an arithmetic operation is performed. 

CC me on the ticket when you get your composite_fields code up. 

Robert


---

Comment by mabshoff created at 2008-12-10 08:50:46

Replying to [comment:31 robertwb]:

> CC me on the ticket when you get your composite_fields code up. 
> 
> Robert

Hi,

I would greatly prefer that now with fixes3 merged on top of the previous patches we could get this ticket (positively) reviewed and address any followup issues or Nick's improvements on a new ticket. That way the credit situation is much cleaner and this ticket isn't left to hang open.

Cheers,

Michael


---

Comment by robertwb created at 2008-12-10 08:53:07

Yes, I'm thinking a separate ticket too. This is a monstrously huge ticket already.


---

Comment by mabshoff created at 2008-12-14 16:56:33

I am giving this a positive review in Nick's name (sue me :)), so that it can be officially merge.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-14 16:57:52

Merged 

 * 4276-nf-coerce-all.patch
 * 4276-nf-coerce-fixes.patch
 * 4276-nf-coerce-fixes2.patch 
 * 4276-nf-coerce-fixes3.patch

in Sage 3.2.2.rc0. Plese open followup tickets for new issues/improvements on top of these patches.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-14 16:58:12

Resolution: fixed


---

Comment by mabshoff created at 2008-12-14 16:58:12

Merged in Sage 3.2.2.rc0.


---

Comment by mabshoff created at 2008-12-14 16:59:23

Nick: Obviously if anything goes wrong I am the one to blame here :)

Cheers,

Michael


---

Comment by robertwb created at 2008-12-15 18:25:09

Thanks. I think Cremona's comment hits the nail on the head--a lot of people have looked at this code but no one was willing to stick their neck out and give a positive review. 

I feel confident that this code will not degrade behavior or give wrong answers. I am also confident that it doesn't do everything that one would want to do, but I consider the latter additional enhancements, not defects in this ticket.


---

Comment by cremona created at 2008-12-15 18:35:08

That is fine with me.  I am confidently hoping that everything I used to do with number fields will still work, with no noticeable performance cost, and that some new things are possible which used not to be.

Do the docstrings for the new code contain some hint of the new capabilities?  As the number of patches has grown rather it is not so easy to tell...

Onward and upward!


---

Comment by robertwb created at 2008-12-15 18:58:57

Yes, there is documentation and examples.
