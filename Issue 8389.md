# Issue 8389: Sage eats all memory trying to evaluate MatrixSpace(QQ, 2)['x']

Issue created by migration from https://trac.sagemath.org/ticket/8389

Original creator: mmezzarobba

Original creation time: 2010-02-27 17:22:15

Assignee: AlexGhitza

CC:  mjo nthiery

This makes Sage eat all available memory until it gets interrupted:


```
$ ./sage     
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: MatrixSpace(QQ, 2)['x']
^C---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)  
| Sage Version 4.3.3, Release Date: 2010-02-21                       |
| Type notebook() for the GUI, and license() for information.        |
/home/marc/co/sage-4.3.3/<ipython console> in <module>()

/home/marc/co/sage-4.3.3/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__getitem__ (sage/structure/parent.c:7653)()                  

/home/marc/co/sage-4.3.3/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent._list_from_iterator_cached (sage/structure/parent.c:7061)()   

/home/marc/co/sage-4.3.3/local/lib/python2.6/site-packages/sage/matrix/matrix_space.pyc in __iter__(self)                                                                         
    792             while True:                                                          
    793                 for iv in sage.combinat.integer_vector.IntegerVectors(weight, number_of_entries):                                                                         
--> 794                     yield self(entries=[base_elements[i] for i in iv], rows=True)                                                                                         
    795
    796                 weight += 1

/home/marc/co/sage-4.3.3/local/lib/python2.6/site-packages/sage/matrix/matrix_space.pyc in __call__(self, entries, coerce, copy, rows)
    393             return self(entries.matrix(), copy=False)
    394
--> 395         return self.matrix(entries, copy=copy, coerce=coerce, rows=rows)
    396
    397     def change_ring(self, R):

/home/marc/co/sage-4.3.3/local/lib/python2.6/site-packages/sage/matrix/matrix_space.pyc in matrix(self, x, coerce, copy, rows)
   1068             if isinstance(x[0], list):
   1069                 x = sum(x,[])
-> 1070             elif hasattr(x[0], "is_vector"): # TODO: is this the best way to test that?
   1071                 e = []
   1072                 for v in x:

/home/marc/co/sage-4.3.3/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2726)()

/home/marc/co/sage-4.3.3/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Field.category (sage/rings/ring.c:8675)()

/home/marc/co/sage-4.3.3/local/lib/python2.6/site-packages/sage/misc/classcall_metaclass.pyc in __call__(cls, *args, **options)
    114             return cls
    115
--> 116     def __call__(cls, *args, **options):
    117         """
    118         This method implements ``cls(<some arguments>)``.

/home/marc/co/sage-4.3.3/local/lib/python2.6/site-packages/sage/interfaces/get_sigs.pyc in my_sigint(x, n)
      7
      8 def my_sigint(x, n):
----> 9     raise KeyboardInterrupt
     10
     11 def my_sigfpe(x, n):
```


Note that `MatrixSpace(QQ, 2)['x']` is not supposed to _work_, since


```
Definition:     PolynomialRing [...]
Docstring:
       [...]
       INPUT:

       * ``base_ring`` -- a commutative ring
```



---

Comment by davidloeffler created at 2011-01-23 11:12:17

The problem's not in the polynomial ring constructor per se:

```
sage: R = PolynomialRing(MatrixSpace(QQ, 2),'x'); R
Univariate Polynomial Ring in x over Full MatrixSpace of 2 by 2 dense matrices over Rational Field
```

Almost nothing works with R because printing of elements is broken, but at least you can construct it! 

The problem reported above lies in the `R['x']` syntax; for some reason, the "list" method of the matrix ring is getting called, and this (of course) never terminates. If you try this with a matrix space over a *finite* ring, the list call succeeds, and it tries to get the element of index 'x' -- which fails because the string 'x' isn't an integer:

```
sage: MatrixSpace(GF(3), 2)['x']
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/masiao/<ipython console> in <module>()

/storage/masiao/sage-4.6.2.alpha1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__getitem__ (sage/structure/parent.c:8072)()

TypeError: list indices must be integers, not str
```



---

Comment by mjo created at 2012-01-16 02:48:50

Changing status from new to needs_review.


---

Comment by mjo created at 2012-01-16 02:48:50

This is fixed, probably by #10470. I've added a doctest in the parent list() method; hopefully that is the proper place for it.


---

Attachment

Add a doctest to the parent list() method.


---

Comment by kcrisman created at 2012-03-16 02:00:30

I was about to give this positive review, but after reading comment:2 I wonder.   Are we just hiding a bug here?  In which case this ticket could just be changed to either raising a `NotImplementedError` or making it do what it's supposed to, namely creating a polynomial ring over the matrix space in question.


