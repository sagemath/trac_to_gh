# Issue 2113: twisted.web2 should be gzip compressing things it sends out to the notebook

archive/issues_002113.json:
```json
{
    "body": "Assignee: boothby\n\nWe ought to check to make sure that twisted has the gzip filter enabled and is sending things in zip encoding when it can.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2113\n\n",
    "created_at": "2008-02-08T14:32:43Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "title": "twisted.web2 should be gzip compressing things it sends out to the notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2113",
    "user": "jason"
}
```
Assignee: boothby

We ought to check to make sure that twisted has the gzip filter enabled and is sending things in zip encoding when it can.


Issue created by migration from https://trac.sagemath.org/ticket/2113





---

archive/issue_comments_013774.json:
```json
{
    "body": "This needs to be optional; for local notebooks (where the notebook and web browser are running on the same machine), this would very likely slow things down.",
    "created_at": "2008-02-08T19:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2113#issuecomment-13774",
    "user": "cwitty"
}
```

This needs to be optional; for local notebooks (where the notebook and web browser are running on the same machine), this would very likely slow things down.



---

archive/issue_comments_013775.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-10-19T05:07:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2113#issuecomment-13775",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_013776.json:
```json
{
    "body": "I posted a new twisted spkg that contains needed modifications to make this work here:  http://sage.math.washington.edu/home/jason/twisted-8.1.0.p2.spkg\n\nThe above patch, combined with this new spkg, makes it so that pretty much all javascript, java, css, and a few other things are sent over the network compressed when the receiving host is not 'localhost' or '127.0.0.1'.  It seems to cut the transfer down to about a third of what it was.",
    "created_at": "2008-10-19T05:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2113#issuecomment-13776",
    "user": "jason"
}
```

I posted a new twisted spkg that contains needed modifications to make this work here:  http://sage.math.washington.edu/home/jason/twisted-8.1.0.p2.spkg

The above patch, combined with this new spkg, makes it so that pretty much all javascript, java, css, and a few other things are sent over the network compressed when the receiving host is not 'localhost' or '127.0.0.1'.  It seems to cut the transfer down to about a third of what it was.



---

archive/issue_comments_013777.json:
```json
{
    "body": "I applied this patch on 3.1.4 after I applied the patch at #4267.",
    "created_at": "2008-10-19T05:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2113#issuecomment-13777",
    "user": "jason"
}
```

I applied this patch on 3.1.4 after I applied the patch at #4267.



---

archive/issue_comments_013778.json:
```json
{
    "body": "The spkg and patch here apply fine on top of #4267 with 3.2.alpha2. How do you measure the actual bandwidth usage? The patch seems simple enough -- I'll presume that twisted really does gzip what it claims to -- but I want to see lower bandwidth usage. :)",
    "created_at": "2008-11-03T08:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2113#issuecomment-13778",
    "user": "ddrake"
}
```

The spkg and patch here apply fine on top of #4267 with 3.2.alpha2. How do you measure the actual bandwidth usage? The patch seems simple enough -- I'll presume that twisted really does gzip what it claims to -- but I want to see lower bandwidth usage. :)



---

archive/issue_comments_013779.json:
```json
{
    "body": "ddrake: use firebug in firefox.  It will show exactly how much each page and include is taking, bandwidth-wise and speed-wise.",
    "created_at": "2008-11-28T04:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2113#issuecomment-13779",
    "user": "jason"
}
```

ddrake: use firebug in firefox.  It will show exactly how much each page and include is taking, bandwidth-wise and speed-wise.



---

