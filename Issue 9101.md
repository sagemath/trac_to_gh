# Issue 9101: linbox reports "ERROR: BLAS not found!" on 64-bit SPARC build

archive/issues_009101.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  mvngu @jaapspies @jhpalmieri\n\nTrying to compile Sage as 64-bit on SPARC, I get an error with linbox:\n\n\n```\nchecking whether GMP is 4.0 or greater... yes\nchecking whether GMP was compiled with --enable-cxx... yes\nchecking for NTL >= 5.0... found\nchecking for GIVARO >= 3.2.10... found\nchecking whether to compile the sage interface... yes\nchecking for C interface to BLAS... not found\nchecking for others BLAS... not found\n\n*******************************************************************************\n ERROR: BLAS not found!\n\n BLAS routines are required for this library to compile. Please\n make sure BLAS are installed and specify its location with the option\n --with-blas=<lib> when running configure.\n*******************************************************************************\nError configuring linbox\n\nreal    0m32.070s\nuser    0m15.156s\nsys     0m12.915s\nsage: An error occurred while installing linbox-1.1.6.p3\n```\n\n\nNo such error occurs when building linbox on OpenSolaris in 64-bit mode. \n\nThis looks to me like it might be an error in spkg/standard/deps, as there is nothing there as far as I can see \n\n\n```\n$(INST)/$(LINBOX): $(BASE) $(INST)/$(MPIR) $(INST)/$(NTL) $(INST)/$(GIVARO) $(INST)/$(GSL) $(INST)/$(ATLAS)\n        $(SAGE_SPKG) $(LINBOX) 2>&1\n\n```\n\n\nto make linbox dependent on BLAS. The BLAS library is not failing to install - it does not try to install.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9101\n\n",
    "created_at": "2010-05-31T03:12:01Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "linbox reports \"ERROR: BLAS not found!\" on 64-bit SPARC build",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9101",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  mvngu @jaapspies @jhpalmieri

Trying to compile Sage as 64-bit on SPARC, I get an error with linbox:


```
checking whether GMP is 4.0 or greater... yes
checking whether GMP was compiled with --enable-cxx... yes
checking for NTL >= 5.0... found
checking for GIVARO >= 3.2.10... found
checking whether to compile the sage interface... yes
checking for C interface to BLAS... not found
checking for others BLAS... not found

*******************************************************************************
 ERROR: BLAS not found!

 BLAS routines are required for this library to compile. Please
 make sure BLAS are installed and specify its location with the option
 --with-blas=<lib> when running configure.
*******************************************************************************
Error configuring linbox

real    0m32.070s
user    0m15.156s
sys     0m12.915s
sage: An error occurred while installing linbox-1.1.6.p3
```


No such error occurs when building linbox on OpenSolaris in 64-bit mode. 

This looks to me like it might be an error in spkg/standard/deps, as there is nothing there as far as I can see 


```
$(INST)/$(LINBOX): $(BASE) $(INST)/$(MPIR) $(INST)/$(NTL) $(INST)/$(GIVARO) $(INST)/$(GSL) $(INST)/$(ATLAS)
        $(SAGE_SPKG) $(LINBOX) 2>&1

```


to make linbox dependent on BLAS. The BLAS library is not failing to install - it does not try to install.

Issue created by migration from https://trac.sagemath.org/ticket/9101





---

archive/issue_comments_084557.json:
```json
{
    "body": "I've since been told ATLAS is a blas library, so this should find ATLAS",
    "created_at": "2010-06-12T12:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9101#issuecomment-84557",
    "user": "drkirkby"
}
```

I've since been told ATLAS is a blas library, so this should find ATLAS



---

archive/issue_comments_084558.json:
```json
{
    "body": "Sure ATLAS is a BLAS, and LinBox should be able to find it. Was ATLAS correctly installed before LinBox? If so, could you post the spkg/build/linbox-1.1.6p3/src/config.log file in order to inverstigate for which reason did the configure test fail to compile.",
    "created_at": "2010-06-28T12:57:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9101#issuecomment-84558",
    "user": "@ClementPernet"
}
```

