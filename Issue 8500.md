# Issue 8500: Add number_of_transitive_group function

archive/issues_008500.json:
```json
{
    "body": "Assignee: nborie\n\nCC:  sage-combinat\n\nKeywords: transitive group\n\nTransitiveGroup are already in Sage and work only if you have the right database installed. As I offen test systematicly over all transitive groups, I will be happy to get this number in Sage.\n\n\n```\nsage: TransitiveGroup(7,7)\nTransitive group number 7 of degree 7\nsage: TransitiveGroup(7,8)\nverbose 0 (846: permgroup_named.py, __init__) Warning: Computing with TransitiveGroups requires the optional database_gap package. Please install it.\nTransitive group number 8 of degree 7\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8500\n\n",
    "created_at": "2010-03-11T20:49:20Z",
    "labels": [
        "group theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Add number_of_transitive_group function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8500",
    "user": "nborie"
}
```
Assignee: nborie

CC:  sage-combinat

Keywords: transitive group

TransitiveGroup are already in Sage and work only if you have the right database installed. As I offen test systematicly over all transitive groups, I will be happy to get this number in Sage.


```
sage: TransitiveGroup(7,7)
Transitive group number 7 of degree 7
sage: TransitiveGroup(7,8)
verbose 0 (846: permgroup_named.py, __init__) Warning: Computing with TransitiveGroups requires the optional database_gap package. Please install it.
Transitive group number 8 of degree 7
```


Issue created by migration from https://trac.sagemath.org/ticket/8500





---

archive/issue_comments_076738.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-11T21:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76738",
    "user": "nborie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076739.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-12T07:23:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76739",
    "user": "nborie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_076740.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-12T23:58:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76740",
    "user": "nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076741.json:
```json
{
    "body": "Wow,that was quick, thanks!\n\nI browsed through the patch, which looks good. Some minor comments before I do the final review:\n\n- Change \"trac 8500 Add the finite enumerated set of TransitiveGroups\" to \"#8500 Add the enumerated set of TransitiveGroups\"\n\n- Keep number_of_transitive_groups a private function (i.e. not in all.py)\n\n- TransitiveGroups() would better model the mathematical set of all transitive groups, even if this is only partially implemented. Hence TransitiveGroups() should be in InfiniteEnumeratedSets (and therefore TransitiveGroups().cardinality() will return infinity). As a side effect, the #long time should not be needed anymore for the TestSuite(TransitiveGroups()).run().\n\n- You may actually want to implement TransitiveGroups() as a DisjointUnionOfEnumeratedSets, which should essentially do all the work for you.\n\n -",
    "created_at": "2010-03-13T09:01:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76741",
    "user": "@nthiery"
}
```

Wow,that was quick, thanks!

I browsed through the patch, which looks good. Some minor comments before I do the final review:

- Change "trac 8500 Add the finite enumerated set of TransitiveGroups" to "#8500 Add the enumerated set of TransitiveGroups"

- Keep number_of_transitive_groups a private function (i.e. not in all.py)

- TransitiveGroups() would better model the mathematical set of all transitive groups, even if this is only partially implemented. Hence TransitiveGroups() should be in InfiniteEnumeratedSets (and therefore TransitiveGroups().cardinality() will return infinity). As a side effect, the #long time should not be needed anymore for the TestSuite(TransitiveGroups()).run().

- You may actually want to implement TransitiveGroups() as a DisjointUnionOfEnumeratedSets, which should essentially do all the work for you.

 -



---

archive/issue_comments_076742.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-13T09:01:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76742",
    "user": "@nthiery"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_076743.json:
```json
{
    "body": "Hi,\n\n* Commit message : will do!\n\n* Private function : Why not? There is no reference page built for permgroup_named.py... It will be used by the very private club...\n\n* Ok, Do you prefer a StopIteration or a NotImplementedError for the __iter__ method ?\n\n* DisjointUnionOfEnumeratedSets????? I don't know this toy but I already like the name. Will play with it (and hope it is robust (like children, when I play....))\n\nThanks for these advises...",
    "created_at": "2010-03-13T09:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76743",
    "user": "nborie"
}
```

Hi,

* Commit message : will do!

* Private function : Why not? There is no reference page built for permgroup_named.py... It will be used by the very private club...

* Ok, Do you prefer a StopIteration or a NotImplementedError for the __iter__ method ?

* DisjointUnionOfEnumeratedSets????? I don't know this toy but I already like the name. Will play with it (and hope it is robust (like children, when I play....))

Thanks for these advises...



---

archive/issue_comments_076744.json:
```json
{
    "body": "Replying to [comment:6 nborie]:\n> * Ok, Do you prefer a StopIteration or a NotImplementedError for the __iter__ method ?\n\nHmm, I guess NotImplementedError. And I assume that should be what occurs by default with DisjointUnionOfEnumeratedSets.\n\n> \n> * DisjointUnionOfEnumeratedSets????? I don't know this toy but I already like the name. Will play with it (and hope it is robust (like children, when I play....))\n\nNote: you'll have a micro-issue with classcall, which Florent is supposed to fix shortly (he stumbled into it yesterday.\n\nOh, by the way: what gap is providing you is actually an unrank function (see enumeratedSets). You just need to implement TransitiveGroups(3).unrank(5), and __iter__ will be provided to you for free.\n\n> Thanks for these advises...\n\nYou are welcome!",
    "created_at": "2010-03-13T11:38:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76744",
    "user": "@nthiery"
}
```

Replying to [comment:6 nborie]:
> * Ok, Do you prefer a StopIteration or a NotImplementedError for the __iter__ method ?

Hmm, I guess NotImplementedError. And I assume that should be what occurs by default with DisjointUnionOfEnumeratedSets.

> 
> * DisjointUnionOfEnumeratedSets????? I don't know this toy but I already like the name. Will play with it (and hope it is robust (like children, when I play....))

Note: you'll have a micro-issue with classcall, which Florent is supposed to fix shortly (he stumbled into it yesterday.

Oh, by the way: what gap is providing you is actually an unrank function (see enumeratedSets). You just need to implement TransitiveGroups(3).unrank(5), and __iter__ will be provided to you for free.

> Thanks for these advises...

You are welcome!



---

archive/issue_comments_076745.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-15T12:28:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76745",
    "user": "nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076746.json:
```json
{
    "body": "I included all yours recommendations. I just didn't remove the # long time for the test :\nTestSuite(TransitiveGroups()).run()\nEven it is now an Infinite Enumerated Set, the test still need around 20 seconds.",
    "created_at": "2010-03-15T13:38:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76746",
    "user": "nborie"
}
```

I included all yours recommendations. I just didn't remove the # long time for the test :
TestSuite(TransitiveGroups()).run()
Even it is now an Infinite Enumerated Set, the test still need around 20 seconds.



---

archive/issue_comments_076747.json:
```json
{
    "body": "Attachment [trac_8500_number_transitive_group-nb.patch](tarball://root/attachments/some-uuid/ticket8500/trac_8500_number_transitive_group-nb.patch) by nborie created at 2010-03-15 15:02:07",
    "created_at": "2010-03-15T15:02:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76747",
    "user": "nborie"
}
```

Attachment [trac_8500_number_transitive_group-nb.patch](tarball://root/attachments/some-uuid/ticket8500/trac_8500_number_transitive_group-nb.patch) by nborie created at 2010-03-15 15:02:07



---

archive/issue_comments_076748.json:
```json
{
    "body": "I just update the patch : I forgot some # optional. Done..",
    "created_at": "2010-03-15T15:03:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76748",
    "user": "nborie"
}
```

I just update the patch : I forgot some # optional. Done..



---

archive/issue_comments_076749.json:
```json
{
    "body": "Attachment [trac_8500_number_transitive_group-review-nt.patch](tarball://root/attachments/some-uuid/ticket8500/trac_8500_number_transitive_group-review-nt.patch) by @nthiery created at 2010-04-18 20:00:19",
    "created_at": "2010-04-18T20:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76749",
    "user": "@nthiery"
}
```

Attachment [trac_8500_number_transitive_group-review-nt.patch](tarball://root/attachments/some-uuid/ticket8500/trac_8500_number_transitive_group-review-nt.patch) by @nthiery created at 2010-04-18 20:00:19



---

archive/issue_comments_076750.json:
```json
{
    "body": "All test pass on Sage 4.3.4 and 4.4-alpha0.\n\nThat will be a useful feature! Thanks for handling this!\n\nPlease check my reviewer's patch, and if it's fine, go ahead and set a positive review.",
    "created_at": "2010-04-18T20:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76750",
    "user": "@nthiery"
}
```

All test pass on Sage 4.3.4 and 4.4-alpha0.

That will be a useful feature! Thanks for handling this!

Please check my reviewer's patch, and if it's fine, go ahead and set a positive review.



---

archive/issue_comments_076751.json:
```json
{
    "body": "I applied the two patches with the dependency. Everything is ok  except the sentence in the doc of the class TransitiveGroupsAll, the set is not finite!\n\n```\nsage.groups.perm_gps.permgroup_named.TransitiveGroupsAll\u00b6\n\n    The finite set of all transitive groups.\n```\n\nThat's my fault from my patch... Who fix that ? modulo the two letter \"in\" before finite, it is a positive review....",
    "created_at": "2010-04-18T21:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76751",
    "user": "nborie"
}
```

I applied the two patches with the dependency. Everything is ok  except the sentence in the doc of the class TransitiveGroupsAll, the set is not finite!

```
sage.groups.perm_gps.permgroup_named.TransitiveGroupsAll¶

    The finite set of all transitive groups.
