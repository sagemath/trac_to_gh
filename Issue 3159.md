# Issue 3159: [with patch; needs review] Patch adding soname to ntl shared library

archive/issues_003159.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  f.r.bissey@massey.ac.nz\n\nFran\u00e7ois Bissey and I merged our patches for adding library versioning and a soname to ntl's shared library and for building the static library without -fPIC and the shared library with -fPIC, and tested that they work for Debian and Gentoo builds.  I believe that if this patch were applied upstream, SAGE would be able to stop patch the ntl makefile as well.  I'm submitting it here so that it can be tested for a standard SAGE build, so we can be sure the patch works before submitting it to Victor Shoup.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3159\n\n",
    "created_at": "2008-05-11T16:56:36Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "[with patch; needs review] Patch adding soname to ntl shared library",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3159",
    "user": "@timabbott"
}
```
Assignee: mabshoff

CC:  f.r.bissey@massey.ac.nz

François Bissey and I merged our patches for adding library versioning and a soname to ntl's shared library and for building the static library without -fPIC and the shared library with -fPIC, and tested that they work for Debian and Gentoo builds.  I believe that if this patch were applied upstream, SAGE would be able to stop patch the ntl makefile as well.  I'm submitting it here so that it can be tested for a standard SAGE build, so we can be sure the patch works before submitting it to Victor Shoup.


Issue created by migration from https://trac.sagemath.org/ticket/3159





---

archive/issue_comments_021912.json:
```json
{
    "body": "Attachment [ntl-dynamic-library.patch](tarball://root/attachments/some-uuid/ticket3159/ntl-dynamic-library.patch) by @timabbott created at 2008-05-11 16:58:37",
    "created_at": "2008-05-11T16:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3159#issuecomment-21912",
    "user": "@timabbott"
}
```

Attachment [ntl-dynamic-library.patch](tarball://root/attachments/some-uuid/ticket3159/ntl-dynamic-library.patch) by @timabbott created at 2008-05-11 16:58:37



---

archive/issue_comments_021913.json:
```json
{
    "body": "Hi Tim, Francois, \n\nthe patch looks good, but as is it needs some changes to our spkg-install. I also noticed some other issues with some scripts in to the src directory, i.e. all shell scripts are missing a shebang, so that causes trouble with csh in some instances. Once I got those sorted out I will respin our spkg and merge this patch while I am at it.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-11T20:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3159#issuecomment-21913",
    "user": "mabshoff"
}
```

Hi Tim, Francois, 

the patch looks good, but as is it needs some changes to our spkg-install. I also noticed some other issues with some scripts in to the src directory, i.e. all shell scripts are missing a shebang, so that causes trouble with csh in some instances. Once I got those sorted out I will respin our spkg and merge this patch while I am at it.

Cheers,

Michael



---

archive/issue_comments_021914.json:
```json
{
    "body": "Mea culpa! One of us should at least have thought about the spkg-install,\nwe were more concerned that it would work correctly with our distros and that\nit was \"minimal\". Good thing is now libntl.a is correctly compiled without\n-fpic and libntl.so is now completely compiled with -fpic.\nI attach a tentative patch for spkg-install.\n\nCheers,\nFrancois",
    "created_at": "2008-05-11T20:46:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3159#issuecomment-21914",
    "user": "@kiwifb"
}
```

Mea culpa! One of us should at least have thought about the spkg-install,
we were more concerned that it would work correctly with our distros and that
it was "minimal". Good thing is now libntl.a is correctly compiled without
-fpic and libntl.so is now completely compiled with -fpic.
I attach a tentative patch for spkg-install.

Cheers,
Francois



---

archive/issue_comments_021915.json:
```json
{
    "body": "Attachment [spkg-install.patch](tarball://root/attachments/some-uuid/ticket3159/spkg-install.patch) by mabshoff created at 2008-05-11 21:20:07\n\nI have fixed a small couple issues with the patch in\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.2/alpha0/ntl-5.4.2.p3.spkg\n\nI did not patch src/src/mfile, but the one in patches, so the new Debian package as well as the ebuild needs to take that into consideration. The spkg builds fine on OSX and Linux, so positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-11T21:20:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3159#issuecomment-21915",
    "user": "mabshoff"
}
```

Attachment [spkg-install.patch](tarball://root/attachments/some-uuid/ticket3159/spkg-install.patch) by mabshoff created at 2008-05-11 21:20:07

I have fixed a small couple issues with the patch in

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.2/alpha0/ntl-5.4.2.p3.spkg

I did not patch src/src/mfile, but the one in patches, so the new Debian package as well as the ebuild needs to take that into consideration. The spkg builds fine on OSX and Linux, so positive review.

Cheers,

Michael



---

archive/issue_comments_021916.json:
```json
{
    "body": "One more thing: When creating symbolic links in spkg-install do not make those links absolute since they will break Sage once it is moved or install to another location. I fixed that and a couple other things, so I am taking partial credit on this ticket :)\n\nCheers,\n\nMichael",
    "created_at": "2008-05-11T21:56:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3159#issuecomment-21916",
    "user": "mabshoff"
}
```

One more thing: When creating symbolic links in spkg-install do not make those links absolute since they will break Sage once it is moved or install to another location. I fixed that and a couple other things, so I am taking partial credit on this ticket :)

Cheers,

Michael



---

archive/issue_comments_021917.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha0",
    "created_at": "2008-05-11T22:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3159#issuecomment-21917",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.alpha0



---

archive/issue_comments_021918.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-11T22:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3159#issuecomment-21918",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021919.json:
```json
{
    "body": "I'll remember that. It was a _tentative_ patch :)",
    "created_at": "2008-05-11T22:32:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3159#issuecomment-21919",
    "user": "@kiwifb"
}
```

I'll remember that. It was a _tentative_ patch :)



---

archive/issue_comments_021920.json:
```json
{
    "body": "I noticed the spkg-install script now has the current NTL version number in it; I'm attaching a patch that copies libntl*.so that should avoid having to update the patch every time there's a new NTL release.",
    "created_at": "2008-05-20T17:26:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3159#issuecomment-21920",
    "user": "@timabbott"
}
```

I noticed the spkg-install script now has the current NTL version number in it; I'm attaching a patch that copies libntl*.so that should avoid having to update the patch every time there's a new NTL release.



---

archive/issue_comments_021921.json:
```json
{
    "body": "Attachment [ntl-forget-version.patch](tarball://root/attachments/some-uuid/ticket3159/ntl-forget-version.patch) by @timabbott created at 2008-05-20 17:26:51",
    "created_at": "2008-05-20T17:26:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3159#issuecomment-21921",
    "user": "@timabbott"
}
```

Attachment [ntl-forget-version.patch](tarball://root/attachments/some-uuid/ticket3159/ntl-forget-version.patch) by @timabbott created at 2008-05-20 17:26:51
