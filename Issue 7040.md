# Issue 7040: Code actually in Sage (not other project) ignores CC and uses gcc.

archive/issues_007040.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: GNUism\n\nUsing\n\n* Solaris 10 update 7 on SPARC\n* sage-4.1.2.alpha2\n* Sun Studio 12.1\n* An updated configure script to allow the Sun compiler to be used http://sagetrac.org/sage_trac/ticket/7021\n\nCC was set to the Sun C compiler. The code in the Sage (probalby \n\n./spkg/standard/sage-4.1.2.alpha2.spkg ) is using gcc  and ignoring CC. \n\n\n```\nmake[1]: Entering directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg'\nsage-spkg sage-4.1.2.alpha2\nYou must set the SAGE_ROOT environment variable or\nrun this script from the SAGE_ROOT or\nSAGE_ROOT/local/bin/ directory.\nsage-4.1.2.alpha2\nMachine:\nSunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000\nDeleting directories from past builds of previous/current versions of sage-4.1.2.alpha2\nExtracting package /export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/standard/sage-4.1.2.alpha2.spkg ...\n-rw-r--r--   1 drkirkby other    39522776 Sep 21 23:28 /export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/standard/sage-4.1.2.alpha2.spkg\nsage-4.1.2.alpha2/\nsage-4.1.2.alpha2/doc/\n<SNIP>\nsage-4.1.2.alpha2/sage/symbolic/callable.py\nsage-4.1.2.alpha2/spkg-install\nsage-4.1.2.alpha2/README.txt\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000\n****************************************************\n****************************************************\nCC Version\n/opt/xxxsunstudio12.1/bin/cc -v\n\n\nusage: cc [ options] files.  Use 'cc -flags' for details\n****************************************************\nmv: cannot access /export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/devel/sage-main\ngcc -o src/convert.pic.o -c -fPIC -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include/python2.6 -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include/NTL -Iinclude src/convert.c\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7040\n\n",
    "created_at": "2009-09-27T16:15:31Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Code actually in Sage (not other project) ignores CC and uses gcc.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7040",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

Keywords: GNUism

Using

* Solaris 10 update 7 on SPARC
* sage-4.1.2.alpha2
* Sun Studio 12.1
* An updated configure script to allow the Sun compiler to be used http://sagetrac.org/sage_trac/ticket/7021

CC was set to the Sun C compiler. The code in the Sage (probalby 

./spkg/standard/sage-4.1.2.alpha2.spkg ) is using gcc  and ignoring CC. 


```
make[1]: Entering directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg'
sage-spkg sage-4.1.2.alpha2
You must set the SAGE_ROOT environment variable or
run this script from the SAGE_ROOT or
SAGE_ROOT/local/bin/ directory.
sage-4.1.2.alpha2
Machine:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
Deleting directories from past builds of previous/current versions of sage-4.1.2.alpha2
Extracting package /export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/standard/sage-4.1.2.alpha2.spkg ...
-rw-r--r--   1 drkirkby other    39522776 Sep 21 23:28 /export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/standard/sage-4.1.2.alpha2.spkg
sage-4.1.2.alpha2/
sage-4.1.2.alpha2/doc/
<SNIP>
sage-4.1.2.alpha2/sage/symbolic/callable.py
sage-4.1.2.alpha2/spkg-install
sage-4.1.2.alpha2/README.txt
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v


usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
mv: cannot access /export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/devel/sage-main
gcc -o src/convert.pic.o -c -fPIC -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include/python2.6 -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include/NTL -Iinclude src/convert.c
```


Issue created by migration from https://trac.sagemath.org/ticket/7040





---

archive/issue_comments_058173.json:
```json
{
    "body": "Sage just runs `distutils`, so it uses whatever compiler Python was configured with.",
    "created_at": "2017-04-19T13:14:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7040#issuecomment-58173",
    "user": "https://github.com/jdemeyer"
}
```

Sage just runs `distutils`, so it uses whatever compiler Python was configured with.



---

archive/issue_comments_058174.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2017-04-19T13:14:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7040#issuecomment-58174",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058175.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-04-19T13:14:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7040#issuecomment-58175",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058176.json:
```json
{
    "body": "Closing tickets in the sage-duplicate/invalid/wontfix module with positive_review (i.e. someone has confirmed they should be closed).",
    "created_at": "2017-07-13T07:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7040#issuecomment-58176",
    "user": "https://github.com/embray"
}
```

Closing tickets in the sage-duplicate/invalid/wontfix module with positive_review (i.e. someone has confirmed they should be closed).



---

archive/issue_events_007261.json:
```json
{
    "actor": "@embray",
    "created_at": "2017-07-13T07:54:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7040",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7040#event-7261"
}
```



---

archive/issue_comments_058177.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2017-07-13T07:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7040#issuecomment-58177",
    "user": "https://github.com/embray"
}
```

Resolution: wontfix
