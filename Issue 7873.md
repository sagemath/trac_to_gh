# Issue 7873: Fix 'gap' to remove usage of '$RM' and replace wth 'rm'

archive/issues_007873.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nAs agreed here:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/bd7ae07a1157bead/970aa0dc8fa56ab7?lnk=raot\n\nthere is no need to have variables for very basic commands such as 'rm'. Gap relies on the use of $RM, $LN and $MKDIR, which seems a bit pointless. All are standard Unix commands, defined by POSIX. We should not make make use of any special options some versions might use. \n\nI'm no fan of GNU, but even their coding standards acknowledge one can assume some commands exist, and include all of these. \n\nhttp://www.gnu.org/prep/standards/standards.html#Utilities-in-Makefiles\n\nHence I would replace the use of $LN, $RM and $MKDIR on the spkg-install and anywhere else it may be found in gap. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7873\n\n",
    "created_at": "2010-01-08T18:11:13Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Fix 'gap' to remove usage of '$RM' and replace wth 'rm'",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7873",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: GeorgSWeber

As agreed here:

http://groups.google.com/group/sage-devel/browse_thread/thread/bd7ae07a1157bead/970aa0dc8fa56ab7?lnk=raot

there is no need to have variables for very basic commands such as 'rm'. Gap relies on the use of $RM, $LN and $MKDIR, which seems a bit pointless. All are standard Unix commands, defined by POSIX. We should not make make use of any special options some versions might use. 

I'm no fan of GNU, but even their coding standards acknowledge one can assume some commands exist, and include all of these. 

http://www.gnu.org/prep/standards/standards.html#Utilities-in-Makefiles

Hence I would replace the use of $LN, $RM and $MKDIR on the spkg-install and anywhere else it may be found in gap. 

Issue created by migration from https://trac.sagemath.org/ticket/7873





---

