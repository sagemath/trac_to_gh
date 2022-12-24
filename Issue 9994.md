# Issue 9994: Python reports compiler is broken on AIX 5.3

archive/issues_009994.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  chapoton\n\n## Hardware and software\n* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)\n* 4 x 332 MHz 32-bit PowerPC CPUs\n* 3 GB RAM\n* A fairly wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)\n* DDS-4 tape drive \n* AIX 5.3 (A POSIX certified operating system)\n* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)\n* sage-4.6.alpha1 (which has python-2.6.4.p9)\n\n## The problem\n\nPython believe the compiler is broken, but it looks to me as if it is searching for an IBM compiler, not gcc. This is based on the contents of config.log, which are attached. \n\n\n```\nWarning: Attempted to overwrite SAGE_ROOT environment variable\npython-2.6.4.p9\nMachine:\nAIX aixbox 3 5 000245984C00\nDeleting directories from past builds of previous/current versions of python-2.6.4.p9\nExtracting package /home/users/drkirkby/sage-4.6.alpha1/spkg/standard/python-2.6.4.p9.spkg ...\n-rw-r--r--   1 drkirkby staff      11790083 25 Jul 22:53 /home/users/drkirkby/sage-4.6.alpha1/spkg/standard/python-2.6.4.p9.spkg\nWarning: Attempted to overwrite SAGE_ROOT environment variable\npython-2.6.4.p9\nMachine:\nAIX aixbox 3 5 000245984C00\nDeleting directories from past builds of previous/current versions of python-2.6.4.p9\nExtracting package /home/users/drkirkby/sage-4.6.alpha1/spkg/standard/python-2.6.4.p9.spkg ...\n-rw-r--r--   1 drkirkby staff      11790083 25 Jul 22:53 /home/users/drkirkby/sage-4.6.alpha1/spkg/standard/python-2.6.4.p9.spkg\npython-2.6.4.p9/\npython-2.6.4.p9/SPKG.txt\npython-2.6.4.p9/spkg-install\npython-2.6.4.p9/.hg/\npython-2.6.4.p9/.hg/undo.dirstate\n\n<snip>\n\npython-2.6.4.p9/src/Modules/almodule.c\npython-2.6.4.p9/.hgignore\nFinished extraction\n****************************************************\nHost system\nuname -a:\nAIX aixbox 3 5 000245984C00\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: powerpc-ibm-aix5.3.0.0\nConfigured with: ../stage/gcc-4.2.4/configure --disable-shared --enable-threads=posix --prefix=/opt/pware --with-long-double-128 --with-mpf\nr=/opt/pware --with-gmp=/opt/pware\nThread model: aix\ngcc version 4.2.4\n****************************************************\nchecking for --with-universal-archs... 32-bit\nchecking MACHDEP... aix5\nchecking EXTRAPLATDIR... \nchecking machine type as reported by uname -m... 000245984C00\nchecking for --without-gcc... \nchecking for gcc... cc_r\nchecking for C compiler default output file name... \nconfigure: error: C compiler cannot create executables\nSee `config.log' for more details.\nError configuring Python.\n\nreal\t0m6.032s\nuser\t0m2.699s\nsys\t0m1.432s\nsage: An error occurred while installing python-2.6.4.p9\n```\n\n\nI'll test this with the latest Python and see if it works any better.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9995\n\n",
    "created_at": "2010-09-24T01:32:37Z",
    "labels": [
        "porting: AIX or HP-UX",
        "major",
        "bug"
    ],
    "title": "Python reports compiler is broken on AIX 5.3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9994",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  chapoton

## Hardware and software
* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
* 4 x 332 MHz 32-bit PowerPC CPUs
* 3 GB RAM
* A fairly wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
* DDS-4 tape drive 
* AIX 5.3 (A POSIX certified operating system)
* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
* sage-4.6.alpha1 (which has python-2.6.4.p9)

## The problem

Python believe the compiler is broken, but it looks to me as if it is searching for an IBM compiler, not gcc. This is based on the contents of config.log, which are attached. 


