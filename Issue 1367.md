# Issue 1367: weird bug creating fractional ideal in relative number field

Issue created by migration from https://trac.sagemath.org/ticket/1367

Original creator: was

Original creation time: 2007-12-02 07:52:55

Assignee: was

I noticed this bug when thinking about implementing factorization of integers
in a general relative number field (via the absolute field corresponding
to it).  If this bug were fixed, then general factorization would be
trivial to implement, as suggested by the example below. 


```
sage: K.<a,b> = NumberField([x^2 + 1, x^2 + 2])
sage: A = K.absolute_field('z')
sage: I = A.factor_integer(3)[0][0]
sage: from_A, to_A = A.structure()
sage: G = [from_A(z) for z in I.gens()]; G
[3, (-2*b - 1)*a + b - 1]
sage: K.fractional_ideal(G)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/was/s/devel/sage-main/sage/rings/number_field/<ipython console> in <module>()

/Users/was/s/local/lib/python2.5/site-packages/IPython/Prompts.py in __call__(self, arg)
    521 
    522             # and now call a possibly user-defined print mechanism
--> 523             manipulated_val = self.display(arg)
    524             
    525             # user display hooks can change the variable to be stored in

/Users/was/s/local/lib/python2.5/site-packages/IPython/Prompts.py in _display(self, arg)
    545         """
    546 
--> 547         return self.shell.hooks.result_display(arg)
    548 
    549     # Assign the default display method:

/Users/was/s/local/lib/python2.5/site-packages/IPython/hooks.py in __call__(self, *args, **kw)
    132             #print "prio",prio,"cmd",cmd #dbg
    133             try:
--> 134                 ret = cmd(*args, **kw)
    135                 return ret
    136             except ipapi.TryNext, exc:

/Users/was/s/local/lib/python2.5/site-packages/IPython/hooks.py in result_display(self, arg)
    160     
    161     if self.rc.pprint:
--> 162         out = pformat(arg)
    163         if '\n' in out:
    164             # So that multi-line strings line up with the left column of

/Users/was/s/local/lib/python2.5/pprint.py in pformat(self, object)
    109     def pformat(self, object):
    110         sio = _StringIO()
--> 111         self._format(object, sio, 0, 0, {}, 0)
    112         return sio.getvalue()
    113 

/Users/was/s/local/lib/python2.5/pprint.py in _format(self, object, stream, indent, allowance, context, level)
    127             self._readable = False
    128             return
--> 129         rep = self._repr(object, context, level - 1)
    130         typ = _type(object)
    131         sepLines = _len(rep) > (self._width - 1 - indent - allowance)

/Users/was/s/local/lib/python2.5/pprint.py in _repr(self, object, context, level)
    193     def _repr(self, object, context, level):
    194         repr, readable, recursive = self.format(object, context.copy(),
--> 195                                                 self._depth, level)
    196         if not readable:
    197             self._readable = False

/Users/was/s/local/lib/python2.5/pprint.py in format(self, object, context, maxlevels, level)
    205         and whether the object represents a recursive construct.
    206         """
--> 207         return _safe_repr(object, context, maxlevels, level)
    208 
    209 

/Users/was/s/local/lib/python2.5/pprint.py in _safe_repr(object, context, maxlevels, level)
    290         return format % _commajoin(components), readable, recursive
    291 
--> 292     rep = repr(object)
    293     return rep, (rep and not rep.startswith('<')), False
    294 

/Users/was/s/local/lib/python2.5/site-packages/sage/rings/number_field/number_field_ideal.py in __repr__(self)
    215 
    216     def __repr__(self):
--> 217         return "Fractional ideal %s"%self._repr_short()
    218 
    219     def _repr_short(self):

/Users/was/s/local/lib/python2.5/site-packages/sage/rings/number_field/number_field_ideal.py in _repr_short(self)
    232         # makes things insanely slow in general.
    233         # When I fix this, I *have* to also change the _latex_ method.
--> 234         return '(%s)'%(', '.join([str(x) for x in self.gens_reduced()]))
    235 
    236     def __div__(self, other):

/Users/was/s/local/lib/python2.5/site-packages/sage/rings/number_field/number_field_ideal_rel.py in gens_reduced(self)
     84             S = L['x']
     85             gens = L.pari_rnf().rnfidealtwoelt(self.pari_rhnf())
---> 86             gens = [ L(R(x.lift().lift())) for x in gens ]
     87             ## Make sure that gens[1] is in L, not K
     88             Lcoeff = [ L(x) for x in list(gens[1].polynomial()) ]

/Users/was/s/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py in __call__(self, x)
   3321             return self.base_field()(x)
   3322         
-> 3323         return self._element_class(self, x)
   3324 
   3325     def _coerce_impl(self, x):

/Users/was/s/devel/sage-main/sage/rings/number_field/number_field_element.pyx in sage.rings.number_field.number_field_element.NumberFieldElement.__init__()
    231         num = f * den
    232         for i from 0 <= i <= num.degree():
--> 233             (<Integer>ZZ(num[i]))._to_ZZ(&coeff)
    234             ZZX_SetCoeff( self.__numerator, i, coeff )
    235 

/Users/was/s/devel/sage-main/sage/rings/number_field/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class.__call__()

<type 'exceptions.TypeError'>: Unable to coerce -b - 2 to an integer

```



