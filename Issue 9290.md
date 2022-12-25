# Issue 9290: Implement Coxeter groups in their geometric representation

archive/issues_009290.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9290\n\n",
    "created_at": "2010-06-21T07:49:19Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.13",
    "title": "Implement Coxeter groups in their geometric representation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9290",
    "user": "https://github.com/nthiery"
}
```
Assignee: sage-combinat

CC:  sage-combinat



Issue created by migration from https://trac.sagemath.org/ticket/9290





---

archive/issue_comments_087352.json:
```json
{
    "body": "Partially depends on #8237",
    "created_at": "2010-06-21T07:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9290#issuecomment-87352",
    "user": "https://github.com/nthiery"
}
```

Partially depends on #8237



---

archive/issue_comments_087353.json:
```json
{
    "body": "Changing keywords from \"\" to \"coxeter\".",
    "created_at": "2012-11-19T16:59:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9290#issuecomment-87353",
    "user": "https://github.com/fchapoton"
}
```

Changing keywords from "" to "coxeter".



---

archive/issue_comments_087354.json:
```json
{
    "body": "see also the code in the ticket #14816",
    "created_at": "2013-07-25T15:14:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9290#issuecomment-87354",
    "user": "https://github.com/fchapoton"
}
```

see also the code in the ticket #14816



---

archive/issue_comments_087355.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-09-11T02:21:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9290#issuecomment-87355",
    "user": "https://github.com/tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087356.json:
```json
{
    "body": "Here's a patch which should take care of all except the second point since I thought Dynkin diagrams where separate from Coxeter diagrams except when there are 1,2,3, or 4 bonds (and even then, we're ignoring the arrows).\n\nBase patch is from #15137, but now uses the UCF as the default field.",
    "created_at": "2013-09-11T02:21:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9290#issuecomment-87356",
    "user": "https://github.com/tscrim"
}
```

Here's a patch which should take care of all except the second point since I thought Dynkin diagrams where separate from Coxeter diagrams except when there are 1,2,3, or 4 bonds (and even then, we're ignoring the arrows).

Base patch is from #15137, but now uses the UCF as the default field.



---

archive/issue_comments_087357.json:
```json
{
    "body": "there are some failing doctests\n\nEDIT: hmm, it rather seems to be a problem with the patchbot..",
    "created_at": "2013-09-15T16:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9290#issuecomment-87357",
    "user": "https://github.com/fchapoton"
}
```

there are some failing doctests

EDIT: hmm, it rather seems to be a problem with the patchbot..



---

archive/issue_comments_087358.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-09-15T16:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9290#issuecomment-87358",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_087359.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-09-16T14:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9290#issuecomment-87359",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_087360.json:
```json
{
    "body": "Yep, something is up with the patchbot, so I gave it a kick.\n\n```\nsage -t ../combinat/root_system/cartan_matrix.py\n    [97 tests, 15.77 s]\nsage -t matrix_gps/coxeter_group.py\n    [72 tests, 0.36 s]\nsage -t ../combinat/root_system/coxeter_group.py\n    [28 tests, 18.65 s]\n----------------------------------------------------------------------\nAll tests passed!\n----------------------------------------------------------------------\nTotal time for all tests: 18.8 seconds\n    cpu time: 26.2 seconds\n    cumulative wall time: 34.8 seconds\n```\n",
    "created_at": "2013-09-16T14:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9290#issuecomment-87360",
    "user": "https://github.com/tscrim"
}
```

Yep, something is up with the patchbot, so I gave it a kick.

```
sage -t ../combinat/root_system/cartan_matrix.py
    [97 tests, 15.77 s]
sage -t matrix_gps/coxeter_group.py
    [72 tests, 0.36 s]
sage -t ../combinat/root_system/coxeter_group.py
    [28 tests, 18.65 s]
----------------------------------------------------------------------
All tests passed!
----------------------------------------------------------------------
Total time for all tests: 18.8 seconds
    cpu time: 26.2 seconds
    cumulative wall time: 34.8 seconds
