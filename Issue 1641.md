# Issue 1641: Make ATLAS restart build on tolerance error

archive/issues_001641.json:
```json
{
    "body": "Assignee: mabshoff\n\nWhen the ATLAS build fails due to tolerance errors we can restart the build by restarting the build process via \"make\". We should do it a set number of times, i.e. 5 and then finally fail. I have hit the problem repeatedly while building in a VMWare machine and have little to no control to prevent the issue from happening. \n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1641\n\n",
    "created_at": "2007-12-30T18:47:05Z",
    "labels": [
        "component: packages: standard",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Make ATLAS restart build on tolerance error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1641",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

When the ATLAS build fails due to tolerance errors we can restart the build by restarting the build process via "make". We should do it a set number of times, i.e. 5 and then finally fail. I have hit the problem repeatedly while building in a VMWare machine and have little to no control to prevent the issue from happening. 

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1641





---

archive/issue_comments_010404.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-31T10:24:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1641#issuecomment-10404",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010405.json:
```json
{
    "body": "This ought to be fixed via #5311.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T13:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1641#issuecomment-10405",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This ought to be fixed via #5311.

Cheers,

Michael



---

archive/issue_comments_010406.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-20T20:59:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1641#issuecomment-10406",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010407.json:
```json
{
    "body": "Fixed via #5311. This can probably be improved upon, but we will open another ticket once we get to this point.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T20:59:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1641#issuecomment-10407",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed via #5311. This can probably be improved upon, but we will open another ticket once we get to this point.

Cheers,

Michael



---

archive/issue_events_001799.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-20T20:59:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1641",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1641#event-1799"
}
```



---

archive/issue_comments_010408.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-02-21T03:38:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1641#issuecomment-10408",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_010409.json:
```json
{
    "body": "REFEREE REPORT:\n\n* There is a typo \"Restartig build for the first time\"\n\n* This patch doesn't work.  I tried this on my vmware farm and what happens is that you restart part of the build that fails, but other parts also fail later.  \n\n* I wonder if it would be better to simply wrap the whole spkg-install in a repeat timer instead of each little bit.  I.e., put the current spkg-install in another file, say spkg-install-script and then make spkg-install try to run spkg-install-script, then wait some amount of time, and try again up to n times.",
    "created_at": "2009-02-21T03:38:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1641#issuecomment-10409",
    "user": "https://github.com/williamstein"
}
```

REFEREE REPORT:

* There is a typo "Restartig build for the first time"

* This patch doesn't work.  I tried this on my vmware farm and what happens is that you restart part of the build that fails, but other parts also fail later.  

* I wonder if it would be better to simply wrap the whole spkg-install in a repeat timer instead of each little bit.  I.e., put the current spkg-install in another file, say spkg-install-script and then make spkg-install try to run spkg-install-script, then wait some amount of time, and try again up to n times.



---

archive/issue_comments_010410.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-02-21T03:38:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1641#issuecomment-10410",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_events_001800.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-02-21T03:38:52Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/1641",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1641#event-1800"
}
```



---

archive/issue_comments_010411.json:
```json
{
    "body": "Replying to [comment:5 was]:\n> REFEREE REPORT:\n> \n>  * There is a typo \"Restartig build for the first time\"\n\nOk.\n\n>  * This patch doesn't work.  I tried this on my vmware farm and what happens is that you restart part of the build that fails, but other parts also fail later.  \n\nThe failures you reported are unrelated to this script: For example the ubuntu64.out failure for 3.3.rc3:\n\n```\n<SNIP>\nATLAS install complete.  Examine \n<SNIP>\nFinished building ATLAS\n<SNIP>\nmake[3]: [install_lib] Error 1 (ignored)\nmake[3]: Leaving directory `/space/wstein/farm/sage-3.3.rc3/spkg/build/atlas-3.8.3/ATLAS-build'\nmake[2]: Leaving directory `/space/wstein/farm/sage-3.3.rc3/spkg/build/atlas-3.8.3/ATLAS-build'\nATLAS failed to build because your system is too heavily loaded to obtain accurate timing.\nPlease restart the build by typing make, when the load on your system has decreased.\n```\n\n \nSo ATLAS did finish tuning and some other error was triggered after the \"make install\" target, so this is not this tickets fault. \n\n>  * I wonder if it would be better to simply wrap the whole spkg-install in a repeat timer instead of each little bit.  I.e., put the current spkg-install in another file, say spkg-install-script and then make spkg-install try to run spkg-install-script, then wait some amount of time, and try again up to n times. \n\nIf you do that you will not reuse the tuning info, but start the tune from scratch each time. \n\nCheers,\n\nMichael",
    "created_at": "2009-02-21T05:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1641#issuecomment-10411",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:5 was]:
