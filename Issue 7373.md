# Issue 7373: [with spkg; needs review] Disable assembly code in libgcrypt on Solaris x86 & rare platforms.

archive/issues_007373.json:
```json
{
    "body": "Assignee: drkirkby\n\nOn my Sun Ultra 27, which has a quad core Xeon, running OpenSolaris 06/2009, libgrcypt would not build. The error message indicated it was related to the use of assembly code. \n\nHowever, I believe libgcrypt did not cause an issue on 'disk.math', so I'm somewhat surprised it did on my Ultra 27. But I think it is safer to disable assembly language on all Solaris x86 systems. (It is **not** necessary to do so on Solaris on SPARC)\n\nI also added some tests for other platforms (AIX, HP-UX, Tru64 and IRIX) and disabled assembly language on them too. It is most unlikely assembly code for them will work, and I hope to try at least some of these platforms in the near future. \n\nThe only updates are to spkg-install and SPKG.txt. The revised files will be put into \n\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/libgcrypt-1.4.4.p1 \n\nwithin 30 minutes of this post. (I thought I'd get the trac ticket in first, so the trac number can go into the SPKG.txt)\n\n\n\nDave\n\nIssue created by migration from https://trac.sagemath.org/ticket/7373\n\n",
    "created_at": "2009-11-02T01:05:58Z",
    "labels": [
        "component: porting",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "[with spkg; needs review] Disable assembly code in libgcrypt on Solaris x86 & rare platforms.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7373",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

On my Sun Ultra 27, which has a quad core Xeon, running OpenSolaris 06/2009, libgrcypt would not build. The error message indicated it was related to the use of assembly code. 

However, I believe libgcrypt did not cause an issue on 'disk.math', so I'm somewhat surprised it did on my Ultra 27. But I think it is safer to disable assembly language on all Solaris x86 systems. (It is **not** necessary to do so on Solaris on SPARC)

I also added some tests for other platforms (AIX, HP-UX, Tru64 and IRIX) and disabled assembly language on them too. It is most unlikely assembly code for them will work, and I hope to try at least some of these platforms in the near future. 

The only updates are to spkg-install and SPKG.txt. The revised files will be put into 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/libgcrypt-1.4.4.p1 

within 30 minutes of this post. (I thought I'd get the trac ticket in first, so the trac number can go into the SPKG.txt)



Dave

Issue created by migration from https://trac.sagemath.org/ticket/7373





---

archive/issue_comments_061657.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-02T04:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7373#issuecomment-61657",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061658.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-02T04:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7373#issuecomment-61658",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061659.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-11-02T04:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7373#issuecomment-61659",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_061660.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-02T05:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7373#issuecomment-61660",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_017435.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-02T05:48:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7373",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7373#event-17435"
}
```
