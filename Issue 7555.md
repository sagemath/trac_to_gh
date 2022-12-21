# Issue 7555: Fix Cayley tables, add operation tables

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2009-11-29 18:55:58

Assignee: AlexGhitza

CC:  jason dimpase nthiery

Keywords: cayley table, operation table

Cayley tables for permutation groups are broken, see #7340.

For other finite algebraic structures, it would be useful for educational purposes to have tables for whatever operation(s) may be present.

Text file included here provides a class that creates a Cayley table object, it can be generalized to provide a similar table for any object with an addition or multiplication - general groups and rings would be the first places to use it.


---

Attachment

Experimental Cayley table class, cut/paste into a notebook cell


---

Comment by rbeezer created at 2009-11-29 18:58:28

Changing status from new to needs_work.


---

Comment by rbeezer created at 2010-03-15 23:36:47

Patch contains a new class, `OperationTable`.

This is meant for educational applications, and is unlikely to be used for anything much bigger than can be displayed on a screen or a sheet of paper.  So the speed (it is a bit slow) is not a concern.

Since it only requires a binary operation, I created the groupoids directory, based on the existence of  a category by the same name.

Next thing will be an application of this class to generic groups, fixing #7340.  There are stubs left here for methods to create color and grayscale graphics of the tables.


---

Comment by rbeezer created at 2010-03-15 23:36:47

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2010-03-17 01:04:19

Changing status from needs_review to needs_work.


---

Comment by rbeezer created at 2010-03-17 01:04:19

It seems a better place to place this is within the categories framework, making it available automatically in a large number of situations.  So it is being reworked right now.  The main routine won't change much at all, so time spent reviewing largely won't need to be redone.  But you'll want to wait on testing.  I'll have an updated patch soon.


---

Attachment


---

Comment by rbeezer created at 2010-03-18 04:46:49

I've tied the new `OperationTable` class into the categories framework as a multiplication table for Semigroups and as an addition table for Commutative Additive Semigroups.  I've also added it as a Cayley table for groups, since I'd like to later expand this somewhat to take advantage of the extra structure in groups.

The old Cayley table was used to build Latin squares.  I believe the behavior now with the new cayley table will be identical - IF the identity is the first element of the group.

Had a hard time constructing a nontrivial finite additive semigroup, so the documentation there is barebones right now.

As more structures become available in the categories this should be all ready to go, unchanged.  Right now it already makes the multiplication table available for all groups, rather than just permutation groups.


---

Comment by rbeezer created at 2010-03-18 04:46:49

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2010-03-18 11:28:12

Hi Rob!

Very nice patch! I'll sure use it soon :-)

Replying to [comment:4 rbeezer]:
> I've tied the new `OperationTable` class into the categories framework as a multiplication table for Semigroups and as an addition table for Commutative Additive Semigroups.  I've also added it as a Cayley table for groups, since I'd like to later expand this somewhat to take advantage of the extra structure in groups.

That's the way to go!

Out of curiosity: what are the specific features of groups that could
be useful?

> The old Cayley table was used to build Latin squares.  I believe the behavior now with the new cayley table will be identical - IF the identity is the first element of the group.

Isn't that more "if the elements are listed in the same order"?

> Had a hard time constructing a nontrivial finite additive semigroup, so the documentation there is barebones right now.

In waiting for something better, you may want to include a test with a
commutative additive group like:


```
    sage: Z5 = IntegerModRing(5)
```


By the way:


```
    sage: from sage.categories.examples.commutative_additive_monoids import FreeCommutativeAdditiveMonoid
    sage: F=FreeCommutativeAdditiveMonoid(('a', 'b'))
```


Is better constructed as::


```
    sage: F = CommutativeAdditiveMonoids().example(('a','b'))
```


And actually should eventually become:


```
    sage: F = CommutativeAdditiveMonoids().free(('a','b'))
```




> As more structures become available in the categories this should be all ready to go, unchanged.  Right now it already makes the multiplication table available for all groups, rather than just permutation groups.

And for semigroups, which I am very interested in :-) Actually, it
could be generalized to Magmas() (just a binary operation, not
necessarily associative) once we have this category.