```




---

archive/issue_comments_087361.json:
```json
{
    "body": "one doctest failing\n\n\n```\nFile \"/home/chapoton/sage-5.12.beta5/devel/sage/sage/groups/matrix_gps/coxeter_group.py\", line 278, in sage.groups.matrix_gps.coxeter_group.CoxeterMatrixGroup.__init__\nFailed example:\n    TestSuite(W).run(max_runs=30) # long time\nExpected nothing\nGot:\n    Failure in _test_matrix_generators:\n    Traceback (most recent call last):\n      File \"/home/chapoton/sage-5.12.beta5/local/lib/python2.7/site-packages/sage/misc/sage_unittest.py\", line 282, in run\n        test_method(tester = tester)\n      File \"/home/chapoton/sage-5.12.beta5/local/lib/python2.7/site-packages/sage/groups/matrix_gps/finitely_generated.py\", line 376, in _test_matrix_generators\n        tester.assertEqual(g.matrix(), h.matrix())\n      File \"cachefunc.pyx\", line 1774, in sage.misc.cachefunc.CachedMethodCallerNoArgs.__call__ (sage/misc/cachefunc.c:9546)\n      File \"/home/chapoton/sage-5.12.beta5/local/lib/python2.7/site-packages/sage/groups/matrix_gps/group_element.py\", line 447, in matrix\n        m = g.matrix(self.base_ring())\n      File \"element.pyx\", line 1076, in sage.libs.gap.element.GapElement.matrix (sage/libs/gap/element.c:8618)\n      File \"element.pyx\", line 1473, in sage.libs.gap.element.GapElement_Cyclotomic.sage (sage/libs/gap/element.c:10511)\n      File \"parent.pyx\", line 761, in sage.structure.parent.Parent.__getattr__ (sage/structure/parent.c:6823)\n      File \"misc.pyx\", line 251, in sage.structure.misc.getattr_from_other_class (sage/structure/misc.c:1606)\n    AttributeError: 'UniversalCyclotomicField_with_category' object has no attribute '_n'\n    ------------------------------------------------------------\n    The following tests failed: _test_matrix_generators\n```\n",
    "created_at": "2013-09-17T18:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9290#issuecomment-87361",
    "user": "https://github.com/fchapoton"
}
```

one doctest failing


```
File "/home/chapoton/sage-5.12.beta5/devel/sage/sage/groups/matrix_gps/coxeter_group.py", line 278, in sage.groups.matrix_gps.coxeter_group.CoxeterMatrixGroup.__init__
Failed example:
    TestSuite(W).run(max_runs=30) # long time
Expected nothing
Got:
    Failure in _test_matrix_generators:
    Traceback (most recent call last):
      File "/home/chapoton/sage-5.12.beta5/local/lib/python2.7/site-packages/sage/misc/sage_unittest.py", line 282, in run
        test_method(tester = tester)
      File "/home/chapoton/sage-5.12.beta5/local/lib/python2.7/site-packages/sage/groups/matrix_gps/finitely_generated.py", line 376, in _test_matrix_generators
        tester.assertEqual(g.matrix(), h.matrix())
      File "cachefunc.pyx", line 1774, in sage.misc.cachefunc.CachedMethodCallerNoArgs.__call__ (sage/misc/cachefunc.c:9546)
      File "/home/chapoton/sage-5.12.beta5/local/lib/python2.7/site-packages/sage/groups/matrix_gps/group_element.py", line 447, in matrix
        m = g.matrix(self.base_ring())
      File "element.pyx", line 1076, in sage.libs.gap.element.GapElement.matrix (sage/libs/gap/element.c:8618)
      File "element.pyx", line 1473, in sage.libs.gap.element.GapElement_Cyclotomic.sage (sage/libs/gap/element.c:10511)
      File "parent.pyx", line 761, in sage.structure.parent.Parent.__getattr__ (sage/structure/parent.c:6823)
      File "misc.pyx", line 251, in sage.structure.misc.getattr_from_other_class (sage/structure/misc.c:1606)
    AttributeError: 'UniversalCyclotomicField_with_category' object has no attribute '_n'
    ------------------------------------------------------------
    The following tests failed: _test_matrix_generators
