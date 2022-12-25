# Issue 1852: Configure R to use Atlas / other improvements to R package

archive/issues_001852.json:
```json
{
    "body": "Assignee: @williamstein\n\nCurrenty R in Sage is configured to use its own implementation of BLAS, it would\nbe better to configure it to use ATLAS (wich has better performance, I think)\n\nA parameter --with-blas can be pased to configure, to tell it wich BLAS we \nwant to use.\n\nA comenet:\nSee also ticket #1721, we should avoid hardcoding the location of \nthe BLAS library . If that thicket is implemented, perhaps an enviroment \nvariable should be setto the BLAS library that we want to use (in sage-env?) \n(or a symlink from $SAGE_LOCAL/libblas.so to the system version)\n\nOther questions:\n- why is R configured with --with-reccomended-packages=no ?\n(perhaps it would be possible to offer the recommended packages as an optional\npackage?)\n\n- why is the whoule source code of R installed in $SAGE_LOCAL/lib/r ? \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1852\n\n",
    "created_at": "2008-01-19T21:39:37Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "Configure R to use Atlas / other improvements to R package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1852",
    "user": "https://github.com/pdenapo"
}
```
Assignee: @williamstein

Currenty R in Sage is configured to use its own implementation of BLAS, it would
be better to configure it to use ATLAS (wich has better performance, I think)

A parameter --with-blas can be pased to configure, to tell it wich BLAS we 
want to use.

A comenet:
See also ticket #1721, we should avoid hardcoding the location of 
the BLAS library . If that thicket is implemented, perhaps an enviroment 
variable should be setto the BLAS library that we want to use (in sage-env?) 
(or a symlink from $SAGE_LOCAL/libblas.so to the system version)

Other questions:
- why is R configured with --with-reccomended-packages=no ?
(perhaps it would be possible to offer the recommended packages as an optional
package?)

- why is the whoule source code of R installed in $SAGE_LOCAL/lib/r ? 


Issue created by migration from https://trac.sagemath.org/ticket/1852





---

archive/issue_comments_011690.json:
```json
{
    "body": "> Other questions: - why is R configured with --with-reccomended-packages=no ? \n> (perhaps it would be possible to offer the recommended packages as an optional package?)\n\nBecause `--with-recommended-packages=yes` takes 5 times to build as no. Simple as that.    And for the first few releases of R in Sage it makes sense to be conservative to keep breakage to a minimal.  We will revisit this... say now.\n\n> - why is the whoule source code of R installed in $SAGE_LOCAL/lib/r ?\n\nNo clue.  I didn't know that.  It is surprising.",
    "created_at": "2008-01-20T01:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1852#issuecomment-11690",
    "user": "https://github.com/williamstein"
}
```

> Other questions: - why is R configured with --with-reccomended-packages=no ? 
> (perhaps it would be possible to offer the recommended packages as an optional package?)

Because `--with-recommended-packages=yes` takes 5 times to build as no. Simple as that.    And for the first few releases of R in Sage it makes sense to be conservative to keep breakage to a minimal.  We will revisit this... say now.

> - why is the whoule source code of R installed in $SAGE_LOCAL/lib/r ?

No clue.  I didn't know that.  It is surprising.



---

archive/issue_comments_011691.json:
```json
{
    "body": "Somebody (was?) does the following in spkg-install:\n\n```\n# For some reason make install sucks -- it doesn't copy the libraries or R bin over ??\n\ncp lib/* \"$SAGE_LOCAL\"/lib/\ncp bin/R \"$SAGE_LOCAL\"/bin/\n```\n\n\nVery, very odd to say the least.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-23T07:41:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1852#issuecomment-11691",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Somebody (was?) does the following in spkg-install:

```
# For some reason make install sucks -- it doesn't copy the libraries or R bin over ??

cp lib/* "$SAGE_LOCAL"/lib/
cp bin/R "$SAGE_LOCAL"/bin/
```


Very, very odd to say the least.

Cheers,

Michael



---

archive/issue_comments_011692.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2008-01-23T07:44:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1852#issuecomment-11692",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_011693.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-23T07:44:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1852#issuecomment-11693",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_events_004492.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-23T09:29:38Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1852",
    "milestone": "sage-2.10.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1852#event-4492"
}
```



---

archive/issue_comments_011694.json:
```json
{
    "body": "Changing component from algebraic geometry to packages.",
    "created_at": "2008-01-24T08:56:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1852#issuecomment-11694",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebraic geometry to packages.



---

archive/issue_comments_011695.json:
```json
{
    "body": "The r.spkg was a total disaster to put it nicely. It took me about sic hours to sort it all out, but two official revisions later I have:\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha2/r-2.6.1.p10.spkg\n\nThe spkg builds on Linux and OSX, passes testall and now uses ATLAS if it is provided.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-25T11:29:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1852#issuecomment-11695",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The r.spkg was a total disaster to put it nicely. It took me about sic hours to sort it all out, but two official revisions later I have:

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha2/r-2.6.1.p10.spkg

The spkg builds on Linux and OSX, passes testall and now uses ATLAS if it is provided.

Cheers,

Michael



---

archive/issue_comments_011696.json:
```json
{
    "body": "I read the new spkg-install, built this package on all our test machines, and ran this test with success on all of them:\n\n\n```\nwas@debian32:~$ echo \"import rpy; rpy.r('2+2')\" | sage-2.10.1.alpha1/sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.10.1.alpha1, Release Date: 2008-01-21               |\n| Type notebook() for the GUI, and license() for information.        |\nsage: 4.0\nsage: \n```\n\n\nSo thumbs up.",
    "created_at": "2008-01-25T15:04:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1852#issuecomment-11696",
    "user": "https://github.com/williamstein"
}
```

I read the new spkg-install, built this package on all our test machines, and ran this test with success on all of them:


```
was@debian32:~$ echo "import rpy; rpy.r('2+2')" | sage-2.10.1.alpha1/sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.1.alpha1, Release Date: 2008-01-21               |
| Type notebook() for the GUI, and license() for information.        |
sage: 4.0
sage: 
```


So thumbs up.



---

archive/issue_comments_011697.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-25T17:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1852#issuecomment-11697",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha2



---

archive/issue_comments_011698.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-25T17:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1852#issuecomment-11698",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004493.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-25T17:28:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1852",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1852#event-4493"
}
```
