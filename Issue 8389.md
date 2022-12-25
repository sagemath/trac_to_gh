# Issue 8389: Sage eats all memory trying to evaluate MatrixSpace(QQ, 2)['x']

archive/issues_008389.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @orlitzky @nthiery\n\nThis makes Sage eat all available memory until it gets interrupted:\n\n\n```\n$ ./sage     \n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: MatrixSpace(QQ, 2)['x']\n^C---------------------------------------------------------------------------\nKeyboardInterrupt                         Traceback (most recent call last)  \n| Sage Version 4.3.3, Release Date: 2010-02-21                       |\n| Type notebook() for the GUI, and license() for information.        |\n/home/marc/co/sage-4.3.3/<ipython console> in <module>()\n\n/home/marc/co/sage-4.3.3/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__getitem__ (sage/structure/parent.c:7653)()                  \n\n/home/marc/co/sage-4.3.3/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent._list_from_iterator_cached (sage/structure/parent.c:7061)()   \n\n/home/marc/co/sage-4.3.3/local/lib/python2.6/site-packages/sage/matrix/matrix_space.pyc in __iter__(self)                                                                         \n    792             while True:                                                          \n    793                 for iv in sage.combinat.integer_vector.IntegerVectors(weight, number_of_entries):                                                                         \n--> 794                     yield self(entries=[base_elements[i] for i in iv], rows=True)                                                                                         \n    795\n    796                 weight += 1\n\n/home/marc/co/sage-4.3.3/local/lib/python2.6/site-packages/sage/matrix/matrix_space.pyc in __call__(self, entries, coerce, copy, rows)\n    393             return self(entries.matrix(), copy=False)\n    394\n--> 395         return self.matrix(entries, copy=copy, coerce=coerce, rows=rows)\n    396\n    397     def change_ring(self, R):\n\n/home/marc/co/sage-4.3.3/local/lib/python2.6/site-packages/sage/matrix/matrix_space.pyc in matrix(self, x, coerce, copy, rows)\n   1068             if isinstance(x[0], list):\n   1069                 x = sum(x,[])\n-> 1070             elif hasattr(x[0], \"is_vector\"): # TODO: is this the best way to test that?\n   1071                 e = []\n   1072                 for v in x:\n\n/home/marc/co/sage-4.3.3/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2726)()\n\n/home/marc/co/sage-4.3.3/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Field.category (sage/rings/ring.c:8675)()\n\n/home/marc/co/sage-4.3.3/local/lib/python2.6/site-packages/sage/misc/classcall_metaclass.pyc in __call__(cls, *args, **options)\n    114             return cls\n    115\n--> 116     def __call__(cls, *args, **options):\n    117         \"\"\"\n    118         This method implements ``cls(<some arguments>)``.\n\n/home/marc/co/sage-4.3.3/local/lib/python2.6/site-packages/sage/interfaces/get_sigs.pyc in my_sigint(x, n)\n      7\n      8 def my_sigint(x, n):\n----> 9     raise KeyboardInterrupt\n     10\n     11 def my_sigfpe(x, n):\n```\n\n\nNote that `MatrixSpace(QQ, 2)['x']` is not supposed to *work*, since\n\n\n```\nDefinition:     PolynomialRing [...]\nDocstring:\n       [...]\n       INPUT:\n\n       * ``base_ring`` -- a commutative ring\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8389\n\n",
    "created_at": "2010-02-27T17:22:15Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.2",
    "title": "Sage eats all memory trying to evaluate MatrixSpace(QQ, 2)['x']",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8389",
    "user": "https://github.com/mezzarobba"
}
```
Assignee: @aghitza

CC:  @orlitzky @nthiery

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


Note that `MatrixSpace(QQ, 2)['x']` is not supposed to *work*, since


```
Definition:     PolynomialRing [...]
Docstring:
       [...]
       INPUT:

       * ``base_ring`` -- a commutative ring
```


Issue created by migration from https://trac.sagemath.org/ticket/8389





---

