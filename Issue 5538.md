# Issue 5538: Family does not copy it's input.

archive/issues_005538.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  sage-combinat\n\nKeywords: Family, mutable input\n\nWhen family got a dictionary it does not copy it's input so that one can modify it. One should use a kind of frozen dictionary. \n\n```\nsage: d = {1:\"a\", 3:\"b\", 4:\"c\"}\nsage: f = Family(d)\nsage: f\nFinite family {1: 'a', 3: 'b', 4: 'c'}\nsage: d.\nsage: d[2] = 'DD'\nsage: d\n{1: 'a', 2: 'DD', 3: 'b', 4: 'c'}\nsage: f\nFinite family {1: 'a', 2: 'DD', 3: 'b', 4: 'c'}\n```\n\n\nFlorent\n\nIssue created by migration from https://trac.sagemath.org/ticket/5538\n\n",
    "created_at": "2009-03-16T23:43:12Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "Family does not copy it's input.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5538",
    "user": "https://github.com/hivert"
}
```
Assignee: @hivert

CC:  sage-combinat

Keywords: Family, mutable input

When family got a dictionary it does not copy it's input so that one can modify it. One should use a kind of frozen dictionary. 

```
sage: d = {1:"a", 3:"b", 4:"c"}
sage: f = Family(d)
sage: f
Finite family {1: 'a', 3: 'b', 4: 'c'}
sage: d.
sage: d[2] = 'DD'
sage: d
{1: 'a', 2: 'DD', 3: 'b', 4: 'c'}
sage: f
Finite family {1: 'a', 2: 'DD', 3: 'b', 4: 'c'}
```


Florent

Issue created by migration from https://trac.sagemath.org/ticket/5538





---

archive/issue_comments_042986.json:
```json
{
    "body": "Attachment [family_improve-fh-5538-submitted.patch](tarball://root/attachments/some-uuid/ticket5538/family_improve-fh-5538-submitted.patch) by @hivert created at 2009-04-06 21:46:43",
    "created_at": "2009-04-06T21:46:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5538#issuecomment-42986",
    "user": "https://github.com/hivert"
}
```

Attachment [family_improve-fh-5538-submitted.patch](tarball://root/attachments/some-uuid/ticket5538/family_improve-fh-5538-submitted.patch) by @hivert created at 2009-04-06 21:46:43



---

archive/issue_comments_042987.json:
```json
{
    "body": "The uploaded patch improve family in several ways.\n\n- first of all the input is now systematically copied to avoid modification;\n\n- now family can handle list and tuple with the class `TrivialFamily`;\n\n- I also corrected the pickling of function when possible and attrcall;\n\n- since it has nothing to do with combinatorics I moved family to sage.set\n\nCheers,\n\nFlorent",
    "created_at": "2009-04-06T21:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5538#issuecomment-42987",
    "user": "https://github.com/hivert"
}
```

The uploaded patch improve family in several ways.

- first of all the input is now systematically copied to avoid modification;

- now family can handle list and tuple with the class `TrivialFamily`;

- I also corrected the pickling of function when possible and attrcall;

- since it has nothing to do with combinatorics I moved family to sage.set

Cheers,

Florent



---

archive/issue_comments_042988.json:
```json
{
    "body": "Attachment [family_doc_fix-final.patch](tarball://root/attachments/some-uuid/ticket5538/family_doc_fix-final.patch) by @hivert created at 2009-04-07 07:56:44\n\nDoc fix",
    "created_at": "2009-04-07T07:56:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5538#issuecomment-42988",
    "user": "https://github.com/hivert"
}
```

Attachment [family_doc_fix-final.patch](tarball://root/attachments/some-uuid/ticket5538/family_doc_fix-final.patch) by @hivert created at 2009-04-07 07:56:44

Doc fix



---

archive/issue_comments_042989.json:
```json
{
    "body": "Since the file is moved, the patch is not very useful. I added a diff from the former `sage/combinat/family.py` to the new `sage/sets/family.py`. It is *not* a patch and should not be applied.",
    "created_at": "2009-04-09T20:43:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5538#issuecomment-42989",
    "user": "https://github.com/hivert"
}
```

Since the file is moved, the patch is not very useful. I added a diff from the former `sage/combinat/family.py` to the new `sage/sets/family.py`. It is *not* a patch and should not be applied.



---

archive/issue_comments_042990.json:
```json
{
    "body": "Attachment [family.diff](tarball://root/attachments/some-uuid/ticket5538/family.diff) by @hivert created at 2009-04-09 20:44:22\n\nDifference of family.py before and after the patch.",
    "created_at": "2009-04-09T20:44:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5538#issuecomment-42990",
    "user": "https://github.com/hivert"
}
```

Attachment [family.diff](tarball://root/attachments/some-uuid/ticket5538/family.diff) by @hivert created at 2009-04-09 20:44:22

Difference of family.py before and after the patch.



---

archive/issue_comments_042991.json:
```json
{
    "body": "On irc, it was decided that we should take chance of this patch to finish the cleanup of the interface of family. I've taken care of this but several issues are still open:\n\n1. The former implementation of family accepted a parameter \"name\" which was never used and which was there to provide a functionality similar to `SageObject.rename`. Therefore it should be removed. Is it ok to keep it and raise a warning so that people in sage-combinat adapt their code according to ?\n\n2. On the other hand, for `LazyFamily` I can use the name of the function to generate a proper name for the family. Here are some examples:\n\n```\nsage: def fun(i): 2*i\nsage: f = LazyFamily([3,4,7], fun); f\nLazy family (fun(i))_{i in [3, 4, 7]}\n\nsage: f = Family(Permutations(3), attrcall(\"to_lehmer_code\"), lazy=True); f\nLazy family (i.to_lehmer_code())_{i in Standard permutations of 3}\n\nsage: f = LazyFamily([3,4,7], lambda i: 2*i); f\nLazy family (<lambda>(i))_{i in [3, 4, 7]}\n```\n\nIs this ok ? In particular the last one used to be printed\n\n```\nLazy family (f(i))_{i in [3, 4, 7]}\n```\n\nI find `<lambda>` more explicit.\n\n3. To have a single interface it was also decided to add a keyword parameter lazy which call's `LazyFamily`. The parameter is False by for now default. I think it depends on the input. In particular if `index` is a combinatorial class which is not a finite one, then the former implementation turned lazy by default. Should we do that ? \n\nCheers,\n\nFlorent",
    "created_at": "2009-04-10T17:05:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5538#issuecomment-42991",
    "user": "https://github.com/hivert"
}
```

On irc, it was decided that we should take chance of this patch to finish the cleanup of the interface of family. I've taken care of this but several issues are still open:

1. The former implementation of family accepted a parameter "name" which was never used and which was there to provide a functionality similar to `SageObject.rename`. Therefore it should be removed. Is it ok to keep it and raise a warning so that people in sage-combinat adapt their code according to ?

2. On the other hand, for `LazyFamily` I can use the name of the function to generate a proper name for the family. Here are some examples:

```
sage: def fun(i): 2*i
sage: f = LazyFamily([3,4,7], fun); f
Lazy family (fun(i))_{i in [3, 4, 7]}

