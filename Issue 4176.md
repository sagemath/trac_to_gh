# Issue 4176: matplotlib build failure due to broken tcl/tk detection

archive/issues_004176.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @jaapspies\n\n```\nBUILDING MATPLOTLIB \n            matplotlib: 0.98.3 \n                python: 2.5.2 (r252:60911, Sep 23 2008, 17:09:57) \n[GCC \n                        4.3.0 20080428 (Red Hat 4.3.0-8)] \n              platform: linux2 \nREQUIRED DEPENDENCIES \n                 numpy: 1.1.0 \n             freetype2: 9.16.3 \nOPTIONAL BACKEND DEPENDENCIES \n                libpng: 1.2.29 \nTraceback (most recent call last): \n  File \"setup.py\", line 125, in <module> \n    if check_for_tk() or (options['build_tkagg'] is True): \n  File \"/home/abhishek/sage-3.1.2/spkg/build/matplotlib-0.98.3.p1/src/ \nsetupext.py\", line 846, in check_for_tk \n    explanation = add_tk_flags(module) \n  File \"/home/abhishek/sage-3.1.2/spkg/build/matplotlib-0.98.3.p1/src/ \nsetupext.py\", line 1106, in add_tk_flags \n    module.libraries.extend(['tk' + tk_ver, 'tcl' + tk_ver]) \nUnboundLocalError: local variable 'tk_ver' referenced before \nassignment \nError building matplotlib package. \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4176\n\n",
    "created_at": "2008-09-23T18:12:53Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "matplotlib build failure due to broken tcl/tk detection",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4176",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @jaapspies

```
BUILDING MATPLOTLIB 
            matplotlib: 0.98.3 
                python: 2.5.2 (r252:60911, Sep 23 2008, 17:09:57) 
[GCC 
                        4.3.0 20080428 (Red Hat 4.3.0-8)] 
              platform: linux2 
REQUIRED DEPENDENCIES 
                 numpy: 1.1.0 
             freetype2: 9.16.3 
OPTIONAL BACKEND DEPENDENCIES 
                libpng: 1.2.29 
Traceback (most recent call last): 
  File "setup.py", line 125, in <module> 
    if check_for_tk() or (options['build_tkagg'] is True): 
  File "/home/abhishek/sage-3.1.2/spkg/build/matplotlib-0.98.3.p1/src/ 
setupext.py", line 846, in check_for_tk 
    explanation = add_tk_flags(module) 
  File "/home/abhishek/sage-3.1.2/spkg/build/matplotlib-0.98.3.p1/src/ 
setupext.py", line 1106, in add_tk_flags 
    module.libraries.extend(['tk' + tk_ver, 'tcl' + tk_ver]) 
