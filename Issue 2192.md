# Issue 2192: [with patch, needs review] various Dirichlet character fixes/improvements

Issue created by migration from https://trac.sagemath.org/ticket/2192

Original creator: craigcitro

Original creation time: 2008-02-17 11:58:22

Assignee: craigcitro

CC:  ncalexan

This patch does a number of different things:

 * It makes it so that for `chi` a Dirichlet character, `chi.__call__` has a new
   optional argument "integral_value", which makes it return values in the 
   maximal order of a cyclotomic field, instead of the cyclotomic field. I 
   needed this so that I could multiply `chi(n)` by an element of a finite field,
   so that it can do coercion for me. In the process of doing this, I ended
   up doing all of the following as well:

 * There was a big "TODO" in the `values()` method for Dirichlet characters, 
   where William left a suggestion for a way to improve the speed of finding 
   all the values of a Dirichlet character. I did this, and here's the result.
   (Note that it caches values, so evaluating on the same character repeatedly
   will only test the code once.)

   BEFORE:
   {{{
   sage: G = DirichletGroup(960)
   sage: time for chi in G: ls = chi.values()
   CPU times: user 2.03 s, sys: 0.20 s, total: 2.22 s
   Wall time: 2.22
   sage: G = DirichletGroup(1040)
   sage: time for chi in G: ls = chi.values()
   CPU times: user 4.11 s, sys: 0.41 s, total: 4.52 s
   Wall time: 4.52
   }}}

   AFTER: 
   {{{
   sage: G = DirichletGroup(960)
   sage: time for chi in G: ls = chi.values()
   CPU times: user 0.50 s, sys: 0.01 s, total: 0.50 s
   Wall time: 0.50
   sage: G = DirichletGroup(1040)
   sage: time for chi in G: ls = chi.values()
   CPU times: user 1.11 s, sys: 0.01 s, total: 1.12 s
   Wall time: 1.12
   }}}

 * I also noticed that evaluating the trivial character was falling through to
   some overly complicated code. Here's the comparison:

   BEFORE:
   {{{
   sage: id = DirichletGroup(1).0
   sage: n = 3
   sage: time for _ in range(1000000): x = id(n)
   CPU times: user 12.08 s, sys: 0.90 s, total: 12.98 s
   Wall time: 12.98
   }}}

   AFTER:
   {{{
   sage: id = DirichletGroup(1).0
   sage: n = 3
   sage: time for _ in range(1000000): x = id(n)
   CPU times: user 3.63 s, sys: 0.74 s, total: 4.37 s
   Wall time: 4.37
   }}}

 * While working on this, I noticed that elements of `CyclotomicField(3)`
   and other degree 2 cyclotomic fields were being represented as 
   `NumberFieldElement`s, not `NumberFieldElement_quadratic`s. I fixed this,
   which involves one silly-looking but necessary piece of code in 
   number_field_element_quadratic.pyx -- it has to convert between two 
   representations of elements, so some amount of mess is unavoidable.

 * I fixed one small bug while doing this: as an example, before this
   patch, Sage claims that you can't coerce `zeta6` into `CyclotomicField(3)`.
   This was a pretty trivial fix.

I think that's it for this patch. 


---

Attachment


---

Comment by craigcitro created at 2008-02-17 12:10:00

Whoops ... I just realized I did an `mpz_init()` without an `mpz_clear()`, so I went and fixed that.


---

Comment by craigcitro created at 2008-02-17 12:10:00

Changing status from new to assigned.


---

Comment by ncalexan created at 2008-02-18 19:37:48

In general I like this patch, but I have the following question:

Why is the integral_values parameter necessary?  Since the output is always an algebraic integer, why not always return a result in the Maximal Order and have the coercion mechanism do the dirty work?


---

Comment by craigcitro created at 2008-02-18 19:48:35

ncalexan -- that's a good point, and I asked William exactly the same thing when I first noticed this. The issue is this: the *main* place that values of Dirichlet characters get used in Sage right now is in modular symbols calculations, which happen over a field (because it's all linear algebra). As a result, if we switched it to always return an element of the maximal order, the modular symbols code would pay the price of doing coercions *every* time it did, well, anything with Dirichlet characters, which is no good.


---

Comment by was created at 2008-02-19 02:36:05

REFEREE REPORT:

Very good patch.  A few minor points:

1. There is at least one more "pyrex"'s that should be Cython appearing in the patch(ed) files.

