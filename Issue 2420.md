# Issue 2420: [with patch, needs review] Extending the gap interface to uni- and multivariate polynomial rings over number fields

Issue created by migration from https://trac.sagemath.org/ticket/2420

Original creator: SimonKing

Original creation time: 2008-03-07 09:05:58

Assignee: SimonKing

CC:  wdj mhansen davidloeffler

Keywords: gap interface, polynomial rings, number fields

Up to now, the gap interface did not work on polynomial rings over number fields. This patch extends the interface accordingly, so that now the following works.
Univariate:

```
sage: F=CyclotomicField(8)
sage: R=PolynomialRing(F,'x')
sage: gap(R)
PolynomialRing( <algebraic extension over the Rationals of degree 4>, ["x"] )
sage: p=R('zeta8^2*x+zeta8')
sage: gap(p)^3
((-1*zeta8^2))*x^3+((-3*zeta8))*x^2+(!-3)*x+(zeta8^3)
sage: p^3
(-zeta8^2)*x^3 + (-3*zeta8)*x^2 + (-3)*x + zeta8^3
```


Multivariate:

```
sage: R=PolynomialRing(F,'x,y')
sage: gap(R)
PolynomialRing( <algebraic extension over the Rationals of degree
4>, ["x", "y"] )
sage: p=R('zeta8*x+zeta8^2*y')^2
sage: gap(p)
(zeta8^2)*x^2+(2*zeta8^3)*x*y-y^2
sage: p
zeta8^2*x^2 + 2*zeta8^3*x*y + (-1)*y^2
```


The patches also provide doc tests.

