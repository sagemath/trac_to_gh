# Issue 6476: [with spkg, positive review] upgrade Singular to 3.1.0.4

archive/issues_006476.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  aginiewicz polybori @johnperry-math @williamstein\n\nSee #6470 and #6362 for a bit of history...\n\nIssue created by migration from https://trac.sagemath.org/ticket/6476\n\n",
    "closed_at": "2009-08-24T04:46:45Z",
    "created_at": "2009-07-07T20:16:38Z",
    "labels": [
        "component: distribution"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with spkg, positive review] upgrade Singular to 3.1.0.4",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6476",
    "user": "https://github.com/rlmill"
}
```
Assignee: tbd

CC:  aginiewicz polybori @johnperry-math @williamstein

See #6470 and #6362 for a bit of history...

Issue created by migration from https://trac.sagemath.org/ticket/6476





---

archive/issue_comments_052246.json:
```json
{
    "body": "The thread http://lists.apple.com/archives/unix-porting/2006/Aug/msg00022.html started years ago by Justin C. Walker on how to build Singular on OS X (for Sage!) brought some more insights.\n\nIf one uses \"g++ -dynamiclib ...\" instead of \"libtool -dynamic ...\" (note the \"lib\" at the ending of \"-dynamiclib\", this seems to superspecial for g++ instead of just gcc on Mac OS X) to build libsingular.dylib, then together with the changes I already wrote in #6470, the modified 3.1.0.4 singular spkg from #6362 (as included in Sage-4.1.rc0) seems finally to (build and also to) work on OS X.\n\nBut one not only needs to adapt \"src.Singular.Makefile.in\" which is already in the patch directory, but also add some \"src.Singular.config.in\" there and even \"src.Singular.config\" because although the Makefile is created from Makefile.in in the install process, config is *not* updated from config.in. This will take some more time, and testing also for the PPC Darwin target. I see if can do that soon and upload a new spkg for review, but probably not in the next days.",
    "created_at": "2009-07-15T22:26:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6476#issuecomment-52246",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

The thread http://lists.apple.com/archives/unix-porting/2006/Aug/msg00022.html started years ago by Justin C. Walker on how to build Singular on OS X (for Sage!) brought some more insights.

If one uses "g++ -dynamiclib ..." instead of "libtool -dynamic ..." (note the "lib" at the ending of "-dynamiclib", this seems to superspecial for g++ instead of just gcc on Mac OS X) to build libsingular.dylib, then together with the changes I already wrote in #6470, the modified 3.1.0.4 singular spkg from #6362 (as included in Sage-4.1.rc0) seems finally to (build and also to) work on OS X.

But one not only needs to adapt "src.Singular.Makefile.in" which is already in the patch directory, but also add some "src.Singular.config.in" there and even "src.Singular.config" because although the Makefile is created from Makefile.in in the install process, config is *not* updated from config.in. This will take some more time, and testing also for the PPC Darwin target. I see if can do that soon and upload a new spkg for review, but probably not in the next days.



---

archive/issue_comments_052247.json:
```json
{
    "body": "I completely lost track.\n\nCan someone please point me to the most recent 3-1-0-4 SPKG I should start working on? I am visiting the Singular group right now so I have them within reach for the week.",
    "created_at": "2009-07-22T08:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6476#issuecomment-52247",
    "user": "https://github.com/malb"
}
```

I completely lost track.

Can someone please point me to the most recent 3-1-0-4 SPKG I should start working on? I am visiting the Singular group right now so I have them within reach for the week.



---

archive/issue_comments_052248.json:
```json
{
    "body": "The last \"official\" Singular 3-1-0-4 spkg was the one included in Sage-4.1.rc0. Since I couldn't find a still working link, I uploaded it here: http://sage.math.washington.edu/home/weberg/spkg/singular-3-1-0-4-20090703.spkg.\n\nAs far as I remember, this spkg did build and work fine, except for OS X. I managed to make it build with rather minor changes, but then Sage wouldn't start on OS X. After looking more deeply into it, I managed to produce a version that both did build and work fine on my MacIntel. I uploaded this version here:\nhttp://sage.math.washington.edu/home/weberg/spkg/singular-3-1-0-4-20090715.spkg\n\nHowever, this is \"work in progress\", the last changes were done in a quick and hackish way, e.g. altering directly the files under /src/ inside the spkg. The remaining work would be to:\n1. clean this up, e.g. create new files under /patch/, make sage-install copy these over, update mercurial repository, ...\n2. make (and test) these changes also for MacPPC\n\nSorry, I didn't get around doing this yet, so you'll have to look into the half-cooked new spkg and search for the \"newest\" files via modification time. If you have questions, please ask.",
    "created_at": "2009-07-22T15:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6476#issuecomment-52248",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

The last "official" Singular 3-1-0-4 spkg was the one included in Sage-4.1.rc0. Since I couldn't find a still working link, I uploaded it here: http://sage.math.washington.edu/home/weberg/spkg/singular-3-1-0-4-20090703.spkg.

As far as I remember, this spkg did build and work fine, except for OS X. I managed to make it build with rather minor changes, but then Sage wouldn't start on OS X. After looking more deeply into it, I managed to produce a version that both did build and work fine on my MacIntel. I uploaded this version here:
http://sage.math.washington.edu/home/weberg/spkg/singular-3-1-0-4-20090715.spkg

However, this is "work in progress", the last changes were done in a quick and hackish way, e.g. altering directly the files under /src/ inside the spkg. The remaining work would be to:
1. clean this up, e.g. create new files under /patch/, make sage-install copy these over, update mercurial repository, ...
2. make (and test) these changes also for MacPPC

Sorry, I didn't get around doing this yet, so you'll have to look into the half-cooked new spkg and search for the "newest" files via modification time. If you have questions, please ask.



---

archive/issue_comments_052249.json:
```json
{
    "body": "Hi, I produced a new SPKG which should contain all your changes (but we fixed a bug in your fix of GNUmakefile.in). I've uploaded it to\n\n  http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090723.spkg\n\nI'll run tests and silently update that file (until it works). I'll report back when I consider it 'stable'. I'll have to check whether it works with GCC 4.4.\n\nCredit for this ticket goes to GeorgSWeber, Michael Brickenstein, Hans Sch\u00f6nemann, aginiewicz and Martin Albrecht.",
    "created_at": "2009-07-23T07:41:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6476#issuecomment-52249",
    "user": "https://github.com/malb"
}
```

Hi, I produced a new SPKG which should contain all your changes (but we fixed a bug in your fix of GNUmakefile.in). I've uploaded it to

  http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090723.spkg

I'll run tests and silently update that file (until it works). I'll report back when I consider it 'stable'. I'll have to check whether it works with GCC 4.4.

Credit for this ticket goes to GeorgSWeber, Michael Brickenstein, Hans Schönemann, aginiewicz and Martin Albrecht.



---

archive/issue_comments_052250.json:
```json
{
    "body": "It seems Georg's fix to replace `-dynamic` with `-dynamiclib` is not universally valid (i.e. on bsd.math it wouldn't compile with his change applied)\n\naginiewicz can you send me a patch with your GCC 4.4 patches, your server is down and I can't track down your changes.",
    "created_at": "2009-07-23T11:33:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6476#issuecomment-52250",
    "user": "https://github.com/malb"
}
```

It seems Georg's fix to replace `-dynamic` with `-dynamiclib` is not universally valid (i.e. on bsd.math it wouldn't compile with his change applied)

aginiewicz can you send me a patch with your GCC 4.4 patches, your server is down and I can't track down your changes.



---

archive/issue_comments_052251.json:
```json
{
    "body": "There version at \n\n   http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090723.spkg\n\nseems to pass tests now on anything but OSX where the `__eprintf` bug shows. As mentioned above, Georg's fix doesn't work for me.",
    "created_at": "2009-07-23T14:01:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6476#issuecomment-52251",
    "user": "https://github.com/malb"
}
```

There version at 

   http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090723.spkg

seems to pass tests now on anything but OSX where the `__eprintf` bug shows. As mentioned above, Georg's fix doesn't work for me.



---

archive/issue_comments_052252.json:
```json
{
    "body": "There version at \n\n  http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090723.spkg\n\nnow seems to work on sage.math and bsd.math ... finally. Please test with a GCC 4.4 compiler.",
    "created_at": "2009-07-23T14:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6476#issuecomment-52252",
    "user": "https://github.com/malb"
}
```

There version at 

  http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090723.spkg

now seems to work on sage.math and bsd.math ... finally. Please test with a GCC 4.4 compiler.



---

archive/issue_comments_052253.json:
```json
{
    "body": "I tried your latest spkg with gcc 4.4.1 and did not get far.  The install log is at\n\nhttp://www.ms.unimelb.edu.au/~aghitza/singular_install.log",
    "created_at": "2009-08-18T02:32:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6476#issuecomment-52253",
    "user": "https://github.com/aghitza"
}
```

I tried your latest spkg with gcc 4.4.1 and did not get far.  The install log is at

http://www.ms.unimelb.edu.au/~aghitza/singular_install.log



---

archive/issue_comments_052254.json:
```json
{
    "body": "Alright, it seems I missed some GCC 4.4 changes. I will provide an updated SPKG (directly instead of patches because the next version of Singular will have exactly the same changes anyway). Is there any machine where I can try GCC 4.4 myself to speed up the process?",
    "created_at": "2009-08-18T09:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6476#issuecomment-52254",
    "user": "https://github.com/malb"
}
```

Alright, it seems I missed some GCC 4.4 changes. I will provide an updated SPKG (directly instead of patches because the next version of Singular will have exactly the same changes anyway). Is there any machine where I can try GCC 4.4 myself to speed up the process?



---

archive/issue_comments_052255.json:
```json
{
    "body": "Alright, try this: http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090818.spkg",
    "created_at": "2009-08-18T09:48:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6476#issuecomment-52255",
    "user": "https://github.com/malb"
}
```

Alright, try this: http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090818.spkg



---

archive/issue_comments_052256.json:
```json
{
    "body": "Martin,\n\nI currently only have GCC 4.4 on my laptop and on a rather slow machine at the office.  If you need access to it, I can make an account for you there.\n\nAnyway, the new spkg builds fine for me.  I am running tests now.",
    "created_at": "2009-08-18T10:29:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6476#issuecomment-52256",
    "user": "https://github.com/aghitza"
}
```

Martin,

I currently only have GCC 4.4 on my laptop and on a rather slow machine at the office.  If you need access to it, I can make an account for you there.

Anyway, the new spkg builds fine for me.  I am running tests now.



---

archive/issue_comments_052257.json:
```json
{
    "body": "Alex, since it builds now I think I won't need access. But thanks for the offer!",
    "created_at": "2009-08-18T11:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6476#issuecomment-52257",
    "user": "https://github.com/malb"
}
```

Alex, since it builds now I think I won't need access. But thanks for the offer!



---

archive/issue_comments_052258.json:
```json
{
    "body": "So far, looks good.  I should be done with testing by tomorrow morning.  There is one very minor issue: the most recent changelog entry in SPKG.txt talks about 3-1-0-4-20090723, where it probably should say something about 3-1-0-4-20090818.  Could you fix this and replace the spkg?",
    "created_at": "2009-08-18T13:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6476#issuecomment-52258",
    "user": "https://github.com/aghitza"
}
```

So far, looks good.  I should be done with testing by tomorrow morning.  There is one very minor issue: the most recent changelog entry in SPKG.txt talks about 3-1-0-4-20090723, where it probably should say something about 3-1-0-4-20090818.  Could you fix this and replace the spkg?



---

archive/issue_comments_052259.json:
```json
{
    "body": "done, the SPKG is at the same place with the same name.",
    "created_at": "2009-08-18T13:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6476#issuecomment-52259",
    "user": "https://github.com/malb"
}
```

done, the SPKG is at the same place with the same name.



---

archive/issue_comments_052260.json:
```json
{
    "body": "OK, I think this is good to go.  Positive review.",
    "created_at": "2009-08-19T07:26:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6476#issuecomment-52260",
    "user": "https://github.com/aghitza"
}
```

OK, I think this is good to go.  Positive review.



---

archive/issue_events_015294.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-24T04:46:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6476",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6476#event-15294"
}
```



---

archive/issue_comments_052261.json:
```json
{
    "body": "Merged `singular-3-1-0-4-20090818.spkg` in the standard spkg repository.",
    "created_at": "2009-08-24T04:46:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6476#issuecomment-52261",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged `singular-3-1-0-4-20090818.spkg` in the standard spkg repository.



---

archive/issue_comments_052262.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-24T04:46:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6476#issuecomment-52262",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
