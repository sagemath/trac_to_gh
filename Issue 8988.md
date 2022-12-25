# Issue 8988: Add support for toric varieties

archive/issues_008988.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @vbraun @loefflerd\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8988\n\n",
    "created_at": "2010-05-18T09:07:51Z",
    "labels": [
        "component: algebraic geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Add support for toric varieties",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8988",
    "user": "https://github.com/novoselt"
}
```
Assignee: @aghitza

CC:  @vbraun @loefflerd



Issue created by migration from https://trac.sagemath.org/ticket/8988





---

archive/issue_comments_082885.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-18T09:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82885",
    "user": "https://github.com/novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082886.json:
```json
{
    "body": "I have marked this ticket as \"needs review\" despite of the broken doctest. Since that doctest seems to be unrelated, please review the ticket and state your opinion independently of it, without actually switching to \"positive review\". If nobody objects, I will shortly post a patch changing that doctest to the new output. As I understand, the purpose of that function is to actually try to \"create some mess\" and so there is no any meaning in a particular output.",
    "created_at": "2010-05-18T10:04:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82886",
    "user": "https://github.com/novoselt"
}
```

I have marked this ticket as "needs review" despite of the broken doctest. Since that doctest seems to be unrelated, please review the ticket and state your opinion independently of it, without actually switching to "positive review". If nobody objects, I will shortly post a patch changing that doctest to the new output. As I understand, the purpose of that function is to actually try to "create some mess" and so there is no any meaning in a particular output.



---

archive/issue_comments_082887.json:
```json
{
    "body": "Attachment [trac_8988_add_support_for_toric_varieties.2.patch](tarball://root/attachments/some-uuid/ticket8988/trac_8988_add_support_for_toric_varieties.2.patch) by @novoselt created at 2010-05-19 03:50:39\n\nOops, forgot to click replace existing file. Only the second patch should be applied. I have added a more formal reference to \"Toric Varieties\" book (and I checked with David Cox that it is OK to put a link to the draft). I have also moved the `kaehler_cone` function from Fano toric varieties to this patch.",
    "created_at": "2010-05-19T03:50:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82887",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_8988_add_support_for_toric_varieties.2.patch](tarball://root/attachments/some-uuid/ticket8988/trac_8988_add_support_for_toric_varieties.2.patch) by @novoselt created at 2010-05-19 03:50:39

Oops, forgot to click replace existing file. Only the second patch should be applied. I have added a more formal reference to "Toric Varieties" book (and I checked with David Cox that it is OK to put a link to the draft). I have also moved the `kaehler_cone` function from Fano toric varieties to this patch.



---

archive/issue_comments_082888.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-21T03:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82888",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082889.json:
```json
{
    "body": "I will make some adjustments to modules on which this patch depends, which may cause some changes in this patch as well. See\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/17743e17d67838ae",
    "created_at": "2010-05-21T03:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82889",
    "user": "https://github.com/novoselt"
}
```

I will make some adjustments to modules on which this patch depends, which may cause some changes in this patch as well. See
http://groups.google.com/group/sage-devel/browse_thread/thread/17743e17d67838ae



---

archive/issue_comments_082890.json:
```json
{
    "body": "A couple little changes to account for changes in previous patches. Plus the fix for the broken doctest in symbolic.",
    "created_at": "2010-05-29T03:53:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82890",
    "user": "https://github.com/novoselt"
}
```

A couple little changes to account for changes in previous patches. Plus the fix for the broken doctest in symbolic.



---

archive/issue_comments_082891.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-29T19:25:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82891",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082892.json:
```json
{
    "body": "Fixed errors caused previously by the code of `affine_patch` of subschemes and removed `NotImplementedError` from the beginning of this function.",
    "created_at": "2010-06-03T03:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82892",
    "user": "https://github.com/novoselt"
}
```

Fixed errors caused previously by the code of `affine_patch` of subschemes and removed `NotImplementedError` from the beginning of this function.



---

archive/issue_comments_082893.json:
```json
{
    "body": "I think the change in the random_test is because the patched sage/schemes/generic/algebraic_scheme now imports latex which imports random which changes the random seed. So it is all right, and fixing the random_test doctest is the right thing to do (TM).",
    "created_at": "2010-06-03T18:46:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82893",
    "user": "https://github.com/vbraun"
}
```

I think the change in the random_test is because the patched sage/schemes/generic/algebraic_scheme now imports latex which imports random which changes the random seed. So it is all right, and fixing the random_test doctest is the right thing to do (TM).



---

archive/issue_comments_082894.json:
```json
{
    "body": "I've read through the code and it looks good. \n\nOne minor issue is that the `_repr_()` is not very descriptive. For example\n\n```\nsage: p0 = P1xP1.affine_patch(0)\nsage: p0\nToric variety of dimension 2\nsage: p0.embedding_morphism()\nScheme morphism:\n  From: Toric variety of dimension 2\n  To:   Toric variety of dimension 2\n  Defn: Defined on coordinates by sending [z0 : z3] to\n        [z0 : 1 : 1 : z3]\n```\n\nMaybe we could return `Toric variety (dim=2, #cones=4)` or so and include the number of generating cones to be able to distinguish the different varieties.\n\nApart from that I'd be happy to review it positively once the rewritten `Fan` is incorporated!",
    "created_at": "2010-06-13T21:38:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82894",
    "user": "https://github.com/vbraun"
}
```

I've read through the code and it looks good. 

One minor issue is that the `_repr_()` is not very descriptive. For example

```
sage: p0 = P1xP1.affine_patch(0)
sage: p0
Toric variety of dimension 2
sage: p0.embedding_morphism()
Scheme morphism:
  From: Toric variety of dimension 2
  To:   Toric variety of dimension 2
  Defn: Defined on coordinates by sending [z0 : z3] to
        [z0 : 1 : 1 : z3]
```

Maybe we could return `Toric variety (dim=2, #cones=4)` or so and include the number of generating cones to be able to distinguish the different varieties.

Apart from that I'd be happy to review it positively once the rewritten `Fan` is incorporated!



---

archive/issue_comments_082895.json:
```json
{
    "body": "How about this?\n\n```\nToric variety of dimension 2 with 4 affine patches\n```\n\nI would like to have a description in \"plain English\" and also patches seem to be more intrinsic to varieties than cones.\n\nIt may be good also to add an option for \"extra\" name, so that varieties from a named database (which is not there yet but I hope to have it eventually based on your code) can print as \n\n```\nToric variety of dimension 2 with 4 affine patches (P1xP1)\n```\n\nor maybe\n\n```\nP1xP1 (Toric variety of dimension 2 with 4 affine patches)\n```\n\nwill be better. There is a way to rename anything in Sage, so\n\n```\nP1xP1\n```\n\nis very easy to do, but seems to be too different from the default one. Which one of three do you prefer?\n\nIt is also possible to print the base field, but I deliberately didn't do it so far because I always think of toric varieties as being defined over complex field. Plus, when the base field is a fraction field of a multivariable polynomial ring (as is the case with ambient spaces of anticanonical hypersurfaces in the next patch), the the description of the field gets really big and distracts from the toric variety itself.",
    "created_at": "2010-06-13T21:58:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82895",
    "user": "https://github.com/novoselt"
}
```

How about this?

```
Toric variety of dimension 2 with 4 affine patches
```

I would like to have a description in "plain English" and also patches seem to be more intrinsic to varieties than cones.

It may be good also to add an option for "extra" name, so that varieties from a named database (which is not there yet but I hope to have it eventually based on your code) can print as 

```
Toric variety of dimension 2 with 4 affine patches (P1xP1)
```

or maybe

```
P1xP1 (Toric variety of dimension 2 with 4 affine patches)
```

will be better. There is a way to rename anything in Sage, so

```
P1xP1
```

is very easy to do, but seems to be too different from the default one. Which one of three do you prefer?

It is also possible to print the base field, but I deliberately didn't do it so far because I always think of toric varieties as being defined over complex field. Plus, when the base field is a fraction field of a multivariable polynomial ring (as is the case with ambient spaces of anticanonical hypersurfaces in the next patch), the the description of the field gets really big and distracts from the toric variety itself.



---

archive/issue_comments_082896.json:
```json
{
    "body": "And in your example the first variety should probably print as\n\n```\nAffine toric variety of dimension 2\n```\n",
    "created_at": "2010-06-13T21:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82896",
    "user": "https://github.com/novoselt"
}
```

And in your example the first variety should probably print as

```
Affine toric variety of dimension 2
```




---

archive/issue_comments_082897.json:
```json
{
    "body": "Since there you can cover any given space always with more patches I'm a bit hesitant; The notation `Toric variety of dimension 2 with 4 affine patches` only makes sense once you translate it back into toric geometry. But plain English is definitely preferable.\n\nI agree that the base field shouldn't be printed. Usually, it is going to be the same for all varieties the user constructs, so it is not a differentiating feature.",
    "created_at": "2010-06-14T00:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82897",
    "user": "https://github.com/vbraun"
}
```

Since there you can cover any given space always with more patches I'm a bit hesitant; The notation `Toric variety of dimension 2 with 4 affine patches` only makes sense once you translate it back into toric geometry. But plain English is definitely preferable.

I agree that the base field shouldn't be printed. Usually, it is going to be the same for all varieties the user constructs, so it is not a differentiating feature.



---

archive/issue_comments_082898.json:
```json
{
    "body": "I agree... How about \"Toric variety of dimension 2 covered by 4 affine patches\"? Such a description a little more clearly refers to some particular cover, rather than arbitrary affine patches, and we do have a \"canonical\" one, returned by method `affine_patch(i)`.",
    "created_at": "2010-06-14T00:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82898",
    "user": "https://github.com/novoselt"
}
```

I agree... How about "Toric variety of dimension 2 covered by 4 affine patches"? Such a description a little more clearly refers to some particular cover, rather than arbitrary affine patches, and we do have a "canonical" one, returned by method `affine_patch(i)`.



---

archive/issue_comments_082899.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-17T06:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82899",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082900.json:
```json
{
    "body": "In the spirit of planned changes to cones and fans I propose printing toric varieties as\n\n```\n2-d toric variety covered by 4 affine patches\n```\n\nand\n\n```\n2-d affine toric variety\n```\n\nfor those generated by a single cone.",
    "created_at": "2010-06-17T06:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82900",
    "user": "https://github.com/novoselt"
}
```

In the spirit of planned changes to cones and fans I propose printing toric varieties as

```
2-d toric variety covered by 4 affine patches
```

and

```
2-d affine toric variety
```

for those generated by a single cone.



---

archive/issue_comments_082901.json:
```json
{
    "body": "I've started a discussion\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/763d9ac5634bf8f3\nas `symbolic/random_tests.py` gives now more grief (I am using 4.4.4.alpha0). Meanwhile I will update the doctest patch with new output...\n\nToric varieties are pretty much unchanged except for renaming fan-related functions and changing the representation.",
    "created_at": "2010-06-17T20:56:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82901",
    "user": "https://github.com/novoselt"
}
```

I've started a discussion
http://groups.google.com/group/sage-devel/browse_thread/thread/763d9ac5634bf8f3
as `symbolic/random_tests.py` gives now more grief (I am using 4.4.4.alpha0). Meanwhile I will update the doctest patch with new output...

Toric varieties are pretty much unchanged except for renaming fan-related functions and changing the representation.



---

archive/issue_comments_082902.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-17T20:56:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82902",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082903.json:
```json
{
    "body": "Apply after the main patch. Broken doctests are fixed by setting random seed.",
    "created_at": "2010-06-17T22:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82903",
    "user": "https://github.com/novoselt"
}
```

Apply after the main patch. Broken doctests are fixed by setting random seed.



---

archive/issue_comments_082904.json:
```json
{
    "body": "Attachment [trac_8988_doctest_fix_for_symbolic_random_tests.patch](tarball://root/attachments/some-uuid/ticket8988/trac_8988_doctest_fix_for_symbolic_random_tests.patch) by @vbraun created at 2010-06-21 16:42:23\n\nLooks good now. One final nitpick is that the Kaehler cone lives in some `ToricLattice` which is somewhat confusing. I propose a `ToricVariety_field.Pic()` method returning a suitable lattice for the Kahler cone to live in. For now thats just `ZZ^k` but in the future we could be more fancy. Also, rename `kaehler_cone` -> `Kaehler_cone` since it is a name. Patch is attached, let me know what you think.",
    "created_at": "2010-06-21T16:42:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82904",
    "user": "https://github.com/vbraun"
}
```

Attachment [trac_8988_doctest_fix_for_symbolic_random_tests.patch](tarball://root/attachments/some-uuid/ticket8988/trac_8988_doctest_fix_for_symbolic_random_tests.patch) by @vbraun created at 2010-06-21 16:42:23

Looks good now. One final nitpick is that the Kaehler cone lives in some `ToricLattice` which is somewhat confusing. I propose a `ToricVariety_field.Pic()` method returning a suitable lattice for the Kahler cone to live in. For now thats just `ZZ^k` but in the future we could be more fancy. Also, rename `kaehler_cone` -> `Kaehler_cone` since it is a name. Patch is attached, let me know what you think.



---

archive/issue_comments_082905.json:
```json
{
    "body": "In the singular case the `Kaehler_cone` method actually computes the cone in the rational (Weyl) divisor class group = `A_{n-1}(X) \\otimes_\\ZZ \\QQ`, and not in the Picard group. The updated patch changes the names accordingly.",
    "created_at": "2010-06-22T19:50:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82905",
    "user": "https://github.com/vbraun"
}
```

In the singular case the `Kaehler_cone` method actually computes the cone in the rational (Weyl) divisor class group = `A_{n-1}(X) \otimes_\ZZ \QQ`, and not in the Picard group. The updated patch changes the names accordingly.



---

archive/issue_comments_082906.json:
```json
{
    "body": "Another thought: It would be nice if `ToricVariety_field.fan()` would take an optional argument and pass it on to the fan so one could write\n\n```\nX = ToricVariety(...)\nX.fan(dim=1)\n```\n\ninstead of\n\n```\nX.fan()(dim=1)\n```\n",
    "created_at": "2010-06-23T14:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82906",
    "user": "https://github.com/vbraun"
}
```

Another thought: It would be nice if `ToricVariety_field.fan()` would take an optional argument and pass it on to the fan so one could write

```
X = ToricVariety(...)
X.fan(dim=1)
```

instead of

```
X.fan()(dim=1)
```




---

archive/issue_comments_082907.json:
```json
{
    "body": "Neat idea! Will do in a few days ;-)",
    "created_at": "2010-06-23T16:50:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82907",
    "user": "https://github.com/novoselt"
}
```

Neat idea! Will do in a few days ;-)



---

archive/issue_comments_082908.json:
```json
{
    "body": "Yet another minor note: we might want to rename `ToricVariety.is_complete` to `ToricVariety.is_compact`. Not a big deal, but probably the better term in that context.",
    "created_at": "2010-06-23T17:28:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82908",
    "user": "https://github.com/vbraun"
}
```

Yet another minor note: we might want to rename `ToricVariety.is_complete` to `ToricVariety.is_compact`. Not a big deal, but probably the better term in that context.



---

archive/issue_comments_082909.json:
```json
{
    "body": "I think I used `is_complete` since compact does not quite make sense for arbitrary fields.\n\nRegarding Kaehler cone - maybe the best option for now is just to remove it until divisors are actually implemented? The reason why it is here now is that I had to compute it for several varieties, so I wrote a quick function based on existing code without worrying too much about how well does it fit into the current picture. It seems that not very well...",
    "created_at": "2010-06-23T18:23:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82909",
    "user": "https://github.com/novoselt"
}
```

I think I used `is_complete` since compact does not quite make sense for arbitrary fields.

Regarding Kaehler cone - maybe the best option for now is just to remove it until divisors are actually implemented? The reason why it is here now is that I had to compute it for several varieties, so I wrote a quick function based on existing code without worrying too much about how well does it fit into the current picture. It seems that not very well...



---

archive/issue_comments_082910.json:
```json
{
    "body": "I think we can't do much better for `Kaehler_cone`. I'll send a patch for divisors soon, maybe that'll help to make a more informed decision. In the meantime, here is a   patch with documentation fixes.",
    "created_at": "2010-06-24T10:32:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82910",
    "user": "https://github.com/vbraun"
}
```

I think we can't do much better for `Kaehler_cone`. I'll send a patch for divisors soon, maybe that'll help to make a more informed decision. In the meantime, here is a   patch with documentation fixes.



---

archive/issue_comments_082911.json:
```json
{
    "body": "Added a Mori_vectors() method while I'm at it.",
    "created_at": "2010-06-25T15:18:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82911",
    "user": "https://github.com/vbraun"
}
```

Added a Mori_vectors() method while I'm at it.



---

archive/issue_comments_082912.json:
```json
{
    "body": "Attachment [trac_8988_Kahlercone_lattice.patch](tarball://root/attachments/some-uuid/ticket8988/trac_8988_Kahlercone_lattice.patch) by @novoselt created at 2010-06-29 04:44:27\n\nAdded parameters to `fan` method and changed the behaviour of `__call__` for fans in the case of no parameters at all - it seems more natural to return the fan in this case rather than all cones of all dimensions (which is what `cones` does).",
    "created_at": "2010-06-29T04:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82912",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_8988_Kahlercone_lattice.patch](tarball://root/attachments/some-uuid/ticket8988/trac_8988_Kahlercone_lattice.patch) by @novoselt created at 2010-06-29 04:44:27

Added parameters to `fan` method and changed the behaviour of `__call__` for fans in the case of no parameters at all - it seems more natural to return the fan in this case rather than all cones of all dimensions (which is what `cones` does).



---

archive/issue_comments_082913.json:
```json
{
    "body": "Attachment [trac_8988_add_support_for_toric_varieties.patch](tarball://root/attachments/some-uuid/ticket8988/trac_8988_add_support_for_toric_varieties.patch) by @novoselt created at 2010-06-29 05:46:41\n\nApply this patch and doctest fix.",
    "created_at": "2010-06-29T05:46:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82913",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_8988_add_support_for_toric_varieties.patch](tarball://root/attachments/some-uuid/ticket8988/trac_8988_add_support_for_toric_varieties.patch) by @novoselt created at 2010-06-29 05:46:41

Apply this patch and doctest fix.



---

archive/issue_comments_082914.json:
```json
{
    "body": "Attachment [trac_8988_Kaehler_Mori_cones.patch](tarball://root/attachments/some-uuid/ticket8988/trac_8988_Kaehler_Mori_cones.patch) by @novoselt created at 2010-06-29 05:48:50\n\nCode to be included later.",
    "created_at": "2010-06-29T05:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82914",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_8988_Kaehler_Mori_cones.patch](tarball://root/attachments/some-uuid/ticket8988/trac_8988_Kaehler_Mori_cones.patch) by @novoselt created at 2010-06-29 05:48:50

Code to be included later.



---

archive/issue_comments_082915.json:
```json
{
    "body": "Hi Volker,\n\nI have done some work on the documentation from your patch and got completely stuck at `Mori_vectors`. Problems from smaller to bigger ones:\n\n* Are we allowed to use non-standard characters? I mean \"a with dots\" in Kaehler. I vaguely remember some discussion about it, but don't recall the result. Personally I prefer to use only characters that are easy to type and display for everyone. It does mean that some names are not accurately represented, but having one of such names I can vote in favour of it ;-) \n\n* Your doctest uses toric varieties library which depends on this patch. It is a good non-trivial doctest, so I have no desire to remove it.\n\n* Why does it return vectors rather than cone (in the same way as `Kaehler_cone`)?\n\n* Kaehler and Mori cones are supposed to be dual, but they are not. Because Kaehler cone is given in some coordinates on the class group and Mori cone is given embedded into a higher dimensional space without a choice of a basis for its \"real space\". Both representations are probably useful and should be available, but it should be done consistently.\n\nSo:\n\n* I have removed my `kaehler_cone` method from the main patch, hopefully now you can give it a positive review together with symbolic doctest fixes only.\n\n* I have uploaded a new patch which contains your rebased changes and my edits to the documentation. It should NOT be applied here, I just wanted to save this code. As a patch it now just contains three new functions and can be easily moved to other tickets, where the library of toric varieties will be available to use in doctests. We will also need to take care of the last two points above.\n\nLet me know what you think of all this.\n\nAndrey",
    "created_at": "2010-06-29T06:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82915",
    "user": "https://github.com/novoselt"
}
```

Hi Volker,

I have done some work on the documentation from your patch and got completely stuck at `Mori_vectors`. Problems from smaller to bigger ones:

* Are we allowed to use non-standard characters? I mean "a with dots" in Kaehler. I vaguely remember some discussion about it, but don't recall the result. Personally I prefer to use only characters that are easy to type and display for everyone. It does mean that some names are not accurately represented, but having one of such names I can vote in favour of it ;-) 

* Your doctest uses toric varieties library which depends on this patch. It is a good non-trivial doctest, so I have no desire to remove it.

* Why does it return vectors rather than cone (in the same way as `Kaehler_cone`)?

* Kaehler and Mori cones are supposed to be dual, but they are not. Because Kaehler cone is given in some coordinates on the class group and Mori cone is given embedded into a higher dimensional space without a choice of a basis for its "real space". Both representations are probably useful and should be available, but it should be done consistently.

So:

* I have removed my `kaehler_cone` method from the main patch, hopefully now you can give it a positive review together with symbolic doctest fixes only.

* I have uploaded a new patch which contains your rebased changes and my edits to the documentation. It should NOT be applied here, I just wanted to save this code. As a patch it now just contains three new functions and can be easily moved to other tickets, where the library of toric varieties will be available to use in doctests. We will also need to take care of the last two points above.

Let me know what you think of all this.

Andrey



---

archive/issue_comments_082916.json:
```json
{
    "body": "* I searched the sage-devel group but did not find any discussion. I think unicode docstrings are fine, but should be marked as `u\"\"\"documentation\"\"\"` which I did not do. Method names are and should be 7bit only.\n  * For those than can't dualize the Kaehler cone manually I envision a `Mori_cone` method. Note that the `Mori_vectors` are (nrays+1)-component vectors, so this will never match the Kaehler cone. If you think that thats too confusing it could be renamed to `GLsM_charge_vectors()`, for example.\n  * So shall we agree that Kahler/Mori cones should live in `QQ^nrays`? The advantage is that there is a canonical basis given by the rays, as you said.",
    "created_at": "2010-06-29T13:20:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82916",
    "user": "https://github.com/vbraun"
}
```

* I searched the sage-devel group but did not find any discussion. I think unicode docstrings are fine, but should be marked as `u"""documentation"""` which I did not do. Method names are and should be 7bit only.
  * For those than can't dualize the Kaehler cone manually I envision a `Mori_cone` method. Note that the `Mori_vectors` are (nrays+1)-component vectors, so this will never match the Kaehler cone. If you think that thats too confusing it could be renamed to `GLsM_charge_vectors()`, for example.
  * So shall we agree that Kahler/Mori cones should live in `QQ^nrays`? The advantage is that there is a canonical basis given by the rays, as you said.



---

archive/issue_comments_082917.json:
```json
{
    "body": "I think (strongly ;-)) that `Kaehler_cone` method should return a cone in the class group in some basis, since such cones with some additions form a complete fan of the GKZ decomposition.\n\nWe should, however, have a clear way of going from divisors associated to rays to this basis and, perhaps, a way to go back. The first is easy, the i-th ray is represented by the i-th column of the Gale transform matrix. However, it may not be obvious and does not feel natural, since one has to involve functions of the fan, rather than toric variety directly.\n\nFor `Mori_cone` I would prefer to get the \"traditional dual\" of the `Kaehler_cone`, i.e. just the cone formed by facet normals, because it is confusing otherwise.\n\nAgain, there should be a clean way to go from any vector in the ambient space of `Mori_cone` to the longer vector with clear interpretation of each entry. I am OK with having a special function for the generators of the Mori cone and your proposed name is fine (although I have always seen this abbreviation as GLSM and would prefer all-capital version).\n\n**Regarding this ticket**, my main point is that these functions require some more work and since they operate with divisors, perhaps we can move them to the ticket implementing divisors? Or, in order to avoid adding more stuff there and therefore potentially delaying it, I can create a new ticket for implementing all of the above (including, finally, `cone.dual` to make `Mori_cone` trivial).",
    "created_at": "2010-06-29T14:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82917",
    "user": "https://github.com/novoselt"
}
```

I think (strongly ;-)) that `Kaehler_cone` method should return a cone in the class group in some basis, since such cones with some additions form a complete fan of the GKZ decomposition.

We should, however, have a clear way of going from divisors associated to rays to this basis and, perhaps, a way to go back. The first is easy, the i-th ray is represented by the i-th column of the Gale transform matrix. However, it may not be obvious and does not feel natural, since one has to involve functions of the fan, rather than toric variety directly.

For `Mori_cone` I would prefer to get the "traditional dual" of the `Kaehler_cone`, i.e. just the cone formed by facet normals, because it is confusing otherwise.

Again, there should be a clean way to go from any vector in the ambient space of `Mori_cone` to the longer vector with clear interpretation of each entry. I am OK with having a special function for the generators of the Mori cone and your proposed name is fine (although I have always seen this abbreviation as GLSM and would prefer all-capital version).

**Regarding this ticket**, my main point is that these functions require some more work and since they operate with divisors, perhaps we can move them to the ticket implementing divisors? Or, in order to avoid adding more stuff there and therefore potentially delaying it, I can create a new ticket for implementing all of the above (including, finally, `cone.dual` to make `Mori_cone` trivial).



---

archive/issue_comments_082918.json:
```json
{
    "body": "In #9337 I did implement a `divisor.rational_class()` method that returns what you want. But there is no canonical way to go from divisor class -> divisor, so the computation of Kahler cones does not depend on the implementation of toric divisors.\n\nI agree that `Mori_cone()` should return just `Kahler_cone().dual()` and we can implement that later.\n\nGLSM is fine with me, too.\n\nIf you want to split off the Kahler cone computation from this ticket then thats fine with me. But we should then make it an independent ticket and not lump into toric divisors.",
    "created_at": "2010-06-29T15:05:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82918",
    "user": "https://github.com/vbraun"
}
```

In #9337 I did implement a `divisor.rational_class()` method that returns what you want. But there is no canonical way to go from divisor class -> divisor, so the computation of Kahler cones does not depend on the implementation of toric divisors.

I agree that `Mori_cone()` should return just `Kahler_cone().dual()` and we can implement that later.

GLSM is fine with me, too.

If you want to split off the Kahler cone computation from this ticket then thats fine with me. But we should then make it an independent ticket and not lump into toric divisors.



---

archive/issue_comments_082919.json:
```json
{
    "body": "Moved cones to #9380. Patches remaining relevant to this ticket:\n\n* trac_8988_add_support_for_toric_varieties.patch (same as before, except that `kaehler_cone` is gone)\n\n* trac_8988_doctest_fix_for_symbolic_random_tests.patch\n\nAny issues you still see with these two?",
    "created_at": "2010-06-29T19:42:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82919",
    "user": "https://github.com/novoselt"
}
```

Moved cones to #9380. Patches remaining relevant to this ticket:

* trac_8988_add_support_for_toric_varieties.patch (same as before, except that `kaehler_cone` is gone)

* trac_8988_doctest_fix_for_symbolic_random_tests.patch

Any issues you still see with these two?



---

archive/issue_comments_082920.json:
```json
{
    "body": "The rest is uncontroversial. The two patches apply cleanly to sage 4.4.4. Positive review!",
    "created_at": "2010-06-29T20:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82920",
    "user": "https://github.com/vbraun"
}
```

The rest is uncontroversial. The two patches apply cleanly to sage 4.4.4. Positive review!



---

archive/issue_comments_082921.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-29T20:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82921",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082922.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-01T08:36:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82922",
    "user": "https://github.com/loefflerd"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_082923.json:
```json
{
    "body": "I couldn't get this patch to apply unless I applied #9062, #8986, #9188 and #8987 beforehand. With these installed on top of 4.5.alpha1 (and no others), I got a doctest failure:\n\n```\n> sage -hg qapplied\ntrac_9062_add_support_for_toric_lattices.patch\ntrac_8986_add_support_for_convex_rational_polyhedral_cones.patch\ntrac_9188_fix_facet_normal.patch\ntrac_9188_fix_facet_normal_reviewer.patch\ntrac_8987_add_support_for_rational_polyhedral_fans.patch\ntrac_8987_add_enhanced_cones_and_fans.patch\ntrac_8987_review_changes.patch\ntrac_8987_repr_changes.patch\ntrac_8988_add_support_for_toric_varieties.patch\ntrac_8988_doctest_fix_for_symbolic_random_tests.patch\n> sage -t sage/misc/sageinspect.py\nsage -t  \"devel/sage-reviewing/sage/misc/sageinspect.py\"\n**********************************************************************\nFile \"/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/misc/sageinspect.py\", line 983:\n    sage: sage_getvariablename(A)\nExpected:\n    ['A', 'B']\nGot:\n    ['B', 'A']\n**********************************************************************\n1 items had failures:\n   1 of   8 in __main__.example_22\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/masiao/.sage//tmp/.doctest_sageinspect.py\n         [2.9 s]\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  \"devel/sage-reviewing/sage/misc/sageinspect.py\"\nTotal time for all tests: 2.9 seconds\n```\n\n\nI have not got the foggiest clue why toric varieties can possibly have anything to do with this; it just looks like the doctests for sageinspect are sensitive to exactly what memory addresses things get stored at. I will put this back to \"needs review\" for now, but upload a tiny patch that sorts the variable name list; if you folks agree that it looks harmless, then we can go back to positive review.",
    "created_at": "2010-07-01T08:36:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82923",
    "user": "https://github.com/loefflerd"
}
```

I couldn't get this patch to apply unless I applied #9062, #8986, #9188 and #8987 beforehand. With these installed on top of 4.5.alpha1 (and no others), I got a doctest failure:

```
> sage -hg qapplied
trac_9062_add_support_for_toric_lattices.patch
trac_8986_add_support_for_convex_rational_polyhedral_cones.patch
trac_9188_fix_facet_normal.patch
trac_9188_fix_facet_normal_reviewer.patch
trac_8987_add_support_for_rational_polyhedral_fans.patch
trac_8987_add_enhanced_cones_and_fans.patch
trac_8987_review_changes.patch
trac_8987_repr_changes.patch
trac_8988_add_support_for_toric_varieties.patch
trac_8988_doctest_fix_for_symbolic_random_tests.patch
> sage -t sage/misc/sageinspect.py
sage -t  "devel/sage-reviewing/sage/misc/sageinspect.py"
**********************************************************************
File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/misc/sageinspect.py", line 983:
    sage: sage_getvariablename(A)
Expected:
    ['A', 'B']
Got:
    ['B', 'A']
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_22
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/masiao/.sage//tmp/.doctest_sageinspect.py
         [2.9 s]

----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage-reviewing/sage/misc/sageinspect.py"
Total time for all tests: 2.9 seconds
```


I have not got the foggiest clue why toric varieties can possibly have anything to do with this; it just looks like the doctests for sageinspect are sensitive to exactly what memory addresses things get stored at. I will put this back to "needs review" for now, but upload a tiny patch that sorts the variable name list; if you folks agree that it looks harmless, then we can go back to positive review.



---

archive/issue_comments_082924.json:
```json
{
    "body": "fix a broken doctest in sageinspect",
    "created_at": "2010-07-01T08:37:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82924",
    "user": "https://github.com/loefflerd"
}
```

fix a broken doctest in sageinspect



---

archive/issue_comments_082925.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-01T08:37:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82925",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082926.json:
```json
{
    "body": "Attachment [trac_8988-sageinspect_doctest_fix.patch](tarball://root/attachments/some-uuid/ticket8988/trac_8988-sageinspect_doctest_fix.patch) by @loefflerd created at 2010-07-01 08:37:38\n\nHere's the fix.",
    "created_at": "2010-07-01T08:37:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82926",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_8988-sageinspect_doctest_fix.patch](tarball://root/attachments/some-uuid/ticket8988/trac_8988-sageinspect_doctest_fix.patch) by @loefflerd created at 2010-07-01 08:37:38

Here's the fix.



---

archive/issue_comments_082927.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-01T09:35:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82927",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082928.json:
```json
{
    "body": "The order of the output of `sage_getvariablename` is in the memory order of some python `dict`, so the doctest had to fail at one point. I grepped through the sage library and the only use of `sage_getvariablename` is in `sage/matrix/matrix0.pyx` where the order of items is actually not used. \n\nSo davidloeffler's fix of sorting the output of `sage_getvariablename` is safe and the right thing to do to return a deterministic output. I give it a positive review.",
    "created_at": "2010-07-01T09:35:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82928",
    "user": "https://github.com/vbraun"
}
```

The order of the output of `sage_getvariablename` is in the memory order of some python `dict`, so the doctest had to fail at one point. I grepped through the sage library and the only use of `sage_getvariablename` is in `sage/matrix/matrix0.pyx` where the order of items is actually not used. 

So davidloeffler's fix of sorting the output of `sage_getvariablename` is safe and the right thing to do to return a deterministic output. I give it a positive review.



---

archive/issue_comments_082929.json:
```json
{
    "body": "I made a systematic mistake in doctests of `__cmp__`  methods of all patches, discovered in #9062. So now I am posting these one-line patches to fix them, please review!",
    "created_at": "2010-07-01T16:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82929",
    "user": "https://github.com/novoselt"
}
```

I made a systematic mistake in doctests of `__cmp__`  methods of all patches, discovered in #9062. So now I am posting these one-line patches to fix them, please review!



---

archive/issue_comments_082930.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-01T16:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82930",
    "user": "https://github.com/novoselt"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_082931.json:
```json
{
    "body": "Attachment [trac_8988_cmp_fix.patch](tarball://root/attachments/some-uuid/ticket8988/trac_8988_cmp_fix.patch) by @novoselt created at 2010-07-01 16:28:46",
    "created_at": "2010-07-01T16:28:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82931",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_8988_cmp_fix.patch](tarball://root/attachments/some-uuid/ticket8988/trac_8988_cmp_fix.patch) by @novoselt created at 2010-07-01 16:28:46



---

archive/issue_comments_082932.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-01T16:28:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82932",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082933.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-01T16:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82933",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082934.json:
```json
{
    "body": "Positive review of the doctest fix!",
    "created_at": "2010-07-01T16:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82934",
    "user": "https://github.com/vbraun"
}
```

Positive review of the doctest fix!



---

archive/issue_comments_082935.json:
```json
{
    "body": "These patches won't apply without #8986, which is currently at \"needs work\", so it can't be merged at present.",
    "created_at": "2010-07-01T17:55:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82935",
    "user": "https://github.com/loefflerd"
}
```

These patches won't apply without #8986, which is currently at "needs work", so it can't be merged at present.



---

archive/issue_comments_082936.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-01T17:55:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82936",
    "user": "https://github.com/loefflerd"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_082937.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-02T10:03:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82937",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082938.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-02T10:03:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82938",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082939.json:
```json
{
    "body": "See #9514 for a patch that fixes the random_tests doctest issue.",
    "created_at": "2010-07-16T04:34:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82939",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

See #9514 for a patch that fixes the random_tests doctest issue.



---

archive/issue_comments_082940.json:
```json
{
    "body": "It will be better to pre-merge #9514 instead of the doctest fix from this ticket. Then the following patches must be applied:\n\n* trac_8988_add_support_for_toric_varieties.patch\n* trac_8988-sageinspect_doctest_fix.patch\n* trac_8988_cmp_fix.patch",
    "created_at": "2010-07-16T15:33:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82940",
    "user": "https://github.com/novoselt"
}
```

It will be better to pre-merge #9514 instead of the doctest fix from this ticket. Then the following patches must be applied:

* trac_8988_add_support_for_toric_varieties.patch
* trac_8988-sageinspect_doctest_fix.patch
* trac_8988_cmp_fix.patch



---

archive/issue_comments_082941.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T08:57:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82941",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_009143.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-07-20T08:57:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8988#event-9143"
}
```



---

archive/issue_comments_082942.json:
```json
{
    "body": "There's a doctest failure in SageNB's `sageinspect.py`:\n\n```python\n$ ./sage -t -long  local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/misc/sageinspect.py\nsage -t -long \"local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/misc/sageinspect.py\"\n**********************************************************************\nFile \"/mnt/usb1/scratch/mpatel/tmp/sage-4.5.1-rm/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/misc/sageinspect.py\", line 997:\n    sage: sage_getvariablename(A)\nExpected:\n    ['A', 'B']\nGot:\n    ['B', 'A']\n**********************************************************************\n1 items had failures:\n   1 of   8 in __main__.example_22\n***Test Failed*** 1 failures.\n```\n\nI'm closing this ticket as fixed but have opened #9554 as a blocker for 4.5.2.",
    "created_at": "2010-07-20T08:57:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8988#issuecomment-82942",
    "user": "https://github.com/qed777"
}
```

There's a doctest failure in SageNB's `sageinspect.py`:

```python
$ ./sage -t -long  local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/misc/sageinspect.py
sage -t -long "local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/misc/sageinspect.py"
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.5.1-rm/local/lib/python2.6/site-packages/sagenb-0.8.1-py2.6.egg/sagenb/misc/sageinspect.py", line 997:
    sage: sage_getvariablename(A)
Expected:
    ['A', 'B']
Got:
    ['B', 'A']
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_22
***Test Failed*** 1 failures.
```

I'm closing this ticket as fixed but have opened #9554 as a blocker for 4.5.2.
