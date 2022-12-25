# Issue 7814: [with spkg; needs review] eclib ignores SAGE64 if OS is not Darwin

archive/issues_007814.json:
```json
{
    "body": "Assignee: drkirkby\n\neclib-20080310.p7 suffered the usual problem of many packages - SAGE64 was ignored unless the operating system was OS X. This trivial patch simply ensure SAGE64 is not ignored on any platform. \n\nI've checked in the changes with 'hg' \n\nSee: \nhttp://boxen.math.washington.edu/home/kirkby/portability/eclib-20080310.p8/\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7814\n\n",
    "created_at": "2010-01-02T04:53:07Z",
    "labels": [
        "component: porting",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "[with spkg; needs review] eclib ignores SAGE64 if OS is not Darwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7814",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

eclib-20080310.p7 suffered the usual problem of many packages - SAGE64 was ignored unless the operating system was OS X. This trivial patch simply ensure SAGE64 is not ignored on any platform. 

I've checked in the changes with 'hg' 

See: 
http://boxen.math.washington.edu/home/kirkby/portability/eclib-20080310.p8/



Issue created by migration from https://trac.sagemath.org/ticket/7814





---

archive/issue_comments_067486.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-01-02T20:53:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7814#issuecomment-67486",
    "user": "https://github.com/jaapspies"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_067487.json:
```json
{
    "body": "I think the wrong spkg is in this link.\n\nJaap",
    "created_at": "2010-01-02T20:53:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7814#issuecomment-67487",
    "user": "https://github.com/jaapspies"
}
```

I think the wrong spkg is in this link.

Jaap



---

archive/issue_comments_067488.json:
```json
{
    "body": "I see:\n\n\n```\nif [ \"$SAGE64\" = \"yes\" ]; then\n    echo \"64 bit MacIntel build\"\n    DYN_FLAGS=\"-m64\"; export DYN_FLAGS\n    PICFLAG=\"-m64 -fPIC\"\nfi\nexport PICFLAG\n\n```\n\n\nin spkg-install\n\nJaap",
    "created_at": "2010-01-02T20:57:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7814#issuecomment-67488",
    "user": "https://github.com/jaapspies"
}
```

I see:


```
if [ "$SAGE64" = "yes" ]; then
    echo "64 bit MacIntel build"
    DYN_FLAGS="-m64"; export DYN_FLAGS
    PICFLAG="-m64 -fPIC"
fi
export PICFLAG