Sure ATLAS is a BLAS, and LinBox should be able to find it. Was ATLAS correctly installed before LinBox? If so, could you post the spkg/build/linbox-1.1.6p3/src/config.log file in order to inverstigate for which reason did the configure test fail to compile.



---

archive/issue_comments_084559.json:
```json
{
    "body": "On closer inspection of the linbox log file, I can see what is wrong. ATLAS has built 32-bit libraries, not 64-bit ones. This is a problem with ATLAS rather than linbox. \n\nThank you very much. I'm quite surprised I did not notice this. I think I've spent more time recently on my Xeon machine making sure the objects were all 64-bit, and overlooked the SPARC. \n\nDave",
    "created_at": "2010-06-28T13:45:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9101#issuecomment-84559",
    "user": "drkirkby"
}
```

On closer inspection of the linbox log file, I can see what is wrong. ATLAS has built 32-bit libraries, not 64-bit ones. This is a problem with ATLAS rather than linbox. 

Thank you very much. I'm quite surprised I did not notice this. I think I've spent more time recently on my Xeon machine making sure the objects were all 64-bit, and overlooked the SPARC. 

Dave



---

archive/issue_comments_084560.json:
```json
{
    "body": "This is invalid, as the problem was ATLAS, not linbox.",
    "created_at": "2010-07-14T08:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9101#issuecomment-84560",
    "user": "drkirkby"
}
```

This is invalid, as the problem was ATLAS, not linbox.



---

archive/issue_comments_084561.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-07-14T08:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9101#issuecomment-84561",
    "user": "drkirkby"
}
```

Resolution: invalid



---

archive/issue_comments_084562.json:
```json
{
    "body": "I'm reopening this, as it does indicate a problem in Sage. Although Linbox is not at fault, the issue still exists, and causes Linbox to fail to build. \n\nI've created #9508 to try to sort out the way the ATLAS libraries are built on Solaris, as they are handled completely differently to other platforms like Linux, OS X and FreeBSD. \n\nDave",
    "created_at": "2010-07-15T14:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9101#issuecomment-84562",
    "user": "drkirkby"
}
```

I'm reopening this, as it does indicate a problem in Sage. Although Linbox is not at fault, the issue still exists, and causes Linbox to fail to build. 

I've created #9508 to try to sort out the way the ATLAS libraries are built on Solaris, as they are handled completely differently to other platforms like Linux, OS X and FreeBSD. 

Dave



---

archive/issue_comments_084563.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2010-07-15T14:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9101#issuecomment-84563",
    "user": "drkirkby"
}
```

Resolution changed from invalid to 



---

archive/issue_comments_084564.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-07-15T14:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9101#issuecomment-84564",
    "user": "drkirkby"
}
```

Changing status from closed to new.



---

archive/issue_comments_084565.json:
```json
{
    "body": "Won't this be fixed by #9508?  If so, do we need both tickets open?",
    "created_at": "2010-07-15T22:45:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9101#issuecomment-84565",
    "user": "@jhpalmieri"
}
```

Won't this be fixed by #9508?  If so, do we need both tickets open?



---

archive/issue_comments_084566.json:
```json
{
    "body": "Replying to [comment:9 jhpalmieri]:\n> Won't this be fixed by #9508?  If so, do we need both tickets open?\n\nI would agree this will be fixed by #9508, but I'm not sure if this should be closed until #9508 is closed. My belief is the bug reported is still valid at this point in time. \n\nDave",
    "created_at": "2010-07-15T23:05:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9101#issuecomment-84566",
    "user": "drkirkby"
}
```

Replying to [comment:9 jhpalmieri]:
> Won't this be fixed by #9508?  If so, do we need both tickets open?

I would agree this will be fixed by #9508, but I'm not sure if this should be closed until #9508 is closed. My belief is the bug reported is still valid at this point in time. 

Dave



---

archive/issue_comments_084567.json:
```json
{
    "body": "I'm closing this since #9508 was closed.",
    "created_at": "2010-09-01T00:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9101#issuecomment-84567",
    "user": "@mwhansen"
}
```

I'm closing this since #9508 was closed.



---

archive/issue_comments_084568.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-09-01T00:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9101#issuecomment-84568",
    "user": "@mwhansen"
}
```

Resolution: invalid
