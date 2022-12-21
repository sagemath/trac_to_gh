# Issue 3738: new coercion model

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-07-29 08:49:17

Assignee: robertwb

This set of patches pulls the core coercion infrastructure from the coercion branch, without actually converting any of the Parents over. All Parents now descent from old_parent.Parent, which has a couple of compatibility routines. 

With this in place Parents can be migrated one at a time. Other coercion branch features should be separate tickets. 


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment

A remark about doctest coverage:

```
On Jul 30, 2008, at 9:49 AM, William Stein wrote:

>> I think this is probably something that it would be good for multiple
>> people could look at. (Both those previously involved in coercion,
>> and those not). It could help spread the work around too.
>>
>
> Michael Abshoff commented to me that the new coercion code you've
> posted introduces new functions that have no doctests.  Any comment?


That is a true accusation, though I feel there is some justification
as many of the functions are not actually being used yet so it is
hard to test them (they were being used in the coercion branch, so
it's not completely untested code, they're just not used until
Parents are converted.) Also, a lot of them are generic helper
functions that are supposed to be overridden. And a third point is
that much of this was written before the 100% doctest rule, and there
is a significant portion that is renaming/re-factoring old code.

That being said, I have strived for better coverage (and
documentation, not just tests). Currently in terms of new (or heavily
modified) code we have:

sage/structure/coerce.pyx
SCORE sage/structure/coerce.pyx: 100% (20 of 20)

sage/structure/coerce_actions.pyx
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE sage/structure/coerce_actions.pyx: 66% (10 of 15)

Missing documentation:
         * __init__(self, G, S)
         * Element _call_(self, g, a)
         * __init__(self, G, S)
         * Element _call_(self, a, g)
         * __cinit__(self)

The first 4 are methods of the RAction and LAction classes that are
not yet used anywhere in the Sage library (but code exists to
instantiate them if _l_action or _r_action is defined on the
elements). I'm not sure if/how __cinit__ should be tested.

sage/structure/coerce_dict.pyx
SCORE sage/structure/coerce_dict.pyx: 100% (14 of 14)

sage/structure/coerce_maps.pyx
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE sage/structure/coerce_maps.pyx: 28% (7 of 25)

Mostly __init__ and _call_ methods, but since no Parents have been
converted over they are never used (and some can't even be used until
we have converted Parents). There still some room for improvement
here, and I will write some more documentation for this file.
Boilerplate __init__ functions are particularly unenlightening to
doctest.

sage/structure/generators.pyx
SCORE sage/structure/generators.pyx: 11% (5 of 45)

[we don't use this yet, other then the fact that there's a cdef'd
slot to put the generators object. If coverage on this file is a
problem, I would go ahead and delete much of this file, and only put
back things as they are needed]


That is where things stand. I will go add more doctests to
coerce_maps.pyx (though I know I can't hit 100% until it's actually
used) but I think it would be good to start reviewing it, and I would
advocate that for this particular project it be grandfathered in to
some extent for practicalities sake. (This is not the case for future
coercion tickets, which should meet the 100% coverage standard.)
```



---

Attachment

Added a bunch of doctests to `parent.pyx` and `coerce_maps.pyx`.


---

Attachment


---

Comment by mabshoff created at 2008-08-13 22:15:25

Merged 

 * coerce.hg
 * 3738-13-docs.patch
 * 3738-fix-1.patch 

in Sage 3.1.alpha2. These patches are on probation, but unless something goes wrong I see them in 3.1.final :)

By the way: "#3744 - Coercion between isomorphic parents should result in an element of the left operand's parent" is in the bundle and hence has also been merged.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-13 22:37:14

With the patch applied I am seeing two doctest failures:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.alpha2$ sage -t -long devel/sage/sage/algebras/steenrod_algebra_element.py
sage -t -long devel/sage/sage/algebras/steenrod_algebra_element.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/tmp/steenrod_algebra_element.py", line 218:
    sage: xm * y
Expected:
    Sq^{5} Sq^{1}
Got:
    Sq(3,1)
**********************************************************************
1 items had failures:
   1 of  90 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.alpha2/tmp/.doctest_steenrod_algebra_element.py
         [3.0 s]
exit code: 1024
```

The above seems to be harmless.

The next one is:

```
sage -t -long devel/sage/sage/sets/set.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/tmp/set.py", line 442:
    sage: Set(ZZ).cardinality()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_20[1]>", line 1, in <module>
        Set(ZZ).cardinality()###line 442:
    sage: Set(ZZ).cardinality()
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/sets/set.py", line 459, in cardinality
        raise NotImplementedError, "computation of cardinality of %s not yet implemented"%self.__object
    NotImplementedError: computation of cardinality of Integer Ring not yet implemented
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/tmp/set.py", line 816:
    sage: X.cardinality()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_42[5]>", line 1, in <module>
        X.cardinality()###line 816:
    sage: X.cardinality()
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/sets/set.py", line 819, in cardinality
        return self.__X.cardinality() + self.__Y.cardinality()
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/sets/set.py", line 459, in cardinality
        raise NotImplementedError, "computation of cardinality of %s not yet implemented"%self.__object
    NotImplementedError: computation of cardinality of Integer Ring not yet implemented
