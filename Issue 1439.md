# Issue 1439: (EASY) make install_package('...') through the notebook far less verbose

archive/issues_001439.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @williamstein\n\nBackground:\n\n\n```\nOn Dec 9, 2007 1:00 PM, root <daly@axiom-developer.org> wrote:\n> >The main plus of this packaging for sage is that it builds from\n> >source quickly (in a few minutes) using precompiled clisp files.\n> \n> Well, on my 2Ghz machine with 2 Gig of memory running VMWare and\n> using the sage vmware image (but upgrading the VM to have 1G memory)\n> I started the package-install at 3:30am this morning. It is now\n> 2:10pm and the build is still \"in-process\". They are heavy things,\n> your minutes :-)\n\nOn a 1.8Ghz opteron (sagemath.org) it takes 18 minutes (I just tested \nthe install).   I am completely baffled that it would take > 11 hours to\ninstall into vmware under windows.  I'll look into that next time I get a\nchance to use windows (in my office).   Thanks for reporting the problem. \n\n> Likely a portion of the problem is due to starting the package-install\n> from the notebook. I'm running native windows and sage in the VM and\n> connecting thru the browser.\n\nThat is very likely the problem.  The output of installing packages through\nthe notebook is way too verbose, so this is in fact a likely source of\nthe problem (which could be remedied).   Better would be to login as \"manage\"\nand type \"sage -i fricas-0.3.1\".  \n\n> I suspect a lot of CPU is going into running jsMath to redraw the\n> output page. The Fricas build has a lot of output (which could be\n> suppressed during package-install) and jsMath is not fast. Axiom\n> has a NOISE variable in the Makefiles to suppress most output.\n\nExcellent. \n\n> You might consider a note suggesting that installs be done from\n> inside the virtual machine rather than thru the notebook interface.\n\nBetter would be to fix things so they work through the notebook well.\n\n```\n\n\nThe fix would likely be to execute the update command, but pipe everything\nto a file, and include a link to that file in the output (so one can look\nat it and press refresh in the browser to test status).  \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1439\n\n",
    "created_at": "2007-12-09T20:06:02Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "(EASY) make install_package('...') through the notebook far less verbose",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1439",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @williamstein

Background:


```
On Dec 9, 2007 1:00 PM, root <daly@axiom-developer.org> wrote:
> >The main plus of this packaging for sage is that it builds from
> >source quickly (in a few minutes) using precompiled clisp files.
> 
> Well, on my 2Ghz machine with 2 Gig of memory running VMWare and
> using the sage vmware image (but upgrading the VM to have 1G memory)
> I started the package-install at 3:30am this morning. It is now
> 2:10pm and the build is still "in-process". They are heavy things,
> your minutes :-)

On a 1.8Ghz opteron (sagemath.org) it takes 18 minutes (I just tested 
the install).   I am completely baffled that it would take > 11 hours to
install into vmware under windows.  I'll look into that next time I get a
chance to use windows (in my office).   Thanks for reporting the problem. 

> Likely a portion of the problem is due to starting the package-install
> from the notebook. I'm running native windows and sage in the VM and
> connecting thru the browser.

That is very likely the problem.  The output of installing packages through
the notebook is way too verbose, so this is in fact a likely source of
the problem (which could be remedied).   Better would be to login as "manage"
and type "sage -i fricas-0.3.1".  

> I suspect a lot of CPU is going into running jsMath to redraw the
> output page. The Fricas build has a lot of output (which could be
> suppressed during package-install) and jsMath is not fast. Axiom
> has a NOISE variable in the Makefiles to suppress most output.

Excellent. 

> You might consider a note suggesting that installs be done from
> inside the virtual machine rather than thru the notebook interface.

Better would be to fix things so they work through the notebook well.

```


The fix would likely be to execute the update command, but pipe everything
to a file, and include a link to that file in the output (so one can look
at it and press refresh in the browser to test status).  



Issue created by migration from https://trac.sagemath.org/ticket/1439





---

archive/issue_comments_009257.json:
```json
{
    "body": "This confirms my hypothesis...\n\n\n```\nWell,per your request, I logged in to the Sage VM and did\n sage -f fricas-0.3.1\nsimply hangs. However,\n sage -f axiom4sage-0.3.1\nsucceeds and shows a total time of\n real 18m42\nor, if I include network time\n real 19.6\nwhich is about the wall-clock time.\n\nSo there appears to be a suggestion that it might\nbe a good idea to do package installs directly rather\nthan thru the notebook interface. Potentially this\ncould be due to the large amount of screen output.\n\nApparently the package rename didn't work.\n\n```\n",
    "created_at": "2007-12-10T07:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1439#issuecomment-9257",
    "user": "https://github.com/williamstein"
}
```

This confirms my hypothesis...


```
Well,per your request, I logged in to the Sage VM and did
 sage -f fricas-0.3.1
simply hangs. However,
 sage -f axiom4sage-0.3.1
succeeds and shows a total time of
 real 18m42
or, if I include network time
 real 19.6
which is about the wall-clock time.

So there appears to be a suggestion that it might
be a good idea to do package installs directly rather
than thru the notebook interface. Potentially this
could be due to the large amount of screen output.

Apparently the package rename didn't work.

```




---

archive/issue_comments_009258.json:
```json
{
    "body": "This is related to #2174.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-16T01:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1439#issuecomment-9258",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is related to #2174.

Cheers,

Michael



---

archive/issue_comments_009259.json:
```json
{
    "body": "Doesn't seem to be a problem anymore. Close?",
    "created_at": "2010-01-18T00:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1439#issuecomment-9259",
    "user": "https://github.com/TimDumol"
}
```

Doesn't seem to be a problem anymore. Close?



---

archive/issue_comments_009260.json:
```json
{
    "body": "Works with sagenb-0.6",
    "created_at": "2010-01-19T03:16:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1439#issuecomment-9260",
    "user": "https://github.com/TimDumol"
}
```

Works with sagenb-0.6



---

archive/issue_comments_009261.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T03:16:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1439#issuecomment-9261",
    "user": "https://github.com/TimDumol"
}
```

Resolution: fixed



---

archive/issue_events_001586.json:
```json
{
    "actor": "@TimDumol",
    "created_at": "2010-01-19T03:16:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1439",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1439#event-1586"
}
```
