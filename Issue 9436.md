# Issue 9436: zodb3 causes downloads during installation

archive/issues_009436.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  leif\n\n\n```\nJust for the record:\n\ngrep -i downloading $SAGE_ROOT/install.log:\n\nDownloading http://download.zope.org/distribution/zdaemon-2.0.0.tar.gz\nDownloading http://download.zope.org/distribution/ZConfig-2.5.tar.gz\nDownloading http://download.zope.org/distribution/zope.testing-3.5.0.tar.gz\nDownloading http://download.zope.org/distribution/zope.proxy-3.4.0.tar.gz\n\n\n-Leif\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9436\n\n",
    "created_at": "2010-07-06T14:21:08Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "zodb3 causes downloads during installation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9436",
    "user": "timdumol"
}
```
Assignee: tbd

CC:  leif


```
Just for the record:

grep -i downloading $SAGE_ROOT/install.log:

Downloading http://download.zope.org/distribution/zdaemon-2.0.0.tar.gz
Downloading http://download.zope.org/distribution/ZConfig-2.5.tar.gz
Downloading http://download.zope.org/distribution/zope.testing-3.5.0.tar.gz
Downloading http://download.zope.org/distribution/zope.proxy-3.4.0.tar.gz


-Leif
```


Issue created by migration from https://trac.sagemath.org/ticket/9436





---

archive/issue_comments_090325.json:
```json
{
    "body": "Attachment\n\nIncludes zodb3's requirements in the package.",
    "created_at": "2010-07-06T14:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9436#issuecomment-90325",
    "user": "timdumol"
}
```

Attachment

Includes zodb3's requirements in the package.



---

archive/issue_comments_090326.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-06T14:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9436#issuecomment-90326",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090327.json:
```json
{
    "body": "Package up at http://sage.math.washington.edu/home/timdumol/zodb3-3.7.0.p4.spkg",
    "created_at": "2010-07-06T14:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9436#issuecomment-90327",
    "user": "timdumol"
}
```

Package up at http://sage.math.washington.edu/home/timdumol/zodb3-3.7.0.p4.spkg



---

archive/issue_comments_090328.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-07-06T15:40:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9436#issuecomment-90328",
    "user": "rlm"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_090329.json:
```json
{
    "body": "Built Sage 4.5.alpha4 from scratch with the new zodb3 spkg (p4), now *another* file is downloaded from another place:\n\n```\n...\nzodb3-3.7.0.p4/.hg/store/00manifest.i\nFinished extraction\n****************************************************\nHost system\nuname -a:\nLinux quadriga 2.6.28-18-generic #60-Ubuntu SMP Fri Mar 12 04:26:47 UTC 2010 x86_64 GNU/Linux\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nCOLLECT_GCC=gcc\nCOLLECT_LTO_WRAPPER=/usr/libexec/gcc/x86_64-unknown-linux-gnu/4.5.0/lto-wrapper\nTarget: x86_64-unknown-linux-gnu\nConfigured with: ../src/configure --prefix=/usr --enable-version-specific-runtime-libs --program-suffix=4.5.0 --with-fpmath=sse --enable-arch=core2\nThread model: posix\ngcc version 4.5.0 (GCC)\n****************************************************\nProcessing zope.interface-3.6.1.tar.gz\nRunning zope.interface-3.6.1/setup.py -q bdist_egg --dist-dir /tmp/easy_install-oWJHZn/zope.interface-3.6.1/egg-dist-tmp-O8uYAn\nRemoving zope.interface 3.5.2 from easy-install.pth file\nAdding zope.interface 3.6.1 to easy-install.pth file\n\nInstalled /home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/zope.interface-3.6.1-py2.6-linux-x86_64.egg\nProcessing dependencies for zope.interface==3.6.1\nFinished processing dependencies for zope.interface==3.6.1\nProcessing zope.proxy-3.6.0.zip\nRunning zope.proxy-3.6.0/setup.py -q bdist_egg --dist-dir /tmp/easy_install-v0n6lX/zope.proxy-3.6.0/egg-dist-tmp-gLPbBv\nAdding zope.proxy 3.6.0 to easy-install.pth file\n\nInstalled /home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/zope.proxy-3.6.0-py2.6-linux-x86_64.egg\nProcessing dependencies for zope.proxy==3.6.0\nFinished processing dependencies for zope.proxy==3.6.0\nProcessing zope.testing-3.9.5.tar.gz\nRunning zope.testing-3.9.5/setup.py -q bdist_egg --dist-dir /tmp/easy_install-0d62W6/zope.testing-3.9.5/egg-dist-tmp-GdpPl2\nwarning: no files found matching 'sampletests' under directory 'src'\nAdding zope.testing 3.9.5 to easy-install.pth file\nInstalling zope-testrunner script to /home/leif/sage-4.5.alpha4-zodb3-p4/local/bin\n\nInstalled /home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/zope.testing-3.9.5-py2.6.egg\nProcessing dependencies for zope.testing==3.9.5\nSearching for zope.exceptions\nReading http://pypi.python.org/simple/zope.exceptions/\nReading http://svn.zope.org/zope.exceptions\nBest match: zope.exceptions 3.6.0\nDownloading http://pypi.python.org/packages/source/z/zope.exceptions/zope.exceptions-3.6.0.tar.gz#md5=491779b577a49f547982ff39b3903b1a\nProcessing zope.exceptions-3.6.0.tar.gz\nRunning zope.exceptions-3.6.0/setup.py -q bdist_egg --dist-dir /tmp/easy_install-DdGPSF/zope.exceptions-3.6.0/egg-dist-tmp-9J8MOH\nAdding zope.exceptions 3.6.0 to easy-install.pth file\n\nInstalled /home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/zope.exceptions-3.6.0-py2.6.egg\nFinished processing dependencies for zope.testing==3.9.5\nProcessing ZConfig-2.8.0.tar.gz\n...\n```\n",
    "created_at": "2010-07-06T17:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9436#issuecomment-90329",
    "user": "leif"
}
```

Built Sage 4.5.alpha4 from scratch with the new zodb3 spkg (p4), now *another* file is downloaded from another place:

```
...
zodb3-3.7.0.p4/.hg/store/00manifest.i
Finished extraction
****************************************************
Host system
uname -a:
Linux quadriga 2.6.28-18-generic #60-Ubuntu SMP Fri Mar 12 04:26:47 UTC 2010 x86_64 GNU/Linux
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/libexec/gcc/x86_64-unknown-linux-gnu/4.5.0/lto-wrapper
Target: x86_64-unknown-linux-gnu
Configured with: ../src/configure --prefix=/usr --enable-version-specific-runtime-libs --program-suffix=4.5.0 --with-fpmath=sse --enable-arch=core2
Thread model: posix
gcc version 4.5.0 (GCC)
****************************************************
Processing zope.interface-3.6.1.tar.gz
Running zope.interface-3.6.1/setup.py -q bdist_egg --dist-dir /tmp/easy_install-oWJHZn/zope.interface-3.6.1/egg-dist-tmp-O8uYAn
Removing zope.interface 3.5.2 from easy-install.pth file
Adding zope.interface 3.6.1 to easy-install.pth file