I browsed quickly through the patch. Here are some suggestions for
improvements:

 - Pass the operation as a function (like operator.mul)
   Then OperationTable will be useful for any binary operation

 - For addition or multiplication, the user won't call directly
   OperationTable, but rather use S.addition_table() /
   S.multiplication_table(). So I would remove the guessing
   feature, and make ``operation`` a required parameter.

   (and possibly add an operation_symbol = "+" option?)

 - Remove the restriction for the empty operation table, unless
   absolutely necessary.

 - comparisons by < do not seem that meaningful. I would just test
   equality of operation tables. Then, there are two possible
   semantics:

    - two tables are equal if they correspond to the same algebraic
      structure, operation and element order

    - two tables are equal if they are equal as "functions", i.e. the
      two operations both map the i-th and j-th element to the same
      k-th element (that's what the current comparison by list of ints
      does)

   I don't have a preference yet.

Note: in many other places, we will need a class for matrices with row
and indices indexed by any objects, and not just integers. This is a
good first step, and it will remain to extract a more general super
class. To prepare the ground, I would suggest the following:

 - Rename list to index_set, or maybe row_index_set, to avoid
   confusion with the usual semantic of list.

 - dict is a bit vague. It is related to ranking (see EnumeratedSets).
   Maybe row_rank, or row_rank_dict.

Is ascii_table really needed? I would tend to just implement _repr_,
and not teach the user another specific way of getting the
representation.

By the way: several other Sage objects (like matrices, partitions,
...) are starting to have a 2d ascii art representation.  We should
standardize the handling of those.

Please add (and use?) a __getitem__ method. It will make
OperationTable not only useful for printing, but also as a useful data
structure for computations.

The last issue is the name of the methods. When we discussed this at
Sage Days 15, we had settled for P.product(x,y) and P.summation(x,y)
as names for the two operations (the choice was not that clear, and
the prevailing argument has been consistency with prod and sum
respectively, and naming the *result* of the operation on x and y)
[1]. Consistency would then call for P.product_table and
P.summation_table, though that is not so nice.


[1] http://trac.sagemath.org/sage_trac/wiki/CategoriesRoadMap

Cheers,
				Nicolas


---

Comment by nthiery created at 2010-03-18 11:28:23

Changing status from needs_review to needs_work.


---

Comment by rbeezer created at 2010-03-18 18:01:21

Replying to [comment:5 nthiery]:

Dear Nicolas,

I knew you'd have some comments!  Thanks for all the helpful advice and suggestions, on categories, and in general.

> That's the way to go!

Yes, it certainly is.  ;-)

> Out of curiosity: what are the specific features of groups that could
> be useful?

Grab a normal subgroup, as close to size sqrt(n) as you can get (perhaps automatically), then order elements in bunches as cosets.  You can sometimes see the quotient structure in the table, especially if done graphically.  But maybe this belongs higher up the hierarchy?

> > The old Cayley table was used to build Latin squares.  I believe the behavior now with the new cayley table will be identical - IF the identity is the first element of the group.
>
> Isn't that more "if the elements are listed in the same order"?

That would of course be sufficient.  The code is a bit cryptic, but it appeared to me that if the identity was first, then the elements were numbered in the order they were listed.  But I didn't study it that carefully, since I was going to pull it out anyway.  Hopefully the change doesn't cause anybody any trouble.

> In waiting for something better, you may want to include a test with a
> commutative additive group like:
>
> {{{
>     sage: Z5 = IntegerModRing(5)
> }}}

I tried this repeatedly.  You get `addition_table` with tab completion, but then


```
AttributeError: 'IntegerModRing_generic' object has no attribute 'addition_table'
```


when you try to execute it. Similarly for `cayley_graph`.  And `FiniteField`s I just assumed rings were not plugged-in yet.  Is there an easy fix?


> Is better constructed as::
>
> {{{
>     sage: F = CommutativeAdditiveMonoids().example(('a','b'))
> }}}

Will do.

> Actually, it
> could be generalized to Magmas() (just a binary operation, not
> necessarily associative) once we have this category.