archive/issue_comments_013780.json:
```json
{
    "body": "REFEREE REPORT:\n\nI will give this a positive review when the following trivial things are all fixed. \n\n1. The spkg has a file in there that it shouldn't have in the root directory:\n\n```\nteragon-2:twisted-8.1.0.p2 wstein$ pwd\n/Users/wstein/Desktop/twisted-8.1.0.p2\nteragon-2:twisted-8.1.0.p2 wstein$ hg status\n? gzip.py.patch\nteragon-2:twisted-8.1.0.p2 wstein$ ls\nSPKG.txt\tgzip.py.patch\tpatches\t\tspkg-install\tsrc\n```\n\nJust delete it and remake the spkg.\n\nThe spkg itself compiles fine. \n\nThat said, I'm confused as to what/where gzip.py.patch comes from.  Evidently mhansen wrote it.  It should probably be upstreamed?\n\n2. There is a problem with SPKG.txt claiming mhansen did something, but actually Jason did:\n\n```\n20:26 < mhansen> How is this due to me?\n20:26 < mhansen> I haven't seen this ticket before.\n20:27 < jason--> the patch on the ticket just modifies twist.py\n20:28 < ws-4636_2113> === twisted-8.1.0.p2 (Mike Hansen, October 18, 2008) === * Apply the patches to make the gzip filter deal \n                      with javascript mime types.\n20:28 < ws-4636_2113> It's in SPKG.txt\n20:28 < jason--> in the spkg that is on the ticket?\n20:28 < ws-4636_2113> I think Jason Grout may have been impersonating you!\n20:28 < mabshoff> And that is why we need SPKG.txt files\n20:28 < jason--> is p1 from mhansen?\n20:28 < jason--> (did I copy and not change something?)\n20:28 < mabshoff> copy & paste?\n20:28 < mhansen> I can't for the life of me remember doing that.\n20:28 < ws-4636_2113> It's checked in by Jason.\n20:29 < ws-4636_2113> So I think you didn't do it -- jason did.\n```\n\n\n3. The patch fails to apply, but almost applies:\n\n```\nwas@sage:~/build/sage-3.2.1.alpha1$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nhg_sage.applsage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/2113/gzip.patch')\nAttempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/2113/gzip.patch?format=raw\nLoading: [.]\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg status\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg status\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg import   \"/home/was/.sage/temp/sage/9182/tmp_0.patch\"\napplying /home/was/.sage/temp/sage/9182/tmp_0.patch\npatching file sage/server/notebook/twist.py\nHunk #10 FAILED at 1791\n1 out of 11 hunks FAILED -- saving rejects to file sage/server/notebook/twist.py.rej\nabort: patch failed to apply\n```\n\n| Sage Version 3.2.1.alpha1, Release Date: 2008-11-26                |\n| Type notebook() for the GUI, and license() for information.        |\nOnly one hunk fails, which doesn't really impact much how this works.",
    "created_at": "2008-11-28T04:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2113#issuecomment-13780",
    "user": "was"
}
```

REFEREE REPORT:

I will give this a positive review when the following trivial things are all fixed. 

1. The spkg has a file in there that it shouldn't have in the root directory:

```
teragon-2:twisted-8.1.0.p2 wstein$ pwd
/Users/wstein/Desktop/twisted-8.1.0.p2
teragon-2:twisted-8.1.0.p2 wstein$ hg status
? gzip.py.patch
teragon-2:twisted-8.1.0.p2 wstein$ ls
SPKG.txt	gzip.py.patch	patches		spkg-install	src
```

Just delete it and remake the spkg.

The spkg itself compiles fine. 

That said, I'm confused as to what/where gzip.py.patch comes from.  Evidently mhansen wrote it.  It should probably be upstreamed?

2. There is a problem with SPKG.txt claiming mhansen did something, but actually Jason did:

```
20:26 < mhansen> How is this due to me?
20:26 < mhansen> I haven't seen this ticket before.
20:27 < jason--> the patch on the ticket just modifies twist.py
20:28 < ws-4636_2113> === twisted-8.1.0.p2 (Mike Hansen, October 18, 2008) === * Apply the patches to make the gzip filter deal 
                      with javascript mime types.
