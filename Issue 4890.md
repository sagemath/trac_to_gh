# Issue 4890: get rid of nauty's stupid interactive license agreement in the optional spkg install

archive/issues_004890.json:
```json
{
    "body": "Assignee: mabshoff\n\nI hate stuff like this:\n\n\n```\n*     B. D. McKay, nauty User's Guide (Version 2.4),\n*         http://cs.anu.edu.au/~bdm/nauty/.\nDo you accept nauty's license agreement, listed above? (y/n)\n```\n\n\nand as an argument against it note that a _lot_ of stuff in optional isn't gpl compatible, is binary only, etc., but we never have any explicit agreements like the above for anything else. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4890\n\n",
    "created_at": "2008-12-30T07:28:07Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "get rid of nauty's stupid interactive license agreement in the optional spkg install",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4890",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

I hate stuff like this:


```
*     B. D. McKay, nauty User's Guide (Version 2.4),
*         http://cs.anu.edu.au/~bdm/nauty/.
Do you accept nauty's license agreement, listed above? (y/n)
```


and as an argument against it note that a _lot_ of stuff in optional isn't gpl compatible, is binary only, etc., but we never have any explicit agreements like the above for anything else. 

Issue created by migration from https://trac.sagemath.org/ticket/4890





---

archive/issue_comments_037002.json:
```json
{
    "body": "This was done explicitly because Nauty is non-free. I would much rather move non-free stuff to its own repo than to just install it without pointing out the license. \n\nCheers,\n\nMichael",
    "created_at": "2008-12-30T10:52:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4890#issuecomment-37002",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This was done explicitly because Nauty is non-free. I would much rather move non-free stuff to its own repo than to just install it without pointing out the license. 

Cheers,

Michael



---

archive/issue_comments_037003.json:
```json
{
    "body": "Is this in gap_packages* only? If so, would be easiest to simply remove grape?",
    "created_at": "2008-12-30T12:34:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4890#issuecomment-37003",
    "user": "https://github.com/wdjoyner"
}
```

Is this in gap_packages* only? If so, would be easiest to simply remove grape?



---

archive/issue_comments_037004.json:
```json
{
    "body": "Replying to [comment:2 wdj]:\n> Is this in gap_packages* only? If so, would be easiest to simply remove grape?\n\nWhat is \"this\"?\n\nWe are talking about spkg-install of the nauty.spkg.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-30T12:38:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4890#issuecomment-37004",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:2 wdj]:
> Is this in gap_packages* only? If so, would be easiest to simply remove grape?

What is "this"?

We are talking about spkg-install of the nauty.spkg.

Cheers,

Michael



---

archive/issue_comments_037005.json:
```json
{
    "body": "Oh.\n\nI was looking here\nhttp://wiki.sagemath.org/optional_packages_available_for_SAGE\nand not here\nhttp://www.sagemath.org/packages/optional/ \n:-)",
    "created_at": "2008-12-30T13:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4890#issuecomment-37005",
    "user": "https://github.com/wdjoyner"
}
```

Oh.

I was looking here
http://wiki.sagemath.org/optional_packages_available_for_SAGE
and not here
http://www.sagemath.org/packages/optional/ 
:-)



---

archive/issue_comments_037006.json:
```json
{
    "body": "I've put a new spkg here:\n\nhttp://sage.math.washington.edu/home/was/patches/nauty-24b7.p1.spkg\n\nIt does much more than just fix the problem cited in the title of this ticket.  It also:\n\n* Reorganize the spkg to the format we've standardized on.\n* Create Mercurial repository.\n* Make the install process way more robust with much better error checking.\n* Support MAKE environment variable.\n\nTo test it you'll also need to use\n\n```\nexport SAGE_CHECK=1\n```\n\nto have it run its test suite.",
    "created_at": "2008-12-30T18:56:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4890#issuecomment-37006",
    "user": "https://github.com/williamstein"
}
```

I've put a new spkg here:

http://sage.math.washington.edu/home/was/patches/nauty-24b7.p1.spkg

It does much more than just fix the problem cited in the title of this ticket.  It also:

* Reorganize the spkg to the format we've standardized on.
* Create Mercurial repository.
* Make the install process way more robust with much better error checking.
* Support MAKE environment variable.

To test it you'll also need to use

```
export SAGE_CHECK=1
```

to have it run its test suite.



---

archive/issue_comments_037007.json:
```json
{
    "body": "some comments:\n\n1. David Joyner asked about gap, since Nauty is *also* in Gap-packages, so it also gets installed there.  Of course there, there is no stupid interactive message.\n\n2. I know that the reason for the message is because it is not a \"GPL-compatible license\".  However, that can be said for several of the things in optional (gap-packages, openssl, kash3, graphviz), but none of the others have a stupid interactive message.\n\n3. Even Debian doesn't have stupid interactive license agreements.  They have a \"non-free\" repo that every normal user justs adds (it's very easy to add), and henceforth one automatically has those packages available by default.\n\n4. Why distinguish between GPL-compatible and non-GPL-compatible for whether or not we have an interactive message?\n\nEven if we put things in a different repository, it won't in any way effect the user experience, since install_package(...) just queries all repositories.  It will make management of repositories more difficult.  \n\nI view half the point of optional as being a place where we can put non-GPL-compatible code like nauty, but for which it is still very easy for users to install it.",
    "created_at": "2008-12-30T23:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4890#issuecomment-37007",
    "user": "https://github.com/williamstein"
}
```

some comments:

1. David Joyner asked about gap, since Nauty is *also* in Gap-packages, so it also gets installed there.  Of course there, there is no stupid interactive message.

2. I know that the reason for the message is because it is not a "GPL-compatible license".  However, that can be said for several of the things in optional (gap-packages, openssl, kash3, graphviz), but none of the others have a stupid interactive message.

3. Even Debian doesn't have stupid interactive license agreements.  They have a "non-free" repo that every normal user justs adds (it's very easy to add), and henceforth one automatically has those packages available by default.

4. Why distinguish between GPL-compatible and non-GPL-compatible for whether or not we have an interactive message?

Even if we put things in a different repository, it won't in any way effect the user experience, since install_package(...) just queries all repositories.  It will make management of repositories more difficult.  

I view half the point of optional as being a place where we can put non-GPL-compatible code like nauty, but for which it is still very easy for users to install it.



---

archive/issue_comments_037008.json:
```json
{
    "body": "I would still not call this interactive error message \"stupid\" since it was done deliberately. Nauty is not only non-free, but its license prohibits its use for works involving primarily military applications, so this is not about non-GPL vs. GPL. If we also ship it in the optional gap.spkg it looks like we will need to do some auditing there, too.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-30T23:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4890#issuecomment-37008",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I would still not call this interactive error message "stupid" since it was done deliberately. Nauty is not only non-free, but its license prohibits its use for works involving primarily military applications, so this is not about non-GPL vs. GPL. If we also ship it in the optional gap.spkg it looks like we will need to do some auditing there, too.

Cheers,

Michael



---

archive/issue_comments_037009.json:
```json
{
    "body": "> I would still not call this interactive error message \"stupid\" since it was done \n> deliberately. \n\nI think interactive license agreements are annoying.    They are all done deliberately. \n\n> Nauty is not only non-free, but its license prohibits its use for \n> works involving primarily military applications, so this is not about \n> non-GPL vs. GPL. \n\nNauty is free as in beer, but the free license it is under is not \"libre\" i.e., not OSI approved and not GPL-compatible.  Nauty's license is: \"Permission is hereby given for use and/or distribution with the exception of sale for profit or application with nontrivial military significance.\" There are essentially no other restrictions.   \n\nSince we have a fundamental disagreement here, this will need to be discussed on sage-devel and possibly voted on.",
    "created_at": "2009-01-01T03:00:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4890#issuecomment-37009",
    "user": "https://github.com/williamstein"
}
```

> I would still not call this interactive error message "stupid" since it was done 
> deliberately. 

I think interactive license agreements are annoying.    They are all done deliberately. 

> Nauty is not only non-free, but its license prohibits its use for 
> works involving primarily military applications, so this is not about 
> non-GPL vs. GPL. 

Nauty is free as in beer, but the free license it is under is not "libre" i.e., not OSI approved and not GPL-compatible.  Nauty's license is: "Permission is hereby given for use and/or distribution with the exception of sale for profit or application with nontrivial military significance." There are essentially no other restrictions.   

Since we have a fundamental disagreement here, this will need to be discussed on sage-devel and possibly voted on.



---

archive/issue_comments_037010.json:
```json
{
    "body": "I posted a message to sage-devel to start a discussion.  We'll see how it goes.\n\nI made the original spkg.  The result of some good discussion at that time was that an interactive license was needed, so that's what I did.  Personally, I don't care either way; I guess Robert's code has weaned me off of nauty for now.",
    "created_at": "2009-02-03T21:33:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4890#issuecomment-37010",
    "user": "https://github.com/jasongrout"
}
```

I posted a message to sage-devel to start a discussion.  We'll see how it goes.

I made the original spkg.  The result of some good discussion at that time was that an interactive license was needed, so that's what I did.  Personally, I don't care either way; I guess Robert's code has weaned me off of nauty for now.



---

archive/issue_comments_037011.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-03-15T22:57:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4890#issuecomment-37011",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid



---

archive/issue_comments_037012.json:
```json
{
    "body": "I'm closing this as invalid based on the discussion.  The fix should be to remove the nauty spkg entirely, or rename it with \"-nonfree\".",
    "created_at": "2009-03-15T22:57:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4890#issuecomment-37012",
    "user": "https://github.com/williamstein"
}
```

I'm closing this as invalid based on the discussion.  The fix should be to remove the nauty spkg entirely, or rename it with "-nonfree".
