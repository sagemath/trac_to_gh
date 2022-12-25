# Issue 1663: scipy build fails in tr_TR locale

archive/issues_001663.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @jasongrout jkantor @TimDumol @rlmill\n\nScipy build fails with the following error when locale is set to `tr_TR.UTF-8`.\n\n```\nbuilding 'odepack' library\ncompiling Fortran sources\nFortran f77 compiler: sage_fortran -ffixed-form -fno-second-underscore\n-O\nFortran f90 compiler: sage_fortran -fno-second-underscore -O\nFortran fix compiler: sage_fortran -ffixed-form -fno-second-underscore\n-O\ncreating build/temp.linux-i686-2.5/scipy/integrate/odepack\ncompile options: '-c'\nsage_fortran:f77: scipy/integrate/odepack/lsoda.f\nsage_fortran:f77: scipy/integrate/odepack/mdp.f\nsage_fortran:f77: scipy/integrate/odepack/vnorm.f\nsage_fortran:f77: scipy/integrate/odepack/xerrwv.f\nIn file scipy/integrate/odepack/xerrwv.f:103\n\n 20   format(6x,'in above message,  i1 =',i10)\n                                          1\nError: Unexpected element in format string at (1)\nIn file scipy/integrate/odepack/xerrwv.f:105\n\n 30   format(6x,'in above message,  i1 =',i10,3x,'i2 =',i10)\n                                          1\nError: Unexpected element in format string at (1)\nIn file scipy/integrate/odepack/xerrwv.f:103\n\n 20   format(6x,'in above message,  i1 =',i10)\n                                          1\nError: Unexpected element in format string at (1)\nIn file scipy/integrate/odepack/xerrwv.f:105\n\n 30   format(6x,'in above message,  i1 =',i10,3x,'i2 =',i10)\n                                          1\nError: Unexpected element in format string at (1)\nerror: Command \"sage_fortran -ffixed-form -fno-second-underscore -O -c\n-c scipy/integrate/odepack/xerrwv.f -o build/temp.linux-i686-2.5/scipy/\nintegrate/odepack/xerrwv.o\" failed with exit status 1\n```\n\nIn the tr_TR locale, lowercase of `I` is `\u0131`, and uppercase of `i` is `\u0130`. This might cause unexpected results for auto generated files.\n\nA simple workaround is to clear the locale environment variables:\n\n```\nunset LANG LC_ALL LC_CTYPE\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1663\n\n",
    "created_at": "2008-01-03T09:59:57Z",
    "labels": [
        "component: packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "scipy build fails in tr_TR locale",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1663",
    "user": "https://github.com/burcin"
}
```
Assignee: mabshoff

CC:  @jasongrout jkantor @TimDumol @rlmill

Scipy build fails with the following error when locale is set to `tr_TR.UTF-8`.

```
building 'odepack' library
compiling Fortran sources
Fortran f77 compiler: sage_fortran -ffixed-form -fno-second-underscore
-O
Fortran f90 compiler: sage_fortran -fno-second-underscore -O
Fortran fix compiler: sage_fortran -ffixed-form -fno-second-underscore
-O
creating build/temp.linux-i686-2.5/scipy/integrate/odepack
compile options: '-c'
sage_fortran:f77: scipy/integrate/odepack/lsoda.f
sage_fortran:f77: scipy/integrate/odepack/mdp.f
sage_fortran:f77: scipy/integrate/odepack/vnorm.f
sage_fortran:f77: scipy/integrate/odepack/xerrwv.f
In file scipy/integrate/odepack/xerrwv.f:103

 20   format(6x,'in above message,  i1 =',i10)
                                          1
Error: Unexpected element in format string at (1)
In file scipy/integrate/odepack/xerrwv.f:105

 30   format(6x,'in above message,  i1 =',i10,3x,'i2 =',i10)
                                          1
Error: Unexpected element in format string at (1)
In file scipy/integrate/odepack/xerrwv.f:103

 20   format(6x,'in above message,  i1 =',i10)
                                          1
Error: Unexpected element in format string at (1)
In file scipy/integrate/odepack/xerrwv.f:105

 30   format(6x,'in above message,  i1 =',i10,3x,'i2 =',i10)
                                          1
Error: Unexpected element in format string at (1)
error: Command "sage_fortran -ffixed-form -fno-second-underscore -O -c
-c scipy/integrate/odepack/xerrwv.f -o build/temp.linux-i686-2.5/scipy/
integrate/odepack/xerrwv.o" failed with exit status 1
```

In the tr_TR locale, lowercase of `I` is `ı`, and uppercase of `i` is `İ`. This might cause unexpected results for auto generated files.

A simple workaround is to clear the locale environment variables:

```
unset LANG LC_ALL LC_CTYPE
```

Issue created by migration from https://trac.sagemath.org/ticket/1663





---

