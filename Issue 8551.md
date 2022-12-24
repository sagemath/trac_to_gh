# Issue 8551: ace-5.0 package has gap version hardwired, etc.

archive/issues_008551.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  wdj\n\nthe gap version 4.4.10 is hardwired there, and few other things are wrong, e.g no SPKG.txt\nA new version with these fixes installs and on Sage >=4.3.3, can be found here:\nhttp://sage.math.washington.edu/home/dima/packages/ace-5.0.p1.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/8551\n\n",
    "created_at": "2010-03-17T06:33:10Z",
    "labels": [
        "packages: optional",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "ace-5.0 package has gap version hardwired, etc.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8551",
    "user": "dimpase"
}
```
Assignee: tbd

CC:  wdj

the gap version 4.4.10 is hardwired there, and few other things are wrong, e.g no SPKG.txt
A new version with these fixes installs and on Sage >=4.3.3, can be found here:
http://sage.math.washington.edu/home/dima/packages/ace-5.0.p1.spkg

Issue created by migration from https://trac.sagemath.org/ticket/8551





---

archive/issue_comments_077327.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-17T06:33:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8551#issuecomment-77327",
    "user": "dimpase"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077328.json:
```json
{
    "body": "and this too...\nBy the way, I don't see why ace ended up being a separate spkg.\nDo you know, by any chance?\nThanks,\nDima",
    "created_at": "2010-03-25T12:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8551#issuecomment-77328",
    "user": "dimpase"
}
```

and this too...
By the way, I don't see why ace ended up being a separate spkg.
Do you know, by any chance?
Thanks,
Dima



---

archive/issue_comments_077329.json:
```json
{
    "body": "Replying to [ticket:8551 dimpase]:\n> the gap version 4.4.10 is hardwired there, and few other things are wrong, e.g no SPKG.txt\n> \n> A new version, with these fixes installs and runs on Sage >=4.3.3, can be found here:\n> http://sage.math.washington.edu/home/dima/packages/ace-5.0.p1.spkg\n\n\nI think the link is wrong. http://boxen.math.washington.edu/home/dima/packages/\nhas no such spkg file.",
    "created_at": "2010-03-26T11:06:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8551#issuecomment-77329",
    "user": "wdj"
}
```

Replying to [ticket:8551 dimpase]:
> the gap version 4.4.10 is hardwired there, and few other things are wrong, e.g no SPKG.txt
> 
> A new version, with these fixes installs and runs on Sage >=4.3.3, can be found here:
> http://sage.math.washington.edu/home/dima/packages/ace-5.0.p1.spkg


I think the link is wrong. http://boxen.math.washington.edu/home/dima/packages/
has no such spkg file.



---

archive/issue_comments_077330.json:
```json
{
    "body": "Replying to [comment:4 wdj]:\n\n> > A new version, with these fixes installs and runs on Sage >=4.3.3, can be found here:\n> > http://sage.math.washington.edu/home/dima/packages/ace-5.0.p1.spkg\n> \n> \n> I think the link is wrong. http://boxen.math.washington.edu/home/dima/packages/\n> has no such spkg file.\n\nOops, sorry. Recovered from a daily backup and put back in place. The link works now. Long live backups!",
    "created_at": "2010-03-27T07:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8551#issuecomment-77330",
    "user": "dimpase"
}
```

Replying to [comment:4 wdj]:

> > A new version, with these fixes installs and runs on Sage >=4.3.3, can be found here:
> > http://sage.math.washington.edu/home/dima/packages/ace-5.0.p1.spkg
> 
> 
> I think the link is wrong. http://boxen.math.washington.edu/home/dima/packages/
> has no such spkg file.

Oops, sorry. Recovered from a daily backup and put back in place. The link works now. Long live backups!



---

archive/issue_comments_077331.json:
```json
{
    "body": "Replying to [comment:5 dimpase]:\n> Replying to [comment:4 wdj]:\n> \n\n...\n\n> \n> Oops, sorry. Recovered from a daily backup and put back in place. \n> The link works now. Long live backups!\n> \n\nWhere is the distribution license? It is not clear that we are\nlegally allowed to distribute this code. I did not see any C code written by\nHavas. Maybe he only contributed design ideas? Did you ask Ramsay \nif he licensed his C code under the GPL (or any code that allows for \nfree distribution) ... ?",
    "created_at": "2010-06-22T23:19:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8551#issuecomment-77331",
    "user": "wdj"
}
```

Replying to [comment:5 dimpase]:
> Replying to [comment:4 wdj]:
> 

...

> 
> Oops, sorry. Recovered from a daily backup and put back in place. 
> The link works now. Long live backups!
> 

Where is the distribution license? It is not clear that we are
legally allowed to distribute this code. I did not see any C code written by
Havas. Maybe he only contributed design ideas? Did you ask Ramsay 
if he licensed his C code under the GPL (or any code that allows for 
free distribution) ... ?



---

archive/issue_comments_077332.json:
```json
{
    "body": "Replying to [comment:6 wdj]:\n> Replying to [comment:5 dimpase]:\n> > Replying to [comment:4 wdj]:\n> > \n> \n> ...\n> \n> > \n> > Oops, sorry. Recovered from a daily backup and put back in place. \n> > The link works now. Long live backups!\n> > \n> \n> Where is the distribution license? It is not clear that we are\n> legally allowed to distribute this code. I did not see any C code written by\n> Havas. Maybe he only contributed design ideas? Did you ask Ramsay \n> if he licensed his C code under the GPL (or any code that allows for \n> free distribution) ... ?\n> \n\nOK, I'll ask. As you know, ACE is distributed via GAP for ages...",
    "created_at": "2010-06-23T05:44:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8551#issuecomment-77332",
    "user": "dimpase"
}
```

Replying to [comment:6 wdj]:
> Replying to [comment:5 dimpase]:
> > Replying to [comment:4 wdj]:
> > 
> 
> ...
> 
> > 
> > Oops, sorry. Recovered from a daily backup and put back in place. 
> > The link works now. Long live backups!
> > 
> 
> Where is the distribution license? It is not clear that we are
> legally allowed to distribute this code. I did not see any C code written by
> Havas. Maybe he only contributed design ideas? Did you ask Ramsay 
> if he licensed his C code under the GPL (or any code that allows for 
> free distribution) ... ?
> 

OK, I'll ask. As you know, ACE is distributed via GAP for ages...



---

archive/issue_comments_077333.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-08-02T10:30:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8551#issuecomment-77333",
    "user": "dimpase"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_077334.json:
```json
{
    "body": "[William is wondering](http://groups.google.com/group/sage-devel/browse_thread/thread/f1d69cfc0a3d220f#) whether we can remove this optional spkg.",
    "created_at": "2013-04-25T18:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8551#issuecomment-77334",
    "user": "leif"
}
```

[William is wondering](http://groups.google.com/group/sage-devel/browse_thread/thread/f1d69cfc0a3d220f#) whether we can remove this optional spkg.



---

archive/issue_comments_077335.json:
```json
{
    "body": "\n```\n./spkg-install: line 36: cd: /Users/.../sage-5.9.rc0/local/lib//pkg//ace/: No such file or directory\n./spkg-install: line 38: ./configure: No such file or directory\n```\n\nThe problem (well, among others) is that it's using \n\n```\nGAP0=`$SAGE_ROOT/spkg/standard/newest_version gap`\n```\n\nAlso, it's first copied to the location and then configured there rather than built in `spkg/build` and then moved.  I don't know if that matters.\n\nI think that until this is fixed, especially if this can just be installed as a GAP package, it would be okay to move ace to \"experimental\".",
    "created_at": "2013-04-26T00:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8551#issuecomment-77335",
    "user": "kcrisman"
}
```


```
./spkg-install: line 36: cd: /Users/.../sage-5.9.rc0/local/lib//pkg//ace/: No such file or directory
./spkg-install: line 38: ./configure: No such file or directory
```

The problem (well, among others) is that it's using 

```
GAP0=`$SAGE_ROOT/spkg/standard/newest_version gap`
```

Also, it's first copied to the location and then configured there rather than built in `spkg/build` and then moved.  I don't know if that matters.

I think that until this is fixed, especially if this can just be installed as a GAP package, it would be okay to move ace to "experimental".



---

archive/issue_comments_077336.json:
```json
{
    "body": "It seems that this package needs an update to work with GAP 4.5, anyway. I several times tried asking Havas about the license, no reply was ever received. One can look at how it is packaged with GAP 4.5.",
    "created_at": "2013-04-26T01:30:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8551#issuecomment-77336",
    "user": "dimpase"
}
```

It seems that this package needs an update to work with GAP 4.5, anyway. I several times tried asking Havas about the license, no reply was ever received. One can look at how it is packaged with GAP 4.5.



---

archive/issue_comments_077337.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2015-04-09T10:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8551#issuecomment-77337",
    "user": "jdemeyer"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_comments_077338.json:
```json
{
    "body": "`ace` is no longer an official Sage package, so this is obsolete.",
    "created_at": "2015-04-09T10:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8551#issuecomment-77338",
    "user": "jdemeyer"
}
```

`ace` is no longer an official Sage package, so this is obsolete.



---

archive/issue_comments_077339.json:
```json
{
    "body": "Replying to [comment:16 jdemeyer]:\n> `ace` is no longer an official Sage package, so this is obsolete.\nhmm, what is an *official* gap package?\nIt's still here:\nhttp://gap-system.org/Packages/ace.html",
    "created_at": "2015-04-09T10:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8551#issuecomment-77339",
    "user": "dimpase"
}
```

Replying to [comment:16 jdemeyer]:
> `ace` is no longer an official Sage package, so this is obsolete.
hmm, what is an *official* gap package?
It's still here:
http://gap-system.org/Packages/ace.html



---

archive/issue_comments_077340.json:
```json
{
    "body": "A package within Sage, I guess.\n\nIn any case, if we don't know the license we can't distribute it. So that settles it.",
    "created_at": "2015-04-09T12:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8551#issuecomment-77340",
    "user": "vbraun"
}
```

A package within Sage, I guess.

In any case, if we don't know the license we can't distribute it. So that settles it.



---

archive/issue_comments_077341.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2015-04-09T12:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8551#issuecomment-77341",
    "user": "vbraun"
}
```

Resolution: wontfix
