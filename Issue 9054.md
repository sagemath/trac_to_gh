# Issue 9054: create a class for basic function_field arithmetic for Sage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-05-26 11:21:12

Assignee: AlexGhitza

CC:  burcin khwilson mderickx mstreng novoselt pbruin minz saraedum

One of the first things we learned at Sage Days 21: Function Fields, is that it is not even possible to really define or even do arithmetic in function fields *at all* in Sage!  It's amazing that this most basic arithmetic still isn't supported, but it isn't (maybe it used to be via generic machinery, but got broken...?).  The point of this ticket is to create classes for standard function field structures, along with support for arithmetic.   This should be organized in a way similar to number fields. 

For this code, the main point is to establish an API that works solidly.  It will be insanely slow.  A subsequent patch will make things fast.


---

Attachment


---

Attachment


---

Attachment


---

Comment by salmanhb created at 2010-05-27 05:38:49

There seems to be an issue with returning the base ring of a RationalFunctionField. Neither base() nor base_ring() return the correct ring:



```
sage: K.<t> = FunctionField(QQ); K
Rational function field in t over Rational Field
sage: R1 = K.base(); R1
Rational function field in t over Rational Field
sage: R2 = K.base_ring(); R2
Rational function field in t over Rational Field
sage: R3.<s> = QQ[]; K3 = Frac(R3); K3
Fraction Field of Univariate Polynomial Ring in s over Rational Field
sage: R3
Univariate Polynomial Ring in s over Rational Field
sage: K3.base() == R3
True
```



---

Attachment


---

Comment by robertwb created at 2010-05-27 10:13:10

Looks like you forgot to add the file `function_field_order`, so I wasn't able to doctest on top of your latest patch (let alone debug it). See also #9051 for added speed in the positive characteristic case.


---

Attachment

polynomial factorization!


---

Comment by jen created at 2010-05-28 01:21:20

FunctionField constructor clips names


```
sage: F = FunctionField(GF(7), 'bit')
sage: F.gen()
b
```



---

Comment by was created at 2010-05-28 06:29:45

ideals and orders!


---

Attachment

inverses of fractional ideals


---

Attachment

Replying to [comment:2 salmanhb]:
> There seems to be an issue with returning the base ring of a RationalFunctionField. Neither base() nor base_ring() return the correct ring:
> 
> 
> {{{
> sage: K.<t> = FunctionField(QQ); K
> Rational function field in t over Rational Field
> sage: R1 = K.base(); R1
> Rational function field in t over Rational Field
> sage: R2 = K.base_ring(); R2
> Rational function field in t over Rational Field
> sage: R3.<s> = QQ[]; K3 = Frac(R3); K3
> Fraction Field of Univariate Polynomial Ring in s over Rational Field
> sage: R3
> Univariate Polynomial Ring in s over Rational Field
> sage: K3.base() == R3
> True
> }}}

The above is correct.  To get what you want, use the constant_field() method. 

```
sage: K.<t> = FunctionField(QQ);
sage: K.constant_field()
Rational Field
```



---

Comment by was created at 2010-05-28 10:55:53

morphisms of function fields


---

Attachment


---

Attachment

Various methods needed for #9095 (doctesets depend on #9094)


---

Comment by khwilson created at 2010-06-04 22:17:13

Should be some automatic way to do the following:


```
K.<T> = FunctionField(GF(17))
P = T-5
f = P^5
R = K._ring
R(f.element()).valuation(R(p.element()))
```



---

Attachment

flattened patch that incorporates all of patches 1-12 above into a single patch.


---

Comment by was created at 2010-07-06 09:37:38

Here is a link to the result of doctesting sage-4.4.4 + patches 1-12:

   http://sage.math.washington.edu/home/wstein/patches/9054-part1-12.doctest.txt

The failed tests:


```
The following tests failed:

        sage -t  devel/sage-main/sage/matrix/matrix2.pyx # 1 doctests failed
        sage -t  devel/sage-main/sage/plot/matrix_plot.py # 0 doctests failed
        sage -t  devel/sage-main/sage/modular/abvar/morphism.py # 1 doctests failed
        sage -t  devel/sage-main/sage/modular/abvar/finite_subgroup.py # 1 doctests failed
        sage -t  devel/sage-main/sage/tests/startup.py # 1 doctests failed
        sage -t  devel/sage-main/sage/modular/modform/hecke_operator_on_qexp.py # 1 doctests failed
        sage -t  devel/sage-main/sage/categories/function_fields.py # 5 doctests failed
        sage -t  devel/sage-main/sage/rings/function_field/function_field_element.pyx # 14 doctests failed
```



---

Comment by was created at 2010-07-06 09:37:38

Changing assignee from AlexGhitza to was.


---

Comment by was created at 2010-07-07 13:01:55

NOTE: #9094 implements sqrt for polynomials, which is relevant to trac_9054-doctest.patch


---

Comment by mderickx created at 2010-07-07 21:17:51

I guess the doctest patch isn't really usefull addition to sage (although making it was a usefull learning experience for Peter Bruin and me since it was our first patch). The patch fixes some bugs which are also fixed in other patches in trac. Some are indeed fixed by #9094 (although i think this can be done faster and more elegant) and another one related calculating the valuation in fraction fields is fixed by 9051-FpT_4.patch in #9051.

Since I'm quite new to developing and using trac and hg etc. I would like to know what is the best thing to do now. And especially how to deal with the relating patches wich also contain fixes for stuff happening here.


---

Comment by mderickx created at 2010-07-17 11:02:34

Added an attachment that fixes all but three doctest failures. The remaining failures are:


