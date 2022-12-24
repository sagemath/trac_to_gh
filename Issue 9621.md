# Issue 9621: Fix GAP interface problem in sylow_subgroup method

archive/issues_009621.json:
```json
{
    "body": "Assignee: joyner\n\nKeywords: GAP string representation\n\nThe following was reported by [Kenny Brown](http://groups.google.com/group/sage-support/browse_thread/thread/9fbca4e4dbadbe37):\n\n```\nsage: n = 3^2 * 7^2\nsage: G = CyclicPermutationGroup(n)\nsage: G.sylow_subgroup(3)\nTraceback (most recent call last):\n...\n```\n\n\nThe problem is that in the sylow_subgroup method, it is attempted to get the string presentation of a permutation in GAP by calling gap.eval(...). However, GAP truncates the output. So, better use gap.eval('Print(...)') instead.\n\nMoreover, the method uses quite generic variable names in the GAP interface. This is dangerous, as the use of variable names that any average user might choose as well can have nasty side effects.\n\nThe attached patch fixes both problems.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9621\n\n",
    "created_at": "2010-07-28T08:18:22Z",
    "labels": [
        "group theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Fix GAP interface problem in sylow_subgroup method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9621",
    "user": "SimonKing"
}
```
Assignee: joyner

Keywords: GAP string representation

