# Issue 2205: new spkg -- sqlalchemy

archive/issues_002205.json:
```json
{
    "body": "Assignee: @yqiang\n\nKeywords: dsage, database, sqlite, sql\n\nspkg can be found here:\n\nhttp://sage.math.washington.edu/home/yqiang/spkgs/SQLAlchemy-0.4.3.p0.spkg\n\ntested on OSX (10.5), Linux\n\ndsage is going to be using sqlalchemy from now on for the database backend since it will make switching database engines seamless and also prevent me from writing crappy sql. I think other parts of SAGE that have a database component could benefit significantly from this package, especially if they are able to use an ORM pattern.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2205\n\n",
    "created_at": "2008-02-18T18:18:12Z",
    "labels": [
        "dsage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "new spkg -- sqlalchemy",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2205",
    "user": "@yqiang"
}
```
Assignee: @yqiang

Keywords: dsage, database, sqlite, sql

spkg can be found here:

http://sage.math.washington.edu/home/yqiang/spkgs/SQLAlchemy-0.4.3.p0.spkg

tested on OSX (10.5), Linux

dsage is going to be using sqlalchemy from now on for the database backend since it will make switching database engines seamless and also prevent me from writing crappy sql. I think other parts of SAGE that have a database component could benefit significantly from this package, especially if they are able to use an ORM pattern.

Issue created by migration from https://trac.sagemath.org/ticket/2205





---

archive/issue_comments_014544.json:
```json
{
    "body": "REFEREE REPORT:\n\n(1) This spkg has the OS X \"kiss of metajunk\" (notice all the ._ files that need\nto be stripped out):\n\n\n```\nteragon:Downloads was$ tar jxvf SQLAlchemy-0.4.3.p0.spkg \nSQLAlchemy-0.4.3.p0/\nSQLAlchemy-0.4.3.p0/._spkg-install\nSQLAlchemy-0.4.3.p0/spkg-install\nSQLAlchemy-0.4.3.p0/._SPKG.txt\nSQLAlchemy-0.4.3.p0/SPKG.txt\nSQLAlchemy-0.4.3.p0/src/\nSQLAlchemy-0.4.3.p0/src/._CHANGES\nSQLAlchemy-0.4.3.p0/src/CHANGES\nSQLAlchemy-0.4.3.p0/src/._doc\nSQLAlchemy-0.4.3.p0/src/doc/\nSQLAlchemy-0.4.3.p0/src/doc/._alphaapi.html\nSQLAlchemy-0.4.3.p0/src/doc/alphaapi.html\nSQLAlchemy-0.4.3.p0/src/doc/._alphaimplementation.html\nSQLAlchemy-0.4.3.p0/src/doc/alphaimplementation.html\nSQLAlchemy-0.4.3.p0/src/doc/._build\nSQLAlchemy-0.4.3.p0/src/doc/build/\nSQLAlchemy-0.4.3.p0/src/doc/build/._content\n...\n```\n\n\nMaybe you can somehow build the spkg on sage.math -- that's what I have to do to avoid this metastuff on OS X?\n\n(2) This spkg downloads stuff off the internet during install:\n\n```\n\n---------------------------------------------------------------------------\nThis script requires setuptools version 0.6c3 to run (even to display\nhelp).  I will attempt to download it for you (from\nhttp://cheeseshop.python.org/packages/2.5/s/setuptools/), but\nyou may need to enable firewall access for this script first.\nI will start the download in 15 seconds.\n\n(Note: if this machine does not have network access, please obtain the file\n\n   http://cheeseshop.python.org/packages/2.5/s/setuptools/setuptools-0.6c3-py2.5.egg\n\nand place it in this directory before rerunning this script.)\n---------------------------------------------------------------------------\nDownloading http://cheeseshop.python.org/packages/2.5/s/setuptools/s\n```\n\n\nThis is absolutely 100% forbidden for Sage packages.   Imagine a computer installation that isn't on the internet at all -- installing Sage on such computers is fully supported by Sage and must remain so.\n\n3. I think spkg-install should start with #!/bin/sh or something:\n\n```\nteragon:SQLAlchemy-0.4.3.p0 was$ more spkg-install \ncd src\npython setup.py install\n```\n\n\n4. Since src/doc is included and is pretty big, maybe it should be installed somewhere standard, e.g., SAGE_ROOT/local/doc/  It's very nice html documentation and is a shame to not install it.  Actually, more generally we should install *all* the docs for packages to SAGE_ROOT/local/doc/.  I don't know why we don't do that already.  Right now only NTL's. docs get installed. \n\n5. Can you write an spkg-check script that runs the SQLAlchemy test suite and exists with code 0 if and only if there is success.",
    "created_at": "2008-02-19T15:10:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2205#issuecomment-14544",
    "user": "@williamstein"
}
```

REFEREE REPORT:

(1) This spkg has the OS X "kiss of metajunk" (notice all the ._ files that need
to be stripped out):


```
teragon:Downloads was$ tar jxvf SQLAlchemy-0.4.3.p0.spkg 
SQLAlchemy-0.4.3.p0/
SQLAlchemy-0.4.3.p0/._spkg-install
SQLAlchemy-0.4.3.p0/spkg-install
SQLAlchemy-0.4.3.p0/._SPKG.txt
SQLAlchemy-0.4.3.p0/SPKG.txt
SQLAlchemy-0.4.3.p0/src/
SQLAlchemy-0.4.3.p0/src/._CHANGES
SQLAlchemy-0.4.3.p0/src/CHANGES
SQLAlchemy-0.4.3.p0/src/._doc
SQLAlchemy-0.4.3.p0/src/doc/
SQLAlchemy-0.4.3.p0/src/doc/._alphaapi.html
SQLAlchemy-0.4.3.p0/src/doc/alphaapi.html
SQLAlchemy-0.4.3.p0/src/doc/._alphaimplementation.html
SQLAlchemy-0.4.3.p0/src/doc/alphaimplementation.html
SQLAlchemy-0.4.3.p0/src/doc/._build
SQLAlchemy-0.4.3.p0/src/doc/build/
SQLAlchemy-0.4.3.p0/src/doc/build/._content
...
```


Maybe you can somehow build the spkg on sage.math -- that's what I have to do to avoid this metastuff on OS X?

(2) This spkg downloads stuff off the internet during install:

```

