# Issue 8903: update pynac to 0.2.0

archive/issues_008903.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @mwhansen\n\nKeywords: pynac\n\nA new pynac package with several critical fixes is available here:\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg\n\nIt contains fixes for:\n\n* #8542: function table for Cygwin\n* #8651: binomial(n, 0) -> 1\n* #8688: extra parenthesis when typesetting fractions\n* #8775: auto evaluation of conjugates\n\nNote that patches from the above tickets need to be applied to test this ticket. Without #8542, you'll get a segfault. The others fix doctests.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8903\n\n",
    "created_at": "2010-05-06T04:08:57Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "update pynac to 0.2.0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8903",
    "user": "https://github.com/burcin"
}
```
Assignee: tbd

CC:  @mwhansen

Keywords: pynac

A new pynac package with several critical fixes is available here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg

It contains fixes for:

* #8542: function table for Cygwin
* #8651: binomial(n, 0) -> 1
* #8688: extra parenthesis when typesetting fractions
* #8775: auto evaluation of conjugates

Note that patches from the above tickets need to be applied to test this ticket. Without #8542, you'll get a segfault. The others fix doctests.

Issue created by migration from https://trac.sagemath.org/ticket/8903





---

archive/issue_comments_081815.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-06T04:32:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8903#issuecomment-81815",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081816.json:
```json
{
    "body": "This package depends on the Python package at #8907.",
    "created_at": "2010-05-06T18:04:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8903#issuecomment-81816",
    "user": "https://github.com/burcin"
}
```

This package depends on the Python package at #8907.



---

archive/issue_comments_081817.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-23T15:10:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8903#issuecomment-81817",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_081818.json:
```json
{
    "body": "The last patch for conjugates and power simplification included in this pynac version breaks doctests in `sage/rings/qqbar.py` and a bunch of other places.\n\nI suppose the fix will involve looking into the `power_helper` in detail, hopefully fixing #8959 on the way. I won't have time for this at least for a week though.\n\nIf anybody is interested in working on the cygwin port, I can prepare a package which includes only the patches relevant for that in the mean time.",
    "created_at": "2010-05-23T15:10:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8903#issuecomment-81818",
    "user": "https://github.com/burcin"
}
```

The last patch for conjugates and power simplification included in this pynac version breaks doctests in `sage/rings/qqbar.py` and a bunch of other places.

I suppose the fix will involve looking into the `power_helper` in detail, hopefully fixing #8959 on the way. I won't have time for this at least for a week though.

If anybody is interested in working on the cygwin port, I can prepare a package which includes only the patches relevant for that in the mean time.



---

archive/issue_comments_081819.json:
```json
{
    "body": "I've put a new spkg up at http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg .  This just has a simple fix for #9307.",
    "created_at": "2010-05-25T22:19:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8903#issuecomment-81819",
    "user": "https://github.com/mwhansen"
}
```

I've put a new spkg up at http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg .  This just has a simple fix for #9307.



---

archive/issue_comments_081820.json:
```json
{
    "body": "err, #8907",
    "created_at": "2010-05-25T22:19:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8903#issuecomment-81820",
    "user": "https://github.com/mwhansen"
}
```

err, #8907



---

archive/issue_comments_081821.json:
```json
{
    "body": "Third time is the charm: #9037",
    "created_at": "2010-05-25T22:20:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8903#issuecomment-81821",
    "user": "https://github.com/mwhansen"
}
```

Third time is the charm: #9037



---

archive/issue_comments_081822.json:
```json
{
    "body": "I've made a new spkg at  http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg which just backs out the commit which adds \"auto evaluation of conjugates\".  All tests in qqbar pass.  We can add the auto evaluation of conjugates in 0.2.1.",
    "created_at": "2010-05-26T02:19:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8903#issuecomment-81822",
    "user": "https://github.com/mwhansen"
}
```

I've made a new spkg at  http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg which just backs out the commit which adds "auto evaluation of conjugates".  All tests in qqbar pass.  We can add the auto evaluation of conjugates in 0.2.1.



---

archive/issue_events_021724.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-05-28T19:32:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8903",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8903#event-21724"
}
```



---

archive/issue_comments_081823.json:
```json
{
    "body": "I merged in   http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg",
    "created_at": "2010-05-28T19:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8903#issuecomment-81823",
    "user": "https://github.com/williamstein"
}
```

I merged in   http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg



---

