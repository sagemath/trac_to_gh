# Issue 5789: create sagelite

archive/issues_005789.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5789\n\n",
    "created_at": "2009-04-15T01:07:39Z",
    "labels": [
        "component: distribution"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "create sagelite",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5789",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff



Issue created by migration from https://trac.sagemath.org/ticket/5789





---

archive/issue_comments_045225.json:
```json
{
    "body": "NOTE: The patches don't apply cleanly.  The bundle works perfectly against sage-3.4.1.rc[1-2] and applies cleanly. \n\nThe authors of this are Mike Hansen and William Stein.  \n\nAfter applying the patch sage should work 100% as usual. However, if in devel/sage/ you type\n\n  ./spkg-distlite\n\nthen the dist directory will contained\n\n  dist/sagelite-3.4.1.tar.gz\n\nYou can take that sagelite-3.4.1.tar.gz and drop it into \"any\" Python (extract and do `python setup.py install`) that has twisted, pexpect, Ipython and maybe some other easy dependencies, and you should be able to do\n\n```\n>>> from sage.server.notebook.notebook_object import notebook\n>>> notebook('test_dir')\n```\nand get the Sage notebook, completely independent of the rest of the Sage library!\n\nIf you switch the mode to python in the list at the top of the screen, you should be able to compute 2+2.\n\n -- William",
    "created_at": "2009-04-15T06:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5789#issuecomment-45225",
    "user": "https://github.com/williamstein"
}
```

NOTE: The patches don't apply cleanly.  The bundle works perfectly against sage-3.4.1.rc[1-2] and applies cleanly. 

The authors of this are Mike Hansen and William Stein.  

After applying the patch sage should work 100% as usual. However, if in devel/sage/ you type

  ./spkg-distlite

then the dist directory will contained

  dist/sagelite-3.4.1.tar.gz

You can take that sagelite-3.4.1.tar.gz and drop it into "any" Python (extract and do `python setup.py install`) that has twisted, pexpect, Ipython and maybe some other easy dependencies, and you should be able to do

```
>>> from sage.server.notebook.notebook_object import notebook
>>> notebook('test_dir')
```
and get the Sage notebook, completely independent of the rest of the Sage library!

If you switch the mode to python in the list at the top of the screen, you should be able to compute 2+2.

 -- William



---

archive/issue_comments_045226.json:
```json
{
    "body": "Here's a link to the sagelite-3.4.1.tar.gz that the above instructions would produce:\n\nhttp://sage.math.washington.edu/home/wstein/patches/sagelite-3.4.1.tar.gz",
    "created_at": "2009-04-15T06:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5789#issuecomment-45226",
    "user": "https://github.com/williamstein"
}
```

Here's a link to the sagelite-3.4.1.tar.gz that the above instructions would produce:

http://sage.math.washington.edu/home/wstein/patches/sagelite-3.4.1.tar.gz



---

archive/issue_comments_045227.json:
```json
{
    "body": "By the way: bundle_of_it_all.hg contains all changes since 3.4, so it might be nice to extract the relevant bits and post a unified patch.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T06:46:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5789#issuecomment-45227",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

By the way: bundle_of_it_all.hg contains all changes since 3.4, so it might be nice to extract the relevant bits and post a unified patch.

Cheers,

Michael



---

archive/issue_comments_045228.json:
```json
{
    "body": "I can confirm that the http://sage.math.washington.edu/home/wstein/patches/sagelite-3.4.1.tar.gz works! Here is a short howto:\n\nhttp://code.google.com/p/spdproject/wiki/AdditionalPackages\n\nthe \"from sage.all import notebook\" doesn't work, but \"from sage.server.notebook.notebook_object import notebook\" and that's what is needed. I tested with sympy and SPD and all is fine. It was maybe small step for you, but a big step for me. :)\n\nI am now going to review the actual patches and try to reproduce the tarball from the sage.",
    "created_at": "2009-04-15T08:14:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5789#issuecomment-45228",
    "user": "https://github.com/certik"
}
```

I can confirm that the http://sage.math.washington.edu/home/wstein/patches/sagelite-3.4.1.tar.gz works! Here is a short howto:

http://code.google.com/p/spdproject/wiki/AdditionalPackages

the "from sage.all import notebook" doesn't work, but "from sage.server.notebook.notebook_object import notebook" and that's what is needed. I tested with sympy and SPD and all is fine. It was maybe small step for you, but a big step for me. :)

I am now going to review the actual patches and try to reproduce the tarball from the sage.



---

archive/issue_comments_045229.json:
```json
{
    "body": "The bundle works fine for me and as far as I can tell, it's +1. However, I'd like if somebody with more familiarity with the code could also look at it, since the patch imho touches important things.\n\nSome comments that I noticed: the following functions have doctests, but don't have any docstring, e.g. I was expecting some line about what the function does -- sometimes it's easy to infer from the example, sometimes it took me a while (e.g. the running_total):\n\n```\n+def prod(x, z=None):\n+    \"\"\"\n\n+def running_total(L, start=None):\n```\n\nAnyway, this is minor.\n\nI run the tests for a sever:\n\n$ ./sage -t devel/sage/sage/server/\n\nThey all pass for me.",
    "created_at": "2009-04-15T14:04:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5789#issuecomment-45229",
    "user": "https://github.com/certik"
}
```

The bundle works fine for me and as far as I can tell, it's +1. However, I'd like if somebody with more familiarity with the code could also look at it, since the patch imho touches important things.

Some comments that I noticed: the following functions have doctests, but don't have any docstring, e.g. I was expecting some line about what the function does -- sometimes it's easy to infer from the example, sometimes it took me a while (e.g. the running_total):

```
+def prod(x, z=None):
+    """

+def running_total(L, start=None):
```

Anyway, this is minor.

I run the tests for a sever:

$ ./sage -t devel/sage/sage/server/

They all pass for me.



---

archive/issue_comments_045230.json:
```json
{
    "body": "I've attach trac_5789.patch which rolls all of the previous patches into one and rebases them against what will be 3.4.1.rc3.  I also added to the docstrings of misc_compat.py",
    "created_at": "2009-04-15T20:34:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5789#issuecomment-45230",
    "user": "https://github.com/mwhansen"
}
```

I've attach trac_5789.patch which rolls all of the previous patches into one and rebases them against what will be 3.4.1.rc3.  I also added to the docstrings of misc_compat.py



---

archive/issue_comments_045231.json:
```json
{
    "body": "I apologize for the two changes above, I used a wrong field to put the comment in. I hope reverted my change correctly.\n\nThe patch is +1 from me.",
    "created_at": "2009-04-15T21:19:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5789#issuecomment-45231",
    "user": "https://github.com/certik"
}
```

I apologize for the two changes above, I used a wrong field to put the comment in. I hope reverted my change correctly.

The patch is +1 from me.



---

archive/issue_comments_045232.json:
```json
{
    "body": "Hopefully now the description is ok.",
    "created_at": "2009-04-15T21:22:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5789#issuecomment-45232",
    "user": "https://github.com/certik"
}
```

Hopefully now the description is ok.



---

archive/issue_comments_045233.json:
```json
{
    "body": "I nuked the bundle since I see no point in keeping a huge 0.5MB bundle around when we now have the patch :)\n\nTaking only trac_5789.patch I get:\n\n```\nbyte-compiling /scratch/mabshoff/sage-3.4.1.rc3/local/lib/python2.5/site-packages/sage/structure/sobj.py to sobj.pyc\n  File \"/scratch/mabshoff/sage-3.4.1.rc3/local/lib/python2.5/site-packages/sage/structure/sobj.py\", line 202\n    cdef bint make_pickle_jar = os.environ.has_key('SAGE_PICKLE_JAR')\n            ^\nSyntaxError: invalid syntax\n\nrunning install_scripts\n```\nCython vs. Python?\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T21:33:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5789#issuecomment-45233",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I nuked the bundle since I see no point in keeping a huge 0.5MB bundle around when we now have the patch :)

Taking only trac_5789.patch I get:

```
byte-compiling /scratch/mabshoff/sage-3.4.1.rc3/local/lib/python2.5/site-packages/sage/structure/sobj.py to sobj.pyc
  File "/scratch/mabshoff/sage-3.4.1.rc3/local/lib/python2.5/site-packages/sage/structure/sobj.py", line 202
    cdef bint make_pickle_jar = os.environ.has_key('SAGE_PICKLE_JAR')
            ^
SyntaxError: invalid syntax

running install_scripts
```
Cython vs. Python?

Cheers,

Michael



---

archive/issue_comments_045234.json:
```json
{
    "body": "Attachment [trac_5789.patch](tarball://root/attachments/some-uuid/ticket5789/trac_5789.patch) by @mwhansen created at 2009-04-15 21:34:52\n\nI updated the patch to take care of this.",
    "created_at": "2009-04-15T21:34:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5789#issuecomment-45234",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_5789.patch](tarball://root/attachments/some-uuid/ticket5789/trac_5789.patch) by @mwhansen created at 2009-04-15 21:34:52

I updated the patch to take care of this.



---

archive/issue_comments_045235.json:
```json
{
    "body": "Replying to [comment:12 mhansen]:\n> I updated the patch to take care of this.\n\n\nThis patch causes one rather bizarre doctest failure:\n\n```\nsage -t -long \"devel/sage/sage/rings/real_rqdf.pyx\"         \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/sage/rings/real_rqdf.pyx\", line 587:\n    sage: loads(s)\nExpected:\n    7.123456789000000000000000000000000000000000000000000000000000000\nGot:\n    doctest:1: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.\n    7.123456789000000000000000000000000000000000000000000000000000000\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_24\n```\nOtherwise we do doctest fine.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T21:51:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5789#issuecomment-45235",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:12 mhansen]:
> I updated the patch to take care of this.


This patch causes one rather bizarre doctest failure:

```
sage -t -long "devel/sage/sage/rings/real_rqdf.pyx"         
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/sage/rings/real_rqdf.pyx", line 587:
    sage: loads(s)
Expected:
    7.123456789000000000000000000000000000000000000000000000000000000
Got:
    doctest:1: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
    7.123456789000000000000000000000000000000000000000000000000000000
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_24
```
Otherwise we do doctest fine.

Cheers,

Michael



---

archive/issue_comments_045236.json:
```json
{
    "body": "Another slight problem: spkg-distlite defines and hard codes\n\n```\nexport SAGE_VERSION=\"3.4.1\"\n```\nIs that desired? It seems like this is something we should define in sage-env.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T21:54:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5789#issuecomment-45236",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Another slight problem: spkg-distlite defines and hard codes

```
export SAGE_VERSION="3.4.1"
```
Is that desired? It seems like this is something we should define in sage-env.

Cheers,

Michael



---

archive/issue_comments_045237.json:
```json
{
    "body": "> `export SAGE_VERSION=\"3.4.1\"`\n> Is that desired?   \n\n\nNope, that's not good.  It should do something more clever. But fixing this is not IMHO a show stopper.",
    "created_at": "2009-04-16T00:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5789#issuecomment-45237",
    "user": "https://github.com/williamstein"
}
```

> `export SAGE_VERSION="3.4.1"`
> Is that desired?   


Nope, that's not good.  It should do something more clever. But fixing this is not IMHO a show stopper.



---

archive/issue_comments_045238.json:
```json
{
    "body": "One fix is to just do\n\n```\nif [ \"$SAGE_VERSION\" = \"\" ]; then\n   echo \"You must set the environment variable SAGE_VERSION.\"\n   exit 1\n```",
    "created_at": "2009-04-16T00:30:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5789#issuecomment-45238",
    "user": "https://github.com/williamstein"
}
```

One fix is to just do

```
if [ "$SAGE_VERSION" = "" ]; then
   echo "You must set the environment variable SAGE_VERSION."
   exit 1
```



---

archive/issue_comments_045239.json:
```json
{
    "body": "Replying to [comment:15 was]:\n\n> Nope, that's not good.  It should do something more clever. But fixing this is not IMHO a show stopper.  \n\n\nI agree that it isn't, but in that case we should address it via a followup ticket.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T01:17:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5789#issuecomment-45239",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:15 was]:

> Nope, that's not good.  It should do something more clever. But fixing this is not IMHO a show stopper.  


I agree that it isn't, but in that case we should address it via a followup ticket.

Cheers,

Michael



---

archive/issue_comments_045240.json:
```json
{
    "body": "I am now in bug fix only mode for 3.4.1.rc4, so this ought to be the first patch in 3.4.2.alpha0 assuming the doctest failure gets fixed and the patch reviewed.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-17T22:48:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5789#issuecomment-45240",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am now in bug fix only mode for 3.4.1.rc4, so this ought to be the first patch in 3.4.2.alpha0 assuming the doctest failure gets fixed and the patch reviewed.

Cheers,

Michael



---

archive/issue_events_013582.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-17T22:48:40Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5789#event-13582"
}
```



---

archive/issue_comments_045241.json:
```json
{
    "body": "This does not apply cleanly against 4.0.2; at the least one would have to make minor changes about where is_64_bit is imported a few places and rebase regarding the additional functionality e.g. unpickle_override in sage_object.pyx.",
    "created_at": "2009-06-22T20:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5789#issuecomment-45241",
    "user": "https://github.com/kcrisman"
}
```

This does not apply cleanly against 4.0.2; at the least one would have to make minor changes about where is_64_bit is imported a few places and rebase regarding the additional functionality e.g. unpickle_override in sage_object.pyx.



---

archive/issue_comments_045242.json:
```json
{
    "body": "Is this ticket now obsolete with the introduction of the sagenb package?  Just curious.",
    "created_at": "2009-11-04T15:46:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5789#issuecomment-45242",
    "user": "https://github.com/kcrisman"
}
```

Is this ticket now obsolete with the introduction of the sagenb package?  Just curious.



---

archive/issue_comments_045243.json:
```json
{
    "body": "To release manager: Since #485 was closed, this one should be as well.",
    "created_at": "2010-01-06T16:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5789#issuecomment-45243",
    "user": "https://github.com/kcrisman"
}
```

To release manager: Since #485 was closed, this one should be as well.



---

archive/issue_events_013583.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-01-06T23:17:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5789#event-13583"
}
```



---

archive/issue_comments_045244.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-01-06T23:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5789#issuecomment-45244",
    "user": "https://github.com/williamstein"
}
```

Resolution: wontfix



---

archive/issue_comments_045245.json:
```json
{
    "body": "Yes, this is obsolete.",
    "created_at": "2010-01-06T23:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5789#issuecomment-45245",
    "user": "https://github.com/williamstein"
}
```

Yes, this is obsolete.



---

archive/issue_events_013584.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-07T00:44:59Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5789#event-13584"
}
```



---

archive/issue_events_013585.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-07T00:44:59Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5789",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5789#event-13585"
}
```
