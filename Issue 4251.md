# Issue 4251: typo in installation manual

archive/issues_004251.json:
```json
{
    "body": "Assignee: tba\n\nCC:  mhansen\n\nThis was reported to by a new user:\n\nSection 2.2 Microsoft Windows in the \nInstallation Guide seems to have a dead line.\nMaybe \n\"http://www.sagemath.org/SAGEbin/vmware/\"\nshould be \n\"http://www.sagemath.org/download.html\"?\n\nI'm not sure what milestone to assign this nor how to\nsubmit a patch since we are in the process of \nswitching the documentation over to a new system.\n\n\n\n```\nDear David,\n  I went to your first link, went to Windows version, at page:\nhttp://www.sagemath.org/doc/inst/node4.html\n\nwhere the first link is dead: http://www.sagemath.org/SAGEbin/vmware/\n\nBut I got the vmware download through some other path (that I don't remember\nright now).\n        Mark\n\n-----Original Message-----\nFrom: David Joyner \nSent: Monday, October 06, 2008 12:06 PM\nTo: ....\nSubject: Re: Sage question\n\nMark Meyerson wrote:\n> Dear Dave,\n>\n> Is their a \"quick start\" document on line somewhere for SAGE - brief\n> directions for a. installing it on my computer and b. using it?  Thanks.\n>\n> Mark\n>\n> -----------      \n>\n>\n>   \n\nYes.\nThe installation document\nhttp://www.sagemath.org/doc/inst/inst.html\n\ndiscusses installation and the tutorial\nhttp://www.sagemath.org/doc/tut/tut.html\n\nand constructions document\nhttp://www.sagemath.org/doc/const/const.html\n\nhave lots of examples.\n\nLet me know if you need help.\n\nDavid \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4251\n\n",
    "created_at": "2008-10-07T17:47:52Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "typo in installation manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4251",
    "user": "wdj"
}
```
Assignee: tba

CC:  mhansen

This was reported to by a new user:

Section 2.2 Microsoft Windows in the 
Installation Guide seems to have a dead line.
Maybe 
"http://www.sagemath.org/SAGEbin/vmware/"
should be 
"http://www.sagemath.org/download.html"?

I'm not sure what milestone to assign this nor how to
submit a patch since we are in the process of 
switching the documentation over to a new system.



```
Dear David,
  I went to your first link, went to Windows version, at page:
http://www.sagemath.org/doc/inst/node4.html

where the first link is dead: http://www.sagemath.org/SAGEbin/vmware/

But I got the vmware download through some other path (that I don't remember
right now).
        Mark

-----Original Message-----
From: David Joyner 
Sent: Monday, October 06, 2008 12:06 PM
To: ....
Subject: Re: Sage question

Mark Meyerson wrote:
> Dear Dave,
>
> Is their a "quick start" document on line somewhere for SAGE - brief
> directions for a. installing it on my computer and b. using it?  Thanks.
>
> Mark
>
> -----------      
>
>
>   

Yes.
The installation document
http://www.sagemath.org/doc/inst/inst.html

discusses installation and the tutorial
http://www.sagemath.org/doc/tut/tut.html

and constructions document
http://www.sagemath.org/doc/const/const.html

have lots of examples.

Let me know if you need help.

David 
```


Issue created by migration from https://trac.sagemath.org/ticket/4251





---

archive/issue_comments_030927.json:
```json
{
    "body": "David,\n\nfeel free to post a patch to fix the issue with the current TeX based documentation. All fixes are also applied (manually) to the ReST tree and while that is likely to come soon I would not hold off on fairly localizes fixes like the above. I would not start a major rewrite of the documentation ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-10-07T21:06:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4251#issuecomment-30927",
    "user": "mabshoff"
}
```

David,

feel free to post a patch to fix the issue with the current TeX based documentation. All fixes are also applied (manually) to the ReST tree and while that is likely to come soon I would not hold off on fairly localizes fixes like the above. I would not start a major rewrite of the documentation ;)

Cheers,

Michael



---

archive/issue_comments_030928.json:
```json
{
    "body": "Attachment [trac_4251-typo-install-guide.patch](tarball://root/attachments/some-uuid/ticket4251/trac_4251-typo-install-guide.patch) by wdj created at 2008-10-08 00:05:13\n\na change to 2 lines of inst.tex, based on 3.1.3.alpha2",
    "created_at": "2008-10-08T00:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4251#issuecomment-30928",
    "user": "wdj"
}
```

Attachment [trac_4251-typo-install-guide.patch](tarball://root/attachments/some-uuid/ticket4251/trac_4251-typo-install-guide.patch) by wdj created at 2008-10-08 00:05:13

a change to 2 lines of inst.tex, based on 3.1.3.alpha2



---

archive/issue_comments_030929.json:
```json
{
    "body": "The attached patch seems to compile fine for me.",
    "created_at": "2008-10-08T00:05:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4251#issuecomment-30929",
    "user": "wdj"
}
```

The attached patch seems to compile fine for me.



---

archive/issue_comments_030930.json:
```json
{
    "body": "The patch looks good to me, but I couldn't get it to apply, I think because the relevant lines contain \"\\SAGE\" instead of \"SAGE\".  I'm attaching a slightly modified patch, which should be used instead.  With that, positive review.",
    "created_at": "2008-10-17T21:12:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4251#issuecomment-30930",
    "user": "jhpalmieri"
}
```

The patch looks good to me, but I couldn't get it to apply, I think because the relevant lines contain "\SAGE" instead of "SAGE".  I'm attaching a slightly modified patch, which should be used instead.  With that, positive review.



---

archive/issue_comments_030931.json:
```json
{
    "body": "Attachment [4251.patch](tarball://root/attachments/some-uuid/ticket4251/4251.patch) by jhpalmieri created at 2008-10-17 21:12:55",
    "created_at": "2008-10-17T21:12:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4251#issuecomment-30931",
    "user": "jhpalmieri"
}
```

Attachment [4251.patch](tarball://root/attachments/some-uuid/ticket4251/4251.patch) by jhpalmieri created at 2008-10-17 21:12:55



---

archive/issue_comments_030932.json:
```json
{
    "body": "Merged 4251.patch in Sage 3.2.alpha0",
    "created_at": "2008-10-18T09:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4251#issuecomment-30932",
    "user": "mabshoff"
}
```

Merged 4251.patch in Sage 3.2.alpha0



---

archive/issue_comments_030933.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-18T09:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4251#issuecomment-30933",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030934.json:
```json
{
    "body": "Mike,\n\nplease make sure to shadow this fix to the ReST documentation.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-18T09:11:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4251#issuecomment-30934",
    "user": "mabshoff"
}
```

Mike,

please make sure to shadow this fix to the ReST documentation.

Cheers,

Michael