archive/issue_comments_081824.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-28T19:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8903#issuecomment-81824",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_081825.json:
```json
{
    "body": "Despite Mike's comments on #9037, this does not resolve the issue there, as it still has:\n\n```\nif [ `uname` = \"Darwin\" -a \"$SAGE64\" = \"yes\" ]; then\n    echo \"64 bit MacIntel\"\n    CXXFLAGS=\"-m64 -O2 -g\"; export CXXFLAGS\n    LDFLAGS=\"-m64\"; export LDFLAGS\nfi\n```\n\nI'll have to create a new package based on this one and apply the fix again. \n\nDave",
    "created_at": "2010-05-30T12:06:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8903#issuecomment-81825",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Despite Mike's comments on #9037, this does not resolve the issue there, as it still has:

```
if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
    echo "64 bit MacIntel"
    CXXFLAGS="-m64 -O2 -g"; export CXXFLAGS
    LDFLAGS="-m64"; export LDFLAGS
fi
```

I'll have to create a new package based on this one and apply the fix again. 

Dave



---

archive/issue_comments_081826.json:
```json
{
    "body": "Hi Dave,\n\nWhich package are you looking at. Unfortunately, there are several packages named pynac-0.2.0.spkg floating around. My version at\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg\n\ndoesn't have the said fix, but Mike's version at \n\nhttp://sage.math.washington.edu/home/mhansen/pynac-0.2.0.spkg\n\nmight do. I believe the version included in the release is the latter.",
    "created_at": "2010-05-30T12:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8903#issuecomment-81826",
    "user": "https://github.com/burcin"
}
```

Hi Dave,

Which package are you looking at. Unfortunately, there are several packages named pynac-0.2.0.spkg floating around. My version at

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg

doesn't have the said fix, but Mike's version at 

http://sage.math.washington.edu/home/mhansen/pynac-0.2.0.spkg

might do. I believe the version included in the release is the latter.



---

archive/issue_comments_081827.json:
```json
{
    "body": "Replying to [comment:12 burcin]:\n> Hi Dave,\n> \n> Which package are you looking at. Unfortunately, there are several packages named pynac-0.2.0.spkg floating around. My version at\n> \n> http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg\n> \n> doesn't have the said fix, but Mike's version at \n> \n> http://sage.math.washington.edu/home/mhansen/pynac-0.2.0.spkg\n> \n> might do. I believe the version included in the release is the latter.\n\n\nI often wish there was a central repository, as having different versions and constant rebasing does get a bit annoying. \n\nMike's version at http://sage.math.washington.edu/home/mhansen/pynac-0.2.0.spkg does have the fix, but the only version mentioned on this trac ticket was yours at http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg which does not have the fix. The comment from William was \n\n\"I merged in  http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg\"\n\nso I can only assume your version, and not Mikes is merged. \n\nActually, it appears changing\n\n```\nif [ `uname` = \"Darwin\" -a \"$SAGE64\" = \"yes\" ]; then\n```\nto \n\n```\nif [ \"$SAGE64\" = \"yes\" ]; then\n```\n\n(as in Mike's version), does not fully solve the 64-bit build issue on OpenSolaris. However, it is certainly a desirable change, so if you make any more changes to pynac, can you change that one line. \n\nIn the mean time, I'll work on trying to resolve why that is not a complete fix for the 64-bit OpenSolaris issue, but it is certainly a necessary change. \n\nDave",
    "created_at": "2010-05-30T12:53:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8903#issuecomment-81827",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:12 burcin]:
> Hi Dave,
> 
> Which package are you looking at. Unfortunately, there are several packages named pynac-0.2.0.spkg floating around. My version at
> 
> http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg
> 
> doesn't have the said fix, but Mike's version at 
> 
> http://sage.math.washington.edu/home/mhansen/pynac-0.2.0.spkg
> 
> might do. I believe the version included in the release is the latter.


I often wish there was a central repository, as having different versions and constant rebasing does get a bit annoying. 

Mike's version at http://sage.math.washington.edu/home/mhansen/pynac-0.2.0.spkg does have the fix, but the only version mentioned on this trac ticket was yours at http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg which does not have the fix. The comment from William was 

"I merged in  http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg"

so I can only assume your version, and not Mikes is merged. 

Actually, it appears changing

```
if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
```
to 

```
if [ "$SAGE64" = "yes" ]; then
```

(as in Mike's version), does not fully solve the 64-bit build issue on OpenSolaris. However, it is certainly a desirable change, so if you make any more changes to pynac, can you change that one line. 

In the mean time, I'll work on trying to resolve why that is not a complete fix for the 64-bit OpenSolaris issue, but it is certainly a necessary change. 

Dave



---

archive/issue_comments_081828.json:
```json
{
    "body": "I'll make sure that mine is the one in 4.4.3.alpha1.",
    "created_at": "2010-05-30T18:16:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8903#issuecomment-81828",
    "user": "https://github.com/mwhansen"
}
```

I'll make sure that mine is the one in 4.4.3.alpha1.



---

archive/issue_comments_081829.json:
```json
{
    "body": "Replying to [comment:14 mhansen]:\n> I'll make sure that mine is the one in 4.4.3.alpha1.\n\n\nThe ticket says Burchin's package has already been merged in sage-4.4.3.alpha1 - whether it is possible to reverse that easily I don't know. \n\nDave",
    "created_at": "2010-05-30T18:48:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8903",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8903#issuecomment-81829",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:14 mhansen]:
> I'll make sure that mine is the one in 4.4.3.alpha1.


The ticket says Burchin's package has already been merged in sage-4.4.3.alpha1 - whether it is possible to reverse that easily I don't know. 

Dave