> REFEREE REPORT:
> 
>  * There is a typo "Restartig build for the first time"

Ok.

>  * This patch doesn't work.  I tried this on my vmware farm and what happens is that you restart part of the build that fails, but other parts also fail later.  

The failures you reported are unrelated to this script: For example the ubuntu64.out failure for 3.3.rc3:

```
<SNIP>
ATLAS install complete.  Examine 
<SNIP>
Finished building ATLAS
<SNIP>
make[3]: [install_lib] Error 1 (ignored)
make[3]: Leaving directory `/space/wstein/farm/sage-3.3.rc3/spkg/build/atlas-3.8.3/ATLAS-build'
make[2]: Leaving directory `/space/wstein/farm/sage-3.3.rc3/spkg/build/atlas-3.8.3/ATLAS-build'
ATLAS failed to build because your system is too heavily loaded to obtain accurate timing.
Please restart the build by typing make, when the load on your system has decreased.
```

 
So ATLAS did finish tuning and some other error was triggered after the "make install" target, so this is not this tickets fault. 

>  * I wonder if it would be better to simply wrap the whole spkg-install in a repeat timer instead of each little bit.  I.e., put the current spkg-install in another file, say spkg-install-script and then make spkg-install try to run spkg-install-script, then wait some amount of time, and try again up to n times. 

If you do that you will not reuse the tuning info, but start the tune from scratch each time. 

Cheers,

Michael



---

archive/issue_comments_010412.json:
```json
{
    "body": "Ok, I figured it out I think: on debian32 this happens: \n\n\n\n```\n   STAGE 2-1-5: GEMV TUNE \nmake -f Makefile INSTALL_LOG/dMVRES pre=d 2>&1 | ./xatlas_tee \nINSTALL_LOG/dMVTUNE.LOG \nmake[3]: *** [build] Error 255 \nmake[3]: Leaving directory `/space/wstein/farm/sage-3.3.rc3/spkg/build/ \natlas-3.8.3/ATLAS-build' \nmake[2]: *** [build] Error 2 \nmake[2]: Leaving directory `/space/wstein/farm/sage-3.3.rc3/spkg/build/ \natlas-3.8.3/ATLAS-build' \nATLAS failed - round 1 - sleeping  5 minutes \n```\n\nThen the restart kicks in and finishes the build. \n\n```\nRestartig build for the first time \nmake[2]: Entering directory `/space/wstein/farm/sage-3.3.rc3/spkg/ \nbuild/atlas-3.8.3/ATLAS-build' \nmake -f Make.top build \nmake[3]: Entering directory `/space/wstein/farm/sage-3.3.rc3/spkg/ \nbuild/atlas-3.8.3/ATLAS-build' \ncd bin/ ; make xatlas_install \n<SNIP> \n```\n\n\nBecause at some point there was  a failure the makefile errors out at \nthe very end even though it all worked. So the script you wrote is \nlikely to hit the same bug unless you completely clean out the ATLAS \nbuild directory. \n\nThe fix here is to figure out which file causes the tuning failure \nmessage in the end and to get rid of it before restart. \n\nThoughts? \n\nCheers,\n\nMichael",
    "created_at": "2009-02-21T05:17:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1641#issuecomment-10412",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, I figured it out I think: on debian32 this happens: 



```
   STAGE 2-1-5: GEMV TUNE 
make -f Makefile INSTALL_LOG/dMVRES pre=d 2>&1 | ./xatlas_tee 
INSTALL_LOG/dMVTUNE.LOG 
make[3]: *** [build] Error 255 
make[3]: Leaving directory `/space/wstein/farm/sage-3.3.rc3/spkg/build/ 
atlas-3.8.3/ATLAS-build' 
make[2]: *** [build] Error 2 
make[2]: Leaving directory `/space/wstein/farm/sage-3.3.rc3/spkg/build/ 
atlas-3.8.3/ATLAS-build' 
ATLAS failed - round 1 - sleeping  5 minutes 
```

Then the restart kicks in and finishes the build. 

```
Restartig build for the first time 
make[2]: Entering directory `/space/wstein/farm/sage-3.3.rc3/spkg/ 
build/atlas-3.8.3/ATLAS-build' 
make -f Make.top build 
make[3]: Entering directory `/space/wstein/farm/sage-3.3.rc3/spkg/ 
build/atlas-3.8.3/ATLAS-build' 
cd bin/ ; make xatlas_install 
<SNIP> 
```