archive/issue_comments_074981.json:
```json
{
    "body": "The problem's not in the polynomial ring constructor per se:\n\n```\nsage: R = PolynomialRing(MatrixSpace(QQ, 2),'x'); R\nUnivariate Polynomial Ring in x over Full MatrixSpace of 2 by 2 dense matrices over Rational Field\n```\n\nAlmost nothing works with R because printing of elements is broken, but at least you can construct it! \n\nThe problem reported above lies in the `R['x']` syntax; for some reason, the \"list\" method of the matrix ring is getting called, and this (of course) never terminates. If you try this with a matrix space over a *finite* ring, the list call succeeds, and it tries to get the element of index 'x' -- which fails because the string 'x' isn't an integer:\n\n```\nsage: MatrixSpace(GF(3), 2)['x']\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/masiao/<ipython console> in <module>()\n\n/storage/masiao/sage-4.6.2.alpha1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__getitem__ (sage/structure/parent.c:8072)()\n\nTypeError: list indices must be integers, not str\n```\n",
    "created_at": "2011-01-23T11:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-74981",
    "user": "https://github.com/loefflerd"
}
```

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

archive/issue_comments_074982.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-16T02:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-74982",
    "user": "https://github.com/orlitzky"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074983.json:
```json
{
    "body": "This is fixed, probably by #10470. I've added a doctest in the parent list() method; hopefully that is the proper place for it.",
    "created_at": "2012-01-16T02:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-74983",
    "user": "https://github.com/orlitzky"
}
```

This is fixed, probably by #10470. I've added a doctest in the parent list() method; hopefully that is the proper place for it.



---

archive/issue_comments_074984.json:
```json
{
    "body": "Attachment [sage-trac_8389.patch](tarball://root/attachments/some-uuid/ticket8389/sage-trac_8389.patch) by @orlitzky created at 2012-01-16 02:49:16\n\nAdd a doctest to the parent list() method.",
    "created_at": "2012-01-16T02:49:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-74984",
    "user": "https://github.com/orlitzky"
}
```