```

sage -t  "devel/sage-mderickx/sage/modular/abvar/morphism.py" # 1 failure

sage -t  "devel/sage-mderickx/sage/modular/abvar/finite_subgroup.py" # 1 failure

sage -t  "devel/sage-main/sage/modular/modform/hecke_operator_on_qexp.py" # 1 failure

}}}They are all related since their error messages all end in:`      File "/Applications/sage/local/lib/python/site-packages/sage/modules/free_module.py", line 4700, in _echelonized_basis        d = self._denominator(basis)      File "/Applications/sage/local/lib/python/site-packages/sage/modules/free_module.py", line 4810, in _denominator        d = d.lcm(x.denominator())    AttributeError: 'int' object has no attribute 'lcm'`It would be nice if someone who has a better understanding of sage to fix this final bug, since then we would have no doctests failing anymore for this patch.


---

Comment by mderickx created at 2010-07-17 11:05:00

Oeps, wrong fromatting. Now a bit more readable:


```
sage -t  "devel/sage-mderickx/sage/modular/abvar/morphism.py" # 1 failure

sage -t  "devel/sage-mderickx/sage/modular/abvar/finite_subgroup.py" # 1 failure

sage -t  "devel/sage-main/sage/modular/modform/hecke_operator_on_qexp.py" # 1 failure

```


They are all related since their error messages all end in:

```

      File "/Applications/sage/local/lib/python/site-packages/sage/modules/free_module.py", line 4700, in _echelonized_basis
        d = self._denominator(basis)
      File "/Applications/sage/local/lib/python/site-packages/sage/modules/free_module.py", line 4810, in _denominator
        d = d.lcm(x.denominator())
    AttributeError: 'int' object has no attribute 'lcm'
```



---

Comment by mderickx created at 2010-07-30 18:36:51

Has there been any work on this since sage days > 23? Even if the work is only partially finnished it would be good to know to avoid double work.


---

Attachment

Aplies to sage 4.4.4 after 1-12 patch and it also needs the #9054 patch trac_9094-sqrt-mderickx.patch


---

Comment by was created at 2010-08-25 05:34:08

Replying to [comment:20 mderickx]:
> Has there been any work on this since sage days > 23? Even if the work is only partially 
> finished it would be good to know to avoid double work.

There has been no further work.   When I do work further on this, I will post a patch.  I always post patches of everything I do as I go, as soon as I'm done with a session of work.


---

Comment by was created at 2010-10-26 15:49:42

I am moving this entirely out of Sage and into the psage library.   See

   http://code.google.com/p/purplesage/issues/detail?id=3


---

Comment by was created at 2010-10-26 22:47:35

Resolution: wontfix


---

Comment by was created at 2010-10-26 22:47:35

I'm closing this since I'm no longer interested in getting it included in the main sage distribution.  It is now in psage as mentioned above.


---

Comment by robertwb created at 2010-10-27 16:05:50

Changing status from closed to new.


---

Comment by robertwb created at 2010-10-27 16:05:50

I think eventually this should be in the main sage distribution, even if no one's actively working on it right now.


---

Comment by robertwb created at 2010-10-27 16:05:50

Resolution changed from wontfix to 


---

Comment by minz created at 2011-03-31 15:14:29

There should be no doctest failures left. Comments, remarks, and reviews are welcome. :)

Apply trac_9054-all-parts.patch

Depends on #9094, #11034


---

Comment by saraedum created at 2011-06-08 19:05:58

The doctests of `function_field.py` contain the following lines:

```
sage: R.<x> = FunctionField(QQ); S.<y> = R[]
sage: R2.<t> = FunctionField(QQ); S2.<w> = R2[]
sage: L2.<w> = R.extension((4*w)^2 - (t+1)^3 - 1)
```

I think it is confusing that it does not make a difference whether you write R.extension or R2.extension in this example. I'm new to sage so maybe I'm misunderstanding something here.


---

Attachment

polynomial used for a field extension must be defined over the base field


---

Comment by saraedum created at 2011-06-28 17:22:53

There are some problems with the zero of a function field:

```
sage: K.<x> = FunctionField(QQ); R.<y> = K[]; L.<y> = K.extension(y^2+x);
sage: coerce(L,L.polynomial())==0
False
sage: y/0
0
```



---

Comment by saraedum created at 2011-06-28 17:23:47

fixes the problems regarding zero.


---

Attachment

Entering the following at the sage prompt produces a `TypeError: Unable to coerce -u^2 (...) to Rational`.

```
K.<x> = FunctionField(QQ); R.<y> = K[]
L.<y> = K.extension(y^2 - x)
M.<u> = FunctionField(QQ); R.<v> = M[]
N.<v> = M.extension(v-u^2)
L.hom([u,v])
```

This is due to the fact that `hom()` determines the codomain by looking only at the first element of `[u,v]`.


---

Attachment

set the correct codomain for function fields


---

Attachment

fixes hash doctests for 32bit and a random doctest


---

Comment by saraedum created at 2011-07-22 17:31:08

Is there a reason why a FunctionFieldMorphism is a Map and not a RingHomomorphism?


---

Attachment

Minimal support for functions field. Does not include all of the above patches.


---

Comment by mderickx created at 2011-08-26 22:27:24

I'm now busy with very troughly checking the entire patch wich at least with some changed free module stuff passes all doctests. There will be a big doctest patch comming up which includes tests I've thought up to also test some more none trivial examples.

There is are at least two big issues which I run in to today. They all occured in the same terminal session.


```
sage: K.<x> = FunctionField(QQ)
sage: R.<y> = K[]
sage: L.<w> = K.extension(y^5 - (x^3 + 2*x*y + 1/x));
sage: w.is_integral()
False
sage: L.order(w)  #should raise a value error since orders can only be generated by integral elements
Order in Function field in w defined by y^5 - 2*x*y + (-x^4 - 1)/x
sage: L.order(w).gens()
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/Users/maarten/Downloads/sage-4.7.2.alpha2/devel/sage-main/<ipython console> in <module>()

/Users/maarten/Downloads/sage-4.7.2.alpha2/local/lib/python2.6/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.ParentWithGens.gens (sage/structure/parent_gens.c:2741)()

