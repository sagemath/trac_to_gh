# Issue 2339: xmin/xmax now broken in plot()

archive/issues_002339.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  bober mhampton @kcrisman\n\n```\nr(t) = 1000 * t * e^(-.5 * t)\nplot(r, xmin=0, xmax=20).show()\n```\n\ndoesn't work. But\n\n```\nplot(r, (0,20)).show()\n```\ndoes. The documentation still says\n\n```\n    PLOT OPTIONS:\n    The plot options are\n    [...]\n        xmin -- starting x value\n        xmax -- ending x value\n    [...]\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2339\n\n",
    "created_at": "2008-02-28T02:36:46Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "xmin/xmax now broken in plot()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2339",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```
Assignee: @williamstein

CC:  bober mhampton @kcrisman

```
r(t) = 1000 * t * e^(-.5 * t)
plot(r, xmin=0, xmax=20).show()
```

doesn't work. But

```
plot(r, (0,20)).show()
```
does. The documentation still says

```
    PLOT OPTIONS:
    The plot options are
    [...]
        xmin -- starting x value
        xmax -- ending x value
    [...]
```

Issue created by migration from https://trac.sagemath.org/ticket/2339





---

archive/issue_comments_015601.json:
```json
{
    "body": "This is still broken in Sage 3.0.alpha1.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-05T00:17:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15601",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is still broken in Sage 3.0.alpha1.

Cheers,

Michael



---

archive/issue_comments_015602.json:
```json
{
    "body": "Changing assignee from @williamstein to mhampton.",
    "created_at": "2008-05-17T18:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15602",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing assignee from @williamstein to mhampton.



---

archive/issue_comments_015603.json:
```json
{
    "body": "Changing keywords from \"\" to \"plot, xmin, xmax\".",
    "created_at": "2008-05-17T20:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15603",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing keywords from "" to "plot, xmin, xmax".



---

archive/issue_comments_015604.json:
```json
{
    "body": "Changing assignee from mhampton to somebody.",
    "created_at": "2008-05-17T20:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15604",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing assignee from mhampton to somebody.



---

archive/issue_comments_015605.json:
```json
{
    "body": "In addition to fixing this problem, I also enforced the xmin, xmax that are given if they are inside [-1,1].",
    "created_at": "2008-05-17T20:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15605",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

In addition to fixing this problem, I also enforced the xmin, xmax that are given if they are inside [-1,1].



---

archive/issue_comments_015606.json:
```json
{
    "body": "should fix the problem",
    "created_at": "2008-05-17T20:33:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15606",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

should fix the problem



---

archive/issue_comments_015607.json:
```json
{
    "body": "Attachment [trac_2339_try1.patch](tarball://root/attachments/some-uuid/ticket2339/trac_2339_try1.patch) by @jhpalmieri created at 2008-06-11 23:58:20\n\nLooks okay to me, although I don't understand the purpose of the change from\n\n```\nG = Graphics() \nfor i in range(0, len(funcs)): \n```\n\nto\n\n```\nG = plot(funcs[0], (xmin, xmax), polar=polar, **kwds) \nfor i in range(1, len(funcs)): \n```",
    "created_at": "2008-06-11T23:58:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15607",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_2339_try1.patch](tarball://root/attachments/some-uuid/ticket2339/trac_2339_try1.patch) by @jhpalmieri created at 2008-06-11 23:58:20

Looks okay to me, although I don't understand the purpose of the change from

```
G = Graphics() 
for i in range(0, len(funcs)): 
```

to

```
G = plot(funcs[0], (xmin, xmax), polar=polar, **kwds) 
for i in range(1, len(funcs)): 
```



---

archive/issue_comments_015608.json:
```json
{
    "body": "The purpose of that change was: I was trying to avoid the xmin of the output being set to -1 if the argument xmin was greater than that.  If you initialize something as Graphics(), xmin is set to -1. \n\nThere is probably a better systematic way of solving that problem but I don't have it in hand.",
    "created_at": "2008-06-12T11:59:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15608",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

The purpose of that change was: I was trying to avoid the xmin of the output being set to -1 if the argument xmin was greater than that.  If you initialize something as Graphics(), xmin is set to -1. 

There is probably a better systematic way of solving that problem but I don't have it in hand.



---

archive/issue_comments_015609.json:
```json
{
    "body": "Hm. If I do:\n\n```\nsage: r(t) = 1000 * t * e^(-0.5*t)\nsage: plot(r, xmin=10, xmax=20).show()\n```\nor (to make sure I didn't misunderstand \"greater than\" -1):\n\n```\nsage: r(t) = 1000 * t * e^(-0.5*t)\nsage: plot(r, xmin=-2, xmax=20).show()\n```\nthen I seem to get the same behavior with or without this particular change in the code.\n\nI have two more questions: what should the following do?\n\n```\nplot (r, xmin=10, xmax=-2).show()\n```\nIt should probably print an error (since xmin > xmax), but right now I get a graph which is a bad approximation to \n\n```\nplot (r, xmin=-2, xmax=10).show()\n```\nIt's actually pretty strange looking...\n\nAlso, do you have any idea why, if I do\n\n```\nplot (r, xmin=5, xmax=20).show()\n```\nthen the vertical axis is the line x=5, not x=0?  When xmin is positive, I seem to get x=xmin as the vertical axis, which looks strange to me.  I guess the same happens if both xmin and xmax are negative: then x=xmax is drawn as the vertical axis.  (This is probably a completely separate issue, but I thought I'd ask.)",
    "created_at": "2008-06-12T15:03:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15609",
    "user": "https://github.com/jhpalmieri"
}
```

Hm. If I do:

```
sage: r(t) = 1000 * t * e^(-0.5*t)
sage: plot(r, xmin=10, xmax=20).show()
```
or (to make sure I didn't misunderstand "greater than" -1):

```
sage: r(t) = 1000 * t * e^(-0.5*t)
sage: plot(r, xmin=-2, xmax=20).show()
```
then I seem to get the same behavior with or without this particular change in the code.

I have two more questions: what should the following do?

```
plot (r, xmin=10, xmax=-2).show()
```
It should probably print an error (since xmin > xmax), but right now I get a graph which is a bad approximation to 

```
plot (r, xmin=-2, xmax=10).show()
```
It's actually pretty strange looking...

Also, do you have any idea why, if I do

```
plot (r, xmin=5, xmax=20).show()
```
then the vertical axis is the line x=5, not x=0?  When xmin is positive, I seem to get x=xmin as the vertical axis, which looks strange to me.  I guess the same happens if both xmin and xmax are negative: then x=xmax is drawn as the vertical axis.  (This is probably a completely separate issue, but I thought I'd ask.)



---

archive/issue_comments_015610.json:
```json
{
    "body": "Changing keywords from \"plot, xmin, xmax\" to \"plot, xmin, xmax, editor_gfurnish\".",
    "created_at": "2008-06-20T04:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15610",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "plot, xmin, xmax" to "plot, xmin, xmax, editor_gfurnish".



---

archive/issue_comments_015611.json:
```json
{
    "body": "This seems correct except for an error check, can we get a patch?",
    "created_at": "2008-06-20T06:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15611",
    "user": "https://github.com/garyfurnish"
}
```

This seems correct except for an error check, can we get a patch?



---

archive/issue_comments_015612.json:
```json
{
    "body": "Here's a new version of the patch.  This (I hope) takes the arguments called xmin and xmax, and sets xmin to be the smaller of the two, xmax to be the larger.  This should fix the strange plots that commands like\n\n```\nplot (r, xmin=10, xmax=-2).show()\n```\nwere giving, as I mentioned above.",
    "created_at": "2008-07-08T19:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15612",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a new version of the patch.  This (I hope) takes the arguments called xmin and xmax, and sets xmin to be the smaller of the two, xmax to be the larger.  This should fix the strange plots that commands like

```
plot (r, xmin=10, xmax=-2).show()
```
were giving, as I mentioned above.



---

archive/issue_comments_015613.json:
```json
{
    "body": "new version of 2399 patch, fixing problem when xmin > xmax",
    "created_at": "2008-07-08T19:13:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15613",
    "user": "https://github.com/jhpalmieri"
}
```

new version of 2399 patch, fixing problem when xmin > xmax



---

archive/issue_comments_015614.json:
```json
{
    "body": "Attachment [2339-new.patch](tarball://root/attachments/some-uuid/ticket2339/2339-new.patch) by @jhpalmieri created at 2008-07-08 19:17:19\n\nBy the way, my patch supersedes Marshall's, but he should get credit for most of the work.  (Is it better to have one patch, for easier installation, or two, to make sure the right people get credit for their work?)\n\nOne question: in my patch, as I described, if you call plot with arguments xmin=10 and xmax=0, then the plot gets drawn between x=0 and x=10, with no error message.  Is this the best behavior, or should an exception be raised instead?",
    "created_at": "2008-07-08T19:17:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15614",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [2339-new.patch](tarball://root/attachments/some-uuid/ticket2339/2339-new.patch) by @jhpalmieri created at 2008-07-08 19:17:19

By the way, my patch supersedes Marshall's, but he should get credit for most of the work.  (Is it better to have one patch, for easier installation, or two, to make sure the right people get credit for their work?)

One question: in my patch, as I described, if you call plot with arguments xmin=10 and xmax=0, then the plot gets drawn between x=0 and x=10, with no error message.  Is this the best behavior, or should an exception be raised instead?



---

archive/issue_comments_015615.json:
```json
{
    "body": "I thought about that issue a bit (xmin > xmax), and I think the lack of an error message is OK. Thanks for working on this more, I am really swamped with other stuff at the moment.",
    "created_at": "2008-07-08T23:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15615",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I thought about that issue a bit (xmin > xmax), and I think the lack of an error message is OK. Thanks for working on this more, I am really swamped with other stuff at the moment.



---

archive/issue_comments_015616.json:
```json
{
    "body": "Can I give a positive review to mhampton's contribution, and vice versa?",
    "created_at": "2008-07-16T01:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15616",
    "user": "https://github.com/jhpalmieri"
}
```

Can I give a positive review to mhampton's contribution, and vice versa?



---

archive/issue_comments_015617.json:
```json
{
    "body": "Replying to [comment:13 jhpalmieri]:\n> Can I give a positive review to mhampton's contribution, and vice versa?\n> \n\n\nYes, that is perfectly fine.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-16T01:21:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15617",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:13 jhpalmieri]:
> Can I give a positive review to mhampton's contribution, and vice versa?
> 


Yes, that is perfectly fine.

Cheers,

Michael



---

archive/issue_comments_015618.json:
```json
{
    "body": "My apologies, I should have positively reviewed this before.  Now I think the patch has to be rebased.  I will try to do that.",
    "created_at": "2008-08-24T15:53:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15618",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

My apologies, I should have positively reviewed this before.  Now I think the patch has to be rebased.  I will try to do that.



---

archive/issue_comments_015619.json:
```json
{
    "body": "File 2339-3.2.alpha0.patch is rebased patch against 3.2.alpha0.   As JHP says, please give credit to Marshall.\n\nInterestingly, all the plot improvements as of late have already fixed both the Graphics initialization problem of [-1,1] and the problem if you get the range in backwards, i.e. all of the following work with this patch:\n\n```\nplot(r, xmin=10, xmax=-2).show()\nplot(r, 10,-2).show()\nplot(r, (10,-2)).show()\n```",
    "created_at": "2008-10-21T18:19:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15619",
    "user": "https://github.com/kcrisman"
}
```

File 2339-3.2.alpha0.patch is rebased patch against 3.2.alpha0.   As JHP says, please give credit to Marshall.

Interestingly, all the plot improvements as of late have already fixed both the Graphics initialization problem of [-1,1] and the problem if you get the range in backwards, i.e. all of the following work with this patch:

```
plot(r, xmin=10, xmax=-2).show()
plot(r, 10,-2).show()
plot(r, (10,-2)).show()
```



---

archive/issue_comments_015620.json:
```json
{
    "body": "Rebased to 3.2.alpha0",
    "created_at": "2008-10-21T18:20:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15620",
    "user": "https://github.com/kcrisman"
}
```

Rebased to 3.2.alpha0



---

archive/issue_comments_015621.json:
```json
{
    "body": "Attachment [2339-3.2.alpha0.patch](tarball://root/attachments/some-uuid/ticket2339/2339-3.2.alpha0.patch) by mhampton created at 2008-10-22 19:23:19\n\nThis is a simple change that seems to solve the problem, positive review.",
    "created_at": "2008-10-22T19:23:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15621",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [2339-3.2.alpha0.patch](tarball://root/attachments/some-uuid/ticket2339/2339-3.2.alpha0.patch) by mhampton created at 2008-10-22 19:23:19

This is a simple change that seems to solve the problem, positive review.



---

archive/issue_comments_015622.json:
```json
{
    "body": "By the way, thanks Karl, this had fallen off my radar.",
    "created_at": "2008-10-22T19:27:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15622",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

By the way, thanks Karl, this had fallen off my radar.



---

archive/issue_comments_015623.json:
```json
{
    "body": "No problem; during the school year I don't have much time for new stuff, but I figure I can help out in this way at least!",
    "created_at": "2008-10-23T00:10:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15623",
    "user": "https://github.com/kcrisman"
}
```

No problem; during the school year I don't have much time for new stuff, but I figure I can help out in this way at least!



---

archive/issue_comments_015624.json:
```json
{
    "body": "Merged 2339-3.2.alpha0.patch only in Sage 3.2.alpha1",
    "created_at": "2008-10-26T03:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15624",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 2339-3.2.alpha0.patch only in Sage 3.2.alpha1



---

archive/issue_comments_015625.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-26T03:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2339#issuecomment-15625",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005523.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-26T03:18:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2339",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2339#event-5523"
}
```
