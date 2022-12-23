# Issue 3810: make abelian group list/iter and classgroup list/iter more modern

Issue created by migration from https://trac.sagemath.org/ticket/3810

Original creator: ncalexan

Original creation time: 2008-08-12 04:56:23

Assignee: was

list/iter on abelian groups does not agree with .list().

Also, list on classgroups returned abstract group elements -- essentially useless:


```
sage: x = QQ['x'].0
sage: K.<a> = NumberField(x^4 + 23)
sage: G = K.class_group()
sage: G
Class group of order 3 with structure C3 of Number Field in a with defining polynomial x^4 + 23
sage: list(G)
[1, c, c^2]
```


This actually lists representatives in the class group.

Apply abelian group patch before classgroup patch.

Passes relevant tests:

```
/Users/ncalexan/sage-3.0.6/sage -b >/dev/null && /Users/ncalexan/sage-3.0.6/sage -t /Users/ncalexan/sage-3.0.6/devel/sage-nca/sage/groups/abelian_gps/*

real	0m1.610s
user	0m0.958s
sys	0m0.623s
sage -t  devel/sage-nca/sage/groups/abelian_gps/abelian_group.py
	 [5.3 s]
sage -t  devel/sage-nca/sage/groups/abelian_gps/abelian_group_element.py
	 [3.6 s]
sage -t  devel/sage-nca/sage/groups/abelian_gps/abelian_group_morphism.py
	 [3.0 s]
sage -t  devel/sage-nca/sage/groups/abelian_gps/all.py      
	 [2.2 s]
sage -t  devel/sage-nca/sage/groups/abelian_gps/dual_abelian_group.py
	 [3.9 s]
sage -t  devel/sage-nca/sage/groups/abelian_gps/dual_abelian_group_element.py
	 [3.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 20.9 seconds
```


and


```
/Users/ncalexan/sage-3.0.6/sage -b >/dev/null && /Users/ncalexan/sage-3.0.6/sage -t /Users/ncalexan/sage-3.0.6/devel/sage-nca/sage/rings/number_field/*

real	0m1.672s
user	0m0.959s
sys	0m0.618s
sage -t  devel/sage-nca/sage/rings/number_field/all.py      
	 [2.0 s]
sage -t  devel/sage-nca/sage/rings/number_field/class_group.py
	 [4.9 s]
sage -t  devel/sage-nca/sage/rings/number_field/galois_group.py
	 [3.5 s]
sage -t  devel/sage-nca/sage/rings/number_field/maps.py     
	 [2.9 s]
sage -t  devel/sage-nca/sage/rings/number_field/morphism.py 
	 [4.1 s]
sage -t  devel/sage-nca/sage/rings/number_field/number_field.py
  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.

	 [28.9 s]
sage -t  devel/sage-nca/sage/rings/number_field/number_field_base.pyx
	 [3.7 s]
sage -t  devel/sage-nca/sage/rings/number_field/number_field_element.pyx
	 [9.0 s]
sage -t  devel/sage-nca/sage/rings/number_field/number_field_element_quadratic.pyx
	 [4.0 s]
sage -t  devel/sage-nca/sage/rings/number_field/number_field_ideal.py
	 [6.6 s]
sage -t  devel/sage-nca/sage/rings/number_field/number_field_ideal_rel.py
	 [3.4 s]
sage -t  devel/sage-nca/sage/rings/number_field/order.py    
	 [10.2 s]
sage -t  devel/sage-nca/sage/rings/number_field/small_primes_of_degree_one.py
	 [3.5 s]
sage -t  devel/sage-nca/sage/rings/number_field/todo.py     
	 [2.1 s]
sage -t  devel/sage-nca/sage/rings/number_field/totallyreal.py
	 [3.1 s]
sage -t  devel/sage-nca/sage/rings/number_field/totallyreal_data.pyx
	 [2.1 s]
sage -t  devel/sage-nca/sage/rings/number_field/totallyreal_phc.py
	 [2.1 s]
sage -t  devel/sage-nca/sage/rings/number_field/totallyreal_rel.py
	 [4.3 s]
sage -t  devel/sage-nca/sage/rings/number_field/unit_group.py
	 [2.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 102.5 seconds

sage-test finished (all test passed) at Mon Aug 11 21:53:13
```