However, there is one problem: On my machine, the doc tests of sage.rings.polynomial.polynomial_element.pyx trigger the bug reported in #2419.
That bug seems to occur only on few machines (up to now, only one other person can reproduce #2419). 

So, there should be discussion how to deal with that issue.


---

Comment by mhansen created at 2008-03-07 11:05:12

The _gap_init_ methods in a/sage/rings/polynomial/multi_polynomial_element.py and a/sage/rings/polynomial/multi_polynomial_ring_generic.pyx need doctests.  Also, the
"proper" way to do

```
sage: F=CyclotomicField(8)
sage: R=PolynomialRing(F,'x')
sage: p=R('zeta8^2*x+zeta8')
```

in Sage is

```
sage: F.<zeta8>=CyclotomicField(8)
sage: R.<x>=PolynomialRing(F)
sage: p=zeta8^2*x+zeta8
```



---

Attachment

new patch, adding more doctests, should apply to sage 2.10.3.rc2


---

Comment by SimonKing created at 2008-03-08 00:45:51

Replying to [comment:1 mhansen]:
> The _gap_init_ methods in a/sage/rings/polynomial/multi_polynomial_element.py and a/sage/rings/polynomial/multi_polynomial_ring_generic.pyx need doctests.  

Thank you, simply i forgot to include them - the new patch contains tests, it uses the "proper" sage syntax you indicated, and also i had to put a bracket in a different place in _gap_init_ for multi_polynomial_element.py

One more example: With the new patch, it is even possible to have polynomial rings over polynomial rings over ... :

```
sage: F.<c> = CyclotomicField(8)
sage: r.<a,b> = PolynomialRing(F)
sage: R.<x,y> = PolynomialRing(r)
sage: p=R.random_element()+c^2*R.random_element()
sage: g=gap(p)
sage: p
((-2*c^2)*a^2 + (-2*c^2)*b^2 + c^2*a + (-c^2)*b - 2*c^2)*x^2 + (2*c^2*a^2 + (-2*c^2 - 2)*a*b + (2*c^2 + 2)*b^2 + c^2*a + (-1)*b + 2*c^2 - 2)*x*y + ((-2*c^2)*a^2 + 2*c^2*a*b + (2*c^2 - 1)*b^2 + (2*c^2 - 2)*a + b + 2)*y^2 + (2*b^2 + a + 1)*x + ((-2*c^2 + 2)*a^2 + (-c^2 - 2)*a*b + (-c^2 + 1)*b^2 + (-c^2 + 2)*a + c^2*b - 2)*y + (-2*c^2)*a^2 + (-2*c^2 - 2)*a*b + c^2*b^2 + a + (-2*c^2)*b + 2*c^2 + 1
sage: g
(((-2*c^2))*a^2+((-2*c^2))*b^2+(c^2)*a+((-1*c^2))*b+((-2*c^2)))*x^2+((2*c^2)*a^2+((-2-2*c^2))*a*b+((2+2*c^2))*b^2+(c^2)*a-b+((-2+2*c^2)))*x*y+(((-2*c^2))*a^2+(2*c^2)*a*b+((-1+2*c^2))*b^2+((-2+2*c^2))*a+b+!2)*y^2+(!2*b^2+a+!1)*x+(((2-2*c^2))*a^2+((-2-1*c^2))*a*b+((1-1*c^2))*b^2+((2-1*c^2))*a+(c^2)*b+(!-2))*y+(((-2*c^2))*a^2+((-2-2*c^2))*a*b+(c^2)*b^2+a+((-2*c^2))*b+((1+2*c^2)))
sage: g^3==gap(p^3)
True
```



---

Comment by SimonKing created at 2008-03-13 10:37:07

I expected that with William's patch from #2419 the doc tests of polynomial_element.pyx would work, but they don't. And the strange thing is that they _do_ work when sage is started from scratch:

Example from _gap_init_():

```
sage: F.<zeta8>=CyclotomicField(8)
sage: R.<x>=F[]
sage: p=zeta8^2*x+zeta8
sage: p._gap_init_()
'(GeneratorsOfField($sage2)[1]*IndeterminatesOfPolynomialRing($sage3)[1]^0)+(GeneratorsOfField($sage2)[1]^2*IndeterminatesOfPolynomialRing($sage3)[1]^1)'
sage: gap(p)^3
((-1*zeta8^2))*x^3+((-3*zeta8))*x^2+(!-3)*x+(zeta8^3)
sage: p^3
(-zeta8^2)*x^3 + (-3*zeta8)*x^2 + (-3)*x + zeta8^3
```


Example from _gap_():

```
sage: R.<y> = ZZ[]
sage: f = y^3 - 17*y + 5
sage: g = gap(f); g
y^3-17*y+5
sage: f._gap_init_()
'(5*IndeterminatesOfPolynomialRing($sage6)[1]^0)+(-17*IndeterminatesOfPolynomialRing($sage6)[1]^1)+(0*IndeterminatesOfPolynomialRing($sage6)[1]^2)+(1*IndeterminatesOfPolynomialRing($sage6)[1]^3)'
sage: R.<z> = ZZ[]
sage: gap(R)
PolynomialRing( Integers, ["z"] )
sage: g
y^3-17*y+5
sage: gap(z^2 + z)
z^2+z
sage: R.<y> = GF(7)[]
sage: f = y^3 - 17*y + 5
sage: g = gap(f); g
y^3+Z(7)^4*y+Z(7)^5
sage: g.Factors()
[ y+Z(7)^0, y+Z(7)^0, y+Z(7)^5 ]
sage: f.factor()
(y + 5) * (y + 1)^2
```


Agh! I got it! If one now does the examples for resultant, it crashes (at least on my machine):

```
sage: R.<x> = QQ[]
sage: f = x^3 + x + 1;  g = x^3 - x - 1
sage: r = f.resultant(g); r
-8
sage: r.parent() is QQ
True
sage: R.<a> = QQ[]
sage: S.<x> = R[]
sage: f = x^2 + a; g = x^3 + a
sage: r = f.resultant(g); r
a^3 + a^2
sage: r.parent() is R
True
sage: R.<a, b> = QQ[]
sage: S.<x> = R[]
sage: f = x^2 + a; g = x^3 + b
sage: r = f.resultant(g); r
---------------------------------------------------------------------------
<type 'exceptions.NameError'>             Traceback (most recent call last)
...
<type 'exceptions.NameError'>: name 'Mod' is not defined
```


But if sage is restarted, the example for resultant works fine!

*Conclusion*:
 * The patch from #2419 doesn't solve the problem. 
 * Probably it is needed to do a synchronization (similar to #2419) for the gap interface as well.


---

Comment by SimonKing created at 2008-03-13 12:20:07

Note that in the above example, eventually R has no dictionary, `hasattr(R,'__dict__')` is False!

Something else seems very strange to me. In my patch i define _gap_init_() as method for a polynomial ring like that:

```
def _gap_init_(self):
    return 'PolynomialRing(%s, ["%s"])'%(sage.interfaces.gap.gap(self.base_ring()).name(), self.variable_name())
```


If i define this function in sage (i.e., not as a method), i get

```
sage: R.<y> = GF(7)[]
sage: gap(_gap_init_(R)).name()
'$sage2'
sage: gap(_gap_init_(R)).name()
'$sage2'
```

so, the gap name is cached. But if _gap_init_ is a method of R, i obtain (re-starting sage)

```
sage: R.<y> = GF(7)[]
sage: gap(R).name()
'$sage2'
sage: gap(R).name()
'$sage3'
sage: gap(R).name()
'$sage3'
```


Hence, it seems that gap(R) doesn't properly caches the things.

Sorry that my post is rather confused, but this is what i am now.


---

Comment by craigcitro created at 2008-06-20 04:45:58

Changing keywords from "gap interface, polynomial rings, number fields" to "gap interface, polynomial rings, number fields, editor_mhansen".


---

Comment by SimonKing created at 2010-07-06 14:32:07

I finally resumed work on this ticket. It now depends on #8909 and #9423. Therefore, I added all people who commented on these tickets as Cc here. I hope you don't mind.

The things that I announced above are still working (main difference: due to #8909, Sage's cyclotomic fields are now represented as cyclotomic fields in GAP).

However, the doctest trouble persist, so, it still is "needs_work". But I was able to narrow the problem down.

Apparently it is a side effect of GAP on Pari. After two days of work, I found that it is triggered by two _different_ doctests in sage/rings/polynomial/polynomial_element.pyx, namely the test for `_gap_()` and for `resultant()`.

It boils down to the following:

```
sage: R.<a, b> = QQ[]
sage: b._pari_()   # this is fine
b
sage: R.<y> = GF(7)[]
sage: f = y^3 - 17*y + 5
sage: g = gap(f)   # this uses the new patch
sage: f.factor()   # this uses pari
(y + 5) * (y + 1)^2
sage: R.<a, b> = QQ[]
sage: b._pari_()   # this is a disaster!
Mod(3, 7)
```


Does any of you have an explanation for this?

Cheers,

Simon


---

Comment by SimonKing created at 2010-07-06 18:56:33

OK, problem solved!

It is a bug in {{IntegerMod_int.log()}}}, which had a side effect in PARI and is fixed at #9438. Apply `trac_2420_GAP_interface_polynomials.patch` after applying the patches from #8909, #9423 and #9438, and `sage -testall` passes!

Here is a summary of the features:

Univariate

```
sage: F.<zeta> = CyclotomicField(8)
sage: R.<x> = F[]
sage: gap(R)
PolynomialRing( CF(8), ["x"] )
sage: p = zeta^2*x+2*zeta
sage: gap(p)^3
(-E(4))*x^3+(-6*E(8))*x^2-12*x+8*E(8)^3
sage: p^3
-zeta^2*x^3 - 6*zeta*x^2 - 12*x + 8*zeta^3
```


Multivariate

```
sage: R.<x,y> = F[]
sage: p = zeta*x+zeta^2*y
sage: gap(p)^2
E(4)*x^2+2*E(8)^3*x*y-y^2
sage: p^2
(zeta^2)*x^2 + (2*zeta^3)*x*y - y^2
```


O dear! A stack of polynomial rings does not work as it should:

```
sage: P.<y> = QQ[]
sage: K.<tau> = NumberField(y^2+y+1)
sage: R.<x,y> = K[]
sage: S.<z> = R[]
sage: p = tau*x+tau^2*z+3*tau^3*x*y*z
sage: p
(3*x*y + (-tau - 1))*z + (tau)*x
sage: gap(p)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/king/SAGE/work/Tickets/9438/<ipython console> in <module>()

/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)
   1032             return cls(self, x, name=name)
   1033         try:
-> 1034             return self._coerce_from_special_method(x)
   1035         except TypeError:
   1036             raise

/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _coerce_from_special_method(self, x)
   1056             s = '_gp_'
   1057         try:
-> 1058             return (x.__getattribute__(s))(self)
   1059         except AttributeError:
   1060             return self(x._interface_init_())

/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial._gap_ (sage/rings/polynomial/polynomial_element.c:27411)()

/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)
   1030
   1031         if isinstance(x, basestring):
-> 1032             return cls(self, x, name=name)
   1033         try:
   1034             return self._coerce_from_special_method(x)

/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)
   1449             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
   1450                 self._session_number = -1
-> 1451                 raise TypeError, x
   1452         self._session_number = parent._session_number
   1453

TypeError: Gap produced error output
Error, no 1st choice method found for `PROD' on 2 arguments

   executing Read("/home/king/.sage//temp/gauss/30709//interface//tmp30709");
```


The string that was supposed to be executed is

```
sage: p._gap_init_()
'CallFuncList(function() local z; z:=Indeterminate($sage12,"z"); return (CallFuncList(function() local x,y; x:=Indeterminate($sage5,"x"); y:=Indeterminate($sage5,"y"); return (GeneratorsOfField($sage5)[1])*x; end,[]))*1+(CallFuncList(function() local x,y; x:=Indeterminate($sage5,"x"); y:=Indeterminate($sage5,"y"); return (3)*x*y+(-GeneratorsOfField($sage5)[1] - 1)*1; end,[]))*z; end,[])'
```


So, it is almost done, but I'd like to fix the last problem too.


---

Attachment

Disregard first patch; apply after the patches from #9205, #9438, #9423, #8909 and #5618


---

Comment by SimonKing created at 2010-07-08 10:46:57

Changing keywords from "gap interface, polynomial rings, number fields, editor_mhansen" to "gap interface, polynomial rings, number fields, interface cache".


---

Comment by SimonKing created at 2010-07-08 10:46:57

Finally it seems to work. `sage -testall` passes for me.

First of all, I assume the result of various other tickets that are related with the GAP interface. To be precise: Before creating my patch, I did

```
hg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9205/trac_9205-discrete_log.patch')
hg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9205/trac_9205-doctest.patch')
hg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9438/trac_9438_IntegerMod_log_vs_PARI.patch')
hg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9423/trac_9423_gap_for_numberfields.patch')
hg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8909/8909_gap2cyclotomic.patch')
hg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8909/trac_8909_catch_exception.patch')
hg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5618/trac_5618_gap_for_cyclotomic_fields.patch')
```


*__Interface cache framework for Parents__*

At [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/92a66b8e67eeae9b), I announced to introduce a general framework for caching interface representations for parents. It works like this:

 * The class `Parent` gets two new methods `_get_interface_cache_` and `_set_interface_cache_` that do exactly what the name suggests.
 * The method `_interface_`, defined on the level of Sage Objects, used to test whether there is an attribute `__interface` for caching. It still does, for backwards compatibility. If this fails, it now tries to call the new cache methods for parents.
 * Originally, the `_interface_` method, applied to an interface `foo` would call a method `_foo_init_` without additional argument. `_foo_init_()` is supposed to return a string, that is then used to call `foo`. I suggest that `_foo_init_` is called with the argument `foo` - see below why I think this is a good idea. Of course, many `_*_init_` methods don't accept an additional argument; we catch the error and thus have backwards compatibility.

*__GAP representation of polynomial rings__*

Polynomial rings can be quite complicated: The base ring might be not as simple as the rational field. You may even have a tower of polynomial rings.

In order to represent a polynomial ring with a complicated base ring in GAP, it seems reasonable to take a recursive approach: First represent the base ring in GAP, than form a polynomial ring over it.

Since `self._gap_init_()` is supposed to return a string, we need a string that determines the GAP representation of `self.base_ring()`. Since (with my patch) the interface is cached for parents, `gap(self.base_ring()).name()` does the job and is quite efficient (i.e., short). Problem: It may be that we have a non-standard instance of the GAP interface. Therefore, I suggest to provide `_gap_init_` with an optional argument `gap`, so that `gap(self.base_ring())` lives in the right GAP instance.

Example:

```
sage: from sage.interfaces.gap import Gap
sage: MyGap = Gap()
sage: MyGap is gap
False
sage: F.<zeta> = CyclotomicField(8)
sage: P.<x,y> = F[]
sage: a = gap(3)
sage: P._gap_init_(gap)
'PolynomialRing($sage2,["x","y"])'
sage: P._gap_init_(MyGap)
'PolynomialRing($sage1,["x","y"])'
sage: gap('$sage1')
3
sage: MyGap('$sage1')
CF(8)
```


*__GAP interface for polynomials__*

While the interface representations for Parents should be cached, I think the representations for elements should (in general) not be cached. So, I don't use a general framework here, I just provide a `_gap_` method that requires one argument, namely the GAP instance to be used.

At [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/a5761e7bf438cc98), I asked whether the variable names of a polynomial ring should be automatically inserted into the GAP interface (currently, they _are_ inserted).

There was no answer. But I believe that automatic insertion of common qualifiers like `x,t` is bad practice.

So, instead of sending the string representation of a polynomial `p` to GAP, I compute `gap(p)` by adding representations of its terms; and for the terms, I access the variables of `gap(p.parent())` by position (rather than by name).

I am not sure if this is the best solution. Anyway, the following now works and is doctested:

```
        Multivariate polynomial over a cyclotomic field::

            sage: F.<zeta> = CyclotomicField(8)
            sage: P.<x,y> = F[]
            sage: p = zeta + zeta^2*x + zeta^3*y + (1+zeta)*x*y
            sage: gap(p)    # indirect doctest
            (1+E(8))*x*y+E(4)*x+E(8)^3*y+E(8)

        Multivariate polynomial over a number field::

            sage: Q.<t> = QQ[]
            sage: K.<tau> = NumberField(t^2+t+1)
            sage: P.<x,y> = K[]
            sage: p = tau + tau^2*x + tau^3*y + (1+tau)*x*y
            sage: p
            (tau + 1)*x*y + (-tau - 1)*x + y + (tau)
            sage: gap(p)     # indirect doctest
            (tau+1)*x*y+(-tau-1)*x+y+tau

        Multivariate polynomial over a polynomial ring
        over a number field::

            sage: S.<z> = K[]
            sage: P.<x,y> = S[]
            sage: p = tau + tau^2*x*z + tau^3*y*z^2 + (1+tau)*x*y*z
            sage: p
            ((tau + 1)*z)*x*y + ((-tau - 1)*z)*x + z^2*y + tau
            sage: gap(p)     # indirect doctest
            ((tau+1)*z)*x*y+((-tau-1)*z)*x+z^2*y+tau
```


Sorry I made this ticket depend on five other tickets, but I think it is worth it, because most of the above examples didn't work _at all_.


---

Comment by SimonKing created at 2010-07-08 10:46:57

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2010-07-08 11:24:31

I forgot to mention:


```
Tower of polynomial rings over a number field

    sage: Q.<t> = QQ[]
    sage: K.<tau> = NumberField(t^2+t+1)
    sage: P.<x,y> = K[]
    sage: R.<z> = P[]
    sage: p = tau + tau^2*x*z + tau^3*y*z^2 + (1+tau)*x*y*z
    sage: gap(p)
    y*z^2+((tau+1)*x*y+(-tau-1)*x)*z+tau
```

works as well!


---

Comment by SimonKing created at 2011-03-08 12:07:20

Apply trac_2420_GAP_interface_polynomials.patch

(for the patchbot)

Probably this stone age patch will not apply, but it may be worth to let the patchbot try.


---

Comment by SimonKing created at 2011-07-22 13:06:04

Replaces the previous patches


---

Attachment

I have rebased the patch, so that it should work on top of sage-4.7.rc2. I haven't run tests, though.

For the patchbot:

Apply trac2420_gap_interface_polynomials.patch


---

Comment by SimonKing created at 2011-07-22 13:26:02

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-07-22 13:26:02

No, some of the examples above don't work.

No idea why that happens, and no idea whether I will have the time to fix it, in the near future.


---

Comment by vdelecroix created at 2016-07-13 20:26:17

Some of the patch is now implemented in #18266 (in a compatible way with libgap).


---

Comment by embray created at 2019-01-15 18:26:00

I wonder if there's still anything worth salvaging from this ticket.  Some of the examples this was intended to make work now _do_ work.  However, some still do not:


```
sage: R.<x,y> = ZZ[]
sage: gap(x+y)
x+y
sage: S.<z> = K[]
sage: P.<x,y> = S[]
sage: p = tau + tau^2*x*z + tau^3*y*z^2 + (1+tau)*x*y*z
sage: p
((tau + 1)*z)*x*y + ((-tau - 1)*z)*x + z^2*y + tau
sage: gap(p)
...
```


results in a long traceback ending with


```
TypeError: Gap produced error output
Error, no method found! For debugging hints type ?Recovery from NoMethodFound
Error, no 1st choice method found for `*' on 2 arguments

   executing \$sage20:=\$sage23 * \$sage21;;
```


and no better if I try libgap:


```
sage: libgap(p)
...

ValueError: libGAP: Syntax warning: Unbound global variable in stream:1
PolynomialRing(PolynomialRing(CallFuncList(function() local t,E; t:=Indeterminate(\$sage11,"t"); E:=AlgebraicExtension(\$sage11,t^2 + t + 1,"tau"); return E; end,[]), ["z"]),["x","y"]);
                                                                                          ^
Syntax warning: Unbound global variable in stream:1
PolynomialRing(PolynomialRing(CallFuncList(function() local t,E; t:=Indeterminate(\$sage11,"t"); E:=AlgebraicExtension(\$sage11,t^2 + t + 1,"tau"); return E; end,[]), ["z"]),["x","y"]);
                                                                                                                               ^
Error, Variable: '$sage11' must have an assigned value
```



---

Comment by embray created at 2019-01-15 18:27:11

Perhaps we don't have to make every imaginable case work in one fell swoop, so long as improvements can be made in specific cases, such as in #27005


---

Comment by vdelecroix created at 2019-01-16 07:30:56

Replying to [comment:22 embray]:
> Perhaps we don't have to make every imaginable case work in one fell swoop, so long as improvements can be made in specific cases, such as in #27005

Or #21020 (that has some overlaps with this ticket).


---

Comment by vdelecroix created at 2019-02-27 18:25:49

One problem is the number field conversion. This is fine

```
sage: libgap(ZZ['x,y'])
Integers[x,y]
```

This is aslo fine

```
sage: K = CyclotomicField(8)
sage: z = K.gen()
sage: x,y = K['x,y'].gens()
sage: libgap((1+z)*x*y^2 + z^2*x)
(1+E(8))*x*y^2+E(4)*x
```

But fails for more fancy number fields as the conversion is not available

```
sage: K = QQ[sqrt(2)]
sage: libgap(K)
...
GAPError: Syntax warning: Unbound global variable in stream:1
CallFuncList(function() local x,E; x:=Indeterminate(\$sage1,"x"); E:=AlgebraicExtension(\$sage1,x^2 - 2,"sqrt2"); return E; end,[]);
```