sage: f = Family(Permutations(3), attrcall("to_lehmer_code"), lazy=True); f
Lazy family (i.to_lehmer_code())_{i in Standard permutations of 3}

sage: f = LazyFamily([3,4,7], lambda i: 2*i); f
Lazy family (<lambda>(i))_{i in [3, 4, 7]}
```

Is this ok ? In particular the last one used to be printed

```
Lazy family (f(i))_{i in [3, 4, 7]}
```

I find `<lambda>` more explicit.

3. To have a single interface it was also decided to add a keyword parameter lazy which call's `LazyFamily`. The parameter is False by for now default. I think it depends on the input. In particular if `index` is a combinatorial class which is not a finite one, then the former implementation turned lazy by default. Should we do that ? 

Cheers,

Florent



---

archive/issue_comments_042992.json:
```json
{
    "body": "Agreed on 1, 2, 3. I very much like the printing in 2.\nI looked at the current diff, and it looks good to me.\n\nJust two suggestions in TrivialFamily:\n-  __iter__ could return self.set.__iter__()\n- self.set is a bit of a misnomer since the order is relevant. self.enumeration?",
    "created_at": "2009-04-13T23:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5538#issuecomment-42992",
    "user": "https://github.com/nthiery"
}
```

Agreed on 1, 2, 3. I very much like the printing in 2.
I looked at the current diff, and it looks good to me.

Just two suggestions in TrivialFamily:
-  __iter__ could return self.set.__iter__()
- self.set is a bit of a misnomer since the order is relevant. self.enumeration?



---

archive/issue_comments_042993.json:
```json
{
    "body": "Attachment [family_interface-cleanup-fh-final.patch](tarball://root/attachments/some-uuid/ticket5538/family_interface-cleanup-fh-final.patch) by @hivert created at 2009-04-14 17:01:51\n\nCleanup of the interface.",
    "created_at": "2009-04-14T17:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5538#issuecomment-42993",
    "user": "https://github.com/hivert"
}
```

Attachment [family_interface-cleanup-fh-final.patch](tarball://root/attachments/some-uuid/ticket5538/family_interface-cleanup-fh-final.patch) by @hivert created at 2009-04-14 17:01:51

Cleanup of the interface.



---

archive/issue_comments_042994.json:
```json
{
    "body": "Attachment [family_adapt-fh-final.patch](tarball://root/attachments/some-uuid/ticket5538/family_adapt-fh-final.patch) by @hivert created at 2009-04-14 17:02:17\n\nAdapted root system with the new interface",
    "created_at": "2009-04-14T17:02:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5538#issuecomment-42994",
    "user": "https://github.com/hivert"
}
```

Attachment [family_adapt-fh-final.patch](tarball://root/attachments/some-uuid/ticket5538/family_adapt-fh-final.patch) by @hivert created at 2009-04-14 17:02:17

Adapted root system with the new interface



---

archive/issue_comments_042995.json:
```json
{
    "body": "The current versions of the patch should be definitive ! Please review. \nThey are four patch that should applied without problem in the following order:\n  \n* attachment:family_improve-fh-5538-submitted.patch\n\n* attachment:family_doc_fix-final.patch\n\n* attachment:family_interface-cleanup-fh-final.patch\n\n* attachment:family_adapt-fh-final.patch\n\nThe last two clean the interface up and adapt part of combinat and in particular root-systems to the new interface. The test should runs without deprecation warning.\n\nCheers,\n\nFlorent",
    "created_at": "2009-04-14T17:09:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5538#issuecomment-42995",
    "user": "https://github.com/hivert"
}
```

The current versions of the patch should be definitive ! Please review. 
They are four patch that should applied without problem in the following order:
  
* attachment:family_improve-fh-5538-submitted.patch

* attachment:family_doc_fix-final.patch

* attachment:family_interface-cleanup-fh-final.patch

* attachment:family_adapt-fh-final.patch

The last two clean the interface up and adapt part of combinat and in particular root-systems to the new interface. The test should runs without deprecation warning.

Cheers,

Florent



---

archive/issue_comments_042996.json:
```json
{
    "body": "Attachment [family_review.patch](tarball://root/attachments/some-uuid/ticket5538/family_review.patch) by @nthiery created at 2009-04-14 18:09:51\n\nPositive review.\n\nFlorent: please update the summary accordingly, after double checking my (trivial) review patch. It needs to be applied last.\n\nMichael: do you mind setting the gard +3_4_1 on the patch server just after the merge?\n(and possibly also for the other recently merged in sage-combinat patches). Thanks!",
    "created_at": "2009-04-14T18:09:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5538#issuecomment-42996",
    "user": "https://github.com/nthiery"
}
```

Attachment [family_review.patch](tarball://root/attachments/some-uuid/ticket5538/family_review.patch) by @nthiery created at 2009-04-14 18:09:51

Positive review.

Florent: please update the summary accordingly, after double checking my (trivial) review patch. It needs to be applied last.

Michael: do you mind setting the gard +3_4_1 on the patch server just after the merge?
(and possibly also for the other recently merged in sage-combinat patches). Thanks!



---

archive/issue_comments_042997.json:
```json
{
    "body": "I meant: +3_4_1 or +3_4_2 depending on where it goes of course.",
    "created_at": "2009-04-14T18:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5538#issuecomment-42997",
    "user": "https://github.com/nthiery"
}
```

I meant: +3_4_1 or +3_4_2 depending on where it goes of course.



---

archive/issue_comments_042998.json:
```json
{
    "body": "Reviewed the review patch. All light green\n\nFlorent",
    "created_at": "2009-04-14T19:00:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5538#issuecomment-42998",
    "user": "https://github.com/hivert"
}
```

Reviewed the review patch. All light green

Florent



---

archive/issue_comments_042999.json:
```json
{
    "body": "Dear Michael, \n\nIf it's still possible I'd like to see this one merged in 3.4.1.\nThis is a basic stuff that is useful and should be advertised.\n\nCheers,\n\nFlorent",
    "created_at": "2009-04-14T22:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5538#issuecomment-42999",
    "user": "https://github.com/hivert"
}
```

Dear Michael, 

If it's still possible I'd like to see this one merged in 3.4.1.
This is a basic stuff that is useful and should be advertised.

Cheers,

Florent



---

archive/issue_comments_043000.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-14T22:14:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5538#issuecomment-43000",
    "user": "https://github.com/hivert"
}
```

