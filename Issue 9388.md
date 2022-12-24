# Issue 9388: Fix rubiks makefile

archive/issues_009388.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  rlm\n\nThe current makefile for the rubiks spkg.\n\nThe makefile erroneously assumes that \"mktemp\" can be run with no arguments.  This is not the case on, at least, recent versions of Mac OS X.\n\nThe probable fix is to run \"mktemp\" with a template filename.  See the man page for details.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9388\n\n",
    "created_at": "2010-06-30T00:53:16Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Fix rubiks makefile",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9388",
    "user": "justin"
}
```
Assignee: GeorgSWeber

CC:  rlm

The current makefile for the rubiks spkg.

The makefile erroneously assumes that "mktemp" can be run with no arguments.  This is not the case on, at least, recent versions of Mac OS X.

The probable fix is to run "mktemp" with a template filename.  See the man page for details.


Issue created by migration from https://trac.sagemath.org/ticket/9388





---

archive/issue_comments_089355.json:
```json
{
    "body": "Attachment [9388.patch](tarball://root/attachments/some-uuid/ticket9388/9388.patch) by justin created at 2010-06-30 03:57:11\n\nPatch for rubiks' \"spkg-install\" script",
    "created_at": "2010-06-30T03:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9388#issuecomment-89355",
    "user": "justin"
}
```

Attachment [9388.patch](tarball://root/attachments/some-uuid/ticket9388/9388.patch) by justin created at 2010-06-30 03:57:11

Patch for rubiks' "spkg-install" script



---

archive/issue_comments_089356.json:
```json
{
    "body": "Updated spkg (new \"spkg-install\")",
    "created_at": "2010-06-30T03:59:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9388#issuecomment-89356",
    "user": "justin"
}
```

Updated spkg (new "spkg-install")



---

archive/issue_comments_089357.json:
```json
{
    "body": "Attachment [rubiks-20070912.p12.spkg](tarball://root/attachments/some-uuid/ticket9388/rubiks-20070912.p12.spkg) by justin created at 2010-06-30 04:01:04\n\nThe patch file is just the fix for the file \"spkg-install\".  The \"spkg\" is a new spkg file with the changed \"spkg-install\" script.",
    "created_at": "2010-06-30T04:01:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9388#issuecomment-89357",
    "user": "justin"
}
```

Attachment [rubiks-20070912.p12.spkg](tarball://root/attachments/some-uuid/ticket9388/rubiks-20070912.p12.spkg) by justin created at 2010-06-30 04:01:04

The patch file is just the fix for the file "spkg-install".  The "spkg" is a new spkg file with the changed "spkg-install" script.



---

archive/issue_comments_089358.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-30T04:05:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9388#issuecomment-89358",
    "user": "justin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089359.json:
```json
{
    "body": "Hi Jason, \nthere's a few problems with this. \n* There's no SPKG.txt entry to show what was changed. \n* Patches should not be attached to the trac server, but instead given to a location where they can be found. \n* Having looked into this more, 'mktemp' is not defined by POSIX so is not portable. We might find this screws up the FreeBSD port. \n\nI'll create another which avoid using it completely. \n\nGive me 15 minutes. \n\nDave",
    "created_at": "2010-06-30T10:50:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9388#issuecomment-89359",
    "user": "drkirkby"
}
```

Hi Jason, 
there's a few problems with this. 
* There's no SPKG.txt entry to show what was changed. 
* Patches should not be attached to the trac server, but instead given to a location where they can be found. 
* Having looked into this more, 'mktemp' is not defined by POSIX so is not portable. We might find this screws up the FreeBSD port. 

I'll create another which avoid using it completely. 

Give me 15 minutes. 

Dave



---

archive/issue_comments_089360.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-30T10:50:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9388#issuecomment-89360",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089361.json:
```json
{
    "body": "Sorry, Justin, not Jason. \n\nA portable fix is coming up very soon. \n\nDave",
    "created_at": "2010-06-30T10:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9388#issuecomment-89361",
    "user": "drkirkby"
}
```

Sorry, Justin, not Jason. 

A portable fix is coming up very soon. 

Dave



---

archive/issue_comments_089362.json:
```json
{
    "body": "Here's a link to the next package, which has an updated SPKG.txt file and avoids the use of mktemp at all. \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/rubiks-20070912.p12.spkg",
    "created_at": "2010-06-30T11:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9388#issuecomment-89362",
    "user": "drkirkby"
}
```

Here's a link to the next package, which has an updated SPKG.txt file and avoids the use of mktemp at all. 

http://boxen.math.washington.edu/home/kirkby/patches/rubiks-20070912.p12.spkg



---

archive/issue_comments_089363.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-30T11:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9388#issuecomment-89363",
    "user": "drkirkby"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089364.json:
```json
{
    "body": "Mercurial patch which fully solves the rubiks makefile problem using only POSIX commands.",
    "created_at": "2010-06-30T11:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9388#issuecomment-89364",
    "user": "drkirkby"
}
```

Mercurial patch which fully solves the rubiks makefile problem using only POSIX commands.



---

archive/issue_comments_089365.json:
```json
{
    "body": "Attachment [9388-fix-Rubiks-portably.patch](tarball://root/attachments/some-uuid/ticket9388/9388-fix-Rubiks-portably.patch) by rlm created at 2010-07-01 17:50:23\n\nDavid --- While credit for individual patches by definition goes to those who make them, the author block is for credit in the release notes, which should go to anyone who helped move the fix towards its final form. I think that Justin still deserves credit here for helping to hunt down the problem in the first place.\n\nIt might be that we're coming from different contexts, but it strikes me as rude to remove someone from the author block.",
    "created_at": "2010-07-01T17:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9388#issuecomment-89365",
    "user": "rlm"
}
```

Attachment [9388-fix-Rubiks-portably.patch](tarball://root/attachments/some-uuid/ticket9388/9388-fix-Rubiks-portably.patch) by rlm created at 2010-07-01 17:50:23

David --- While credit for individual patches by definition goes to those who make them, the author block is for credit in the release notes, which should go to anyone who helped move the fix towards its final form. I think that Justin still deserves credit here for helping to hunt down the problem in the first place.

It might be that we're coming from different contexts, but it strikes me as rude to remove someone from the author block.



---

archive/issue_comments_089366.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-01T17:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9388#issuecomment-89366",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089367.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-01T18:14:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9388#issuecomment-89367",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_089368.json:
```json
{
    "body": "Replying to [comment:6 rlm]:\n\n> It might be that we're coming from different contexts, but it strikes me as rude to remove someone from the author block.\n\nThat certainly was not my intension. I was coming it from the point that an author could not review it, and it would make it possible for Justin to review it. \nIf you look at a comment on sage-devel today, I specifically asked Francois to remove me from an author or #9097 since he had another idea on this, then I would be able to review it. \n\nSorry if I caused any offense to Justin or yourself - that was certainly not my intension. \n\nDave",
    "created_at": "2010-07-01T18:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9388#issuecomment-89368",
    "user": "drkirkby"
}
```

Replying to [comment:6 rlm]:

> It might be that we're coming from different contexts, but it strikes me as rude to remove someone from the author block.

That certainly was not my intension. I was coming it from the point that an author could not review it, and it would make it possible for Justin to review it. 
If you look at a comment on sage-devel today, I specifically asked Francois to remove me from an author or #9097 since he had another idea on this, then I would be able to review it. 

Sorry if I caused any offense to Justin or yourself - that was certainly not my intension. 

Dave



---

archive/issue_comments_089369.json:
```json
{
    "body": "Replying to [comment:8 drkirkby]:\n> That certainly was not my intension. I was coming it from the point that an author could not review it, and it would make it possible for Justin to review it. \n> If you look at a comment on sage-devel today, I specifically asked Francois to remove me from an author or #9097 since he had another idea on this, then I would be able to review it. \n\nI frequently see the same two people listed as author and reviewer. Often there are multiple patches, with (author, reviewer) switching between persons (a,b) and (b,a), for one example. I am sure you did not intend anything rude, I just wanted to bring it up to avoid misunderstanding. The author and reviewer fields on the trac server should be the union of anyone who feels that they have contributed to that part of the process. The only rule to follow strictly is that the author of a patch cannot review that patch, but as you have seen, trac tickets frequently become pretty complicated. One applies that rule patch by patch, not ticket by ticket.\n\n> \n> Sorry if I caused any offense to Justin or yourself - that was certainly not my intension. \n> \n\nThere is no offense here.\n\nCheers!\n-- RLM",
    "created_at": "2010-07-01T20:27:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9388#issuecomment-89369",
    "user": "rlm"
}
```

Replying to [comment:8 drkirkby]:
> That certainly was not my intension. I was coming it from the point that an author could not review it, and it would make it possible for Justin to review it. 
> If you look at a comment on sage-devel today, I specifically asked Francois to remove me from an author or #9097 since he had another idea on this, then I would be able to review it. 

I frequently see the same two people listed as author and reviewer. Often there are multiple patches, with (author, reviewer) switching between persons (a,b) and (b,a), for one example. I am sure you did not intend anything rude, I just wanted to bring it up to avoid misunderstanding. The author and reviewer fields on the trac server should be the union of anyone who feels that they have contributed to that part of the process. The only rule to follow strictly is that the author of a patch cannot review that patch, but as you have seen, trac tickets frequently become pretty complicated. One applies that rule patch by patch, not ticket by ticket.

> 
> Sorry if I caused any offense to Justin or yourself - that was certainly not my intension. 
> 

There is no offense here.

Cheers!
-- RLM
