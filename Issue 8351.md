# Issue 8351: ratpoints-2.1.3.p0 fails to build in Open Solaris x64 as 64 bit even if SAGE64=yes

archive/issues_008351.json:
```json
{
    "body": "Assignee: drkirkby\n\nratpoints builds in 32 bit mode on Solaris x64.\n\nA patch is coming up.\n\nJaap\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8351\n\n",
    "created_at": "2010-02-24T19:52:47Z",
    "labels": [
        "component: porting",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "ratpoints-2.1.3.p0 fails to build in Open Solaris x64 as 64 bit even if SAGE64=yes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8351",
    "user": "https://github.com/jaapspies"
}
```
Assignee: drkirkby

ratpoints builds in 32 bit mode on Solaris x64.

A patch is coming up.

Jaap



Issue created by migration from https://trac.sagemath.org/ticket/8351





---

archive/issue_comments_074451.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-24T20:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8351#issuecomment-74451",
    "user": "https://github.com/jaapspies"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074452.json:
```json
{
    "body": "Attachment [ratpoints-2.1.3.p1.patch](tarball://root/attachments/some-uuid/ticket8351/ratpoints-2.1.3.p1.patch) by @jaapspies created at 2010-02-24 20:09:30\n\nA new spkg can be found here:\n\n[http://boxen.math.washington.edu/home/jsp/ports/ratpoints-2.1.3.p1.spkg](http://boxen.math.washington.edu/home/jsp/ports/ratpoints-2.1.3.p1.spkg)\n\n\n\n```\nfind_points.o:\tELF 64-bit LSB relocatable AMD64 Version 1\ninit.o:\t\tELF 64-bit LSB relocatable AMD64 Version 1\nsift.o:\t\tELF 64-bit LSB relocatable AMD64 Version 1\nsturm.o:\tELF 64-bit LSB relocatable AMD64 Version 1\n\n```\n\n\nJaap",
    "created_at": "2010-02-24T20:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8351#issuecomment-74452",
    "user": "https://github.com/jaapspies"
}
```

