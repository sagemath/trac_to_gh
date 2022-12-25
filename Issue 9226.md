# Issue 9226: README.txt says " Sage builds with GCC >= 3.x" but it does NOT

archive/issues_009226.json:
```json
{
    "body": "Assignee: mvngu\n\nThe title pretty much says it all. There is no way Sage will build with any gcc <= 4.0.1. The 'prereq' script will stop any attempt and even if you bypass that stop (by setting the appropiate environment variable), Sage will not build \n\nI've attached a revised README.txt, which addresses this and\n\n* The fact gcc, g++ and gfortran need to be the same versions. \n* Spelling change of Sparc -> SPARC. \n* Better information about what does and does not work on Solaris.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9226\n\n",
    "created_at": "2010-06-12T11:51:57Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "README.txt says \" Sage builds with GCC >= 3.x\" but it does NOT",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9226",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: mvngu

The title pretty much says it all. There is no way Sage will build with any gcc <= 4.0.1. The 'prereq' script will stop any attempt and even if you bypass that stop (by setting the appropiate environment variable), Sage will not build 

I've attached a revised README.txt, which addresses this and

* The fact gcc, g++ and gfortran need to be the same versions. 
* Spelling change of Sparc -> SPARC. 
* Better information about what does and does not work on Solaris.

Issue created by migration from https://trac.sagemath.org/ticket/9226





---

archive/issue_comments_086429.json:
```json
{
    "body": "Attachment [README.txt](tarball://root/attachments/some-uuid/ticket9226/README.txt) by drkirkby created at 2010-06-12 12:25:58\n\nSuggested revised README.txt",
    "created_at": "2010-06-12T12:25:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9226#issuecomment-86429",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [README.txt](tarball://root/attachments/some-uuid/ticket9226/README.txt) by drkirkby created at 2010-06-12 12:25:58

Suggested revised README.txt



---

archive/issue_comments_086430.json:
```json
{
    "body": "Attachment [README.txt.diff](tarball://root/attachments/some-uuid/ticket9226/README.txt.diff) by drkirkby created at 2010-06-12 12:26:40\n\nDifferences from README.txt in Sage 4.4.3",
    "created_at": "2010-06-12T12:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9226#issuecomment-86430",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [README.txt.diff](tarball://root/attachments/some-uuid/ticket9226/README.txt.diff) by drkirkby created at 2010-06-12 12:26:40

Differences from README.txt in Sage 4.4.3



---

archive/issue_comments_086431.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-12T16:29:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9226#issuecomment-86431",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086432.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-12T16:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9226#issuecomment-86432",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086433.json:
```json
{
    "body": "Replaced SAGE_ROOT/README.txt with the README.txt here in 4.5.2.alpha1.",
    "created_at": "2010-07-22T09:03:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9226#issuecomment-86433",
    "user": "https://github.com/dandrake"
}
```

Replaced SAGE_ROOT/README.txt with the README.txt here in 4.5.2.alpha1.



---

archive/issue_events_009384.json:
```json
{
    "actor": "@dandrake",
    "created_at": "2010-07-22T09:03:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9226",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9226#event-9384"
}
```



---

archive/issue_comments_086434.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-22T09:03:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9226#issuecomment-86434",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed



---

archive/issue_comments_086435.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-08-05T02:22:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9226#issuecomment-86435",
    "user": "https://github.com/qed777"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_086436.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-08-05T02:22:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9226#issuecomment-86436",
    "user": "https://github.com/qed777"
}
```

Changing status from closed to new.



---

archive/issue_events_009385.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-08-05T02:22:57Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/9226",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9226#event-9385"
}
```



---

archive/issue_comments_086437.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-08-05T02:22:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9226#issuecomment-86437",
    "user": "https://github.com/qed777"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_086438.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-05T03:01:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9226#issuecomment-86438",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086439.json:
```json
{
    "body": "I just tried to correct a couple of typos in the description and managed to remove the positive review. I've restored it now.",
    "created_at": "2010-08-05T03:02:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9226#issuecomment-86439",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I just tried to correct a couple of typos in the description and managed to remove the positive review. I've restored it now.



---

archive/issue_comments_086440.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-05T03:02:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9226#issuecomment-86440",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086441.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-05T10:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9226#issuecomment-86441",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_009386.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-08-05T10:59:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9226",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9226#event-9386"
}
```



---

archive/issue_comments_086442.json:
```json
{
    "body": "It's unfortunate that this is so, because there is still a problem, namely that \n\n```\nPPC              Apple Mac OS X 10.4.x, 10.5.x, 10.6.x\n```\n\nis by definition wrong, since 10.6.x will only work on Intel chips.  Also see other README.txt updates lurking on Trac, such as #7484, which also fixes #8106; #6055 perhaps should be closed, while #5505 I'm less clear on; #5339 seems closable as dup; #3131 perhaps is not relevant, but while I'm listing all of them...",
    "created_at": "2010-08-05T15:11:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9226#issuecomment-86442",
    "user": "https://github.com/kcrisman"
}
```

It's unfortunate that this is so, because there is still a problem, namely that 

```
PPC              Apple Mac OS X 10.4.x, 10.5.x, 10.6.x
```

is by definition wrong, since 10.6.x will only work on Intel chips.  Also see other README.txt updates lurking on Trac, such as #7484, which also fixes #8106; #6055 perhaps should be closed, while #5505 I'm less clear on; #5339 seems closable as dup; #3131 perhaps is not relevant, but while I'm listing all of them...



---

archive/issue_comments_086443.json:
```json
{
    "body": "Replying to [comment:10 kcrisman]:\n> It's unfortunate that this is so, because there is still a problem, namely that \n> {{{\n> PPC              Apple Mac OS X 10.4.x, 10.5.x, 10.6.x\n> }}}\n> is by definition wrong, since 10.6.x will only work on Intel chips.  Also see other README.txt updates lurking on Trac, such as #7484, which also fixes #8106; #6055 perhaps should be closed, while #5505 I'm less clear on; #5339 seems closable as dup; #3131 perhaps is not relevant, but while I'm listing all of them... \n\nI would recommend that anyone currently working on fixing the SAGE_ROOT README.txt, the spkg/standard/deps file, or any of the other crucial files that are not under revision control...please take a look at #9433, which will put these files into a Mercurial repository, and make dealing with them reasonable, instead of the current mess. #9433 should actually be pretty easy to review.",
    "created_at": "2010-08-05T17:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9226#issuecomment-86443",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:10 kcrisman]:
> It's unfortunate that this is so, because there is still a problem, namely that 
> {{{
> PPC              Apple Mac OS X 10.4.x, 10.5.x, 10.6.x
> }}}
> is by definition wrong, since 10.6.x will only work on Intel chips.  Also see other README.txt updates lurking on Trac, such as #7484, which also fixes #8106; #6055 perhaps should be closed, while #5505 I'm less clear on; #5339 seems closable as dup; #3131 perhaps is not relevant, but while I'm listing all of them... 

I would recommend that anyone currently working on fixing the SAGE_ROOT README.txt, the spkg/standard/deps file, or any of the other crucial files that are not under revision control...please take a look at #9433, which will put these files into a Mercurial repository, and make dealing with them reasonable, instead of the current mess. #9433 should actually be pretty easy to review.



---

archive/issue_comments_086444.json:
```json
{
    "body": "> I would recommend that anyone currently working on fixing the SAGE_ROOT README.txt, the spkg/standard/deps file, or any of the other crucial files that are not under revision control...please take a look at #9433, which will put these files into a Mercurial repository, and make dealing with them reasonable, instead of the current mess. #9433 should actually be pretty easy to review.\n\nYes, I just didn't mention this one since it was a meta-ticket.  I don't feel technically capable of it (not knowing ins and outs of hg), otherwise I would have done so weeks ago :(",
    "created_at": "2010-08-05T17:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9226#issuecomment-86444",
    "user": "https://github.com/kcrisman"
}
```

> I would recommend that anyone currently working on fixing the SAGE_ROOT README.txt, the spkg/standard/deps file, or any of the other crucial files that are not under revision control...please take a look at #9433, which will put these files into a Mercurial repository, and make dealing with them reasonable, instead of the current mess. #9433 should actually be pretty easy to review.

Yes, I just didn't mention this one since it was a meta-ticket.  I don't feel technically capable of it (not knowing ins and outs of hg), otherwise I would have done so weeks ago :(



---

archive/issue_comments_086445.json:
```json
{
    "body": "Replying to [comment:12 kcrisman]:\n> \n> > I would recommend that anyone currently working on fixing the SAGE_ROOT README.txt, the spkg/standard/deps file, or any of the other crucial files that are not under revision control...please take a look at #9433, which will put these files into a Mercurial repository, and make dealing with them reasonable, instead of the current mess. #9433 should actually be pretty easy to review.\n> \n> Yes, I just didn't mention this one since it was a meta-ticket.  I don't feel technically capable of it (not knowing ins and outs of hg), otherwise I would have done so weeks ago :(\n\nSame here. I don't feel able to review it. If Dan believes it is an easy review, perhaps he could consider doing it if he has time, as at least two of us don't feel able to do it, and nobody else has stepped up. Yet I am one who agrees this would be a useful addition to Sage. The current system for such files is a bit silly. \n\nDave",
    "created_at": "2010-08-06T17:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9226#issuecomment-86445",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:12 kcrisman]:
> 
> > I would recommend that anyone currently working on fixing the SAGE_ROOT README.txt, the spkg/standard/deps file, or any of the other crucial files that are not under revision control...please take a look at #9433, which will put these files into a Mercurial repository, and make dealing with them reasonable, instead of the current mess. #9433 should actually be pretty easy to review.
> 
> Yes, I just didn't mention this one since it was a meta-ticket.  I don't feel technically capable of it (not knowing ins and outs of hg), otherwise I would have done so weeks ago :(

Same here. I don't feel able to review it. If Dan believes it is an easy review, perhaps he could consider doing it if he has time, as at least two of us don't feel able to do it, and nobody else has stepped up. Yet I am one who agrees this would be a useful addition to Sage. The current system for such files is a bit silly. 

Dave