Changing status from new to assigned.



---

archive/issue_comments_043001.json:
```json
{
    "body": "This patch breaks a lot of pickles:\n\n```\n    Failed:\n    _class__sage_combinat_family_FiniteFamilyWithHiddenKeys__.sobj\n    _class__sage_combinat_family_FiniteFamily__.sobj\n    _class__sage_combinat_family_LazyFamily__.sobj\n    _class__sage_combinat_finite_class_FiniteCombinatorialClass_l__.sobj\n    _class__sage_combinat_free_module_CombinatorialFreeModuleElement__.sobj\n    _class__sage_combinat_free_module_CombinatorialFreeModule__.sobj\n    _class__sage_combinat_root_system_root_space_RootSpace__.sobj\n    _class__sage_combinat_root_system_type_A_ambient_space__.sobj\n    _class__sage_combinat_root_system_type_C_ambient_space__.sobj\n    _class__sage_combinat_root_system_type_E_ambient_space__.sobj\n    _class__sage_combinat_root_system_type_F_ambient_space__.sobj\n    _class__sage_combinat_root_system_type_G_ambient_space__.sobj\n    _class__sage_combinat_root_system_type_reducible_CartanType__.sobj\n    _class__sage_combinat_root_system_weight_space_WeightSpace__.sobj\n    _class__sage_combinat_root_system_weyl_characters_WeightRing__.sobj\n    _class__sage_combinat_root_system_weyl_characters_WeylCharacterRing_class__.sobj\n    _class__sage_combinat_root_system_weyl_characters_WeylCharacter__.sobj\n    _class__sage_combinat_root_system_weyl_group_WeylGroupElement__.sobj\n    _class__sage_combinat_root_system_weyl_group_WeylGroup_gens__.sobj\n    Successfully unpickled 464 objects.\n    Failed to unpickle 19 objects.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-04-14T23:29:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5538#issuecomment-43001",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch breaks a lot of pickles:

```
    Failed:
    _class__sage_combinat_family_FiniteFamilyWithHiddenKeys__.sobj
    _class__sage_combinat_family_FiniteFamily__.sobj
    _class__sage_combinat_family_LazyFamily__.sobj
    _class__sage_combinat_finite_class_FiniteCombinatorialClass_l__.sobj
    _class__sage_combinat_free_module_CombinatorialFreeModuleElement__.sobj
    _class__sage_combinat_free_module_CombinatorialFreeModule__.sobj
    _class__sage_combinat_root_system_root_space_RootSpace__.sobj
    _class__sage_combinat_root_system_type_A_ambient_space__.sobj
    _class__sage_combinat_root_system_type_C_ambient_space__.sobj
    _class__sage_combinat_root_system_type_E_ambient_space__.sobj
    _class__sage_combinat_root_system_type_F_ambient_space__.sobj
    _class__sage_combinat_root_system_type_G_ambient_space__.sobj
    _class__sage_combinat_root_system_type_reducible_CartanType__.sobj
    _class__sage_combinat_root_system_weight_space_WeightSpace__.sobj
    _class__sage_combinat_root_system_weyl_characters_WeightRing__.sobj
    _class__sage_combinat_root_system_weyl_characters_WeylCharacterRing_class__.sobj
    _class__sage_combinat_root_system_weyl_characters_WeylCharacter__.sobj
    _class__sage_combinat_root_system_weyl_group_WeylGroupElement__.sobj
    _class__sage_combinat_root_system_weyl_group_WeylGroup_gens__.sobj
    Successfully unpickled 464 objects.
    Failed to unpickle 19 objects.
```