/Users/maarten/Downloads/sage-4.7.2.alpha2/local/lib/python2.6/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.ParentWithGens.ngens (sage/structure/parent_gens.c:2548)()

/Users/maarten/Downloads/sage-4.7.2.alpha2/local/lib/python2.6/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.check_old_coerce (sage/structure/parent_gens.c:1228)()

RuntimeError: Order in Function field in w defined by y^5 - 2*x*y + (-x^4 - 1)/x still using old coercion framework
```



---

Comment by mderickx created at 2011-08-28 06:11:58

the review patch is not entirely ready, but julian wanted to have a look so I uploaded it


---

Comment by SimonKing created at 2011-08-28 06:58:28

At [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c62fa3dae0a2ca82), Maarten mentioned that pickling does not seem to work for the code posted here, which seems to be due to some attributes typically involved in coercion.

Looking at [attachment:trac_9054-all-parts.patch], I see that the base class for function fields is derived from `sage.rings.ring.Field`, but `Field.__init__` is not called.

The rings in vanilla Sage do not pay enough attention to coercion and categories. #9944 and (in particular) #9138 aim at improving the situation. In particular, with #9138 it should now possible to avoid any direct call to `ParentWithGens.__init__`; calling `Field.__init__` should just work (tm). Can you try?


---

Comment by SimonKing created at 2011-08-28 07:03:44

PS: After [attachment:trac_9054-all-parts.patch] was created, several other patches were posted. Can you please clearly state (in the ticket description and, for the patchbot, also in a comment) which patches are supposed to be applied? It is difficult to work on the pickling problem (or reviewing) if it is not clear what code exactly we are talking about.


---

Comment by SimonKing created at 2011-08-28 08:02:43

Here are some comments on [attachment:trac_9054-all-parts.patch]:

 * Please remove the `__contains__` method from the category `FunctionFields`. Containment in categories should rely on the default implementation, unless there is a compelling reason to do otherwise.

 Even worse, your containment test is ultimately based on testing class inheritance (namely in the function `is_FunctionField`). That totally undermines the category framework. It must be possible for an object to be a function field even without inheriting from `sage.rings.function_field.function_field.FunctionField`.

 The default implementation of `F in FunctionFields()` relies on the category of F: The containment test returns True if and only if `F.category()` is a sub-category of `FunctionFields()`. That should be much better, from a mathematical point of view, than testing class inheritance!

 * You should add a test of the form `TestSuite(F).run()`, where F is a function field. The test suite is formed by some generic tests defined in the category framework and includes many sanity tests (such as pickling for the field and its elements, associativity, commtativity, ...). If you can think of specific tests for function fields, then you should add methods named `_test_...` as parent or element methods of `sage.categories.function_fields.FunctionFields`. Such methods will be automatically called when running `TestSuite(F).run()`.

 * You should also add a test of the form `loads(dumps(F)) is F`, in order to test uniqueness of parent structures; if I recall correctly, the test suite from the category would only test `loads(dumps(F))==F`.

 * It should not be needed to have a function `is_FunctionField` (that just tests class inheritance) - `F in FunctionFields()` is a better test, IMHO. If you do want to preserve `is_FunctionField` then please do not simply put it in the global name space. At least, it should be deprecated, similar to `is_Ring` being deprecated. There is a function decorator to do so.

 * In the doc test for the `_element_constructor_` method, you explicitly call the method. I think it should better be an indirect test (after all, the documentation is supposed to show how the user is supposed to work with stuff). Hence, not `L._element_constructor_(L.polynomial_ring().gen())` but `L(L.polynomial_ring().gen())   #indirect doctest`.

 * I already mentioned, since `FunctionField` is derived from `sage.rings.ring.Field`, that `Field.__init__(...)` should be called. It could be that this only works when #9138 is used. Just calling `ParentWithGens.__init__` may be insufficient.

 * There are several methods, such as polynomial_ring or vector_space, that use a hand-made cache. Please use the `@`cached_method decorator instead! That has several reasons. 
   1. It is more easy. You don't need to manually update attributes.
   2. With #11115, the `@`cached_method decorator is rewritten in Cython and provides a faster cache than anything you could possibly create with Python.

 * Is there a reason why you have a method `base_field` that simply returns the function field itself? From the behaviour of the  `base_ring` method of polynomial rings, I would rather expect that `FunctionField(QQ,['t']).base_field()` returns the rational field.


---

Comment by SimonKing created at 2011-08-28 16:17:56

Replying to [comment:37 SimonKing]:
> 
>  * I already mentioned, 

... namely on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c62fa3dae0a2ca82),

> that `Field.__init__(...)` should be called. It could be that this only works when #9138 is used. Just calling `ParentWithGens.__init__` may be insufficient.


---

Comment by was created at 2011-08-28 16:35:09

Replying to [comment:37 SimonKing]:
> Here are some comments on [attachment:trac_9054-all-parts.patch]:
> 
>  * Please remove the `__contains__` method from the category `FunctionFields`. Containment in categories should rely on the default implementation, unless there is a compelling reason to do otherwise.
> 
>  Even worse, your containment test is ultimately based on testing class inheritance (namely in the function `is_FunctionField`). That totally undermines the category framework. It must be possible for an object to be a function field even without inheriting from `sage.rings.function_field.function_field.FunctionField`.
> 
>  The default implementation of `F in FunctionFields()` relies on the category of F: The containment test returns True if and only if `F.category()` is a sub-category of `FunctionFields()`. That should be much better, from a mathematical point of view, than testing class inheritance!
> 

Technically this is true.   But this category framework instead of inheritance -- really two very different approaches to design -- leads directly to slow code in some cases in practice, which is *really* annoying, IMHO.   For example, see #11657, where one of the root causes of slowness was code in is_Ring that was added to support this category approach, and which slowed everything down.   Fortunately for me I have psage where I can write streamlined code without having to be weighed down, and for generic Sage working well and being extensible is more important, so of course I agree with you in this case.  

