# Issue 1416: get the R statistics software into Sage

archive/issues_001416.json:
```json
{
    "body": "Assignee: @williamstein\n\nTODO list\n* upgrade to 2.6.1\n* patch rpy\n* fix build issues and install issues\n* finish pexpect interface.\n* worry about graphics / X11 issues\n* readline\n* gfortran support (extra setup.py in rpy package)\n\nIssue created by migration from https://trac.sagemath.org/ticket/1416\n\n",
    "created_at": "2007-12-07T07:23:33Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "get the R statistics software into Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1416",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

TODO list
* upgrade to 2.6.1
* patch rpy
* fix build issues and install issues
* finish pexpect interface.
* worry about graphics / X11 issues
* readline
* gfortran support (extra setup.py in rpy package)

Issue created by migration from https://trac.sagemath.org/ticket/1416





---

archive/issue_comments_009106.json:
```json
{
    "body": "NOTE: For building on OSX I had to remove SAGE_ROOT/local/lib/libsqlite3.so",
    "created_at": "2007-12-07T07:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1416#issuecomment-9106",
    "user": "https://github.com/williamstein"
}
```

NOTE: For building on OSX I had to remove SAGE_ROOT/local/lib/libsqlite3.so



---

archive/issue_comments_009107.json:
```json
{
    "body": "See this for valuable info for building on osx 10.5:\nhttp://r.research.att.com/building.html",
    "created_at": "2007-12-07T07:58:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1416#issuecomment-9107",
    "user": "https://github.com/williamstein"
}
```

See this for valuable info for building on osx 10.5:
http://r.research.att.com/building.html



---

archive/issue_comments_009108.json:
```json
{
    "body": "For the integration of R we already had #348, but this ticket had more info, I turned the other ticket into a dup and closed it.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-07T10:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1416#issuecomment-9108",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

For the integration of R we already had #348, but this ticket had more info, I turned the other ticket into a dup and closed it.

Cheers,

Michael



---

archive/issue_comments_009109.json:
```json
{
    "body": "Add this to spkg/install\n\n```\nR=`$newest r`\nexport R\n```\n\n\nAdd this to spkg/standard/deps (somewhere in the middle):\n\n```\n$(INST)/$(R): $(INST)/$(PYTHON)      \n        $(SAGE_SPKG) $(R) 2>&1\n        $(MAKEREL)\n```\n\nand also add this to the big list of things the $(INST)/$(SAGE) target depends on:\n\n```\n                $(INST)/$(R)  \\\n```\n\n\nWARNING: The above is untested, so probably not perfect -- though I'm pretty confident.",
    "created_at": "2007-12-09T18:48:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1416#issuecomment-9109",
    "user": "https://github.com/williamstein"
}
```

Add this to spkg/install

```
R=`$newest r`
export R
```


Add this to spkg/standard/deps (somewhere in the middle):

```
$(INST)/$(R): $(INST)/$(PYTHON)      
        $(SAGE_SPKG) $(R) 2>&1
        $(MAKEREL)
```

and also add this to the big list of things the $(INST)/$(SAGE) target depends on:

```
                $(INST)/$(R)  \
```


WARNING: The above is untested, so probably not perfect -- though I'm pretty confident.



---

archive/issue_comments_009110.json:
```json
{
    "body": "Get the latest spkg for R here:\n\nhttp://sagemath.org/packages/optional/",
    "created_at": "2007-12-09T18:53:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1416#issuecomment-9110",
    "user": "https://github.com/williamstein"
}
```

Get the latest spkg for R here:

http://sagemath.org/packages/optional/



---

archive/issue_comments_009111.json:
```json
{
    "body": "WAIT: Readline detection still doesn't work -- i.e., only using the readline in sage -- at least on one platform, namely sagemath.org (opteron ubuntu 64bit):\n\n\n```\n0.3 -L/usr/lib/gcc -lf95 -lm  ../extra/zlib/libz.a ../extra/bzip2/libbz2.a ../extra/pcre/libpcre.a  -lreadline -lncurses  -ldl -lm\n/usr/bin/ld: cannot find -lreadline\ncollect2: ld returned 1 exit status\nmake[3]: *** [libR.so] Error 1\nmake[3]: Leaving directory `/home2/sage/s/local/lib/r/src/main'\nmake[2]: *** [R] Error 2\nmake[2]: Leaving directory `/home2/sage/s/local/lib/r/src/main'\nmake[1]: *** [R] Error 1\nmake[1]: Leaving directory `/home2/sage/s/local/lib/r/src'\nmake: *** [R] Error 1\nError building R.\n\nreal\t2m59.168s\nuser\t1m9.016s\nsys\t0m30.386s\nsage: An error occurred while installing r-2.6.1.p2\nPlease email sage-devel http://groups.google.com/group/sage-devel\nexplaining the problem and send the relevant part of\nof /home2/sage/s/install.log.  Describe your computer, operating system, etc.\nIf you want to try to fix the problem, yourself *don't* just cd to\n/home2/sage/s/spkg/build/r-2.6.1.p2 and type 'make'.\nInstead type \"/home2/sage/s/sage -sh\"\nin order to set all environment variables correctly, then cd to\n/home2/sage/s/spkg/build/r-2.6.1.p2\n(When you are done debugging, you can type \"exit\" to leave the\nsubshell.)\n\n```\n",
    "created_at": "2007-12-09T19:54:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1416#issuecomment-9111",
    "user": "https://github.com/williamstein"
}
```

WAIT: Readline detection still doesn't work -- i.e., only using the readline in sage -- at least on one platform, namely sagemath.org (opteron ubuntu 64bit):


```
0.3 -L/usr/lib/gcc -lf95 -lm  ../extra/zlib/libz.a ../extra/bzip2/libbz2.a ../extra/pcre/libpcre.a  -lreadline -lncurses  -ldl -lm
/usr/bin/ld: cannot find -lreadline
collect2: ld returned 1 exit status
make[3]: *** [libR.so] Error 1
make[3]: Leaving directory `/home2/sage/s/local/lib/r/src/main'
make[2]: *** [R] Error 2
make[2]: Leaving directory `/home2/sage/s/local/lib/r/src/main'
make[1]: *** [R] Error 1
make[1]: Leaving directory `/home2/sage/s/local/lib/r/src'
make: *** [R] Error 1
Error building R.

real	2m59.168s
user	1m9.016s
sys	0m30.386s
sage: An error occurred while installing r-2.6.1.p2
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /home2/sage/s/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/home2/sage/s/spkg/build/r-2.6.1.p2 and type 'make'.
Instead type "/home2/sage/s/sage -sh"
in order to set all environment variables correctly, then cd to
/home2/sage/s/spkg/build/r-2.6.1.p2
(When you are done debugging, you can type "exit" to leave the
subshell.)

```