Cheers,

Michael



---

archive/issue_comments_043002.json:
```json
{
    "body": "Oups ! The problem is due to a file which has been moved and a class which has been renamed. Everything was ready to correctly pickle, but I mixed things up in my backward compatibility import links. I just updated a simple patch which solve the problem on my machine.\n\nMichael: can you review it ? You are the master of checking pickle !\n\nI'm still hoping to be in time for 3.4.1 ...\n\nSorry for the mess,\n\nFlorent",
    "created_at": "2009-04-15T10:03:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5538#issuecomment-43002",
    "user": "https://github.com/hivert"
}
```

Oups ! The problem is due to a file which has been moved and a class which has been renamed. Everything was ready to correctly pickle, but I mixed things up in my backward compatibility import links. I just updated a simple patch which solve the problem on my machine.

Michael: can you review it ? You are the master of checking pickle !

I'm still hoping to be in time for 3.4.1 ...

Sorry for the mess,

Florent



---

archive/issue_comments_043003.json:
```json
{
    "body": "Fixing the Pickle + Minimal doc header.",
    "created_at": "2009-04-15T14:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5538#issuecomment-43003",
    "user": "https://github.com/hivert"
}
```

Fixing the Pickle + Minimal doc header.



---

archive/issue_comments_043004.json:
```json
{
    "body": "Attachment [family_pickle_fix-fh.patch](tarball://root/attachments/some-uuid/ticket5538/family_pickle_fix-fh.patch) by mabshoff created at 2009-04-15 22:21:51\n\nPositive review for the pickle fix patch. The five patches together make the test suite pass.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T22:21:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5538#issuecomment-43004",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [family_pickle_fix-fh.patch](tarball://root/attachments/some-uuid/ticket5538/family_pickle_fix-fh.patch) by mabshoff created at 2009-04-15 22:21:51

Positive review for the pickle fix patch. The five patches together make the test suite pass.

Cheers,

Michael



---

archive/issue_events_005785.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-04-15T22:22:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5538",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5538#event-5785"
}
```



---

archive/issue_comments_043005.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-15T22:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5538#issuecomment-43005",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_043006.json:
```json
{
    "body": "Merged\n\n* trac_5538_part_1_family_improve-fh-5538-submitted.patch\n* trac_5538_part_2_family_doc_fix-final.patch\n* trac_5538_part_3_family_interface-cleanup-fh-final.patch\n* trac_5538_part_4_family_adapt-fh-final.patch\n* trac_5538_part_5_family_pickle_fix-fh.patch\n\nin Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T22:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5538#issuecomment-43006",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged

* trac_5538_part_1_family_improve-fh-5538-submitted.patch
* trac_5538_part_2_family_doc_fix-final.patch
* trac_5538_part_3_family_interface-cleanup-fh-final.patch
* trac_5538_part_4_family_adapt-fh-final.patch
* trac_5538_part_5_family_pickle_fix-fh.patch

in Sage 3.4.1.rc3.

Cheers,

Michael
