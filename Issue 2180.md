# Issue 2180: cython skipping build optimization

archive/issues_002180.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @bobmoretti\n\nIn 2.10.2.alpha0, there appears to be a small problem with the cython skipping \nstep. \u00a0To illustrate the bug:\n1) \u00a0Start with a 2.10.2.alpha0 (with padic import patch) which is built \nup-to-date\n2) \u00a0Add a new patch which adds a new .pyx file\n3) \u00a0sage -br\n4) \u00a0The bug is that you get a message like: \nbuilding 'sage.rings.polynomial.multi_polynomial_factor' extension\nerror: unknown file type '.pyx' \n(from 'sage/rings/polynomial/multi_polynomial_factor.pyx')\nsage: There was an error installing modified sage library code.\n\n\nThis appears to arise because the new .pyx file is not in the cache and so the \nbuild optimizer believes that there are no .pyx files to build and just lets \nthe ordinary disttools do their work. \u00a0Of course, the ordinary disttools \ndon't know what to do with .pyx files.\n\nA work-around is to 'touch' a .pyx file anywhere in the tree which is already \nin the cache. \u00a0A build after the touch will build the touch'ed file and the \nnew file.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2180\n\n",
    "created_at": "2008-02-16T20:56:40Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "cython skipping build optimization",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2180",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```
Assignee: @williamstein

CC:  @bobmoretti

In 2.10.2.alpha0, there appears to be a small problem with the cython skipping 
step.  To illustrate the bug:
1)  Start with a 2.10.2.alpha0 (with padic import patch) which is built 
up-to-date
2)  Add a new patch which adds a new .pyx file
3)  sage -br
4)  The bug is that you get a message like: 
building 'sage.rings.polynomial.multi_polynomial_factor' extension
error: unknown file type '.pyx' 
(from 'sage/rings/polynomial/multi_polynomial_factor.pyx')
sage: There was an error installing modified sage library code.


This appears to arise because the new .pyx file is not in the cache and so the 
build optimizer believes that there are no .pyx files to build and just lets 
the ordinary disttools do their work.  Of course, the ordinary disttools 
don't know what to do with .pyx files.

A work-around is to 'touch' a .pyx file anywhere in the tree which is already 
in the cache.  A build after the touch will build the touch'ed file and the 
new file.

Issue created by migration from https://trac.sagemath.org/ticket/2180





---

archive/issue_comments_014285.json:
```json
{
    "body": "Changing component from algebraic geometry to packages.",
    "created_at": "2008-02-16T20:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2180#issuecomment-14285",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Changing component from algebraic geometry to packages.



---

archive/issue_comments_014286.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2008-02-16T20:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2180#issuecomment-14286",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_014287.json:
```json
{
    "body": "I have seen this issue before and I believe the new caching code is at fault, so it should be assigned to Bobby Moretti. I have speculated that if you patch in a new file the time stamp of the new file is too old for the precomputed hashes to be recomputed. \n\nCheers,\n\nMichael",
    "created_at": "2008-02-24T00:26:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2180#issuecomment-14287",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I have seen this issue before and I believe the new caching code is at fault, so it should be assigned to Bobby Moretti. I have speculated that if you patch in a new file the time stamp of the new file is too old for the precomputed hashes to be recomputed. 

Cheers,

Michael



---

archive/issue_comments_014288.json:
```json
{
    "body": "Changing assignee from mabshoff to @bobmoretti.",
    "created_at": "2008-02-24T00:26:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2180#issuecomment-14288",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from mabshoff to @bobmoretti.



---

archive/issue_comments_014289.json:
```json
{
    "body": "Replying to [comment:2 mabshoff]:\n> I have seen this issue before and I believe the new caching code is at fault, so it should be assigned to Bobby Moretti. I have speculated that if you patch in a new file the time stamp of the new file is too old for the precomputed hashes to be recomputed. \n> \n> Cheers,\n> \n> Michael\n\nMicheal, I think you're dead on. This is actually William's code, but I'm pretty familiar with it and I'll try to implement a fix.\n\n-Bobby",
    "created_at": "2008-02-24T02:27:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2180#issuecomment-14289",
    "user": "https://github.com/bobmoretti"
}
```

Replying to [comment:2 mabshoff]:
> I have seen this issue before and I believe the new caching code is at fault, so it should be assigned to Bobby Moretti. I have speculated that if you patch in a new file the time stamp of the new file is too old for the precomputed hashes to be recomputed. 
> 
> Cheers,
> 
> Michael

Micheal, I think you're dead on. This is actually William's code, but I'm pretty familiar with it and I'll try to implement a fix.

-Bobby



---

archive/issue_comments_014290.json:
```json
{
    "body": "Joel,\n\nWere you running hg from the command line or were you applying the patch from within Sage? I cannot get the error to reproduce.\n\n-Bobby",
    "created_at": "2008-02-24T03:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2180#issuecomment-14290",
    "user": "https://github.com/bobmoretti"
}
```

Joel,

Were you running hg from the command line or were you applying the patch from within Sage? I cannot get the error to reproduce.

-Bobby



---

archive/issue_comments_014291.json:
```json
{
    "body": "I do not know how to reproduce this.  I've tried what you suggested and I can't.\nI also think it is very unlikely that this is caused by the initial caching (i.e., my code) as Bobby suggests, since that code is really ridiculously simple.  It's just this: \n\n```\ndef hash_of_cython_file_timestamps():\n    h = 0\n    extensions = set(['.pyx', '.pxd', '.pxi'])\n    def hash_of_dir(dir):\n        h = 0\n        for f in os.listdir(dir):\n            z = dir + '/' + f\n            if os.path.isdir(z):\n                h += hash_of_dir(z)\n            elif f[-4:] in extensions and f[0] != '.':\n                h += hash(os.path.getmtime(z))\n        return h\n    return hash_of_dir('sage')\n```\n\n\nThe above just computes a hash of *all* cython related files in all subdirectories.\nIf you change anything it changes and the cythoning code reruns.  All that matters is that something has changed in any timestamp of any cython-related file, even something not listed in setup.py.  This gets run and if it isn't the same as last time then the usual Cython code gets run (Bobby's code).  If a patch has a Cython file in it, even if it hasn't changed in a long time, it'll change the above hash, which will make the Cythoning rerun.  \n\nSo I can't understand how to reproduce your bug.  Could you please please find a systematic way to reproduce it, so we can fix it?  I'm not clever enough to think of anything based on the hints.\n\nDid you definitely do `hg_sage.update()`?\n\nWAIT -- idea!\nActually, one possibility might be that the patch added a .pyx file that you \nalready had with the same time stamp, but it *only* added it to setup.py.  Thus setup.py changed but no Cython files changed, but indeed it's now necessary to\nrerun Cython.  Ah ha.  I bet the fix is to just add setup.py to the list of \"cython\"\nrelated files. \n\nI've made a patch based on this idea, and also added a little bit of nice\nverbose timing information about how long Cython'ing takes and attached a patch.\nJoel -- please referee this and let me know if this maybe solves this problem.\n\nOnce again, thanks for reporting these subtle bugs!",
    "created_at": "2008-02-24T05:15:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2180#issuecomment-14291",
    "user": "https://github.com/williamstein"
}
```

I do not know how to reproduce this.  I've tried what you suggested and I can't.
I also think it is very unlikely that this is caused by the initial caching (i.e., my code) as Bobby suggests, since that code is really ridiculously simple.  It's just this: 

```
def hash_of_cython_file_timestamps():
    h = 0
    extensions = set(['.pyx', '.pxd', '.pxi'])
    def hash_of_dir(dir):
        h = 0
        for f in os.listdir(dir):
            z = dir + '/' + f
            if os.path.isdir(z):
                h += hash_of_dir(z)
            elif f[-4:] in extensions and f[0] != '.':
                h += hash(os.path.getmtime(z))
        return h
    return hash_of_dir('sage')
```


The above just computes a hash of *all* cython related files in all subdirectories.
If you change anything it changes and the cythoning code reruns.  All that matters is that something has changed in any timestamp of any cython-related file, even something not listed in setup.py.  This gets run and if it isn't the same as last time then the usual Cython code gets run (Bobby's code).  If a patch has a Cython file in it, even if it hasn't changed in a long time, it'll change the above hash, which will make the Cythoning rerun.  

So I can't understand how to reproduce your bug.  Could you please please find a systematic way to reproduce it, so we can fix it?  I'm not clever enough to think of anything based on the hints.

Did you definitely do `hg_sage.update()`?

WAIT -- idea!
Actually, one possibility might be that the patch added a .pyx file that you 
already had with the same time stamp, but it *only* added it to setup.py.  Thus setup.py changed but no Cython files changed, but indeed it's now necessary to
rerun Cython.  Ah ha.  I bet the fix is to just add setup.py to the list of "cython"
related files. 

I've made a patch based on this idea, and also added a little bit of nice
verbose timing information about how long Cython'ing takes and attached a patch.
Joel -- please referee this and let me know if this maybe solves this problem.

Once again, thanks for reporting these subtle bugs!



---

archive/issue_comments_014292.json:
```json
{
    "body": "this might (?) completely fix the bug; it also adds some nice timing output",
    "created_at": "2008-02-24T05:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2180#issuecomment-14292",
    "user": "https://github.com/williamstein"
}
```

this might (?) completely fix the bug; it also adds some nice timing output



---

archive/issue_comments_014293.json:
```json
{
    "body": "Attachment [sage-2180.patch](tarball://root/attachments/some-uuid/ticket2180/sage-2180.patch) by mabshoff created at 2008-02-24 09:22:45",
    "created_at": "2008-02-24T09:22:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2180#issuecomment-14293",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [sage-2180.patch](tarball://root/attachments/some-uuid/ticket2180/sage-2180.patch) by mabshoff created at 2008-02-24 09:22:45



---

archive/issue_comments_014294.json:
```json
{
    "body": "This error happened when I created a .pyx file, saved it, then put it into setup.py.  This would suggest that William is right about what's going on.",
    "created_at": "2008-02-24T10:22:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2180#issuecomment-14294",
    "user": "https://github.com/roed314"
}
```

This error happened when I created a .pyx file, saved it, then put it into setup.py.  This would suggest that William is right about what's going on.



---

archive/issue_comments_014295.json:
```json
{
    "body": "This patch looks good. It does fix the bug in question, but #2295 is also relevant in this case for a bug with the same symptoms, but different cause. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-24T20:35:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2180#issuecomment-14295",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch looks good. It does fix the bug in question, but #2295 is also relevant in this case for a bug with the same symptoms, but different cause. Positive review.

Cheers,

Michael



---

archive/issue_comments_014296.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-24T20:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2180#issuecomment-14296",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014297.json:
```json
{
    "body": "Merged in Sage 2.10.3.alpha0",
    "created_at": "2008-02-24T20:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2180#issuecomment-14297",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.alpha0