Yes, I wanted this category.  Will there be two - additive and multiplicative?  Also called "groupoids" if we want avoid confusion with the CAS.  Doing `search_src` on "magma" turns up lots of things related to the program, not the structure.

> I browsed quickly through the patch. Here are some suggestions for
> improvements:
>
>  - Pass the operation as a function (like operator.mul)
>    Then OperationTable will be useful for any binary operation
>
>  - For addition or multiplication, the user won't call directly
>    OperationTable, but rather use S.addition_table() /
>    S.multiplication_table(). So I would remove the guessing
>    feature, and make ``operation`` a required parameter.

Guessing was a "feature" before I found categories.  It'll go away.

>    (and possibly add an operation_symbol = "+" option?)
>
>  - Remove the restriction for the empty operation table, unless
>    absolutely necessary.

Didn't check, but thought I'd have to add lots more logic to handle this case.  Maybe not.

>  - Rename list to index_set, or maybe row_index_set, to avoid
>    confusion with the usual semantic of list.

How about "headings"?

>  - dict is a bit vague. It is related to ranking (see EnumeratedSets).
>    Maybe row_rank, or row_rank_dict.

The returned dictionary pairs elements with their names.  Names can be any string, not just integers, so this doesn't feel like a ranking or an enumerated set to me.  It's more of a translation table.  So maybe there is a better name.  "translation"?  But I think rank would be confusing.

> Is ascii_table really needed? I would tend to just implement _repr_,
> and not teach the user another specific way of getting the
> representation.

OK

> By the way: several other Sage objects (like matrices, partitions,
> ...) are starting to have a 2d ascii art representation.  We should
> standardize the handling of those.

Yes, I did much the same thing once already for Sudoku puzzles.

> Please add (and use?) a __getitem__ method. It will make
> OperationTable not only useful for printing, but also as a useful data
> structure for computations.

Not sure how you mean this to work?  If T is a table, then T[i]=<element>, or T[i,j]=<table-entry>??  More precisely,.....

> The last issue is the name of the methods. When we discussed this at
> Sage Days 15, we had settled for P.product(x,y) and P.summation(x,y)
> as names for the two operations (the choice was not that clear, and
> the prevailing argument has been consistency with prod and sum
> respectively, and naming the *result* of the operation on x and y)
> [1]. Consistency would then call for P.product_table and
> P.summation_table, though that is not so nice.

I really had students in mind as I built this, though everybody might find it useful.  "product" is OK, "summation" sounds like more than two terms.  In any event, what about having both (ie product and multiplication, summation and addition)?  I know people don't like this, and it clutters up tab-completion.  Permutation groups had `multiplication_table` as an alias for `cayley_table`.  I'd really like this to be dead-obvious for the beginner finding their way in Sage.

Thanks again for the interest and help!

Rob


---

Comment by nthiery created at 2010-03-19 22:14:11

Hi!

Replying to [comment:7 rbeezer]:
> I knew you'd have some comments!  Thanks for all the helpful advice and suggestions, on categories, and in general.

:-)

> > Out of curiosity: what are the specific features of groups that could
> > be useful?
> Grab a normal subgroup, as close to size sqrt(n) as you can get (perhaps automatically), then order elements in bunches as cosets.  You can sometimes see the quotient structure in the table, especially if done graphically.  But maybe this belongs higher up the hierarchy?

Ok. Or maybe it can be just a helper function for how to list the
elements by default, which would be overridden in Groups.

> > In waiting for something better, you may want to include a test with a
> > commutative additive group like:
> >
> > {{{
> >     sage: Z5 = IntegerModRing(5)
> > }}}
> 
> I tried this repeatedly.  You get `addition_table` with tab completion, but then
> 
> {{{
> AttributeError: 'IntegerModRing_generic' object has no attribute 'addition_table'
> }}}
> 
> when you try to execute it. Similarly for `cayley_graph`.  And `FiniteField`s I just assumed rings were not plugged-in yet.  Is there an easy fix?

See #8562, which you are very welcome to review :-) IntegerModRing's
were not yet categorified. I'll upload a patch after running the full
tests on it.