```




---

archive/issue_comments_087362.json:
```json
{
    "body": "The problem was the conversion from gap's cyclotomics to sage by using the UCF. This is fixed in #15204.\n\n```\nsage: W = CoxeterGroup([[1,3,2],[3,1,6],[2,6,1]])\nsage: W._test_matrix_generators()\n```\n",
    "created_at": "2013-09-17T19:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9290#issuecomment-87362",
    "user": "https://github.com/tscrim"
}
```

The problem was the conversion from gap's cyclotomics to sage by using the UCF. This is fixed in #15204.

```
sage: W = CoxeterGroup([[1,3,2],[3,1,6],[2,6,1]])
sage: W._test_matrix_generators()
```




---

archive/issue_comments_087363.json:
```json
{
    "body": "Hello, I have a few comments and questions\n\n\"assert implementation\" : I think this use of assert to check input is not encouraged\n\n\"lazy_import('sage.groups.raag', 'RightAngledArtinGroup')\" : has this something to do in this ticket ?\n\nWhat are the changes \"sage/groups/matrix_gps/finitely_generated.py\" for ?",
    "created_at": "2013-09-21T16:22:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9290#issuecomment-87363",
    "user": "https://github.com/fchapoton"
}
```

Hello, I have a few comments and questions

"assert implementation" : I think this use of assert to check input is not encouraged

"lazy_import('sage.groups.raag', 'RightAngledArtinGroup')" : has this something to do in this ticket ?

What are the changes "sage/groups/matrix_gps/finitely_generated.py" for ?



---

archive/issue_comments_087364.json:
```json
{
    "body": "Hey Frederic,\n\nReplying to [comment:11 chapoton]:\n> \"assert implementation\" : I think this use of assert to check input is not encouraged\n\nThis was a hold-over from the previous implementation, but this is definitely a good time to get rid of it. Fixed.\n\n> \"lazy_import('sage.groups.raag', 'RightAngledArtinGroup')\" : has this something to do in this ticket ?\n\nBecause I didn't split it cleanly with #15137. Fixed.\n\n> What are the changes \"sage/groups/matrix_gps/finitely_generated.py\" for ?\n\nI need to pass the `CoxeterGroups` category up during the initialization, so I had to make those changes.\n\nThanks for catching that,\n\nTravis",
    "created_at": "2013-09-21T17:10:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9290#issuecomment-87364",
    "user": "https://github.com/tscrim"
}
```

Hey Frederic,

Replying to [comment:11 chapoton]:
> "assert implementation" : I think this use of assert to check input is not encouraged

This was a hold-over from the previous implementation, but this is definitely a good time to get rid of it. Fixed.

> "lazy_import('sage.groups.raag', 'RightAngledArtinGroup')" : has this something to do in this ticket ?

Because I didn't split it cleanly with #15137. Fixed.

> What are the changes "sage/groups/matrix_gps/finitely_generated.py" for ?

I need to pass the `CoxeterGroups` category up during the initialization, so I had to make those changes.

Thanks for catching that,

Travis



---

archive/issue_comments_087365.json:
```json
{
    "body": "Well, it seems that the patch triggers the import of numpy at startup. I have not tried to investigate where this happens.",
    "created_at": "2013-09-22T11:11:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9290#issuecomment-87365",
    "user": "https://github.com/fchapoton"
}
```

Well, it seems that the patch triggers the import of numpy at startup. I have not tried to investigate where this happens.



---

archive/issue_comments_087366.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-09-22T11:24:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9290#issuecomment-87366",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_087367.json:
```json
{
    "body": "Attachment [trac_9290-geometric_coxeter_groups-ts.patch](tarball://root/attachments/some-uuid/ticket9290/trac_9290-geometric_coxeter_groups-ts.patch) by @tscrim created at 2013-09-23 02:20:41\n\nI made `CoxeterMatrixGroup` lazy import in to fix the numpy startup import.",
    "created_at": "2013-09-23T02:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9290#issuecomment-87367",
    "user": "https://github.com/tscrim"
}
```

Attachment [trac_9290-geometric_coxeter_groups-ts.patch](tarball://root/attachments/some-uuid/ticket9290/trac_9290-geometric_coxeter_groups-ts.patch) by @tscrim created at 2013-09-23 02:20:41

I made `CoxeterMatrixGroup` lazy import in to fix the numpy startup import.



---

archive/issue_comments_087368.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-09-23T02:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9290#issuecomment-87368",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_087369.json:
```json
{
    "body": "Attachment [trac-9290-review.patch](tarball://root/attachments/some-uuid/ticket9290/trac-9290-review.patch) by @fchapoton created at 2013-10-20 20:29:30",
    "created_at": "2013-10-20T20:29:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9290#issuecomment-87369",
    "user": "https://github.com/fchapoton"
}
```

Attachment [trac-9290-review.patch](tarball://root/attachments/some-uuid/ticket9290/trac-9290-review.patch) by @fchapoton created at 2013-10-20 20:29:30



---

archive/issue_comments_087370.json:
```json
{
    "body": "Hello Travis,\n\nI have made a cosmetic review patch, that you can fold into yours if you want.\n\nThis almost looks good to go, but I was a bit disappointed when I tried:\n\n```\nsage: K = NumberField(x**2+5,'t')\nsage: CoxeterGroup(['H',3],base_ring=K)\n```\n\nand it failed. If there is a way to make that work, it would be great !",
    "created_at": "2013-10-20T20:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9290#issuecomment-87370",
    "user": "https://github.com/fchapoton"
}
```

Hello Travis,

I have made a cosmetic review patch, that you can fold into yours if you want.

This almost looks good to go, but I was a bit disappointed when I tried:

```
sage: K = NumberField(x**2+5,'t')
sage: CoxeterGroup(['H',3],base_ring=K)
```

and it failed. If there is a way to make that work, it would be great !



---

archive/issue_comments_087371.json:
```json
{
    "body": "ok, I can see no easy way to do that. Let us forget this for the moment.\n\nGood to go ?",
    "created_at": "2013-10-21T18:32:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9290#issuecomment-87371",
    "user": "https://github.com/fchapoton"
}
```

ok, I can see no easy way to do that. Let us forget this for the moment.

Good to go ?



---

archive/issue_comments_087372.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-10-22T21:32:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9290#issuecomment-87372",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087373.json:
```json
{
    "body": "Hey Frederic,\n\nI can't see an easy way to do so either. There might be a solution, but it'll probably be either complicated or cumbersome.\n\nThanks for doing the review,\n\nTravis",
    "created_at": "2013-10-22T21:32:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9290#issuecomment-87373",
    "user": "https://github.com/tscrim"
}
```

Hey Frederic,

I can't see an easy way to do so either. There might be a solution, but it'll probably be either complicated or cumbersome.

Thanks for doing the review,

Travis



---

archive/issue_comments_087374.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-10-31T19:15:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9290#issuecomment-87374",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_009451.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-10-31T19:15:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9290",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9290#event-9451"
}
```
