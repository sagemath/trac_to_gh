# Issue 3765: make it so "sage -br" does the cythonization in parallel using pyprocessing

archive/issues_003765.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis would be just a few lines of code to implement and would make doing \"sage -br\" much faster. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3765\n\n",
    "created_at": "2008-08-03T18:26:24Z",
    "labels": [
        "build",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "make it so \"sage -br\" does the cythonization in parallel using pyprocessing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3765",
    "user": "@williamstein"
}
```
Assignee: @williamstein

This would be just a few lines of code to implement and would make doing "sage -br" much faster. 

Issue created by migration from https://trac.sagemath.org/ticket/3765





---

archive/issue_comments_026773.json:
```json
{
    "body": "I also experimented with ideas for making the gcc part of the build fast.  Here's some code.  This is *not* in this patch and should not be part of this ticket:\n\n\n```\nimport distutils.spawn\ndistutils_spawn = distutils.spawn.spawn\ncommand_list = []\ndef my_spawn(cmd,search_path=1,verbose=0,dry_run=0):\n    command_list.append(' '.join(cmd))\ndistutils.spawn.spawn = my_spawn\ncode = setup(dry_run=True,\n             ext_modules = ext_modules, include_dirs = include_dirs,\n             packages=packages, scripts=scripts, data_files=data_files)\nexecute_list_of_commands(command_list)\n\ndistutils.spawn.spawn = distutils.spawn\n\nsetup(name        = 'sage', \n      version     =  SAGE_VERSION,\n      description = 'Sage: Open Source Mathematics Software',\n      license     = 'GNU Public License (GPL)',\n      author      = 'William Stein et al.',\n      author_email= 'http://groups.google.com/group/sage-support',\n      url         = 'http://www.sagemath.org',\n      ext_modules = ext_modules, include_dirs = include_dirs,\n      packages=packages, scripts=scripts, data_files=data_files)\n```\n\n\nHere I separated out the packages, scripts, and data_files list.\n\nThe above doesn't work because distutils copies all the .o files over to the build/lib-* directory so none of the gcc link commands above work.   Also, doing the dry run seems to make the non dry run\nwork differently -- probably the Extension objects are modified.",
    "created_at": "2008-08-03T21:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3765#issuecomment-26773",
    "user": "@williamstein"
}
```

I also experimented with ideas for making the gcc part of the build fast.  Here's some code.  This is *not* in this patch and should not be part of this ticket:


```
import distutils.spawn
distutils_spawn = distutils.spawn.spawn
command_list = []
def my_spawn(cmd,search_path=1,verbose=0,dry_run=0):
    command_list.append(' '.join(cmd))
distutils.spawn.spawn = my_spawn
code = setup(dry_run=True,
             ext_modules = ext_modules, include_dirs = include_dirs,
             packages=packages, scripts=scripts, data_files=data_files)
execute_list_of_commands(command_list)

distutils.spawn.spawn = distutils.spawn

setup(name        = 'sage', 
      version     =  SAGE_VERSION,
      description = 'Sage: Open Source Mathematics Software',
      license     = 'GNU Public License (GPL)',
      author      = 'William Stein et al.',
      author_email= 'http://groups.google.com/group/sage-support',
      url         = 'http://www.sagemath.org',
      ext_modules = ext_modules, include_dirs = include_dirs,
      packages=packages, scripts=scripts, data_files=data_files)
