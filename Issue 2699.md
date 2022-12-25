# Issue 2699: scipy fails to build

archive/issues_002699.json:
```json
{
    "body": "Assignee: mabshoff\n\ndoing a `make` in a fresh install of 2.10.4:\n\nsystem is linux, kubuntu 6.06 LTS\n\n\n```\ncreating build/temp.linux-i686-2.5/scipy/sparse\ncreating build/temp.linux-i686-2.5/scipy/sparse/sparsetools\ncompile options: '-Iscipy/sparse/sparsetools -I/local/scratch/schilly/sage/local/lib/python2.5/site-packages/numpy/core/include -I/local/scratch/schilly/sage/local/include/python2.5 -c'\ng++: scipy/sparse/sparsetools/sparsetools_wrap.cxx\ng++ gcc -pthread -shared build/temp.linux-i686-2.5/scipy/sparse/sparsetools/sparsetools_wrap.o -Lbuild/temp.linux-i686-2.5 -o build/lib.linux-i686-2.5/scipy/sparse/_sparsetools.so\ng++: gcc: No such file or directory\ng++: gcc: No such file or directory\nerror: Command \"g++ gcc -pthread -shared build/temp.linux-i686-2.5/scipy/sparse/sparsetools/sparsetools_wrap.o -Lbuild/temp.linux-i686-2.5 -o build/lib.linux-i686-2.5/scipy/sparse/_sparsetools.so\" failed with exit status 1\nError building scipy.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2699\n\n",
    "created_at": "2008-03-28T14:07:06Z",
    "labels": [
        "component: build",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "scipy fails to build",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2699",
    "user": "https://github.com/haraldschilly"
}
```
Assignee: mabshoff

doing a `make` in a fresh install of 2.10.4:

system is linux, kubuntu 6.06 LTS


```
creating build/temp.linux-i686-2.5/scipy/sparse
creating build/temp.linux-i686-2.5/scipy/sparse/sparsetools
compile options: '-Iscipy/sparse/sparsetools -I/local/scratch/schilly/sage/local/lib/python2.5/site-packages/numpy/core/include -I/local/scratch/schilly/sage/local/include/python2.5 -c'
g++: scipy/sparse/sparsetools/sparsetools_wrap.cxx
g++ gcc -pthread -shared build/temp.linux-i686-2.5/scipy/sparse/sparsetools/sparsetools_wrap.o -Lbuild/temp.linux-i686-2.5 -o build/lib.linux-i686-2.5/scipy/sparse/_sparsetools.so
g++: gcc: No such file or directory
g++: gcc: No such file or directory
error: Command "g++ gcc -pthread -shared build/temp.linux-i686-2.5/scipy/sparse/sparsetools/sparsetools_wrap.o -Lbuild/temp.linux-i686-2.5 -o build/lib.linux-i686-2.5/scipy/sparse/_sparsetools.so" failed with exit status 1
Error building scipy.
```


Issue created by migration from https://trac.sagemath.org/ticket/2699





---

archive/issue_comments_018577.json:
```json
{
    "body": "Attachment [install.log.tar.tar.bz2](tarball://root/attachments/some-uuid/ticket2699/install.log.tar.tar.bz2) by @haraldschilly created at 2008-03-28 14:10:02\n\ninstall.log of failed scipy build",
    "created_at": "2008-03-28T14:10:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2699#issuecomment-18577",
    "user": "https://github.com/haraldschilly"
}
```

Attachment [install.log.tar.tar.bz2](tarball://root/attachments/some-uuid/ticket2699/install.log.tar.tar.bz2) by @haraldschilly created at 2008-03-28 14:10:02

install.log of failed scipy build



---

archive/issue_comments_018578.json:
```json
{
    "body": "What is CC and CXX set to? This looks very fishy and is likely not the fault of Sage. Please report build issues to sage-devel and so not open ticket until it is clear if there is actually a bug in Sage.\n\nAlso:\n* please provide the complete install.log\n* do not attach compressed files to trac since those tend to cause problems\n\nCheers,\n\nMichael",
    "created_at": "2008-03-28T15:06:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2699#issuecomment-18578",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

What is CC and CXX set to? This looks very fishy and is likely not the fault of Sage. Please report build issues to sage-devel and so not open ticket until it is clear if there is actually a bug in Sage.

Also:
* please provide the complete install.log
* do not attach compressed files to trac since those tend to cause problems

Cheers,

Michael



---

archive/issue_comments_018579.json:
```json
{
    "body": "Replying to [comment:1 mabshoff]:\n> What is CC and CXX set to? \n\nsystemwide they are not set, in the -sh environment\n\n\n```\n$ ./sage -sh\n\nStarting subshell with Sage environment variables set.\nBe sure to exit when you are done and do not do anything\nwith other copies of Sage!\n\n\n$/local/scratch/schilly/sage$ echo $CC\ngcc\n$/local/scratch/schilly/sage$ echo $CXX\ng++\n```\n\n\n> This looks very fishy and is likely not the fault of Sage. Please report build issues to \n> sage-devel and so not open ticket until it is clear if there is actually a bug in Sage.\n\nwell, it looks like a scipy issue...\n\n> Also:\n>  * please provide the complete install.log\n>  * do not attach compressed files to trac since those tend to cause problems\n\nit was too big so i compressed it",
    "created_at": "2008-03-28T15:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2699#issuecomment-18579",
    "user": "https://github.com/haraldschilly"
}
```

Replying to [comment:1 mabshoff]:
> What is CC and CXX set to? 

systemwide they are not set, in the -sh environment


```
$ ./sage -sh

Starting subshell with Sage environment variables set.
Be sure to exit when you are done and do not do anything
with other copies of Sage!


$/local/scratch/schilly/sage$ echo $CC
gcc
$/local/scratch/schilly/sage$ echo $CXX
g++
```


> This looks very fishy and is likely not the fault of Sage. Please report build issues to 
> sage-devel and so not open ticket until it is clear if there is actually a bug in Sage.

well, it looks like a scipy issue...

> Also:
>  * please provide the complete install.log
>  * do not attach compressed files to trac since those tend to cause problems

it was too big so i compressed it



---

archive/issue_comments_018580.json:
```json
{
    "body": "Replying to [comment:2 schilly]:\n> Replying to [comment:1 mabshoff]:\n> > What is CC and CXX set to? \n> \n> systemwide they are not set, in the -sh environment\n> \n> {{{\n> $ ./sage -sh\n> \n> Starting subshell with Sage environment variables set.\n> Be sure to exit when you are done and do not do anything\n> with other copies of Sage!\n> \n\nOk.\n\n> $/local/scratch/schilly/sage$ echo $CC\n> gcc\n> $/local/scratch/schilly/sage$ echo $CXX\n> g++\n> }}}\n\nThat looks perfectly fine. I assume you are not using distcc?\n\n> > This looks very fishy and is likely not the fault of Sage. Please report build issues to \n> > sage-devel and so not open ticket until it is clear if there is actually a bug in Sage.\n> \n> well, it looks like a scipy issue...\n\nSure, but now we are poking around here while it should happen on sage-devel :)\n\n> > Also:\n> >  * please provide the complete install.log\n> >  * do not attach compressed files to trac since those tend to cause problems\n> \n> it was too big so i compressed it\n\nYep, the recommended thing to do: gzip install.log and post a link to it where it can be downloaded. I would still like to see the complete install.log. g++ somehow seems to be screwed up and I am sure that somebody did build on LTS. So if this is a general problem I am surprised it never popped up. matplotlib is build before scipy and that uses a C++ compiler. But it uses cc1plus, so can you check if g++ works as expected?\n\nCheers,\n\nMichael",
    "created_at": "2008-03-28T15:50:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2699#issuecomment-18580",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:2 schilly]:
> Replying to [comment:1 mabshoff]:
> > What is CC and CXX set to? 
> 
> systemwide they are not set, in the -sh environment
> 
> {{{
> $ ./sage -sh
> 
> Starting subshell with Sage environment variables set.
> Be sure to exit when you are done and do not do anything
> with other copies of Sage!
> 

Ok.

> $/local/scratch/schilly/sage$ echo $CC
> gcc
> $/local/scratch/schilly/sage$ echo $CXX
> g++
> }}}

That looks perfectly fine. I assume you are not using distcc?

> > This looks very fishy and is likely not the fault of Sage. Please report build issues to 
> > sage-devel and so not open ticket until it is clear if there is actually a bug in Sage.
> 
> well, it looks like a scipy issue...

Sure, but now we are poking around here while it should happen on sage-devel :)

> > Also:
> >  * please provide the complete install.log
> >  * do not attach compressed files to trac since those tend to cause problems
> 
> it was too big so i compressed it

Yep, the recommended thing to do: gzip install.log and post a link to it where it can be downloaded. I would still like to see the complete install.log. g++ somehow seems to be screwed up and I am sure that somebody did build on LTS. So if this is a general problem I am surprised it never popped up. matplotlib is build before scipy and that uses a C++ compiler. But it uses cc1plus, so can you check if g++ works as expected?

Cheers,

Michael



---

archive/issue_comments_018581.json:
```json
{
    "body": "Matplotlib also fails to build [at least the C++ bits - with the same issue, i.e. invoking \"g++ gcc ...]. Even after exporting LANG=C the problem still happens. In this case  LANG is set to de_AT.UTF-8.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-28T16:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2699#issuecomment-18581",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Matplotlib also fails to build [at least the C++ bits - with the same issue, i.e. invoking "g++ gcc ...]. Even after exporting LANG=C the problem still happens. In this case  LANG is set to de_AT.UTF-8.

Cheers,

Michael



---

archive/issue_comments_018582.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-12T18:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2699#issuecomment-18582",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002889.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-05-12T18:53:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2699",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2699#event-2889"
}
```



---

archive/issue_comments_018583.json:
```json
{
    "body": "\n```\n[20:06] <mabshoff> schilly: is #2699 still an issue for you?\n[20:06] <mabshoff> I have been unable to hit it on 6.06 LTS and also 8.04 LTS.\n[20:06] <schilly> err ... let me see\n[20:09] <schilly> mabshoff: close it, if it happens again i'll open another ticket. i think this was simply solved by the next version after 2.10. or something like that\n```\n",
    "created_at": "2008-05-12T18:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2699#issuecomment-18583",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```


```
[20:06] <mabshoff> schilly: is #2699 still an issue for you?
[20:06] <mabshoff> I have been unable to hit it on 6.06 LTS and also 8.04 LTS.
[20:06] <schilly> err ... let me see
[20:09] <schilly> mabshoff: close it, if it happens again i'll open another ticket. i think this was simply solved by the next version after 2.10. or something like that
```