---

Attachment


---

Comment by was created at 2008-08-13 02:40:43

Needs work.  Your fix patch introduces a bug:

```
sage: G = AbelianGroup([2,3], names = "ab") sage: v = G.list()
sage: v
[1, b, b^2, a, a*b, a*b^2]
sage: v[0] = "hi nick!"
sage: G.list()
['hi nick!', b, b^2, a, a*b, a*b^2]
```



---

Attachment


---

Comment by ncalexan created at 2008-08-13 21:43:25

`3810-ncalexan-abelian-group-iter-2.patch` replaces `3810-ncalexan-abelian-group-iter.patch` and addresses referee comment.


---

Comment by cremona created at 2008-08-23 17:44:17

This is functionality which I wanted a few days ago so I am pleased to see this ticket!

I applied 3810-ncalexan-abelian-group-iter-2.patch and then 3810-ncalexan-class-group-list.patch in that order.  When Sage applied the second one I was surprised that it popped up an edit window as when one does a commit.  I just closed the window.

So I don't really know what it was I tested, but it seemed to work as advertised (and without the bug William pointed out).

Here's an enhancement I would like:  If I create an ideal class from some random ideal, nothing really happens, and I cannot tell which class I got without testing for equality with every class.  Am I missing something?  I actually would have been happy to have class group elements display as abstract group elements (as they would in Magma), as long as functions were provided to go from fractional ideals to abstract ideal classes and back again.


---

Comment by mabshoff created at 2008-08-25 02:29:18

With the two patches John mentioned I get the following doctest failure:

```
sage -t -long devel/sage/sage/rings/number_field/class_group.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/tmp/class_group.py", line 117:
    sage: list(G)
Expected:
    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 + a - 1/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
Got:
    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 - a + 3/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/tmp/class_group.py", line 119:
    sage: G.list()
Expected:
    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 + a - 1/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
Got:
    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 - a + 3/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
**********************************************************************
```

The reason that trac_3810-ncalexan-class-group-list.patch popped up a window is that it is a straight diff instead of a patch. Nick: Can you post a unified patch and delete the old ones?

Cheers,

Michael


---

Comment by cremona created at 2008-08-25 09:15:14

Those doctest differences are insignificant in that the output is mathematically identical to what is expected.  For deterministic output we need (as well as the usual sorting):  the same ideals representing each class, and the same presentation of each ideal.  Here it's just that the second ideal in the list has a different second generator.

My understanding is that these generators come from pari.  If so, it is probably safe to replace the doctest output with the new output.  Perhaps Nick could say if that sounds right to him.


---

Comment by cremona created at 2008-11-30 11:51:23

Nick, any news on this?  It might be relevant to #4061 which I am about to post a patch for.


---

Comment by ncalexan created at 2008-12-01 04:28:50

I think these should be applied.  The doctest output should be updated, but I don't have the original patch queue anymore to give a non-patch.


---

Comment by cremona created at 2008-12-06 23:09:40

Just one thing is stopping me giving this the ok:

```
sage: G=AbelianGroup([])
sage: G.list()
[]
sage: list(G)
[]
sage: G.order()
1
```

Trivial groups do have one element!  This special case is handled ok in the class groups patch, and a similar special case is needed for abelian groups.  (It happens because mrange() delivers nothing at all for an empty list of lists, that is one valid way of defining a trivial abelian group.)

What's bugging me is that I discovered that same issue with listing trivial groups myself a few days ago, and somewhere else in trac there's a patch which does what is needed here -- but I cannot remember which one!  So this might cause some merge problems when my patch goes in.

Apart from this, the second and third patches apply fine to 3.2.1 and tests pass.  *Ignore the first patch which is replaced by the third!*


---

Comment by cremona created at 2008-12-07 10:12:49

NB The patch at #4061 which has just been merged into 3.2.2 contains a fix for the trivial group list problem, so this ticket should be checked against that.  I hope to get to that today.  With luck it will mean that I can remove my one misgiving about this one!


---

Attachment

Replaces all previous; apply to 3.2.1 + #4061 patches


---

Comment by cremona created at 2008-12-07 17:15:51

