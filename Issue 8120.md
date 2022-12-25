# Issue 8120: UniqueRepresentation and hash value

archive/issues_008120.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @zimmermann6 @nthiery\n\nThe documentation of `UniqueRepresentation` says \n\n```\n    Similarly, the identity is used as hash function, which is also as\n    fast as it can get. However this means that the hash function may\n    change in between Sage sessions, or even within the same Sage\n    session (see below). Subclasses should overload :meth:`__hash__`\n    if this could be a problem.\n```\n\nBut there is no implementation of `__hash__`.\n\nI'm adding one.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8120\n\n",
    "created_at": "2010-01-29T15:31:33Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "UniqueRepresentation and hash value",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8120",
    "user": "https://github.com/hivert"
}
```
Assignee: @aghitza

CC:  @zimmermann6 @nthiery

The documentation of `UniqueRepresentation` says 

```
    Similarly, the identity is used as hash function, which is also as
    fast as it can get. However this means that the hash function may
    change in between Sage sessions, or even within the same Sage
    session (see below). Subclasses should overload :meth:`__hash__`
    if this could be a problem.
```

But there is no implementation of `__hash__`.

I'm adding one.

Issue created by migration from https://trac.sagemath.org/ticket/8120





---

archive/issue_comments_071251.json:
```json
{
    "body": "Changing assignee from @aghitza to @hivert.",
    "created_at": "2010-01-29T15:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71251",
    "user": "https://github.com/hivert"
}
```

Changing assignee from @aghitza to @hivert.



---

archive/issue_comments_071252.json:
```json
{
    "body": "Changing keywords from \"\" to \"UniqueRepresentation hash\".",
    "created_at": "2010-01-29T15:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71252",
    "user": "https://github.com/hivert"
}
```

Changing keywords from "" to "UniqueRepresentation hash".



---

archive/issue_comments_071253.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-29T15:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71253",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071254.json:
```json
{
    "body": "I just submitted a patch which comply with the documentation. However, since we are in `UniqueRepresentations` we could use `__classcall__` which knows the parameters that constructed the object to insert into the created object the hash value of those parameters in the same veins it insert some stuff needed for pickling/unpickling. Any comment about that ?\n\nFlorent",
    "created_at": "2010-01-29T15:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71254",
    "user": "https://github.com/hivert"
}
```

I just submitted a patch which comply with the documentation. However, since we are in `UniqueRepresentations` we could use `__classcall__` which knows the parameters that constructed the object to insert into the created object the hash value of those parameters in the same veins it insert some stuff needed for pickling/unpickling. Any comment about that ?

Florent



---

archive/issue_comments_071255.json:
```json
{
    "body": "I'd like to review that patch but I'm missing an example to try.\n\nPaul",
    "created_at": "2010-02-06T20:26:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71255",
    "user": "https://github.com/zimmermann6"
}
```

I'd like to review that patch but I'm missing an example to try.

Paul



---

archive/issue_comments_071256.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-07T06:03:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71256",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071257.json:
```json
{
    "body": "Hi Paul,\n\nReplying to [comment:3 zimmerma]:\n> I'd like to review that patch but I'm missing an example to try.\n\nI'm not sure what you want: in the patch you have the following tests example:\n\n```\nsage: class bla(UniqueRepresentation, SageObject): pass \nsage: x = bla(); hx = hash(x) \nsage: x.rename(\"toto\")    \nsage: hx == hash(x) \nTrue \n```\n\nIf you want more elaborated examples using `UniqueRepresentation`, they are dozens of them through sage library (the ultimate goal is that nearly each parent inherits from this). Pick you favorite one (prime.py is a good example see #7397):\n\n```\ntomahawk-*ge-combinat/sage $ grep -l UniqueRepresentation **/*.py\ncategories/category.py\ncategories/enumerated_sets.py\ncategories/examples/commutative_additive_monoids.py\ncategories/examples/commutative_additive_semigroups.py\ncategories/examples/finite_coxeter_groups.py\ncategories/examples/finite_enumerated_sets.py\ncategories/examples/finite_monoids.py\ncategories/examples/finite_semigroups.py\ncategories/examples/finite_weyl_groups.py\ncategories/examples/infinite_enumerated_sets.py\ncategories/examples/monoids.py\ncategories/examples/semigroups.py\ncategories/examples/sets_cat.py\ncategories/primer.py\ncategories/semigroups.py\ncategories/sets_cat.py\ncombinat/crystals/affine.py\ncombinat/crystals/letters.py\ncombinat/free_module.py\ncombinat/root_system/cartan_type.py\ncombinat/root_system/root_system.py\ncombinat/root_system/type_dual.py\ncombinat/root_system/type_relabel.py\ncombinat/root_system/weyl_group.py\ncombinat/sf/sf.py\ngroups/matrix_gps/general_linear.py\ngroups/matrix_gps/special_linear.py\ngroups/perm_gps/permgroup_named.py\nmisc/classcall_metaclass.py\nmisc/constant_function.py\nmisc/nested_class_test.py\nsets/disjoint_union_enumerated_sets.py\nsets/finite_enumerated_set.py\nsets/non_negative_integers.py\nsets/primes.py\nstructure/all.py\nstructure/dynamic_class.py\nstructure/unique_representation.py\n```\n",
    "created_at": "2010-02-07T09:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71257",
    "user": "https://github.com/hivert"
}
```

Hi Paul,

Replying to [comment:3 zimmerma]:
> I'd like to review that patch but I'm missing an example to try.

I'm not sure what you want: in the patch you have the following tests example:

```
sage: class bla(UniqueRepresentation, SageObject): pass 
sage: x = bla(); hx = hash(x) 
sage: x.rename("toto")    
sage: hx == hash(x) 
True 
```

If you want more elaborated examples using `UniqueRepresentation`, they are dozens of them through sage library (the ultimate goal is that nearly each parent inherits from this). Pick you favorite one (prime.py is a good example see #7397):

```
tomahawk-*ge-combinat/sage $ grep -l UniqueRepresentation **/*.py
categories/category.py
categories/enumerated_sets.py
categories/examples/commutative_additive_monoids.py
categories/examples/commutative_additive_semigroups.py
categories/examples/finite_coxeter_groups.py
categories/examples/finite_enumerated_sets.py
categories/examples/finite_monoids.py
categories/examples/finite_semigroups.py
categories/examples/finite_weyl_groups.py
categories/examples/infinite_enumerated_sets.py
categories/examples/monoids.py
categories/examples/semigroups.py
categories/examples/sets_cat.py
categories/primer.py
categories/semigroups.py
categories/sets_cat.py
combinat/crystals/affine.py
combinat/crystals/letters.py
combinat/free_module.py
combinat/root_system/cartan_type.py
combinat/root_system/root_system.py
combinat/root_system/type_dual.py
combinat/root_system/type_relabel.py
combinat/root_system/weyl_group.py
combinat/sf/sf.py
groups/matrix_gps/general_linear.py
groups/matrix_gps/special_linear.py
groups/perm_gps/permgroup_named.py
misc/classcall_metaclass.py
misc/constant_function.py
misc/nested_class_test.py
sets/disjoint_union_enumerated_sets.py
sets/finite_enumerated_set.py
sets/non_negative_integers.py
sets/primes.py
structure/all.py
structure/dynamic_class.py
structure/unique_representation.py
```




---

archive/issue_comments_071258.json:
```json
{
    "body": "I tried the patch and sage -t * and got the same failures that I get without the patch\n(on x86_64 Fedora12, see #7773). Thus a positive review for me.",
    "created_at": "2010-02-08T11:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71258",
    "user": "https://github.com/zimmermann6"
}
```

I tried the patch and sage -t * and got the same failures that I get without the patch
(on x86_64 Fedora12, see #7773). Thus a positive review for me.



---

archive/issue_comments_071259.json:
```json
{
    "body": "Replying to [comment:6 zimmerma]:\n> I tried the patch and sage -t * and got the same failures that I get without the patch\n> (on x86_64 Fedora12, see #7773). Thus a positive review for me.\n\nSo are you waiting for another review ? Or did you simply forgot to check the relevant box ?",
    "created_at": "2010-02-08T12:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71259",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:6 zimmerma]:
> I tried the patch and sage -t * and got the same failures that I get without the patch
> (on x86_64 Fedora12, see #7773). Thus a positive review for me.

So are you waiting for another review ? Or did you simply forgot to check the relevant box ?



---

archive/issue_comments_071260.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-08T12:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71260",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071261.json:
```json
{
    "body": "> So are you waiting for another review ?\n\nno, I was waiting for the \"needs review\" status.",
    "created_at": "2010-02-08T12:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71261",
    "user": "https://github.com/zimmermann6"
}
```

> So are you waiting for another review ?

no, I was waiting for the "needs review" status.



---

archive/issue_comments_071262.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-08T12:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71262",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071263.json:
```json
{
    "body": "Remove assignee @hivert.",
    "created_at": "2010-02-08T13:34:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71263",
    "user": "https://github.com/nthiery"
}
```

Remove assignee @hivert.



---

archive/issue_comments_071264.json:
```json
{
    "body": "Just one thing Florent: please fix the following doctest:\n\n```\nsage: hash(x) # random \nTrue\n```\n\nso that the reader expects some integer result.\n\nMaybe some test like:\n\n```\nsage: type(hash(x))\nint\n```\n\ncould be added.",
    "created_at": "2010-02-08T13:34:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71264",
    "user": "https://github.com/nthiery"
}
```

Just one thing Florent: please fix the following doctest:

```
sage: hash(x) # random 
True
```

so that the reader expects some integer result.

Maybe some test like:

```
sage: type(hash(x))
int
```

could be added.



---

archive/issue_comments_071265.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-02-08T16:16:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71265",
    "user": "https://github.com/hivert"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_071266.json:
```json
{
    "body": "Replying to [comment:9 nthiery]:\n> \n> Just one thing Florent: please fix the following doctest:\n> {{{\n> sage: hash(x) # random \n> True\n> }}}\n> so that the reader expects some integer result.\n> \n> Maybe some test like:\n> {{{\n> sage: type(hash(x))\n> int\n> }}}\n> could be added.\n\nOups !!! I'm resubmitting a patch with the following diff:\n\n```\ndiff --git a/sage/structure/unique_representation.py b/sage/structure/unique_represent\nation.py\n--- a/sage/structure/unique_representation.py\n+++ b/sage/structure/unique_representation.py\n@@ -483,7 +483,9 @@ class UniqueRepresentation:\n             sage: x = UniqueRepresentation()\n             sage: y = UniqueRepresentation()\n             sage: hash(x) # random\n-            True\n+            74153040\n+            sage: type(hash(x))\n+            <type 'int'>\n             sage: hash(x) == hash(y)\n             True\n             sage: class bla(UniqueRepresentation, SageObject): pass\n```\n\n\nPlease re-review...\n\nFlorent",
    "created_at": "2010-02-08T16:16:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71266",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:9 nthiery]:
> 
> Just one thing Florent: please fix the following doctest:
> {{{
> sage: hash(x) # random 
> True
> }}}
> so that the reader expects some integer result.
> 
> Maybe some test like:
> {{{
> sage: type(hash(x))
> int
> }}}
> could be added.

Oups !!! I'm resubmitting a patch with the following diff:

```
diff --git a/sage/structure/unique_representation.py b/sage/structure/unique_represent
ation.py
--- a/sage/structure/unique_representation.py
+++ b/sage/structure/unique_representation.py
@@ -483,7 +483,9 @@ class UniqueRepresentation:
             sage: x = UniqueRepresentation()
             sage: y = UniqueRepresentation()
             sage: hash(x) # random
-            True
+            74153040
+            sage: type(hash(x))
+            <type 'int'>
             sage: hash(x) == hash(y)
             True
             sage: class bla(UniqueRepresentation, SageObject): pass
```


Please re-review...

Florent



---

archive/issue_comments_071267.json:
```json
{
    "body": "Attachment [trac_8120-uniquerep_hash-fh.patch](tarball://root/attachments/some-uuid/ticket8120/trac_8120-uniquerep_hash-fh.patch) by @hivert created at 2010-02-08 16:18:18",
    "created_at": "2010-02-08T16:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71267",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8120-uniquerep_hash-fh.patch](tarball://root/attachments/some-uuid/ticket8120/trac_8120-uniquerep_hash-fh.patch) by @hivert created at 2010-02-08 16:18:18



---

archive/issue_comments_071268.json:
```json
{
    "body": "> Please re-review... \n\nwill do it as soon as my current sage -t * finishes. In the meantime you can click on\n\"needs review\", unless more work is needed.",
    "created_at": "2010-02-08T16:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71268",
    "user": "https://github.com/zimmermann6"
}
```

> Please re-review... 

will do it as soon as my current sage -t * finishes. In the meantime you can click on
"needs review", unless more work is needed.



---

archive/issue_comments_071269.json:
```json
{
    "body": "Replying to [comment:11 zimmerma]:\n> > Please re-review... \n> \n> will do it as soon as my current sage -t * finishes. In the meantime you can click on\n> \"needs review\", unless more work is needed.\n\nActually, the precise button I needed to hit was \"Submit Changes\" ;-)",
    "created_at": "2010-02-08T16:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71269",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:11 zimmerma]:
> > Please re-review... 
> 
> will do it as soon as my current sage -t * finishes. In the meantime you can click on
> "needs review", unless more work is needed.

Actually, the precise button I needed to hit was "Submit Changes" ;-)



---

archive/issue_comments_071270.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-08T16:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71270",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071271.json:
```json
{
    "body": "Nicolas (and also Paul), you didn't comment about the following thought:\n\nHowever, since we are in `UniqueRepresentations` we could use `__classcall__` which knows the parameters that constructed the object to insert into the created object the hash value of those parameters in the same veins it insert some stuff needed for pickling/unpickling. Any comment about that ?\n\nAnyway, whatever is decided, I suggest to keep it for a forthcomming ticket, since it can raise some backward compatibility issues...",
    "created_at": "2010-02-08T16:35:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71271",
    "user": "https://github.com/hivert"
}
```

Nicolas (and also Paul), you didn't comment about the following thought:

However, since we are in `UniqueRepresentations` we could use `__classcall__` which knows the parameters that constructed the object to insert into the created object the hash value of those parameters in the same veins it insert some stuff needed for pickling/unpickling. Any comment about that ?

Anyway, whatever is decided, I suggest to keep it for a forthcomming ticket, since it can raise some backward compatibility issues...



---

archive/issue_comments_071272.json:
```json
{
    "body": "Replying to [comment:13 hivert]:\n> Nicolas (and also Paul), you didn't comment about the following thought:\n> \n> However, since we are in `UniqueRepresentations` we could use `__classcall__` which knows the parameters that constructed the object to insert into the created object the hash value of those parameters in the same veins it insert some stuff needed for pickling/unpickling. Any comment about that ?\n\nThat sounds good. We should probably include the class of the object in the hash calculation.\n\n> Anyway, whatever is decided, I suggest to keep it for a forthcomming ticket, since it can raise some backward compatibility issues...\n\nYup.",
    "created_at": "2010-02-08T16:49:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71272",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:13 hivert]:
> Nicolas (and also Paul), you didn't comment about the following thought:
> 
> However, since we are in `UniqueRepresentations` we could use `__classcall__` which knows the parameters that constructed the object to insert into the created object the hash value of those parameters in the same veins it insert some stuff needed for pickling/unpickling. Any comment about that ?

That sounds good. We should probably include the class of the object in the hash calculation.

> Anyway, whatever is decided, I suggest to keep it for a forthcomming ticket, since it can raise some backward compatibility issues...

Yup.



---

archive/issue_comments_071273.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-09T07:09:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71273",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071274.json:
```json
{
    "body": "I did try with the new patch, and it is ok. Thus a positive review.",
    "created_at": "2010-02-09T07:09:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71274",
    "user": "https://github.com/zimmermann6"
}
```

I did try with the new patch, and it is ok. Thus a positive review.



---

archive/issue_comments_071275.json:
```json
{
    "body": "The ticket number is missing from the commit string.  I've refreshed the patch I've applied to 4.3.3.alpha0.",
    "created_at": "2010-02-10T14:24:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71275",
    "user": "https://github.com/qed777"
}
```

The ticket number is missing from the commit string.  I've refreshed the patch I've applied to 4.3.3.alpha0.



---

archive/issue_comments_071276.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:48:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71276",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_008328.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-02-11T14:48:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8120#event-8328"
}
```



---

archive/issue_comments_071277.json:
```json
{
    "body": "Oops!",
    "created_at": "2010-02-11T15:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8120#issuecomment-71277",
    "user": "https://github.com/qed777"
}
```

Oops!