> > Actually, it could be generalized to Magmas() (just a binary
> > operation, not necessarily associative) once we have this
> > category.
> 
> Yes, I wanted this category.  Will there be two - additive and multiplicative?  Also called "groupoids" if we want avoid confusion with the CAS.  Doing `search_src` on "magma" turns up lots of things related to the program, not the structure.

With groupds, there is a possible confusion with the other use of
groupoids (http://en.wikipedia.org/wiki/Groupoid) which is about
having a partially defined operation; but with associativity holding
whenever meaningful.

Thanks to the s, there is no naming clash between Magmas and Magma, so
that's probably fine (http://en.wikipedia.org/wiki/Magma_%28algebra%29)

> Guessing was a "feature" before I found categories.  It'll go away.

Great.

> >    (and possibly add an operation_symbol = "+" option?)
> >
> >  - Remove the restriction for the empty operation table, unless
> >    absolutely necessary.
> 
> Didn't check, but thought I'd have to add lots more logic to handle this case.  Maybe not.

Ok; let me know how it goes.

> >  - Rename list to index_set, or maybe row_index_set, to avoid
> >    confusion with the usual semantic of list.
> 
> How about "headings"?

Thinking twice about it, I vote for m.column_keys() / m.row_keys() for
consistency with the d.keys() of a dictionary (which we also use for
Family's, and CombinatorialFreeModule elements).

> >  - dict is a bit vague. It is related to ranking (see EnumeratedSets).
> >    Maybe row_rank, or row_rank_dict.
> 

> The returned dictionary pairs elements with their names.

Ah, ok, sorry; I thought it would map an element to its position in
the list.

>  So maybe there is a better name.  "translation"?

names_of_elements? or just names? labels? element_labels?

> > By the way: several other Sage objects (like matrices, partitions,
> > ...) are starting to have a 2d ascii art representation.  We should
> > standardize the handling of those.
> 
> Yes, I did much the same thing once already for Sudoku puzzles.

Another coming soon usage will be character tables.

> > Please add (and use?) a __getitem__ method. It will make
> > OperationTable not only useful for printing, but also as a useful data
> > structure for computations.
> 
> Not sure how you mean this to work?  If T is a table, then T[i]=<element>, or T[i,j]=<table-entry>??  More precisely,.....

They multiplication table looks very much like a matrix, so one would
want, for u,v elements (not names/labels) of the group to have m[u,v]
be u*v.

> I really had students in mind as I built this, though everybody might find it useful.  "product" is OK, "summation" sounds like more than two terms.  In any event, what about having both (ie product and multiplication, summation and addition)?  I know people don't like this, and it clutters up tab-completion.  Permutation groups had `multiplication_table` as an alias for `cayley_table`.  I'd really like this to be dead-obvious for the beginner finding their way in Sage.

Yeah, hard point. multiplication / addition is consistent with __mul__
and __add__. So that's probably ok without cluttering the namespace.

By the way: congrats on being essentially the first non Sage-Combinat
contributer to categories :-) How did it go?

Cheers,
				Nicolas


---

Comment by rbeezer created at 2010-03-19 22:42:39

Hi Nicolas,

Been working most of the day straightening this up.

Allowing more general operations is a big improvement.  See example of table of commutators of a finite group once I get a patch up.  ;-)

> Ok. Or maybe it can be just a helper function for how to list the
> elements by default, which would be overridden in Groups.

I'll include a note in the source to this effect.

> See #8562, which you are very welcome to review :-) IntegerModRing's
> were not yet categorified. I'll upload a patch after running the full
> tests on it.

Aah - that answers lots of questions.  Thanks.  "categorified"??  Your English is excellent, but that is pretty bad.  ;-) ;-)  ;-)  (But it was I might have said too).

