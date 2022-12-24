# Issue 6042: Bring doctests of modular/modsym/ambient.py up to 100%

archive/issues_006042.json:
```json
{
    "body": "Assignee: craigcitro\n\nKeywords: documentation, modular symbols\n\nThis 2500-line file has a low score:\n 26% (26 of 97)\n\nI have nearly finished documenting it and will upload a patch over the weekend.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6042\n\n",
    "created_at": "2009-05-15T07:21:34Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "Bring doctests of modular/modsym/ambient.py up to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6042",
    "user": "cremona"
}
```
Assignee: craigcitro

Keywords: documentation, modular symbols

This 2500-line file has a low score:
 26% (26 of 97)

I have nearly finished documenting it and will upload a patch over the weekend.


Issue created by migration from https://trac.sagemath.org/ticket/6042





---

archive/issue_comments_048112.json:
```json
{
    "body": "Applies to 3.4.2",
    "created_at": "2009-05-16T15:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6042#issuecomment-48112",
    "user": "cremona"
}
```

Applies to 3.4.2



---

archive/issue_comments_048113.json:
```json
{
    "body": "Attachment [trac_6042.patch](tarball://root/attachments/some-uuid/ticket6042/trac_6042.patch) by cremona created at 2009-05-16 15:39:20\n\nThis is just sickening.  I must have spent over 10 hours in the last week documenting this file, resulting in a patch over 2000 lines long, and 100% doctest coverage.  But now I cannot apply it since after the 7 patches on 3 tickets which David warned me about (#5736, #4357 and #5250 all already merged in 4.0alpha0, in that order) I get this mess:\n\n\n```\njohn@ubuntu%sage -hg qpush\napplying trac_6042.patch\npatching file sage/modular/modsym/ambient.py\nHunk #17 FAILED at 800\nHunk #25 FAILED at 1291\nHunk #45 FAILED at 2230\nHunk #60 FAILED at 2829\nHunk #61 FAILED at 2836\nHunk #65 FAILED at 2962\nHunk #71 FAILED at 3195\n7 out of 76 hunks FAILED -- saving rejects to file sage/modular/modsym/ambient.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nErrors during apply, please fix and refresh trac_6042.patch\n```\n\n\nI'm really not sure I can be bothered to mess with this any more.  Is there any system to actually help one merge conflicting patches sensibly?  I have never managed to get things like k3diff to work.\n\nI will at least upload my patch  so that it does not get lost, but I have other things to do.",
    "created_at": "2009-05-16T15:39:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6042#issuecomment-48113",
    "user": "cremona"
}
```

Attachment [trac_6042.patch](tarball://root/attachments/some-uuid/ticket6042/trac_6042.patch) by cremona created at 2009-05-16 15:39:20

This is just sickening.  I must have spent over 10 hours in the last week documenting this file, resulting in a patch over 2000 lines long, and 100% doctest coverage.  But now I cannot apply it since after the 7 patches on 3 tickets which David warned me about (#5736, #4357 and #5250 all already merged in 4.0alpha0, in that order) I get this mess:


```
john@ubuntu%sage -hg qpush
applying trac_6042.patch
patching file sage/modular/modsym/ambient.py
Hunk #17 FAILED at 800
Hunk #25 FAILED at 1291
Hunk #45 FAILED at 2230
Hunk #60 FAILED at 2829
Hunk #61 FAILED at 2836
Hunk #65 FAILED at 2962
Hunk #71 FAILED at 3195
7 out of 76 hunks FAILED -- saving rejects to file sage/modular/modsym/ambient.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh trac_6042.patch
```


I'm really not sure I can be bothered to mess with this any more.  Is there any system to actually help one merge conflicting patches sensibly?  I have never managed to get things like k3diff to work.

I will at least upload my patch  so that it does not get lost, but I have other things to do.



---

archive/issue_comments_048114.json:
```json
{
    "body": "Replying to [comment:1 cremona]:\n> This is just sickening.  I must have spent over 10 hours in the last week documenting this file, resulting in a patch over 2000 lines long, and 100% doctest coverage.  But now I cannot apply it since after the 7 patches on 3 tickets which David warned me about (#5736, #4357 and #5250 all already merged in 4.0alpha0, in that order) I get this mess:\n> \n> I will at least upload my patch  so that it does not get lost, but I have other things to do.\n\nHi John,\n\nI feel your pain.  I don't know of an automated system to get this done properly.  But I'll try to rebase it to 4.0alpha0, and review it in the process.  Hopefully I can do this in the next 36 hours or so.",
    "created_at": "2009-05-17T00:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6042#issuecomment-48114",
    "user": "AlexGhitza"
}
```

Replying to [comment:1 cremona]:
> This is just sickening.  I must have spent over 10 hours in the last week documenting this file, resulting in a patch over 2000 lines long, and 100% doctest coverage.  But now I cannot apply it since after the 7 patches on 3 tickets which David warned me about (#5736, #4357 and #5250 all already merged in 4.0alpha0, in that order) I get this mess:
> 
> I will at least upload my patch  so that it does not get lost, but I have other things to do.

Hi John,

I feel your pain.  I don't know of an automated system to get this done properly.  But I'll try to rebase it to 4.0alpha0, and review it in the process.  Hopefully I can do this in the next 36 hours or so.



---

archive/issue_comments_048115.json:
```json
{
    "body": "Alex: have you already started on this? (I'm not sure what time zone you're in.) I ask because I'm probably the best placed person to sort it out, as the changes which have caused the conflicts were mine, which also puts me under a certain moral obligation as well :-). I don't want to tread on your toes if you've already done it so let me know if you have, but if not, leave it to me and I'll sort it out tomorrow morning.",
    "created_at": "2009-05-17T21:51:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6042#issuecomment-48115",
    "user": "davidloeffler"
}
```

Alex: have you already started on this? (I'm not sure what time zone you're in.) I ask because I'm probably the best placed person to sort it out, as the changes which have caused the conflicts were mine, which also puts me under a certain moral obligation as well :-). I don't want to tread on your toes if you've already done it so let me know if you have, but if not, leave it to me and I'll sort it out tomorrow morning.



---

archive/issue_comments_048116.json:
```json
{
    "body": "I have started but haven't gotten very far yet, so I won't be upset if you want to do it.  Most of the stuff is fairly straightforward, but there are some functions where you introduced documentation and examples, and then John's patch is doing things all over again.  So that would best be done by one of you.",
    "created_at": "2009-05-17T22:04:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6042#issuecomment-48116",
    "user": "AlexGhitza"
}
```

I have started but haven't gotten very far yet, so I won't be upset if you want to do it.  Most of the stuff is fairly straightforward, but there are some functions where you introduced documentation and examples, and then John's patch is doing things all over again.  So that would best be done by one of you.



---

archive/issue_comments_048117.json:
```json
{
    "body": "I've rebased the patch to 4.0.alpha0 and checked that it passes doctests, and had a look through the code, and it all looks fine -- let's get this in without further delay!",
    "created_at": "2009-05-18T09:08:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6042#issuecomment-48117",
    "user": "davidloeffler"
}
```

I've rebased the patch to 4.0.alpha0 and checked that it passes doctests, and had a look through the code, and it all looks fine -- let's get this in without further delay!



---

archive/issue_comments_048118.json:
```json
{
    "body": "Thanks David (and Alex)!",
    "created_at": "2009-05-18T09:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6042#issuecomment-48118",
    "user": "cremona"
}
```

Thanks David (and Alex)!



---

archive/issue_comments_048119.json:
```json
{
    "body": "BTW, I see that \"rebasing\" has included \"reattributing credit in the patch header\"! :)",
    "created_at": "2009-05-18T15:23:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6042#issuecomment-48119",
    "user": "cremona"
}
```

BTW, I see that "rebasing" has included "reattributing credit in the patch header"! :)



---

archive/issue_comments_048120.json:
```json
{
    "body": "Replying to [comment:7 cremona]:\n> BTW, I see that \"rebasing\" has included \"reattributing credit in the patch header\"! :)\n\nHehe, I will fix this once I import the patch. \n\nDavid: Before posting the patch you can just edit the credit in the hg header at the top of the file.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-18T15:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6042#issuecomment-48120",
    "user": "mabshoff"
}
```

Replying to [comment:7 cremona]:
> BTW, I see that "rebasing" has included "reattributing credit in the patch header"! :)

Hehe, I will fix this once I import the patch. 

David: Before posting the patch you can just edit the credit in the hg header at the top of the file.

Cheers,

Michael



---

archive/issue_comments_048121.json:
```json
{
    "body": "Replying to [comment:8 mabshoff]:\n> Replying to [comment:7 cremona]:\n> > BTW, I see that \"rebasing\" has included \"reattributing credit in the patch header\"! :)\n> \n> Hehe, I will fix this once I import the patch. \n> \n> David: Before posting the patch you can just edit the credit in the hg header at the top of the file.\n> \n> Cheers,\n> \n> Michael\n\nOf course I would like credit to go to David too, if hg will allow.",
    "created_at": "2009-05-18T15:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6042#issuecomment-48121",
    "user": "cremona"
}
```

Replying to [comment:8 mabshoff]:
> Replying to [comment:7 cremona]:
> > BTW, I see that "rebasing" has included "reattributing credit in the patch header"! :)
> 
> Hehe, I will fix this once I import the patch. 
> 
> David: Before posting the patch you can just edit the credit in the hg header at the top of the file.
> 
> Cheers,
> 
> Michael

Of course I would like credit to go to David too, if hg will allow.



---

archive/issue_comments_048122.json:
```json
{
    "body": "Attachment [trac_6042-rebase.patch](tarball://root/attachments/some-uuid/ticket6042/trac_6042-rebase.patch) by davidloeffler created at 2009-05-18 15:39:24\n\npatch against 4.0.alpha0",
    "created_at": "2009-05-18T15:39:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6042#issuecomment-48122",
    "user": "davidloeffler"
}
```

Attachment [trac_6042-rebase.patch](tarball://root/attachments/some-uuid/ticket6042/trac_6042-rebase.patch) by davidloeffler created at 2009-05-18 15:39:24

patch against 4.0.alpha0



---

archive/issue_comments_048123.json:
```json
{
    "body": "I just found out about \"qrefresh -u\", so I can masquerade as anybody I like. I'll now attribute any patches that don't work to some unsuspecting victim :-) I've uploaded a new version with credit correctly attributed to John.",
    "created_at": "2009-05-18T15:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6042#issuecomment-48123",
    "user": "davidloeffler"
}
```

I just found out about "qrefresh -u", so I can masquerade as anybody I like. I'll now attribute any patches that don't work to some unsuspecting victim :-) I've uploaded a new version with credit correctly attributed to John.



---

archive/issue_comments_048124.json:
```json
{
    "body": "Replying to [comment:10 davidloeffler]:\n> I just found out about \"qrefresh -u\", so I can masquerade as anybody I like. I'll now attribute any patches that don't work to some unsuspecting victim :-) I've uploaded a new version with credit correctly attributed to John.\n\nthanks -- I don't really mind, of course, but I was looking when I made sure that yours was a replacement patch and not a second patch.",
    "created_at": "2009-05-18T15:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6042#issuecomment-48124",
    "user": "cremona"
}
```

Replying to [comment:10 davidloeffler]:
> I just found out about "qrefresh -u", so I can masquerade as anybody I like. I'll now attribute any patches that don't work to some unsuspecting victim :-) I've uploaded a new version with credit correctly attributed to John.

thanks -- I don't really mind, of course, but I was looking when I made sure that yours was a replacement patch and not a second patch.



---

archive/issue_comments_048125.json:
```json
{
    "body": "The rebased patch on top of two other trivial tickets in my 4.0.rc0 merge tree:\n\n```\nOverall weighted coverage score:  75.0%\nTotal number of functions:  22100\nWe need    6 more function to get to 75% coverage.\n```\n\n\n:))\n\nCheers,\n\nMichael",
    "created_at": "2009-05-18T16:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6042#issuecomment-48125",
    "user": "mabshoff"
}
```

The rebased patch on top of two other trivial tickets in my 4.0.rc0 merge tree:

```
Overall weighted coverage score:  75.0%
Total number of functions:  22100
We need    6 more function to get to 75% coverage.
```


:))

Cheers,

Michael



---

archive/issue_comments_048126.json:
```json
{
    "body": "That makes it all worth while!",
    "created_at": "2009-05-18T17:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6042#issuecomment-48126",
    "user": "cremona"
}
```

That makes it all worth while!



---

archive/issue_comments_048127.json:
```json
{
    "body": "Merged in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-18T18:05:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6042#issuecomment-48127",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_comments_048128.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-18T18:05:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6042#issuecomment-48128",
    "user": "mabshoff"
}
```

Resolution: fixed