```

That's my fault from my patch... Who fix that ? modulo the two letter "in" before finite, it is a positive review....



---

archive/issue_comments_076752.json:
```json
{
    "body": "Attachment [trac_8500_number_transitive_group-review-nb.patch](tarball://root/attachments/some-uuid/ticket8500/trac_8500_number_transitive_group-review-nb.patch) by nborie created at 2010-04-19 08:06:22",
    "created_at": "2010-04-19T08:06:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76752",
    "user": "nborie"
}
```

Attachment [trac_8500_number_transitive_group-review-nb.patch](tarball://root/attachments/some-uuid/ticket8500/trac_8500_number_transitive_group-review-nb.patch) by nborie created at 2010-04-19 08:06:22



---

archive/issue_comments_076753.json:
```json
{
    "body": "I clearly set a positive review on your reviewer patch!\n\nI had a failure in :\nsage -t sage/groups/perm_gps/permgroup_named.py --optional --long\n\n```\nsage -t --optional --long \"devel/sage-review/sage/groups/perm_gps/permgroup_named.py\"\n**********************************************************************\nFile \"/opt/sage/devel/sage-review/sage/groups/perm_gps/permgroup_named.py\", line 884:\n    sage: TransitiveGroup(5,0)                 # requires optional database_gap\nExpected:\n    Traceback (most recent call last):\n    ...\n    AssertionError: n should be in {1,..,5}\nGot:\n    Traceback (most recent call last):\n    ...\n        assert n > 0\n    AssertionError\n```\n\n\nThus I propose you a final patch (very easy to review) with a fix of the doc of TransitiveGroupsAll and a move of an assert on the index of a transitive group.\n\nNow, all tests long and optional passes. I hope we don't leave any error in the doc too.",
    "created_at": "2010-04-19T08:16:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76753",
    "user": "nborie"
}
```

I clearly set a positive review on your reviewer patch!

I had a failure in :
sage -t sage/groups/perm_gps/permgroup_named.py --optional --long

```
sage -t --optional --long "devel/sage-review/sage/groups/perm_gps/permgroup_named.py"
**********************************************************************
File "/opt/sage/devel/sage-review/sage/groups/perm_gps/permgroup_named.py", line 884:
    sage: TransitiveGroup(5,0)                 # requires optional database_gap