Attachment [ratpoints-2.1.3.p1.patch](tarball://root/attachments/some-uuid/ticket8351/ratpoints-2.1.3.p1.patch) by @jaapspies created at 2010-02-24 20:09:30

A new spkg can be found here:

[http://boxen.math.washington.edu/home/jsp/ports/ratpoints-2.1.3.p1.spkg](http://boxen.math.washington.edu/home/jsp/ports/ratpoints-2.1.3.p1.spkg)



```
find_points.o:	ELF 64-bit LSB relocatable AMD64 Version 1
init.o:		ELF 64-bit LSB relocatable AMD64 Version 1
sift.o:		ELF 64-bit LSB relocatable AMD64 Version 1
sturm.o:	ELF 64-bit LSB relocatable AMD64 Version 1

```


Jaap



---

archive/issue_comments_074453.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-24T20:24:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8351#issuecomment-74453",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074454.json:
```json
{
    "body": "There is a problem with this patch, in that tests for CCFLAG64, not CFLAG64 as others do. So it needs work. \n\nHowever, there are other problems with ratpoints that I am aware of. It is using the compiler option \n\n\n```\n-DUSE_SSE \n```\n\n\non SPARC, even though the SPARC processor has no SSE instructions. That does not appear to be a serious issue, but ratpoints has been implicated as the reason the Sage library does not build - see #7867, which is **very** serious.\n\nIt might be better if you leave this one to me to try to sort out, as the SPARC issues are more serious. \n\nDave",
    "created_at": "2010-02-24T20:24:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8351#issuecomment-74454",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

There is a problem with this patch, in that tests for CCFLAG64, not CFLAG64 as others do. So it needs work. 

However, there are other problems with ratpoints that I am aware of. It is using the compiler option 


```
-DUSE_SSE 
```


on SPARC, even though the SPARC processor has no SSE instructions. That does not appear to be a serious issue, but ratpoints has been implicated as the reason the Sage library does not build - see #7867, which is **very** serious.

It might be better if you leave this one to me to try to sort out, as the SPARC issues are more serious. 

Dave



---

archive/issue_comments_074455.json:
```json
{
    "body": "Replying to [comment:2 drkirkby]:\n> There is a problem with this patch, in that tests for CCFLAG64, not CFLAG64 as others do. So it needs work. \n> \n\nOk, I can do that though CFLAG64 is not used in this spkg.\n\n\n> However, there are other problems with ratpoints that I am aware of. It is using the compiler option \n> \n> {{{\n> -DUSE_SSE \n> }}}\n> \n> on SPARC, even though the SPARC processor has no SSE instructions. That does not appear to be a serious issue, but ratpoints has been implicated as the reason the Sage library does not build - see #7867, which is **very** serious.\n> \n> It might be better if you leave this one to me to try to sort out, as the SPARC issues are more serious. \n> \n\nYes, please solve the problems on SPARC, but that is certainly an other ticket.\nLet this spkg work on Open Solaris x64 is the only issue solved with this ticket.\n\nCheers,\n\nJaap\n\n\n> Dave",
    "created_at": "2010-02-24T21:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8351#issuecomment-74455",
    "user": "https://github.com/jaapspies"
}
```

Replying to [comment:2 drkirkby]:
> There is a problem with this patch, in that tests for CCFLAG64, not CFLAG64 as others do. So it needs work. 
> 

Ok, I can do that though CFLAG64 is not used in this spkg.


> However, there are other problems with ratpoints that I am aware of. It is using the compiler option 
> 
> {{{
> -DUSE_SSE 
> }}}
> 
> on SPARC, even though the SPARC processor has no SSE instructions. That does not appear to be a serious issue, but ratpoints has been implicated as the reason the Sage library does not build - see #7867, which is **very** serious.
> 
> It might be better if you leave this one to me to try to sort out, as the SPARC issues are more serious. 
> 

Yes, please solve the problems on SPARC, but that is certainly an other ticket.
Let this spkg work on Open Solaris x64 is the only issue solved with this ticket.

Cheers,

Jaap


> Dave



---

archive/issue_comments_074456.json:
```json
{
    "body": "Attachment [ratpoints-2.1.3.p1+.patch](tarball://root/attachments/some-uuid/ticket8351/ratpoints-2.1.3.p1+.patch) by @jaapspies created at 2010-02-24 21:32:40",
    "created_at": "2010-02-24T21:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8351#issuecomment-74456",
    "user": "https://github.com/jaapspies"
}
```

Attachment [ratpoints-2.1.3.p1+.patch](tarball://root/attachments/some-uuid/ticket8351/ratpoints-2.1.3.p1+.patch) by @jaapspies created at 2010-02-24 21:32:40



---

archive/issue_comments_074457.json:
```json
{
    "body": "New spkg with the same name:\n\n[http://boxen.math.washington.edu/home/jsp/ports/ratpoints-2.1.3.p1.spkg](http://boxen.math.washington.edu/home/jsp/ports/ratpoints-2.1.3.p1.spkg)\n\nJaap",
    "created_at": "2010-02-24T21:34:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8351#issuecomment-74457",
    "user": "https://github.com/jaapspies"
}
```

New spkg with the same name:

[http://boxen.math.washington.edu/home/jsp/ports/ratpoints-2.1.3.p1.spkg](http://boxen.math.washington.edu/home/jsp/ports/ratpoints-2.1.3.p1.spkg)

Jaap



---

archive/issue_comments_074458.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-24T21:34:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8351#issuecomment-74458",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074459.json:
```json
{
    "body": "Sorry, I should have noted this earlier, but the package says \n\n\"Building with extra 64-bit flags for OS X and Open Solaris\"\n\nWhereas a more accurate description would be \n\n\"Building with the compiler flag(s) $CFLAG64 for a 64-bit build\"\n\nHopefully this should work at the very least on Solaris 10, and hopefully other platforms such as Cygwin, perhaps HP-UX and/or AIX.\n\nI would avoid mentioning Solaris specifically unless it is necessary. In this case it is not. \n\nDave",
    "created_at": "2010-03-03T21:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8351#issuecomment-74459",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Sorry, I should have noted this earlier, but the package says 

"Building with extra 64-bit flags for OS X and Open Solaris"

Whereas a more accurate description would be 

"Building with the compiler flag(s) $CFLAG64 for a 64-bit build"

Hopefully this should work at the very least on Solaris 10, and hopefully other platforms such as Cygwin, perhaps HP-UX and/or AIX.

I would avoid mentioning Solaris specifically unless it is necessary. In this case it is not. 

Dave



---

archive/issue_comments_074460.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-03T21:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8351#issuecomment-74460",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074461.json:
```json
{
    "body": "Replying to [comment:5 drkirkby]:\n> Sorry, I should have noted this earlier, but the package says \n> \n> \"Building with extra 64-bit flags for OS X and Open Solaris\"\n> \n> Whereas a more accurate description would be \n> \n> \"Building with the compiler flag(s) $CFLAG64 for a 64-bit build\"\n> \n\nHow important is this nit picking?\n\n> Hopefully this should work at the very least on Solaris 10, and hopefully other platforms such as Cygwin, perhaps HP-UX and/or AIX.\n> \n\nSolaris 10 64 bit? Since when is this an option?\n\n> I would avoid mentioning Solaris specifically unless it is necessary. In this case it is not. \n> \n\nPlease go ahead and make a reviewers patch.\n\nJaap\n\n\n> Dave",
    "created_at": "2010-03-03T21:21:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8351#issuecomment-74461",
    "user": "https://github.com/jaapspies"
}
```

Replying to [comment:5 drkirkby]:
> Sorry, I should have noted this earlier, but the package says 
> 
> "Building with extra 64-bit flags for OS X and Open Solaris"
> 
> Whereas a more accurate description would be 
> 
> "Building with the compiler flag(s) $CFLAG64 for a 64-bit build"
> 

How important is this nit picking?

> Hopefully this should work at the very least on Solaris 10, and hopefully other platforms such as Cygwin, perhaps HP-UX and/or AIX.
> 

Solaris 10 64 bit? Since when is this an option?

> I would avoid mentioning Solaris specifically unless it is necessary. In this case it is not. 
> 

Please go ahead and make a reviewers patch.

Jaap


> Dave



---

archive/issue_comments_074462.json:
```json
{
    "body": "Replying to [comment:6 jsp]:\n> Replying to [comment:5 drkirkby]:\n> > Sorry, I should have noted this earlier, but the package says \n> > \n> > \"Building with extra 64-bit flags for OS X and Open Solaris\"\n> > \n> > Whereas a more accurate description would be \n> > \n> > \"Building with the compiler flag(s) $CFLAG64 for a 64-bit build\"\n> > \n> \n> How important is this nit picking?\n\nI do not consider it nit-picking, for reasons you see below. \n \n> > Hopefully this should work at the very least on Solaris 10, and hopefully other platforms such as Cygwin, perhaps HP-UX and/or AIX.\n> > \n> \n> Solaris 10 64 bit? Since when is this an option?\n\nIt is very much a Sage goal. There is every reason to believe a Solaris 10 port will be 64-bit. The only reason the port was first 32-bit is that gcc tends to be less reliable on 64-bit SPARC. \n\nIt could even beat the Open Solaris port, though my interest is more in Open Solaris now. \n\nDave",
    "created_at": "2010-03-03T22:39:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8351#issuecomment-74462",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:6 jsp]:
> Replying to [comment:5 drkirkby]:
> > Sorry, I should have noted this earlier, but the package says 
> > 
> > "Building with extra 64-bit flags for OS X and Open Solaris"
> > 
> > Whereas a more accurate description would be 
> > 
> > "Building with the compiler flag(s) $CFLAG64 for a 64-bit build"
> > 
> 
> How important is this nit picking?

I do not consider it nit-picking, for reasons you see below. 
 
> > Hopefully this should work at the very least on Solaris 10, and hopefully other platforms such as Cygwin, perhaps HP-UX and/or AIX.
> > 
> 
> Solaris 10 64 bit? Since when is this an option?

It is very much a Sage goal. There is every reason to believe a Solaris 10 port will be 64-bit. The only reason the port was first 32-bit is that gcc tends to be less reliable on 64-bit SPARC. 

It could even beat the Open Solaris port, though my interest is more in Open Solaris now. 

Dave



---

archive/issue_comments_074463.json:
```json
{
    "body": "Replying to [comment:7 drkirkby]:\n> Replying to [comment:6 jsp]:\n> > Replying to [comment:5 drkirkby]:\n> > > Sorry, I should have noted this earlier, but the package says \n> > > \n> > > \"Building with extra 64-bit flags for OS X and Open Solaris\"\n> > > \n> > > Whereas a more accurate description would be \n> > > \n> > > \"Building with the compiler flag(s) $CFLAG64 for a 64-bit build\"\n> > > \n> > \n> > How important is this nit picking?\n> \n> I do not consider it nit-picking, for reasons you see below. \n> \n\nI don't see that.\n\n> > > Hopefully this should work at the very least on Solaris 10, and hopefully other platforms such as Cygwin, perhaps HP-UX and/or AIX.\n> > > \n> > \n> > Solaris 10 64 bit? Since when is this an option?\n> \n> It is very much a Sage goal. There is every reason to believe a Solaris 10 port will be 64-bit. The only reason the port was first 32-bit is that gcc tends to be less reliable on 64-bit SPARC. \n> \n> It could even beat the Open Solaris port, though my interest is more in Open Solaris now. \n> \n\nPlease make it possible. My interest is in Open Solaris too. Let's make this\npossible asap. If you insist on making this ticket the first in a target to make Solaris 10 64 bit work, please go ahead and count me off.\n\nJaap\n\n\n> Dave \n>",
    "created_at": "2010-03-03T22:59:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8351#issuecomment-74463",
    "user": "https://github.com/jaapspies"
}
```

Replying to [comment:7 drkirkby]:
> Replying to [comment:6 jsp]:
> > Replying to [comment:5 drkirkby]:
> > > Sorry, I should have noted this earlier, but the package says 
> > > 
> > > "Building with extra 64-bit flags for OS X and Open Solaris"
> > > 
> > > Whereas a more accurate description would be 
> > > 
> > > "Building with the compiler flag(s) $CFLAG64 for a 64-bit build"
> > > 
> > 
> > How important is this nit picking?
> 
> I do not consider it nit-picking, for reasons you see below. 
> 

I don't see that.

> > > Hopefully this should work at the very least on Solaris 10, and hopefully other platforms such as Cygwin, perhaps HP-UX and/or AIX.
> > > 
> > 
> > Solaris 10 64 bit? Since when is this an option?
> 
> It is very much a Sage goal. There is every reason to believe a Solaris 10 port will be 64-bit. The only reason the port was first 32-bit is that gcc tends to be less reliable on 64-bit SPARC. 
> 
> It could even beat the Open Solaris port, though my interest is more in Open Solaris now. 
> 

Please make it possible. My interest is in Open Solaris too. Let's make this
possible asap. If you insist on making this ticket the first in a target to make Solaris 10 64 bit work, please go ahead and count me off.

Jaap


> Dave 
>



---

archive/issue_comments_074464.json:
```json
{
    "body": "Lets just get this done. It works. \n\nDave",
    "created_at": "2010-06-04T10:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8351#issuecomment-74464",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Lets just get this done. It works. 

Dave



---

archive/issue_comments_074465.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-04T10:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8351#issuecomment-74465",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074466.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-04T10:09:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8351#issuecomment-74466",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074467.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T07:31:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8351#issuecomment-74467",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
