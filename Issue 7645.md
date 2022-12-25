# Issue 7645: 'set -e' used inappropriately in python-2.6.2.p4

archive/issues_007645.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @williamstein @mwhansen\n\nThe following is one more example of where trying to build Sage on an uncommon platform (HP-UX) discovers bugs which affect **all** platforms. This is yet one more justification of why it is desirable to POSIX compatible portable code and check Sage on many platforms.  \n\nAs you can see below, python does not build on my HP C3600 running HP-UX 11i, but we have no clue whatsoever why. Normally Sage would give some clue, but here there is none. \n\n```\npython-2.6.2.p4/src/Tools/world/README\npython-2.6.2.p4/src/Tools/world/world\nFinished extraction\n****************************************************\nHost system\nuname -a:\nHP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: hppa1.1-hp-hpux11.11\nConfigured with: /tmp/gcc-4.3.3.tar.gz/gcc-4.3.3/configure --host=hppa1.1-hp-hpux11.11 --target=hppa1.1-hp-hpux11.11 --build=hppa1.1-hp-hpux11.11 --prefix=/opt/hp-gcc-4.3.3 --with-gnu-as --without-gnu-ld --enable-threads=posix --enable-languages=c,c++ --with-gmp=/proj/opensrc/be/hppa1.1-hp-hpux11.11 --with-mpfr=/proj/opensrc/be/hppa1.1-hp-hpux11.11\nThread model: posix\ngcc version 4.3.3 (GCC) \n****************************************************\n\nreal\t0m0.111s\nuser\t0m0.050s\nsys\t0m0.040s\nsage: An error occurred while installing python-2.6.2.p4\n```\n\n\nThe reason no error message is generated, is due to the inappropriate use of \n\n\n```\nset -e\n```\n\n\nin the spkg-install script. The package python-2.6.2.p4 has in spkg-install\n\n\n```\n# This tells Bash to exit the script if any statement returns \n# a non-true value.\nset -e\n\n# PATCH\n\ncp patches/ctypes__init__.py src/Lib/ctypes/__init__.py\nif [ $? -ne 0 ]; then\n    echo \"Error copying patched ctypes\"\n    exit 1\nfi\n\ncp patches/locale.py src/Lib/\nif [ $? -ne 0 ]; then\n    echo \"Error copying patched locale.py\"\n    exit 1\nfi\n\n```\n\n\nIt should be noted that 'set -e' causes any failure to result in the script exiting **immediately** with a non-zero exit code. Since the script has exited, no further processing takes place - even the code which checks for an error! \n\nI've cc'ed the ticket to Mike and William, as they are listed as package maintainers. \n\n\nDave \n\nIssue created by migration from https://trac.sagemath.org/ticket/7645\n\n",
    "created_at": "2009-12-10T00:17:47Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "'set -e' used inappropriately in python-2.6.2.p4",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7645",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: GeorgSWeber

CC:  @williamstein @mwhansen

The following is one more example of where trying to build Sage on an uncommon platform (HP-UX) discovers bugs which affect **all** platforms. This is yet one more justification of why it is desirable to POSIX compatible portable code and check Sage on many platforms.  

As you can see below, python does not build on my HP C3600 running HP-UX 11i, but we have no clue whatsoever why. Normally Sage would give some clue, but here there is none. 

```
python-2.6.2.p4/src/Tools/world/README
python-2.6.2.p4/src/Tools/world/world
Finished extraction
****************************************************
Host system
uname -a:
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: hppa1.1-hp-hpux11.11
Configured with: /tmp/gcc-4.3.3.tar.gz/gcc-4.3.3/configure --host=hppa1.1-hp-hpux11.11 --target=hppa1.1-hp-hpux11.11 --build=hppa1.1-hp-hpux11.11 --prefix=/opt/hp-gcc-4.3.3 --with-gnu-as --without-gnu-ld --enable-threads=posix --enable-languages=c,c++ --with-gmp=/proj/opensrc/be/hppa1.1-hp-hpux11.11 --with-mpfr=/proj/opensrc/be/hppa1.1-hp-hpux11.11
Thread model: posix
gcc version 4.3.3 (GCC) 
****************************************************

real	0m0.111s
user	0m0.050s
sys	0m0.040s
sage: An error occurred while installing python-2.6.2.p4
```


The reason no error message is generated, is due to the inappropriate use of 


```
set -e
```


in the spkg-install script. The package python-2.6.2.p4 has in spkg-install


```
# This tells Bash to exit the script if any statement returns 
# a non-true value.
set -e

# PATCH

cp patches/ctypes__init__.py src/Lib/ctypes/__init__.py
if [ $? -ne 0 ]; then
    echo "Error copying patched ctypes"
    exit 1
fi

cp patches/locale.py src/Lib/
if [ $? -ne 0 ]; then
    echo "Error copying patched locale.py"
    exit 1
fi

```


It should be noted that 'set -e' causes any failure to result in the script exiting **immediately** with a non-zero exit code. Since the script has exited, no further processing takes place - even the code which checks for an error! 

I've cc'ed the ticket to Mike and William, as they are listed as package maintainers. 


Dave 

Issue created by migration from https://trac.sagemath.org/ticket/7645





---

archive/issue_comments_065258.json:
```json
{
    "body": "Old version, no longer relevant.",
    "created_at": "2013-05-19T13:05:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7645#issuecomment-65258",
    "user": "https://github.com/jdemeyer"
}
```

Old version, no longer relevant.



---

archive/issue_comments_065259.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-05-19T13:05:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7645#issuecomment-65259",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065260.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-05-19T13:06:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7645#issuecomment-65260",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065261.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-05-21T07:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7645#issuecomment-65261",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid



---

archive/issue_events_007868.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-05-21T07:24:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7645",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7645#event-7868"
}
```