Expected:
    Traceback (most recent call last):
    ...
    AssertionError: n should be in {1,..,5}
Got:
    Traceback (most recent call last):
    ...
        assert n > 0
    AssertionError
```


Thus I propose you a final patch (very easy to review) with a fix of the doc of TransitiveGroupsAll and a move of an assert on the index of a transitive group.

Now, all tests long and optional passes. I hope we don't leave any error in the doc too.



---

archive/issue_comments_076754.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-19T17:25:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76754",
    "user": "@nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076755.json:
```json
{
    "body": "Replying to [comment:14 nborie]:\n> I clearly set a positive review on your reviewer patch!\n\nOk, thanks for checking!\n\n> I had a failure in :\n> sage -t sage/groups/perm_gps/permgroup_named.py --optional --long\n\nOops, I let that one slip through. Thanks for the report!\n\n> Thus I propose you a final patch (very easy to review) with a fix of the doc of TransitiveGroupsAll and a move of an assert on the index of a transitive group.\n\nI merged your doc fix in my patch. For the assertion, I fixed the doctest instead. The message is not as nice, but using assert n>0 has the (admittedly limited) advantage of failing even if the database is not there.\n\nWith this the patch is good to go. Positive review. Thanks for your work on this!\n\nI'll now fold the two patches together and upload the final version here.",
    "created_at": "2010-04-19T17:25:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76755",
    "user": "@nthiery"
}
```

Replying to [comment:14 nborie]:
> I clearly set a positive review on your reviewer patch!

Ok, thanks for checking!

> I had a failure in :
> sage -t sage/groups/perm_gps/permgroup_named.py --optional --long

Oops, I let that one slip through. Thanks for the report!

> Thus I propose you a final patch (very easy to review) with a fix of the doc of TransitiveGroupsAll and a move of an assert on the index of a transitive group.

I merged your doc fix in my patch. For the assertion, I fixed the doctest instead. The message is not as nice, but using assert n>0 has the (admittedly limited) advantage of failing even if the database is not there.

With this the patch is good to go. Positive review. Thanks for your work on this!

I'll now fold the two patches together and upload the final version here.



---

archive/issue_comments_076756.json:
```json
{
    "body": "Apply only this one",
    "created_at": "2010-04-19T17:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76756",
    "user": "@nthiery"
}
```

Apply only this one



---

archive/issue_comments_076757.json:
```json
{
    "body": "Changing keywords from \"transitive group\" to \"transitive groups\".",
    "created_at": "2010-04-19T17:33:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76757",
    "user": "@nthiery"
}
```

Changing keywords from "transitive group" to "transitive groups".



---

archive/issue_comments_076758.json:
```json
{
    "body": "Attachment [trac_8500_transitive_groups-final.patch](tarball://root/attachments/some-uuid/ticket8500/trac_8500_transitive_groups-final.patch) by @nthiery created at 2010-04-19 17:33:14",
    "created_at": "2010-04-19T17:33:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76758",
    "user": "@nthiery"
}
```

Attachment [trac_8500_transitive_groups-final.patch](tarball://root/attachments/some-uuid/ticket8500/trac_8500_transitive_groups-final.patch) by @nthiery created at 2010-04-19 17:33:14



---

archive/issue_comments_076759.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-22T02:08:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76759",
    "user": "@jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_076760.json:
```json
{
    "body": "If I apply \"trac_8500_transitive_groups-final.patch\" on top of 4.4.alpha1, all tests pass.  If I instead apply the patch from #8549, all tests pass.  If I apply *both* patches, though, then on my Mac (OS X 10.6.3), I get a doctest failure:\n\n```\nsage -t -long \"devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py\"\n**********************************************************************\nFile \"/Applications/sage_builds/sage-4.4.alpha1/devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py\", line 315:\n    sage: len(C.points())\nException raised:\n    Traceback (most recent call last):\n      File \"/Applications/sage_builds/sage-4.4.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Applications/sage_builds/sage-4.4.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Applications/sage_builds/sage-4.4.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[7]>\", line 1, in <module>\n        len(C.points())###line 315:\n    sage: len(C.points())\n      File \"/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py\", line 327, in points\n        self.__points = self._points_fast_sqrt() # this is fast using Zech logarithms\n      File \"/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py\", line 239, in _points_fast_sqrt\n        points.append(self.point([x, v+sqrtD, one], check=True))\n      File \"/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/scheme.py\", line 256, in point\n        return self._point_class(self, v, check=check)\n      File \"/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/algebraic_scheme.py\", line 196, in _point_class\n        return self.__A._point_class(*args, **kwds)\n      File \"/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/projective_space.py\", line 535, in _point_class\n        return morphism.SchemeMorphism_projective_coordinates_field(*args, **kwds)\n      File \"/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/morphism.py\", line 608, in __init__\n        X.codomain()._check_satisfies_equations(v)\n      File \"/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/algebraic_scheme.py\", line 465, in _check_satisfies_equations\n        raise TypeError, \"Coordinates %s do not define a point on %s\"%(list(v),self)\n    TypeError: Coordinates [7*a + 9, 2*a + 2, 1] do not define a point on Hyperelliptic Curve over Finite Field in a of size 11^2 defined by y^2 + (x^2 + 2)*y = x^5 + x + 10\n**********************************************************************\n1 items had failures:\n   1 of   8 in __main__.example_6\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /Users/palmieri/.sage//tmp/.doctest_hyperelliptic_finite_field.py\n\t [8.2 s]\n```\n",
    "created_at": "2010-04-22T02:08:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76760",
    "user": "@jhpalmieri"
}
```

If I apply "trac_8500_transitive_groups-final.patch" on top of 4.4.alpha1, all tests pass.  If I instead apply the patch from #8549, all tests pass.  If I apply *both* patches, though, then on my Mac (OS X 10.6.3), I get a doctest failure:

```
sage -t -long "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py"
**********************************************************************
File "/Applications/sage_builds/sage-4.4.alpha1/devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py", line 315:
    sage: len(C.points())
