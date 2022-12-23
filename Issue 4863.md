# Issue 4863: bug in install_package

archive/issues_004863.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  mhansen mvngu\n\nIt is impossible to use the `install_package` command to install pyopenssl-0.6.  See below:\n\n\n```\nsage: install_package('pyopenssl-0.6')\nPossible names of non-installed packages starting with 'pyopenssl-0.6':\n  pyopenssl-0.6\n  pyopenssl-0.6\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/usr/local/sage/<ipython console> in <module>()\n\n/usr/local/sage/local/lib/python2.5/site-packages/sage/misc/package.pyc in install_package(package, force)\n     79         for P in L:\n     80             print \" \", P\n---> 81         raise ValueError, \"There is more than one package name starting with '%s'. Please specify!\"%(package)\n     82     if len(L)==0:\n     83         if not force:\n\nValueError: There is more than one package name starting with 'pyopenssl-0.6'. Please specify!\nsage: \n```\n\n\nI verified this error in sage-3.2.2 on Linux and OS X.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4863\n\n",
    "created_at": "2008-12-24T04:52:27Z",
    "labels": [
        "packages: optional",
        "minor",
        "bug"
    ],
    "title": "bug in install_package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4863",
    "user": "was"
}
```
Assignee: mabshoff

CC:  mhansen mvngu

It is impossible to use the `install_package` command to install pyopenssl-0.6.  See below:


```
sage: install_package('pyopenssl-0.6')
Possible names of non-installed packages starting with 'pyopenssl-0.6':
  pyopenssl-0.6
  pyopenssl-0.6
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/usr/local/sage/<ipython console> in <module>()

/usr/local/sage/local/lib/python2.5/site-packages/sage/misc/package.pyc in install_package(package, force)
     79         for P in L:
     80             print " ", P
---> 81         raise ValueError, "There is more than one package name starting with '%s'. Please specify!"%(package)
     82     if len(L)==0:
     83         if not force:

ValueError: There is more than one package name starting with 'pyopenssl-0.6'. Please specify!
sage: 
```


I verified this error in sage-3.2.2 on Linux and OS X.

Issue created by migration from https://trac.sagemath.org/ticket/4863





---

archive/issue_comments_036858.json:
```json
{
    "body": "Replying to [ticket:4863 was]:\n> It is impossible to use the `install_package` command to install pyopenssl-0.6.  \n<snip>\n> I verified this error in sage-3.2.2 on Linux and OS X.\n\nNo problem for me, at least in sage-3.2.1 on Linux.\n\nSo maybe I'll try to upgrade and check again.",
    "created_at": "2008-12-28T11:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4863#issuecomment-36858",
    "user": "SimonKing"
}
```

Replying to [ticket:4863 was]:
> It is impossible to use the `install_package` command to install pyopenssl-0.6.  
<snip>
> I verified this error in sage-3.2.2 on Linux and OS X.

No problem for me, at least in sage-3.2.1 on Linux.

So maybe I'll try to upgrade and check again.



---

archive/issue_comments_036859.json:
```json
{
    "body": "Replying to [comment:1 SimonKing]:\n> No problem for me, at least in sage-3.2.1 on Linux.\n> \n> So maybe I'll try to upgrade and check again.\n\nMeanwhile I upgraded and removed `SAGE_ROOT/spkg/installed/pyopenssl-0.6` and `SAGE_ROOT/optional/pyopenssl-0.6.spkg`. Then I tried \n`install_package('pyopenssl-0.6')` again. \n\nThere was no problem. So, I can not reproduce the bug.",
    "created_at": "2008-12-30T22:50:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4863#issuecomment-36859",
    "user": "SimonKing"
}
```

Replying to [comment:1 SimonKing]:
> No problem for me, at least in sage-3.2.1 on Linux.
> 
> So maybe I'll try to upgrade and check again.

Meanwhile I upgraded and removed `SAGE_ROOT/spkg/installed/pyopenssl-0.6` and `SAGE_ROOT/optional/pyopenssl-0.6.spkg`. Then I tried 
`install_package('pyopenssl-0.6')` again. 

There was no problem. So, I can not reproduce the bug.



---

archive/issue_comments_036860.json:
```json
{
    "body": "Replying to [ticket:4863 was]:\n> It is impossible to use the `install_package` command to install pyopenssl-0.6.  See below:\n>\n\n> ...\n>\n\n> I verified this error in sage-3.2.2 on Linux and OS X.\n\nStill (meanwhile sage-3.2.3 on Linux) I can not reproduce the problem. Doing `install_package('pyopen')` resulted in the installation of pyopenssl, meanwhile in version 0.8.\n\nSo, I suggest to resolve the bug as invalid.",
    "created_at": "2009-02-06T21:48:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4863#issuecomment-36860",
    "user": "SimonKing"
}
```

Replying to [ticket:4863 was]:
> It is impossible to use the `install_package` command to install pyopenssl-0.6.  See below:
>

> ...
>

> I verified this error in sage-3.2.2 on Linux and OS X.

Still (meanwhile sage-3.2.3 on Linux) I can not reproduce the problem. Doing `install_package('pyopen')` resulted in the installation of pyopenssl, meanwhile in version 0.8.

So, I suggest to resolve the bug as invalid.



---

archive/issue_comments_036861.json:
```json
{
    "body": "3.4 is for ReST tickets only.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T23:02:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4863#issuecomment-36861",
    "user": "mabshoff"
}
```

3.4 is for ReST tickets only.

Cheers,

Michael



---

archive/issue_comments_036862.json:
```json
{
    "body": "Please note the request to close this.",
    "created_at": "2009-10-06T19:29:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4863#issuecomment-36862",
    "user": "jason"
}
```

Please note the request to close this.



---

archive/issue_comments_036863.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-10-07T04:01:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4863#issuecomment-36863",
    "user": "mhansen"
}
```

Resolution: invalid
