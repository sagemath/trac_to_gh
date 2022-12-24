# Issue 9998: Status of AIX port of Sage.

archive/issues_009998.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @fchapoton\n\nThis ticket lists those parts of Sage that have built in Sage, along with whether they have passed the tests. Unless otherwise stated, they results are from the following hardware. \n\n* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)\n* 4 x 332 MHz 32-bit PowerPC CPUs\n* 3 GB RAM\n* A fairly wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)\n* DDS-4 tape drive \n* AIX 5.3 (A POSIX certified operating system)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9999\n\n",
    "created_at": "2010-09-24T02:40:34Z",
    "labels": [
        "porting: AIX or HP-UX",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Status of AIX port of Sage.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9998",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  @fchapoton

This ticket lists those parts of Sage that have built in Sage, along with whether they have passed the tests. Unless otherwise stated, they results are from the following hardware. 

* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
* 4 x 332 MHz 32-bit PowerPC CPUs
* 3 GB RAM
* A fairly wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
* DDS-4 tape drive 
* AIX 5.3 (A POSIX certified operating system)


Issue created by migration from https://trac.sagemath.org/ticket/9999





---

archive/issue_comments_100449.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-09-26T04:39:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9998#issuecomment-100449",
    "user": "@robertwb"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_100450.json:
```json
{
    "body": "Since I have the hardware and the software, I'll add myself here.\n\nI should have a aix-7.1 test box soon and some power 7 box on which we may install anything from aix-5.3 to 7.1 by July/August.",
    "created_at": "2011-03-17T01:33:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9998#issuecomment-100450",
    "user": "@kiwifb"
}
```

Since I have the hardware and the software, I'll add myself here.

I should have a aix-7.1 test box soon and some power 7 box on which we may install anything from aix-5.3 to 7.1 by July/August.



---

archive/issue_comments_100451.json:
```json
{
    "body": "Replying to [comment:4 fbissey]:\n> Since I have the hardware and the software, I'll add myself here.\n> \n> I should have a aix-7.1 test box soon and some power 7 box on which we may install anything from aix-5.3 to 7.1 by July/August.\n\nI'm limited to AIX 5.3 due to the rather old hardware - you can see what I have listed above. \n\nThere was some interest from IBM to semi-fund an AIX port of Sage. They contacted William and were considering giving one or two people access to a quick machine. But due to security issues about where the machine was hosted, it could only be one or two developers and from a couple of IP addresses. As such, both William and I said it was not worth bothering with. \n\nThen it became apparent IBM wanted us to concentrate on one specific package - it seemed to me IBM were hoping to get a specific tool working on AIX for zero cost to them. I said I'd do that bit if they paid me, but nothing came of that. \n\nDave",
    "created_at": "2011-03-17T02:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9998#issuecomment-100451",
    "user": "drkirkby"
}
```

Replying to [comment:4 fbissey]:
> Since I have the hardware and the software, I'll add myself here.
> 
> I should have a aix-7.1 test box soon and some power 7 box on which we may install anything from aix-5.3 to 7.1 by July/August.

I'm limited to AIX 5.3 due to the rather old hardware - you can see what I have listed above. 

There was some interest from IBM to semi-fund an AIX port of Sage. They contacted William and were considering giving one or two people access to a quick machine. But due to security issues about where the machine was hosted, it could only be one or two developers and from a couple of IP addresses. As such, both William and I said it was not worth bothering with. 

Then it became apparent IBM wanted us to concentrate on one specific package - it seemed to me IBM were hoping to get a specific tool working on AIX for zero cost to them. I said I'd do that bit if they paid me, but nothing came of that. 

Dave



---

archive/issue_comments_100452.json:
```json
{
    "body": "Given the kind of relationship we have with IBM here I should make some enquiries. Can you name the tool in question?",
    "created_at": "2011-03-17T02:30:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9998#issuecomment-100452",
    "user": "@kiwifb"
}
```

Given the kind of relationship we have with IBM here I should make some enquiries. Can you name the tool in question?



---

archive/issue_comments_100453.json:
```json
{
    "body": "Replying to [comment:6 fbissey]:\n> Given the kind of relationship we have with IBM here I should make some enquiries. Can you name the tool in question?\n\nYes, I just checked my emails. It was Numpy and Scipy that someone at IBM wanted on AIX - I assume for his personal work. I've no idea of the work in doing this, but I'd be willing to at least consider it on a contract basis. \n\nI don't think there would be much appetite for an AIX port of Sage by sage-developers. In any case, for a port to take place, some decent hardware would be needed. My machine is too old, so even permitting others to use it (and I've done that several times), it would not be suitable for Sage development. Neither is a machine which has access restricted to a couple of people. \n\nThe offers made by IBM before, while I'm sure were made with good intentions, were not acceptable to either William or I. \n\nAnother issue, is that even if IBM gave William a server, he has no AIX administrator. I don't know AIX that well - though perhaps just about to set up a server. I've set my own up OK. \n\nIBM were supposed to be giving me an account on this 4 GHz AIX box, but I never got it, so I'm stuck using my own RS/6000, which is too old. \n\nDave",
    "created_at": "2011-03-17T04:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9998#issuecomment-100453",
    "user": "drkirkby"
}
```

Replying to [comment:6 fbissey]:
> Given the kind of relationship we have with IBM here I should make some enquiries. Can you name the tool in question?

Yes, I just checked my emails. It was Numpy and Scipy that someone at IBM wanted on AIX - I assume for his personal work. I've no idea of the work in doing this, but I'd be willing to at least consider it on a contract basis. 

I don't think there would be much appetite for an AIX port of Sage by sage-developers. In any case, for a port to take place, some decent hardware would be needed. My machine is too old, so even permitting others to use it (and I've done that several times), it would not be suitable for Sage development. Neither is a machine which has access restricted to a couple of people. 

The offers made by IBM before, while I'm sure were made with good intentions, were not acceptable to either William or I. 

Another issue, is that even if IBM gave William a server, he has no AIX administrator. I don't know AIX that well - though perhaps just about to set up a server. I've set my own up OK. 

IBM were supposed to be giving me an account on this 4 GHz AIX box, but I never got it, so I'm stuck using my own RS/6000, which is too old. 

Dave



---

archive/issue_comments_100454.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-04-01T14:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9998#issuecomment-100454",
    "user": "@mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_100455.json:
```json
{
    "body": "should be closed as outdated",
    "created_at": "2020-04-01T14:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9998#issuecomment-100455",
    "user": "@mkoeppe"
}
```

should be closed as outdated



---

archive/issue_comments_100456.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-04-01T14:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9998#issuecomment-100456",
    "user": "@fchapoton"
}
```

Resolution: invalid



---

archive/issue_comments_100457.json:
```json
{
    "body": "agreed",
    "created_at": "2020-04-01T14:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9998#issuecomment-100457",
    "user": "@fchapoton"
}
```

agreed