---

Comment by mjo created at 2012-03-16 14:27:30

Replying to [comment:4 kcrisman]:
> I was about to give this positive review, but after reading comment:2 I wonder.   Are we just hiding a bug here?  In which case this ticket could just be changed to either raising a `NotImplementedError` or making it do what it's supposed to, namely creating a polynomial ring over the matrix space in question.

This is "easy" to do for one variable by overriding `MatrixSpace_generic.__getitem__` to check for a string, and then calling `PolynomialRing()`.

But ideally, we would want to offer the same interface that we do when constructing polynomial rings from other rings or fields. Does constructing a polynomial ring over matrix spaces even make sense mathematically? All of the existing code to do this is in `ring.__getitem__`, which sounds right to me, but this is very much not a strong point of mine.


---

Comment by kcrisman created at 2012-03-16 14:36:51

Changing status from needs_review to needs_info.


---

Comment by kcrisman created at 2012-03-16 14:36:51

Changing priority from major to minor.


---

Comment by kcrisman created at 2012-03-16 14:36:51

In any case, I think that this is at least 'needs info' until we decide what to do.  It's not as high priority as it once was since it just raises an error instead of bringing the computer to a crashing halt!


---

Comment by tscrim created at 2013-04-14 14:15:53

There is (a duplicate) #10608 which has a patch that gives `MatrixSpace_generic` a `__getitem__()` method, so I think this should be fixed (i.e. return a polynomial ring). Also I don't think this hides a problem and is mathematically correct since all `n x n` matrices form a ring (although not the nicest of rings). Plus `PolynomialRing(MatrixSpace(QQ, 2), 'x')` works.

However what I'm thinking as a solution is that any parent in the category of `Rings` should have a default `__getitem__` which checks for string/list input and returns a polynomial/power series ring resp. Thoughts?


---

Comment by mmezzarobba created at 2013-12-22 12:43:36

Replying to [comment:7 tscrim]:
> However what I'm thinking as a solution is that any parent in the category of `Rings` should have a default `__getitem__` which checks for string/list input and returns a polynomial/power series ring resp. Thoughts?

In principle, I agree. Unfortunately, matrix spaces currently do not use the category framework by default (one needs to call `M.full_category_initialisation()` first) for efficiency reasons. So the change you are suggesting would not solve the problem with matrix spaces by itself.

And I'm honestly at lost as to how to use the category framework with fundamental, widely used parents.

In our case, it would make sense (despite the issue with matrix rings) to move the definition of `__getitem__` that deals with polynomials rings and the like from `sage.structure.Rings` to `sage.category.rings.Rings.ParentMethods`. But many common rings do not descend from `Rings().parent_class`, so one would need a wrapper in one direction or the other. Since `Rings.ParentMethods` is supposedly the recommended place to add generic stuff for rings in the long run, it would be natural to move the implementation there and provide a compatibility wrapper in `Ring`. Except that `Ring` comes before `Rings.ParentMethods` in the MRO of (most?) rings that use both...

(On the top of that, there is a hack in `Parent.__getitem__` that one needs to be careful not to break...)


---

Comment by mmezzarobba created at 2014-01-31 20:33:28

Changing status from needs_info to needs_review.


---

Comment by mmezzarobba created at 2014-01-31 20:33:28

Ok, after talking with Nicolas I think I understand better what is going on and what should be done. Here is an attempt to streamline the implementation of `__getitem__` for general rings.

I _didn't_ leave a version `__getitem__` in `ring.Ring` after all, because virtually all rings properly initialize their category by now. The doctests pass, but there is at least one ring (namely `InfinityRing`) rings for which `R['x']` will fail while it used to work, and there may be more. Thoughts?
----
New commits:


---

Comment by nthiery created at 2014-02-20 17:32:28

Hi Mark!

I went through the changes, and overall it looks good! Thanks so much for the cleanup!

Some tiny remarks / suggestions:

- Doc of __getitem__
  - TODO -> .. TODO
  - Is Frac nicer than .fraction_field()?
- Doc of _gen_names, line 2: replacing `ZZ['x']` by `ZZ[sqrt(5)]` could make it more meaninful?
- getitem for a matrix space M: could `M[sqrt(5)]` be a meaningful notation to extend the base ring?
  If yes, I'd be in favor of completely deprecating `M[3]` in favor of `M.unrank(3)`, in order to eventually allow for the notation `M[sqrt(5)]` without ambiguity in the corner case `M[1]`.

By the way: shall we use the occasion to also move `PrincipalIdealDomain.__getitem__` in the corresponding category? Or are there some principal ideal domains in Sage that are not yet in the `PrincipalIdealDomains` category?

