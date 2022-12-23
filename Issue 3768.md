# Issue 3768: move jsmath into its own spkg

archive/issues_003768.json:
```json
{
    "body": "Assignee: mabshoff\n\nWe should move jsmath into its own spkg.  Like jquery, there seem to be two copies of it, and it'd be good to get rid of this duplication and track its versioning explicitly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3768\n\n",
    "created_at": "2008-08-03T19:29:09Z",
    "labels": [
        "packages: standard",
        "minor",
        "enhancement"
    ],
    "title": "move jsmath into its own spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3768",
    "user": "tabbott"
}
```
Assignee: mabshoff

We should move jsmath into its own spkg.  Like jquery, there seem to be two copies of it, and it'd be good to get rid of this duplication and track its versioning explicitly.

Issue created by migration from https://trac.sagemath.org/ticket/3768





---

archive/issue_comments_026814.json:
```json
{
    "body": "I'm working on this.",
    "created_at": "2008-10-10T23:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3768#issuecomment-26814",
    "user": "jason"
}
```

I'm working on this.



---

archive/issue_comments_026815.json:
```json
{
    "body": "Jason,\n\ncan you post the spkg here? This should be fairly orthogonal to all the other javascript work you are doing. Since the other patches need to be rebased anyway this would likey make it easier.",
    "created_at": "2008-12-04T17:42:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3768#issuecomment-26815",
    "user": "mabshoff"
}
```

Jason,

can you post the spkg here? This should be fairly orthogonal to all the other javascript work you are doing. Since the other patches need to be rebased anyway this would likey make it easier.



---

archive/issue_comments_026816.json:
```json
{
    "body": "This is posted at #4267 :\n\nhttp://sage.math.washington.edu/home/jason/notebook/jsmath-3.6a.spkg",
    "created_at": "2008-12-04T17:54:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3768#issuecomment-26816",
    "user": "jason"
}
```

This is posted at #4267 :

http://sage.math.washington.edu/home/jason/notebook/jsmath-3.6a.spkg



---

archive/issue_comments_026817.json:
```json
{
    "body": "I think it relies on changes in #4267, though, since it changes the paths that the notebook uses to include jsmath.  All of these changes are intertangled at #4267.",
    "created_at": "2008-12-04T17:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3768#issuecomment-26817",
    "user": "jason"
}
```

I think it relies on changes in #4267, though, since it changes the paths that the notebook uses to include jsmath.  All of these changes are intertangled at #4267.



---

archive/issue_comments_026818.json:
```json
{
    "body": "Replying to [comment:4 jason]:\n> I think it relies on changes in #4267, though, since it changes the paths that the notebook uses to include jsmath.  All of these changes are intertangled at #4267.\n\nMmh, the jsmath changes should be pretty harmless and as is #4267 is a mess. So taking care of jsmath independently and then redoing #4267 might be an option, but unless somebody else is doing the work I guess it is your call :)\n\nCheers,\n\nMichael",
    "created_at": "2008-12-04T17:58:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3768#issuecomment-26818",
    "user": "mabshoff"
}
```

Replying to [comment:4 jason]:
> I think it relies on changes in #4267, though, since it changes the paths that the notebook uses to include jsmath.  All of these changes are intertangled at #4267.

Mmh, the jsmath changes should be pretty harmless and as is #4267 is a mess. So taking care of jsmath independently and then redoing #4267 might be an option, but unless somebody else is doing the work I guess it is your call :)

Cheers,

Michael



---

archive/issue_comments_026819.json:
```json
{
    "body": "I'd rather try doing it all at once, since once I'm sifting through the changes in #4267, it'll be easiest just to break it up all at once.  I'll try to get this done before the Joint Meetings (hopefully way before).",
    "created_at": "2008-12-04T18:01:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3768#issuecomment-26819",
    "user": "jason"
}
```

I'd rather try doing it all at once, since once I'm sifting through the changes in #4267, it'll be easiest just to break it up all at once.  I'll try to get this done before the Joint Meetings (hopefully way before).



---