---

Comment by cremona created at 2008-02-18 12:08:58

This might well be fixed by the patches posted for #1946.  Unfortunately I do not seem to be able to test that, owing to my complete incompetence in applying patches, even my own.  It would be a good idea if #1946 was cross-referenced to this one.

 In case this seems crazy:  fixing #1946 by adding lots of doctests to the code for Tate's algorithm over number fields revealed some minor bugs in its implementation, and fixing those revealed some bugs in the code for ideals and fractional ideals in number fields.  I fixed that (in late January, partly jointly with William) and at the same time -- I seem to remember -- fixed this thing about ideals in relative extensions.

 Both the patches  attached to #1946 are waiting review....


---

Comment by AlexGhitza created at 2008-04-25 01:00:54

This is still broken in sage-3.0.


---

Comment by fwclarke created at 2008-07-18 17:57:05

The problem is triggered at line 89 of `number_field_ideal_rel.py` (in 3.0.5):

```
            gens = [ L(R(x.lift().lift())) for x in gens ]
```

In the case above , `L` is the field `K` and (when `x` is `gens[1]`) `R(x.lift().lift())` is the polynomial `(-b + 1)*x - b - 2` over the base field of `K`.   But the real difficulty is that `NumberFieldElement.__init__` doesn't work properly for relative fields; it ought to coerce a polynomial over the base field into the field, but doesn't.

Rather than trying to resolve the general problem with this coercion, it's easy to rewrite the above line 89, as in 
the attached patch.  Then the following works:

```
sage: K.<a, b> = NumberField([x^2 + 1, x^2 + 2])
sage: A = K.absolute_field('z')
sage: from_A, to_A = A.structure()
sage: abs_ideals = [f[0] for f in A.factor(3)]
sage: rel_ideals = [K.ideal([from_A(y) for y in I.gens()]) for I in abs_ideals]
sage: rel_ideals
[Fractional ideal (3, a - 1), Fractional ideal (3, (-1)*a - 1)]
sage: prod(rel_ideals)
Fractional ideal (3)
sage: [J.is_principal() for J in rel_ideals]
[True, True]
```



---

Attachment


---

Comment by mabshoff created at 2008-07-18 18:19:31

Hi Francis, 

I changed the title slightly so our various sql queries pick it up.

Cheers,

Michael


---

Comment by dmharvey created at 2008-07-18 18:54:35

Hi,

Two things. First, the patch needs at least one doctest.

Second, something very fishy is going on. After applying this patch, I try out the example at the top of the definition of `NumberFieldFractionalIdeal_rel`, under the WARNING:


```
sage: K.<a> = NumberField([x^2 + 1, x^2 + 2]); K
Number Field in a0 with defining polynomial x^2 + 1 over its base field
sage: i = K.ideal([a+1])
sage: i
Fractional ideal (1)
```


If `a+1` generates the unit ideal, it had better be a unit. But a+1 is really 1+i (the Gaussian integer), which is not a unit. Alternatively

```
sage: (a+1).norm()
4
```

which is not +1 or -1.


---

Comment by fwclarke created at 2008-07-18 23:30:49

Continuing the calculation, we have

```
sage: i.gens()
(a + 1,)
sage: i.gens_reduced()
(1,)
```

and `i.__repr__()` via `i._repr_short(self)` uses `i.gens_reduced()`

The problem is with lines 90–92 of `number_field_ideal_rel.py`

