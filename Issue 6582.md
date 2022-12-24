# Issue 6582: Potential issue in polybori - 0.5rc.p8 and/or  0.5rc.p9

archive/issues_006582.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  alexanderdreyer polybori david.kirkby@onetel.net\n\nI believe there is an issue which *may* affect Solaris with polybori 0.5rc.p8, and assuming my patch to .p9 gets positive review, will affect that too, as I have not tried to fix this. \n\nHere are some notes I put in patches/custom.py\n\n\n\n```\n# Note, these 'SAGE_DEBUG' linker flags added by someone\n# are likely to break if used on Solaris\n# with the Sun linker, as -p option to the Sun linker is:\n#         [-p auditlib]   identify audit library to accompany this object\n# This has not been confirmed, and I don't have time to test it.\n# David Kirkby, 21st July 2009. I suggest this is revisited by someone soon.\nif os.environ.has_key('SAGE_DEBUG'):\n    CPPDEFINES=[]\n    CCFLAGS=[\" -pg\"] + CCFLAGS\n    CXXFLAGS=[\" -pg\"] + CXXFLAGS\n    LINKFLAGS=[\" -pg\"]\n\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6582\n\n",
    "created_at": "2009-07-21T18:55:35Z",
    "labels": [
        "porting: Solaris",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Potential issue in polybori - 0.5rc.p8 and/or  0.5rc.p9",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6582",
    "user": "drkirkby"
}
```
Assignee: tbd

CC:  alexanderdreyer polybori david.kirkby@onetel.net

I believe there is an issue which *may* affect Solaris with polybori 0.5rc.p8, and assuming my patch to .p9 gets positive review, will affect that too, as I have not tried to fix this. 

Here are some notes I put in patches/custom.py



```
# Note, these 'SAGE_DEBUG' linker flags added by someone
# are likely to break if used on Solaris
# with the Sun linker, as -p option to the Sun linker is:
#         [-p auditlib]   identify audit library to accompany this object
# This has not been confirmed, and I don't have time to test it.
# David Kirkby, 21st July 2009. I suggest this is revisited by someone soon.
if os.environ.has_key('SAGE_DEBUG'):
    CPPDEFINES=[]
    CCFLAGS=[" -pg"] + CCFLAGS
    CXXFLAGS=[" -pg"] + CXXFLAGS
    LINKFLAGS=[" -pg"]


```


Issue created by migration from https://trac.sagemath.org/ticket/6582





---

archive/issue_comments_053761.json:
```json
{
    "body": "Another issue, which is this case I am 100% sure about, is that PolyBoRi (as of polybori-0.6.3-20090827.spkg) in sage-4.1.2.alpha4 is that PolyBoRi is sending GNU-specific options to the Sun compiler. See #7034",
    "created_at": "2009-09-28T09:33:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6582#issuecomment-53761",
    "user": "drkirkby"
}
```

Another issue, which is this case I am 100% sure about, is that PolyBoRi (as of polybori-0.6.3-20090827.spkg) in sage-4.1.2.alpha4 is that PolyBoRi is sending GNU-specific options to the Sun compiler. See #7034



---

archive/issue_comments_053762.json:
```json
{
    "body": "Is this still a problem?",
    "created_at": "2012-04-30T10:10:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6582#issuecomment-53762",
    "user": "jdemeyer"
}
```

Is this still a problem?



---

archive/issue_comments_053763.json:
```json
{
    "body": "No, it was fixed. For instance, in #12655 for PolyBoRi 0.8.1.",
    "created_at": "2012-04-30T10:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6582#issuecomment-53763",
    "user": "AlexanderDreyer"
}
```

No, it was fixed. For instance, in #12655 for PolyBoRi 0.8.1.



---

archive/issue_comments_053764.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-06-25T09:29:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6582#issuecomment-53764",
    "user": "AlexanderDreyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_053765.json:
```json
{
    "body": "Duplicate of#12655.",
    "created_at": "2012-06-25T09:29:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6582#issuecomment-53765",
    "user": "AlexanderDreyer"
}
```

Duplicate of#12655.



---

archive/issue_comments_053766.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-06-25T09:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6582#issuecomment-53766",
    "user": "AlexanderDreyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053767.json:
```json
{
    "body": "Abusing \"positive review\".",
    "created_at": "2012-06-25T09:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6582#issuecomment-53767",
    "user": "AlexanderDreyer"
}
```

Abusing "positive review".



---

archive/issue_comments_053768.json:
```json
{
    "body": "In such cases, you should set the milestone to \"sage-duplicate/invalid/wontfix\".",
    "created_at": "2012-06-25T09:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6582#issuecomment-53768",
    "user": "jdemeyer"
}
```

In such cases, you should set the milestone to "sage-duplicate/invalid/wontfix".



---

archive/issue_comments_053769.json:
```json
{
    "body": "Replying to [comment:7 jdemeyer]:\n> In such cases, you should set the milestone to \"sage-duplicate/invalid/wontfix\".\nThanks, I'll do so next time.",
    "created_at": "2012-06-25T09:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6582#issuecomment-53769",
    "user": "AlexanderDreyer"
}
```

Replying to [comment:7 jdemeyer]:
> In such cases, you should set the milestone to "sage-duplicate/invalid/wontfix".
Thanks, I'll do so next time.



---

archive/issue_comments_053770.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-07-04T07:16:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6582#issuecomment-53770",
    "user": "jdemeyer"
}
```

Resolution: duplicate