---

archive/issue_comments_009112.json:
```json
{
    "body": "The r package itself appears to check versions and correctly link libf95 or libgfortran on its own. \nIt compiled fine using gfortran. The rpy package does not do this, but the spkg in 1427 that fixes the osx 10.4 build also makes is work with g95 or gfortran. So just use that rpy package.",
    "created_at": "2007-12-09T20:59:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1416#issuecomment-9112",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

The r package itself appears to check versions and correctly link libf95 or libgfortran on its own. 
It compiled fine using gfortran. The rpy package does not do this, but the spkg in 1427 that fixes the osx 10.4 build also makes is work with g95 or gfortran. So just use that rpy package.



---

archive/issue_comments_009113.json:
```json
{
    "body": "you may just want to grab the newest rpy from my home directory to make sure you actually got the newest one. \n\n                                                          Josh",
    "created_at": "2007-12-09T21:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1416#issuecomment-9113",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

you may just want to grab the newest rpy from my home directory to make sure you actually got the newest one. 

                                                          Josh



---

archive/issue_comments_009114.json:
```json
{
    "body": "Merged in 2.9.alpha3.",
    "created_at": "2007-12-10T05:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1416#issuecomment-9114",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.alpha3.



---

archive/issue_comments_009115.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-10T05:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1416#issuecomment-9115",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
