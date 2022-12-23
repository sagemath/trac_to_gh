# Issue 5261: Straigten out some annoyances with the OSX Sage.app bundle

archive/issues_005261.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  kcrisman\n\nThis is somewhat of a multi issue ticket, but I don't think that doing all four of them individually will give us much of a benefit.\n\n* default the name to Sage-x.y.z.app - that way you can have many Sage releases in parallel :) \n* fix a bug that causes the app to fail to start if the name of the app contains spaces \n* remove the extra copyright work in credits as well as give credit to \"William Stein and the Sage Development Team\" \n* do not put the app skeleton in a tar.gz in the ext repo since it makes applying patches very expensive and opaque \n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5261\n\n",
    "created_at": "2009-02-14T00:09:23Z",
    "labels": [
        "porting",
        "major",
        "bug"
    ],
    "title": "Straigten out some annoyances with the OSX Sage.app bundle",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5261",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  kcrisman

This is somewhat of a multi issue ticket, but I don't think that doing all four of them individually will give us much of a benefit.

* default the name to Sage-x.y.z.app - that way you can have many Sage releases in parallel :) 
* fix a bug that causes the app to fail to start if the name of the app contains spaces 
* remove the extra copyright work in credits as well as give credit to "William Stein and the Sage Development Team" 
* do not put the app skeleton in a tar.gz in the ext repo since it makes applying patches very expensive and opaque 


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5261





---

archive/issue_comments_040378.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-14T13:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5261#issuecomment-40378",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040379.json:
```json
{
    "body": "One more point from #5254, not to be forgotten (no discussion on sage-devel yet):\n\nWhat do you think of putting in the name also the dependency \"Intel vs. PPC\" resp. \"32Bit vs. 64Bit\"?",
    "created_at": "2009-02-17T22:21:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5261#issuecomment-40379",
    "user": "GeorgSWeber"
}
```

One more point from #5254, not to be forgotten (no discussion on sage-devel yet):

What do you think of putting in the name also the dependency "Intel vs. PPC" resp. "32Bit vs. 64Bit"?



---

archive/issue_comments_040380.json:
```json
{
    "body": "Replying to [comment:3 GeorgSWeber]:\n> One more point from #5254, not to be forgotten (no discussion on sage-devel yet):\n> \n> What do you think of putting in the name also the dependency \"Intel vs. PPC\" resp. \"32Bit vs. 64Bit\"?\n\nIt might happen, but it is something bigger, i.e. we should add a check in the startup script that this is the right arch to begin with, i.e. it should be another ticket altogether.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-17T22:24:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5261#issuecomment-40380",
    "user": "mabshoff"
}
```

Replying to [comment:3 GeorgSWeber]:
> One more point from #5254, not to be forgotten (no discussion on sage-devel yet):
> 
> What do you think of putting in the name also the dependency "Intel vs. PPC" resp. "32Bit vs. 64Bit"?

It might happen, but it is something bigger, i.e. we should add a check in the startup script that this is the right arch to begin with, i.e. it should be another ticket altogether.

Cheers,

Michael



---

archive/issue_comments_040381.json:
```json
{
    "body": "Better luck in 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T02:26:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5261#issuecomment-40381",
    "user": "mabshoff"
}
```

Better luck in 3.4.1.

Cheers,

Michael



---

archive/issue_comments_040382.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-11-28T09:05:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5261#issuecomment-40382",
    "user": "iandrus"
}
```

Attachment



---

archive/issue_comments_040383.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-28T09:12:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5261#issuecomment-40383",
    "user": "iandrus"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_040384.json:
```json
{
    "body": "The patch (spaces-5261.patch) requires that the patch at #7546 be applied first.  \n\nThis patch is a hack to ensure there are no spaces in the path.  It would be much better to fix the components that don't support it, but there are too many of them for me to be confident that I found them all.\n\nIt also does the location checking from #5254, but I don't actually think it's necessary with the hack above.\n\nThe naming Sage-x.y.z and changing from tar.gz were taken care of in #7546.\n\nSomeone with a better understanding of the copyright situation should change data/extcode/sage/ext/mac-app/Sage.app/Contents/Info.plist (it's an xml file) in two places.",
    "created_at": "2009-11-28T09:12:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5261#issuecomment-40384",
    "user": "iandrus"
}
```

The patch (spaces-5261.patch) requires that the patch at #7546 be applied first.  

This patch is a hack to ensure there are no spaces in the path.  It would be much better to fix the components that don't support it, but there are too many of them for me to be confident that I found them all.

It also does the location checking from #5254, but I don't actually think it's necessary with the hack above.

The naming Sage-x.y.z and changing from tar.gz were taken care of in #7546.

Someone with a better understanding of the copyright situation should change data/extcode/sage/ext/mac-app/Sage.app/Contents/Info.plist (it's an xml file) in two places.



---

archive/issue_comments_040385.json:
```json
{
    "body": "The naming in #7546 works fine.\n\nLocation changes seem to work okay, I'll put in final positive review once I've checked a few more things.\n\nCopyright is now #7622, naming for PPC/Intel is #7623.",
    "created_at": "2009-12-08T16:17:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5261#issuecomment-40385",
    "user": "kcrisman"
}
```

The naming in #7546 works fine.

Location changes seem to work okay, I'll put in final positive review once I've checked a few more things.

Copyright is now #7622, naming for PPC/Intel is #7623.



---

archive/issue_comments_040386.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-08T16:44:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5261#issuecomment-40386",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_040387.json:
```json
{
    "body": "Unfortunately, if I rename the app bundle to have a space, things don't work.  I misread the stuff above - now I understand what the problem was. \n\nI am renaming the ticket, and hopefully this will be possible to fix still.",
    "created_at": "2009-12-08T16:44:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5261#issuecomment-40387",
    "user": "kcrisman"
}
```

Unfortunately, if I rename the app bundle to have a space, things don't work.  I misread the stuff above - now I understand what the problem was. 

I am renaming the ticket, and hopefully this will be possible to fix still.



---

archive/issue_comments_040388.json:
```json
{
    "body": "Sorry, I must have made a mistake in which app bundle to use - it works!  On both PPC and Macintel, though occasionally I get weird cookie issues, presumably not directly related, which a reload fixes.",
    "created_at": "2009-12-08T16:51:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5261#issuecomment-40388",
    "user": "kcrisman"
}
```

Sorry, I must have made a mistake in which app bundle to use - it works!  On both PPC and Macintel, though occasionally I get weird cookie issues, presumably not directly related, which a reload fixes.



---

archive/issue_comments_040389.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-08T16:51:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5261#issuecomment-40389",
    "user": "kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_040390.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-08T16:51:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5261#issuecomment-40390",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_040391.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-09T02:44:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5261#issuecomment-40391",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_040392.json:
```json
{
    "body": "Just to check, I did end up trying an Intel build on a PPC finally. It runs sage-location and then gives messages like\n\n```\n/tmp/sage-map-app/local/bin/python: /tmp/sage-map-app/local/bin/python: cannot execute binary file\n```\n\nSo presumably this is what we want?  Or should there be a better error message?",
    "created_at": "2009-12-17T17:01:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5261#issuecomment-40392",
    "user": "kcrisman"
}
```

Just to check, I did end up trying an Intel build on a PPC finally. It runs sage-location and then gives messages like

```
/tmp/sage-map-app/local/bin/python: /tmp/sage-map-app/local/bin/python: cannot execute binary file
```

So presumably this is what we want?  Or should there be a better error message?
