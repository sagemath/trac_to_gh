# Issue 2999: Some packages don't respect the CC environment variable

archive/issues_002999.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @orlitzky\n\nPackages which seem to not honor CC environment variable (they use \"gcc\"):\n\n\n```\nflint-1.06.p2\natlas-3.8.1.p1\nf2c-20070816.p0\nsymmetrica-2.0.p2\npolybori-0.3.1.p1\nrubiks-20070912.p5\nzn_poly-0.8.p0\nsage-3.0.rc1\ngap-4.4.10.p7 // guava3.4\ntachyon-0.98beta.p5\npalp-1.1.p1\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2999\n\n",
    "created_at": "2008-04-22T16:42:08Z",
    "labels": [
        "component: build",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Some packages don't respect the CC environment variable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2999",
    "user": "https://github.com/dfdeshom"
}
```
Assignee: mabshoff

CC:  @orlitzky

Packages which seem to not honor CC environment variable (they use "gcc"):


```
flint-1.06.p2
atlas-3.8.1.p1
f2c-20070816.p0
symmetrica-2.0.p2
polybori-0.3.1.p1
rubiks-20070912.p5
zn_poly-0.8.p0
sage-3.0.rc1
gap-4.4.10.p7 // guava3.4
tachyon-0.98beta.p5
palp-1.1.p1
```


Issue created by migration from https://trac.sagemath.org/ticket/2999





---

archive/issue_comments_020572.json:
```json
{
    "body": "For PolyBoRi see the patch for the custom.py file. Feel free to add additional Variables there\n\nGood Night,\n  Alexander",
    "created_at": "2008-04-22T21:07:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20572",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

For PolyBoRi see the patch for the custom.py file. Feel free to add additional Variables there

Good Night,
  Alexander



---

archive/issue_comments_020573.json:
```json
{
    "body": "CC/CXX patch",
    "created_at": "2008-04-22T21:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20573",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

CC/CXX patch



---

archive/issue_comments_020574.json:
```json
{
    "body": "Attachment [pbori-custom_py.patch](tarball://root/attachments/some-uuid/ticket2999/pbori-custom_py.patch) by mabshoff created at 2008-04-26 10:45:37",
    "created_at": "2008-04-26T10:45:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20574",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [pbori-custom_py.patch](tarball://root/attachments/some-uuid/ticket2999/pbori-custom_py.patch) by mabshoff created at 2008-04-26 10:45:37



---

archive/issue_comments_020575.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-26T10:45:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20575",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020576.json:
```json
{
    "body": "Ticket #6437 has an updated spkg so that polybori can be built under Solaris.",
    "created_at": "2009-07-14T07:58:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20576",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Ticket #6437 has an updated spkg so that polybori can be built under Solaris.



---

archive/issue_comments_020577.json:
```json
{
    "body": "There are other spkgs which also fail to respect CC: from [http://groups.google.com/group/sage-devel/msg/a9192a6b51a74d22 this thread](http://groups.google.com/group/sage-devel/msg/a9192a6b51a74d22 this thread), I see the following spkgs which are not listed above:\n\n> * cliquer-1.2\n>\n> * symmetrica-2.0.p4\n>\n> * ratpoints-2.1.2.p2",
    "created_at": "2009-09-16T23:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20577",
    "user": "https://github.com/dandrake"
}
```

There are other spkgs which also fail to respect CC: from [http://groups.google.com/group/sage-devel/msg/a9192a6b51a74d22 this thread](http://groups.google.com/group/sage-devel/msg/a9192a6b51a74d22 this thread), I see the following spkgs which are not listed above:

> * cliquer-1.2
>
> * symmetrica-2.0.p4
>
> * ratpoints-2.1.2.p2



---

archive/issue_comments_020578.json:
```json
{
    "body": "Cliquer should respect the CC environment variable now. See ticket #6681.",
    "created_at": "2009-09-16T23:13:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20578",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Cliquer should respect the CC environment variable now. See ticket #6681.



---

archive/issue_comments_020579.json:
```json
{
    "body": "The f2c package is fixed at #7027, so I've removed it from the list.",
    "created_at": "2012-02-25T21:05:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20579",
    "user": "https://github.com/orlitzky"
}
```

The f2c package is fixed at #7027, so I've removed it from the list.



---

archive/issue_comments_020580.json:
```json
{
    "body": "symmetrica fixed at #10719, so removing that too.",
    "created_at": "2012-02-25T21:17:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20580",
    "user": "https://github.com/orlitzky"
}
```

symmetrica fixed at #10719, so removing that too.



---

archive/issue_comments_020581.json:
```json
{
    "body": "flint and zn_poly have their own tickets at #7024 and #12433 respectively, so there's no need to duplicate them here.",
    "created_at": "2012-02-25T21:19:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20581",
    "user": "https://github.com/orlitzky"
}
```

flint and zn_poly have their own tickets at #7024 and #12433 respectively, so there's no need to duplicate them here.



---

archive/issue_comments_020582.json:
```json
{
    "body": "Polybori also respects `$CC` now, although I can't pin down the ticket where it went from doesn't-work-at-all to something else.",
    "created_at": "2012-02-25T22:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20582",
    "user": "https://github.com/orlitzky"
}
```

Polybori also respects `$CC` now, although I can't pin down the ticket where it went from doesn't-work-at-all to something else.



---

archive/issue_comments_020583.json:
```json
{
    "body": "Tachyon should have been fixed by #9379 and #10681. Waiting on #7069 to confirm on Solaris.",
    "created_at": "2012-02-25T22:45:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20583",
    "user": "https://github.com/orlitzky"
}
```

Tachyon should have been fixed by #9379 and #10681. Waiting on #7069 to confirm on Solaris.



---

archive/issue_comments_020584.json:
```json
{
    "body": "And gap was fixed at #2575 and #4161...",
    "created_at": "2012-02-25T22:52:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20584",
    "user": "https://github.com/orlitzky"
}
```

And gap was fixed at #2575 and #4161...



---

archive/issue_comments_020585.json:
```json
{
    "body": "Rubiks fixed at #7036.",
    "created_at": "2012-02-25T22:55:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20585",
    "user": "https://github.com/orlitzky"
}
```

Rubiks fixed at #7036.



---

archive/issue_comments_020586.json:
```json
{
    "body": "Working on palp at #7071.",
    "created_at": "2012-02-25T23:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20586",
    "user": "https://github.com/orlitzky"
}
```

Working on palp at #7071.



---

archive/issue_comments_020587.json:
```json
{
    "body": "ATLAS supports CC since atlas-3.8.3.p18.",
    "created_at": "2012-02-26T19:39:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20587",
    "user": "https://github.com/vbraun"
}
```

ATLAS supports CC since atlas-3.8.3.p18.



---

archive/issue_comments_020588.json:
```json
{
    "body": "Ok, atlas was fixed in #10226 and we have a ticket for the sage library at #12443. I replaced the initial list for review.",
    "created_at": "2012-02-27T14:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20588",
    "user": "https://github.com/orlitzky"
}
```

Ok, atlas was fixed in #10226 and we have a ticket for the sage library at #12443. I replaced the initial list for review.



---

archive/issue_comments_020589.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-02-27T14:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20589",
    "user": "https://github.com/orlitzky"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_020590.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-02-27T17:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20590",
    "user": "https://github.com/ohanar"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_020591.json:
```json
{
    "body": "Yup, there are plenty of tickets regarding all of these packages -- some from me with the clang port, some from David Kirby with the Sun CC port.",
    "created_at": "2012-02-27T17:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20591",
    "user": "https://github.com/ohanar"
}
```

Yup, there are plenty of tickets regarding all of these packages -- some from me with the clang port, some from David Kirby with the Sun CC port.



---

archive/issue_comments_020592.json:
```json
{
    "body": "Thanks, I did the same thing with the `$CXX` ticket at #3000.",
    "created_at": "2012-02-27T18:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20592",
    "user": "https://github.com/orlitzky"
}
```

Thanks, I did the same thing with the `$CXX` ticket at #3000.



---

archive/issue_comments_020593.json:
```json
{
    "body": "Replying to [comment:9 mjo]:\n> Polybori also respects `$CC` now, although I can't pin down the ticket where it went from doesn't-work-at-all to something else.\nThat was #6437 as mentioned above.",
    "created_at": "2012-02-28T09:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20593",
    "user": "https://github.com/alexanderdreyer"
}
```

Replying to [comment:9 mjo]:
> Polybori also respects `$CC` now, although I can't pin down the ticket where it went from doesn't-work-at-all to something else.
That was #6437 as mentioned above.



---

archive/issue_comments_020594.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-03-04T21:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20594",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_comments_020595.json:
```json
{
    "body": "Replying to [comment:16 ohanar]:\n> Yup, there are plenty of tickets regarding all of these packages -- some from me with the clang port, some from David Kirby with the Sun CC port.\n\nAFAIK at least ratpoints doesn't [yet] have its own ticket; I would have left this ticket open as a meta-ticket until all issues (or spkgs) have really been fixed.",
    "created_at": "2012-03-17T02:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20595",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:16 ohanar]:
> Yup, there are plenty of tickets regarding all of these packages -- some from me with the clang port, some from David Kirby with the Sun CC port.

AFAIK at least ratpoints doesn't [yet] have its own ticket; I would have left this ticket open as a meta-ticket until all issues (or spkgs) have really been fixed.



---

archive/issue_comments_020596.json:
```json
{
    "body": "Replying to [comment:11 mjo]:\n> And gap was fixed at #2575 and #4161...\n\nAha.  I knew `CC` was \"intentionally\" unset in GAP's `spkg-install` for a long time (which was annoying anyway), but **now** I still get:\n\n```\ngcc version 4.6.3 (GCC) \n****************************************************\n*WARNING*: Unsetting CC since that tends to break GAP building\n*WARNING*: Unsetting CXX since that tends to break GAP building\nchecking build system type... x86_64-unknown-linux-gnu\nchecking host system type... x86_64-unknown-linux-gnu\nchecking target system type... x86_64-unknown-linux-gnu\nchecking for gcc... gcc\nchecking for C compiler default output file name... \nconfigure: error: C compiler cannot create executables\nSee `config.log' for more details.\nConfiguration of GAP failed.\n\nreal\t0m0.793s\nuser\t0m0.160s\nsys\t0m0.050s\n************************************************************************\nError installing package gap-4.4.12.p6\n************************************************************************\n```\n\n\nSo if there's been an issue with `CC` and `CXX` set, it might have been **fixed upstream** (I believe so), but it **isn't fixed in Sage**.\n\n[The problem here simply is that the \"default\" `gcc`, which is 4.4.3, doesn't understand some of the options I pass in `CFLAGS`.  GCC 4.6.3, specified in `CC`, of course *does* understand them.]",
    "created_at": "2012-03-17T10:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20596",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:11 mjo]:
> And gap was fixed at #2575 and #4161...

Aha.  I knew `CC` was "intentionally" unset in GAP's `spkg-install` for a long time (which was annoying anyway), but **now** I still get:

```
gcc version 4.6.3 (GCC) 
****************************************************
*WARNING*: Unsetting CC since that tends to break GAP building
*WARNING*: Unsetting CXX since that tends to break GAP building
checking build system type... x86_64-unknown-linux-gnu
checking host system type... x86_64-unknown-linux-gnu
checking target system type... x86_64-unknown-linux-gnu
checking for gcc... gcc
checking for C compiler default output file name... 
configure: error: C compiler cannot create executables
See `config.log' for more details.
Configuration of GAP failed.

real	0m0.793s
user	0m0.160s
sys	0m0.050s
************************************************************************
Error installing package gap-4.4.12.p6
************************************************************************
```


So if there's been an issue with `CC` and `CXX` set, it might have been **fixed upstream** (I believe so), but it **isn't fixed in Sage**.

[The problem here simply is that the "default" `gcc`, which is 4.4.3, doesn't understand some of the options I pass in `CFLAGS`.  GCC 4.6.3, specified in `CC`, of course *does* understand them.]



---

archive/issue_comments_020597.json:
```json
{
    "body": "Replying to [comment:20 leif]:\n> Replying to [comment:16 ohanar]:\n> > Yup, there are plenty of tickets regarding all of these packages -- some from me with the clang port, some from David Kirby with the Sun CC port.\n> \n> AFAIK at least ratpoints doesn't [yet] have its own ticket [...]\n\nThis (ratpoints) is now #12682 (**needing review**).",
    "created_at": "2012-03-17T15:02:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2999#issuecomment-20597",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:20 leif]:
> Replying to [comment:16 ohanar]:
> > Yup, there are plenty of tickets regarding all of these packages -- some from me with the clang port, some from David Kirby with the Sun CC port.
> 
> AFAIK at least ratpoints doesn't [yet] have its own ticket [...]

This (ratpoints) is now #12682 (**needing review**).
