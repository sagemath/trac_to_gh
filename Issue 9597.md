# Issue 9597: Crap in pari-2.3.5.p1's spkg-install

archive/issues_009597.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @mwhansen\n\nFrom `#sage-devel`:\n\n```\n<peter-}> Has anyone looked at the top line of pari-2.3.5.p1/spkg-install lately?\n```\n\n\n```sh\nleif@portland:~/Sage/spkgs/pari-2.3.5.p1$ hg diff -r18 -r20 spkg-install | head\ndiff -r d622871cde08 -r eb10b79a288a spkg-install\n--- a/spkg-install\tFri Mar 05 22:12:34 2010 -0800\n+++ b/spkg-install\tTue Apr 27 09:04:49 2010 -0700\n@@ -1,4 +1,4 @@\n-#!/bin/sh\n+B1;2000;0c#!/bin/sh\n ###########################################\n ## PARI\n ###########################################\n@@ -163,7 +163,11 @@\nleif@portland:~/Sage/spkgs/pari-2.3.5.p1$ hg blame spkg-install | head -n 1  \n20: B1;2000;0c#!/bin/sh\n```\n\n(This has been introduced with #8782, which was merged into Sage 4.4.3.alpha0.)\n \nThe first line should be\n\n```sh\n#!/usr/bin/env bash\n```\n\nanyway. Other clean-ups should perhaps be on another ticket, s.t. this gets fixed immediately before someone runs into problems. \n\nThe behavior is somewhat unpredictable and depends on the user's system configuration, the following is **just luck**:\n\n```\n...\n****************************************************\n./spkg-install: line 1: B1: command not found\n./spkg-install: line 1: 2000: command not found\n./spkg-install: line 1: 0c#!/bin/sh: No such file or directory\nConfiguring pari-2.3.5 (STABLE)\n...\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9597\n\n",
    "created_at": "2010-07-25T20:55:00Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Crap in pari-2.3.5.p1's spkg-install",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9597",
    "user": "https://github.com/nexttime"
}
```
Assignee: tbd

CC:  @mwhansen

From `#sage-devel`:

```
<peter-}> Has anyone looked at the top line of pari-2.3.5.p1/spkg-install lately?
```


```sh
leif@portland:~/Sage/spkgs/pari-2.3.5.p1$ hg diff -r18 -r20 spkg-install | head
diff -r d622871cde08 -r eb10b79a288a spkg-install
--- a/spkg-install	Fri Mar 05 22:12:34 2010 -0800
+++ b/spkg-install	Tue Apr 27 09:04:49 2010 -0700
@@ -1,4 +1,4 @@
-#!/bin/sh
+B1;2000;0c#!/bin/sh
 ###########################################
 ## PARI
 ###########################################
@@ -163,7 +163,11 @@
leif@portland:~/Sage/spkgs/pari-2.3.5.p1$ hg blame spkg-install | head -n 1  
20: B1;2000;0c#!/bin/sh
```