Attachment [sage-trac_8389.patch](tarball://root/attachments/some-uuid/ticket8389/sage-trac_8389.patch) by @orlitzky created at 2012-01-16 02:49:16

Add a doctest to the parent list() method.



---

archive/issue_comments_074985.json:
```json
{
    "body": "I was about to give this positive review, but after reading comment:2 I wonder.   Are we just hiding a bug here?  In which case this ticket could just be changed to either raising a `NotImplementedError` or making it do what it's supposed to, namely creating a polynomial ring over the matrix space in question.",
    "created_at": "2012-03-16T02:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-74985",
    "user": "https://github.com/kcrisman"
}
```

I was about to give this positive review, but after reading comment:2 I wonder.   Are we just hiding a bug here?  In which case this ticket could just be changed to either raising a `NotImplementedError` or making it do what it's supposed to, namely creating a polynomial ring over the matrix space in question.



---

archive/issue_comments_074986.json:
```json
{
    "body": "Replying to [comment:4 kcrisman]:\n> I was about to give this positive review, but after reading comment:2 I wonder.   Are we just hiding a bug here?  In which case this ticket could just be changed to either raising a `NotImplementedError` or making it do what it's supposed to, namely creating a polynomial ring over the matrix space in question.\n\nThis is \"easy\" to do for one variable by overriding `MatrixSpace_generic.__getitem__` to check for a string, and then calling `PolynomialRing()`.\n\nBut ideally, we would want to offer the same interface that we do when constructing polynomial rings from other rings or fields. Does constructing a polynomial ring over matrix spaces even make sense mathematically? All of the existing code to do this is in `ring.__getitem__`, which sounds right to me, but this is very much not a strong point of mine.",
    "created_at": "2012-03-16T14:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-74986",
    "user": "https://github.com/orlitzky"
}
```

Replying to [comment:4 kcrisman]:
> I was about to give this positive review, but after reading comment:2 I wonder.   Are we just hiding a bug here?  In which case this ticket could just be changed to either raising a `NotImplementedError` or making it do what it's supposed to, namely creating a polynomial ring over the matrix space in question.

This is "easy" to do for one variable by overriding `MatrixSpace_generic.__getitem__` to check for a string, and then calling `PolynomialRing()`.

But ideally, we would want to offer the same interface that we do when constructing polynomial rings from other rings or fields. Does constructing a polynomial ring over matrix spaces even make sense mathematically? All of the existing code to do this is in `ring.__getitem__`, which sounds right to me, but this is very much not a strong point of mine.



---

archive/issue_comments_074987.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2012-03-16T14:36:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-74987",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_074988.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2012-03-16T14:36:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-74988",
    "user": "https://github.com/kcrisman"
}
```

Changing priority from major to minor.



---

archive/issue_comments_074989.json:
```json
{
    "body": "In any case, I think that this is at least 'needs info' until we decide what to do.  It's not as high priority as it once was since it just raises an error instead of bringing the computer to a crashing halt!",
    "created_at": "2012-03-16T14:36:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-74989",
    "user": "https://github.com/kcrisman"
}
```

In any case, I think that this is at least 'needs info' until we decide what to do.  It's not as high priority as it once was since it just raises an error instead of bringing the computer to a crashing halt!



---

archive/issue_comments_074990.json:
```json
{
    "body": "There is (a duplicate) #10608 which has a patch that gives `MatrixSpace_generic` a `__getitem__()` method, so I think this should be fixed (i.e. return a polynomial ring). Also I don't think this hides a problem and is mathematically correct since all `n x n` matrices form a ring (although not the nicest of rings). Plus `PolynomialRing(MatrixSpace(QQ, 2), 'x')` works.\n\nHowever what I'm thinking as a solution is that any parent in the category of `Rings` should have a default `__getitem__` which checks for string/list input and returns a polynomial/power series ring resp. Thoughts?",
    "created_at": "2013-04-14T14:15:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-74990",
    "user": "https://github.com/tscrim"
}
```

There is (a duplicate) #10608 which has a patch that gives `MatrixSpace_generic` a `__getitem__()` method, so I think this should be fixed (i.e. return a polynomial ring). Also I don't think this hides a problem and is mathematically correct since all `n x n` matrices form a ring (although not the nicest of rings). Plus `PolynomialRing(MatrixSpace(QQ, 2), 'x')` works.

However what I'm thinking as a solution is that any parent in the category of `Rings` should have a default `__getitem__` which checks for string/list input and returns a polynomial/power series ring resp. Thoughts?



---

archive/issue_comments_074991.json:
```json
{
    "body": "Replying to [comment:7 tscrim]:\n> However what I'm thinking as a solution is that any parent in the category of `Rings` should have a default `__getitem__` which checks for string/list input and returns a polynomial/power series ring resp. Thoughts?\n\nIn principle, I agree. Unfortunately, matrix spaces currently do not use the category framework by default (one needs to call `M.full_category_initialisation()` first) for efficiency reasons. So the change you are suggesting would not solve the problem with matrix spaces by itself.\n\nAnd I'm honestly at lost as to how to use the category framework with fundamental, widely used parents.\n\nIn our case, it would make sense (despite the issue with matrix rings) to move the definition of `__getitem__` that deals with polynomials rings and the like from `sage.structure.Rings` to `sage.category.rings.Rings.ParentMethods`. But many common rings do not descend from `Rings().parent_class`, so one would need a wrapper in one direction or the other. Since `Rings.ParentMethods` is supposedly the recommended place to add generic stuff for rings in the long run, it would be natural to move the implementation there and provide a compatibility wrapper in `Ring`. Except that `Ring` comes before `Rings.ParentMethods` in the MRO of (most?) rings that use both...\n\n(On the top of that, there is a hack in `Parent.__getitem__` that one needs to be careful not to break...)",
    "created_at": "2013-12-22T12:43:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-74991",
    "user": "https://github.com/mezzarobba"
}
```

Replying to [comment:7 tscrim]:
> However what I'm thinking as a solution is that any parent in the category of `Rings` should have a default `__getitem__` which checks for string/list input and returns a polynomial/power series ring resp. Thoughts?

In principle, I agree. Unfortunately, matrix spaces currently do not use the category framework by default (one needs to call `M.full_category_initialisation()` first) for efficiency reasons. So the change you are suggesting would not solve the problem with matrix spaces by itself.

And I'm honestly at lost as to how to use the category framework with fundamental, widely used parents.

In our case, it would make sense (despite the issue with matrix rings) to move the definition of `__getitem__` that deals with polynomials rings and the like from `sage.structure.Rings` to `sage.category.rings.Rings.ParentMethods`. But many common rings do not descend from `Rings().parent_class`, so one would need a wrapper in one direction or the other. Since `Rings.ParentMethods` is supposedly the recommended place to add generic stuff for rings in the long run, it would be natural to move the implementation there and provide a compatibility wrapper in `Ring`. Except that `Ring` comes before `Rings.ParentMethods` in the MRO of (most?) rings that use both...

(On the top of that, there is a hack in `Parent.__getitem__` that one needs to be careful not to break...)



---

archive/issue_comments_074992.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2014-01-31T20:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-74992",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_074993.json:
```json
{
    "body": "Ok, after talking with Nicolas I think I understand better what is going on and what should be done. Here is an attempt to streamline the implementation of `__getitem__` for general rings.\n\nI *didn't* leave a version `__getitem__` in `ring.Ring` after all, because virtually all rings properly initialize their category by now. The doctests pass, but there is at least one ring (namely `InfinityRing`) rings for which `R['x']` will fail while it used to work, and there may be more. Thoughts?\n----\nNew commits:",
    "created_at": "2014-01-31T20:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-74993",
    "user": "https://github.com/mezzarobba"
}
```

Ok, after talking with Nicolas I think I understand better what is going on and what should be done. Here is an attempt to streamline the implementation of `__getitem__` for general rings.

I *didn't* leave a version `__getitem__` in `ring.Ring` after all, because virtually all rings properly initialize their category by now. The doctests pass, but there is at least one ring (namely `InfinityRing`) rings for which `R['x']` will fail while it used to work, and there may be more. Thoughts?
----
New commits:



---

archive/issue_comments_074994.json:
```json
{
    "body": "Hi Mark!\n\nI went through the changes, and overall it looks good! Thanks so much for the cleanup!\n\nSome tiny remarks / suggestions:\n\n- Doc of __getitem__\n  - TODO -> .. TODO\n  - Is Frac nicer than .fraction_field()?\n- Doc of _gen_names, line 2: replacing `ZZ['x']` by `ZZ[sqrt(5)]` could make it more meaninful?\n- getitem for a matrix space M: could `M[sqrt(5)]` be a meaningful notation to extend the base ring?\n  If yes, I'd be in favor of completely deprecating `M[3]` in favor of `M.unrank(3)`, in order to eventually allow for the notation `M[sqrt(5)]` without ambiguity in the corner case `M[1]`.\n\nBy the way: shall we use the occasion to also move `PrincipalIdealDomain.__getitem__` in the corresponding category? Or are there some principal ideal domains in Sage that are not yet in the `PrincipalIdealDomains` category?\n\nSpeaking of this method: its documentation says \"Create a polynomial or power series ring over ``self`` and inject the variables into the global module scope.\"; the latter statement is wrong, right?\n\nCheers,\n                         Nicolas",
    "created_at": "2014-02-20T17:32:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-74994",
    "user": "https://github.com/nthiery"
}
```

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

archive/issue_comments_074995.json:
```json
{
    "body": "Thanks for your review!\n\nReplying to [comment:12 nthiery]:\n> - Doc of __getitem__\n>   - TODO -> .. TODO\n\nNo, that was on purpose: the TODO was part of the SEEALSO block. But I added the missing cross-references and removed the TODO line altogether. (I'll push the new commit in a moment.)\n\n>   - Is Frac nicer than .fraction_field()?\n\nNo idea, I didn't touch this part `:-)`.\nLet's mention both.\n\n> - Doc of _gen_names, line 2: replacing `ZZ['x']` by `ZZ[sqrt(5)]` could make it more meaninful?\n\nSame thing here.\n\n> - getitem for a matrix space M: could `M[sqrt(5)]` be a meaningful notation to extend the base ring?\n>   If yes, I'd be in favor of completely deprecating `M[3]` in favor of `M.unrank(3)`, in order to eventually allow for the notation `M[sqrt(5)]` without ambiguity in the corner case `M[1]`.\n\nI believe `M[sqrt(5)]` would make sense, and I wouldn't mind deprecating the notation `parent[integer]` (as a way of enumerating the elements). But I'd rather do that in another ticket.\n\n> By the way: shall we use the occasion to also move `PrincipalIdealDomain.__getitem__` in the corresponding category? Or are there some principal ideal domains in Sage that are not yet in the `PrincipalIdealDomains` category?\n> \n> Speaking of this method: its documentation says \"Create a polynomial or power series ring over ``self`` and inject the variables into the global module scope.\"; the latter statement is wrong, right?\n\nWhat method are you talking about?\n\nThanks again,\n\nMarc",
    "created_at": "2014-02-21T09:45:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-74995",
    "user": "https://github.com/mezzarobba"
}
```

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

archive/issue_comments_074996.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-02-21T10:26:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-74996",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_074997.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-02-24T12:51:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-74997",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_074998.json:
```json
{
    "body": "Replying to [comment:13 mmezzarobba]:\n> No, that was on purpose: the TODO was part of the SEEALSO block. But I added the missing cross-references and removed the TODO line altogether. (I'll push the new commit in a moment.)\n> >   - Is Frac nicer than .fraction_field()?\n> \n> No idea, I didn't touch this part `:-)`.\n> Let's mention both.\n> \n> > - Doc of _gen_names, line 2: replacing `ZZ['x']` by `ZZ[sqrt(5)]` could make it more meaninful?\n> \n> Same thing here.\n\nOk. I double checked your changes and am happy with them!\n\n> I believe `M[sqrt(5)]` would make sense, and I wouldn't mind deprecating the notation `parent[integer]` (as a way of enumerating the elements). But I'd rather do that in another ticket.\n\nFair enough :-) Do you mind creating a ticket for this task?\n\n> > By the way: shall we use the occasion to also move `PrincipalIdealDomain.__getitem__` in the corresponding category? Or are there some principal ideal domains in Sage that are not yet in the `PrincipalIdealDomains` category?\n> > \n> > Speaking of this method: its documentation says \"Create a polynomial or power series ring over ``self`` and inject the variables into the global module scope.\"; the latter statement is wrong, right?\n> \n> What method are you talking about?\n\nSorry, I confused myself with Ring.__getitem__ from another branch ...\n\nBtw: what do you think we should do with IntegerRing.__getitem__ which\ncalls explicitly PrincipalIdealDomains.__getitem__? Just leave it as\nit is?\n\nCheers,\n                           Nicolas",
    "created_at": "2014-03-03T13:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-74998",
    "user": "https://github.com/nthiery"
}
```

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

archive/issue_comments_074999.json:
```json
{
    "body": "Replying to [comment:16 nthiery]:\n> > I believe `M[sqrt(5)]` would make sense, and I wouldn't mind deprecating the notation `parent[integer]` (as a way of enumerating the elements). But I'd rather do that in another ticket.\n> \n> Fair enough :-) Do you mind creating a ticket for this task?\n\nDone (#15885).\n\n> Btw: what do you think we should do with IntegerRing.__getitem__ which\n> calls explicitly PrincipalIdealDomains.__getitem__? Just leave it as\n> it is?\n\nFor now yes.\n\nCan you please set the ticket to positive review if you are happy with it?",
    "created_at": "2014-03-03T15:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-74999",
    "user": "https://github.com/mezzarobba"
}
```

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

archive/issue_comments_075000.json:
```json
{
    "body": "Replying to [comment:17 mmezzarobba]:\n> Done (#15885).\n\nThanks!\n\n> For now yes.\n\nOk.\n\n> Can you please set the ticket to positive review if you are happy with it?\n\nDone!",
    "created_at": "2014-03-03T16:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-75000",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:17 mmezzarobba]:
> Done (#15885).

Thanks!

> For now yes.

Ok.

> Can you please set the ticket to positive review if you are happy with it?

Done!



---

archive/issue_comments_075001.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-03-03T16:37:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-75001",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075002.json:
```json
{
    "body": "Oh, by the way, should this be a defect fix or an enhancement?",
    "created_at": "2014-03-03T16:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-75002",
    "user": "https://github.com/nthiery"
}
```

Oh, by the way, should this be a defect fix or an enhancement?



---

archive/issue_comments_075003.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2014-03-03T18:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-75003",
    "user": "https://github.com/mezzarobba"
}
```

Changing type from defect to enhancement.



---

archive/issue_events_008574.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-03-03T18:55:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8389#event-8574"
}
```



---

archive/issue_comments_075004.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-03-03T18:55:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8389#issuecomment-75004",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