```
            ## Make sure that gens[1] is in L, not K
            Lcoeff = [ L(x) for x in list(gens[1].polynomial()) ]
            gens[1] = S.hom([L.gen()])(S(Lcoeff))
```

which seem totally wrong-headed.  In the case in question `gens` is `[2, (-b)*a]` (which is ok).  Then `(-b)*a` gets 
converted to `1/2*x^2 + 3/2`, which is the polynomial representing it in the _absolute_ field, after which `x` is (in a most
convoluted way) replaced by `a`, giving (of course) `1` (which is not ok).

There must be a much simpler way to achieve the object of ensuring that the generator is an element of the relative field.


---

Comment by dmharvey created at 2008-07-19 04:57:43

Oh look, the patch is probably fine, but I go completely nuts every time I delve into any of the algebraic number theory stuff in Sage. I mean, why on earth is `NumberFieldFractionalIdeal` a subclass of `Ideal_generic`?? That's completely nuts. ***A fractional ideal is not an ideal.*** That's about as sensible as making `Rational` a subclass of `Integer`. Trying to patch this one line at a time is like trying to stop global warming with a toothpick.

I suggest that you (1) report the above as a separate ticket, (2) add a doctest to your patch to at least illustrate the corrected behaviour, (3) "correct" the doctest under the WARNING so at least it doesn't fail when doctests are run, (4) do a full run of doctests to see what else "breaks", (5) replace "Willia Stein" by "William Stein" in the authors at the top of the file, and (6) find someone else game enough to review this patch.


---

Comment by cremona created at 2008-07-19 08:55:49

I spent several evening 6 months ago on this chunk of code, trying to see how it was supposed to work and fixing what didn't.  It was not a very happy experience -- not helped by the fact that this was just about the first ever Sage development which I did.  On the other hand, I was helped a lot at the time by William.  Th eonly reason I got into that code at all was that I decided to add doctests to `ell_number_field.py` and found lots of things broken. 

Anyway, while I cannot guarantee to have time to review this properly soon, I'll do what I can.


---

Comment by fwclarke created at 2008-07-19 09:21:26

The more I look at `number_field_ideal_rel.py`, the more I notice needs doing.  For example, in

```
    def absolute_ideal(self):
        """
        If this is an ideal in the extension L/K, return the ideal with
        the same generators in the absolute field L/Q.
        """
        try:
            return self.__absolute_ideal
        except AttributeError:
            rnf = self.number_field().pari_rnf()
            L = self.number_field().absolute_field('a')
            R = L['x']
            nf = L.pari_nf()
            genlist = [L(R(x.polynomial())) for x in list(self.gens())]
            self.__absolute_ideal = L.ideal(genlist)
            return self.__absolute_ideal
```

(1) The generator of the absolute field is always called 'a'; it would be much better if the user could choose the name, and, even better, was also able to get the absolute ideal via something like `A = K.absolute_field('z'); A(J)`. (2) Neither `rnf` nor `nf` get used. (3) Since `x.polynomial()` is a rational polynomial, `L(R(x.polynomial()))` is the same as `L(x.polynomial())`. (4) In this context, `list(self.gens())`is no different from `self.gens()`.

I've come to the conclusion that a more serious rewrite (with some more testing doctests) is needed, for which I'm unlikely to have much time in the next few weeks.  My one-line patch was really only meant to point out where the defect lay.


---

Comment by dmharvey created at 2008-07-19 13:38:32

I have made a new ticket #3680 to cover my general gripes about the algebraic number theory framework. But I don't have time to work on it now.


---

Comment by ncalexan created at 2009-01-24 09:39:56

This relies on #5066.  Apply that first.

This DOES NOT address every issue with relative number fields, but it does help in the creation and coercion.  Significantly.

Plenty of doctests, but tons of work left to be done.  The important part is that one can now create relative number field elements from relative polynomials self.base_ring()['x'] or from stacked polynomials QQ['base']['ext'].  Fixes all sorts of things.

Don't forget to close #4869 and #4727 after this is merged.


---

Attachment


---

Comment by ncalexan created at 2009-01-24 10:03:43

Do not apply `sage-1367.patch`.

There may be doctests missing on some functions, but I can't fix this, document a ton of stuff, and doctest every untested function in one go.  This is very much a work in progress patch.


---

Comment by roed created at 2009-01-24 17:31:37

There are a few things I want to discuss (probably at lunch).

The first is that I'm not completely convinced that the following example is the behavior we want:

