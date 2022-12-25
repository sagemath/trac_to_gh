# Issue 7553: document exactly where SAGE_FORTRAN is used

archive/issues_007553.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @mwhansen\n\nAs discussed at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/f59fc5f7aef7448a) thread, we need to document exactly where the environment variable `SAGE_FORTRAN` is used. The file README.txt mentions this environment variable. It should also say something about where exactly this variable is used.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7553\n\n",
    "created_at": "2009-11-29T08:47:51Z",
    "labels": [
        "component: documentation",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "document exactly where SAGE_FORTRAN is used",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7553",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mvngu

CC:  @mwhansen

As discussed at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/f59fc5f7aef7448a) thread, we need to document exactly where the environment variable `SAGE_FORTRAN` is used. The file README.txt mentions this environment variable. It should also say something about where exactly this variable is used.

Issue created by migration from https://trac.sagemath.org/ticket/7553





---

archive/issue_comments_064080.json:
```json
{
    "body": "The attachment `README.txt` is based on Sage 4.3.alpha0 and contains some notes about the `SAGE_FORTRAN` environment variable. I have listed William Stein as co-author since some of those notes are based on his responses at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/f59fc5f7aef7448a) thread. I also cleaned up the `README.txt` file, including:\n\n1. Fixing typos.\n2. Reformatting the text.\n\nThe file `README.txt` is found under `SAGE_ROOT`, which is not under revision control. There is no need to apply the attached patch `readme.patch`; it is there to show the differences between the old and new `README.txt` files. All you need to do is replace the `README.txt` file with the attached `README.txt`.",
    "created_at": "2009-11-29T09:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7553#issuecomment-64080",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The attachment `README.txt` is based on Sage 4.3.alpha0 and contains some notes about the `SAGE_FORTRAN` environment variable. I have listed William Stein as co-author since some of those notes are based on his responses at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/f59fc5f7aef7448a) thread. I also cleaned up the `README.txt` file, including:

1. Fixing typos.
2. Reformatting the text.

The file `README.txt` is found under `SAGE_ROOT`, which is not under revision control. There is no need to apply the attached patch `readme.patch`; it is there to show the differences between the old and new `README.txt` files. All you need to do is replace the `README.txt` file with the attached `README.txt`.



---

archive/issue_comments_064081.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-29T09:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7553#issuecomment-64081",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064082.json:
```json
{
    "body": "A couple of comments, one specific to the SAGE_FORTRAN, others more general. I believe the oppotunity should be taken to update the issue of gcc versions. The others can be left. \n\n == Specific to SAGE_FORTRAN == \n\nThe text:\n\n*\"If you're using Fortran on a platform without g95 binaries included e.g. Itanium, you must ..\"* \n\nis a bit ambiguous. Itanium is a processor, on which many operating systems run. I personally consider Windows and Linux different platforms, despite they can both run on x86 processors. \n\n* Microsoft Windows Server 2003 and 2008 runs on Itanium. \n* HP-UX runs on Itanium\n* IA-64 Linux runs on Itanium\n* Debian Linux runs on Itanium\n* Redhat runs on Itanium. \n\nIs this a specific linux distribution you mean that does not come with Fortran binaries? If so, I would state which, or put \"some linux distributions for Itanium\". I doubt there is not one Linux distribution that does not come with the binaries. \n\n* Solaris 10 does not ship with any Fortran binaries either, so I would add that as an example along with the Itanium. (Do not forget the number '10' there, as the latest OpenSolaris comes with Fortran binaries, though they are too old to build Sage). \n\nI think the SAGE_FORTRAN section should be after the information about supported and unsupported platforms. Currently the order is \n\n* SUPPORTED\n* FORTRAN\n* NOT OFFICIALLY SUPPORTED, BUT NEARLY WORKS\n* NOT SUPPORTED\n\nI would have kept all the platform specific things one after the other. \n\n == Important to add ==\n\nSomewhere I would mention you need gcc >=4.0.1. There is a discussion about this on Apple, but you do need >=4.0.1 on **any** platform. \n\n == Not specific to SAGE_FORTRAN, but perhaps worth fixing, or leave to another time. == \n\nUnder 'NOT SUPPORTED'\n\nI would HP-UX and say there is some effort made on both FreeBSD and HP-UX\n\ni.e. \n\nsomething like\n\nNOT SUPPORTED \n* Arch Linux\n* FreeBSD - port in progress. Further developers would speed the progress.  \n* Gentoo Linux\n* HP-UX  - a little work done. Further developers appreciated. \n* Microsoft Windows (via Cygwin)\n* Microsoft Windows (via Visual Studio C++)\n* OpenSolaris (aka Solaris 11). A port will be completed in 2010. \n(I put them in alphabetical order)\n\nIs it necessary to use clips on Solaris 10 x86?  I would have thought ECL would have built on that.  \n\nDave",
    "created_at": "2009-11-29T11:42:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7553#issuecomment-64082",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

A couple of comments, one specific to the SAGE_FORTRAN, others more general. I believe the oppotunity should be taken to update the issue of gcc versions. The others can be left. 

 == Specific to SAGE_FORTRAN == 

The text:

*"If you're using Fortran on a platform without g95 binaries included e.g. Itanium, you must .."* 

is a bit ambiguous. Itanium is a processor, on which many operating systems run. I personally consider Windows and Linux different platforms, despite they can both run on x86 processors. 

* Microsoft Windows Server 2003 and 2008 runs on Itanium. 
* HP-UX runs on Itanium
* IA-64 Linux runs on Itanium
* Debian Linux runs on Itanium
* Redhat runs on Itanium. 

Is this a specific linux distribution you mean that does not come with Fortran binaries? If so, I would state which, or put "some linux distributions for Itanium". I doubt there is not one Linux distribution that does not come with the binaries. 

* Solaris 10 does not ship with any Fortran binaries either, so I would add that as an example along with the Itanium. (Do not forget the number '10' there, as the latest OpenSolaris comes with Fortran binaries, though they are too old to build Sage). 

I think the SAGE_FORTRAN section should be after the information about supported and unsupported platforms. Currently the order is 

* SUPPORTED
* FORTRAN
* NOT OFFICIALLY SUPPORTED, BUT NEARLY WORKS
* NOT SUPPORTED

I would have kept all the platform specific things one after the other. 

 == Important to add ==

Somewhere I would mention you need gcc >=4.0.1. There is a discussion about this on Apple, but you do need >=4.0.1 on **any** platform. 

 == Not specific to SAGE_FORTRAN, but perhaps worth fixing, or leave to another time. == 

Under 'NOT SUPPORTED'

I would HP-UX and say there is some effort made on both FreeBSD and HP-UX

i.e. 

something like

NOT SUPPORTED 
* Arch Linux
* FreeBSD - port in progress. Further developers would speed the progress.  
* Gentoo Linux
* HP-UX  - a little work done. Further developers appreciated. 
* Microsoft Windows (via Cygwin)
* Microsoft Windows (via Visual Studio C++)
* OpenSolaris (aka Solaris 11). A port will be completed in 2010. 
(I put them in alphabetical order)

Is it necessary to use clips on Solaris 10 x86?  I would have thought ECL would have built on that.  

Dave



---

archive/issue_comments_064083.json:
```json
{
    "body": "See #7565 for a related ticket.",
    "created_at": "2009-11-30T23:25:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7553#issuecomment-64083",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

See #7565 for a related ticket.



---

archive/issue_comments_064084.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-01T09:39:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7553#issuecomment-64084",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064085.json:
```json
{
    "body": "based on #7565",
    "created_at": "2009-12-01T11:24:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7553#issuecomment-64085",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

based on #7565



---

archive/issue_comments_064086.json:
```json
{
    "body": "Attachment [readme.patch](tarball://root/attachments/some-uuid/ticket7553/readme.patch) by mvngu created at 2009-12-01 11:25:15\n\ndifferences between old and new README.txt; do not apply",
    "created_at": "2009-12-01T11:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7553#issuecomment-64086",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [readme.patch](tarball://root/attachments/some-uuid/ticket7553/readme.patch) by mvngu created at 2009-12-01 11:25:15

differences between old and new README.txt; do not apply



---

archive/issue_comments_064087.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-01T11:32:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7553#issuecomment-64087",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064088.json:
```json
{
    "body": "A new `README.txt` is attached. It is based on #7565. The file `readme.patch` shows the differences between the `README.txt` at #7565 and the attached `README.txt`. Do not apply that patch. The new `README.txt` includes the following changes:\n\n1. Clean up the formatting of the file.\n2. Fix various typos.\n3. Document exactly where the `SAGE_FORTRAN` variable is used.\n4. Incorporate David Kirkby's suggestions.",
    "created_at": "2009-12-01T11:32:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7553#issuecomment-64088",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

A new `README.txt` is attached. It is based on #7565. The file `readme.patch` shows the differences between the `README.txt` at #7565 and the attached `README.txt`. Do not apply that patch. The new `README.txt` includes the following changes:

1. Clean up the formatting of the file.
2. Fix various typos.
3. Document exactly where the `SAGE_FORTRAN` variable is used.
4. Incorporate David Kirkby's suggestions.



---

archive/issue_events_007783.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-12-02T19:11:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7553",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7553#event-7783"
}
```



---

archive/issue_comments_064089.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-12-02T19:11:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7553#issuecomment-64089",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_064090.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-02T19:11:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7553#issuecomment-64090",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