Exception raised:
    Traceback (most recent call last):
      File "/Applications/sage_builds/sage-4.4.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Applications/sage_builds/sage-4.4.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Applications/sage_builds/sage-4.4.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[7]>", line 1, in <module>
        len(C.points())###line 315:
    sage: len(C.points())
      File "/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py", line 327, in points
        self.__points = self._points_fast_sqrt() # this is fast using Zech logarithms
      File "/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py", line 239, in _points_fast_sqrt
        points.append(self.point([x, v+sqrtD, one], check=True))
      File "/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/scheme.py", line 256, in point
        return self._point_class(self, v, check=check)
      File "/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/algebraic_scheme.py", line 196, in _point_class
        return self.__A._point_class(*args, **kwds)
      File "/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/projective_space.py", line 535, in _point_class
        return morphism.SchemeMorphism_projective_coordinates_field(*args, **kwds)
      File "/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/morphism.py", line 608, in __init__
        X.codomain()._check_satisfies_equations(v)
      File "/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/algebraic_scheme.py", line 465, in _check_satisfies_equations
        raise TypeError, "Coordinates %s do not define a point on %s"%(list(v),self)
    TypeError: Coordinates [7*a + 9, 2*a + 2, 1] do not define a point on Hyperelliptic Curve over Finite Field in a of size 11^2 defined by y^2 + (x^2 + 2)*y = x^5 + x + 10
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_6
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/palmieri/.sage//tmp/.doctest_hyperelliptic_finite_field.py
	 [8.2 s]