> > > Actually, it could be generalized to Magmas() (just a binary
> > > operation, not necessarily associative) once we have this
> > > category.
> > 
> > Yes, I wanted this category.  Will there be two - additive and multiplicative?  Also called "groupoids" if we want avoid confusion with the CAS.  Doing `search_src` on "magma" turns up lots of things related to the program, not the structure.
> 
> With groupds, there is a possible confusion with the other use of
> groupoids (http://en.wikipedia.org/wiki/Groupoid) which is about
> having a partially defined operation; but with associativity holding
> whenever meaningful.
> 
> Thanks to the s, there is no naming clash between Magmas and Magma, so
> that's probably fine (http://en.wikipedia.org/wiki/Magma_%28algebra%29)

Got it.

> > Didn't check, but thought I'd have to add lots more logic to handle this case.  Maybe not.
> 
> Ok; let me know how it goes.

Not too bad.  Empty latex table is nice, empty ascii table is so-so, but not worth anymore effort.

> > >  - Rename list to index_set, or maybe row_index_set, to avoid
> > >    confusion with the usual semantic of list.
> > 
> > How about "headings"?
> 
> Thinking twice about it, I vote for m.column_keys() / m.row_keys() for
> consistency with the d.keys() of a dictionary (which we also use for
> Family's, and CombinatorialFreeModule elements).

I did index_set.  ;-(

> > >  - dict is a bit vague. It is related to ranking (see EnumeratedSets).
> > >    Maybe row_rank, or row_rank_dict.
> > 
> 
> > The returned dictionary pairs elements with their names.
> 
> Ah, ok, sorry; I thought it would map an element to its position in
> the list.
> 
> >  So maybe there is a better name.  "translation"?
> 
> names_of_elements? or just names? labels? element_labels?

Used translation.  :-(


> They multiplication table looks very much like a matrix, so one would
> want, for u,v elements (not names/labels) of the group to have m[u,v]
> be u*v.

OK, that should be easy.

> Yeah, hard point. multiplication / addition is consistent with __mul__
> and __add__. So that's probably ok without cluttering the namespace.
> 
> By the way: congrats on being essentially the first non Sage-Combinat
> contributer to categories :-) How did it go?

Nice.  I like it.  I'm a fan.  And your ring patch will help me recognize when/how categorification happens.

I'm running out of time on this, it's semester break this week, so I'll throw something up soon.

Rob


---

Comment by rbeezer created at 2010-03-20 02:55:19

Illustrates doctest failure


---

Attachment

Ignore that doctest failure patch - I found the problem.


---

Comment by rbeezer created at 2010-03-20 21:25:41

Changing status from needs_work to needs_review.


---

Attachment

Patch is complete enough to review.

`__getitem__` implemented.

row_keys/column_keys are the latest name for elements in headings-order.

Left `translation` dictionary as-is.

`addition_table` is a stub of sorts.  Has a doctest, and so on, but can be much better documented when `IntegerModRing` is settled at #8562.  It'll mostly be a cut/paste job from `multiplication_table` with new examples.  

But I'd like this to move forward independently, since my time will be limited for a few weeks.


---

Comment by nthiery created at 2010-03-21 08:10:07

Hi Rob!

Replying to [comment:11 rbeezer]:
> Patch is complete enough to review.
> But I'd like this to move forward independently, since my time will be limited for a few weeks.

Thanks for you work on this. This sounds very good, so will set up a
positive review as soon as I get a running 4.3.4 sage to launch the
tests.

Three minor thing I am hesitating about:

 - Do we really want coercion in __getitem__. By default, I would tend
   to not do it for efficiency, unless a strong use case comes up in
   practice.

 - In OperationTable, there is now a bit of redundancy between S and
   elements; the only place where S is used is to coerce the elements.
   In particular, what about just accepting:

	OperationTable(iterable, operation)

   where iterable is any iterable (up to the user to make sure that it
   is finite).

   No big deal; this can be added later if desirable.

I'll probably post a small reviewer patch with once I can double check
the html doc with micro typos and, if you agree, removing coercion in
__getitem__.

Cheers,
				Nicolas


---

Comment by nthiery created at 2010-03-21 08:14:28

Replying to [comment:9 rbeezer]:
> Been working most of the day straightening this up.

Thanks!

> Allowing more general operations is a big improvement.  See example of table of commutators of a finite group once I get a patch up.  ;-)

Cool :-)
> Aah - that answers lots of questions.  Thanks.  "categorified"??  Your English is excellent, but that is pretty bad.  ;-) ;-)  ;-)  (But it was I might have said too).

