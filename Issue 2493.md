# Issue 2493: Updated experimental vtk spkg (vtk-5.0.4.spkg)

archive/issues_002493.json:
```json
{
    "body": "Assignee: was\n\nUpdated to vtk-5.0.4\n\nNow compiles with GL2EPS enabled. So it is possible to save pictures as eps, ps and pdf files.\n\nDepency cmake updated to cmake-2.4.8\n\nFiles see:\n\n```\nhttp://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.0/cmake-2.4.8.spkg\nhttp://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.0/vtk-5.0.4.spkg\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2493\n\n",
    "created_at": "2008-03-12T14:44:00Z",
    "labels": [
        "graphics",
        "minor",
        "enhancement"
    ],
    "title": "Updated experimental vtk spkg (vtk-5.0.4.spkg)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2493",
    "user": "jsp"
}
```
Assignee: was

Updated to vtk-5.0.4

Now compiles with GL2EPS enabled. So it is possible to save pictures as eps, ps and pdf files.

Depency cmake updated to cmake-2.4.8

Files see:

```
http://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.0/cmake-2.4.8.spkg
http://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.0/vtk-5.0.4.spkg
```



Issue created by migration from https://trac.sagemath.org/ticket/2493





---

archive/issue_comments_016890.json:
```json
{
    "body": "Files:\n\nhttp://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.0/cmake-2.4.8.spkg\n\nhttp://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.0/vtk-5.0.4.spkg",
    "created_at": "2008-03-12T14:45:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2493#issuecomment-16890",
    "user": "jsp"
}
```

Files:

http://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.0/cmake-2.4.8.spkg

http://sage.math.washington.edu/home/jsp/SPKGS/mayavi_2.1.0/vtk-5.0.4.spkg



---

archive/issue_comments_016891.json:
```json
{
    "body": "I think reviewing this is easy. In experimental there are already cmake-2.4.7 and vtk-5.0.3\n\nThis are only minor updates to the latest versions.\n\nWith one exception: vtk-5.0.4 comes now with GL3EPS enabled! Making it possible to save\nfigures as eps, ps and pdf files.\n\nThis update is needed for the mayavi_2.1.1 package!",
    "created_at": "2008-03-15T19:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2493#issuecomment-16891",
    "user": "jsp"
}
```

I think reviewing this is easy. In experimental there are already cmake-2.4.7 and vtk-5.0.3

This are only minor updates to the latest versions.

With one exception: vtk-5.0.4 comes now with GL3EPS enabled! Making it possible to save
figures as eps, ps and pdf files.

This update is needed for the mayavi_2.1.1 package!



---

archive/issue_comments_016892.json:
```json
{
    "body": "I used these packages to upgrade from earlier versions of Jaap's packages; the installations went perfectly, and my code (which uses wxPython, vtk, and tvtk (from mayavi)) worked fine after the upgrade.\n\nDebian testing 32-bit x86.",
    "created_at": "2008-03-20T20:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2493#issuecomment-16892",
    "user": "cwitty"
}
```

I used these packages to upgrade from earlier versions of Jaap's packages; the installations went perfectly, and my code (which uses wxPython, vtk, and tvtk (from mayavi)) worked fine after the upgrade.

Debian testing 32-bit x86.



---

archive/issue_comments_016893.json:
```json
{
    "body": "Hi, \n\nI checked in the changes into the repo. The result is at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/experimental/vtk-5.0.4.p0.spkg\n\nI didn't look at SPKG.txt yet\n\nCheers,\n\nMichael",
    "created_at": "2008-03-22T05:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2493#issuecomment-16893",
    "user": "mabshoff"
}
```

Hi, 

I checked in the changes into the repo. The result is at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/experimental/vtk-5.0.4.p0.spkg

I didn't look at SPKG.txt yet

Cheers,

Michael



---

archive/issue_comments_016894.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-22T05:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2493#issuecomment-16894",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016895.json:
```json
{
    "body": "Merged both spkgs into the experimental spkg repo.",
    "created_at": "2008-03-22T05:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2493#issuecomment-16895",
    "user": "mabshoff"
}
```

Merged both spkgs into the experimental spkg repo.



---

archive/issue_comments_016896.json:
```json
{
    "body": "Replying to [comment:5 mabshoff]:\n> Hi, \n> \n> I checked in the changes into the repo. The result is at \n> \n> http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/experimental/vtk-5.0.4.p0.spkg\n> \n> I didn't look at SPKG.txt yet\n> \n\nThis spkg depends on cmake-2.4.8 (see spkg-install). Probably it will work also with cmake-2.4.7,\nwhich is already in experimental. But this should be reflected in the spkg-install file.\n\nJaap",
    "created_at": "2008-03-22T17:46:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2493#issuecomment-16896",
    "user": "jsp"
}
```

Replying to [comment:5 mabshoff]:
> Hi, 
> 
> I checked in the changes into the repo. The result is at 
> 
> http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/experimental/vtk-5.0.4.p0.spkg
> 
> I didn't look at SPKG.txt yet
> 

This spkg depends on cmake-2.4.8 (see spkg-install). Probably it will work also with cmake-2.4.7,
which is already in experimental. But this should be reflected in the spkg-install file.

Jaap
