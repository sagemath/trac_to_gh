# Issue 9009: Mercurial is not building 64-bit with OpenSolaris with SAGE64=yes.

archive/issues_009009.json:
```json
{
    "body": "Assignee: drkirkby\n\nThe title says it all. This should be a pretty easy one to solve:\n\n\n```\ncreating build/lib.solaris-2.11-i86pc-2.6/hgext/zeroconf\ncopying hgext/zeroconf/__init__.py -> build/lib.solaris-2.11-i86pc-2.6/hgext/zeroconf\ncopying hgext/zeroconf/Zeroconf.py -> build/lib.solaris-2.11-i86pc-2.6/hgext/zeroconf\nrunning build_ext\nbuilding 'mercurial.base85' extension\ncreating build/temp.solaris-2.11-i86pc-2.6\ncreating build/temp.solaris-2.11-i86pc-2.6/mercurial\ngcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC -I/export/home/drkirkby/sage-4.4.2/local/include/python2.6 -c mercurial/base85.c -o build/temp.solaris-2.11-i86pc-2.6/mercurial/base85.o\nIn file included from /export/home/drkirkby/sage-4.4.2/local/include/python2.6/Python.h:58,\n                 from mercurial/base85.c:12:\n/export/home/drkirkby/sage-4.4.2/local/include/python2.6/pyport.h:685:2: error: #error \"LONG_BIT definition appears wrong for platform (bad gcc/glibc config?).\"\nerror: command 'gcc' failed with exit status 1\nError building mercurial\n\nreal\t0m0.142s\nuser\t0m0.083s\nsys\t0m0.055s\nsage: An error occurred while installing mercurial-1.3.1.p1\n```\n\n\nThe option -m64 is only being added if SAGE64 is set to yes **and** the platform is OS X, so it does not work on OpenSolaris. I've seen this problem many times, and the fix is pretty simple. \n\nIssue created by migration from https://trac.sagemath.org/ticket/9009\n\n",
    "created_at": "2010-05-21T16:17:10Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "title": "Mercurial is not building 64-bit with OpenSolaris with SAGE64=yes.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9009",
    "user": "drkirkby"
}
```
Assignee: drkirkby

The title says it all. This should be a pretty easy one to solve:


```
creating build/lib.solaris-2.11-i86pc-2.6/hgext/zeroconf
copying hgext/zeroconf/__init__.py -> build/lib.solaris-2.11-i86pc-2.6/hgext/zeroconf
copying hgext/zeroconf/Zeroconf.py -> build/lib.solaris-2.11-i86pc-2.6/hgext/zeroconf
running build_ext
building 'mercurial.base85' extension
creating build/temp.solaris-2.11-i86pc-2.6
creating build/temp.solaris-2.11-i86pc-2.6/mercurial
gcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC -I/export/home/drkirkby/sage-4.4.2/local/include/python2.6 -c mercurial/base85.c -o build/temp.solaris-2.11-i86pc-2.6/mercurial/base85.o
In file included from /export/home/drkirkby/sage-4.4.2/local/include/python2.6/Python.h:58,
                 from mercurial/base85.c:12:
/export/home/drkirkby/sage-4.4.2/local/include/python2.6/pyport.h:685:2: error: #error "LONG_BIT definition appears wrong for platform (bad gcc/glibc config?)."
error: command 'gcc' failed with exit status 1
Error building mercurial