```


Here I separated out the packages, scripts, and data_files list.

The above doesn't work because distutils copies all the .o files over to the build/lib-* directory so none of the gcc link commands above work.   Also, doing the dry run seems to make the non dry run
work differently -- probably the Extension objects are modified.



---

archive/issue_comments_026774.json:
```json
{
    "body": "Wasn't this the point of pbuild?",
    "created_at": "2008-08-03T22:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3765#issuecomment-26774",
    "user": "@garyfurnish"
}
```

Wasn't this the point of pbuild?



---

archive/issue_comments_026775.json:
```json
{
    "body": "I tried this out, and it worked perfectly.  A few comments:\n\n1) Don't we already have a function for CPU detection that execute_list_of_commands should use?\n\n2) There are no doctests for any of the new functions.",
    "created_at": "2008-08-04T09:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3765#issuecomment-26775",
    "user": "@mwhansen"
}
```

I tried this out, and it worked perfectly.  A few comments:

1) Don't we already have a function for CPU detection that execute_list_of_commands should use?

2) There are no doctests for any of the new functions.



---

archive/issue_comments_026776.json:
```json
{
    "body": "> I tried this out, and it worked perfectly. A few comments:\n\n> 1) Don't we already have a function for CPU detection that execute_list_of_commands should use?\n\nI copied those 4 lines of code into setup.py, since this is a chicken and egg problem.  You can't call sage library code from setup.py, since setup.py is run to install the sage library.   It's only about four lines of code anyways.\n\n> 2) There are no doctests for any of the new functions.\n\nUnfortunately it is impossible to doctest setup.py since the act of importing setup.py would cause the distutils stuff to get run.    Also setup.py isn't part of the sage library, so it's functions aren't available elsewhere.\n\nThat said, it might make sense to separate as much code as possible out of setup.py into a separate module that is not part of the sage library.  I think such refactoring should be in another ticket though.",
    "created_at": "2008-08-05T05:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3765#issuecomment-26776",
    "user": "@williamstein"
}
```

> I tried this out, and it worked perfectly. A few comments:

> 1) Don't we already have a function for CPU detection that execute_list_of_commands should use?

I copied those 4 lines of code into setup.py, since this is a chicken and egg problem.  You can't call sage library code from setup.py, since setup.py is run to install the sage library.   It's only about four lines of code anyways.

> 2) There are no doctests for any of the new functions.

Unfortunately it is impossible to doctest setup.py since the act of importing setup.py would cause the distutils stuff to get run.    Also setup.py isn't part of the sage library, so it's functions aren't available elsewhere.

That said, it might make sense to separate as much code as possible out of setup.py into a separate module that is not part of the sage library.  I think such refactoring should be in another ticket though.



---

archive/issue_comments_026777.json:
```json
{
    "body": "Comments seem reasonable to me.  Positive review",
    "created_at": "2008-08-05T09:51:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3765#issuecomment-26777",
    "user": "@mwhansen"
}
```

Comments seem reasonable to me.  Positive review



---

archive/issue_comments_026778.json:
```json
{
    "body": "Should we not check some env variable (SAGE_THREADS ?) before just assuming we want to use all CPUs simultaneously? Imagine two or three people on sage.math building in parallel ...\n\nCheers,\n\nMichael",
    "created_at": "2008-08-06T00:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3765#issuecomment-26778",
    "user": "mabshoff"
}
```

Should we not check some env variable (SAGE_THREADS ?) before just assuming we want to use all CPUs simultaneously? Imagine two or three people on sage.math building in parallel ...

Cheers,

Michael



---

archive/issue_comments_026779.json:
```json
{
    "body": "Checking SAGE_THREADS seems like a good idea especially if that environment variable is used elsewhere.  What would a good default for it be? 2?  Would a user have to edit sage-env if they wanted to say always use 4 threads on their machine?",
    "created_at": "2008-08-06T19:48:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3765#issuecomment-26779",
    "user": "@mwhansen"
}
```

Checking SAGE_THREADS seems like a good idea especially if that environment variable is used elsewhere.  What would a good default for it be? 2?  Would a user have to edit sage-env if they wanted to say always use 4 threads on their machine?



---

archive/issue_comments_026780.json:
```json
{
    "body": "We need to make the Sage library depend on PyProcessing since otherwise this will blow up for a fresh build.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-08T22:43:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3765#issuecomment-26780",
    "user": "mabshoff"
}
```

We need to make the Sage library depend on PyProcessing since otherwise this will blow up for a fresh build.

Cheers,

Michael



---

archive/issue_comments_026781.json:
```json
{
    "body": "What's the status of it? It has a positive review but the comments read like \"needs work\"",
    "created_at": "2008-09-07T13:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3765#issuecomment-26781",
    "user": "@malb"
}
```

What's the status of it? It has a positive review but the comments read like "needs work"



---

archive/issue_comments_026782.json:
```json
{
    "body": "Replying to [comment:10 malb]:\n> What's the status of it? It has a positive review but the comments read like \"needs work\"\n\nYes, it does. That is the reason it has not been merged yet :)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-07T14:25:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3765#issuecomment-26782",
    "user": "mabshoff"
}
```

Replying to [comment:10 malb]:
> What's the status of it? It has a positive review but the comments read like "needs work"

Yes, it does. That is the reason it has not been merged yet :)

Cheers,

Michael



---

archive/issue_comments_026783.json:
```json
{
    "body": "\n```\nFrom mabshoff:\n\nYeah, the above was the one thing about the patch that really bothered\nme since on sage.math the old version would just grab 16 cores\nregardless of the load for example. Using -br #n works for me.\n\nI am not sure if if I mentioned this on the ticket, but in that case\nwe should make the Sage library depend on pyprocessing and also use\nsome env variable to pass the number of threads to the build process\nwhen building the Sage library for the first time.\n```\n\n\nResponses: good.  Yes, we would definitely have to change spkg/standard/deps to\ndepend on PYPROCESSING, and that will be part of this ticket.  I've attached\na new deps file that does this (note -- deps isn't under any repo, and the \nattached file is from 3.1.2). \n\nAnother option can be to parse the environment variable MAKE and if it has\na -j option, then use that.  This will make it so our current standard \n\n```\nexport MAKE=\"make -j4\"\nmake\n```\n\nworks and does at least the cythoning in parallel.\n\nWilliam",
    "created_at": "2008-09-22T04:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3765#issuecomment-26783",
    "user": "@williamstein"
}
```


```
From mabshoff:

Yeah, the above was the one thing about the patch that really bothered
me since on sage.math the old version would just grab 16 cores
regardless of the load for example. Using -br #n works for me.

I am not sure if if I mentioned this on the ticket, but in that case
we should make the Sage library depend on pyprocessing and also use
some env variable to pass the number of threads to the build process
when building the Sage library for the first time.
```


Responses: good.  Yes, we would definitely have to change spkg/standard/deps to
depend on PYPROCESSING, and that will be part of this ticket.  I've attached
a new deps file that does this (note -- deps isn't under any repo, and the 
attached file is from 3.1.2). 

Another option can be to parse the environment variable MAKE and if it has
a -j option, then use that.  This will make it so our current standard 

```
export MAKE="make -j4"
make
```

works and does at least the cythoning in parallel.

William



---

archive/issue_comments_026784.json:
```json
{
    "body": "Attachment [deps](tarball://root/attachments/some-uuid/ticket3765/deps) by @williamstein created at 2008-09-22 04:54:43",
    "created_at": "2008-09-22T04:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3765#issuecomment-26784",
    "user": "@williamstein"
}
```

Attachment [deps](tarball://root/attachments/some-uuid/ticket3765/deps) by @williamstein created at 2008-09-22 04:54:43



---

archive/issue_comments_026785.json:
```json
{
    "body": "I have modified this code so that now it does nothing unless the environment variable MAKE is set and include \"-j[number]\" in it.  If it is set, then it does the cython'ing on the pyx files using number cores. \n\nAs an example test, if you touch *.pyx in devel/sage/matrix, then do this on sage.math\n\n```\nexport MAKE=\"make -j20\"; sage -br\n```\n\n\nYou get \n\n```\n...\nTime to execute 28 commands: 43.5897231102 seconds\n```\n\n\nThis would take far longer than 43 seconds in serial.\n\nNote that the gcc'ing part is still done in serial. \n\nThis is an incredibly simple patch that will save a lot of time, and is quite non-intrusive and natural, I think.\n\nWilliam",
    "created_at": "2008-10-23T20:48:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3765#issuecomment-26785",
    "user": "@williamstein"
}
```

I have modified this code so that now it does nothing unless the environment variable MAKE is set and include "-j[number]" in it.  If it is set, then it does the cython'ing on the pyx files using number cores. 

As an example test, if you touch *.pyx in devel/sage/matrix, then do this on sage.math

```
export MAKE="make -j20"; sage -br
```


You get 

```
...
Time to execute 28 commands: 43.5897231102 seconds
```


This would take far longer than 43 seconds in serial.

Note that the gcc'ing part is still done in serial. 

This is an incredibly simple patch that will save a lot of time, and is quite non-intrusive and natural, I think.

William



---

archive/issue_comments_026786.json:
```json
{
    "body": "this is rebased against sage-3.2.alpha0 and uses an environment variable MAKE",
    "created_at": "2008-10-23T20:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3765#issuecomment-26786",
    "user": "@williamstein"
}
```

this is rebased against sage-3.2.alpha0 and uses an environment variable MAKE



---

archive/issue_comments_026787.json:
```json
{
    "body": "Attachment [sage-3765.patch](tarball://root/attachments/some-uuid/ticket3765/sage-3765.patch) by mabshoff created at 2008-10-26 18:11:52\n\nLooks good to me. I will fix deps so that the Sage libraru depends on pyprocessing.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-26T18:11:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3765#issuecomment-26787",
    "user": "mabshoff"
}
```

Attachment [sage-3765.patch](tarball://root/attachments/some-uuid/ticket3765/sage-3765.patch) by mabshoff created at 2008-10-26 18:11:52

Looks good to me. I will fix deps so that the Sage libraru depends on pyprocessing.

Cheers,

Michael



---

archive/issue_comments_026788.json:
```json
{
    "body": "Merged in Sage 3.2.alpha1",
    "created_at": "2008-10-27T02:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3765#issuecomment-26788",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha1



---

archive/issue_comments_026789.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-27T02:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3765#issuecomment-26789",
    "user": "mabshoff"
}
```

Resolution: fixed
