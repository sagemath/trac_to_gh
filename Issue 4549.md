# Issue 4549: New method horizontal_border_strip using new IntegerListsLex combinatorial class

archive/issues_004549.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nSee the title. Patch integer_lists_lex-nt in development in sage-combinat.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4549\n\n",
    "created_at": "2008-11-19T16:24:29Z",
    "labels": [
        "component: combinatorics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "New method horizontal_border_strip using new IntegerListsLex combinatorial class",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4549",
    "user": "https://github.com/nthiery"
}
```
Assignee: @mwhansen

CC:  sage-combinat

See the title. Patch integer_lists_lex-nt in development in sage-combinat.

Issue created by migration from https://trac.sagemath.org/ticket/4549





---

archive/issue_comments_034011.json:
```json
{
    "body": "Attachment [integer_lists_lex-4549-nt.patch](tarball://root/attachments/some-uuid/ticket4549/integer_lists_lex-4549-nt.patch) by @nthiery created at 2009-02-13 16:34:51\n\nReworked the integer lists lexicographic generator into a full featured combinatorial class IntegerListsLex\nUse it systematically in Partitions to get constant amortized time iterators.\nAlso implements horizontal_border_strip.\n\nNote: the attached patch does not contain the commit messages!",
    "created_at": "2009-02-13T16:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4549#issuecomment-34011",
    "user": "https://github.com/nthiery"
}
```

Attachment [integer_lists_lex-4549-nt.patch](tarball://root/attachments/some-uuid/ticket4549/integer_lists_lex-4549-nt.patch) by @nthiery created at 2009-02-13 16:34:51

Reworked the integer lists lexicographic generator into a full featured combinatorial class IntegerListsLex
Use it systematically in Partitions to get constant amortized time iterators.
Also implements horizontal_border_strip.

Note: the attached patch does not contain the commit messages!



---

archive/issue_comments_034012.json:
```json
{
    "body": "Replying to [ticket:4549 nthiery]:\n> See the title. Patch integer_lists_lex-nt in development in sage-combinat.\n\nNote: this patch depends on #4371 and #5255.",
    "created_at": "2009-02-13T16:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4549#issuecomment-34012",
    "user": "https://github.com/saliola"
}
```

Replying to [ticket:4549 nthiery]:
> See the title. Patch integer_lists_lex-nt in development in sage-combinat.

Note: this patch depends on #4371 and #5255.



---

archive/issue_events_010359.json:
```json
{
    "actor": "https://github.com/hivert",
    "created_at": "2009-02-13T23:34:11Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4549#event-10359"
}
```



---

archive/issue_comments_034013.json:
```json
{
    "body": "Changing assignee from @mwhansen to @nthiery.",
    "created_at": "2009-02-14T18:27:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4549#issuecomment-34013",
    "user": "https://github.com/nthiery"
}
```

Changing assignee from @mwhansen to @nthiery.



---

archive/issue_comments_034014.json:
```json
{
    "body": "Attachment [trac_4549-review.patch](tarball://root/attachments/some-uuid/ticket4549/trac_4549-review.patch) by @mwhansen created at 2009-02-14 23:26:56",
    "created_at": "2009-02-14T23:26:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4549#issuecomment-34014",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4549-review.patch](tarball://root/attachments/some-uuid/ticket4549/trac_4549-review.patch) by @mwhansen created at 2009-02-14 23:26:56



---

archive/issue_comments_034015.json:
```json
{
    "body": "I've added a patch which adds some doctests, adds a warning when min_part=0 is passed to partitions, and changed the default implementation of count to use Integers so that we don't have to reimplemented in IntegerListsLex\n\nAssuming someone okay's my changes, I think both patches are good to go in.",
    "created_at": "2009-02-14T23:28:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4549#issuecomment-34015",
    "user": "https://github.com/mwhansen"
}
```

I've added a patch which adds some doctests, adds a warning when min_part=0 is passed to partitions, and changed the default implementation of count to use Integers so that we don't have to reimplemented in IntegerListsLex

Assuming someone okay's my changes, I think both patches are good to go in.



---

archive/issue_comments_034016.json:
```json
{
    "body": "Replying to [comment:5 mhansen]:\nIt's ok for me ! The warning is a good idea. Go ahead.",
    "created_at": "2009-02-15T01:24:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4549#issuecomment-34016",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:5 mhansen]:
It's ok for me ! The warning is a good idea. Go ahead.



---

archive/issue_comments_034017.json:
```json
{
    "body": "This patch breaks the pickle jar which according to Mike is no surprise:\n\n```\nsage -t -long \"devel/sage/sage/structure/sage_object.pyx\"   \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.rc1/devel/sage/sage/structure/sage_object.pyx\", line 682:\n    sage: sage.structure.sage_object.unpickle_all(std)\nExpected:\n    doctest:...: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.\n    doctest:...: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.\n    Successfully unpickled ... objects.\n    Failed to unpickle 0 objects.\nGot:\n    doctest:1172: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.\n    doctest:1172: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.\n    ** failed:  _class__sage_combinat_partition_PartitionsGreatestEQ_nk__.sobj\n    ** failed:  _class__sage_combinat_partition_Partitions_constraints__.sobj\n    ** failed:  _class__sage_combinat_partition_PartitionsGreatestLE_nk__.sobj\n    Failed:\n    _class__sage_combinat_partition_PartitionsGreatestEQ_nk__.sobj\n    _class__sage_combinat_partition_Partitions_constraints__.sobj\n    _class__sage_combinat_partition_PartitionsGreatestLE_nk__.sobj\n    Successfully unpickled 445 objects.\n    Failed to unpickle 3 objects.\n**********************************************************************\n```\n\n\nWe need to make a call if we are going to break this pickles or not. Other than that there were no doctesting issues.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-15T08:37:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4549#issuecomment-34017",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch breaks the pickle jar which according to Mike is no surprise:

```
sage -t -long "devel/sage/sage/structure/sage_object.pyx"   
**********************************************************************
File "/scratch/mabshoff/sage-3.3.rc1/devel/sage/sage/structure/sage_object.pyx", line 682:
    sage: sage.structure.sage_object.unpickle_all(std)
Expected:
    doctest:...: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.
    doctest:...: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
    Successfully unpickled ... objects.
    Failed to unpickle 0 objects.
Got:
    doctest:1172: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.
    doctest:1172: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
    ** failed:  _class__sage_combinat_partition_PartitionsGreatestEQ_nk__.sobj
    ** failed:  _class__sage_combinat_partition_Partitions_constraints__.sobj
    ** failed:  _class__sage_combinat_partition_PartitionsGreatestLE_nk__.sobj
    Failed:
    _class__sage_combinat_partition_PartitionsGreatestEQ_nk__.sobj
    _class__sage_combinat_partition_Partitions_constraints__.sobj
    _class__sage_combinat_partition_PartitionsGreatestLE_nk__.sobj
    Successfully unpickled 445 objects.
    Failed to unpickle 3 objects.
**********************************************************************
```


We need to make a call if we are going to break this pickles or not. Other than that there were no doctesting issues.

Cheers,

Michael



---

archive/issue_comments_034018.json:
```json
{
    "body": "Replying to [comment:5 mhansen]:\n> I've added a patch which adds some doctests, adds a warning when min_part=0 is passed to partitions, \nThanks!\n\n> and changed the default implementation of count to use Integers \n\nGood.\n\n> so that we don't have to reimplemented in IntegerListsLex\n\nWe still do! Sorry, I did not comment on this in the code, but the implementation of count differs from\nthe default one from CombinatorialClass, as it bypasses the call to _element_constructor_!",
    "created_at": "2009-02-15T22:32:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4549#issuecomment-34018",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:5 mhansen]:
> I've added a patch which adds some doctests, adds a warning when min_part=0 is passed to partitions, 
Thanks!

> and changed the default implementation of count to use Integers 

Good.

> so that we don't have to reimplemented in IntegerListsLex

We still do! Sorry, I did not comment on this in the code, but the implementation of count differs from
the default one from CombinatorialClass, as it bypasses the call to _element_constructor_!



---

archive/issue_comments_034019.json:
```json
{
    "body": "Replying to [comment:8 mabshoff]:\n> This patch breaks the pickle jar which according to Mike is no surprise:\n\nIndeed no surprise. \n\n> We need to make a call if we are going to break this pickles or not. Other than that there were no doctesting issues.\n\nI would tend to break the pickles indeed, unless someone cries very loud for this.\n\nCheers,\n\t\t\t\tNicolas",
    "created_at": "2009-02-15T22:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4549#issuecomment-34019",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:8 mabshoff]:
> This patch breaks the pickle jar which according to Mike is no surprise:

Indeed no surprise. 

> We need to make a call if we are going to break this pickles or not. Other than that there were no doctesting issues.

I would tend to break the pickles indeed, unless someone cries very loud for this.

Cheers,
				Nicolas



---

archive/issue_events_010360.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-16T04:59:59Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4549#event-10360"
}
```



---

archive/issue_events_010361.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-16T04:59:59Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4549#event-10361"
}
```



---

archive/issue_comments_034020.json:
```json
{
    "body": "I am cleaning up the 3.3 milestone. If a patch with positive review is put up to this ticket on time it might make it into 3.3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T04:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4549#issuecomment-34020",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am cleaning up the 3.3 milestone. If a patch with positive review is put up to this ticket on time it might make it into 3.3.

Cheers,

Michael



---

archive/issue_comments_034021.json:
```json
{
    "body": "Attachment [integer_lists_lex-4549-submitted.patch](tarball://root/attachments/some-uuid/ticket4549/integer_lists_lex-4549-submitted.patch) by @nthiery created at 2009-04-02 05:27:50",
    "created_at": "2009-04-02T05:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4549#issuecomment-34021",
    "user": "https://github.com/nthiery"
}
```

Attachment [integer_lists_lex-4549-submitted.patch](tarball://root/attachments/some-uuid/ticket4549/integer_lists_lex-4549-submitted.patch) by @nthiery created at 2009-04-02 05:27:50



---

archive/issue_comments_034022.json:
```json
{
    "body": "Updated patch:\n- Now handles pickles of PartitionsGreatestEQ and PartitionsGreatestLE from sage <= 3.4.1.\n- Rebased against 3.4 (and sphinx)",
    "created_at": "2009-04-02T05:28:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4549#issuecomment-34022",
    "user": "https://github.com/nthiery"
}
```

Updated patch:
- Now handles pickles of PartitionsGreatestEQ and PartitionsGreatestLE from sage <= 3.4.1.
- Rebased against 3.4 (and sphinx)



---

archive/issue_comments_034023.json:
```json
{
    "body": "I should mention: only the last patch is needed; it integrates the previous ones",
    "created_at": "2009-04-02T05:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4549#issuecomment-34023",
    "user": "https://github.com/nthiery"
}
```

I should mention: only the last patch is needed; it integrates the previous ones



---

archive/issue_comments_034024.json:
```json
{
    "body": "Dear Nicolas,\n\n> I should mention: only the last patch is needed; it integrates the previous ones\n\nThe patch looks good to me. However, though I'm not 100% sure I launched the correct check, it seems that one of the old pickle is still broken:\n\n```\nsage: std = os.environ['SAGE_DATA'] + '/extcode/pickle_jar/pickle_jar.tar.bz2'\nsage: sage.structure.sage_object.unpickle_all(std)\n** failed:  _class__sage_combinat_partition_Partitions_constraints__.sobj\n/usr/local/sage/sage/local/lib/python2.5/site-packages/IPython/iplib.py:2073: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.\n  exec code_obj in self.user_global_ns, self.user_ns\nFailed:\n_class__sage_combinat_partition_Partitions_constraints__.sobj\nSuccessfully unpickled 486 objects.\nFailed to unpickle 1 objects.\n```\n\nAm I doing something wrong ?\n\nCheers,\n\nFlorent",
    "created_at": "2009-04-02T09:49:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4549#issuecomment-34024",
    "user": "https://github.com/hivert"
}
```

Dear Nicolas,

> I should mention: only the last patch is needed; it integrates the previous ones

The patch looks good to me. However, though I'm not 100% sure I launched the correct check, it seems that one of the old pickle is still broken:

```
sage: std = os.environ['SAGE_DATA'] + '/extcode/pickle_jar/pickle_jar.tar.bz2'
sage: sage.structure.sage_object.unpickle_all(std)
** failed:  _class__sage_combinat_partition_Partitions_constraints__.sobj
/usr/local/sage/sage/local/lib/python2.5/site-packages/IPython/iplib.py:2073: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
  exec code_obj in self.user_global_ns, self.user_ns
Failed:
_class__sage_combinat_partition_Partitions_constraints__.sobj
Successfully unpickled 486 objects.
Failed to unpickle 1 objects.
```

Am I doing something wrong ?

Cheers,

Florent



---

archive/issue_comments_034025.json:
```json
{
    "body": "Fix for the remaining broken pickle + tests for the other one.",
    "created_at": "2009-04-03T16:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4549#issuecomment-34025",
    "user": "https://github.com/hivert"
}
```

Fix for the remaining broken pickle + tests for the other one.



---

archive/issue_comments_034026.json:
```json
{
    "body": "Attachment [integer_lists_lex-4549-review.patch](tarball://root/attachments/some-uuid/ticket4549/integer_lists_lex-4549-review.patch) by @hivert created at 2009-04-03 16:36:02\n\nDear All,\n\n> The patch looks good to me. However, though I'm not 100% sure I launched the correct check, it seems that one of the old pickle is still broken:\n\nI added a review patch which should fix this remaining pickle problem. If someone reread it I'm ready to give a positive review. \n\nFlorent",
    "created_at": "2009-04-03T16:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4549#issuecomment-34026",
    "user": "https://github.com/hivert"
}
```

Attachment [integer_lists_lex-4549-review.patch](tarball://root/attachments/some-uuid/ticket4549/integer_lists_lex-4549-review.patch) by @hivert created at 2009-04-03 16:36:02

Dear All,

> The patch looks good to me. However, though I'm not 100% sure I launched the correct check, it seems that one of the old pickle is still broken:

I added a review patch which should fix this remaining pickle problem. If someone reread it I'm ready to give a positive review. 

Florent



---

archive/issue_comments_034027.json:
```json
{
    "body": "Thanks Florent for the fix. I had overlooked this pickle. \nOh, and thanks for pointing out how one can test backward compatibility unpickles :-)\n\nI tried the patch on my machine and it looks and works fine.\n\nSo, I allow myself to set the positive review  flag on behalf of Florent!\n\nI also lifted the priority to major, since this gives a large (memory) efficiency gain.",
    "created_at": "2009-04-04T00:49:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4549#issuecomment-34027",
    "user": "https://github.com/nthiery"
}
```

Thanks Florent for the fix. I had overlooked this pickle. 
Oh, and thanks for pointing out how one can test backward compatibility unpickles :-)

I tried the patch on my machine and it looks and works fine.

So, I allow myself to set the positive review  flag on behalf of Florent!

I also lifted the priority to major, since this gives a large (memory) efficiency gain.



---

archive/issue_comments_034028.json:
```json
{
    "body": "If its still possible, I'd rather see this integrated in 3.4.1, this allows for #5308 being integrated as soon as possible.\n\nFlorent",
    "created_at": "2009-04-04T08:29:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4549#issuecomment-34028",
    "user": "https://github.com/hivert"
}
```

If its still possible, I'd rather see this integrated in 3.4.1, this allows for #5308 being integrated as soon as possible.

Florent



---

archive/issue_events_010362.json:
```json
{
    "actor": "https://github.com/hivert",
    "created_at": "2009-04-04T08:29:26Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4549#event-10362"
}
```



---

archive/issue_events_010363.json:
```json
{
    "actor": "https://github.com/hivert",
    "created_at": "2009-04-04T08:29:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4549#event-10363"
}
```



---

archive/issue_comments_034029.json:
```json
{
    "body": "Merged\n\n* integer_lists_lex-4549-submitted.patch\n* integer_lists_lex-4549-review.patch\n\nin Sage 3.4.1.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-04T23:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4549#issuecomment-34029",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged

* integer_lists_lex-4549-submitted.patch
* integer_lists_lex-4549-review.patch

in Sage 3.4.1.rc0.

Cheers,

Michael



---

archive/issue_comments_034030.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-04T23:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4549#issuecomment-34030",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_010364.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-04T23:56:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4549",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4549#event-10364"
}
```