```




---

archive/issue_comments_076761.json:
```json
{
    "body": "Replying to [comment:17 jhpalmieri]:\n> If I apply \"trac_8500_transitive_groups-final.patch\" on top of 4.4.alpha1, all tests pass.  If I instead apply the patch from #8549, all tests pass.  If I apply *both* patches, though, then on my Mac (OS X 10.6.3), I get a doctest failure:\n\nOuch?!?!? How can two patches that add isolated features possibly break something so unrelated???\n\nI am totally clueless on how to attack this. Is there a mac somewhere online where I could login to play around? Is the gap-database installed on that mac?\n\nThanks!",
    "created_at": "2010-04-22T06:25:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76761",
    "user": "@nthiery"
}
```

Replying to [comment:17 jhpalmieri]:
> If I apply "trac_8500_transitive_groups-final.patch" on top of 4.4.alpha1, all tests pass.  If I instead apply the patch from #8549, all tests pass.  If I apply *both* patches, though, then on my Mac (OS X 10.6.3), I get a doctest failure:

Ouch?!?!? How can two patches that add isolated features possibly break something so unrelated???

I am totally clueless on how to attack this. Is there a mac somewhere online where I could login to play around? Is the gap-database installed on that mac?

Thanks!



---

archive/issue_comments_076762.json:
```json
{
    "body": "Replying to [comment:18 nthiery]:\n>\n> Ouch?!?!? How can two patches that add isolated features possibly break something so unrelated???\n\nI don't know, but it was quite repeatable: apply either patch first, no doctest failure, then apply the second one, and boom.  (Although it took me a little while to track down that two independent tickets seemed to be causing the problem.)  I just confirmed this on a second mac.  It seems to require 4.4.alpha1, not 4.4.alpha0, so it must also be related to one of the tickets already merged there: see [http://trac.sagemath.org/sage_trac/query?order=priority&col=id&col=summary&col=status&col=type&col=priority&col=milestone&col=component&merged=%7Esage-4.4.alpha1](http://trac.sagemath.org/sage_trac/query?order=priority&col=id&col=summary&col=status&col=type&col=priority&col=milestone&col=component&merged=%7Esage-4.4.alpha1) for a list. Of course, none of those touch the file schemes/hyperelliptic_curves/hyperelliptic_finite_field.py, either.  At least #8496, #8505, and #8557 have something to do with schemes...\n \n> I am totally clueless on how to attack this. Is there a mac somewhere online where I could login to play around? Is the gap-database installed on that mac?\n\nAs far as I know, bsd.math.washington.edu is a mac which is used for Sage development.  You will need a separate account on it: an account on sage.math doesn't automatically give you one on bsd.math.  Ask William (or maybe Tom Boothby?) about that.",
    "created_at": "2010-04-22T22:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76762",
    "user": "@jhpalmieri"
}
```

Replying to [comment:18 nthiery]:
>
> Ouch?!?!? How can two patches that add isolated features possibly break something so unrelated???

I don't know, but it was quite repeatable: apply either patch first, no doctest failure, then apply the second one, and boom.  (Although it took me a little while to track down that two independent tickets seemed to be causing the problem.)  I just confirmed this on a second mac.  It seems to require 4.4.alpha1, not 4.4.alpha0, so it must also be related to one of the tickets already merged there: see [http://trac.sagemath.org/sage_trac/query?order=priority&col=id&col=summary&col=status&col=type&col=priority&col=milestone&col=component&merged=%7Esage-4.4.alpha1](http://trac.sagemath.org/sage_trac/query?order=priority&col=id&col=summary&col=status&col=type&col=priority&col=milestone&col=component&merged=%7Esage-4.4.alpha1) for a list. Of course, none of those touch the file schemes/hyperelliptic_curves/hyperelliptic_finite_field.py, either.  At least #8496, #8505, and #8557 have something to do with schemes...
 
> I am totally clueless on how to attack this. Is there a mac somewhere online where I could login to play around? Is the gap-database installed on that mac?

As far as I know, bsd.math.washington.edu is a mac which is used for Sage development.  You will need a separate account on it: an account on sage.math doesn't automatically give you one on bsd.math.  Ask William (or maybe Tom Boothby?) about that.



---

archive/issue_comments_076763.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-29T04:56:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76763",
    "user": "@rbeezer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076764.json:
```json
{
    "body": "I asked Jason Grout via IRC to test #8500 and #8549 on hyperelliptic_finite_field.py with OSX 10.6 and the file passed tests.  Slightly edited IRC discussion.\n\n\n```\n[21:34] <rbeezer> jason-: ping\n[21:34] <jason-> pong\n[21:35] <rbeezer> could you do a simple OSX 10.6 test?\n[21:35] <rbeezer> #8500, #8549, apply one patch from each, then\n[21:35] <rbeezer> sage -t -long \"devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py\"\n[21:35] <rbeezer> ???\n[21:36] <jason-> Let me see\n[21:37] <rbeezer> thanks - this particular combo is holding up both tickets\n[21:39] <jason-> all tests passed!\n[21:40] <rbeezer> thanks\n[21:41] <jason-> rbeezer: that's osx 10.6\n```\n\n\nSame combination passed all long tests on 64-bit Ubuntu 9.04, in addition to the one file passing tests for Mike Hansen.\n\nI ran long tests on `devel/sage/sage/groups/perm_gps/permgroup_named.py` with the gap database installed and it all passed tests.\n\nGiven that this seemed ready for a positive review and now passes tests on the OSX combination, I am going to set this to positive review and add Jason to the reviewer list.\n\nRob",
    "created_at": "2010-05-29T04:56:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76764",
    "user": "@rbeezer"
}
```

I asked Jason Grout via IRC to test #8500 and #8549 on hyperelliptic_finite_field.py with OSX 10.6 and the file passed tests.  Slightly edited IRC discussion.


```
[21:34] <rbeezer> jason-: ping
[21:34] <jason-> pong
[21:35] <rbeezer> could you do a simple OSX 10.6 test?
[21:35] <rbeezer> #8500, #8549, apply one patch from each, then
[21:35] <rbeezer> sage -t -long "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py"
[21:35] <rbeezer> ???
[21:36] <jason-> Let me see
[21:37] <rbeezer> thanks - this particular combo is holding up both tickets
[21:39] <jason-> all tests passed!
[21:40] <rbeezer> thanks
[21:41] <jason-> rbeezer: that's osx 10.6
```


Same combination passed all long tests on 64-bit Ubuntu 9.04, in addition to the one file passing tests for Mike Hansen.

I ran long tests on `devel/sage/sage/groups/perm_gps/permgroup_named.py` with the gap database installed and it all passed tests.

Given that this seemed ready for a positive review and now passes tests on the OSX combination, I am going to set this to positive review and add Jason to the reviewer list.

Rob



---

archive/issue_comments_076765.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-29T04:57:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76765",
    "user": "@rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076766.json:
```json
{
    "body": "I just tried on bsd.sagemath.org, with 4.4.2 and just those two patches, and all test pass as well.",
    "created_at": "2010-05-31T10:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76766",
    "user": "@nthiery"
}
```

I just tried on bsd.sagemath.org, with 4.4.2 and just those two patches, and all test pass as well.



---

archive/issue_comments_076767.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-05T22:28:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8500#issuecomment-76767",
    "user": "@mwhansen"
}
```

Resolution: fixed
