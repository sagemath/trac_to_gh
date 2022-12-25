# Issue 1233: [with spkg, with positive review] mwrank wrapper causes crashes and error on non-minimal curves

archive/issues_001233.json:
```json
{
    "body": "Assignee: jec\n\nI found that elliptic curves which are defined by non-minimal equations cause rank() etc to crash or give error messages.  Possibly only when there is 2-torsion.  Since mwrank itself handles the same curves with no problem, there is a problem with the wrapper code.  First here are two examples of what goes wrong:\n\n```\nsage: E=mwrank_EllipticCurve([-1323,3942])\nsage: E.rank()\nResult of shifting the point [36:-108:1] is [1:-1:1] which is not a valid point on its curve [0,0,0,-1323,3942]!\nPoint [1:-1:1], height = 3.1490443504515297201640615419259554770993208565687 --warning: NOT on curve!\n1\nsage: E=EllipticCurve([-1323,3942])\nsage: E.rank()\n---------------------------------------------------------------------------\n<type 'exceptions.RuntimeError'>          Traceback (most recent call last)\n\n/home/jec/tex/papers/<ipython console> in <module>()\n\n/home/src/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py in rank(self, use_database, verbose, only_use_mwrank, algorithm, proof)\n    989         elif algorithm == 'mwrank_shell':\n    990             misc.verbose(\"using mwrank shell\")\n--> 991             X = self.mwrank()\n    992             if not 'The rank and full Mordell-Weil basis have been determined unconditionally' in X:\n    993                 if proof:\n\n/home/src/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py in mwrank(self, options)\n    163             from sage.interfaces.all import Mwrank\n    164             mwrank = Mwrank(options=options)\n--> 165         return mwrank(self.a_invariants())\n    166\n    167     def conductor(self, algorithm=\"pari\"):\n\n/home/src/sage/local/lib/python2.5/site-packages/sage/interfaces/mwrank.py in __call__(self, cmd)\n     69\n     70     def __call__(self, cmd):\n---> 71         return self.eval(str(cmd))\n     72\n     73     def console(self):\n\n/home/src/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in eval(self, code, strip, **kwds)\n    705         try:\n    706             with gc_disabled():\n--> 707                 return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n    708         except KeyboardInterrupt:\n    709             # DO NOT CATCH KeyboardInterrupt, as it is being caught\n\n/home/src/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in _eval_line(self, line, allow_use_file, wait_for_prompt)\n    641                         # we expect to get an EOF if we're quitting.\n    642                         return ''\n--> 643                     raise RuntimeError, \"%s\\n%s crashed executing %s\"%(msg,self, line)\n    644                 out = E.before\n    645             else:\n\n<type 'exceptions.RuntimeError'>: End Of File (EOF) in read_nonblocking(). Exception style platform.\n<pexpect.spawn instance at 0x982f58c>\nversion: 2.0 ($Revision: 1.151 $)\ncommand: /home/src/sage/local/bin/mwrank\nargs: ['/home/src/sage/local/bin/mwrank']\npatterns:\n    Enter curve:\nbuffer (last 100 chars):\nbefore (last 100 chars): [0, 0, 0, -1323, 3942]\n\nafter: <class 'pexpect.EOF'>\nmatch: None\nmatch_index: None\nexitstatus: None\nflag_eof: 1\npid: 6057\nchild_fd: 3\ntimeout: None\ndelimiter: <class 'pexpect.EOF'>\nlogfile: None\nmaxread: 10000\nsearchwindowsize: None\ndelaybeforesend: 0\nMwrank crashed executing [0, 0, 0, -1323, 3942]\n```\nExplanation:   In the stand-alone mwrank binary (run via !mwrank for example) curves are converted to minimal models after input and any points computed are converted back so that the points output are on the input curve (!).  But the Sage wrapper does not so this and everything gets confused.\n\nOne solution would be for me to change the mwrank code itself so that the two_descent class itself handled the minimalization.  That would be cleanest, and would not require any changes to the Sage wrapping.  Otherwise, as with Simon's code, we would run up against the fact that currently Sage has no means of changing models and points itself.\n\nSo I guess this lands on my own to-do list.\n\njec\n\nIssue created by migration from https://trac.sagemath.org/ticket/1233\n\n",
    "closed_at": "2007-12-20T18:08:15Z",
    "created_at": "2007-11-21T10:25:30Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.1",
    "title": "[with spkg, with positive review] mwrank wrapper causes crashes and error on non-minimal curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1233",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: jec

I found that elliptic curves which are defined by non-minimal equations cause rank() etc to crash or give error messages.  Possibly only when there is 2-torsion.  Since mwrank itself handles the same curves with no problem, there is a problem with the wrapper code.  First here are two examples of what goes wrong:

```
sage: E=mwrank_EllipticCurve([-1323,3942])
sage: E.rank()
Result of shifting the point [36:-108:1] is [1:-1:1] which is not a valid point on its curve [0,0,0,-1323,3942]!
Point [1:-1:1], height = 3.1490443504515297201640615419259554770993208565687 --warning: NOT on curve!
1
sage: E=EllipticCurve([-1323,3942])
sage: E.rank()
---------------------------------------------------------------------------
<type 'exceptions.RuntimeError'>          Traceback (most recent call last)

/home/jec/tex/papers/<ipython console> in <module>()

/home/src/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py in rank(self, use_database, verbose, only_use_mwrank, algorithm, proof)
    989         elif algorithm == 'mwrank_shell':
    990             misc.verbose("using mwrank shell")
--> 991             X = self.mwrank()
    992             if not 'The rank and full Mordell-Weil basis have been determined unconditionally' in X:
    993                 if proof:

/home/src/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py in mwrank(self, options)
    163             from sage.interfaces.all import Mwrank
    164             mwrank = Mwrank(options=options)
--> 165         return mwrank(self.a_invariants())
    166
    167     def conductor(self, algorithm="pari"):

/home/src/sage/local/lib/python2.5/site-packages/sage/interfaces/mwrank.py in __call__(self, cmd)
     69
     70     def __call__(self, cmd):
---> 71         return self.eval(str(cmd))
     72
     73     def console(self):

/home/src/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in eval(self, code, strip, **kwds)
    705         try:
    706             with gc_disabled():
--> 707                 return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
    708         except KeyboardInterrupt:
    709             # DO NOT CATCH KeyboardInterrupt, as it is being caught

/home/src/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in _eval_line(self, line, allow_use_file, wait_for_prompt)
    641                         # we expect to get an EOF if we're quitting.
    642                         return ''
--> 643                     raise RuntimeError, "%s\n%s crashed executing %s"%(msg,self, line)
    644                 out = E.before
    645             else:

<type 'exceptions.RuntimeError'>: End Of File (EOF) in read_nonblocking(). Exception style platform.
<pexpect.spawn instance at 0x982f58c>
version: 2.0 ($Revision: 1.151 $)
command: /home/src/sage/local/bin/mwrank
args: ['/home/src/sage/local/bin/mwrank']
patterns:
    Enter curve:
buffer (last 100 chars):
before (last 100 chars): [0, 0, 0, -1323, 3942]

after: <class 'pexpect.EOF'>
match: None
match_index: None
exitstatus: None
flag_eof: 1
pid: 6057
child_fd: 3
timeout: None
delimiter: <class 'pexpect.EOF'>
logfile: None
maxread: 10000
searchwindowsize: None
delaybeforesend: 0
Mwrank crashed executing [0, 0, 0, -1323, 3942]
```
Explanation:   In the stand-alone mwrank binary (run via !mwrank for example) curves are converted to minimal models after input and any points computed are converted back so that the points output are on the input curve (!).  But the Sage wrapper does not so this and everything gets confused.

One solution would be for me to change the mwrank code itself so that the two_descent class itself handled the minimalization.  That would be cleanest, and would not require any changes to the Sage wrapping.  Otherwise, as with Simon's code, we would run up against the fact that currently Sage has no means of changing models and points itself.

So I guess this lands on my own to-do list.

jec

Issue created by migration from https://trac.sagemath.org/ticket/1233





---

archive/issue_comments_007658.json:
```json
{
    "body": "Apologies for the hopeless formatting of the above, which looked quite different before I pressed the \"submit\" button.",
    "created_at": "2007-11-21T10:26:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1233#issuecomment-7658",
    "user": "https://github.com/JohnCremona"
}
```

Apologies for the hopeless formatting of the above, which looked quite different before I pressed the "submit" button.



---

archive/issue_events_003255.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-21T10:40:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1233",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1233#event-3255"
}
```



---

archive/issue_comments_007659.json:
```json
{
    "body": "See model-changing code at #1239",
    "created_at": "2007-12-05T19:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1233#issuecomment-7659",
    "user": "https://github.com/robertwb"
}
```

See model-changing code at #1239



---

archive/issue_comments_007660.json:
```json
{
    "body": "Attachment [jec-20071219.hg](tarball://root/attachments/some-uuid/ticket1233/jec-20071219.hg) by @JohnCremona created at 2007-12-19 11:26:25",
    "created_at": "2007-12-19T11:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1233#issuecomment-7660",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [jec-20071219.hg](tarball://root/attachments/some-uuid/ticket1233/jec-20071219.hg) by @JohnCremona created at 2007-12-19 11:26:25



---

archive/issue_comments_007661.json:
```json
{
    "body": "Attachment [jec-20071219.2.hg](tarball://root/attachments/some-uuid/ticket1233/jec-20071219.2.hg) by @JohnCremona created at 2007-12-19 11:31:13",
    "created_at": "2007-12-19T11:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1233#issuecomment-7661",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [jec-20071219.2.hg](tarball://root/attachments/some-uuid/ticket1233/jec-20071219.2.hg) by @JohnCremona created at 2007-12-19 11:31:13



---

archive/issue_comments_007662.json:
```json
{
    "body": "Attachment [jec-20071219.3.hg](tarball://root/attachments/some-uuid/ticket1233/jec-20071219.3.hg) by @JohnCremona created at 2007-12-19 11:33:06",
    "created_at": "2007-12-19T11:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1233#issuecomment-7662",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [jec-20071219.3.hg](tarball://root/attachments/some-uuid/ticket1233/jec-20071219.3.hg) by @JohnCremona created at 2007-12-19 11:33:06



---

archive/issue_comments_007663.json:
```json
{
    "body": "I have changed the mwrank source code so that non-minimal models are now handled properly.  All the work is done on a minimal model, but opints are mapped back to the input model if that is different.\n\nNote that it is not correct to say that this was a Sage-wrapping problem!   The stand-alone mwrank binary used to manage this properly by converting to a minimal model before calling the two_descent class, and the latter just assumed it was being given a minimal model.  The Sage wrapping went straight into the two_descent.  Now, the two_descent class handles this itself (so that the mwrank.cc program has less to do).\n\nI will attach a bundle which corrects this;  it should be possible to apply this to the cremona*.spkg in Sage 2.9.\n\nNo, that failed, since it did not recognise the parent.  Help!",
    "created_at": "2007-12-19T11:33:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1233#issuecomment-7663",
    "user": "https://github.com/JohnCremona"
}
```

I have changed the mwrank source code so that non-minimal models are now handled properly.  All the work is done on a minimal model, but opints are mapped back to the input model if that is different.

Note that it is not correct to say that this was a Sage-wrapping problem!   The stand-alone mwrank binary used to manage this properly by converting to a minimal model before calling the two_descent class, and the latter just assumed it was being given a minimal model.  The Sage wrapping went straight into the two_descent.  Now, the two_descent class handles this itself (so that the mwrank.cc program has less to do).

I will attach a bundle which corrects this;  it should be possible to apply this to the cremona*.spkg in Sage 2.9.

No, that failed, since it did not recognise the parent.  Help!



---

archive/issue_events_003256.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-19T11:59:42Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1233",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1233#event-3256"
}
```



---

archive/issue_events_003257.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-19T11:59:42Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1233",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1233#event-3257"
}
```



---

archive/issue_comments_007664.json:
```json
{
    "body": "An updated spkg which solves this and fixes some other bugs is at\n\nhttp://www.warwick.ac.uk/staff/J.E.Cremona/cremona-20071219.spkg",
    "created_at": "2007-12-19T13:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1233#issuecomment-7664",
    "user": "https://github.com/JohnCremona"
}
```

An updated spkg which solves this and fixes some other bugs is at

http://www.warwick.ac.uk/staff/J.E.Cremona/cremona-20071219.spkg



---

archive/issue_comments_007665.json:
```json
{
    "body": "And \n\nhttp://sage.math.washington.edu/home/mabshoff/cremona-20071219.p0.spkg\n\nbuilds :)\n\nCheers,\n\nMichael",
    "created_at": "2007-12-19T14:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1233#issuecomment-7665",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

And 

http://sage.math.washington.edu/home/mabshoff/cremona-20071219.p0.spkg

builds :)

Cheers,

Michael



---

archive/issue_comments_007666.json:
```json
{
    "body": "With the above spkg I get doctest failures for:\n\n```\ndevel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py\ndevel/sage-main/sage/schemes/elliptic_curves/sha.py\ndevel/sage-main/sage/libs/mwrank/interface.py\n```\nOne example:\n\n```\nsage: EllipticCurve('11a').regulator()\n-infinity\nsage:\nExiting SAGE (CPU time 0m0.17s, Wall time 0m8.09s).\nfatal error:\n    Internal error: can't free this _ntl_gbigint\nexit...\n```\n\nCheers,\n\nMichael",
    "created_at": "2007-12-19T17:13:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1233#issuecomment-7666",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With the above spkg I get doctest failures for:

```
devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py
devel/sage-main/sage/schemes/elliptic_curves/sha.py
devel/sage-main/sage/libs/mwrank/interface.py
```
One example:

```
sage: EllipticCurve('11a').regulator()
-infinity
sage:
Exiting SAGE (CPU time 0m0.17s, Wall time 0m8.09s).
fatal error:
    Internal error: can't free this _ntl_gbigint
exit...
```

Cheers,

Michael



---

archive/issue_comments_007667.json:
```json
{
    "body": "John Cremona fixed the issue mentioned above. I applied the patch to \n\nhttp://sage.math.washington.edu/home/mabshoff/cremona-20071219.p1.spkg\n\nMake also sure to apply #1573 and touch mwrank.pyx due to #1574. -testall passes on sage.math.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-20T12:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1233#issuecomment-7667",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

John Cremona fixed the issue mentioned above. I applied the patch to 

http://sage.math.washington.edu/home/mabshoff/cremona-20071219.p1.spkg

Make also sure to apply #1573 and touch mwrank.pyx due to #1574. -testall passes on sage.math.

Cheers,

Michael



---

archive/issue_comments_007668.json:
```json
{
    "body": "`cremona-20071219.p1.spkg` and #1573 merged in 2.9.1 alpha2",
    "created_at": "2007-12-20T18:08:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1233#issuecomment-7668",
    "user": "https://github.com/rlmill"
}
```

`cremona-20071219.p1.spkg` and #1573 merged in 2.9.1 alpha2



---

archive/issue_events_003258.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2007-12-20T18:08:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1233",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1233#event-3258"
}
```



---

archive/issue_comments_007669.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-20T18:08:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1233#issuecomment-7669",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