Because at some point there was  a failure the makefile errors out at 
the very end even though it all worked. So the script you wrote is 
likely to hit the same bug unless you completely clean out the ATLAS 
build directory. 

The fix here is to figure out which file causes the tuning failure 
message in the end and to get rid of it before restart. 

Thoughts? 

Cheers,

Michael



---

archive/issue_comments_010413.json:
```json
{
    "body": "The latest spkg is at:\n\nhttp://sage.math.washington.edu/home/was/patches/atlas-3.8.3.p0.spkg\n\nTwo things need fixing:\n\n* spkg-install claims up to 10 tries, but max_tries is set to 5 :)\n* SPKG.txt overwrites my 3.8.3 entry, but William's changes need to be 3.8.3.p0:\n\n```\n-=== atlas-3.8.3 (Michael Abshoff, Januar 2nd, 2009) ===\n- * rebase against latest upstream (#5311)\n- * make ATLAS automatically restart build on tolerance error (#1641)\n+=== atlas-3.8.3 (William Stein, February 20, 2009) ===\n+ * implement up to 5 auto-restarts with random timeouts. \n```\n\n\nThe 3.8.3 entry also needs to be dated February 20th, but that was my bug.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-21T06:28:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1641#issuecomment-10413",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The latest spkg is at:

http://sage.math.washington.edu/home/was/patches/atlas-3.8.3.p0.spkg

Two things need fixing:

* spkg-install claims up to 10 tries, but max_tries is set to 5 :)
* SPKG.txt overwrites my 3.8.3 entry, but William's changes need to be 3.8.3.p0:

```
-=== atlas-3.8.3 (Michael Abshoff, Januar 2nd, 2009) ===
- * rebase against latest upstream (#5311)
- * make ATLAS automatically restart build on tolerance error (#1641)
+=== atlas-3.8.3 (William Stein, February 20, 2009) ===
+ * implement up to 5 auto-restarts with random timeouts. 
```


The 3.8.3 entry also needs to be dated February 20th, but that was my bug.

Cheers,

Michael



---

archive/issue_comments_010414.json:
```json
{
    "body": "The bug in my 3.8.3.spkg was actually not killing error* in ATLAS's build directory on restart:\n\n```\ncd $CUR/ATLAS-build\nif [ -f error* ]; then\n   echo \"ATLAS failed to build because your system is too heavily loaded to obtain accurate timing.\"\n   echo \"Please restart the build by typing make, when the load on your system has decreased.\"\n   exit 1\nfi\n```\n\n\nThat error message is wrong by the way since not every failure is due to timing issues - even though these days for ATLAS 99.9% of the time an error indicates a tolerance failure. \n\nI still think an incremental restart is better than start from scratch, i.e. think of being two hours into a tune on Sparc or Itanium and it blows up. I have made this #5328.",
    "created_at": "2009-02-21T07:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1641#issuecomment-10414",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The bug in my 3.8.3.spkg was actually not killing error* in ATLAS's build directory on restart:

```
cd $CUR/ATLAS-build
if [ -f error* ]; then
   echo "ATLAS failed to build because your system is too heavily loaded to obtain accurate timing."
   echo "Please restart the build by typing make, when the load on your system has decreased."
   exit 1
fi
```


That error message is wrong by the way since not every failure is due to timing issues - even though these days for ATLAS 99.9% of the time an error indicates a tolerance failure. 

I still think an incremental restart is better than start from scratch, i.e. think of being two hours into a tune on Sparc or Itanium and it blows up. I have made this #5328.



---

archive/issue_comments_010415.json:
```json
{
    "body": "I think the new spkg at \n\nhttp://sage.math.washington.edu/home/was/patches/atlas-3.8.3.p0.spkg\n\naddresses all of the above comments.",
    "created_at": "2009-02-21T08:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1641#issuecomment-10415",
    "user": "https://github.com/williamstein"
}
```

I think the new spkg at 

http://sage.math.washington.edu/home/was/patches/atlas-3.8.3.p0.spkg

addresses all of the above comments.



---

archive/issue_comments_010416.json:
```json
{
    "body": "Positive review. All my concerns have been addressed. \n\nCheers,\n\nMichael",
    "created_at": "2009-02-21T09:06:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1641#issuecomment-10416",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review. All my concerns have been addressed. 

Cheers,

Michael



---

archive/issue_comments_010417.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-21T09:42:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1641#issuecomment-10417",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010418.json:
```json
{
    "body": "Merged in Sage 3.3.final.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-21T09:42:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1641#issuecomment-10418",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.final.

Cheers,

Michael



---

archive/issue_events_001801.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-21T09:42:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1641",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1641#event-1801"
}
```
