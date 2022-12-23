# Issue 2695: ensure that we have sufficient amounts of RAM to build Sage

archive/issues_002695.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\n[06:27] <mabshoff> wstein: toothpaste's problem is RAM, not [only] disk space.\n[06:27] <wstein> RAM. Wow.\n[06:27] <mabshoff> gcc isn't very efficient.\n[06:27] <wstein> his problem might be lack of a toothbrush.\n[06:27] <mabshoff> And it fails in eclib, so linbox_wrap will be worst.\n[06:28] <wstein> Wow, I see.\n[06:28] <wstein> Dang C++ templates.\n[06:28] <mabshoff> RTFL :)\n[06:28] <wstein> what does rtfl stand for?\n[06:28] <wstein> read the frickin' L?\n[06:28] <mabshoff> read the fine log ;) [edited :)]\n[06:28] <wstein> ahh.\n[06:28] <wstein> good point.\n[06:28] <mabshoff> That was a new failure.\n[06:29] <wstein> Maybe we should check for at least 1GB ram right at the beginning\n[06:29] <mabshoff> I guess the hosted VMs in his case have a rather small, hardcoded limit.\n[06:29] <wstein> of the build, and if the user has less, give an error?\n[06:29] <mabshoff> probably, but 700 MB seems enough.\n[06:29] <wstein> OK, we could check for that.\n[06:29] <wstein> And test that it works using ulimit.\n[06:29] <wstein> That's the sort of thing autohell never does...\n[06:32] <mabshoff> I am not sure if ulimit tests if you have that much memory available.\n[06:33] <mabshoff> It just limits the max allocatable amount.\n[06:33] <wstein> We could just write a small C program that malloc's 700MB.\n[06:33] <wstein> if it fails, then sage doesn't build further.\n[06:33] <mabshoff> Yeah. \n[06:34] <wstein> If this actually sounds like a good idea to you, paste this log in a trac ticket.\n[06:34] <mabshoff> :)\n[06:34] <wstein> If it doesn't, just ignore it.  I leave it up to your taste to decide.\n[06:34] <mabshoff> printf(\"You cheapskate, buy your computer more RAM!\");\n[06:34] <mabshoff> :)\n[06:35] <wstein> :-)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2695\n\n",
    "created_at": "2008-03-28T06:09:41Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "ensure that we have sufficient amounts of RAM to build Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2695",
    "user": "mabshoff"
}
```
Assignee: mabshoff


```
[06:27] <mabshoff> wstein: toothpaste's problem is RAM, not [only] disk space.
[06:27] <wstein> RAM. Wow.
[06:27] <mabshoff> gcc isn't very efficient.
[06:27] <wstein> his problem might be lack of a toothbrush.
[06:27] <mabshoff> And it fails in eclib, so linbox_wrap will be worst.
[06:28] <wstein> Wow, I see.
[06:28] <wstein> Dang C++ templates.
[06:28] <mabshoff> RTFL :)
[06:28] <wstein> what does rtfl stand for?
[06:28] <wstein> read the frickin' L?
[06:28] <mabshoff> read the fine log ;) [edited :)]
[06:28] <wstein> ahh.
[06:28] <wstein> good point.
[06:28] <mabshoff> That was a new failure.
[06:29] <wstein> Maybe we should check for at least 1GB ram right at the beginning
[06:29] <mabshoff> I guess the hosted VMs in his case have a rather small, hardcoded limit.
[06:29] <wstein> of the build, and if the user has less, give an error?
[06:29] <mabshoff> probably, but 700 MB seems enough.
[06:29] <wstein> OK, we could check for that.
[06:29] <wstein> And test that it works using ulimit.
[06:29] <wstein> That's the sort of thing autohell never does...
[06:32] <mabshoff> I am not sure if ulimit tests if you have that much memory available.
[06:33] <mabshoff> It just limits the max allocatable amount.
[06:33] <wstein> We could just write a small C program that malloc's 700MB.
[06:33] <wstein> if it fails, then sage doesn't build further.
[06:33] <mabshoff> Yeah. 
[06:34] <wstein> If this actually sounds like a good idea to you, paste this log in a trac ticket.
[06:34] <mabshoff> :)
[06:34] <wstein> If it doesn't, just ignore it.  I leave it up to your taste to decide.
[06:34] <mabshoff> printf("You cheapskate, buy your computer more RAM!");
[06:34] <mabshoff> :)
[06:35] <wstein> :-)
```


Issue created by migration from https://trac.sagemath.org/ticket/2695





---

archive/issue_comments_018546.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-28T06:09:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2695#issuecomment-18546",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_018547.json:
```json
{
    "body": "FYI, I have 700MB of Ram and I'm able to build Sage fine (as of 2.10.2, I think). So... aim lower :)",
    "created_at": "2008-03-28T14:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2695#issuecomment-18547",
    "user": "dfdeshom"
}
```

FYI, I have 700MB of Ram and I'm able to build Sage fine (as of 2.10.2, I think). So... aim lower :)



---

archive/issue_comments_018548.json:
```json
{
    "body": "I have 512 mb in my laptop and 2.10.x built/upgraded perfectly fine and I'm currently 'sage -upgrade'ing to 2.11 and I got past linbox_wrap.  Only 100kb of swap is currently showing as used.",
    "created_at": "2008-03-31T14:31:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2695#issuecomment-18548",
    "user": "jbmohler"
}
```

I have 512 mb in my laptop and 2.10.x built/upgraded perfectly fine and I'm currently 'sage -upgrade'ing to 2.11 and I got past linbox_wrap.  Only 100kb of swap is currently showing as used.



---

archive/issue_comments_018549.json:
```json
{
    "body": "Replying to [comment:3 jbmohler]:\n> I have 512 mb in my laptop and 2.10.x built/upgraded perfectly fine and I'm currently 'sage -upgrade'ing to 2.11 and I got past linbox_wrap.  Only 100kb of swap is currently showing as used.\n\nHi Joel,\n\nthe amount of RAM required for linbox_wrap does depend on the gcc released. I have seen 700 MB, but even 350MB is an unreasonable amount of memory to compile that bit of code. To resolve this ticket we should check the amount of memory available and emit a warning if we consider the amount too low. It might be 0.5GB for now.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-31T14:50:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2695#issuecomment-18549",
    "user": "mabshoff"
}
```

Replying to [comment:3 jbmohler]:
> I have 512 mb in my laptop and 2.10.x built/upgraded perfectly fine and I'm currently 'sage -upgrade'ing to 2.11 and I got past linbox_wrap.  Only 100kb of swap is currently showing as used.

Hi Joel,

the amount of RAM required for linbox_wrap does depend on the gcc released. I have seen 700 MB, but even 350MB is an unreasonable amount of memory to compile that bit of code. To resolve this ticket we should check the amount of memory available and emit a warning if we consider the amount too low. It might be 0.5GB for now.

Cheers,

Michael



---

archive/issue_comments_018550.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:19:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2695#issuecomment-18550",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_018551.json:
```json
{
    "body": "FWIW, with enough (and fast :) ) swap space, Sage 5.x (still) builds on 32-bit machines with 512 MB RAM (and Gnome or some other GUI running).\n\n\n\n\nAnother issue is that meanwhile a few [long] doctests are really poor, in eating up nearly 2x 2 GB (Sage + `gp`).  Others just allocate that much, without actually using it (such that they'll fail with `ulimit -v` for no real reason).\n\n768 MB (including a GUI) used to be sufficient to (build Sage and) run all long doctests without any swapping a while ago.",
    "created_at": "2013-04-25T13:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2695#issuecomment-18551",
    "user": "leif"
}
```

FWIW, with enough (and fast :) ) swap space, Sage 5.x (still) builds on 32-bit machines with 512 MB RAM (and Gnome or some other GUI running).




Another issue is that meanwhile a few [long] doctests are really poor, in eating up nearly 2x 2 GB (Sage + `gp`).  Others just allocate that much, without actually using it (such that they'll fail with `ulimit -v` for no real reason).

768 MB (including a GUI) used to be sufficient to (build Sage and) run all long doctests without any swapping a while ago.



---

archive/issue_comments_018552.json:
```json
{
    "body": "Replying to [comment:6 leif]:\n> 768 MB (including a GUI) used to be sufficient to (build Sage and) run all long doctests without any swapping a while ago.\nfor large values of \"a while\" I guess...",
    "created_at": "2013-04-25T13:13:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2695#issuecomment-18552",
    "user": "jdemeyer"
}
```

Replying to [comment:6 leif]:
> 768 MB (including a GUI) used to be sufficient to (build Sage and) run all long doctests without any swapping a while ago.
for large values of "a while" I guess...



---

archive/issue_comments_018553.json:
```json
{
    "body": "Replying to [comment:7 jdemeyer]:\n> Replying to [comment:6 leif]:\n> > 768 MB (including a GUI) used to be sufficient to (build Sage and) run all long doctests without any swapping a while ago.\n> for large values of \"a while\" I guess...\n\nNope;  I actually wanted to add \"not that long ago\"...  Mid or late 2011 IIRC (last time I recall having tested that; i.e., probably even past that time).",
    "created_at": "2013-04-25T13:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2695#issuecomment-18553",
    "user": "leif"
}
```

Replying to [comment:7 jdemeyer]:
> Replying to [comment:6 leif]:
> > 768 MB (including a GUI) used to be sufficient to (build Sage and) run all long doctests without any swapping a while ago.
> for large values of "a while" I guess...

Nope;  I actually wanted to add "not that long ago"...  Mid or late 2011 IIRC (last time I recall having tested that; i.e., probably even past that time).



---

archive/issue_comments_018554.json:
```json
{
    "body": "P.S.:  W.r.t. the doctests, the \"winners\" in memory consumption used to be those in `schemes/elliptic_curves/`, with definitely less than 400 MB (300-350 I think).",
    "created_at": "2013-04-25T13:30:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2695#issuecomment-18554",
    "user": "leif"
}
```

P.S.:  W.r.t. the doctests, the "winners" in memory consumption used to be those in `schemes/elliptic_curves/`, with definitely less than 400 MB (300-350 I think).



---

archive/issue_comments_018555.json:
```json
{
    "body": "Replying to [comment:8 leif]:\n> Nope;  I actually wanted to add \"not that long ago\"...  Mid or late 2011 IIRC (last time I recall having tested that; i.e., probably even past that time).\nI don't believe you, the Heegner tests exist longer than that and always required around 2GB of memory.",
    "created_at": "2013-05-19T13:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2695#issuecomment-18555",
    "user": "jdemeyer"
}
```

Replying to [comment:8 leif]:
> Nope;  I actually wanted to add "not that long ago"...  Mid or late 2011 IIRC (last time I recall having tested that; i.e., probably even past that time).
I don't believe you, the Heegner tests exist longer than that and always required around 2GB of memory.



---

archive/issue_comments_018556.json:
```json
{
    "body": "Replying to [comment:10 jdemeyer]:\n> Replying to [comment:8 leif]:\n> > Nope;  I actually wanted to add \"not that long ago\"...  Mid or late 2011 IIRC (last time I recall having tested that; i.e., probably even past that time).\n> I don't believe you, the Heegner tests exist longer than that and always required around 2GB of memory.\n\nI'm especially sure about the tests in `schemes/elliptic_curves/`, since these used to be the record holders, as mentioned. :-)\n\nThis is just one example of a couple of doctests where PARI tries to **allocate** a huge amount of memory, but actually **uses** only a fraction of it.  (You might have to set up enough swap space to run these tests, but you'll usually not experience swapping even with just 512 MB RAM, say.)",
    "created_at": "2013-05-19T16:16:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2695#issuecomment-18556",
    "user": "leif"
}
```

Replying to [comment:10 jdemeyer]:
> Replying to [comment:8 leif]:
> > Nope;  I actually wanted to add "not that long ago"...  Mid or late 2011 IIRC (last time I recall having tested that; i.e., probably even past that time).
> I don't believe you, the Heegner tests exist longer than that and always required around 2GB of memory.

I'm especially sure about the tests in `schemes/elliptic_curves/`, since these used to be the record holders, as mentioned. :-)

This is just one example of a couple of doctests where PARI tries to **allocate** a huge amount of memory, but actually **uses** only a fraction of it.  (You might have to set up enough swap space to run these tests, but you'll usually not experience swapping even with just 512 MB RAM, say.)



---

archive/issue_comments_018557.json:
```json
{
    "body": "... like I already mentioned [comment:6 above]:\n> [...] Others just allocate that much, without actually using it (such that they'll fail with `ulimit -v` for no real reason).\n> \n> 768 MB (including a GUI) used to be sufficient to (build Sage and) run all long doctests without any swapping a while ago. [...]",
    "created_at": "2013-05-19T16:23:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2695#issuecomment-18557",
    "user": "leif"
}
```

... like I already mentioned [comment:6 above]:
> [...] Others just allocate that much, without actually using it (such that they'll fail with `ulimit -v` for no real reason).
> 
> 768 MB (including a GUI) used to be sufficient to (build Sage and) run all long doctests without any swapping a while ago. [...]



---

archive/issue_comments_018558.json:
```json
{
    "body": "Similar to #1517, I don't think it's up to Sage to decide how much RAM is enough.",
    "created_at": "2013-06-13T12:40:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2695#issuecomment-18558",
    "user": "jdemeyer"
}
```

Similar to #1517, I don't think it's up to Sage to decide how much RAM is enough.



---

archive/issue_comments_018559.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-06-13T12:40:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2695#issuecomment-18559",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_018560.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-13T12:42:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2695#issuecomment-18560",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_018561.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2013-06-19T12:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2695",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2695#issuecomment-18561",
    "user": "jdemeyer"
}
```

Resolution: wontfix