**********************************************************************
2 items had failures:
   1 of   5 in __main__.example_20
   1 of   6 in __main__.example_42
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.alpha2/tmp/.doctest_set.py
         [3.4 s]
```


Cheers,

Michael


---

Comment by robertwb created at 2008-08-14 04:37:42

Thanks Nick and Robert for looking at this. Craig Citro has been reviewing it as well. I'm attaching a patch for the sets doctest failure.


---

Attachment


---

Comment by ncalexan created at 2008-08-14 05:14:53

Spent a few hours of reading with rlm.  We reviewed, quite carefully, patches 0, 1, 2, and 3.

I am confident that:

1) the new code is solid -- not necc. bug free, but fixable

2) the likelihood of this set of patches causing catastrophic failure is very low -- the sticky points (__getattr__ :) appear to be covered.

I support applying this patch and moving forward with the conversion process 'in vivo'.


---

Attachment


---

Comment by rlm created at 2008-08-14 05:17:01

I also support moving forward with these patches applied. It seems much more feasible to continue incrementally like this.


---

Attachment


---

Comment by robertwb created at 2008-08-14 06:15:41

Thank you for your good comments. I've incorporated some of the feedback in 3738-referee-comments.patch

> There are no docs in generators.

True. See my earlier comments.  

> sage/structure/parent.pyx:128 - What is the syntax foo(bar=None, *, etc=None) doing? Does it throw away all but the first non-kwd arg?

http://www.python.org/dev/peps/pep-3102/

> Why not always pass the parent (_unique morphism)?

There are two use cases, the first is speed for some critical types (Integer, Rational, RealDoubleElement)--the PY_NEW needs a constructor that takes no arguments. The second is often the element constructor is a bound method, in which case the parent is implicitly already passed in. 

> sage/structure/parent.pyx:256 (typo) this it will always be 

Fixed. 

> In the Parent class, why is it not the case that __call__ delegates to coerce?

Coerce throws a (potentially expensive) error on failure.

> sage/structure/parent.pyx:256 - needs to be wrapped in a list to prevent modification

Note sure what you mean here. 

> sage/structure/parent.pyx:~438 - Hom vs. hom should be explained in docs (definitions are there, but perhaps a warning)

Not sure I understand what you mean by warning. These functions (and their documentation) are mostly verbatim from the old Parent. 

> sage/structure/parent.pyx:597-9 etc. - should this be a copy?

You're right, though now these lists aren't modified near as often. 

> sage/structure/parent.pyx:530-1 - why not use the _generic_convert_map here? why does coerce_list use _generic_convert_map? what is the difference?

This should be a coercion, not a conversion. Also, Hom could do something special here. (This code is not mine, don't want to break it now.) 

> sage/structure/parent.pyx:807-24 - needs to be resolved

This needs to be thought through some more, but I think leaving the code and comments there does a good job of expressing our intent. 

> sage/structure/parent.pyx:839 - what does '"best"' mean? (868 - will this change in future patches?)

One that has the lowest _coerce_cost sum, but in reality it isn't used yet. I've changed the docstring to reflect this. 

> Can you clarify why _coerce_map_from_ is checked for overrides, but there is no such check for conversion?

Because _coerce_map_from_ and _has_coerce_map_from_ circularly call each other. I clarified this a bit more. 

> Why was coerce graph removed? :-(

It wasn't working. I want this too, but it should probably be a separate ticket. 

> sage/structure/category_object.pyx:500 WHY ARE YOU WRITING Pyrex?

That was old documentation, but I changed it. 

> All the comment blocks at the beginning of files are in the old style. i.e. copyright 2006... etc.

Lets fix this with another ticket. 

> Sometime it's pretty hard to figure out what's going on because there is some pretty damn random stuff with no docs or comments at all. (not a blocking comment, just saying...)

I tried to be really explicit with what I'm doing (especially the new stuff) but I won't claim to be perfect. Please ask if there is a particularly befuddling spot. A lot of parent is really, really old code too. 

> Why are inexact morphisms bad, Mommy?

Because they may not commute (e.g. due to rounding errors), and potentially loose information. 

> sage/structure/coerce_actions - Why are left and right different, my friends? Python?

As an example, let R be a non-commutative ring, and a \in R. Then a acts on elements in R[x] by multiplication on the left and by multiplication on the right. 

> sage/structure/coerce_actions.pyx:193 - typo "rikght"

Oops. 

> The inplace stuff needs more explanation.

Added comment. Currently the threshold is set to 0, so no inplace operations are used. 

> In coerce_map.pyx, "differs" should be "defers" in several places.

Oops again. 

> There are a lot of if-else statements which special case out things which are automatically handled by Python syntax. Is this for speed?

Probably, do you have an example? 

> sage/structure/coerce.pyx gets four thumbs up.

Thanks.


---

Comment by ncalexan created at 2008-08-14 06:51:32

> > sage/structure/parent.pyx:256 - needs to be wrapped in a list to prevent modification
> 
> Note sure what you mean here. 

There are a few cases where input lists are assigned as is, and then returned to the user (think of gens).  That allows a user to say:

sage: x = R.gens()
sage: x[0] = 0
sage: R.gens()
*wrong*

> > sage/structure/coerce_actions - Why are left and right different, my friends? Python?
> 
> As an example, let R be a non-commutative ring, and a \in R. Then a acts on elements in R[x] by multiplication on the left and by multiplication on the right. 

Sorry, that wasn't clear.  One of the actions has in_place, the other does not.  Why are they so different?  Is it because there is a *= g but no g =* a?

> > There are a lot of if-else statements which special case out things which are automatically handled by Python syntax. Is this for speed?
> 
> Probably, do you have an example?

There is some code that checks if args is not None, and then kwds is not None, and dispatches f(x), f(x, *args), f(x, *args, **kwds) accordingly.  Seems odd.


---

Comment by robertwb created at 2008-08-14 07:17:23

>>> sage/structure/parent.pyx:256 - needs to be wrapped in a list to prevent modification

>> Not sure what you mean here.

> There are a few cases where input lists are assigned as is, and then returned to the user (think of gens)...

I think they're all OK now. Gens is not passed in this way for instance. 


>> sage/structure/coerce_actions - Why are left and right different, my friends? Python?

>>  As an example, let R be a non-commutative ring, and a \in R. Then a acts on elements in R[x] by multiplication on the left and by multiplication on the right.

> Sorry, that wasn't clear. One of the actions has in_place, the other does not. Why are they so different? Is it because there is a *= g but no g =* a? 

Yes, exactly. 

>>> There are a lot of if-else statements which special case out things which are automatically handled by Python syntax. Is this for speed?

>> Probably, do you have an example?

> There is some code that checks if args is not None, and then kwds is not None, and dispatches f(x), f(x, *args), f(x, *args, **kwds) accordingly. Seems odd. 

Yes, this is for speed. Calling functions with variable-length arguments (and especially keywords) can be an non-negligible overhead for simple elements, and by by far the most common case is to have neither or just a single argument which the code is optimized for.


---

Comment by rlm created at 2008-08-14 07:53:13

Replying to [comment:14 robertwb]:
> >>> sage/structure/parent.pyx:256 - needs to be wrapped in a list to prevent modification
> 
> >> Not sure what you mean here.
> 
> > There are a few cases where input lists are assigned as is, and then returned to the user (think of gens)...
> 
> I think they're all OK now. Gens is not passed in this way for instance. 

I seem to recall a few instances where this happened which wasn't covered by your latest patch. After looking for a while I can't find any, but I am pretty tired.


I just want to say again, this code looks __SOLID__. Excellent work!


---

Comment by craigcitro created at 2008-08-14 10:14:15

I just want to pipe in and say that I'm really happy to see this getting merged. I haven't had as much time as I'd like to look through the code, but what I've seen looks good. I think that merging this and going from there is the way to go. My plan for refereeing is to start by writing some documentation about how exactly the new coercion code should be working, and seeing if it does as claimed. I'll start submitting some patches with more documentation as soon as I can, but since Nick and Robert have already looked over the first bits of this, I'm happy to say we merge it and go from there.


---

Comment by mabshoff created at 2008-08-14 16:47:41

Someone please review 3738-cardinality.patch and 3738-referee-comments.patch so that I can merge those two patches and close the ticket.

Cheers,

Michael


---

Comment by rlm created at 2008-08-14 16:51:06

Replying to [comment:18 mabshoff]:
> Someone please review 3738-cardinality.patch and 3738-referee-comments.patch so that I can merge those two patches and close the ticket.

I'll give this a positive review. I haven't run tests with `3738-cardinality.patch`, but it's an obvious typo fix. The patch `3738-cardinality.patch` addresses all of the issues in the referee comments (which are both Nick's and mine, for the record).

 + 1


---

Comment by rlm created at 2008-08-14 16:55:33

Rather,

The patch `3738-referee-comments.patch` addresses all of the issues in the referee comments (which are both Nick's and mine, for the record).


---

Comment by mabshoff created at 2008-08-14 16:57:44

Merged 3738-cardinality.patch and 3738-referee-comments.patch in Sage 3.1.rc0.

Can someone please tell me how the credit should be assigned on this ticket? My impression:

Code: Robert Bradshaw, David Roe
Review: Nick Alexander, Robert Miller, Craig Citro

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-14 16:57:44

Resolution: fixed


---

Comment by ncalexan created at 2008-08-14 17:22:16

I, ncalexan, am fine with review credit.


---

Comment by mabshoff created at 2008-08-14 22:11:49

We need the following fix to make doctests pass with the patches applied:

```
--- a/sage/structure/parent.pyx Wed Aug 13 18:50:14 2008 -0700
+++ b/sage/structure/parent.pyx Thu Aug 14 15:03:16 2008 -0700
`@``@` -16,6 +16,8 `@``@`
 cimport element
 cimport sage.categories.morphism as morphism
 cimport sage.categories.map as map
+
+from copy import copy
```

Credit goes to William.

Cheers,

Michael


---

Comment by robertwb created at 2008-08-15 07:23:49

Re credit, that looks good to me.
