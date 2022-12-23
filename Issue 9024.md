# Issue 9024: tachyon is buiding 32-bit on OpenSolaris x64 even when SAGE64 is set to "yes"

archive/issues_009024.json:
```json
{
    "body": "Assignee: drkirkby\n\n'tachyon' has a script called 'Make-arch' which has various architectures. But there was not one for 64-bit Solaris on x86. The code in Sage currently uses the target 'solaris-pthreads-gcc' - see below\n\n\n```\nif [ $UNAME = \"SunOS\" ]; then\n    make solaris-pthreads-gcc\n    finished\nfi\n```\n\n\nThat target consists of the lines:\n\n\n```\nsolaris-pthreads-gcc:\n        $(MAKE) all \\\n        \"ARCH = solaris-pthreads-gcc\" \\\n        \"CC = gcc\" \\\n        \"CFLAGS = -Wall -O6 -fomit-frame-pointer -ffast-math -D_REENTRANT -DSunOS $(MISCFLAGS) -DTHR -DUSEPOSIXTHREADS\" \\\n        \"AR = ar\" \\\n        \"ARFLAGS = r\" \\\n        \"STRIP = strip\" \\\n        \"LIBS = -L. -ltachyon $(MISCLIB) -lm -lpthread\"\n```\n\n\nNote there are two problems with this. \n\n* '-O6' is not an option for gcc. \n* There is no option to make this build 64-bit objects. \n\nThese problems should be easily solved. \n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9024\n\n",
    "created_at": "2010-05-23T22:05:30Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "title": "tachyon is buiding 32-bit on OpenSolaris x64 even when SAGE64 is set to \"yes\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9024",
    "user": "drkirkby"
}
```
Assignee: drkirkby

'tachyon' has a script called 'Make-arch' which has various architectures. But there was not one for 64-bit Solaris on x86. The code in Sage currently uses the target 'solaris-pthreads-gcc' - see below


```
if [ $UNAME = "SunOS" ]; then
    make solaris-pthreads-gcc
    finished
fi
```


That target consists of the lines:


```
solaris-pthreads-gcc:
        $(MAKE) all \
        "ARCH = solaris-pthreads-gcc" \
        "CC = gcc" \
        "CFLAGS = -Wall -O6 -fomit-frame-pointer -ffast-math -D_REENTRANT -DSunOS $(MISCFLAGS) -DTHR -DUSEPOSIXTHREADS" \
        "AR = ar" \
        "ARFLAGS = r" \
        "STRIP = strip" \
        "LIBS = -L. -ltachyon $(MISCLIB) -lm -lpthread"
```


Note there are two problems with this. 

* '-O6' is not an option for gcc. 
* There is no option to make this build 64-bit objects. 

These problems should be easily solved. 




Issue created by migration from https://trac.sagemath.org/ticket/9024





---

archive/issue_comments_083492.json:
```json
{
    "body": "The attached patch has a new target which I called 'solaris-pthreads-gcc-64-bit'\n\n\n```\nsolaris-pthreads-gcc-64-bit:\n        $(MAKE) all \\\n        \"ARCH = solaris-pthreads-gcc\" \\\n        \"CC = gcc\" \\\n        \"CFLAGS = -Wall -O4 -m64 -fomit-frame-pointer -ffast-math -D_REENTRANT -DSunOS $(MISCFLAGS) -DTHR -DUSEPOSIXTHREADS\" \\\n        \"AR = ar\" \\\n        \"ARFLAGS = r\" \\\n        \"STRIP = strip\" \\\n        \"LIBS = -L. -ltachyon $(MISCLIB) -lm -lpthread\"\n\n```\n\n\nNote the '-O6' has been changed to '-O4' and a -m64 added. The revised spkg-install then builds tachyon differently for 32 and 64-bit builds. \n\n\n```\nif [ $UNAME = \"SunOS\" ]; then\n    if [ \"x$SAGE64\" = xyes ] ; then\n       # There was nothing suitable for 64-bit mode with \n       # gcc, so I made a new target. David Kirkby, May 2010. \n       make solaris-pthreads-gcc-64-bit\n    else\n       make solaris-pthreads-gcc\n    fi\n    finished\nfi\n```\n\n\nThe new package can be found at:\n\nhttp://boxen.math.washington.edu/home/kirkby/patches/tachyon-0.98beta.p11.spkg\n\nNote:\n\nThe file patches/Make-arch.patch was a bit out of date - someone had obviously updated patches/Make-arch without changing patches/Make-arch.patch. This has now been resolved too. \n\nDave",
    "created_at": "2010-05-23T22:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9024#issuecomment-83492",
    "user": "drkirkby"
}
```

The attached patch has a new target which I called 'solaris-pthreads-gcc-64-bit'


```
solaris-pthreads-gcc-64-bit:
        $(MAKE) all \
        "ARCH = solaris-pthreads-gcc" \
        "CC = gcc" \
        "CFLAGS = -Wall -O4 -m64 -fomit-frame-pointer -ffast-math -D_REENTRANT -DSunOS $(MISCFLAGS) -DTHR -DUSEPOSIXTHREADS" \
        "AR = ar" \
        "ARFLAGS = r" \
        "STRIP = strip" \
        "LIBS = -L. -ltachyon $(MISCLIB) -lm -lpthread"