UnboundLocalError: local variable 'tk_ver' referenced before 
assignment 
Error building matplotlib package. 
```

Issue created by migration from https://trac.sagemath.org/ticket/4176





---

archive/issue_comments_030235.json:
```json
{
    "body": "The issue came up in http://groups.google.com/group/sage-support/t/1ee74c5c3b1a391",
    "created_at": "2008-09-23T18:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4176#issuecomment-30235",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The issue came up in http://groups.google.com/group/sage-support/t/1ee74c5c3b1a391



---

archive/issue_comments_030236.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-23T18:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4176#issuecomment-30236",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030237.json:
```json
{
    "body": "The issue has also been reported in http://groups.google.com/group/sage-support/t/a44e084a94b72724\n\nSome more info: This also happens with\n\n```\nit's scientific linux 4.2, but have seen it on newer systems (will \nhave alook again) \nMachine: Linux fwnc7122.wks.gorlaeus.net 2.6.9-67.0.15.ELsmp #1 SMP \nWed May 7 04:33:01 CDT 2008 i686 i686 i386 GNU/Linux \nif you want I can send the install.log \n-eiso\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-11-21T20:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4176#issuecomment-30237",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The issue has also been reported in http://groups.google.com/group/sage-support/t/a44e084a94b72724

Some more info: This also happens with

```
it's scientific linux 4.2, but have seen it on newer systems (will 
have alook again) 
Machine: Linux fwnc7122.wks.gorlaeus.net 2.6.9-67.0.15.ELsmp #1 SMP 
Wed May 7 04:33:01 CDT 2008 i686 i686 i386 GNU/Linux 
if you want I can send the install.log 
-eiso
```

Cheers,

Michael



---

archive/issue_comments_030238.json:
```json
{
    "body": "And it is also broken on the freshly release Fedora Core 10:\n\n```\nBUILDING MATPLOTLIB \n             matplotlib: 0.98.3 \n                 python: 2.5.2 (r252:60911, Nov 25 2008, 20:08:09)  [GCC \n                         4.3.2 20081105 (Red Hat 4.3.2-7)] \n               platform: linux2 \nREQUIRED DEPENDENCIES \n                  numpy: 1.2.0 \n              freetype2: 9.18.3 \nOPTIONAL BACKEND DEPENDENCIES \n                 libpng: 1.2.33 \nTraceback (most recent call last): \n   File \"setup.py\", line 125, in <module> \n     if check_for_tk() or (options['build_tkagg'] is True): \n   File \"/home/jaap/Download/sage-3.2.1.alpha0/spkg/build/matplotlib-0.98.3.p2/src/ setupext.py\", \nline 846, in check_for_tk \n     explanation = add_tk_flags(module) \n   File \"/home/jaap/Download/sage-3.2.1.alpha0/spkg/build/matplotlib-0.98.3.p2/src/ setupext.py\", \nline 1106, in add_tk_flags \n     module.libraries.extend(['tk' + tk_ver, 'tcl' + tk_ver]) \nUnboundLocalError: local variable 'tk_ver' referenced before assignment \nError building matplotlib package. \n```\nSo let's make this a blocker.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-25T20:20:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4176#issuecomment-30238",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

And it is also broken on the freshly release Fedora Core 10:

```
BUILDING MATPLOTLIB 
             matplotlib: 0.98.3 
                 python: 2.5.2 (r252:60911, Nov 25 2008, 20:08:09)  [GCC 
                         4.3.2 20081105 (Red Hat 4.3.2-7)] 
               platform: linux2 
REQUIRED DEPENDENCIES 
                  numpy: 1.2.0 
              freetype2: 9.18.3 
OPTIONAL BACKEND DEPENDENCIES 
                 libpng: 1.2.33 
Traceback (most recent call last): 
   File "setup.py", line 125, in <module> 
     if check_for_tk() or (options['build_tkagg'] is True): 
   File "/home/jaap/Download/sage-3.2.1.alpha0/spkg/build/matplotlib-0.98.3.p2/src/ setupext.py", 
line 846, in check_for_tk 
     explanation = add_tk_flags(module) 
   File "/home/jaap/Download/sage-3.2.1.alpha0/spkg/build/matplotlib-0.98.3.p2/src/ setupext.py", 
line 1106, in add_tk_flags 
     module.libraries.extend(['tk' + tk_ver, 'tcl' + tk_ver]) 
UnboundLocalError: local variable 'tk_ver' referenced before assignment 
Error building matplotlib package. 
```
So let's make this a blocker.

Cheers,

Michael



---

archive/issue_comments_030239.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-11-25T20:20:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4176#issuecomment-30239",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_030240.json:
```json
{
    "body": "New spkg at http://sage.math.washington.edu/home/was/patches/matplotlib-0.98.3.p3.spkg\n\nI don't have access to a system to test for the problem or if this fixes it.  I just read the relevant source code, and there is *clearly* a bug in upstream, which this new spkg fixes.",
    "created_at": "2008-11-26T05:27:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4176#issuecomment-30240",
    "user": "https://github.com/williamstein"
}
```

New spkg at http://sage.math.washington.edu/home/was/patches/matplotlib-0.98.3.p3.spkg

I don't have access to a system to test for the problem or if this fixes it.  I just read the relevant source code, and there is *clearly* a bug in upstream, which this new spkg fixes.



---

archive/issue_comments_030241.json:
```json
{
    "body": "That ain't no patch :)\n\nCheers,\n\nMichael",
    "created_at": "2008-11-26T06:17:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4176#issuecomment-30241",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

That ain't no patch :)

Cheers,

Michael



---

archive/issue_comments_030242.json:
```json
{
    "body": "Jaap,\n\nsince you are the man with the box that fails please try the spkg William posted.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-26T09:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4176#issuecomment-30242",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Jaap,

since you are the man with the box that fails please try the spkg William posted.

Cheers,

Michael



---

archive/issue_comments_030243.json:
```json
{
    "body": "The spkg worked for me!\n\n\n```\nreal\t2m8.649s\nuser\t1m32.105s\nsys\t0m5.449s\nSuccessfully installed matplotlib-0.98.3.p3\nNow cleaning up tmp files.\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing matplotlib-0.98.3.p3.spkg\n\n\n\n```\n\nJaap\n\nSo positive review!",
    "created_at": "2008-11-26T16:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4176#issuecomment-30243",
    "user": "https://github.com/jaapspies"
}
```

The spkg worked for me!


```
real	2m8.649s
user	1m32.105s
sys	0m5.449s
Successfully installed matplotlib-0.98.3.p3
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing matplotlib-0.98.3.p3.spkg



```

Jaap

So positive review!



---

archive/issue_comments_030244.json:
```json
{
    "body": "changed Cc: to jsp",
    "created_at": "2008-11-26T18:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4176#issuecomment-30244",
    "user": "https://github.com/jaapspies"
}
```

changed Cc: to jsp



---

archive/issue_comments_030245.json:
```json
{
    "body": "fix typo",
    "created_at": "2008-11-26T19:25:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4176#issuecomment-30245",
    "user": "https://github.com/williamstein"
}
```

fix typo



---

archive/issue_comments_030246.json:
```json
{
    "body": "Spkg looks good to me, i.e. changes to SPKG.txt and so on. The only change I did was to update \n\n* patches/setupext.py.diff\n\nto reflect the fixes done by William to setupext.py. I always check the diff in between src and patches since that makes applying fixes from our end to upstream somewhat easier once we upgrade an spkg. \n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T02:19:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4176#issuecomment-30246",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Spkg looks good to me, i.e. changes to SPKG.txt and so on. The only change I did was to update 

* patches/setupext.py.diff

to reflect the fixes done by William to setupext.py. I always check the diff in between src and patches since that makes applying fixes from our end to upstream somewhat easier once we upgrade an spkg. 

Cheers,

Michael



---

archive/issue_comments_030247.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha2",
    "created_at": "2008-11-27T02:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4176#issuecomment-30247",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.alpha2



---

archive/issue_events_009479.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-27T02:21:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4176",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4176#event-9479"
}
```



---

archive/issue_comments_030248.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-27T02:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4176#issuecomment-30248",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030249.json:
```json
{
    "body": "The fix should obviously go upstream. I have a FreeBSD 7 build fix that I will submit in the not too distant future. I will also send this patch upstream then.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T02:26:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4176#issuecomment-30249",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The fix should obviously go upstream. I have a FreeBSD 7 build fix that I will submit in the not too distant future. I will also send this patch upstream then.

Cheers,

Michael