```
Warning: Attempted to overwrite SAGE_ROOT environment variable
python-2.6.4.p9
Machine:
AIX aixbox 3 5 000245984C00
Deleting directories from past builds of previous/current versions of python-2.6.4.p9
Extracting package /home/users/drkirkby/sage-4.6.alpha1/spkg/standard/python-2.6.4.p9.spkg ...
-rw-r--r--   1 drkirkby staff      11790083 25 Jul 22:53 /home/users/drkirkby/sage-4.6.alpha1/spkg/standard/python-2.6.4.p9.spkg
Warning: Attempted to overwrite SAGE_ROOT environment variable
python-2.6.4.p9
Machine:
AIX aixbox 3 5 000245984C00
Deleting directories from past builds of previous/current versions of python-2.6.4.p9
Extracting package /home/users/drkirkby/sage-4.6.alpha1/spkg/standard/python-2.6.4.p9.spkg ...
-rw-r--r--   1 drkirkby staff      11790083 25 Jul 22:53 /home/users/drkirkby/sage-4.6.alpha1/spkg/standard/python-2.6.4.p9.spkg
python-2.6.4.p9/
python-2.6.4.p9/SPKG.txt
python-2.6.4.p9/spkg-install
python-2.6.4.p9/.hg/
python-2.6.4.p9/.hg/undo.dirstate

<snip>

python-2.6.4.p9/src/Modules/almodule.c
python-2.6.4.p9/.hgignore
Finished extraction
****************************************************
Host system
uname -a:
AIX aixbox 3 5 000245984C00
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: powerpc-ibm-aix5.3.0.0
Configured with: ../stage/gcc-4.2.4/configure --disable-shared --enable-threads=posix --prefix=/opt/pware --with-long-double-128 --with-mpf
r=/opt/pware --with-gmp=/opt/pware
Thread model: aix
gcc version 4.2.4
****************************************************
checking for --with-universal-archs... 32-bit
checking MACHDEP... aix5
checking EXTRAPLATDIR... 
checking machine type as reported by uname -m... 000245984C00
checking for --without-gcc... 
checking for gcc... cc_r
checking for C compiler default output file name... 
configure: error: C compiler cannot create executables
See `config.log' for more details.
Error configuring Python.

real	0m6.032s
user	0m2.699s
sys	0m1.432s
sage: An error occurred while installing python-2.6.4.p9
```


I'll test this with the latest Python and see if it works any better.

Issue created by migration from https://trac.sagemath.org/ticket/9995





---

archive/issue_comments_100427.json:
```json
{
    "body": "config.log generated by Python. It looks like its using the wrong compiler.",
    "created_at": "2010-09-24T01:35:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9994#issuecomment-100427",
    "user": "drkirkby"
}
```

config.log generated by Python. It looks like its using the wrong compiler.



---

archive/issue_comments_100428.json:
```json
{
    "body": "Attachment [config.log](tarball://root/attachments/some-uuid/ticket9995/config.log) by drkirkby created at 2010-10-06 07:14:10\n\nThis is quite easy to fix - Python just needs to configure option `--with-gcc=\"$CC\"` added. See attached patch.",
    "created_at": "2010-10-06T07:14:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9994#issuecomment-100428",
    "user": "drkirkby"
}
```

Attachment [config.log](tarball://root/attachments/some-uuid/ticket9995/config.log) by drkirkby created at 2010-10-06 07:14:10

This is quite easy to fix - Python just needs to configure option `--with-gcc="$CC"` added. See attached patch.



---

archive/issue_comments_100429.json:
```json
{
    "body": "I'll attach the patch later!!",
    "created_at": "2010-10-06T07:21:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9994#issuecomment-100429",
    "user": "drkirkby"
}
```

I'll attach the patch later!!



---

archive/issue_comments_100430.json:
```json
{
    "body": "I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).",
    "created_at": "2019-01-15T18:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9994#issuecomment-100430",
    "user": "embray"
}
```

I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).



---

archive/issue_comments_100431.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9994#issuecomment-100431",
    "user": "mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_100432.json:
```json
{
    "body": "We should close this ticket as outdated.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9994#issuecomment-100432",
    "user": "mkoeppe"
}
```

We should close this ticket as outdated.



---

archive/issue_comments_100433.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-06-25T13:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9994#issuecomment-100433",
    "user": "chapoton"
}
```

Resolution: invalid