The following was reported by [Kenny Brown](http://groups.google.com/group/sage-support/browse_thread/thread/9fbca4e4dbadbe37):

```
sage: n = 3^2 * 7^2
sage: G = CyclicPermutationGroup(n)
sage: G.sylow_subgroup(3)
Traceback (most recent call last):
...
```


The problem is that in the sylow_subgroup method, it is attempted to get the string presentation of a permutation in GAP by calling gap.eval(...). However, GAP truncates the output. So, better use gap.eval('Print(...)') instead.

Moreover, the method uses quite generic variable names in the GAP interface. This is dangerous, as the use of variable names that any average user might choose as well can have nasty side effects.

The attached patch fixes both problems.

Issue created by migration from https://trac.sagemath.org/ticket/9621





---

archive/issue_comments_093192.json:
```json
{
    "body": "Attachment [trac-9621_permgroup_sylow_subgroup.patch](tarball://root/attachments/some-uuid/ticket9621/trac-9621_permgroup_sylow_subgroup.patch) by SimonKing created at 2010-07-28 08:24:11\n\nFixes GAP interface bug of sylow_subgroup method (with doctest)",
    "created_at": "2010-07-28T08:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93192",
    "user": "SimonKing"
}
```

Attachment [trac-9621_permgroup_sylow_subgroup.patch](tarball://root/attachments/some-uuid/ticket9621/trac-9621_permgroup_sylow_subgroup.patch) by SimonKing created at 2010-07-28 08:24:11

Fixes GAP interface bug of sylow_subgroup method (with doctest)



---

archive/issue_comments_093193.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-28T08:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93193",
    "user": "SimonKing"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093194.json:
```json
{
    "body": "Bear with me as this is my first action on the ticket system :-)\n\nIt seems that some parsing functionality has already been built into the gap interface, so all the last lines of sylow_subgroups can be greatly simplified. I have added an extra patch file for this.",
    "created_at": "2010-07-30T11:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93194",
    "user": "jsrn"
}
```

Bear with me as this is my first action on the ticket system :-)

It seems that some parsing functionality has already been built into the gap interface, so all the last lines of sylow_subgroups can be greatly simplified. I have added an extra patch file for this.



---

archive/issue_comments_093195.json:
```json
{
    "body": "Simplification of the above patch",
    "created_at": "2010-07-30T11:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93195",
    "user": "jsrn"
}
```

Simplification of the above patch



---

archive/issue_comments_093196.json:
```json
{
    "body": "Attachment [trac_9621_simplification.patch](tarball://root/attachments/some-uuid/ticket9621/trac_9621_simplification.patch) by SimonKing created at 2010-07-30 13:10:22\n\nReplaces the other two patches",
    "created_at": "2010-07-30T13:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93196",
    "user": "SimonKing"
}
```

Attachment [trac_9621_simplification.patch](tarball://root/attachments/some-uuid/ticket9621/trac_9621_simplification.patch) by SimonKing created at 2010-07-30 13:10:22

Replaces the other two patches



---

archive/issue_comments_093197.json:
```json
{
    "body": "Attachment [trac-9621_permgroup_sylow_subgroup_with_simplification.patch](tarball://root/attachments/some-uuid/ticket9621/trac-9621_permgroup_sylow_subgroup_with_simplification.patch) by SimonKing created at 2010-07-30 13:11:55\n\nHi Johan!\n\nReplying to [comment:2 jsrn]:\n> It seems that some parsing functionality has already been built into the gap interface, so all the last lines of sylow_subgroups can be greatly simplified. \n\nYou have a misprint in your patch. You wrote self_element_class(), but it should be self._element_class().\n\nHowever, your suggestion makes indeed sense. So, I created a patch that corrects that misprint and combines both of our patches into one.\n\nNow the big question is: I think we are both Authors now (and I inserted your name in the corresponding field of this ticket). So, who will review??\n\nCheers,\nSimon",
    "created_at": "2010-07-30T13:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93197",
    "user": "SimonKing"
}
```

Attachment [trac-9621_permgroup_sylow_subgroup_with_simplification.patch](tarball://root/attachments/some-uuid/ticket9621/trac-9621_permgroup_sylow_subgroup_with_simplification.patch) by SimonKing created at 2010-07-30 13:11:55

Hi Johan!

Replying to [comment:2 jsrn]:
> It seems that some parsing functionality has already been built into the gap interface, so all the last lines of sylow_subgroups can be greatly simplified. 

You have a misprint in your patch. You wrote self_element_class(), but it should be self._element_class().

However, your suggestion makes indeed sense. So, I created a patch that corrects that misprint and combines both of our patches into one.

Now the big question is: I think we are both Authors now (and I inserted your name in the corresponding field of this ticket). So, who will review??

Cheers,
Simon



---

archive/issue_comments_093198.json:
```json
{
    "body": "Ah, embarrassing; I had seen that mistake, but must have forgotten to remake the patch or something :-) \n\nThanks for adding me as author. I guess we'll have to wait for a nice person to come along and review the (final?) patch.\n\nRegards,\nJohan\n\nReplying to [comment:3 SimonKing]:\n> Hi Johan!\n> \n> Replying to [comment:2 jsrn]:\n> > It seems that some parsing functionality has already been built into the gap interface, so all the last lines of sylow_subgroups can be greatly simplified. \n> \n> You have a misprint in your patch. You wrote self_element_class(), but it should be self._element_class().\n> \n> However, your suggestion makes indeed sense. So, I created a patch that corrects that misprint and combines both of our patches into one.\n> \n> Now the big question is: I think we are both Authors now (and I inserted your name in the corresponding field of this ticket). So, who will review??\n> \n> Cheers,\n> Simon",
    "created_at": "2010-07-30T13:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93198",
    "user": "jsrn"
}
```

Ah, embarrassing; I had seen that mistake, but must have forgotten to remake the patch or something :-) 

Thanks for adding me as author. I guess we'll have to wait for a nice person to come along and review the (final?) patch.

Regards,
Johan

Replying to [comment:3 SimonKing]:
> Hi Johan!
> 
> Replying to [comment:2 jsrn]:
> > It seems that some parsing functionality has already been built into the gap interface, so all the last lines of sylow_subgroups can be greatly simplified. 
> 
> You have a misprint in your patch. You wrote self_element_class(), but it should be self._element_class().
> 
> However, your suggestion makes indeed sense. So, I created a patch that corrects that misprint and combines both of our patches into one.
> 
> Now the big question is: I think we are both Authors now (and I inserted your name in the corresponding field of this ticket). So, who will review??
> 
> Cheers,
> Simon



---

archive/issue_comments_093199.json:
```json
{
    "body": "Apply trac-9621_permgroup_sylow_subgroup_with_simplification.patch\n\n(For the patchbot)\n\nProbably this patch is bit rotting and we need rebasing. But who knows, perhaps we are lucky...",
    "created_at": "2011-03-08T12:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93199",
    "user": "SimonKing"
}
```

Apply trac-9621_permgroup_sylow_subgroup_with_simplification.patch

(For the patchbot)

Probably this patch is bit rotting and we need rebasing. But who knows, perhaps we are lucky...



---

archive/issue_comments_093200.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-11-30T21:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93200",
    "user": "johanbosman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_093201.json:
```json
{
    "body": "Replying to [comment:5 SimonKing]:\n> Apply trac-9621_permgroup_sylow_subgroup_with_simplification.patch\n> \n> (For the patchbot)\n> \n> Probably this patch is bit rotting and we need rebasing. \nIndeed we do. :).",
    "created_at": "2011-11-30T21:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93201",
    "user": "johanbosman"
}
```

Replying to [comment:5 SimonKing]:
> Apply trac-9621_permgroup_sylow_subgroup_with_simplification.patch
> 
> (For the patchbot)
> 
> Probably this patch is bit rotting and we need rebasing. 
Indeed we do. :).



---

archive/issue_comments_093202.json:
```json
{
    "body": "I think this can be closed as I fixed this problem in #10334.",
    "created_at": "2012-05-14T22:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93202",
    "user": "mhansen"
}
```

I think this can be closed as I fixed this problem in #10334.



---

archive/issue_comments_093203.json:
```json
{
    "body": "Replying to [comment:7 mhansen]:\n> I think this can be closed as I fixed this problem in #10334.\n\nOK, I just tested that it works with sage-5.0.rc0. Hence, it is a duplicate (or sub-problem) of #10334.",
    "created_at": "2012-05-15T05:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93203",
    "user": "SimonKing"
}
```

Replying to [comment:7 mhansen]:
> I think this can be closed as I fixed this problem in #10334.

OK, I just tested that it works with sage-5.0.rc0. Hence, it is a duplicate (or sub-problem) of #10334.



---

archive/issue_comments_093204.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-05-15T05:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93204",
    "user": "SimonKing"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_093205.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-05-21T08:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93205",
    "user": "jdemeyer"
}
```

Resolution: duplicate