```


in spkg-install

Jaap



---

archive/issue_comments_067489.json:
```json
{
    "body": "yes, I should have removed that comment about the MacIntel. I think you will find it does build, but I will remove that command and make a new package.",
    "created_at": "2010-01-02T21:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7814#issuecomment-67489",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

yes, I should have removed that comment about the MacIntel. I think you will find it does build, but I will remove that command and make a new package.



---

archive/issue_comments_067490.json:
```json
{
    "body": "If there is a new spkg (see above) I can give it a positive review. Tested on Fedora 12 and Open Solaris 32 bit\n\n```\nreal\t4m15.073s\nuser\t3m35.053s\nsys\t0m24.029s\nSuccessfully installed eclib-20080310.p8\nYou can safely delete the temporary build directory\n/export/home/jaap/Downloads/sage-4.3/spkg/build/eclib-20080310.p8\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing eclib-20080310.p8.spkg\njaap@opensolaris:~/Downloads/sage-4.3$ \n\n```\n\nAfter a successful install of ntl and pari.\n\nJaap",
    "created_at": "2010-01-03T19:18:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7814#issuecomment-67490",
    "user": "https://github.com/jaapspies"
}
```

If there is a new spkg (see above) I can give it a positive review. Tested on Fedora 12 and Open Solaris 32 bit

```
real	4m15.073s
user	3m35.053s
sys	0m24.029s
Successfully installed eclib-20080310.p8
You can safely delete the temporary build directory
/export/home/jaap/Downloads/sage-4.3/spkg/build/eclib-20080310.p8
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing eclib-20080310.p8.spkg
jaap@opensolaris:~/Downloads/sage-4.3$ 

```

After a successful install of ntl and pari.

Jaap



---

archive/issue_comments_067491.json:
```json
{
    "body": "I've updated the package. It is now missing the comment that its a MacIntel. \n\nPlease double check the package again though please - just in case I've messed up. \n\ndave",
    "created_at": "2010-01-03T20:39:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7814#issuecomment-67491",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I've updated the package. It is now missing the comment that its a MacIntel. 

Please double check the package again though please - just in case I've messed up. 

dave



---

archive/issue_comments_067492.json:
```json
{
    "body": "Replying to [comment:5 drkirkby]:\n> I've updated the package. It is now missing the comment that its a MacIntel. \n> \n> Please double check the package again though please - just in case I've messed up. \n> \n> dave \n\n\nSure,\n\nJaap",
    "created_at": "2010-01-03T20:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7814#issuecomment-67492",
    "user": "https://github.com/jaapspies"
}
```

Replying to [comment:5 drkirkby]:
> I've updated the package. It is now missing the comment that its a MacIntel. 
> 
> Please double check the package again though please - just in case I've messed up. 
> 
> dave 


Sure,

Jaap



---

archive/issue_comments_067493.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-03T21:11:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7814#issuecomment-67493",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067494.json:
```json
{
    "body": "On Open Solaris:\n\n```\nreal\t4m8.443s\nuser\t3m36.556s\nsys\t0m24.188s\nSuccessfully installed eclib-20080310.p8\n\n```\n\nLooks good, build tested on Fedora 12 and Fedora 11.\n\nPositive review.\n\nJaap",
    "created_at": "2010-01-03T21:11:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7814#issuecomment-67494",
    "user": "https://github.com/jaapspies"
}
```

On Open Solaris:

```
real	4m8.443s
user	3m36.556s
sys	0m24.188s
Successfully installed eclib-20080310.p8

```

Looks good, build tested on Fedora 12 and Fedora 11.

Positive review.

Jaap



---

archive/issue_comments_067495.json:
```json
{
    "body": "Couldn't change to positive review. Will do now.\n\nJaap",
    "created_at": "2010-01-03T21:12:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7814#issuecomment-67495",
    "user": "https://github.com/jaapspies"
}
```

Couldn't change to positive review. Will do now.

Jaap



---

archive/issue_comments_067496.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-03T21:12:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7814#issuecomment-67496",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067497.json:
```json
{
    "body": "Cheers. \n\nI'm just going to remove the 'needs review from the title. I'm not sure if we are still supposed to do that or not. I find it easier to find me own sometime if its in the title. But anyway, I'm removing it now.",
    "created_at": "2010-01-03T21:29:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7814#issuecomment-67497",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Cheers. 

I'm just going to remove the 'needs review from the title. I'm not sure if we are still supposed to do that or not. I find it easier to find me own sometime if its in the title. But anyway, I'm removing it now.



---

archive/issue_comments_067498.json:
```json
{
    "body": "Hi,\n\nIt already had a positive review, so ...?\n\nCheers,\n\nJaap",
    "created_at": "2010-01-03T21:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7814#issuecomment-67498",
    "user": "https://github.com/jaapspies"
}
```

Hi,

It already had a positive review, so ...?

Cheers,

Jaap



---

archive/issue_comments_067499.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T06:28:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7814#issuecomment-67499",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_018706.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-13T06:28:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7814",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7814#event-18706"
}
```



---

archive/issue_comments_067500.json:
```json
{
    "body": "Dave, I only just noticed this ticket (from the Release Notes).  I think you should have incereased the patch level from p8 to p9 - there now exist two different version s of the eclib spkg both called eclib-20080310.p8 which is rather confusing.\n\nJohn",
    "created_at": "2010-01-24T14:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7814#issuecomment-67500",
    "user": "https://github.com/JohnCremona"
}
```

Dave, I only just noticed this ticket (from the Release Notes).  I think you should have incereased the patch level from p8 to p9 - there now exist two different version s of the eclib spkg both called eclib-20080310.p8 which is rather confusing.

John



---

archive/issue_comments_067501.json:
```json
{
    "body": "Looking at the diff file I made of the SPKG.txt\n\nhttp://boxen.math.washington.edu/home/kirkby/portability/eclib-20080310.p8/SPKG.txt.diff\n\nthe last revision made was in \n\n === eclib-20080310.p7 (Michael Abshoff, October 12th, 2008) ===\n* Work around paralle make issue (#4228)\n\nthen I added \n\n### eclib-20080310.p8 (David Kirkby, 2nd January 2010)\n* Allow SAGE64 to work on all platforms, not just OS X. \n\nAre you sure the previous one was patch level 8 and not 7? If it was, then SPKG.txt was not updated when it moved to 8. Sorry about that, if I did overlook this. I agree it is confusing, if this is so. \n\nFor it to also be merged, and the release manager not notice, seems a bit strange. \n\nDave",
    "created_at": "2010-01-24T18:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7814#issuecomment-67501",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Looking at the diff file I made of the SPKG.txt

http://boxen.math.washington.edu/home/kirkby/portability/eclib-20080310.p8/SPKG.txt.diff

the last revision made was in 

 === eclib-20080310.p7 (Michael Abshoff, October 12th, 2008) ===
* Work around paralle make issue (#4228)

then I added 

### eclib-20080310.p8 (David Kirkby, 2nd January 2010)
* Allow SAGE64 to work on all platforms, not just OS X. 

Are you sure the previous one was patch level 8 and not 7? If it was, then SPKG.txt was not updated when it moved to 8. Sorry about that, if I did overlook this. I agree it is confusing, if this is so. 

For it to also be merged, and the release manager not notice, seems a bit strange. 

Dave



---

archive/issue_comments_067502.json:
```json
{
    "body": "What I found was this.  On my own computer I have a p8 with the following changelog entry:\n\n```\n### eclib-20080310.p8 (John Cremona, January 6th, 2009)\n * Change to debugging output in procs/p2points.cc (not relevant for Sage)\n * Change to pdivs() in procs/marith.cc (not relevant for Sage)\n```\nNow, whatever that was about, it was not relevant for Sage (either referred to functions not used by anything wrapped in Sage, or under compiler options which Sage does not use), and presumably for that reason I did not make a ticket for it to replace the (then) standard p7 in Sage.\n\nI guess the thing for me to do now is to make a p9 which has both the changes I made in my p8 and the ones you made, and get it into Sage.  I have to keep the version of the source files which are used by Sage in sync with the versions I have, otherwise I'll go mad.",
    "created_at": "2010-01-24T19:59:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7814#issuecomment-67502",
    "user": "https://github.com/JohnCremona"
}
```

What I found was this.  On my own computer I have a p8 with the following changelog entry:

```
### eclib-20080310.p8 (John Cremona, January 6th, 2009)
 * Change to debugging output in procs/p2points.cc (not relevant for Sage)
 * Change to pdivs() in procs/marith.cc (not relevant for Sage)
```
Now, whatever that was about, it was not relevant for Sage (either referred to functions not used by anything wrapped in Sage, or under compiler options which Sage does not use), and presumably for that reason I did not make a ticket for it to replace the (then) standard p7 in Sage.

I guess the thing for me to do now is to make a p9 which has both the changes I made in my p8 and the ones you made, and get it into Sage.  I have to keep the version of the source files which are used by Sage in sync with the versions I have, otherwise I'll go mad.
