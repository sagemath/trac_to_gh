# Issue 9982: boehm_gc fails to build properly on AIX 5.3

archive/issues_009982.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @fchapoton\n\nUsing the following system: \n\n* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)\n* 4 x 332 MHz 32-bit PowerPC CPUs\n* 3 GB RAM\n* A fair wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)\n* AIX 5.3 (A POSIX certified operating system)\n* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)\n* DDS-4 tape drive \n\nboehm_gc-7.1.p6 fails to build properly on AIX. See attached log of the build. I'm not sure yet if this is an upstream problem on a Sage problem. \n\nIssue created by migration from https://trac.sagemath.org/ticket/9983\n\n",
    "created_at": "2010-09-23T20:26:50Z",
    "labels": [
        "component: porting: aix or hp-ux",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "boehm_gc fails to build properly on AIX 5.3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9982",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @fchapoton

Using the following system: 

* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
* 4 x 332 MHz 32-bit PowerPC CPUs
* 3 GB RAM
* A fair wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
* AIX 5.3 (A POSIX certified operating system)
* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
* DDS-4 tape drive 

boehm_gc-7.1.p6 fails to build properly on AIX. See attached log of the build. I'm not sure yet if this is an upstream problem on a Sage problem. 

Issue created by migration from https://trac.sagemath.org/ticket/9983





---

archive/issue_comments_100147.json:
```json
{
    "body": "Log of a failed build on an RS/6000 running AIX 5.3",
    "created_at": "2010-09-23T20:27:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9982#issuecomment-100147",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Log of a failed build on an RS/6000 running AIX 5.3



---

archive/issue_comments_100148.json:
```json
{
    "body": "Attachment [boehm_gc-7.1.p6.log](tarball://root/attachments/some-uuid/ticket9983/boehm_gc-7.1.p6.log) by @jm58660 created at 2016-08-30 04:43:09\n\nEOL for AIX 5.3 was four years ago, and nobody seems to care about this ticket. So I suggest we close this as wontfix.",
    "created_at": "2016-08-30T04:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9982#issuecomment-100148",
    "user": "https://github.com/jm58660"
}
```

Attachment [boehm_gc-7.1.p6.log](tarball://root/attachments/some-uuid/ticket9983/boehm_gc-7.1.p6.log) by @jm58660 created at 2016-08-30 04:43:09

EOL for AIX 5.3 was four years ago, and nobody seems to care about this ticket. So I suggest we close this as wontfix.



---

archive/issue_comments_100149.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-08-30T04:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9982#issuecomment-100149",
    "user": "https://github.com/jm58660"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_100150.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-08-30T07:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9982#issuecomment-100150",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_100151.json:
```json
{
    "body": "Should we mass-close all tickets about AIX?",
    "created_at": "2016-08-30T09:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9982#issuecomment-100151",
    "user": "https://github.com/jdemeyer"
}
```

Should we mass-close all tickets about AIX?



---

archive/issue_comments_100152.json:
```json
{
    "body": "Replying to [comment:3 jdemeyer]:\n> Should we mass-close all tickets about AIX?\n\nIs anyone using [SageMath](SageMath) on AIX?\n\nAt least #9993 (\"Singular fails to build on AIX 5.3\") has no value, as it just tells an error. But  #9990 (\"Pari fails to build on AIX\") contains some discussion. But OTOH also closed tickets can be searched.",
    "created_at": "2016-08-30T10:06:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9982#issuecomment-100152",
    "user": "https://github.com/jm58660"
}
```

Replying to [comment:3 jdemeyer]:
> Should we mass-close all tickets about AIX?

Is anyone using [SageMath](SageMath) on AIX?

At least #9993 ("Singular fails to build on AIX 5.3") has no value, as it just tells an error. But  #9990 ("Pari fails to build on AIX") contains some discussion. But OTOH also closed tickets can be searched.



---

archive/issue_comments_100153.json:
```json
{
    "body": "Determined to be invalid/duplicate/wontfix (closing as \"wontfix\" as a catch-all resolution).",
    "created_at": "2016-08-30T13:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9982#issuecomment-100153",
    "user": "https://github.com/embray"
}
```

Determined to be invalid/duplicate/wontfix (closing as "wontfix" as a catch-all resolution).



---

archive/issue_events_010106.json:
```json
{
    "actor": "@embray",
    "created_at": "2016-08-30T13:32:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9982",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9982#event-10106"
}
```



---

archive/issue_comments_100154.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2016-08-30T13:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9982#issuecomment-100154",
    "user": "https://github.com/embray"
}
```

Resolution: wontfix
