# Issue 9273: doctest elliptic_curves/BSD.py reports "file not found"

archive/issues_009273.json:
```json
{
    "body": "Assignee: cremona\n\nCC:  robertwb rlm was jhpalmieri\n\n#9127 was supposed to fix this, but it seems the fix is not complete. \n\n## Hardware & associated software\n\n* Sun Blade 1000\n* 2 x 900 MHz UltraSPARC III+ CPUs\n* 2 GB RAM\n* Solaris 10 03/2005 (first release of Solaris 10)\n* gcc 4.4.3 (uses Sun linker and assembler)\n\n == Sage version ==\n* 4.4.4.alpha1\n\n\n == The error ==\n\n```\nsage -t  -long devel/sage/sage/calculus/riemann.pyx\n         [712.7 s]\n\n-------------------------------------------------------------\n\nThe following tests failed:\n\n        sage -t  -long devel/sage/sage/schemes/elliptic_curves/BSD.py # File not found\n-------------------------------------------------------------\nTotal time for all tests: 33947.4 seconds\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9273\n\n",
    "created_at": "2010-06-19T16:01:10Z",
    "labels": [
        "elliptic curves",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "doctest elliptic_curves/BSD.py reports \"file not found\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9273",
    "user": "drkirkby"
}
```
Assignee: cremona

CC:  robertwb rlm was jhpalmieri

#9127 was supposed to fix this, but it seems the fix is not complete. 

## Hardware & associated software

* Sun Blade 1000
* 2 x 900 MHz UltraSPARC III+ CPUs
* 2 GB RAM
* Solaris 10 03/2005 (first release of Solaris 10)
* gcc 4.4.3 (uses Sun linker and assembler)

 == Sage version ==
* 4.4.4.alpha1


 == The error ==

```
sage -t  -long devel/sage/sage/calculus/riemann.pyx
         [712.7 s]

-------------------------------------------------------------

The following tests failed:

        sage -t  -long devel/sage/sage/schemes/elliptic_curves/BSD.py # File not found