:-)

> Not too bad.  Empty latex table is nice, empty ascii table is so-so, but not worth anymore effort.

Cool. Florent will appreciate not to have to handle yet another empty object :-)


---

Comment by rbeezer created at 2010-03-22 02:57:28

Replying to [comment:12 nthiery]:
Hi Nicolas,

> Three minor thing I am hesitating about:

I only see two, not that I'm looking for trouble.

>  - Do we really want coercion in __getitem__. By default, I would tend
>    to not do it for efficiency, unless a strong use case comes up in
>    practice.

Coercion here could go away - I've perhaps gone overboard with coercion, envisioning students typing in strings that are not really elements, such as permutations.  So I want to keep coercion in `__init__`.  You are right, if no coercion in `__getitem__` then the object does not need to hold a reference to S.


>  - In OperationTable, there is now a bit of redundancy between S and
>    elements; the only place where S is used is to coerce the elements.
>    In particular, what about just accepting:
>
>       OperationTable(iterable, operation)
>
>    where iterable is any iterable (up to the user to make sure that it
>    is finite).
>
>    No big deal; this can be added later if desirable.

This struck me as a good idea at first, but again, I'd like a chance to coerce the contents of `elements` (when present) into something (S, a parent), so I'd really like to keep this feature.  It's only on creation, and only once per element.  I find coercion is a hard idea for students to come to grips with, so I'd like to help out as much as possible here and not assume that the input is pure.

> I'll probably post a small reviewer patch with once I can double check
> the html doc with micro typos and, if you agree, removing coercion in
> __getitem__.

Sure, you can clean-up `__getitem__` to suit your tastes.

Thanks for all your help with this.

Rob

PS  I'm glad I can make Florent's life that much easier.  ;-)


---

Comment by nthiery created at 2010-03-22 21:36:56

Hi Robert,

The updated patch contains the following changes:

 - OperationTable is moved in sage.matrix.operation_table

 - multiplication_table and addition_table are moved in the new
   categories Magmas and AdditiveMagmas respectively (sorry, this
   introduces a dependency on #8579; but there will be many changes
   soon in Semigroups, and this will avoid later conflicts when moving
   things around)

 - __getitem__ does not do coercion anymore

 - The input can be a finite iterable, as in:


```
        sage: T = OperationTable([False, True], operator.or_, names = 'elements')
        sage: T
            .  False  True
             +------------
        False| False  True
         True|  True  True
```


 - self._elts (and thus the column/row keys) is a tuple (reduces the
   risk of accidently changing its content)

 - a couple minor doc improvements: using directly :: at the end of a
   sentence describing the next example, putting default values within
   () ...

 - I allowed myself to change the '+' and '*' to operator.add and
   operator.mul, for a more uniform logic (anyway, the basic user
   won't use OperationTable directly, and for the others, it is nice
   to show them directly the general approach).

Given that all the code was moved around, a reviewer patch would not
have brought any useful information. So I just folded everything
together.

All tests pass on my ubuntu laptop.


---

Comment by nthiery created at 2010-03-22 21:41:10

Oh, Rob, I forgot to mention: your changes are good! So this patch just needs a cross positive review from you on my changes, and I consider it as good to go.


---

Comment by rbeezer created at 2010-03-23 04:31:35

Hi Nicolas,

Thanks for all your help, and attention to this.  Changes look good, but I had trouble with #8579, so I haven't been able to test them.  Thanks for adding magmas - that is where this belongs.

More comments when I can test more.

Rob


---

Comment by nthiery created at 2010-03-23 07:16:13

Replying to [comment:17 rbeezer]:
> Hi Nicolas,
> 
> Thanks for all your help, and attention to this.  Changes look good, but I had trouble with #8579, so I haven't been able to test them.  Thanks for adding magmas - that is where this belongs.
> 
> More comments when I can test more.

Oops, sorry, I forgot to mention the trivial syntactic dependency of #8579 on #7880.


---

Comment by hivert created at 2010-03-23 13:46:42