>  * You should add a test of the form `TestSuite(F).run()`, where F is a function field. The test suite is formed by some generic tests defined in the category framework and includes many sanity tests (such as pickling for the field and its elements, associativity, commtativity, ...). If you can think of specific tests for function fields, then you should add methods named `_test_...` as parent or element methods of `sage.categories.function_fields.FunctionFields`. Such methods will be automatically called when running `TestSuite(F).run()`.
> 
>  * You should also add a test of the form `loads(dumps(F)) is F`, in order to test uniqueness of parent structures; if I recall correctly, the test suite from the category would only test `loads(dumps(F))==F`.
> 

This is also testing that pickling works at all.  This code is used by the pickle jar to create pickles for testing later. 

>  * It should not be needed to have a function `is_FunctionField` (that just tests class inheritance) - `F in FunctionFields()` is a better test, IMHO. If you do want to preserve `is_FunctionField` then please do not simply put it in the global name space. At least, it should be deprecated, similar to `is_Ring` being deprecated. There is a function decorator to do so.
> 

is_Ring is only deprecated when used from the top level (i.e., the Sage prompt).   However, there is still a is_Ring function, which can be used in library code, and is not deprecated for this purpose.   And the is_Ring function does test for category stuff. 

>  * In the doc test for the `_element_constructor_` method, you explicitly call the method. I think i
t should better be an indirect test (after all, the documentation is supposed to show how the user is supposed to work with stuff). Hence, not `L._element_constructor_(L.polynomial_ring().gen())` but `L(L.polynomial_ring().gen())   #indirect doctest`.
> 

I disagree.   I view "#indirect test" for situations where you can't think of a clean way of directly calling the function.  If there is such a way, use it!  That way, at least you know for sure it is really being tested.  Suggesting to get rid of that makes no sense to me.  What if `L(L.polynomial_ring().gen())` doesn't call `_element_constructor_` at all?   Also, one can also just have two tests -- one that is indirect and one that isn't.

>  * I already mentioned, since `FunctionField` is derived from `sage.rings.ring.Field`, that `Field.__init__(...)` should be called. It could be that this only works when #9138 is used. Just calling `ParentWithGens.__init__` may be insufficient.
> 
>  * There are several methods, such as polynomial_ring or vector_space, that use a hand-made cache. Please use the `@`cached_method decorator instead! That has several reasons. 
>    1. It is more easy. You don't need to manually update attributes.
>    2. With #11115, the `@`cached_method decorator is rewritten in Cython and provides a faster cache than anything you could possibly create with Python.

+1.  Note that when the very first version of the function field code was written (by me) `@`cached_method was disturbingly slow.  I really, really appreciate the fast Cython rewrite. 

>  * Is there a reason why you have a method `base_field` that simply returns the function field itself? From the behaviour of the  `base_ring` method of polynomial rings, I would rather expect that `FunctionField(QQ,['t']).base_field()` returns the rational field.
> 

No.  The base field of a function field is a rational function field in 1 variable.  The base field of that rational function field is then a field such as QQ.   Most function fields aren't rational, e.g., they are finite extensions K/QQ(t), or even relative extensions L/K.  In the first case, the base field is QQ(t) and in the second it is K.  
If Simon was confused by this, it should be documented better.   



>


---

Comment by SimonKing created at 2011-08-28 17:42:58

Replying to [comment:39 was]:
> Replying to [comment:37 SimonKing]:
> > Here are some comments on [attachment:trac_9054-all-parts.patch]:
> > 
> >  * Please remove the `__contains__` method from the category `FunctionFields`. Containment in categories should rely on the default implementation, unless there is a compelling reason to do otherwise.
> ...
> 
> Technically this is true.   But this category framework instead of inheritance -- really two very different approaches to design -- leads directly to slow code in some cases in practice, which is *really* annoying, IMHO. 

A while ago, I had worked on a ticket #10667 about category containment. One purpose was to get a speedup. The trick was (again) to use Cython. For some reason, the work on that ticket has stalled. Perhaps it would be worth while to resume it.

Generally, I think it is better to improve the category framework, rather than to work around it.

>  For example, see #11657, where one of the root causes of slowness was code in is_Ring that was added to support this category approach, and which slowed everything down.

Then why is the existing `is_Ring` not rewritten along the lines of what you do in #11657?

> is_Ring is only deprecated when used from the top level (i.e., the Sage prompt).

Yes, this is what I meant. I did not mean "deprecated" in the sense of "will soon be removed", but in the sense of "please don't try this at home".

>  And the is_Ring function does test for category stuff. 

Actually I have not been aware that category stuff is tested in `is_Ring`. I was thinking about various other `is_...` methods that really do nothing more than isinstance.
 
> >  * Is there a reason why you have a method `base_field` that simply returns the function field itself? From the behaviour of the  `base_ring` method of polynomial rings, I would rather expect that `FunctionField(QQ,['t']).base_field()` returns the rational field.
> > 
> 
> No.  The base field of a function field is a rational function field in 1 variable. 

Ouch, so I was mistaken.

> The base field of that rational function field is then a field such as QQ.   Most function fields aren't rational, e.g., they are finite extensions K/QQ(t), or even relative extensions L/K.  In the first case, the base field is QQ(t) and in the second it is K.  
> If Simon was confused by this, it should be documented better.   

Not needed. What I stated was based on reading the patch "diagonally". I only noticed one of the two base_field methods.


---

Comment by was created at 2011-08-28 17:56:42

Replying to [comment:40 SimonKing]:
> A while ago, I had worked on a ticket #10667 about category containment. One purpose was to get a speedup. The trick was (again) to use Cython. For some reason, the work on that ticket has stalled. Perhaps it would be worth while to resume it.
> 

+1