Installed /home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/zope.interface-3.6.1-py2.6-linux-x86_64.egg
Processing dependencies for zope.interface==3.6.1
Finished processing dependencies for zope.interface==3.6.1
Processing zope.proxy-3.6.0.zip
Running zope.proxy-3.6.0/setup.py -q bdist_egg --dist-dir /tmp/easy_install-v0n6lX/zope.proxy-3.6.0/egg-dist-tmp-gLPbBv
Adding zope.proxy 3.6.0 to easy-install.pth file

Installed /home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/zope.proxy-3.6.0-py2.6-linux-x86_64.egg
Processing dependencies for zope.proxy==3.6.0
Finished processing dependencies for zope.proxy==3.6.0
Processing zope.testing-3.9.5.tar.gz
Running zope.testing-3.9.5/setup.py -q bdist_egg --dist-dir /tmp/easy_install-0d62W6/zope.testing-3.9.5/egg-dist-tmp-GdpPl2
warning: no files found matching 'sampletests' under directory 'src'
Adding zope.testing 3.9.5 to easy-install.pth file
Installing zope-testrunner script to /home/leif/sage-4.5.alpha4-zodb3-p4/local/bin

Installed /home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/zope.testing-3.9.5-py2.6.egg
Processing dependencies for zope.testing==3.9.5
Searching for zope.exceptions
Reading http://pypi.python.org/simple/zope.exceptions/
Reading http://svn.zope.org/zope.exceptions
Best match: zope.exceptions 3.6.0
Downloading http://pypi.python.org/packages/source/z/zope.exceptions/zope.exceptions-3.6.0.tar.gz#md5=491779b577a49f547982ff39b3903b1a
Processing zope.exceptions-3.6.0.tar.gz
Running zope.exceptions-3.6.0/setup.py -q bdist_egg --dist-dir /tmp/easy_install-DdGPSF/zope.exceptions-3.6.0/egg-dist-tmp-9J8MOH
Adding zope.exceptions 3.6.0 to easy-install.pth file

Installed /home/leif/sage-4.5.alpha4/local/lib/python2.6/site-packages/zope.exceptions-3.6.0-py2.6.egg
Finished processing dependencies for zope.testing==3.9.5
Processing ZConfig-2.8.0.tar.gz
...
```




---

archive/issue_comments_090330.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-06T17:15:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9436#issuecomment-90330",
    "user": "leif"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_090331.json:
```json
{
    "body": "New version with zope.exceptions now at the same url. I checked the requirements of each package recursively, so there should be no more downloads.",
    "created_at": "2010-07-07T15:22:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9436#issuecomment-90331",
    "user": "timdumol"
}
```

New version with zope.exceptions now at the same url. I checked the requirements of each package recursively, so there should be no more downloads.



---

archive/issue_comments_090332.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-07T15:22:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9436#issuecomment-90332",
    "user": "timdumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_090333.json:
```json
{
    "body": "Changing keywords from \"\" to \"undesired download, zope, zodb3\".",
    "created_at": "2010-07-08T13:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9436#issuecomment-90333",
    "user": "leif"
}
```

Changing keywords from "" to "undesired download, zope, zodb3".



---

archive/issue_comments_090334.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-08T13:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9436#issuecomment-90334",
    "user": "leif"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090335.json:
```json
{
    "body": "**Works as advertised.**\n\nUbuntu 9.04, Sage 4.5.alpha4 with SageNB 0.8.1 (#9430) and zodb3 3.7.0.p4 (here) built from scratch.",
    "created_at": "2010-07-08T13:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9436#issuecomment-90335",
    "user": "leif"
}
```

**Works as advertised.**

Ubuntu 9.04, Sage 4.5.alpha4 with SageNB 0.8.1 (#9430) and zodb3 3.7.0.p4 (here) built from scratch.



---

archive/issue_comments_090336.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-08T19:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9436#issuecomment-90336",
    "user": "rlm"
}
```

Resolution: fixed
