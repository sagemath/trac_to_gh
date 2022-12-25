# Issue 5111: axiom --> fricas

archive/issues_005111.json:
```json
{
    "body": "Assignee: @williamstein\n\nChange axiom.py to fricas.py and the axiom command to fricas.  \n\nThis is more logical since the doctests test fricas not axiom.  Also, this has been specifically requested by Tim Daly -- the trademark owner on the name Axiom -- and I think it is best to respect his request.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5111\n\n",
    "created_at": "2009-01-27T20:33:05Z",
    "labels": [
        "component: interfaces"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "axiom --> fricas",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5111",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Change axiom.py to fricas.py and the axiom command to fricas.  

This is more logical since the doctests test fricas not axiom.  Also, this has been specifically requested by Tim Daly -- the trademark owner on the name Axiom -- and I think it is best to respect his request.

Issue created by migration from https://trac.sagemath.org/ticket/5111





---

archive/issue_comments_038973.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-02-18T04:32:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5111#issuecomment-38973",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_038974.json:
```json
{
    "body": "It's been brought up that this may be a bad idea, since after all we still have an axiom interface.  The purpose of this ticket is this:\n\n* gather results from discussion and possible voting\n* decide what if any change to make\n* make said change",
    "created_at": "2009-02-18T04:40:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5111#issuecomment-38974",
    "user": "https://github.com/williamstein"
}
```

It's been brought up that this may be a bad idea, since after all we still have an axiom interface.  The purpose of this ticket is this:

* gather results from discussion and possible voting
* decide what if any change to make
* make said change



---

archive/issue_comments_038975.json:
```json
{
    "body": "\n```\n20:41 < wstein> On the other hand, if Tim Daly really is the trademark owner of axiom, can't he\n20:41 < wstein> just tell us we can't use the name and that is that?\n20:41 < cwitty> I don't think so.\n20:41 < cwitty> He can tell us we can't call our product axiom.\n20:42 < cwitty> He can probably tell us we can't call fricas axiom, which is closer to what we're doing.\n20:43 < mhansen> cwitty: We're actually just calling whatever \"axiom\" command happens to be on the system.\n```\n",
    "created_at": "2009-02-18T04:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5111#issuecomment-38975",
    "user": "https://github.com/williamstein"
}
```


```
20:41 < wstein> On the other hand, if Tim Daly really is the trademark owner of axiom, can't he
20:41 < wstein> just tell us we can't use the name and that is that?
20:41 < cwitty> I don't think so.
20:41 < cwitty> He can tell us we can't call our product axiom.
20:42 < cwitty> He can probably tell us we can't call fricas axiom, which is closer to what we're doing.
20:43 < mhansen> cwitty: We're actually just calling whatever "axiom" command happens to be on the system.
```




---

archive/issue_comments_038976.json:
```json
{
    "body": "Attachment [trac_5111.patch](tarball://root/attachments/some-uuid/ticket5111/trac_5111.patch) by @mwhansen created at 2009-02-19 17:39:40",
    "created_at": "2009-02-19T17:39:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5111#issuecomment-38976",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_5111.patch](tarball://root/attachments/some-uuid/ticket5111/trac_5111.patch) by @mwhansen created at 2009-02-19 17:39:40



---

archive/issue_comments_038977.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-19T17:41:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5111#issuecomment-38977",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038978.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2009-02-19T17:41:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5111#issuecomment-38978",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_038979.json:
```json
{
    "body": "Note that this applies on top of the ReST patches so it should not go in until those are in.\n\nAlso, this patch includes the changes found in #4036.",
    "created_at": "2009-02-19T17:41:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5111#issuecomment-38979",
    "user": "https://github.com/mwhansen"
}
```

Note that this applies on top of the ReST patches so it should not go in until those are in.

Also, this patch includes the changes found in #4036.



---

archive/issue_comments_038980.json:
```json
{
    "body": "Also, all of the axiom() commands pass tests with the January 2009 release of Axiom.",
    "created_at": "2009-02-19T17:42:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5111#issuecomment-38980",
    "user": "https://github.com/mwhansen"
}
```

Also, all of the axiom() commands pass tests with the January 2009 release of Axiom.



---

archive/issue_comments_038981.json:
```json
{
    "body": "Mike,\n\nI do not understand the reference to \"ReST patches\". Are these in or out of sage-3.3? Bottom line: Can your patch be applied directly to sage-3.3?\n\nBill.",
    "created_at": "2009-02-23T17:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5111#issuecomment-38981",
    "user": "https://trac.sagemath.org/admin/accounts/users/bpage"
}
```

Mike,

I do not understand the reference to "ReST patches". Are these in or out of sage-3.3? Bottom line: Can your patch be applied directly to sage-3.3?

Bill.



---

archive/issue_comments_038982.json:
```json
{
    "body": "Replying to [comment:6 bpage]:\n> Mike,\n\nHi Bill,\n\n> I do not understand the reference to \"ReST patches\". Are these in or out of sage-3.3? Bottom line: Can your patch be applied directly to sage-3.3?\n\nNo. The ReST patches are about 35 tickets work of documentation fixes that will go into 3.4. It will be out before the weekend, so you might want to wait until then to play with this. Note that 3.4.alpha0 ought in about 24 hours ought to contain all the ReST patches, so that might be something you could use for review.\n\nCheers,\n\nMichael\n\n> Bill.",
    "created_at": "2009-02-23T17:42:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5111#issuecomment-38982",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:6 bpage]:
> Mike,

Hi Bill,

> I do not understand the reference to "ReST patches". Are these in or out of sage-3.3? Bottom line: Can your patch be applied directly to sage-3.3?

No. The ReST patches are about 35 tickets work of documentation fixes that will go into 3.4. It will be out before the weekend, so you might want to wait until then to play with this. Note that 3.4.alpha0 ought in about 24 hours ought to contain all the ReST patches, so that might be something you could use for review.

Cheers,

Michael

> Bill.



---

archive/issue_comments_038983.json:
```json
{
    "body": "Mike,\n\nThanks. I have successfully applied this patch to sage-3.4.alpha0 and have just begun testing. I noticed however that patch returned the warning:\n\npatching file sage/structure/sage_object.pyx\nHunk #1 succeeded at 305 (offset 7 lines)\n\nSo I guess there has already by some code drift.\n\nThe first bug I noticed was that\n\n  ./sage -fricas\n\ndoes not start a FriCAS session.\n\n  ./sage -axiom\n\nhowever still starts FriCAS even though /usr/local/axiom has been replaced with a dummy script.\n\nI guess this command line processing must be done in some other part of sage?\n\nRegards,\nBill Page.",
    "created_at": "2009-02-25T05:39:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5111#issuecomment-38983",
    "user": "https://trac.sagemath.org/admin/accounts/users/bpage"
}
```

Mike,

Thanks. I have successfully applied this patch to sage-3.4.alpha0 and have just begun testing. I noticed however that patch returned the warning:

patching file sage/structure/sage_object.pyx
Hunk #1 succeeded at 305 (offset 7 lines)

So I guess there has already by some code drift.

The first bug I noticed was that

  ./sage -fricas

does not start a FriCAS session.

  ./sage -axiom

however still starts FriCAS even though /usr/local/axiom has been replaced with a dummy script.

I guess this command line processing must be done in some other part of sage?

Regards,
Bill Page.



---

archive/issue_comments_038984.json:
```json
{
    "body": "Mike,\n\nOn my Debian 5.0 (Lenny) x86 system I have not been able to compile recent versions of Axiom from source using the instructions here:\n\n  http://axiom.axiom-developer.org/axiom-website/download.html\n\nI get build errors early in the process. What did you use to get the \"January 2009 release of Axiom\" referred to in your tests?\n\nAfter installing the binary version of Axiom via\n\n```\n  apt-get install axiom\n```\n\nI do get the older \"2005\" version of Axiom which does seem to run ok (known problems with Hyperdoc etc. notwithstanding). However this version seems to have pexpect synchronization problems.\n\n```\n  sage: axiom('1+1')\n\n  sage:\n```\n\nreturns no visible result, while\n\n```\n  sage: fricas('1+1')\n  2\n  sage:\n```\n\nbehaves as expected.\n\nI think the problem is probably caused by the differences in readline behavior under gcl and/or minor differences in the initial prompts. I am not sure how to handle this so long as we depend on an externally installed version of Axiom. If Sage is going to continue to support Axiom as an option, perhaps some effort needs to be given to creating an optional Axiom spkg ... (Don't look at me! :-). Otherwise, I would not be against getting rid of the 'axiom' function all together.\n\nOn this same subject: What consideration, if any, has been given to providing a similar interface for OpenAxiom? Does anyone want this?\n\nRegards,\nBill Page.",
    "created_at": "2009-02-25T17:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5111#issuecomment-38984",
    "user": "https://trac.sagemath.org/admin/accounts/users/bpage"
}
```

Mike,

On my Debian 5.0 (Lenny) x86 system I have not been able to compile recent versions of Axiom from source using the instructions here:

  http://axiom.axiom-developer.org/axiom-website/download.html

I get build errors early in the process. What did you use to get the "January 2009 release of Axiom" referred to in your tests?

After installing the binary version of Axiom via

```
  apt-get install axiom
```

I do get the older "2005" version of Axiom which does seem to run ok (known problems with Hyperdoc etc. notwithstanding). However this version seems to have pexpect synchronization problems.

```
  sage: axiom('1+1')

  sage:
```

returns no visible result, while

```
  sage: fricas('1+1')
  2
  sage:
```

behaves as expected.

I think the problem is probably caused by the differences in readline behavior under gcl and/or minor differences in the initial prompts. I am not sure how to handle this so long as we depend on an externally installed version of Axiom. If Sage is going to continue to support Axiom as an option, perhaps some effort needs to be given to creating an optional Axiom spkg ... (Don't look at me! :-). Otherwise, I would not be against getting rid of the 'axiom' function all together.

On this same subject: What consideration, if any, has been given to providing a similar interface for OpenAxiom? Does anyone want this?

Regards,
Bill Page.



---

archive/issue_comments_038985.json:
```json
{
    "body": "Replying to [comment:9 bpage]:\n> Mike,\n> \n> On my Debian 5.0 (Lenny) x86 system I have not been able to compile recent versions of Axiom from source using the instructions here:\n> \n>   http://axiom.axiom-developer.org/axiom-website/download.html\n> \n> I get build errors early in the process. What did you use to get the \"January 2009 release of Axiom\" referred to in your tests?\n\nI just used the binary found here: http://www.axiom-developer.org/axiom-website/downloads/axiom-ubuntu64-jan2009-bin.tgz\n\n\n> \n> After installing the binary version of Axiom via\n> {{{\n>   apt-get install axiom\n> }}}\n> I do get the older \"2005\" version of Axiom which does seem to run ok (known problems with Hyperdoc etc. notwithstanding). However this version seems to have pexpect synchronization problems.\n\nYes, this is not too surprising.\n\n> I think the problem is probably caused by the differences in readline behavior under gcl and/or minor differences in the initial prompts. I am not sure how to handle this so long as we depend on an externally installed version of Axiom. If Sage is going to continue to support Axiom as an option, perhaps some effort needs to be given to creating an optional Axiom spkg ... (Don't look at me! :-). Otherwise, I would not be against getting rid of the 'axiom' function all together.\n\nI think Camm is updating the version of Axiom in Debian.  It'd be silly not to have some support since it's very little extra work.\n\n> On this same subject: What consideration, if any, has been given to providing a similar interface for OpenAxiom? Does anyone want this?\n\nI don't know -- I don't really use this software.  It should be pretty trivial to add support for.",
    "created_at": "2009-02-25T17:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5111#issuecomment-38985",
    "user": "https://github.com/mwhansen"
}
```

Replying to [comment:9 bpage]:
> Mike,
> 
> On my Debian 5.0 (Lenny) x86 system I have not been able to compile recent versions of Axiom from source using the instructions here:
> 
>   http://axiom.axiom-developer.org/axiom-website/download.html
> 
> I get build errors early in the process. What did you use to get the "January 2009 release of Axiom" referred to in your tests?

I just used the binary found here: http://www.axiom-developer.org/axiom-website/downloads/axiom-ubuntu64-jan2009-bin.tgz


> 
> After installing the binary version of Axiom via
> {{{
>   apt-get install axiom
> }}}
> I do get the older "2005" version of Axiom which does seem to run ok (known problems with Hyperdoc etc. notwithstanding). However this version seems to have pexpect synchronization problems.

Yes, this is not too surprising.

> I think the problem is probably caused by the differences in readline behavior under gcl and/or minor differences in the initial prompts. I am not sure how to handle this so long as we depend on an externally installed version of Axiom. If Sage is going to continue to support Axiom as an option, perhaps some effort needs to be given to creating an optional Axiom spkg ... (Don't look at me! :-). Otherwise, I would not be against getting rid of the 'axiom' function all together.

I think Camm is updating the version of Axiom in Debian.  It'd be silly not to have some support since it's very little extra work.

> On this same subject: What consideration, if any, has been given to providing a similar interface for OpenAxiom? Does anyone want this?

I don't know -- I don't really use this software.  It should be pretty trivial to add support for.



---

archive/issue_comments_038986.json:
```json
{
    "body": "Attachment [trac_5111b.patch](tarball://root/attachments/some-uuid/ticket5111/trac_5111b.patch) by bpage created at 2009-02-26 00:06:40",
    "created_at": "2009-02-26T00:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5111#issuecomment-38986",
    "user": "https://trac.sagemath.org/admin/accounts/users/bpage"
}
```

Attachment [trac_5111b.patch](tarball://root/attachments/some-uuid/ticket5111/trac_5111b.patch) by bpage created at 2009-02-26 00:06:40



---

archive/issue_comments_038987.json:
```json
{
    "body": "Here is a patch (trac_5111b.patch) that disables readline support for Axiom. With this change the axiom interface now works for me.\n\nAlso, I discovered that I was able to compile Axiom from the January 2009 source tarball. I still have a problem compiling the git or cvs head version on Debian 5.0.\n\nRe: Axiom binaries on Debian instead of an spkg. Is there any other case in Sage where an interface is provided from something that is not available for install as an spkg? I thought this might be a Sage policy.",
    "created_at": "2009-02-26T00:07:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5111#issuecomment-38987",
    "user": "https://trac.sagemath.org/admin/accounts/users/bpage"
}
```

Here is a patch (trac_5111b.patch) that disables readline support for Axiom. With this change the axiom interface now works for me.

Also, I discovered that I was able to compile Axiom from the January 2009 source tarball. I still have a problem compiling the git or cvs head version on Debian 5.0.

Re: Axiom binaries on Debian instead of an spkg. Is there any other case in Sage where an interface is provided from something that is not available for install as an spkg? I thought this might be a Sage policy.



---

archive/issue_comments_038988.json:
```json
{
    "body": "Replying to [comment:11 bpage]:\n> Here is a patch (trac_5111b.patch) that disables readline support for Axiom. With this change the axiom interface now works for me.\n\nCool!  Thanks for the fixes (and typo catches).\n\n> Re: Axiom binaries on Debian instead of an spkg. Is there any other case in Sage where an interface is provided from something that is not available for install as an spkg? I thought this might be a Sage policy.\n\nYeah, there are plenty of things like that.  For example, all of the proprietary math software interfaces :-)\n\n--Mike",
    "created_at": "2009-02-26T00:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5111#issuecomment-38988",
    "user": "https://github.com/mwhansen"
}
```

Replying to [comment:11 bpage]:
> Here is a patch (trac_5111b.patch) that disables readline support for Axiom. With this change the axiom interface now works for me.

Cool!  Thanks for the fixes (and typo catches).

> Re: Axiom binaries on Debian instead of an spkg. Is there any other case in Sage where an interface is provided from something that is not available for install as an spkg? I thought this might be a Sage policy.

Yeah, there are plenty of things like that.  For example, all of the proprietary math software interfaces :-)

--Mike



---

archive/issue_comments_038989.json:
```json
{
    "body": "I did a fairly fast skim of the code (I didn't study it), and tested the axiom interface on my computer (against an old version of axiom).  A couple of doctests failed with slightly different printing than expected (probably because the axiom version was old; the answer was correct, only the printing was wrong), but almost all of them passed.\n\nPositive review (apply both patches).",
    "created_at": "2009-04-19T04:09:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5111#issuecomment-38989",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

I did a fairly fast skim of the code (I didn't study it), and tested the axiom interface on my computer (against an old version of axiom).  A couple of doctests failed with slightly different printing than expected (probably because the axiom version was old; the answer was correct, only the printing was wrong), but almost all of them passed.

Positive review (apply both patches).



---

archive/issue_comments_038990.json:
```json
{
    "body": "Merged both patches in Sage 3.4.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T01:00:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5111#issuecomment-38990",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.4.2.alpha0.

Cheers,

Michael



---

archive/issue_comments_038991.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-24T01:00:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5111#issuecomment-38991",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005358.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-24T01:00:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5111",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5111#event-5358"
}
```
