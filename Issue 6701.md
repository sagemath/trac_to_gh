# Issue 6701: prereq-0.3.tar has many issues and needs updating.

archive/issues_006701.json:
```json
{
    "body": "Assignee: tbd\n\nThere are numerous sensible things the prereq-0.3.tar could do which it does not currently do. \n\n* The old version detects if gcc is version 3 or above, yet at least 4.0.1 is needed to build Sage. \n\n* The old version fails to let one use a non-GNU compiler. Whilst I realise such compilers are unsupported in Sage, it would be sensible to issue a warning and let people continue. The Sun compilers are better than gcc on Solaris - particularly for 64-bit code.  \n\n* The old version does not check if the versions of the GNU compilers are all the same. So if one sets CC to one version of gcc (say 4.4.0) and forgets to set CXX and/or SAGE_FORTRAN, this will not be detected. So older version of those might be found. Building some files with one version of gcc and other files with another will not work reliably (if at all)\n\n\n* I understand some version of 4.0.1 on OS X will build Sage, but an older release of the tools with gcc 4.0.1 will not. This problem is not detected. \n\n* The old configure.ac is not really written as configure.ac scripts are supposed to be written. It does not make sensible use of macros, but has inline code which is not even working well. \n\n\n* No doubt other things. \n\nI intend making an updated version of at least configure.ac which fixes these and any other possible build issues I can think of. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6701\n\n",
    "created_at": "2009-08-09T08:24:09Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "prereq-0.3.tar has many issues and needs updating.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6701",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

There are numerous sensible things the prereq-0.3.tar could do which it does not currently do. 

* The old version detects if gcc is version 3 or above, yet at least 4.0.1 is needed to build Sage. 

* The old version fails to let one use a non-GNU compiler. Whilst I realise such compilers are unsupported in Sage, it would be sensible to issue a warning and let people continue. The Sun compilers are better than gcc on Solaris - particularly for 64-bit code.  

* The old version does not check if the versions of the GNU compilers are all the same. So if one sets CC to one version of gcc (say 4.4.0) and forgets to set CXX and/or SAGE_FORTRAN, this will not be detected. So older version of those might be found. Building some files with one version of gcc and other files with another will not work reliably (if at all)


* I understand some version of 4.0.1 on OS X will build Sage, but an older release of the tools with gcc 4.0.1 will not. This problem is not detected. 

* The old configure.ac is not really written as configure.ac scripts are supposed to be written. It does not make sensible use of macros, but has inline code which is not even working well. 


* No doubt other things. 

I intend making an updated version of at least configure.ac which fixes these and any other possible build issues I can think of. 



Issue created by migration from https://trac.sagemath.org/ticket/6701





---

archive/issue_events_006936.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2009-10-07T15:43:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6701",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6701#event-6936"
}
```



---

archive/issue_comments_054950.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-07T15:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6701#issuecomment-54950",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