```


Note the '-O6' has been changed to '-O4' and a -m64 added. The revised spkg-install then builds tachyon differently for 32 and 64-bit builds. 


```
if [ $UNAME = "SunOS" ]; then
    if [ "x$SAGE64" = xyes ] ; then
       # There was nothing suitable for 64-bit mode with 
       # gcc, so I made a new target. David Kirkby, May 2010. 
       make solaris-pthreads-gcc-64-bit
    else
       make solaris-pthreads-gcc
    fi
    finished
fi
```


The new package can be found at:

http://boxen.math.washington.edu/home/kirkby/patches/tachyon-0.98beta.p11.spkg

Note:

The file patches/Make-arch.patch was a bit out of date - someone had obviously updated patches/Make-arch without changing patches/Make-arch.patch. This has now been resolved too. 

Dave



---

archive/issue_comments_083493.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-23T22:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9024#issuecomment-83493",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083494.json:
```json
{
    "body": "Attachment\n\nMercurial patch to allow to build 64-bit on Solaris (both SPARC and x64)",
    "created_at": "2010-05-23T22:27:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9024#issuecomment-83494",
    "user": "drkirkby"
}
```

Attachment

Mercurial patch to allow to build 64-bit on Solaris (both SPARC and x64)



---

archive/issue_comments_083495.json:
```json
{
    "body": "For other OpenSolaris issues, see #9026",
    "created_at": "2010-05-24T18:23:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9024#issuecomment-83495",
    "user": "drkirkby"
}
```

For other OpenSolaris issues, see #9026



---

archive/issue_comments_083496.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-10T15:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9024#issuecomment-83496",
    "user": "jsp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083497.json:
```json
{
    "body": "Looks ok to me on Open Solaris:\n\n\n\n```\nSuccessfully installed tachyon-0.98beta.p11\nYou can safely delete the temporary build directory\n/export/home/jaap/sage_port/sage-4.4.3/spkg/build/tachyon-0.98beta.p11\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing tachyon-0.98beta.p11.spkg\n-bash-4.0$ file local/bin/tachyon \nlocal/bin/tachyon:      ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, stripped\n-bash-4.0$ \n\n```\n\n\nAlso tested on other platforms (Fedora 32 bit and 64 bit)\n\nPositive review.\n\nJaap",
    "created_at": "2010-06-10T15:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9024#issuecomment-83497",
    "user": "jsp"
}
```

Looks ok to me on Open Solaris:



```
Successfully installed tachyon-0.98beta.p11
You can safely delete the temporary build directory
/export/home/jaap/sage_port/sage-4.4.3/spkg/build/tachyon-0.98beta.p11
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing tachyon-0.98beta.p11.spkg
-bash-4.0$ file local/bin/tachyon 
local/bin/tachyon:      ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, stripped
-bash-4.0$ 

```


Also tested on other platforms (Fedora 32 bit and 64 bit)

Positive review.

Jaap



---

archive/issue_comments_083498.json:
```json
{
    "body": "Merged http://sage.math.washington.edu/home/mhansen/tachyon-0.98beta.p11.spkg which just adds a description to the entry in SPKG.txt",
    "created_at": "2010-06-11T18:31:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9024#issuecomment-83498",
    "user": "mhansen"
}
```

Merged http://sage.math.washington.edu/home/mhansen/tachyon-0.98beta.p11.spkg which just adds a description to the entry in SPKG.txt



---

archive/issue_comments_083499.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-11T18:31:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9024#issuecomment-83499",
    "user": "mhansen"
}
```

Resolution: fixed