2. The doctests of {_lift_cyclotomic_element(self, new_parent)} in `number_field_element_quadratic.pyx` are NOT testing quadratic elements.  Change the doctests to test the right thing.

3. This appears twice in the code now:

```
        # Right now, I'm a little confused why quadratic extension
        # fields have a zeta_order function. I would rather they not
        # have this function, since I don't want to do this isinstance
        # check here.
```

Maybe we could delete it?  Or?

4. A comment says:

```
	        if new_parent.degree() == 2: 
	            ## we can only get here if self.parent() and 
	            ## new_parent are exactly the two fields 
	            ## CyclotomicField(3) and CyclotomicField(6) 
```

Why?

5. Regarding the `integral_value` point, the current implementation
(in this patch) is wrong.  The right solution should be to make it 
so this works:

```
sage: G = DirichletGroup(60, CyclotomicField(4).ring_of_integers())
<boom right now>
```


Right now this fails because `is_field` isn't defined for rings 
of integers (see trac #2208). However that should get fixed.  The
idea with the DirichletGroup command is that `DirichletGroup(N,R)`
gives Dirichlet characters with values in R.  One shouldn't use an option to `__call__` to determine the values of the character.  Code like this

```
            if not integral_value:
                return result
            else:
                return self.base_ring().ring_of_integers()(result)
```

in the patch will actually break if one makes `DirichletGroup(N,R)`
and R doesn't have a `ring_of_integer()` function, and the user asks for `integral_value`. 

SUMMARY: Improve the comments a little, get rid of the `integral_value` option, and make a new trac ticket for fixing `DirichletGroup(N,R)` so it works when R is the ring of integers.  Also possibly make `DirichletGroup(N, integral=True)` return the group with values in the ring of integers of the best cyclotomic field. 

William


---

Comment by craigcitro created at 2008-03-14 07:39:15

single patch with all changes


---

Attachment

I've fixed several things, addressed all the referee's comments, and attached a new patch. Here's a quick description of what went into the new patch:

 * Took William's advice, and simply fixed `DirichletGroup(N,R)` to do what one would    expect. Removed the `integral_value` option my previous patch introduced.

 * Fixing this, and making it work, involved changing something: 
   {{{
   sage: CyclotomicField(5).zeta_order()
   }}}
   has become
   {{{
   sage: CyclotomicField(5).zeta_order()
   10
   sage: CyclotomicField(5)._n()
   5
   }}}
   That is, I've made it explicit that adding an `n`th root of unity with `n` odd adds a `2n`th root of unity. I debated not doing this, but it ended up being that if I didn't make this change, then every time someone called `zeta_order()` on a `CyclotomicField`, they had to check to see if the result was odd, and if so, multiply it by two to actually make what they were doing correct. I figured that this was a much better fix, and William agreed, so it seemed like a reasonable plan. 
   This involved making lots of changes all over the place, and introducing the `_n()` method. I've tested it pretty thoroughly, so I don't think there's any craziness left, but I'm happy to fix bugs if I've missed anything.
   Making `CyclotomicField(3)(CyclotomicField(6).0)` still work correctly with this change took some extra coding. I mention this so that whoever is reviewing this patch doesn't think I was changing things at random.

Just for the sake of completeness, let me address all the comments in William's referee report:

 1. Changed all the `pyrex`s to `cython`s.
 1. Actually, this doctests are perfectly fine. Notice that (somewhat counter-intuitively for me, as well as you) it's a method on the *element*, not on the *field*. So if `x` is in a quadratic extension, `x._lift_cyclotomic_element(...)` calls specifically that code. 
 1. Yep, took those out. I always feel rude removing other people's comments -- after all, if I leave comments in the code, I think it's for a reason. But these are now gone.
 1. This is similar to (2) -- the issue is that in that case, you know both `self.parent()` and `new_parent` are cyclotomic fields of degree 2 over Q, and that an embedding is possible. Actually, I guess you could also have cf3 and cf3, or cf6 and cf6. The code still works in this case, but I've corrected the comment and I'll add the patch after I finish typing this.
 1. Done. I agree, this is cleaner. I didn't read until the end that you thought it should be on a separate ticket, so I'm including it here (since it's already pretty mixed in with this character code). I also added the `integral` flag.

I think that covers it.


---

Attachment

apply after trac-2192-full.patch


---

Comment by mabshoff created at 2008-03-15 07:26:41

Resolution: fixed


---

Comment by mabshoff created at 2008-03-15 07:26:41

Merged both patches as directed in Sage 2.10.4.alpha0