Speaking of this method: its documentation says "Create a polynomial or power series ring over ``self`` and inject the variables into the global module scope."; the latter statement is wrong, right?

Cheers,
                         Nicolas


---

Comment by mmezzarobba created at 2014-02-21 09:45:20

Thanks for your review!

Replying to [comment:12 nthiery]:
> - Doc of __getitem__
>   - TODO -> .. TODO

No, that was on purpose: the TODO was part of the SEEALSO block. But I added the missing cross-references and removed the TODO line altogether. (I'll push the new commit in a moment.)

>   - Is Frac nicer than .fraction_field()?

No idea, I didn't touch this part `:-)`.
Let's mention both.

> - Doc of _gen_names, line 2: replacing `ZZ['x']` by `ZZ[sqrt(5)]` could make it more meaninful?

Same thing here.

> - getitem for a matrix space M: could `M[sqrt(5)]` be a meaningful notation to extend the base ring?
>   If yes, I'd be in favor of completely deprecating `M[3]` in favor of `M.unrank(3)`, in order to eventually allow for the notation `M[sqrt(5)]` without ambiguity in the corner case `M[1]`.

I believe `M[sqrt(5)]` would make sense, and I wouldn't mind deprecating the notation `parent[integer]` (as a way of enumerating the elements). But I'd rather do that in another ticket.

> By the way: shall we use the occasion to also move `PrincipalIdealDomain.__getitem__` in the corresponding category? Or are there some principal ideal domains in Sage that are not yet in the `PrincipalIdealDomains` category?
> 
> Speaking of this method: its documentation says "Create a polynomial or power series ring over ``self`` and inject the variables into the global module scope."; the latter statement is wrong, right?

What method are you talking about?

Thanks again,

Marc


---

Comment by git created at 2014-02-21 10:26:42

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-02-24 12:51:55

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by nthiery created at 2014-03-03 13:11:01

Replying to [comment:13 mmezzarobba]:
> No, that was on purpose: the TODO was part of the SEEALSO block. But I added the missing cross-references and removed the TODO line altogether. (I'll push the new commit in a moment.)
> >   - Is Frac nicer than .fraction_field()?
> 
> No idea, I didn't touch this part `:-)`.
> Let's mention both.
> 
> > - Doc of _gen_names, line 2: replacing `ZZ['x']` by `ZZ[sqrt(5)]` could make it more meaninful?
> 
> Same thing here.

Ok. I double checked your changes and am happy with them!

> I believe `M[sqrt(5)]` would make sense, and I wouldn't mind deprecating the notation `parent[integer]` (as a way of enumerating the elements). But I'd rather do that in another ticket.

Fair enough :-) Do you mind creating a ticket for this task?

> > By the way: shall we use the occasion to also move `PrincipalIdealDomain.__getitem__` in the corresponding category? Or are there some principal ideal domains in Sage that are not yet in the `PrincipalIdealDomains` category?
> > 
> > Speaking of this method: its documentation says "Create a polynomial or power series ring over ``self`` and inject the variables into the global module scope."; the latter statement is wrong, right?
> 
> What method are you talking about?

Sorry, I confused myself with Ring.__getitem__ from another branch ...

Btw: what do you think we should do with IntegerRing.__getitem__ which
calls explicitly PrincipalIdealDomains.__getitem__? Just leave it as
it is?

Cheers,
                           Nicolas


---

Comment by mmezzarobba created at 2014-03-03 15:14:12

Replying to [comment:16 nthiery]:
> > I believe `M[sqrt(5)]` would make sense, and I wouldn't mind deprecating the notation `parent[integer]` (as a way of enumerating the elements). But I'd rather do that in another ticket.
> 
> Fair enough :-) Do you mind creating a ticket for this task?

Done (#15885).

> Btw: what do you think we should do with IntegerRing.__getitem__ which
> calls explicitly PrincipalIdealDomains.__getitem__? Just leave it as
> it is?

For now yes.

Can you please set the ticket to positive review if you are happy with it?


---

Comment by nthiery created at 2014-03-03 16:37:06

Replying to [comment:17 mmezzarobba]:
> Done (#15885).

Thanks!

> For now yes.

Ok.

> Can you please set the ticket to positive review if you are happy with it?

Done!


---

Comment by nthiery created at 2014-03-03 16:37:24

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2014-03-03 16:38:12

Oh, by the way, should this be a defect fix or an enhancement?


---

Comment by mmezzarobba created at 2014-03-03 18:20:50

Changing type from defect to enhancement.


---

Comment by vbraun created at 2014-03-03 18:55:36

Resolution: fixed