real	0m0.142s
user	0m0.083s
sys	0m0.055s
sage: An error occurred while installing mercurial-1.3.1.p1
```


The option -m64 is only being added if SAGE64 is set to yes **and** the platform is OS X, so it does not work on OpenSolaris. I've seen this problem many times, and the fix is pretty simple. 

Issue created by migration from https://trac.sagemath.org/ticket/9009





---

archive/issue_comments_083335.json:
```json
{
    "body": "Attachment\n\nMercurial patch to allow to build 64-bit on any operating system, not just OS X",
    "created_at": "2010-05-23T11:41:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9009#issuecomment-83335",
    "user": "drkirkby"
}
```

Attachment

Mercurial patch to allow to build 64-bit on any operating system, not just OS X



---

archive/issue_comments_083336.json:
```json
{
    "body": "The revised spkg at http://boxen.math.washington.edu/home/kirkby/patches/mercurial-1.3.1.p2/mercurial-1.3.1.p2.spkg\n\nresolves this issue, by removing the restriction that the operating system needs to be OS X in order that a 64-bit compilation can be performed.  \n\n\n```\ncreating /export/home/drkirkby/sage-4.4.2/local/lib/python/mercurial/locale/el/LC_MESSAGES\ncopying locale/el/LC_MESSAGES/hg.mo -> /export/home/drkirkby/sage-4.4.2/local/lib/python/mercurial/locale/el/LC_MESSAGES\nrunning install_egg_info\nWriting /export/home/drkirkby/sage-4.4.2/local/lib/python/mercurial-1.3.1-py2.6.egg-info\nDeleting dead links\n\nreal    0m1.380s\nuser    0m1.068s\nsys     0m0.269s\nSuccessfully installed mercurial-1.3.1.p2\n```\n",
    "created_at": "2010-05-23T11:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9009#issuecomment-83336",
    "user": "drkirkby"
}
```

The revised spkg at http://boxen.math.washington.edu/home/kirkby/patches/mercurial-1.3.1.p2/mercurial-1.3.1.p2.spkg

resolves this issue, by removing the restriction that the operating system needs to be OS X in order that a 64-bit compilation can be performed.  


```
creating /export/home/drkirkby/sage-4.4.2/local/lib/python/mercurial/locale/el/LC_MESSAGES
copying locale/el/LC_MESSAGES/hg.mo -> /export/home/drkirkby/sage-4.4.2/local/lib/python/mercurial/locale/el/LC_MESSAGES
running install_egg_info
Writing /export/home/drkirkby/sage-4.4.2/local/lib/python/mercurial-1.3.1-py2.6.egg-info
Deleting dead links

real    0m1.380s
user    0m1.068s
sys     0m0.269s
Successfully installed mercurial-1.3.1.p2
```




---

archive/issue_comments_083337.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-23T11:45:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9009#issuecomment-83337",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083338.json:
```json
{
    "body": "The patch looks ok (though I don't like *overwriting* CFLAGS, but this has been in before).\n\nShould perhaps be tested/reviewed by some MacOS and/or Solaris users.",
    "created_at": "2010-05-23T15:49:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9009#issuecomment-83338",
    "user": "leif"
}
```

The patch looks ok (though I don't like *overwriting* CFLAGS, but this has been in before).

Should perhaps be tested/reviewed by some MacOS and/or Solaris users.



---

archive/issue_comments_083339.json:
```json
{
    "body": "I have tested the updated spkg on the machines t2.math (Solaris), sage.math (Ubuntu), and bsd.math (Mac OS X). The effect of the change is more prominent on t2.math because without the updated spkg, Mercurial won't build at all on that machine during the the Sage compilation process. Positive review from me.",
    "created_at": "2010-05-23T21:31:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9009#issuecomment-83339",
    "user": "mvngu"
}
```

I have tested the updated spkg on the machines t2.math (Solaris), sage.math (Ubuntu), and bsd.math (Mac OS X). The effect of the change is more prominent on t2.math because without the updated spkg, Mercurial won't build at all on that machine during the the Sage compilation process. Positive review from me.



---

archive/issue_comments_083340.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-23T21:31:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9009#issuecomment-83340",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083341.json:
```json
{
    "body": "For other OpenSolaris issues, see #9026",
    "created_at": "2010-05-24T18:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9009#issuecomment-83341",
    "user": "drkirkby"
}
```

For other OpenSolaris issues, see #9026



---

archive/issue_comments_083342.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-07T04:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9009#issuecomment-83342",
    "user": "mhansen"
}
```

Resolution: fixed
