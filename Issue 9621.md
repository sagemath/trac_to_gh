# Issue 9621: Fix GAP interface problem in sylow_subgroup method

archive/issues_009621.json:
```json
{
    "body": "Assignee: joyner\n\nKeywords: GAP string representation\n\nThe following was reported by [Kenny Brown](http://groups.google.com/group/sage-support/browse_thread/thread/9fbca4e4dbadbe37):\n\n```\nsage: n = 3^2 * 7^2\nsage: G = CyclicPermutationGroup(n)\nsage: G.sylow_subgroup(3)\nTraceback (most recent call last):\n...\n```\n\n\nThe problem is that in the sylow_subgroup method, it is attempted to get the string presentation of a permutation in GAP by calling gap.eval(...). However, GAP truncates the output. So, better use gap.eval('Print(...)') instead.\n\nMoreover, the method uses quite generic variable names in the GAP interface. This is dangerous, as the use of variable names that any average user might choose as well can have nasty side effects.\n\nThe attached patch fixes both problems.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9621\n\n",
    "created_at": "2010-07-28T08:18:22Z",
    "labels": [
        "component: group theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Fix GAP interface problem in sylow_subgroup method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9621",
    "user": "https://github.com/simon-king-jena"
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

archive/issue_comments_093037.json:
```json
{
    "body": "Attachment [trac-9621_permgroup_sylow_subgroup.patch](tarball://root/attachments/some-uuid/ticket9621/trac-9621_permgroup_sylow_subgroup.patch) by @simon-king-jena created at 2010-07-28 08:24:11\n\nFixes GAP interface bug of sylow_subgroup method (with doctest)",
    "created_at": "2010-07-28T08:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93037",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [trac-9621_permgroup_sylow_subgroup.patch](tarball://root/attachments/some-uuid/ticket9621/trac-9621_permgroup_sylow_subgroup.patch) by @simon-king-jena created at 2010-07-28 08:24:11

Fixes GAP interface bug of sylow_subgroup method (with doctest)



---

archive/issue_comments_093038.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-28T08:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93038",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093039.json:
```json
{
    "body": "Bear with me as this is my first action on the ticket system :-)\n\nIt seems that some parsing functionality has already been built into the gap interface, so all the last lines of sylow_subgroups can be greatly simplified. I have added an extra patch file for this.",
    "created_at": "2010-07-30T11:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93039",
    "user": "https://github.com/johanrosenkilde"
}
```

Bear with me as this is my first action on the ticket system :-)

It seems that some parsing functionality has already been built into the gap interface, so all the last lines of sylow_subgroups can be greatly simplified. I have added an extra patch file for this.



---

archive/issue_comments_093040.json:
```json
{
    "body": "Simplification of the above patch",
    "created_at": "2010-07-30T11:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93040",
    "user": "https://github.com/johanrosenkilde"
}
```

Simplification of the above patch



---

archive/issue_comments_093041.json:
```json
{
    "body": "Attachment [trac_9621_simplification.patch](tarball://root/attachments/some-uuid/ticket9621/trac_9621_simplification.patch) by @simon-king-jena created at 2010-07-30 13:10:22\n\nReplaces the other two patches",
    "created_at": "2010-07-30T13:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93041",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [trac_9621_simplification.patch](tarball://root/attachments/some-uuid/ticket9621/trac_9621_simplification.patch) by @simon-king-jena created at 2010-07-30 13:10:22

Replaces the other two patches



---

archive/issue_comments_093042.json:
```json
{
    "body": "Attachment [trac-9621_permgroup_sylow_subgroup_with_simplification.patch](tarball://root/attachments/some-uuid/ticket9621/trac-9621_permgroup_sylow_subgroup_with_simplification.patch) by @simon-king-jena created at 2010-07-30 13:11:55\n\nHi Johan!\n\nReplying to [comment:2 jsrn]:\n> It seems that some parsing functionality has already been built into the gap interface, so all the last lines of sylow_subgroups can be greatly simplified. \n\nYou have a misprint in your patch. You wrote self_element_class(), but it should be self._element_class().\n\nHowever, your suggestion makes indeed sense. So, I created a patch that corrects that misprint and combines both of our patches into one.\n\nNow the big question is: I think we are both Authors now (and I inserted your name in the corresponding field of this ticket). So, who will review??\n\nCheers,\nSimon",
    "created_at": "2010-07-30T13:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93042",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [trac-9621_permgroup_sylow_subgroup_with_simplification.patch](tarball://root/attachments/some-uuid/ticket9621/trac-9621_permgroup_sylow_subgroup_with_simplification.patch) by @simon-king-jena created at 2010-07-30 13:11:55

Hi Johan!

Replying to [comment:2 jsrn]:
> It seems that some parsing functionality has already been built into the gap interface, so all the last lines of sylow_subgroups can be greatly simplified. 

You have a misprint in your patch. You wrote self_element_class(), but it should be self._element_class().

However, your suggestion makes indeed sense. So, I created a patch that corrects that misprint and combines both of our patches into one.

Now the big question is: I think we are both Authors now (and I inserted your name in the corresponding field of this ticket). So, who will review??

Cheers,
Simon



---

archive/issue_comments_093043.json:
```json
{
    "body": "Ah, embarrassing; I had seen that mistake, but must have forgotten to remake the patch or something :-) \n\nThanks for adding me as author. I guess we'll have to wait for a nice person to come along and review the (final?) patch.\n\nRegards,\nJohan\n\nReplying to [comment:3 SimonKing]:\n> Hi Johan!\n> \n> Replying to [comment:2 jsrn]:\n> > It seems that some parsing functionality has already been built into the gap interface, so all the last lines of sylow_subgroups can be greatly simplified. \n> \n> You have a misprint in your patch. You wrote self_element_class(), but it should be self._element_class().\n> \n> However, your suggestion makes indeed sense. So, I created a patch that corrects that misprint and combines both of our patches into one.\n> \n> Now the big question is: I think we are both Authors now (and I inserted your name in the corresponding field of this ticket). So, who will review??\n> \n> Cheers,\n> Simon",
    "created_at": "2010-07-30T13:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93043",
    "user": "https://github.com/johanrosenkilde"
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

archive/issue_comments_093044.json:
```json
{
    "body": "Apply trac-9621_permgroup_sylow_subgroup_with_simplification.patch\n\n(For the patchbot)\n\nProbably this patch is bit rotting and we need rebasing. But who knows, perhaps we are lucky...",
    "created_at": "2011-03-08T12:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93044",
    "user": "https://github.com/simon-king-jena"
}
```

Apply trac-9621_permgroup_sylow_subgroup_with_simplification.patch

(For the patchbot)

Probably this patch is bit rotting and we need rebasing. But who knows, perhaps we are lucky...



---

archive/issue_comments_093045.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-11-30T21:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93045",
    "user": "https://trac.sagemath.org/admin/accounts/users/johanbosman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_093046.json:
```json
{
    "body": "Replying to [comment:5 SimonKing]:\n> Apply trac-9621_permgroup_sylow_subgroup_with_simplification.patch\n> \n> (For the patchbot)\n> \n> Probably this patch is bit rotting and we need rebasing. \nIndeed we do. :).",
    "created_at": "2011-11-30T21:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93046",
    "user": "https://trac.sagemath.org/admin/accounts/users/johanbosman"
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

archive/issue_comments_093047.json:
```json
{
    "body": "I think this can be closed as I fixed this problem in #10334.",
    "created_at": "2012-05-14T22:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93047",
    "user": "https://github.com/mwhansen"
}
```

I think this can be closed as I fixed this problem in #10334.



---

archive/issue_comments_093048.json:
```json
{
    "body": "Replying to [comment:7 mhansen]:\n> I think this can be closed as I fixed this problem in #10334.\n\nOK, I just tested that it works with sage-5.0.rc0. Hence, it is a duplicate (or sub-problem) of #10334.",
    "created_at": "2012-05-15T05:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93048",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:7 mhansen]:
> I think this can be closed as I fixed this problem in #10334.

OK, I just tested that it works with sage-5.0.rc0. Hence, it is a duplicate (or sub-problem) of #10334.



---

archive/issue_comments_093049.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-05-15T05:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93049",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_events_023977.json:
```json
{
    "actor": "https://github.com/simon-king-jena",
    "created_at": "2012-05-15T05:20:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9621#event-23977"
}
```



---

archive/issue_comments_093050.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-05-21T08:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9621#issuecomment-93050",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_023978.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-05-21T08:02:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9621",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9621#event-23978"
}
```
