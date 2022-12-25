# Issue 2754: plotting with frame=True and ymin/ymax sometimes is buggy as a Florida swamp in summer

archive/issues_002754.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  @jasongrout mvngu\n\n```\n\nOn Tue, Apr 1, 2008 at 7:29 AM, Axel <axelgrau@gmail.com> wrote:\n> \n>  How can I specify the range of y coordinates in a 2d plot? I tried\n>  \n>  show(plot(sin(x),-10,10),ymin=-0.5, ymax=0.5,frame=true)\n>  \n>  but the actual plot goes between -0.6, and 0.6, and the curve goes out\n>  of the frame.\n\nI think that's an honest-to-goodness *bug*.  For now you can try\nto workaround it sort of with:\n    show(plot(sin(x),-10,10),ymin=-0.41, ymax=0.41,frame=true)\nbut still the curve goes outside the frame.\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2754\n\n",
    "closed_at": "2009-09-29T15:58:29Z",
    "created_at": "2008-04-01T15:59:45Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "plotting with frame=True and ymin/ymax sometimes is buggy as a Florida swamp in summer",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2754",
    "user": "https://github.com/williamstein"
}
```
Assignee: @mwhansen

CC:  @jasongrout mvngu

```

On Tue, Apr 1, 2008 at 7:29 AM, Axel <axelgrau@gmail.com> wrote:
> 
>  How can I specify the range of y coordinates in a 2d plot? I tried
>  
>  show(plot(sin(x),-10,10),ymin=-0.5, ymax=0.5,frame=true)
>  
>  but the actual plot goes between -0.6, and 0.6, and the curve goes out
>  of the frame.

I think that's an honest-to-goodness *bug*.  For now you can try
to workaround it sort of with:
    show(plot(sin(x),-10,10),ymin=-0.41, ymax=0.41,frame=true)
but still the curve goes outside the frame.
```

Issue created by migration from https://trac.sagemath.org/ticket/2754





---

archive/issue_comments_018875.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-03T00:54:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2754#issuecomment-18875",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_018876.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2008-09-03T00:54:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2754#issuecomment-18876",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_018877.json:
```json
{
    "body": "This is now fixed, presumably with the new matplotlib.\n\nQuestion: is it possible to verify this in a doctest?  The problem is that show uses save, but the saved figure is just a png.",
    "created_at": "2009-09-29T14:52:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2754#issuecomment-18877",
    "user": "https://github.com/kcrisman"
}
```

This is now fixed, presumably with the new matplotlib.

Question: is it possible to verify this in a doctest?  The problem is that show uses save, but the saved figure is just a png.



---

archive/issue_comments_018878.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-29T15:50:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2754#issuecomment-18878",
    "user": "https://github.com/jasongrout"
}
```

Resolution: fixed



---

archive/issue_events_006386.json:
```json
{
    "actor": "https://github.com/jasongrout",
    "created_at": "2009-09-29T15:50:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2754",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2754#event-6386"
}
```



---

archive/issue_comments_018879.json:
```json
{
    "body": "Nope, I don't think a doctest makes much sense here, with our current framework.\n\nSometime, we'll probably use matplotlib's image testing framework...\n\nMinh, can you close this?  It works now on alpha.sagenb.org",
    "created_at": "2009-09-29T15:50:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2754#issuecomment-18879",
    "user": "https://github.com/jasongrout"
}
```

Nope, I don't think a doctest makes much sense here, with our current framework.

Sometime, we'll probably use matplotlib's image testing framework...

Minh, can you close this?  It works now on alpha.sagenb.org



---

archive/issue_comments_018880.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-09-29T15:50:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2754#issuecomment-18880",
    "user": "https://github.com/jasongrout"
}
```

Changing status from closed to reopened.



---

archive/issue_events_006387.json:
```json
{
    "actor": "https://github.com/jasongrout",
    "created_at": "2009-09-29T15:50:41Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/2754",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2754#event-6387"
}
```



---

archive/issue_comments_018881.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-09-29T15:50:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2754#issuecomment-18881",
    "user": "https://github.com/jasongrout"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_018882.json:
```json
{
    "body": "(oops, I didn't mean to close it---I don't know exactly what your procedure is for things to do when you close a ticket...)",
    "created_at": "2009-09-29T15:51:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2754#issuecomment-18882",
    "user": "https://github.com/jasongrout"
}
```

(oops, I didn't mean to close it---I don't know exactly what your procedure is for things to do when you close a ticket...)



---

archive/issue_comments_018883.json:
```json
{
    "body": "Attachment [plot-sin.png](tarball://root/attachments/some-uuid/ticket2754/plot-sin.png) by mvngu created at 2009-09-29 15:57:04\n\nbased on Sage 4.1.2.alpha4",
    "created_at": "2009-09-29T15:57:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2754#issuecomment-18883",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [plot-sin.png](tarball://root/attachments/some-uuid/ticket2754/plot-sin.png) by mvngu created at 2009-09-29 15:57:04

based on Sage 4.1.2.alpha4



---

archive/issue_events_006388.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-29T15:58:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2754",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2754#event-6388"
}
```



---

archive/issue_comments_018884.json:
```json
{
    "body": "I can confirm this is now fixed:\n\n```\n[mvngu@darkstar sage-4.1.2.alpha4]$ ./sage -br main\n\n----------------------------------------------------------\nsage: Building and installing modified Sage library files.\n\n\nInstalling c_lib\nscons: `install' is up to date.\nUpdating Cython code....\nTime to execute 0 commands: 2.50339508057e-05 seconds\nFinished compiling Cython code (time = 6.12911605835 seconds)\nrunning install\nrunning build\nrunning build_py\nrunning build_ext\nTotal time spent compiling C/C++ extensions:  0.919514894485 seconds.\nrunning install_lib\nrunning install_egg_info\nRemoving /home/mvngu/scratch/sandbox/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info\nWriting /home/mvngu/scratch/sandbox/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: show(plot(sin(x),-10,10),ymin=-0.5, ymax=0.5,frame=true)\n```\nThe resulting plot is attached.",
    "created_at": "2009-09-29T15:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2754#issuecomment-18884",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I can confirm this is now fixed:

```
[mvngu@darkstar sage-4.1.2.alpha4]$ ./sage -br main

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Time to execute 0 commands: 2.50339508057e-05 seconds
Finished compiling Cython code (time = 6.12911605835 seconds)
running install
running build
running build_py
running build_ext
Total time spent compiling C/C++ extensions:  0.919514894485 seconds.
running install_lib
running install_egg_info
Removing /home/mvngu/scratch/sandbox/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
Writing /home/mvngu/scratch/sandbox/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: show(plot(sin(x),-10,10),ymin=-0.5, ymax=0.5,frame=true)
```
The resulting plot is attached.



---

archive/issue_comments_018885.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-29T15:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2754#issuecomment-18885",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