archive/issue_comments_026820.json:
```json
{
    "body": "(when I say \"all at once\", I mean \"breaking up #4267 into functional tickets\" instead of trying to just pull out one change and then redo #4267).\n\nLikely, #4267 will end up as several tickets:\n\n1. Make all the existing javascript code spkgs\n2. Various jquery-related cleanups of the javascript code\n3. Add TinyMCE as an (optional?) spkg\n4. Make the shift-click work (in-place wysiwyg editing).",
    "created_at": "2008-12-04T18:04:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3768#issuecomment-26820",
    "user": "jason"
}
```

(when I say "all at once", I mean "breaking up #4267 into functional tickets" instead of trying to just pull out one change and then redo #4267).

Likely, #4267 will end up as several tickets:

1. Make all the existing javascript code spkgs
2. Various jquery-related cleanups of the javascript code
3. Add TinyMCE as an (optional?) spkg
4. Make the shift-click work (in-place wysiwyg editing).



---

archive/issue_comments_026821.json:
```json
{
    "body": "#4674 is also a ticket about updating jsmath (but also includes one other thing).",
    "created_at": "2008-12-04T18:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3768#issuecomment-26821",
    "user": "jason"
}
```

#4674 is also a ticket about updating jsmath (but also includes one other thing).



---

archive/issue_comments_026822.json:
```json
{
    "body": "Replying to [comment:8 jason]:\n> #4674 is also a ticket about updating jsmath (but also includes one other thing).\n\nI agree, so I am closing this as a dupe of #4674.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-04T18:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3768#issuecomment-26822",
    "user": "mabshoff"
}
```

Replying to [comment:8 jason]:
> #4674 is also a ticket about updating jsmath (but also includes one other thing).

I agree, so I am closing this as a dupe of #4674.

Cheers,

Michael



---

archive/issue_comments_026823.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-12-04T18:09:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3768#issuecomment-26823",
    "user": "mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_026824.json:
```json
{
    "body": "Replying to [comment:7 jason]:\n> (when I say \"all at once\", I mean \"breaking up #4267 into functional tickets\" instead of trying to just pull out one change and then redo #4267).\n> \n> Likely, #4267 will end up as several tickets:\n> \n>  1. Make all the existing javascript code spkgs\n>  1. Various jquery-related cleanups of the javascript code\n>  1. Add TinyMCE as an (optional?) spkg\n>  1. Make the shift-click work (in-place wysiwyg editing).\n> \n\nI would much rather have individual tickers:\n\n* move jsmath to its own spkg (#4674)\n* move jquery to its own spkg and remove both in tree copies (#3767)\n* cleanups of jquery code\n* TinyMCE\n* in place wysiwyg editing \n\nin exactly that order. Feel free to open three tickets (since we already have the jsmath and the jquery one) and then nuke #4267 and #4184 since both of them are a mess.\n\nDoing multiple related, but independent tasks always leads to giant screw ups like #4276 where one small issue with one aspect of the ticket leads to the whole ticket going stale. \n\nCheers,\n\nMichael",
    "created_at": "2008-12-04T18:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3768#issuecomment-26824",
    "user": "mabshoff"
}
```

Replying to [comment:7 jason]:
> (when I say "all at once", I mean "breaking up #4267 into functional tickets" instead of trying to just pull out one change and then redo #4267).
> 
> Likely, #4267 will end up as several tickets:
> 
>  1. Make all the existing javascript code spkgs
>  1. Various jquery-related cleanups of the javascript code
>  1. Add TinyMCE as an (optional?) spkg
>  1. Make the shift-click work (in-place wysiwyg editing).
> 

I would much rather have individual tickers:

* move jsmath to its own spkg (#4674)
* move jquery to its own spkg and remove both in tree copies (#3767)
* cleanups of jquery code
* TinyMCE
* in place wysiwyg editing 

in exactly that order. Feel free to open three tickets (since we already have the jsmath and the jquery one) and then nuke #4267 and #4184 since both of them are a mess.

Doing multiple related, but independent tasks always leads to giant screw ups like #4276 where one small issue with one aspect of the ticket leads to the whole ticket going stale. 

Cheers,

Michael