> Generally, I think it is better to improve the category framework, rather than to work around it.
> 
> >  For example, see #11657, where one of the root causes of slowness was code in is_Ring that was added to support this category approach, and which slowed everything down.
> 
> Then why is the existing `is_Ring` not rewritten along the lines of what you do in #11657?

What I did there slows down `is_Ring` testing if the object in question does not derive from Ring. 

> > is_Ring is only deprecated when used from the top level (i.e., the Sage prompt).
> 
> Yes, this is what I meant. I did not mean "deprecated" in the sense of "will soon be removed", but in the sense of "please don't try this at home".
> 

If you are developing on the Sage library, I think it is OK to use. 

> >  And the is_Ring function does test for category stuff. 
> 
> Actually I have not been aware that category stuff is tested in `is_Ring`. I was thinking about various other `is_...` methods that really do nothing more than isinstance.
>  

Yes, take a look at the code.  I too was surprised by this!

 -- William


---

Comment by mderickx created at 2011-08-28 19:09:53

I changed the description so that it's clear which code to look at. I will read the rest of all the remarks when I'm back from lunch.


---

Comment by mderickx created at 2011-08-29 02:44:11

Dear Simon,

Thanks for the help and suggestions. But sadly it did not help (altough I find #9138 a very cool ticket it's good to make a lot of rings finally more consistent with the current model of doing things with the category framework).

After some fiddeling around I managed to reduce the error to something in FunctionFieldElement_rational initialization code (hence probably not something with the categorie an coercion framework).


```
sage: K = QQ['x'].fraction_field(); x = K.gen(0)
sage: sage.rings.function_field.function_field_element.FunctionFieldElement_rational(K, x)
x
sage: l=sage.rings.function_field.function_field_element.FunctionFieldElement_rational(K, x)
sage: dumps(l)
PicklingError                             Traceback (most recent call last)
...
PicklingError: Can't pickle <type 'dictproxy'>: attribute lookup __builtin__.dictproxy failed
sage: l.__getstate__()
(Fraction Field of Univariate Polynomial Ring in x over Rational Field, <dictproxy object at 0x10ddf9948>)
```



---

Comment by mderickx created at 2011-08-29 06:51:00

It took me a while to find out how to solve the problems with pickling but I finally managed to do so. It was because of cython objects not being pickleable automatically so you have to write your own pickling methods. A more experienced programmer might have found this out way faster then me, but I had a lot of trouble (basically spent this entire afternoon reading about how pickling protocol works so I could fix it. I will now look into the issues you described and get a definite patch up.


---

Comment by SimonKing created at 2011-08-29 09:57:11

Just for your information: I resumed work on #10667. 

Testing whether QQ is a ring works faster with the methods from #11115 and #10667 than with using the current `is_Ring`:

```
sage: C = CommutativeRings().objects()
sage: QQ in C
True
sage: %timeit QQ in C
625 loops, best of 3: 3.88 µs per loop
```

versus

```
sage: from sage.rings.ring import is_Ring
sage: %timeit is_Ring(QQ)
625 loops, best of 3: 5.06 µs per loop
```


Of course, just testing the class is a lot faster:

```
sage: from sage.rings.ring import Ring
sage: %timeit isinstance(QQ,Ring)
625 loops, best of 3: 666 ns per loop
```



---

Comment by SimonKing created at 2011-08-29 11:09:43

I really think that `is_Ring` should be _globally_ improved. For example, it already helps to define

```
def is_Ring(x):
    """
    Return True if x is a ring.

    EXAMPLES::

        sage: from sage.rings.ring import is_Ring
        sage: is_Ring(ZZ)
        True
    """
    if isinstance(x, Ring):
        return True
    from sage.categories.rings import Rings
    return x in Rings()
```

hence, only do the import when needed.

The timings become

```
sage: from sage.rings.ring import is_Ring
sage: P.<x,y,z> = QQ[]
sage: is_Ring(P)
True
sage: %timeit is_Ring(P)
625 loops, best of 3: 243 ns per loop
sage: MS = MatrixSpace(QQ,2)
sage: is_Ring(MS)
True
sage: %timeit is_Ring(MS)
625 loops, best of 3: 21.5 µs per loop
```

versus

```
sage: from sage.rings.ring import is_Ring
sage: sage: P.<x,y,z> = QQ[]
sage: is_Ring(P)
True
sage: %timeit is_Ring(P)
625 loops, best of 3: 4.93 µs per loop
sage: MS = MatrixSpace(QQ,2)
sage: sage: is_Ring(MS)
True
sage: %timeit is_Ring(MS)
625 loops, best of 3: 26.4 µs per loop
```


But I think I'll move it to #10667.


---

Comment by SimonKing created at 2011-08-30 10:09:19

Time for a little advertisement: I obtain a much improved performance with #10667 (introducing the class of objects and morphisms of a category, written in Cython). Perhaps it is useful for you?

*__Testing commutative rings__*

The function `is_CommutativeRing` does nothing but testing the class. But it is a Python function. Let us compare its speed with the speed of a Cython container, testing category containment.

`is_CommutativeRing`:

```
sage: from sage.rings.commutative_ring import is_CommutativeRing
sage: is_CommutativeRing??
...
Source:
def is_CommutativeRing(R):
    return isinstance(R, CommutativeRing)
sage: is_CommutativeRing(QQ)
True
sage: s = SymmetricGroup(4)
sage: is_CommutativeRing(s)
False
sage: %timeit is_CommutativeRing(QQ)
625 loops, best of 3: 1.09 µs per loop
sage: %timeit is_CommutativeRing(s)
625 loops, best of 3: 3.51 µs per loop
```


Cython container:

```
sage: O = CommutativeRings().objects()
sage: QQ in O
True
sage: s in O
False
sage: %timeit QQ in O
625 loops, best of 3: 1.5 µs per loop
sage: %timeit s in O
625 loops, best of 3: 1.46 µs per loop
```

Hence, when applied to a symmetric group, the container performs a category containment test (with negative result, of course) that is _faster_ than a Python class check!

*__Testing rings__*

As you have observed, the current `is_Ring` function is suboptimal. I rewrote it in #10667.

Without #10667 (but with #11115 for a fast cache):

```
sage: from sage.rings.ring import is_Ring
sage: MS = MatrixSpace(QQ,2)
sage: %timeit is_Ring(QQ)
625 loops, best of 3: 5.1 µs per loop
sage: is_Ring(MS)
True
sage: %timeit is_Ring(MS)
625 loops, best of 3: 17.3 µs per loop
sage: C = Rings()
sage: %timeit QQ in C
625 loops, best of 3: 4.18 µs per loop
sage: %timeit MS in C
625 loops, best of 3: 4.31 µs per loop
```

With #10667 in addition:

```
sage: from sage.rings.ring import is_Ring
sage: MS = MatrixSpace(QQ,2)
sage: %timeit is_Ring(QQ)
625 loops, best of 3: 259 ns per loop
sage: %timeit is_Ring(MS)
625 loops, best of 3: 17.5 µs per loop
sage: C = Rings().objects()
sage: %timeit QQ in C
625 loops, best of 3: 1.49 µs per loop
sage: %timeit MS in C
625 loops, best of 3: 1.57 µs per loop
```



---

Comment by mderickx created at 2011-09-01 00:59:28

Ok I'm done with my reviewing of the original work. I guess a review patch of 39.8 KB deserves a review of its own :P


---

Comment by mderickx created at 2011-09-01 00:59:28

Changing status from new to needs_review.


---

Comment by mderickx created at 2011-09-01 02:53:29

Note that this patch needs the patch at http://trac.sagemath.org/sage_trac/ticket/11751 to work, but altough the patch at that ticket makes all the doctest for function fields pass, it makes a lot of other doctests fail :(


---

Comment by mderickx created at 2011-09-10 21:21:15

Ok #11751 is ready for review and the code here passes all tests (at least I tested it on sage 4.7.2.alpha2 ) after you apply the tickets at 11751. So this one can finally get merged as soon as it has positive review.


---

Attachment


---

Attachment

revert changes to misc.unittest introduced by the review patch


---

Attachment

use category in is_FunctionField()


---

Attachment

replace manual caching with cached_method


---

Attachment

_element_constructor_ checks that element is in maximal order


---

Comment by saraedum created at 2011-09-15 01:13:37

added missing calls to superclass constructors


---

Attachment

use UniqueFactory instead of cached_method in constructors


---

Comment by saraedum created at 2011-09-15 01:21:21

refactored maps class hieararchy


---

Attachment

extended and unified doctests


---

Comment by saraedum created at 2011-09-15 02:07:18

cleanup code and imports


---

Attachment

added authors and copyright headers


---

Attachment


---

Comment by saraedum created at 2011-09-15 02:20:54

Apply trac_9054-all-parts.patch, trac_9054_polynomial_base_field.patch, trac_9054_zero.patch, trac_9054_codomain.patch, trac_9054_doctest-2.patch, trac_9054-review.patch, trac_9054_undo_unittest.patch, trac_9054-invert_ideal.patch, trac_9054_isFunctionField.patch, trac_9054_UniqueFactory.patch, trac_9054_cached_method.patch, trac_9054_maximal_order_member_check.patch, trac_9054_call_super_constructors.patch, trac_9054_maps_refactor.patch, trac_9054_doctests-3.patch, trac_9054_cleanup.patch, trac_9054_authors.patch


---

Comment by saraedum created at 2011-09-15 02:36:56

(Apparently the patchbot expects these "Apply" instructions in a comment and not in the ticket description)

A more detailed description of the patches since `trac_9054-invert_ideal.patch`:
 
 * `trac_9054_isFunctionField.patch` hopefully does what Simon King proposed for `is_FunctionField`
 * `trac_9054_UniqueFactory.patch` replaces the ``@`cached_method` in `constructor.py` with UniqueFactories -- apparently that class is meant for that purpose
 * `trac_9054_cached_method.patch` replaces all manual caching with ``@`cached_method` methods
 * `trac_9054_maximal_order_member_check.patch` fixes a todo about checking that members  passed to an `_element_constructor` are actually in the order
 * `trac_9054_call_super_constructors.patch` is the one I'm not sure about. At two places the super classes were not properly called -- was that by intention? I hope this fixes it.
 * `trac_9054_maps_refactor.patch` slightly changes the base classes of function field morphisms
 * `trac_9054_doctests-3.patch` essentially unifies the naming of variables in the doctests, so function fields are now called K and L, variables x, y, z. Also I added an entry to `/doc/en/reference/index.rst`, is that correct?
 * `trac_9054_cleanup.patch` reorganizes some imports and removes empty lines
 * `trac_9054_authors.patch` adds authors and copyrights to the files. I followed [http://www.sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files](http://www.sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files), hopefully I got it right?

I also reviewed Maarten's changes and they looked good except for the very few things I patched here. Maarten could you review my patches? It looks like a lot of work, but it should be fairly trivial to review.


---

Attachment

identical to trac_9054_isFunctionField.patch but the patch bot does not like upper case in patch files


---

Attachment

identical to trac_9054_UniqueFactory.patch (patchbot does not like uppercase)


---

Comment by saraedum created at 2011-09-19 14:05:06

Apply trac_9054-all-parts.patch, trac_9054_polynomial_base_field.patch, trac_9054_zero.patch, trac_9054_codomain.patch, trac_9054_doctest-2.patch, trac_9054-review.patch, trac_9054_undo_unittest.patch, trac_9054-invert_ideal.patch, trac_9054_is_function_field.patch, trac_9054_unique_factory.patch, trac_9054_cached_method.patch, trac_9054_maximal_order_member_check.patch, trac_9054_call_super_constructors.patch, trac_9054_maps_refactor.patch, trac_9054_doctests-3.patch, trac_9054_cleanup.patch, trac_9054_authors.patch


---

Comment by saraedum created at 2011-09-19 15:25:00

fixes in the reference manual


---

Attachment


---

Comment by saraedum created at 2011-09-20 09:41:20

Changing status from needs_review to needs_work.


---

Comment by saraedum created at 2011-09-20 09:41:20

[attachment:trac_9054_cleanup.patch] introduced a problem with cyclic imports ­— I'm working on it.


---

Comment by saraedum created at 2011-09-20 12:30:39

fixes an import problem in factor()


---

Attachment

It turned out not to be a cyclic import problem but just the wrong module that was imported. I'm waiting for the doctests to set this back to needs_review.


---

Comment by saraedum created at 2011-09-20 13:27:02

orders have no category set


---

Comment by saraedum created at 2011-09-20 13:48:04

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by mderickx created at 2011-11-05 18:01:25

Changing status from needs_review to needs_work.


---

Comment by mderickx created at 2011-11-05 18:01:25

On sage.math using the just released sage-4.7.2 with the following 21! patches applied

```
mderickx`@`sage:/scratch/mderickx/sage/devel/sage$ hg qser | nl
     1	9138_flat.patch
     2	trac_9054-all-parts.patch
     3	trac_9054_polynomial_base_field.patch
     4	trac_9054_zero.patch
     5	trac_9054_codomain.patch
     6	trac_9054_doctest-2.patch
     7	trac_9054-review.patch
     8	trac_9054_undo_unittest.patch
     9	trac_9054-invert_ideal.patch
    10	trac_9054_is_function_field.patch
    11	trac_9054_unique_factory.patch
    12	trac_9054_cached_method.patch
    13	trac_9054_maximal_order_member_check.patch
    14	trac_9054_call_super_constructors.patch
    15	trac_9054_maps_refactor.patch
    16	trac_9054_doctests-3.patch
    17	trac_9054_cleanup.patch
    18	trac_9054_authors.patch
    19	trac_9054_reference.patch
    20	trac_9054_factor.patch
    21	trac_9054_order_category.patch
```


I get 


```

The following tests failed:

	sage -t --long devel/sage-main/sage/rings/function_field/maps.py # 1 doctests failed
	sage -t --long devel/sage-main/sage/rings/function_field/function_field.py # 7 doctests failed
----------------------------------------------------------------------
Total time for all tests: 1102.4 seconds
```



---

Comment by mderickx created at 2011-11-05 18:03:14

Changing status from needs_work to needs_review.


---

Comment by mderickx created at 2011-11-05 18:03:14

Sorry false alarm. I didn't have all patches applied!


---

Comment by mderickx created at 2011-11-07 13:36:35

All patches till review.patch combined


---

Attachment

All julians patches after review.patch combined


---

Attachment

Fixes last minor errors introduced by julians patches


---

Comment by mderickx created at 2011-11-07 13:45:47

It turned out that also when applying all julians patches to sage 4.7.2 with #9138 we get some errors. I fixed this in my minor review2.patch. I also combined some patches so that it becomes easier for someone else to do something with this ticket (i.e. doesnt have to download 20 patches). I'm now reading trough [attachment:trac_9054-julian-combined.patch] if it does logical things.


---

Comment by SimonKing created at 2011-11-07 14:32:54

Just a note on #9138: It had already been merged, but was unmerged because of an unacceptable regression in elliptic curve computations. But at #11900, I was able to avoid the regression and even turn it into a speed-up, in some cases. #11900 needs review, and then I guess #9138 would be merged again.


---

Comment by mderickx created at 2011-11-07 15:58:31

Ok these are the results from reading trough you patches:

Why did you make some_elements in function_field.py return only one element? This number should be at least two (and preferable even at least 3) since else a lot of tests in TestSuite(F).run() will be meaningless with just one element because one element is always equal to itself for example!

If you make vector_space a cached method then why don't you change

```
self._vector_space = (V, from_V, to_V) 
return self._vector_space 
```

to

```
return (V, from_V, to_V) 
```

This code is in two places.

In function_field_order.py there is a typo in the sentence "the function field in which this iss an order."

Why did you remove:

```
if is_Ideal(gens): 
    gens = gens.gens() 
```

in function_field_order.py. I suspect the code was there to make the (not doctested) use case of:

```
sage: K.<x> = FunctionField(QQ) 
sage: O=K.maximal_order()
sage: I=O.ideal(x)
sage: O.ideal(I)
```

since you should be able to make an ideal with input an ideal.

For the rest your combination patch looks very nice. Also good that you made the documentation quality so much higher. If you either answer the above questions with the right arguments or if you change them back it seems that we can finally have function fields in sage!


---

Comment by mderickx created at 2011-11-07 15:58:31

Changing status from needs_review to needs_work.


---

Comment by saraedum created at 2011-11-07 16:18:00

Replying to [comment:67 mderickx]:
> Why did you make some_elements in function_field.py return only one element? This number should be at least two (and preferable even at least 3) since else a lot of tests in TestSuite(F).run() will be meaningless with just one element because one element is always equal to itself for example!

I think I had seen that somewhere else only one element was returned and copied that. (at that time I didn't know what some_elements() was good for)
I'll fix that.

> If you make vector_space a cached method then why don't you change
> {{{
> self._vector_space = (V, from_V, to_V) 
> return self._vector_space 
> }}}
> to
> {{{
> return (V, from_V, to_V) 
> }}}
> This code is in two places.
That's true. Must have missed that.

> In function_field_order.py there is a typo in the sentence "the function field in which this iss an order."
Will be fixed in the next patch.

> Why did you remove:
> {{{
> if is_Ideal(gens): 
>     gens = gens.gens() 
> }}}
> in function_field_order.py. I suspect the code was there to make the (not doctested) use case of:
> {{{
> sage: K.<x> = FunctionField(QQ) 
> sage: O=K.maximal_order()
> sage: I=O.ideal(x)
> sage: O.ideal(I)
> }}}
> since you should be able to make an ideal with input an ideal.
Good question. It's part of a doctest patch so I guess it just got in by accident.

> For the rest your combination patch looks very nice. Also good that you made the documentation quality so much higher. If you either answer the above questions with the right arguments or if you change them back it seems that we can finally have function fields in sage!
Ok. I'll prepare a patch to fix these issues. Thanks you took the time and had a look at these patches. :)


---

Comment by saraedum created at 2011-11-07 19:58:18

patches to mderickx's review comments


---

Attachment

Apply trac_9054-all-parts.patch, trac_9054-julian-combined.patch, trac_9054-review2.patch, trac_9054_review_fixup.patch.

Maarten, I'm not so sure about the is_Ideal() check anymore. Is it really expected behavior that ideal(I) creates the ideal generated by the generators of I — no matter where the ideal I lives? If you feel like that should happen, then add these two lines again and set the ticket to positive review. Or don't add them if you feel that people should be more explicit by actually calling ideal(I.gens()).


---

Comment by saraedum created at 2011-11-07 20:07:51

Changing status from needs_work to needs_review.


---

Comment by mderickx created at 2011-11-07 23:20:31

I will add it just to be consistent with numberfields.

```
sage: K.<a> = QQ.extension(x^2-2)
sage: I = K.ideal(3)
sage: L.<b> = K.extension(x^2-3)
sage: L.ideal(I)
Fractional ideal (3)
sage: L.ideal(p).factor()
(Fractional ideal (b))^2
```


Note that it also mathematically makes sense in the most general setting since the ideal created this way is the ideal extension corresponding to the coersion map from I.ring() to self.


---

Attachment


---

Comment by mderickx created at 2011-11-08 00:34:32

If you can just check my last patch then it can have positive review.


---

Comment by saraedum created at 2011-11-08 16:32:04


```
sage: K.<x> = FunctionField(QQ)
sage: R.<y> = K[]
sage: L.<y> = K.extension(y^3-x)
sage: loads(dumps(L))
AttributeError: ("'module' object has no attribute 'FunctionField_polymod'", <built-in function lookup_global>, ('FunctionField_polymod',))
```


This was also checked by `sage: TestSuite(L).run() #long time` in function_field.py.

The latest patch fixes this problem.

Maarten, if you agree with this latest patch you can set it to positive review.


---

Comment by mderickx created at 2011-11-08 17:08:48

I guess my last ticket name was a bit to hopefull. I just forgot to do add a --long after sage -tp 20 once and immediately a bug slips trough. I'm now testing everything with your last patch.


---

Comment by mderickx created at 2011-11-08 20:14:37

One more question. Shouldn't the line

FunctionField = FunctionFieldFactory("FunctionField")

also be changed in a way similar in you last patch. I mean the two things should work in the same way right?


---

Comment by saraedum created at 2011-11-09 12:46:45

We could change it but it is not necessary. `FunctionField` is exported to sage.all so the pickling infrastructure can find the name there. `FunctionField_polymod`, however, can not be found in sage.all, that's why there is the fully qualified name.


---

Attachment

fix pickling of FunctionField_polymod


---

Comment by mderickx created at 2011-11-11 12:22:56

I'd like to have the consistency so I changed you last patch. If your ok with it this ticket can finally have a positive review.


---

Comment by saraedum created at 2011-11-11 15:01:33

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-11-15 11:36:39

The commit messages of the patches could be cleaned up:
 1. [attachment:trac_9054-julian-combined.patch]: the commit message _starts_ with `* * *` instead of something useful.
 1. [attachment:trac_9054-review.patch] has no proper commit message.  This improper commit message is also in [attachment:trac_9054-all-parts.patch], which should be fixed.
 1. [attachment:trac_9054-all-parts.patch] "`contains parts 1-12, marteen's additions and final doctest fixes`" makes no sense if you don't know this ticket, the message should makes sense on its own.  The word "function field" does not even appear in the message of this patch!


---

Comment by jdemeyer created at 2011-11-15 11:36:39

Changing status from positive_review to needs_work.


---

Comment by saraedum created at 2011-11-15 13:36:28

I'm replacing the commit messages now. I don't have privileges to replace attachements so I have to upload a new set of patches instead.


---

Comment by saraedum created at 2011-11-15 13:36:59

provide basic function field arithmetic (combined patch by various authors)


---

Attachment

cleanup function field code and documentation


---

Attachment

fix doctests for function fields


---

Attachment

fixes for function fields related to the review comments by mderickx


---

Attachment

last fixes for function fields


---

Comment by saraedum created at 2011-11-15 13:39:44

fix pickling for extensions of function fields


---

Attachment

Apply trac_9054-all-parts.2.patch, trac_9054-julian-combined.2.patch, trac_9054-review2.2.patch, trac_9054_review_fixup.2.patch, trac_9054-can_this_really_be_the_last.2.patch, trac_9054_pickling.2.patch


---

Comment by saraedum created at 2011-11-15 13:42:17

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2012-01-22 21:23:44

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-01-22 21:23:44

Patches [attachment:trac_9054-all-parts.2.patch] and [attachment:trac_9054-review2.2.patch] apply with fuzz 2 against sage-5.0.beta1.  Please rebase such that they apply cleanly.


---

Comment by jdemeyer created at 2012-01-30 10:51:06

Changing status from needs_work to positive_review.


---

Comment by mderickx created at 2012-01-30 12:55:11

Thanks for rebasing, I added it to my todo list, but didn't get to it yet.


---

Attachment


---

Comment by jdemeyer created at 2012-02-02 12:52:09

Resolution: fixed
