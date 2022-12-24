# Issue 9025: PALP is building 32-bit on OpenSolaris - probably other platforms too.

archive/issues_009025.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  jsp\n\nAttempting a 64-bit build of Sage on OpenSolaris I noticed several files are built 32-bit, even though SAGE64 is set to yes. This includes the following files. \n\n\n```\nrkirkby@hawk:~/sage-4.4.2$ file local/bin/*.x | grep 32\nlocal/bin/class.x:\tELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped\nlocal/bin/cws.x:\tELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped\nlocal/bin/nef.x:\tELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped\nlocal/bin/poly.x:\tELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped\n\n```\n\n\nwhich are all part of 'PALP' There is nothing in the Makefile to force a 64-bit build on any platform, so I would not be surprised if only 32-bit objects were built on OS X or anywhere else where SAGE64 needs to be set to \"yes\" to get a 64-bit build.\n\nFixing this should be quite easy.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9025\n\n",
    "created_at": "2010-05-23T23:57:34Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "title": "PALP is building 32-bit on OpenSolaris - probably other platforms too.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9025",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  jsp

Attempting a 64-bit build of Sage on OpenSolaris I noticed several files are built 32-bit, even though SAGE64 is set to yes. This includes the following files. 


```
rkirkby@hawk:~/sage-4.4.2$ file local/bin/*.x | grep 32
local/bin/class.x:	ELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped
local/bin/cws.x:	ELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped
local/bin/nef.x:	ELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped
local/bin/poly.x:	ELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped

```


which are all part of 'PALP' There is nothing in the Makefile to force a 64-bit build on any platform, so I would not be surprised if only 32-bit objects were built on OS X or anywhere else where SAGE64 needs to be set to "yes" to get a 64-bit build.

Fixing this should be quite easy.

Issue created by migration from https://trac.sagemath.org/ticket/9025





---

archive/issue_comments_083500.json:
```json
{
    "body": "Attachment [PALP-64-bit.patch](tarball://root/attachments/some-uuid/ticket9025/PALP-64-bit.patch) by drkirkby created at 2010-05-24 00:31:12\n\nMercurial patch",
    "created_at": "2010-05-24T00:31:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9025#issuecomment-83500",
    "user": "drkirkby"
}
```

Attachment [PALP-64-bit.patch](tarball://root/attachments/some-uuid/ticket9025/PALP-64-bit.patch) by drkirkby created at 2010-05-24 00:31:12

Mercurial patch



---

archive/issue_comments_083501.json:
```json
{
    "body": "This was easily fixed by adding the flag -m64. I did this via 'sed' as it was the simplest way to change a few bytes in a large file. The revised package may be found here:\n\nhttp://boxen.math.washington.edu/home/kirkby/patches/palp-1.1.p2.spkg\n\nNow the files build 64-bit:\n\n\n```\ndrkirkby@hawk:~/sage-4.4.2$ file local/bin/*.x\nlocal/bin/class.x:\tELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped\nlocal/bin/cws.x:\tELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped\nlocal/bin/nef.x:\tELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped\nlocal/bin/poly.x:\tELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped\n```\n",
    "created_at": "2010-05-24T00:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9025#issuecomment-83501",
    "user": "drkirkby"
}
```

This was easily fixed by adding the flag -m64. I did this via 'sed' as it was the simplest way to change a few bytes in a large file. The revised package may be found here:

http://boxen.math.washington.edu/home/kirkby/patches/palp-1.1.p2.spkg

Now the files build 64-bit:


```
drkirkby@hawk:~/sage-4.4.2$ file local/bin/*.x
local/bin/class.x:	ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped
local/bin/cws.x:	ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped
local/bin/nef.x:	ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped
local/bin/poly.x:	ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped
```




---

archive/issue_comments_083502.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-24T00:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9025#issuecomment-83502",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083503.json:
```json
{
    "body": "For other OpenSolaris issues, see #9026",
    "created_at": "2010-05-24T18:23:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9025#issuecomment-83503",
    "user": "drkirkby"
}
```

For other OpenSolaris issues, see #9026



---

archive/issue_comments_083504.json:
```json
{
    "body": "This needs rebasing.",
    "created_at": "2010-06-05T22:11:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9025#issuecomment-83504",
    "user": "drkirkby"
}
```

This needs rebasing.



---

archive/issue_comments_083505.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-05T22:11:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9025#issuecomment-83505",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_083506.json:
```json
{
    "body": "Replying to [comment:5 drkirkby]:\n> This needs rebasing. \n\nWhat do you mean? Isn't renaming enough?\n\nJaap",
    "created_at": "2010-06-14T12:18:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9025#issuecomment-83506",
    "user": "jsp"
}
```

Replying to [comment:5 drkirkby]:
> This needs rebasing. 

What do you mean? Isn't renaming enough?

Jaap



---

archive/issue_comments_083507.json:
```json
{
    "body": "Someone has made other changes, so they need to be considered. It is not as simple as just renaming this package. I dobut it is rocket science though - leave it with me. It will be ready for review later today. I have a chess game in half an hour, so do not have time to do it now. \n\nIt is better if I do it, rather than you. Then you can review it. \n\nDave",
    "created_at": "2010-06-14T12:29:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9025#issuecomment-83507",
    "user": "drkirkby"
}
```

Someone has made other changes, so they need to be considered. It is not as simple as just renaming this package. I dobut it is rocket science though - leave it with me. It will be ready for review later today. I have a chess game in half an hour, so do not have time to do it now. 

It is better if I do it, rather than you. Then you can review it. 

Dave



---

archive/issue_comments_083508.json:
```json
{
    "body": "It's here now, awaiting review. \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/palp-1.1.p3.spkg",
    "created_at": "2010-06-14T13:02:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9025#issuecomment-83508",
    "user": "drkirkby"
}
```

It's here now, awaiting review. 

http://boxen.math.washington.edu/home/kirkby/patches/palp-1.1.p3.spkg



---

archive/issue_comments_083509.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-14T13:02:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9025#issuecomment-83509",
    "user": "drkirkby"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083510.json:
```json
{
    "body": "Ok, on OpenSolaris:\n\n\n```\nFinished installing palp-1.1.p3.spkg\n-bash-4.0$ file local/bin/*.x | grep 32\n-bash-4.0$ file local/bin/*.x | grep 64\nlocal/bin/class.x:      ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped\nlocal/bin/cws.x:        ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped\nlocal/bin/nef.x:        ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped\nlocal/bin/poly.x:       ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped\n-bash-4.0$ \n\n```\n\n\nPositive review.\n\nJaap",
    "created_at": "2010-06-14T13:40:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9025#issuecomment-83510",
    "user": "jsp"
}
```

Ok, on OpenSolaris:


```
Finished installing palp-1.1.p3.spkg
-bash-4.0$ file local/bin/*.x | grep 32
-bash-4.0$ file local/bin/*.x | grep 64
local/bin/class.x:      ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped
local/bin/cws.x:        ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped
local/bin/nef.x:        ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped
local/bin/poly.x:       ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped
-bash-4.0$ 

```


Positive review.

Jaap



---

archive/issue_comments_083511.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-14T13:40:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9025#issuecomment-83511",
    "user": "jsp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083512.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-25T15:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9025#issuecomment-83512",
    "user": "rlm"
}
```

Resolution: fixed