archive/issue_comments_010539.json:
```json
{
    "body": "This sounds fine as a temporary workaround, but we need to do the following things:\n\n* figure out if it happens with an unmodified python and numpy/scipy\n* if not figure out what we did wrong\n* alternatively report this upstream to the scipy people\n\nCheers,\n\nMichael",
    "created_at": "2008-01-03T11:57:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1663#issuecomment-10539",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This sounds fine as a temporary workaround, but we need to do the following things:

* figure out if it happens with an unmodified python and numpy/scipy
* if not figure out what we did wrong
* alternatively report this upstream to the scipy people

Cheers,

Michael



---

archive/issue_comments_010540.json:
```json
{
    "body": "scipy standalone build works fine on Pardus, I suspect this is due to our Python changes,\n\nwe build with following configure options added: --enable-unicode=ucs4 --with-wctype-functions\n\nand we apply http://svn.uludag.org.tr/pardus/devel/system/base/python/files/default-utf8.patch\n\nRegards,\nismail",
    "created_at": "2008-01-03T14:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1663#issuecomment-10540",
    "user": "https://trac.sagemath.org/admin/accounts/users/cartman"
}
```

scipy standalone build works fine on Pardus, I suspect this is due to our Python changes,

we build with following configure options added: --enable-unicode=ucs4 --with-wctype-functions

and we apply http://svn.uludag.org.tr/pardus/devel/system/base/python/files/default-utf8.patch

Regards,
ismail



---

archive/issue_comments_010541.json:
```json
{
    "body": "The ticket to switch to ucs4 is #551. The 2.10 release should be a good point in time to do the conversion since we will update a boat load of spkgs.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-03T14:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1663#issuecomment-10541",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The ticket to switch to ucs4 is #551. The 2.10 release should be a good point in time to do the conversion since we will update a boat load of spkgs.

Cheers,

Michael



---

archive/issue_comments_010542.json:
```json
{
    "body": "We should also check Pardus's svn repo for fixes at.\n\nhttp://svn.uludag.org.tr/pardus/devel/system/base/python/files\n\nCheers,\n\nMichael",
    "created_at": "2008-01-03T15:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1663#issuecomment-10542",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

We should also check Pardus's svn repo for fixes at.

http://svn.uludag.org.tr/pardus/devel/system/base/python/files

Cheers,

Michael



---

archive/issue_comments_010543.json:
```json
{
    "body": "The problem remains, after the switch to ucs4, using a python built with the changes mentioned in comment:2. \n\nLooking at the error message again, I don't see how this can be related to python. I can't find any other changes in the Pardus repository which might effect the scipy build. Ismail, any ideas?\n\nI suggest clearing the LANG, LC_ALL and LC_CTYPE variables in the scipy spkg-install for now, as a work around.",
    "created_at": "2008-01-17T16:28:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1663#issuecomment-10543",
    "user": "https://github.com/burcin"
}
```

The problem remains, after the switch to ucs4, using a python built with the changes mentioned in comment:2. 

Looking at the error message again, I don't see how this can be related to python. I can't find any other changes in the Pardus repository which might effect the scipy build. Ismail, any ideas?

I suggest clearing the LANG, LC_ALL and LC_CTYPE variables in the scipy spkg-install for now, as a work around.



---

archive/issue_comments_010544.json:
```json
{
    "body": "Setting LC_ALL to C should workaround all this problems, weird thing is how it compiles here. I will dig a bit more and let you know. Sorry for the late reply, trac somehow does not e-mail me new messages :-/",
    "created_at": "2008-01-21T13:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1663#issuecomment-10544",
    "user": "https://trac.sagemath.org/admin/accounts/users/cartman"
}
```

Setting LC_ALL to C should workaround all this problems, weird thing is how it compiles here. I will dig a bit more and let you know. Sorry for the late reply, trac somehow does not e-mail me new messages :-/



---

archive/issue_comments_010545.json:
```json
{
    "body": "The SciPy people have actually fixed this bug, so once we update it should be resolved.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-01T22:44:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1663#issuecomment-10545",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The SciPy people have actually fixed this bug, so once we update it should be resolved.

Cheers,

Michael



---

archive/issue_comments_010546.json:
```json
{
    "body": "Since the Scipy people have not done a release in an eternity we should really add the workaround to our scipy.spkg for now to close the issue. I will take care of this in the short term.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-11T12:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1663#issuecomment-10546",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Since the Scipy people have not done a release in an eternity we should really add the workaround to our scipy.spkg for now to close the issue. I will take care of this in the short term.

Cheers,

Michael



---

archive/issue_comments_010547.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-11T12:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1663#issuecomment-10547",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010548.json:
```json
{
    "body": "scipy was upgraded with #3391, but this problem still remains. Error message is the same.\n\nTo reproduce the error, \n\n```\nexport LC_CTYPE=tr_TR.UTF-8\n```\n\nand build Sage as usual.",
    "created_at": "2009-06-15T09:39:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1663#issuecomment-10548",
    "user": "https://github.com/burcin"
}
```

scipy was upgraded with #3391, but this problem still remains. Error message is the same.

To reproduce the error, 

```
export LC_CTYPE=tr_TR.UTF-8
```

and build Sage as usual.



---

archive/issue_comments_010549.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T12:46:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1663#issuecomment-10549",
    "user": "https://github.com/burcin"
}
```

Resolution: fixed



---

archive/issue_events_004107.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2010-01-19T12:46:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1663",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1663#event-4107"
}
```



---

archive/issue_comments_010550.json:
```json
{
    "body": "Sage-4.3.1.rc1 just built with `LC_CTYPE=tr_TR.UTF-8` on my laptop. This seems to be fixed by the latest scipy update.",
    "created_at": "2010-01-19T12:46:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1663#issuecomment-10550",
    "user": "https://github.com/burcin"
}
```

Sage-4.3.1.rc1 just built with `LC_CTYPE=tr_TR.UTF-8` on my laptop. This seems to be fixed by the latest scipy update.



---

archive/issue_comments_010551.json:
```json
{
    "body": "The SciPy 0.7.1 package included in Sage was done by Jason Grout, not by me. The setup.py packages of his package were more up-to-date, so his was included (also, he made his much earlier).",
    "created_at": "2010-01-21T10:40:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1663#issuecomment-10551",
    "user": "https://github.com/TimDumol"
}
```

The SciPy 0.7.1 package included in Sage was done by Jason Grout, not by me. The setup.py packages of his package were more up-to-date, so his was included (also, he made his much earlier).