---------------------------------------------------------------------------
This script requires setuptools version 0.6c3 to run (even to display
help).  I will attempt to download it for you (from
http://cheeseshop.python.org/packages/2.5/s/setuptools/), but
you may need to enable firewall access for this script first.
I will start the download in 15 seconds.

(Note: if this machine does not have network access, please obtain the file

   http://cheeseshop.python.org/packages/2.5/s/setuptools/setuptools-0.6c3-py2.5.egg

and place it in this directory before rerunning this script.)
---------------------------------------------------------------------------
Downloading http://cheeseshop.python.org/packages/2.5/s/setuptools/s
```


This is absolutely 100% forbidden for Sage packages.   Imagine a computer installation that isn't on the internet at all -- installing Sage on such computers is fully supported by Sage and must remain so.

3. I think spkg-install should start with #!/bin/sh or something:

```
teragon:SQLAlchemy-0.4.3.p0 was$ more spkg-install 
cd src
python setup.py install
```


4. Since src/doc is included and is pretty big, maybe it should be installed somewhere standard, e.g., SAGE_ROOT/local/doc/  It's very nice html documentation and is a shame to not install it.  Actually, more generally we should install *all* the docs for packages to SAGE_ROOT/local/doc/.  I don't know why we don't do that already.  Right now only NTL's. docs get installed. 

5. Can you write an spkg-check script that runs the SQLAlchemy test suite and exists with code 0 if and only if there is success.



---

archive/issue_comments_014545.json:
```json
{
    "body": "Thanks for the feedback.\n\n1. Fixed\n\n2. We will need to make a separate package for setuptools. We should talk about using setuptools to install python packages. It is *extremely* nice. Check out\nhttp://peak.telecommunity.com/DevCenter/setuptools\nThese days if I want to install any python module, i just do 'easy_install python_module', it does the rest for me.\n\n3. Fixed\n\n4. Fixed\n\n5. What calls spkg-check? Should I call it at the end of spkg-install?",
    "created_at": "2008-02-19T16:25:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2205#issuecomment-14545",
    "user": "@yqiang"
}
```

Thanks for the feedback.

1. Fixed

2. We will need to make a separate package for setuptools. We should talk about using setuptools to install python packages. It is *extremely* nice. Check out
http://peak.telecommunity.com/DevCenter/setuptools
These days if I want to install any python module, i just do 'easy_install python_module', it does the rest for me.

3. Fixed

4. Fixed

5. What calls spkg-check? Should I call it at the end of spkg-install?



---

archive/issue_comments_014546.json:
```json
{
    "body": "Replying to [comment:2 yi]:\n> Thanks for the feedback.\n> \n> 1. Fixed\n> \n> 2. We will need to make a separate package for setuptools. We should talk about using setuptools to install python packages. It is *extremely* nice. Check out\n> http://peak.telecommunity.com/DevCenter/setuptools\n> These days if I want to install any python module, i just do 'easy_install python_module', it does the rest for me.\n\nJaap did make a setuptools.spkg already, so that should be easy to get that issue resolved. You said something about a specific version you needed. Which one is that?\n\n> 3. Fixed\n> \n> 4. Fixed\n> \n> 5. What calls spkg-check? Should I call it at the end of spkg-install?\n\nNope, it is done automatically by sage-spkg when SAGE_CHECK is non-empty. It is run before deleting the build directory. Look at the mpfr.spkg for example for a good spkg-check script.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-19T16:54:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2205#issuecomment-14546",
    "user": "mabshoff"
}
```

Replying to [comment:2 yi]:
> Thanks for the feedback.
> 
> 1. Fixed
> 
> 2. We will need to make a separate package for setuptools. We should talk about using setuptools to install python packages. It is *extremely* nice. Check out
> http://peak.telecommunity.com/DevCenter/setuptools
> These days if I want to install any python module, i just do 'easy_install python_module', it does the rest for me.

Jaap did make a setuptools.spkg already, so that should be easy to get that issue resolved. You said something about a specific version you needed. Which one is that?

> 3. Fixed
> 
> 4. Fixed
> 
> 5. What calls spkg-check? Should I call it at the end of spkg-install?

Nope, it is done automatically by sage-spkg when SAGE_CHECK is non-empty. It is run before deleting the build directory. Look at the mpfr.spkg for example for a good spkg-check script.

Cheers,

Michael



---

archive/issue_comments_014547.json:
```json
{
    "body": "Replying to [comment:3 mabshoff]:\n> Replying to [comment:2 yi]:\n> > Thanks for the feedback.\n> > \n> > 1. Fixed\n> > \n> > 2. We will need to make a separate package for setuptools. We should talk about using setuptools to install python packages. It is *extremely* nice. Check out\n> > http://peak.telecommunity.com/DevCenter/setuptools\n> > These days if I want to install any python module, i just do 'easy_install python_module', it does the rest for me.\n> \n> Jaap did make a setuptools.spkg already, so that should be easy to get that issue resolved. You said something about a specific version you needed. Which one is that?\n> \nIt needs setuptools-0.6c3 or higher.\n\n> > 3. Fixed\n> > \n> > 4. Fixed\n> > \n> > 5. What calls spkg-check? Should I call it at the end of spkg-install?\n> \n> Nope, it is done automatically by sage-spkg when SAGE_CHECK is non-empty. It is run before deleting the build directory. Look at the mpfr.spkg for example for a good spkg-check script.\n\nOk fantastic, I've added a spkg-check script which runs the unittests for SQLAlchemy. \n\nPlease review the updated spkg here:\n\nhttp://sage.math.washington.edu/home/yqiang/spkgs/SQLAlchemy-0.4.3.p0.spkg\n> \n> Cheers,\n> \n> Michael",
    "created_at": "2008-02-19T17:23:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2205#issuecomment-14547",
    "user": "@yqiang"
}
```

Replying to [comment:3 mabshoff]:
> Replying to [comment:2 yi]:
> > Thanks for the feedback.
> > 
> > 1. Fixed
> > 
> > 2. We will need to make a separate package for setuptools. We should talk about using setuptools to install python packages. It is *extremely* nice. Check out
> > http://peak.telecommunity.com/DevCenter/setuptools
> > These days if I want to install any python module, i just do 'easy_install python_module', it does the rest for me.
> 
> Jaap did make a setuptools.spkg already, so that should be easy to get that issue resolved. You said something about a specific version you needed. Which one is that?
> 
It needs setuptools-0.6c3 or higher.

> > 3. Fixed
> > 
> > 4. Fixed
> > 
> > 5. What calls spkg-check? Should I call it at the end of spkg-install?
> 
> Nope, it is done automatically by sage-spkg when SAGE_CHECK is non-empty. It is run before deleting the build directory. Look at the mpfr.spkg for example for a good spkg-check script.

Ok fantastic, I've added a spkg-check script which runs the unittests for SQLAlchemy. 

Please review the updated spkg here:

http://sage.math.washington.edu/home/yqiang/spkgs/SQLAlchemy-0.4.3.p0.spkg
> 
> Cheers,
> 
> Michael



---

archive/issue_comments_014548.json:
```json
{
    "body": "Depends on http://trac.sagemath.org/sage_trac/ticket/1868",
    "created_at": "2008-02-19T17:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2205#issuecomment-14548",
    "user": "@yqiang"
}
```

Depends on http://trac.sagemath.org/sage_trac/ticket/1868



---

archive/issue_comments_014549.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-03-12T05:25:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2205#issuecomment-14549",
    "user": "@rlmill"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_014550.json:
```json
{
    "body": "Replying to [comment:5 yi]:\n> Depends on http://trac.sagemath.org/sage_trac/ticket/1868\n\nNope, it depends on #2481 :)\n\nCheers,\n\nMichael",
    "created_at": "2008-03-14T15:23:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2205#issuecomment-14550",
    "user": "mabshoff"
}
```

Replying to [comment:5 yi]:
> Depends on http://trac.sagemath.org/sage_trac/ticket/1868

Nope, it depends on #2481 :)

Cheers,

Michael



---

archive/issue_comments_014551.json:
```json
{
    "body": "Hi Yi,\n\nI did various things:\n* add an hg repo\n* add .hgignore\n* fix various small issues.\n* rename the spkg to all lowercase\n\nAll changes can be found in \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.4/alpha0/sqlalchemy-0.4.3.p1.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-03-14T17:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2205#issuecomment-14551",
    "user": "mabshoff"
}
```

Hi Yi,

I did various things:
* add an hg repo
* add .hgignore
* fix various small issues.
* rename the spkg to all lowercase

All changes can be found in 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.4/alpha0/sqlalchemy-0.4.3.p1.spkg

Cheers,

Michael



---

archive/issue_comments_014552.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-14T17:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2205#issuecomment-14552",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014553.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-14T17:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2205#issuecomment-14553",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.alpha0



---

archive/issue_comments_014554.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-03-14T19:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2205#issuecomment-14554",
    "user": "@williamstein"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_014555.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-03-14T19:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2205#issuecomment-14555",
    "user": "@williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_014556.json:
```json
{
    "body": "I'm reopening this because there is now a procedure for new spkg's to go into sage, and we need to follow it.",
    "created_at": "2008-03-14T19:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2205#issuecomment-14556",
    "user": "@williamstein"
}
```

I'm reopening this because there is now a procedure for new spkg's to go into sage, and we need to follow it.



---

archive/issue_comments_014557.json:
```json
{
    "body": "As per http://groups.google.com/group/sage-devel/t/1c42fb1e4ca32230 we have a unanimous vote for inclusion.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-15T08:35:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2205#issuecomment-14557",
    "user": "mabshoff"
}
```

As per http://groups.google.com/group/sage-devel/t/1c42fb1e4ca32230 we have a unanimous vote for inclusion.

Cheers,

Michael



---

archive/issue_comments_014558.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-15T08:35:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2205#issuecomment-14558",
    "user": "mabshoff"
}
```

Resolution: fixed