-------------------------------------------------------------
Total time for all tests: 33947.4 seconds
```


Issue created by migration from https://trac.sagemath.org/ticket/9273





---

archive/issue_comments_087332.json:
```json
{
    "body": "This has nothing to do with the file `BSD.py`. It is a bug in the doctesting code, which is triggered (as William tells me) by lag times on file systems and the like. It starts testing before the doctesting file is created.\n\nDid you try running the tests again?",
    "created_at": "2010-06-22T16:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9273#issuecomment-87332",
    "user": "rlm"
}
```

This has nothing to do with the file `BSD.py`. It is a bug in the doctesting code, which is triggered (as William tells me) by lag times on file systems and the like. It starts testing before the doctesting file is created.

Did you try running the tests again?



---

archive/issue_comments_087333.json:
```json
{
    "body": "Replying to [comment:2 rlm]:\n> This has nothing to do with the file `BSD.py`. It is a bug in the doctesting code, which is triggered (as William tells me) by lag times on file systems and the like. It starts testing before the doctesting file is created.\n> \n> Did you try running the tests again?\n\nI run that test more than once and it failed more than once. \n\nNote although the machine is rather old (900 MHz CPUs), the disks are local, with a 2 Gbit/s fibre channel interface and 15,000 rpm, so the disk performance is probably better than most modern PCs. If the disks were on a NFS file system, I could perhaps understand that, but it seems unlikely with local disks like this. \n\nI managed to mess up my build (started a 64-bit build in the same directory as the 32-bit one!), so are rebuilding now. I'll try again once complete. \n\nDave",
    "created_at": "2010-06-22T16:35:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9273#issuecomment-87333",
    "user": "drkirkby"
}
```

Replying to [comment:2 rlm]:
> This has nothing to do with the file `BSD.py`. It is a bug in the doctesting code, which is triggered (as William tells me) by lag times on file systems and the like. It starts testing before the doctesting file is created.
> 
> Did you try running the tests again?

I run that test more than once and it failed more than once. 

Note although the machine is rather old (900 MHz CPUs), the disks are local, with a 2 Gbit/s fibre channel interface and 15,000 rpm, so the disk performance is probably better than most modern PCs. If the disks were on a NFS file system, I could perhaps understand that, but it seems unlikely with local disks like this. 

I managed to mess up my build (started a 64-bit build in the same directory as the 32-bit one!), so are rebuilding now. I'll try again once complete. 

Dave



---

archive/issue_comments_087334.json:
```json
{
    "body": "I just updated the technical details of the hardware in the description. I usually put the details, but not normally the disks. But in this case I thought it prudent to add it.",
    "created_at": "2010-06-22T17:35:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9273#issuecomment-87334",
    "user": "drkirkby"
}
```

I just updated the technical details of the hardware in the description. I usually put the details, but not normally the disks. But in this case I thought it prudent to add it.



---

archive/issue_comments_087335.json:
```json
{
    "body": "I've rebuilt this and tried BSD.py and it passes each time. I've no idea what the underlying problem may be, but the doc test has passed several times now. \n\nDave",
    "created_at": "2010-06-23T00:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9273#issuecomment-87335",
    "user": "drkirkby"
}
```

I've rebuilt this and tried BSD.py and it passes each time. I've no idea what the underlying problem may be, but the doc test has passed several times now. 

Dave



---

archive/issue_comments_087336.json:
```json
{
    "body": "Then I suggest we close this ticket.\n\nIs there a ticket for the \"file not found\" issue in general? It would be nice if there were a way to reproduce the issue...",
    "created_at": "2010-06-23T02:55:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9273#issuecomment-87336",
    "user": "rlm"
}
```

Then I suggest we close this ticket.

Is there a ticket for the "file not found" issue in general? It would be nice if there were a way to reproduce the issue...



---

archive/issue_comments_087337.json:
```json
{
    "body": "There is a ticket for \"file not found\" - see #9316.\n\nThe assumption being made on that ticket is that the real cause of the \"file not found\" message is a timeout. John Cremona says \n\n*The reason for the timeout was simply that I suspended my laptop for a couple of hours and then woke it up.*\n\nI'm personally not convinced that is the reason this test has failed for me. When BSD.py passes, it does so in around 205 seconds. SAGE_TIMEOUT is set to 1000 seconds and SAGE_TIMEOUT_LONG is set to 10000 seconds. Since the BSD.py test is marked as long, it would need to slow down by a factor of 48 (10000/205) before causing a timeout. My SPARC is quite and old machine and does not go to sleep in the same way some computers do. \n\nThere appears to be another test which is randomly failing in a different way - see #9310. \n\nI don't know what the cause(s) are but I'm less than convinced this is due to delays on file systems or processors going to sleep. \n\nI think the ticket should remain open until such time as it gets resolved. Being random in nature, it might not be easy to resolve.",
    "created_at": "2010-06-25T07:03:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9273#issuecomment-87337",
    "user": "drkirkby"
}
```

There is a ticket for "file not found" - see #9316.

The assumption being made on that ticket is that the real cause of the "file not found" message is a timeout. John Cremona says 

*The reason for the timeout was simply that I suspended my laptop for a couple of hours and then woke it up.*

I'm personally not convinced that is the reason this test has failed for me. When BSD.py passes, it does so in around 205 seconds. SAGE_TIMEOUT is set to 1000 seconds and SAGE_TIMEOUT_LONG is set to 10000 seconds. Since the BSD.py test is marked as long, it would need to slow down by a factor of 48 (10000/205) before causing a timeout. My SPARC is quite and old machine and does not go to sleep in the same way some computers do. 

There appears to be another test which is randomly failing in a different way - see #9310. 

I don't know what the cause(s) are but I'm less than convinced this is due to delays on file systems or processors going to sleep. 

I think the ticket should remain open until such time as it gets resolved. Being random in nature, it might not be easy to resolve.



---

archive/issue_comments_087338.json:
```json
{
    "body": "Changing keywords from \"\" to \"ecc2011\".",
    "created_at": "2011-09-16T13:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9273#issuecomment-87338",
    "user": "zimmerma"
}
```

Changing keywords from "" to "ecc2011".



---

archive/issue_comments_087339.json:
```json
{
    "body": "David, does this problem still happen?\n\nPaul",
    "created_at": "2011-09-16T13:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9273#issuecomment-87339",
    "user": "zimmerma"
}
```

David, does this problem still happen?

Paul



---

archive/issue_comments_087340.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2011-09-16T13:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9273#issuecomment-87340",
    "user": "zimmerma"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_087341.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2013-02-28T16:08:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9273#issuecomment-87341",
    "user": "jdemeyer"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_087342.json:
```json
{
    "body": "I have never seen this problem and in any case, the doctesting framework will be rewritten completely: #12415.",
    "created_at": "2013-02-28T16:08:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9273#issuecomment-87342",
    "user": "jdemeyer"
}
```

I have never seen this problem and in any case, the doctesting framework will be rewritten completely: #12415.



---

archive/issue_comments_087343.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-02-28T16:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9273#issuecomment-87343",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087344.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-03-07T08:17:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9273#issuecomment-87344",
    "user": "jdemeyer"
}
```

Resolution: invalid