Hi there,

The patch which is on sage-combinat queue (which seems to have to difference
which the one here) causes the following failure. This is with with
sage-4.3.4, on sage.saegmath.org and on my laptop (openSuSE 11.1):

```
sage -t  "4.3.4/devel/sage-combinat/sage/categories/groups.py"
**********************************************************************
File "/usr/local/sage/sage-4.3.4/devel/sage-combinat/sage/categories/groups.py", line 138:
    sage: T.column_keys()
Expected:
    [(), (5,6,7), (5,7,6)...(1,4,2,3)(5,7)]
Got:
    ((), (5,6,7), (5,7,6), (1,2)(3,4), (1,2)(3,4)(5,6,7), (1,2)(3,4)(5,7,6), (1,3,2,4)(6,7), (1,3,2,4)(5,6), (1,3,2,4)(5,7), (1,4,2,3)(6,7), (1,4,2,3)(5,6), (1,4,2,3)(5,7))
**********************************************************************
File "/usr/local/sage/sage-4.3.4/devel/sage-combinat/sage/categories/groups.py", line 159:
    sage: M.cayley_table()
Expected:
    *  a b c d e f
    +------------
    a| c e a f b d
    b| d f b e a c
    c| a b c d e f
    d| b a d c f e
    e| f d e b c a
    f| e c f a d b
Got:
    *  a b c d e f
     +------------
    a| d c b a f e
    b| e f a b c d
    c| f e d c b a
    d| a b c d e f
    e| b a f e d c
    f| c d e f a b
    <BLANKLINE>
**********************************************************************
1 items had failures:
   2 of  35 in __main__.example_5
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/averell/.sage//tmp/.doctest_groups.py
         [17.4 s]
sage -t  sage/categories/magmas.py
**********************************************************************
File "/mnt/usb1/scratch/hivert/sage-4.3.4-sage.math.washington.edu-x86_64-Linux/devel/sage-combinat/sage/categories/magmas.py", line 195:
    sage: T.column_keys()
Expected:
    ['a', 'b', 'ab', 'ba']
Got:
    ('a', 'b', 'ab', 'ba')
**********************************************************************
File "/mnt/usb1/scratch/hivert/sage-4.3.4-sage.math.washington.edu-x86_64-Linux/devel/sage-combinat/sage/categories/magmas.py", line 254:
    sage: T.column_keys()
Expected:
    [(), (1,2,3), (1,3,2)]
Got:
    ((), (1,2,3), (1,3,2))
**********************************************************************
1 items had failures:
   2 of  22 in __main__.example_5
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/hivert/dot_sage/tmp/.doctest_magmas.py
         [3.9 s]
```



---

Comment by rbeezer created at 2010-03-23 14:33:50

Hi Florent,

Nicolas changed a list to a tuple, so that explains part of this.  Not sure why the table changed.  I'll be working on this about 12 hours from now, so will double-check everything then.

Rob


---

Comment by nthiery created at 2010-03-23 15:23:07

Thanks Florent for catching this. Ooops, I indeed apparently forgot to rerun some tests after the list -> tuple change.

For the other one: I had made the assumption that G=SL(2,2) was a proper enumerated set, that is G.list() == list(G). It is not, which is a bug.

I guess we can ignore this, and just update the doctest output. I'll put up an updated patch when I am back home (in 2-3 hours) unless someone beats me to it.


---

Comment by nthiery created at 2010-03-23 15:23:07

Changing status from needs_review to needs_work.


---

Comment by nthiery created at 2010-03-23 16:30:55

Back online for a couple minutes. I'll upload an updated patch shortly.

SL bug on: #8588


---

Comment by nthiery created at 2010-03-23 16:35:05

Replaces all the previous ones


---

Attachment

Done. Diff to previous version on: http://combinat.sagemath.org/hgwebdir.cgi/patches/diff/233de3ecbcb7/trac_7555_operation_table-categories.patch


---

Comment by nthiery created at 2010-03-23 16:37:54

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-03-23 17:11:19

Changing status from needs_review to needs_work.


---

Comment by jason created at 2010-03-23 17:11:19

