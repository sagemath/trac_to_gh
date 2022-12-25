# Issue 2192: [with patch, needs review] various Dirichlet character fixes/improvements

archive/issues_002192.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  @ncalexan\n\nThis patch does a number of different things:\n\n* It makes it so that for `chi` a Dirichlet character, `chi.__call__` has a new\n  optional argument \"integral_value\", which makes it return values in the \n  maximal order of a cyclotomic field, instead of the cyclotomic field. I \n  needed this so that I could multiply `chi(n)` by an element of a finite field,\n  so that it can do coercion for me. In the process of doing this, I ended\n  up doing all of the following as well:\n\n* There was a big \"TODO\" in the `values()` method for Dirichlet characters, \n  where William left a suggestion for a way to improve the speed of finding \n  all the values of a Dirichlet character. I did this, and here's the result.\n  (Note that it caches values, so evaluating on the same character repeatedly\n  will only test the code once.)\n\n  BEFORE:\n  {{{\n  sage: G = DirichletGroup(960)\n  sage: time for chi in G: ls = chi.values()\n  CPU times: user 2.03 s, sys: 0.20 s, total: 2.22 s\n  Wall time: 2.22\n  sage: G = DirichletGroup(1040)\n  sage: time for chi in G: ls = chi.values()\n  CPU times: user 4.11 s, sys: 0.41 s, total: 4.52 s\n  Wall time: 4.52\n  }}}\n\n  AFTER: \n  {{{\n  sage: G = DirichletGroup(960)\n  sage: time for chi in G: ls = chi.values()\n  CPU times: user 0.50 s, sys: 0.01 s, total: 0.50 s\n  Wall time: 0.50\n  sage: G = DirichletGroup(1040)\n  sage: time for chi in G: ls = chi.values()\n  CPU times: user 1.11 s, sys: 0.01 s, total: 1.12 s\n  Wall time: 1.12\n  }}}\n\n* I also noticed that evaluating the trivial character was falling through to\n  some overly complicated code. Here's the comparison:\n\n  BEFORE:\n  {{{\n  sage: id = DirichletGroup(1).0\n  sage: n = 3\n  sage: time for _ in range(1000000): x = id(n)\n  CPU times: user 12.08 s, sys: 0.90 s, total: 12.98 s\n  Wall time: 12.98\n  }}}\n\n  AFTER:\n  {{{\n  sage: id = DirichletGroup(1).0\n  sage: n = 3\n  sage: time for _ in range(1000000): x = id(n)\n  CPU times: user 3.63 s, sys: 0.74 s, total: 4.37 s\n  Wall time: 4.37\n  }}}\n\n* While working on this, I noticed that elements of `CyclotomicField(3)`\n  and other degree 2 cyclotomic fields were being represented as \n  `NumberFieldElement`s, not `NumberFieldElement_quadratic`s. I fixed this,\n  which involves one silly-looking but necessary piece of code in \n  number_field_element_quadratic.pyx -- it has to convert between two \n  representations of elements, so some amount of mess is unavoidable.\n\n* I fixed one small bug while doing this: as an example, before this\n  patch, Sage claims that you can't coerce `zeta6` into `CyclotomicField(3)`.\n  This was a pretty trivial fix.\n\nI think that's it for this patch. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2192\n\n",
    "created_at": "2008-02-17T11:58:22Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "[with patch, needs review] various Dirichlet character fixes/improvements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2192",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

CC:  @ncalexan

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

Issue created by migration from https://trac.sagemath.org/ticket/2192





---