archive/issue_comments_068268.json:
```json
{
    "body": "patch file to replace $RM with 'rm' and similar",
    "created_at": "2010-01-08T20:17:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7873#issuecomment-68268",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

patch file to replace $RM with 'rm' and similar



---

archive/issue_comments_068269.json:
```json
{
    "body": "Attachment [gap-#7873.patch](tarball://root/attachments/some-uuid/ticket7873/gap-#7873.patch) by drkirkby created at 2010-01-08 20:22:42\n\nAt a new spkg, which fixes these can found at \n\nhttp://boxen.math.washington.edu/home/kirkby/portability/gap-4.4.10.p13/gap-4.4.10.p13.spkg\n\n\nDave",
    "created_at": "2010-01-08T20:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7873#issuecomment-68269",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [gap-#7873.patch](tarball://root/attachments/some-uuid/ticket7873/gap-#7873.patch) by drkirkby created at 2010-01-08 20:22:42

At a new spkg, which fixes these can found at 

http://boxen.math.washington.edu/home/kirkby/portability/gap-4.4.10.p13/gap-4.4.10.p13.spkg


Dave



---

archive/issue_comments_068270.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-08T20:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7873#issuecomment-68270",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068271.json:
```json
{
    "body": "Two comments: you've changed \"$CP\" to \"cp\" even though $CP is still defined in sage-env.  Does this matter?\n\nAlso (and this is not new -- it happens with the old spkg, too): when I install the spkg, I get this at the end:\n\n```\ncp: ../../bin is a directory (not copied).\ncp: cp: No such file or directory\n```\n\nAny ideas why?  Anyway, since gap works, maybe we shouldn't worry about this right now.",
    "created_at": "2010-01-08T20:53:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7873#issuecomment-68271",
    "user": "https://github.com/jhpalmieri"
}
```

Two comments: you've changed "$CP" to "cp" even though $CP is still defined in sage-env.  Does this matter?

Also (and this is not new -- it happens with the old spkg, too): when I install the spkg, I get this at the end:

```
cp: ../../bin is a directory (not copied).
cp: cp: No such file or directory
```

Any ideas why?  Anyway, since gap works, maybe we shouldn't worry about this right now.



---

archive/issue_comments_068272.json:
```json
{
    "body": "Replying to [comment:3 jhpalmieri]:\n> Two comments: you've changed \"$CP\" to \"cp\" even though $CP is still defined in sage-env.  Does this matter?\n\nNo. I looked at that before deciding to replace them, but could see no reason not to in this case. One was a simple copy\n\n```\ncp patches/gap_cygwin \"$SAGE_LOCAL\"/bin/gap\n```\n\nthe other was recursive, but simply used the POSIX compatible '-r' option. There seemed to be no reason to use any other version of cp in such cases. \n\nThe GNU verison of 'cp' has some non-POSIX options (-a being one of them). Had that be iused in gap, then I would have left the $CP, but in this case, with only a very standard option used, there is no reason not to use whatever version of 'cp' is in the path first. Any 'cp' will work. \n\n> Also (and this is not new -- it happens with the old spkg, too): when I install the spkg, I get this at the end:\n> {{{\n> cp: ../../bin is a directory (not copied).\n> cp: cp: No such file or directory\n> }}}\n> Any ideas why?  Anyway, since gap works, maybe we shouldn't worry about this right now.\n\nLooking at the 'cp' (or $CP) command I could not work out what spkg-install was trying to do (I just posted something on sage-devel about it). The code simply makes no sense to me. \n\nSince \n* The package functions, despite the errors. \n* I wanted to do it asap, in case it caused an issue with the sage-env ticket (#7818) \n* I could not work out what was the intended behavior. 'cp' is used in a way I'd never use it. \n* There is talk on sage-devel of updating gap\n\nit seemed like it was best left to another day. Like the fact CC and CXX get unset. I think it would be wise to find a way around the issues this creates, but again I did not attempt to fix it. That will certainly present a problem if one tried to use a Sun compiler to build gap. \n\nI'm not even convinced this will work in 64-bit mode on OS X, as it does not have the SAGE64 stuff which every other spkg-install file has. \n\nSo, overall, the changes I made were only necessary ones, and no others. \n\nDave",
    "created_at": "2010-01-08T21:17:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7873#issuecomment-68272",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:3 jhpalmieri]:
> Two comments: you've changed "$CP" to "cp" even though $CP is still defined in sage-env.  Does this matter?

No. I looked at that before deciding to replace them, but could see no reason not to in this case. One was a simple copy

```
cp patches/gap_cygwin "$SAGE_LOCAL"/bin/gap
```

the other was recursive, but simply used the POSIX compatible '-r' option. There seemed to be no reason to use any other version of cp in such cases. 

The GNU verison of 'cp' has some non-POSIX options (-a being one of them). Had that be iused in gap, then I would have left the $CP, but in this case, with only a very standard option used, there is no reason not to use whatever version of 'cp' is in the path first. Any 'cp' will work. 

> Also (and this is not new -- it happens with the old spkg, too): when I install the spkg, I get this at the end:
> {{{
> cp: ../../bin is a directory (not copied).
> cp: cp: No such file or directory
> }}}
> Any ideas why?  Anyway, since gap works, maybe we shouldn't worry about this right now.

Looking at the 'cp' (or $CP) command I could not work out what spkg-install was trying to do (I just posted something on sage-devel about it). The code simply makes no sense to me. 

Since 
* The package functions, despite the errors. 
* I wanted to do it asap, in case it caused an issue with the sage-env ticket (#7818) 
* I could not work out what was the intended behavior. 'cp' is used in a way I'd never use it. 
* There is talk on sage-devel of updating gap

it seemed like it was best left to another day. Like the fact CC and CXX get unset. I think it would be wise to find a way around the issues this creates, but again I did not attempt to fix it. That will certainly present a problem if one tried to use a Sun compiler to build gap. 

I'm not even convinced this will work in 64-bit mode on OS X, as it does not have the SAGE64 stuff which every other spkg-install file has. 

So, overall, the changes I made were only necessary ones, and no others. 

Dave



---

archive/issue_comments_068273.json:
```json
{
    "body": "It works for me on OS X 10.6, and the changes are obviously the right ones to make.  Positive review.",
    "created_at": "2010-01-08T21:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7873#issuecomment-68273",
    "user": "https://github.com/jhpalmieri"
}
```

It works for me on OS X 10.6, and the changes are obviously the right ones to make.  Positive review.



---

archive/issue_comments_068274.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-08T21:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7873#issuecomment-68274",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068275.json:
```json
{
    "body": "Thank you very much for the positive review.",
    "created_at": "2010-01-08T22:39:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7873#issuecomment-68275",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Thank you very much for the positive review.



---

archive/issue_events_008088.json:
```json
{
    "actor": "@rlmill",
    "created_at": "2010-01-14T02:39:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7873",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7873#event-8088"
}
```



---

archive/issue_comments_068276.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-14T02:39:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7873#issuecomment-68276",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