This is fantastic.  Here are some more very minor things:

 * two typos in the docs for _name_maker: "fromatting" and "adictionary"
 * in column_keys, the OUTPUT: header looks weird without a blank line between it and the following text
 * The first example on _ascii_table doesn't look like the top row lines up with the first column (the +---- line should be padded with one more space on the left)

And an enhancement:

 * If it makes sense to support slice notation in get_item, or multiple rows/columns, to get a submatrix (subtable), then it would be easy to call the sage.misc.misc_c.normalize_index on the indices that you are already finding in _get_item_ to easily get a nice subtable.


---

Comment by jason created at 2010-03-23 21:31:30

(I should add that the enhancement above is not the "needs work" request.  Also, I mainly read the documentation, but didn't look at the code too much, so my points above are not a review of the code.)


---

Comment by rbeezer created at 2010-03-24 03:40:24

Replying to [comment:24 jason]:
> This is fantastic.  Here are some more very minor things:

Jason,

Thanks for catching a few details, and for the suggestion.

This is getting mixed up with a bunch of other patches, so I'd like to finalize it.  I have to come back and improve the documentation for the addition table (once integer mod rings are straightened away), so I'll look into slicing then.

Thanks again,
Rob


---

Attachment


---

Comment by rbeezer created at 2010-03-24 05:19:39

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2010-03-24 05:19:39

Hi Nicolas,

Your changes all look good - thanks for those.  Feel free to add yourself to the author field - it'd be good to "share" a patch with you.  So this is a positive review on those.

With latest "fixup" patch, passes all tests in Sage library, docs build without warnings and look OK.

Now the ball is in your court.  A handful of little things, in a separate patch so they are easy to isolate.

- self._S is removed, since it is not needed in `__getitem__` anymore

- "\\cdot" with two backslashesfor latex symbol for generic operation, my mistake

- four fixes from Jason (above)

- title for reference manual, and GPL header in sage/matrix/operation_table.py

- fixed a reference to semigroups which has now moved

So I believe you could check these and we'd be done?

Rob


---

Comment by nthiery created at 2010-03-24 08:47:20

Replying to [comment:27 rbeezer]:
> Feel free to add yourself to the author field - it'd be good to "share" a patch with you.

Thanks for the offer! It'd be a pleasure indeed. Now, you really wrote the bulk of the code. I just did my reviewer's job: all in all, my main code contribution is the writing of the Magmas category, which is not much and for which I'll get credit separately. 

It was a pleasure working as a team on this patch, and I am looking forward writing another patch together :-) 

> With latest "fixup" patch, passes all tests in Sage library, docs build without warnings and look OK.
> ...
> So I believe you could check these and we'd be done?

Your fixups look good! I just changed the copyright header as per the
template in http://www.sagemath.org/doc/developer/conventions.html,
and used the occasion to replace a r'\blah' into '\\blah' in the
doctests for consistency with the other occurrences in this file.

I reran the tests on the file itself, and on the category code, which I
believe is sufficient. So, on my account, it's now all good to go. Feel
free to set a positive review once you have double checked my changes.


---

Attachment


---

Attachment

Apply only this one


---

Comment by nthiery created at 2010-03-24 08:54:17

Jason: feel free to add yourself as a reviewer


---

Comment by rbeezer created at 2010-03-24 15:32:29

OK, all done.  This has a (cumulative) positive review.

Thanks, Jason, for the contributions, and thanks, Nicolas, for stepping in with all the prompt help with categories and useful fixes and enhancements.  When #8562 is done the addition table docstring can be expanded - doing this is #8596.

To do:  Add slicing as Jason suggests, make graphical output (#8598).

Release manager:

This needs #7880 first, then #8579.  Apply just the "all-in-one" patch.  Once merged, #7340 (the root motivator) can be marked fixed.


---

Comment by rbeezer created at 2010-03-24 15:32:29

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 20:14:34

Merged "trac_7555_operation_table-categories-all-in-one.patch" in 4.4.alpha0


---

Comment by jhpalmieri created at 2010-04-15 20:14:34

Resolution: fixed