(This has been introduced with #8782, which was merged into Sage 4.4.3.alpha0.)
 
The first line should be

```sh
#!/usr/bin/env bash
```

anyway. Other clean-ups should perhaps be on another ticket, s.t. this gets fixed immediately before someone runs into problems. 

The behavior is somewhat unpredictable and depends on the user's system configuration, the following is **just luck**:

```
...
****************************************************
./spkg-install: line 1: B1: command not found
./spkg-install: line 1: 2000: command not found
./spkg-install: line 1: 0c#!/bin/sh: No such file or directory
Configuring pari-2.3.5 (STABLE)
...
```


Issue created by migration from https://trac.sagemath.org/ticket/9597





---

archive/issue_comments_092691.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-26T07:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9597#issuecomment-92691",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092692.json:
```json
{
    "body": "I've put a new spkg at\n\n http://sage.math.washington.edu/home/mpatel/trac/9597/pari-2.3.5.p2.spkg",
    "created_at": "2010-07-26T07:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9597#issuecomment-92692",
    "user": "https://github.com/qed777"
}
```

I've put a new spkg at

 http://sage.math.washington.edu/home/mpatel/trac/9597/pari-2.3.5.p2.spkg



---

archive/issue_comments_092693.json:
```json
{
    "body": "Fix first line of `spkg-install`.  Also, use `/usr/bin/env bash`.",
    "created_at": "2010-07-26T07:24:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9597#issuecomment-92693",
    "user": "https://github.com/qed777"
}
```

Fix first line of `spkg-install`.  Also, use `/usr/bin/env bash`.



---

archive/issue_comments_092694.json:
```json
{
    "body": "Attachment [trac_9597-pari_hash_bang.patch](tarball://root/attachments/some-uuid/ticket9597/trac_9597-pari_hash_bang.patch) by @qed777 created at 2010-07-26 07:33:47",
    "created_at": "2010-07-26T07:33:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9597#issuecomment-92694",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_9597-pari_hash_bang.patch](tarball://root/attachments/some-uuid/ticket9597/trac_9597-pari_hash_bang.patch) by @qed777 created at 2010-07-26 07:33:47



---

archive/issue_comments_092695.json:
```json
{
    "body": "How on earth did that ever work?!",
    "created_at": "2010-07-26T07:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9597#issuecomment-92695",
    "user": "https://github.com/dandrake"
}
```

How on earth did that ever work?!



---

archive/issue_comments_092696.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-26T07:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9597#issuecomment-92696",
    "user": "https://github.com/dandrake"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009741.json:
```json
{
    "actor": "@dandrake",
    "created_at": "2010-07-26T07:47:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9597",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9597#event-9741"
}
```



---

archive/issue_comments_092697.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-26T07:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9597#issuecomment-92697",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed



---

archive/issue_comments_092698.json:
```json
{
    "body": "merged in 4.5.2.alpha1.",
    "created_at": "2010-07-26T07:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9597#issuecomment-92698",
    "user": "https://github.com/dandrake"
}
```

merged in 4.5.2.alpha1.



---

archive/issue_comments_092699.json:
```json
{
    "body": "Replying to [comment:3 ddrake]:\n> How on earth did that ever work?!\nI was wondering the same thing myself. I suspect \n\n\n```\n$ /path/to/doggy/script \n```\n\nwould not work, as the script would not execute properly, but\n\n```\n$ sh /path/to/doggy/script \n```\n\nwill work, as the first line is just a syntax error.\n\nAnyway, its good it's fixed. \n\nDave",
    "created_at": "2010-07-27T18:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9597#issuecomment-92699",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:3 ddrake]:
> How on earth did that ever work?!
I was wondering the same thing myself. I suspect 


```
$ /path/to/doggy/script 
```

would not work, as the script would not execute properly, but

```
$ sh /path/to/doggy/script 
```

will work, as the first line is just a syntax error.

Anyway, its good it's fixed. 

Dave



---

archive/issue_comments_092700.json:
```json
{
    "body": "Replying to [comment:5 drkirkby]:\n> Replying to [comment:3 ddrake]:\n> > How on earth did that ever work?!\n> I was wondering the same thing myself. I suspect  \n\n```\n$ /path/to/doggy/script \n```\n\n> would not work, as the script would not execute properly,\n\nWell, unless the loader interprets the first bytes as indicating something else, the script is fed to the default interpreter (which need not be a shell). (Some shells might interpret the header by themselves first.)\n\n(Btw, `sage-spkg` does this:\n\n```sh\n...\nchmod +x spkg-install\n...\nelse # not Debian\n    time ./spkg-install\nfi\n...\n```\n\n)\n\n> but\n\n```\n$ sh /path/to/doggy/script \n```\n\n> will work, as the first line is just a syntax error.\n\nThat depends on whether you have the programs `B1` and `2000` installed (or likewise defined a shell alias/function).",
    "created_at": "2010-07-27T18:54:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9597#issuecomment-92700",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:5 drkirkby]:
> Replying to [comment:3 ddrake]:
> > How on earth did that ever work?!
> I was wondering the same thing myself. I suspect  

```
$ /path/to/doggy/script 
```

> would not work, as the script would not execute properly,

Well, unless the loader interprets the first bytes as indicating something else, the script is fed to the default interpreter (which need not be a shell). (Some shells might interpret the header by themselves first.)

(Btw, `sage-spkg` does this:

```sh
...
chmod +x spkg-install
...
else # not Debian
    time ./spkg-install
fi
...
```

)

> but

```
$ sh /path/to/doggy/script 
```

> will work, as the first line is just a syntax error.

That depends on whether you have the programs `B1` and `2000` installed (or likewise defined a shell alias/function).



---

archive/issue_comments_092701.json:
```json
{
    "body": "What do you think about creating a `sage-spkg-{check,checker,lint}` script that checks for various common spkg problems?  Or integrating the new checks into `sage-pkg`?",
    "created_at": "2010-07-28T05:19:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9597#issuecomment-92701",
    "user": "https://github.com/qed777"
}
```

What do you think about creating a `sage-spkg-{check,checker,lint}` script that checks for various common spkg problems?  Or integrating the new checks into `sage-pkg`?



---

archive/issue_comments_092702.json:
```json
{
    "body": "Replying to [comment:7 mpatel]:\n> What do you think about creating a `sage-spkg-{check,checker,lint}` script that checks for various common spkg problems?  Or integrating the new checks into `sage-pkg`?\n\nSounds great. Doctesting for spkg packaging. So, you're volunteering? :)",
    "created_at": "2010-07-28T06:52:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9597#issuecomment-92702",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:7 mpatel]:
> What do you think about creating a `sage-spkg-{check,checker,lint}` script that checks for various common spkg problems?  Or integrating the new checks into `sage-pkg`?

Sounds great. Doctesting for spkg packaging. So, you're volunteering? :)



---

archive/issue_comments_092703.json:
```json
{
    "body": "At the moment, and probably over the next few months, I have several other incomplete projects that need more immediate attention.  But I've opened #9622.",
    "created_at": "2010-07-28T08:42:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9597#issuecomment-92703",
    "user": "https://github.com/qed777"
}
```

At the moment, and probably over the next few months, I have several other incomplete projects that need more immediate attention.  But I've opened #9622.