sage: K.<a> = NumberField(ZZ['x'].0^5 + 2, 'a') 
sage: L.<b> = K.extension(ZZ['x'].0^2 + 3*a, 'b') 
sage: u = QQ['u'].gen() 
sage: t = u.parent()['t'].gen()

sage: L(u*5)
5*b

I guess if we're going to convert at all this makes the most sense, but I want to think about it a bit more.  I'm even less convinced of the following:

sage: W.<w> = t.parent()[]
sage: L(w*5)
5*b
sage: L(W(t))
5*a
sage: L(W(u))
TypeError

The second issue is a naming one.  The function coerce_non_number_field_element_in should probably be a convert function rather than a coerce one.

Overall, though, it looks quite good.


---

Comment by ncalexan created at 2009-01-24 20:06:42

The patch explains why the first behaviour is correct.  Do you want

```
sage: x = ZZ['x'].0
sage: K.<a> = QuadraticField(5)
sage: L.<b> = K.extension(x^2 - a)
sage: L(x + 2) in L
True
```

or

```
sage: L(x + 2) in K
True
```


I think the first is *much* more desirable.

Your second issue is a good point.  I should make sure you're either giving QQ['x'] (or something isomorphic) or QQ['base']['ext'] or base['ext'].  But that's hard at this time.

As for naming: make it a new ticket.  It's not worth shuffing a rename in with a reorganization in my opinion.


---

Comment by mabshoff created at 2009-01-29 04:10:53

Nick, David: any chance to see some movement on this? I would like to get this in before it rots and potential issues can be addressed via followup tickets.

Thoughts?

Cheers,

Michael


---

Comment by ncalexan created at 2009-01-29 05:00:17

I think this should be applied and more tickets opened for any additional issues.

 * It's an improvement upon the old code and addresses 3 tickets.

 * It was never going to be the final say in this area.

 * I don't have time to work on it more, and neither does David Roe.


---

Comment by mabshoff created at 2009-01-29 05:03:07

Replying to [comment:17 ncalexan]:
> I think this should be applied and more tickets opened for any additional issues.
> 
>  * It's an improvement upon the old code and addresses 3 tickets.
> 
>  * It was never going to be the final say in this area.
> 
>  * I don't have time to work on it more, and neither does David Roe.

Thanks Nick. Please open followup tickets and chance it to a positive review. I will then merge this ticket and its dependencies.

Cheers,

Michael


---

Comment by ncalexan created at 2009-01-29 05:09:51

Opened #5126 and #5127.


---

Comment by mabshoff created at 2009-01-29 05:34:09

Ok, to make this patch apply I need to do two things:

 * change cannonical in this patch to canonical
 * apply the following patch

```
diff -r ec9f29930e81 sage/rings/number_field/number_field_ideal_rel.py
--- a/sage/rings/number_field/number_field_ideal_rel.py Sun Jan 25 08:47:06 2009 +0100
+++ b/sage/rings/number_field/number_field_ideal_rel.py Wed Jan 28 21:27:03 2009 -0800
@@ -69,8 +69,11 @@
         try:
             return self.__absolute_ideal
         except AttributeError:
+            rnf = self.number_field().pari_rnf()
             L = self.number_field().absolute_field('a')
-            genlist = [L(x.polynomial()) for x in list(self.gens())]
+            R = L['x']
+            nf = L.pari_nf()
+            genlist = [L(R(x.polynomial())) for x in list(self.gens())]
             self.__absolute_ideal = L.ideal(genlist)
             return self.__absolute_ideal
```

due to 

```
changeset:   11444:4196cd54c996
user:        Robert Bradshaw <robertwb@math.washington.edu>
date:        Fri Jan 23 03:38:03 2009 -0800
summary:     Convert univariate polynomials to new coercion model.
```

This changes

```
genlist = [L(R(x.polynomial())) for x in list(self.gens())]
```

to 

```
genlist = [L(R(x.polynomial())) for x in self.gens()]
```

but doctests do pass. 

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-29 05:41:09

This is Nick's patch with cannonical -> canonical fixed


---

Attachment

This patch is required due to #5069 to make Nick's patch apply


---

Attachment

Merged trac_1367-prebase.patch and trac_1367.2.patch in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-29 05:42:49

Resolution: fixed


---

Comment by mabshoff created at 2009-01-29 05:43:57

The issues David remarked about are now being handled via #5126 and #5127.

Cheers,

Michael