archive/issue_comments_014354.json:
```json
{
    "body": "Attachment [trac-2192-pt2.patch](tarball://root/attachments/some-uuid/ticket2192/trac-2192-pt2.patch) by @craigcitro created at 2008-02-17 12:09:26",
    "created_at": "2008-02-17T12:09:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2192#issuecomment-14354",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-2192-pt2.patch](tarball://root/attachments/some-uuid/ticket2192/trac-2192-pt2.patch) by @craigcitro created at 2008-02-17 12:09:26



---

archive/issue_comments_014355.json:
```json
{
    "body": "Whoops ... I just realized I did an `mpz_init()` without an `mpz_clear()`, so I went and fixed that.",
    "created_at": "2008-02-17T12:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2192#issuecomment-14355",
    "user": "https://github.com/craigcitro"
}
```

Whoops ... I just realized I did an `mpz_init()` without an `mpz_clear()`, so I went and fixed that.



---

archive/issue_comments_014356.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-17T12:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2192#issuecomment-14356",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014357.json:
```json
{
    "body": "In general I like this patch, but I have the following question:\n\nWhy is the integral_values parameter necessary?  Since the output is always an algebraic integer, why not always return a result in the Maximal Order and have the coercion mechanism do the dirty work?",
    "created_at": "2008-02-18T19:37:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2192#issuecomment-14357",
    "user": "https://github.com/ncalexan"
}
```

In general I like this patch, but I have the following question:

Why is the integral_values parameter necessary?  Since the output is always an algebraic integer, why not always return a result in the Maximal Order and have the coercion mechanism do the dirty work?



---

archive/issue_comments_014358.json:
```json
{
    "body": "ncalexan -- that's a good point, and I asked William exactly the same thing when I first noticed this. The issue is this: the *main* place that values of Dirichlet characters get used in Sage right now is in modular symbols calculations, which happen over a field (because it's all linear algebra). As a result, if we switched it to always return an element of the maximal order, the modular symbols code would pay the price of doing coercions *every* time it did, well, anything with Dirichlet characters, which is no good.",
    "created_at": "2008-02-18T19:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2192#issuecomment-14358",
    "user": "https://github.com/craigcitro"
}
```

ncalexan -- that's a good point, and I asked William exactly the same thing when I first noticed this. The issue is this: the *main* place that values of Dirichlet characters get used in Sage right now is in modular symbols calculations, which happen over a field (because it's all linear algebra). As a result, if we switched it to always return an element of the maximal order, the modular symbols code would pay the price of doing coercions *every* time it did, well, anything with Dirichlet characters, which is no good.



---

archive/issue_comments_014359.json:
```json
{
    "body": "REFEREE REPORT:\n\nVery good patch.  A few minor points:\n\n1. There is at least one more \"pyrex\"'s that should be Cython appearing in the patch(ed) files.\n\n2. The doctests of {_lift_cyclotomic_element(self, new_parent)} in `number_field_element_quadratic.pyx` are NOT testing quadratic elements.  Change the doctests to test the right thing.\n\n3. This appears twice in the code now:\n\n```\n        # Right now, I'm a little confused why quadratic extension\n        # fields have a zeta_order function. I would rather they not\n        # have this function, since I don't want to do this isinstance\n        # check here.\n```\n\nMaybe we could delete it?  Or?\n\n4. A comment says:\n\n```\n\t        if new_parent.degree() == 2: \n\t            ## we can only get here if self.parent() and \n\t            ## new_parent are exactly the two fields \n\t            ## CyclotomicField(3) and CyclotomicField(6) \n```\n\nWhy?\n\n5. Regarding the `integral_value` point, the current implementation\n(in this patch) is wrong.  The right solution should be to make it \nso this works:\n\n```\nsage: G = DirichletGroup(60, CyclotomicField(4).ring_of_integers())\n<boom right now>\n```\n\n\nRight now this fails because `is_field` isn't defined for rings \nof integers (see trac #2208). However that should get fixed.  The\nidea with the DirichletGroup command is that `DirichletGroup(N,R)`\ngives Dirichlet characters with values in R.  One shouldn't use an option to `__call__` to determine the values of the character.  Code like this\n\n```\n            if not integral_value:\n                return result\n            else:\n                return self.base_ring().ring_of_integers()(result)\n```\n\nin the patch will actually break if one makes `DirichletGroup(N,R)`\nand R doesn't have a `ring_of_integer()` function, and the user asks for `integral_value`. \n\nSUMMARY: Improve the comments a little, get rid of the `integral_value` option, and make a new trac ticket for fixing `DirichletGroup(N,R)` so it works when R is the ring of integers.  Also possibly make `DirichletGroup(N, integral=True)` return the group with values in the ring of integers of the best cyclotomic field. \n\nWilliam",
    "created_at": "2008-02-19T02:36:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2192#issuecomment-14359",
    "user": "https://github.com/williamstein"
}
```

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

archive/issue_comments_014360.json:
```json
{
    "body": "single patch with all changes",
    "created_at": "2008-03-14T07:39:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2192#issuecomment-14360",
    "user": "https://github.com/craigcitro"
}
```

single patch with all changes



---

archive/issue_comments_014361.json:
```json
{
    "body": "Attachment [trac-2192-full.patch](tarball://root/attachments/some-uuid/ticket2192/trac-2192-full.patch) by @craigcitro created at 2008-03-14 08:02:15\n\nI've fixed several things, addressed all the referee's comments, and attached a new patch. Here's a quick description of what went into the new patch:\n\n* Took William's advice, and simply fixed `DirichletGroup(N,R)` to do what one would    expect. Removed the `integral_value` option my previous patch introduced.\n\n* Fixing this, and making it work, involved changing something: \n  {{{\n  sage: CyclotomicField(5).zeta_order()\n  }}}\n  has become\n  {{{\n  sage: CyclotomicField(5).zeta_order()\n  10\n  sage: CyclotomicField(5)._n()\n  5\n  }}}\n  That is, I've made it explicit that adding an `n`th root of unity with `n` odd adds a `2n`th root of unity. I debated not doing this, but it ended up being that if I didn't make this change, then every time someone called `zeta_order()` on a `CyclotomicField`, they had to check to see if the result was odd, and if so, multiply it by two to actually make what they were doing correct. I figured that this was a much better fix, and William agreed, so it seemed like a reasonable plan. \n  This involved making lots of changes all over the place, and introducing the `_n()` method. I've tested it pretty thoroughly, so I don't think there's any craziness left, but I'm happy to fix bugs if I've missed anything.\n  Making `CyclotomicField(3)(CyclotomicField(6).0)` still work correctly with this change took some extra coding. I mention this so that whoever is reviewing this patch doesn't think I was changing things at random.\n\nJust for the sake of completeness, let me address all the comments in William's referee report:\n\n1. Changed all the `pyrex`s to `cython`s.\n2. Actually, this doctests are perfectly fine. Notice that (somewhat counter-intuitively for me, as well as you) it's a method on the *element*, not on the *field*. So if `x` is in a quadratic extension, `x._lift_cyclotomic_element(...)` calls specifically that code. \n3. Yep, took those out. I always feel rude removing other people's comments -- after all, if I leave comments in the code, I think it's for a reason. But these are now gone.\n4. This is similar to (2) -- the issue is that in that case, you know both `self.parent()` and `new_parent` are cyclotomic fields of degree 2 over Q, and that an embedding is possible. Actually, I guess you could also have cf3 and cf3, or cf6 and cf6. The code still works in this case, but I've corrected the comment and I'll add the patch after I finish typing this.\n5. Done. I agree, this is cleaner. I didn't read until the end that you thought it should be on a separate ticket, so I'm including it here (since it's already pretty mixed in with this character code). I also added the `integral` flag.\n\nI think that covers it.",
    "created_at": "2008-03-14T08:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2192#issuecomment-14361",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-2192-full.patch](tarball://root/attachments/some-uuid/ticket2192/trac-2192-full.patch) by @craigcitro created at 2008-03-14 08:02:15

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
2. Actually, this doctests are perfectly fine. Notice that (somewhat counter-intuitively for me, as well as you) it's a method on the *element*, not on the *field*. So if `x` is in a quadratic extension, `x._lift_cyclotomic_element(...)` calls specifically that code. 
3. Yep, took those out. I always feel rude removing other people's comments -- after all, if I leave comments in the code, I think it's for a reason. But these are now gone.
4. This is similar to (2) -- the issue is that in that case, you know both `self.parent()` and `new_parent` are cyclotomic fields of degree 2 over Q, and that an embedding is possible. Actually, I guess you could also have cf3 and cf3, or cf6 and cf6. The code still works in this case, but I've corrected the comment and I'll add the patch after I finish typing this.
5. Done. I agree, this is cleaner. I didn't read until the end that you thought it should be on a separate ticket, so I'm including it here (since it's already pretty mixed in with this character code). I also added the `integral` flag.

I think that covers it.



---

archive/issue_comments_014362.json:
```json
{
    "body": "Attachment [trac-2192-touch-up.patch](tarball://root/attachments/some-uuid/ticket2192/trac-2192-touch-up.patch) by @craigcitro created at 2008-03-14 08:03:16\n\napply after trac-2192-full.patch",
    "created_at": "2008-03-14T08:03:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2192#issuecomment-14362",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-2192-touch-up.patch](tarball://root/attachments/some-uuid/ticket2192/trac-2192-touch-up.patch) by @craigcitro created at 2008-03-14 08:03:16

apply after trac-2192-full.patch



---

archive/issue_comments_014363.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-15T07:26:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2192#issuecomment-14363",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014364.json:
```json
{
    "body": "Merged both patches as directed in Sage 2.10.4.alpha0",
    "created_at": "2008-03-15T07:26:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2192#issuecomment-14364",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches as directed in Sage 2.10.4.alpha0



---

archive/issue_events_002358.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-15T07:26:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2192",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2192#event-2358"
}
```