20:28 < ws-4636_2113> It's in SPKG.txt
20:28 < jason--> in the spkg that is on the ticket?
20:28 < ws-4636_2113> I think Jason Grout may have been impersonating you!
20:28 < mabshoff> And that is why we need SPKG.txt files
20:28 < jason--> is p1 from mhansen?
20:28 < jason--> (did I copy and not change something?)
20:28 < mabshoff> copy & paste?
20:28 < mhansen> I can't for the life of me remember doing that.
20:28 < ws-4636_2113> It's checked in by Jason.
20:29 < ws-4636_2113> So I think you didn't do it -- jason did.
```


3. The patch fails to apply, but almost applies:

```
was@sage:~/build/sage-3.2.1.alpha1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
hg_sage.applsage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/2113/gzip.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/2113/gzip.patch?format=raw
Loading: [.]
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg import   "/home/was/.sage/temp/sage/9182/tmp_0.patch"
applying /home/was/.sage/temp/sage/9182/tmp_0.patch
patching file sage/server/notebook/twist.py
Hunk #10 FAILED at 1791
1 out of 11 hunks FAILED -- saving rejects to file sage/server/notebook/twist.py.rej
abort: patch failed to apply
```

| Sage Version 3.2.1.alpha1, Release Date: 2008-11-26                |
| Type notebook() for the GUI, and license() for information.        |
Only one hunk fails, which doesn't really impact much how this works.



---

archive/issue_comments_013781.json:
```json
{
    "body": "Changing assignee from boothby to jason.",
    "created_at": "2008-11-28T04:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2113#issuecomment-13781",
    "user": "jason"
}
```

Changing assignee from boothby to jason.



---

archive/issue_comments_013782.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-28T04:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2113#issuecomment-13782",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013783.json:
```json
{
    "body": "I've refreshed the spkg to address the concerns above.  The patch applies cleanly for me on a (slightly modified) sage 3.3alpha3.",
    "created_at": "2009-02-03T09:16:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2113#issuecomment-13783",
    "user": "jason"
}
```

I've refreshed the spkg to address the concerns above.  The patch applies cleanly for me on a (slightly modified) sage 3.3alpha3.



---

archive/issue_comments_013784.json:
```json
{
    "body": "Looks good now.",
    "created_at": "2009-02-07T00:39:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2113#issuecomment-13784",
    "user": "was"
}
```

Looks good now.



---

archive/issue_comments_013785.json:
```json
{
    "body": "Merged twisted-8.1.0.p2.spkg in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-07T01:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2113#issuecomment-13785",
    "user": "mabshoff"
}
```

Merged twisted-8.1.0.p2.spkg in Sage 3.3.alpha6.

Cheers,

Michael



---

archive/issue_comments_013786.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-07T01:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2113#issuecomment-13786",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013787.json:
```json
{
    "body": "Did gzip.patch get merged? On 3.3.alpha6, I don't see anything from that patch in twist.py, and I also don't see anything getting gzip'ed. When I apply the patch, I get some things, but not all, gzip encoded.\n\nAlso, on 3.3.alpha6, in spkg/installed, I see twisted-8.1.0.p1 and twisted-8.1.0.p2. Should there just be one there?",
    "created_at": "2009-02-10T10:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2113#issuecomment-13787",
    "user": "ddrake"
}
```

Did gzip.patch get merged? On 3.3.alpha6, I don't see anything from that patch in twist.py, and I also don't see anything getting gzip'ed. When I apply the patch, I get some things, but not all, gzip encoded.

Also, on 3.3.alpha6, in spkg/installed, I see twisted-8.1.0.p1 and twisted-8.1.0.p2. Should there just be one there?



---

archive/issue_comments_013788.json:
```json
{
    "body": "Replying to [comment:13 ddrake]:\n> Did gzip.patch get merged? On 3.3.alpha6, I don't see anything from that patch in twist.py, and I also don't see anything getting gzip'ed. When I apply the patch, I get some things, but not all, gzip encoded.\n\nOops, merging the patch now. I thought it was inside the spkg and did not apply to the Sage library. Thanks for checking. \n\n> Also, on 3.3.alpha6, in spkg/installed, I see twisted-8.1.0.p1 and twisted-8.1.0.p2. Should there just be one there?\n\nYes, I am deleting p1 now. \n\nI guess this wasn't the best merge :(\n\nCheers,\n\nMichael",
    "created_at": "2009-02-10T10:16:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2113#issuecomment-13788",
    "user": "mabshoff"
}
```

Replying to [comment:13 ddrake]:
> Did gzip.patch get merged? On 3.3.alpha6, I don't see anything from that patch in twist.py, and I also don't see anything getting gzip'ed. When I apply the patch, I get some things, but not all, gzip encoded.

Oops, merging the patch now. I thought it was inside the spkg and did not apply to the Sage library. Thanks for checking. 

> Also, on 3.3.alpha6, in spkg/installed, I see twisted-8.1.0.p1 and twisted-8.1.0.p2. Should there just be one there?

Yes, I am deleting p1 now. 

I guess this wasn't the best merge :(

Cheers,

Michael



---

archive/issue_comments_013789.json:
```json
{
    "body": "Dan,\n\nI checked my 3.3.rc0 merge tree and I only have twisted-8.1.0.p2.spkg, so if you upgraded it would explain why you might have twisted-8.1.0.p1.spkg also in tree. Maybe -bdist also killed the extra twisted.spkg, but I am too lazy to find out :)\n\nCheers,\n\nMichael",
    "created_at": "2009-02-10T10:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2113#issuecomment-13789",
    "user": "mabshoff"
}
```

Dan,

I checked my 3.3.rc0 merge tree and I only have twisted-8.1.0.p2.spkg, so if you upgraded it would explain why you might have twisted-8.1.0.p1.spkg also in tree. Maybe -bdist also killed the extra twisted.spkg, but I am too lazy to find out :)

Cheers,

Michael
