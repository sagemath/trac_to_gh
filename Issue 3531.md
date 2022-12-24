# Issue 3531: [With SPKG, needs review] Boehm_GC spkg

archive/issues_003531.json:
```json
{
    "body": "Assignee: gfurnish\n\nBoehm GC is a prerequisite for ECL lisp and M2 (See #10)\nDownload at http://sage.math.washington.edu/home/gfurnish/spkg/boehm_gc-7.1.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/3531\n\n",
    "created_at": "2008-06-28T23:36:39Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.6",
    "title": "[With SPKG, needs review] Boehm_GC spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3531",
    "user": "gfurnish"
}
```
Assignee: gfurnish

Boehm GC is a prerequisite for ECL lisp and M2 (See #10)
Download at http://sage.math.washington.edu/home/gfurnish/spkg/boehm_gc-7.1.spkg

Issue created by migration from https://trac.sagemath.org/ticket/3531





---

archive/issue_comments_024907.json:
```json
{
    "body": "This builds fine on my machine.",
    "created_at": "2008-06-29T19:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3531#issuecomment-24907",
    "user": "mhansen"
}
```

This builds fine on my machine.



---

archive/issue_comments_024908.json:
```json
{
    "body": "The issue here is that as is with the current config the amount of memory available to the gc is 1GB and that is not even enough to run the M2 test suite, hence not ready for review.\n\nGary: Next time you change the summary of a ticket make sure to provide sufficient information why it was changed.",
    "created_at": "2008-06-29T19:48:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3531#issuecomment-24908",
    "user": "mabshoff"
}
```

The issue here is that as is with the current config the amount of memory available to the gc is 1GB and that is not even enough to run the M2 test suite, hence not ready for review.

Gary: Next time you change the summary of a ticket make sure to provide sufficient information why it was changed.



---

archive/issue_comments_024909.json:
```json
{
    "body": "We are not actually convinced this is not as intended - M2 does not build Boehm with nonstandard options.",
    "created_at": "2008-06-30T04:46:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3531#issuecomment-24909",
    "user": "gfurnish"
}
```

We are not actually convinced this is not as intended - M2 does not build Boehm with nonstandard options.



---

archive/issue_comments_024910.json:
```json
{
    "body": "Replying to [comment:4 gfurnish]:\n> We are not actually convinced this is not as intended - M2 does not build Boehm with nonstandard options. \n\nYes, but last time I tested M2's own test suite failed due to out of memory conditions. Enabling\n\n```\n  --enable-large-config   Optimize for large (> 100 MB) heap or root set\n```\n\nought to fix the problem. This option carries slight memory consumption overhead, see http://gcc.gnu.org/ml/java/2005-02/msg00181.html but I will enforce `--enable-large-config` for ecl anyway.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-30T06:13:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3531#issuecomment-24910",
    "user": "mabshoff"
}
```

Replying to [comment:4 gfurnish]:
> We are not actually convinced this is not as intended - M2 does not build Boehm with nonstandard options. 

Yes, but last time I tested M2's own test suite failed due to out of memory conditions. Enabling

```
  --enable-large-config   Optimize for large (> 100 MB) heap or root set
```

ought to fix the problem. This option carries slight memory consumption overhead, see http://gcc.gnu.org/ml/java/2005-02/msg00181.html but I will enforce `--enable-large-config` for ecl anyway.

Cheers,

Michael



---

archive/issue_comments_024911.json:
```json
{
    "body": "I have replaced the old spkg with one with --enable-large-config.  Please rereview.",
    "created_at": "2008-06-30T16:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3531#issuecomment-24911",
    "user": "gfurnish"
}
```

I have replaced the old spkg with one with --enable-large-config.  Please rereview.



---

archive/issue_comments_024912.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-30T16:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3531#issuecomment-24912",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_024913.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mabshoff\".",
    "created_at": "2008-07-02T20:01:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3531#issuecomment-24913",
    "user": "mabshoff"
}
```

Changing keywords from "" to "editor_mabshoff".



---

archive/issue_comments_024914.json:
```json
{
    "body": "\n```\n[09:44am] mabshoff|afk: gfurnish: oops, negative review.;\n[09:44am] gfurnish: also yay to that\n[09:44am] gfurnish: boo\n[09:44am] mabshoff|afk: just kidding \n[09:44am] schilly: mabshoff|afk: very good\n[09:44am] mabshoff|afk: I have not looked yet \n[09:45am] You are now known as mabshoff.\n[09:47am] mabshoff: boehm_gc-7.1$ hg status\n[09:47am] mabshoff: abort: There is no Mercurial repository here (.hg not found)!\n[09:47am] mabshoff: then: spkg-install is not executable\n[09:47am] gfurnish: is that bad\n[09:47am] mabshoff: And there is OSX crap in there.\n[09:47am] mabshoff: ._src\n[09:47am] mabshoff: re executable: Not really, but it ought to be.\n[09:47am] gfurnish: uh\n[09:47am] mabshoff: spkg-install makes it executable as needed.\n[09:47am] gfurnish: reviewer fix? \n[09:48am] mabshoff: SPKG.txt is also not in the proper format.\n[09:48am] gfurnish: what the heck SPKG.txt is in the proper format\n[09:48am] gfurnish: I copied the template right off the wiki!\n[09:48am] mabshoff: And my dead grand mother could write a better spkg-install.\n[09:49am] mabshoff: Maybe even my imaginary cat could \n[09:49am] mabshoff: I doubt that.\n[09:49am] gfurnish: what is wrong with the spkg-install\n[09:49am] elbie joined the chat room.\n[09:49am] mabshoff: you need to copy http://wiki.sagemath.org/spkgTemplate?action=edit&editor=text\n[09:49am] mabshoff: I.e. SPKG.txt is written in wiki text\n[09:49am] mabshoff: re spkg-install\n[09:49am] mabshoff: shebang is missing\n[09:50am] mabshoff: #633 needs to be checked\n[09:50am] mabshoff: cd src\n[09:50am] mabshoff: ./configure\n[09:50am] mabshoff: You also don't seem to believe in error checking \n[09:50am] gfurnish: well it successfully blows up on error\n[09:51am] mabshoff: And the shebang has to be #!/usr/bin/env  bash\n[09:51am] mabshoff: I don't care we check return codes and print proper error messages.\n[09:51am] gfurnish:  \n[09:52am] gfurnish: is there an example of a simple spkg-install that is well done?\n[09:52am] mabshoff: Sure.\n[09:52am] gfurnish: can you tell me an example of a simple spkg-install that is well done? \n[09:53am] mabshoff: The problem is that all the really good ones are comples.\n[09:53am] mabshoff: *complex\n[09:53am] mabshoff: I am looking for a simple good one right now.\n[09:54am] gfurnish: alternatively you could fix boehm_gc and then I'll fix gdbm and m2\n[09:54am] gfurnish: but I do some complicated stuff in m2 so it would be nice if you would look at it first too\n[09:54am] mabshoff: Well, that is probably the easiest idea.\n[09:54am] gfurnish: namely M2 does OS specific stuff\n[09:54am] mabshoff: Otherwise I will send you back a couple times until you get it right.\n[09:55am] gfurnish: that I think avoids bashisms given it works on sparc solaris\n[09:55am] gfurnish: but it still would be nice if you\n[09:55am] gfurnish: give me some advice on it\n[09:55am] mabshoff: Well, M2 is not a high concern to me personally, boehm is since it will become standard soon.\n```\n",
    "created_at": "2008-07-16T16:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3531#issuecomment-24914",
    "user": "mabshoff"
}
```


```
[09:44am] mabshoff|afk: gfurnish: oops, negative review.;
[09:44am] gfurnish: also yay to that
[09:44am] gfurnish: boo
[09:44am] mabshoff|afk: just kidding 
[09:44am] schilly: mabshoff|afk: very good
[09:44am] mabshoff|afk: I have not looked yet 
[09:45am] You are now known as mabshoff.
[09:47am] mabshoff: boehm_gc-7.1$ hg status
[09:47am] mabshoff: abort: There is no Mercurial repository here (.hg not found)!
[09:47am] mabshoff: then: spkg-install is not executable
[09:47am] gfurnish: is that bad
[09:47am] mabshoff: And there is OSX crap in there.
[09:47am] mabshoff: ._src
[09:47am] mabshoff: re executable: Not really, but it ought to be.
[09:47am] gfurnish: uh
[09:47am] mabshoff: spkg-install makes it executable as needed.
[09:47am] gfurnish: reviewer fix? 
[09:48am] mabshoff: SPKG.txt is also not in the proper format.
[09:48am] gfurnish: what the heck SPKG.txt is in the proper format
[09:48am] gfurnish: I copied the template right off the wiki!
[09:48am] mabshoff: And my dead grand mother could write a better spkg-install.
[09:49am] mabshoff: Maybe even my imaginary cat could 
[09:49am] mabshoff: I doubt that.
[09:49am] gfurnish: what is wrong with the spkg-install
[09:49am] elbie joined the chat room.
[09:49am] mabshoff: you need to copy http://wiki.sagemath.org/spkgTemplate?action=edit&editor=text
[09:49am] mabshoff: I.e. SPKG.txt is written in wiki text
[09:49am] mabshoff: re spkg-install
[09:49am] mabshoff: shebang is missing
[09:50am] mabshoff: #633 needs to be checked
[09:50am] mabshoff: cd src
[09:50am] mabshoff: ./configure
[09:50am] mabshoff: You also don't seem to believe in error checking 
[09:50am] gfurnish: well it successfully blows up on error
[09:51am] mabshoff: And the shebang has to be #!/usr/bin/env  bash
[09:51am] mabshoff: I don't care we check return codes and print proper error messages.
[09:51am] gfurnish:  
[09:52am] gfurnish: is there an example of a simple spkg-install that is well done?
[09:52am] mabshoff: Sure.
[09:52am] gfurnish: can you tell me an example of a simple spkg-install that is well done? 
[09:53am] mabshoff: The problem is that all the really good ones are comples.
[09:53am] mabshoff: *complex
[09:53am] mabshoff: I am looking for a simple good one right now.
[09:54am] gfurnish: alternatively you could fix boehm_gc and then I'll fix gdbm and m2
[09:54am] gfurnish: but I do some complicated stuff in m2 so it would be nice if you would look at it first too
[09:54am] mabshoff: Well, that is probably the easiest idea.
[09:54am] gfurnish: namely M2 does OS specific stuff
[09:54am] mabshoff: Otherwise I will send you back a couple times until you get it right.
[09:55am] gfurnish: that I think avoids bashisms given it works on sparc solaris
[09:55am] gfurnish: but it still would be nice if you
[09:55am] gfurnish: give me some advice on it
[09:55am] mabshoff: Well, M2 is not a high concern to me personally, boehm is since it will become standard soon.
```




---

archive/issue_comments_024915.json:
```json
{
    "body": "The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.6/alpha0/boehm_gc-7.1.p0.spkg\n\nfixes all known issues.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-16T17:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3531#issuecomment-24915",
    "user": "mabshoff"
}
```

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.6/alpha0/boehm_gc-7.1.p0.spkg

fixes all known issues.

Cheers,

Michael



---

archive/issue_comments_024916.json:
```json
{
    "body": "Merged in Sage 3.0.6.alpha0",
    "created_at": "2008-07-16T18:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3531#issuecomment-24916",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.6.alpha0



---

archive/issue_comments_024917.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-16T18:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3531#issuecomment-24917",
    "user": "mabshoff"
}
```

Resolution: fixed