I hope I have done this right.  I took a clone of 3.2.1 and applied the (already merged) patches at #4061, which included a fix for trivial abelian group list().  I merged Nick's two patches from this ticket, adapting them accordingly and fixing the trivial group thing I mentioned above, adding a doctest.  The result became the "combined" patch attached here.   It looks strange when you view it because the file abelian_groups.py has two successive diffs, but I tried applying this patch to a fresh clone (+#4061) and it does end up in the right state.

If this makes sense to Michael, and works for him, I hope this will finish off this one.


---

Comment by mabshoff created at 2008-12-08 04:22:30

I am seeing one doctest failure with this patch applied on a 64 bit Linux box:

```
sage -t -long "devel/sage/sage/rings/number_field/class_group.py"
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage/sage/rings/number_field/class_group.py", line 148, in __main__.example_8
Failed example:
    list(G)###line 117:_sage_    >>> list(G)
Expected:
    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 + a - 1/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
Got:
    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 - a + 3/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage/sage/rings/number_field/class_group.py", line 150, in __main__.example_8
Failed example:
    G.list()###line 119:_sage_    >>> G.list()
Expected:
    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 + a - 1/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
Got:
    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 - a + 3/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
**********************************************************************
```



---

Comment by cremona created at 2008-12-08 09:29:09

Replying to [comment:13 mabshoff]:
> I am seeing one doctest failure with this patch applied on a 64 bit Linux box:
> {{{
> sage -t -long "devel/sage/sage/rings/number_field/class_group.py"
> **********************************************************************
> File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage/sage/rings/number_field/class_group.py", line 148, in __main__.example_8
> Failed example:
>     list(G)###line 117:_sage_    >>> list(G)
> Expected:
>     [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 + a - 1/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
> Got:
>     [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 - a + 3/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
> **********************************************************************
> File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage/sage/rings/number_field/class_group.py", line 150, in __main__.example_8
> Failed example:
>     G.list()###line 119:_sage_    >>> G.list()
> Expected:
>     [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 + a - 1/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
> Got:
>     [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 - a + 3/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
> **********************************************************************
> }}}

What a nuisance;  sorry, I only did a 32-bit test at the weekend.   The got/expected are equally valid mathematically, and my guess is that the difference comes from the pari library.

Would it be dishonest to look for an example for the doctest where the output was identical on 32- and 64-bit machines?


---

Comment by mabshoff created at 2008-12-08 09:33:03

Replying to [comment:14 cremona]:

Hi John,

> What a nuisance;  sorry, I only did a 32-bit test at the weekend.   The got/expected are equally valid mathematically, and my guess is that the difference comes from the pari library.

Yes, Nick said the same thing in IRC, but I was asleep at that point.
 
> Would it be dishonest to look for an example for the doctest where the output was identical on 32- and 64-bit machines?

I am fine marking those two doctests with #32 bit and #64 bit output and to get the patch in. If anybody wants to have a "prettier" doctest that can be addressed via a followup patch.

Cheers,

Michael


---

Comment by cremona created at 2008-12-08 09:43:01

Replying to [comment:15 mabshoff]:
> Replying to [comment:14 cremona]:
> 
> Hi John,
> 
> > What a nuisance;  sorry, I only did a 32-bit test at the weekend.   The got/expected are equally valid mathematically, and my guess is that the difference comes from the pari library.
> 
> Yes, Nick said the same thing in IRC, but I was asleep at that point.
>  
> > Would it be dishonest to look for an example for the doctest where the output was identical on 32- and 64-bit machines?
> 
> I am fine marking those two doctests with #32 bit and #64 bit output and to get the patch in. If anybody wants to have a "prettier" doctest that can be addressed via a followup patch.

Sounds good to me.  If it is more random than that it will be picked up by the merry horde of alpha testers....

John

> 
> Cheers,
> 
> Michael
>


---

Attachment


---

Comment by cremona created at 2008-12-08 10:09:33

New patch fixes the 32/64 problem, has been tested on both.


---

Comment by mabshoff created at 2008-12-08 10:58:58

Resolution: fixed


---

Comment by mabshoff created at 2008-12-08 10:58:58

Merged sage-3810-combined.patch and sage-3810-fix64.patch in Sage 3.2.2.alpha1
