# Issue 6503: remove the pyprocessing spkg from sage, then sort out any fallout that results

archive/issues_006503.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @mwhansen\n\nIn sage-4.1 we ship pyprocessing-0.52.p0.spkg, however a newer better version of that same code is standard in Python-2.6.x, which we also ship.  So we need to remove pyprocessing, do a clean build/test cycle, and see what problems arise, then sort them out. \n\nBe sure to test \"sage -tp\", which isn't tested by the test suite unless you do \"make ptest\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/6503\n\n",
    "created_at": "2009-07-09T19:01:10Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "remove the pyprocessing spkg from sage, then sort out any fallout that results",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6503",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

CC:  @mwhansen

In sage-4.1 we ship pyprocessing-0.52.p0.spkg, however a newer better version of that same code is standard in Python-2.6.x, which we also ship.  So we need to remove pyprocessing, do a clean build/test cycle, and see what problems arise, then sort them out. 

Be sure to test "sage -tp", which isn't tested by the test suite unless you do "make ptest".

Issue created by migration from https://trac.sagemath.org/ticket/6503





---

archive/issue_comments_052844.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-26T05:13:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52844",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_052845.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-01-26T05:13:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52845",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_052846.json:
```json
{
    "body": "Just delete the spkg and delete the relevant lines in spkg/standard/deps.  That should be it.",
    "created_at": "2010-01-26T05:13:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52846",
    "user": "https://github.com/williamstein"
}
```

Just delete the spkg and delete the relevant lines in spkg/standard/deps.  That should be it.



---

archive/issue_comments_052847.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-26T05:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52847",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_052848.json:
```json
{
    "body": "This might not be as easy as it seems. In my merge tree, I tried removing the pyprocessing spkg, and edited `spkg/install` and `spkg/standard/deps` to get rid of the rules relating to building pyprocessing. Based on this tree with pyprocessing removed, I cut a source tarball and parallel compile (using \"export MAKE='make -j4'\") everything from source. Trouble kicks in while compiling the Sage library. Here's a relevant snippet from the install log:\n\n```\nBuilding modified file sage/ext/interpreters/wrapper_el.pyx.\nExecute 248 commands (using 4 threads)\nTraceback (most recent call last):\n  File \"setup.py\", line 752, in <module>\n    execute_list_of_commands(queue)\n  File \"setup.py\", line 249, in execute_list_of_commands\n    execute_list_of_commands_in_parallel(command_list, nthreads)\n  File \"setup.py\", line 188, in execute_list_of_commands_in_parallel\n    from processing import Pool\nImportError: No module named processing\nsage: There was an error installing modified sage library code.\n\n\nreal    0m3.261s\nuser    0m2.540s\nsys     0m0.770s\nError building new version of SAGE.\nYou might try typing 'sage -ba' or write to sage-support with as much information as possible.\n\nreal    0m7.376s\nuser    0m5.570s\nsys     0m1.820s\nsage: An error occurred while installing sage-4.3.1.alpha0-take1\n```\n\nThe build error cannot be due to the patches or updated spkg's in my merge tree. I also tried cutting a source tarball of my merge tree (with pyprocessing intact where it is), and compile everything from source. This went OK. Removing pyrocessing would need to wait after releasing Sage 4.3.2.alpha0. I'm putting this back to \"needs work\". The likely place to look is the file `devel/sage-main/setup.py`, especially the following function:\n\n```python\ndef execute_list_of_commands_in_parallel(command_list, nthreads):\n    \"\"\"                                                                                                                                                                                                                            \n    INPUT:                                                                                                                                                                                                                         \n        command_list -- a list of pairs, consisting of a                                                                                                                                                                           \n             function to call and its argument                                                                                                                                                                                     \n        nthreads -- integer; number of threads to use                                                                                                                                                                              \n                                                                                                                                                                                                                                   \n    OUTPUT:                                                                                                                                                                                                                        \n        Executes the given list of commands, possibly in parallel,                                                                                                                                                                 \n        using nthreads threads.  Terminates setup.py with an exit code of 1                                                                                                                                                        \n        if an error occurs in any subcommand.                                                                                                                                                                                      \n                                                                                                                                                                                                                                   \n    WARNING: commands are run roughly in order, but of course successive                                                                                                                                                           \n    commands may be run at the same time.                                                                                                                                                                                          \n    \"\"\"\n    print \"Execute %s commands (using %s threads)\"%(len(command_list), min(len(command_list),nthreads))\n    from processing import Pool\n    p = Pool(nthreads)\n    for r in p.imap(apply_pair, command_list):\n        if r:\n            print \"Parallel build failed with status %s.\"%r\n            sys.exit(1)\n```\n",
    "created_at": "2010-01-26T15:29:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52848",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

This might not be as easy as it seems. In my merge tree, I tried removing the pyprocessing spkg, and edited `spkg/install` and `spkg/standard/deps` to get rid of the rules relating to building pyprocessing. Based on this tree with pyprocessing removed, I cut a source tarball and parallel compile (using "export MAKE='make -j4'") everything from source. Trouble kicks in while compiling the Sage library. Here's a relevant snippet from the install log:

```
Building modified file sage/ext/interpreters/wrapper_el.pyx.
Execute 248 commands (using 4 threads)
Traceback (most recent call last):
  File "setup.py", line 752, in <module>
    execute_list_of_commands(queue)
  File "setup.py", line 249, in execute_list_of_commands
    execute_list_of_commands_in_parallel(command_list, nthreads)
  File "setup.py", line 188, in execute_list_of_commands_in_parallel
    from processing import Pool
ImportError: No module named processing
sage: There was an error installing modified sage library code.


real    0m3.261s
user    0m2.540s
sys     0m0.770s
Error building new version of SAGE.
You might try typing 'sage -ba' or write to sage-support with as much information as possible.

real    0m7.376s
user    0m5.570s
sys     0m1.820s
sage: An error occurred while installing sage-4.3.1.alpha0-take1
```

The build error cannot be due to the patches or updated spkg's in my merge tree. I also tried cutting a source tarball of my merge tree (with pyprocessing intact where it is), and compile everything from source. This went OK. Removing pyrocessing would need to wait after releasing Sage 4.3.2.alpha0. I'm putting this back to "needs work". The likely place to look is the file `devel/sage-main/setup.py`, especially the following function:

```python
def execute_list_of_commands_in_parallel(command_list, nthreads):
    """                                                                                                                                                                                                                            
    INPUT:                                                                                                                                                                                                                         
        command_list -- a list of pairs, consisting of a                                                                                                                                                                           
             function to call and its argument                                                                                                                                                                                     
        nthreads -- integer; number of threads to use                                                                                                                                                                              
                                                                                                                                                                                                                                   
    OUTPUT:                                                                                                                                                                                                                        
        Executes the given list of commands, possibly in parallel,                                                                                                                                                                 
        using nthreads threads.  Terminates setup.py with an exit code of 1                                                                                                                                                        
        if an error occurs in any subcommand.                                                                                                                                                                                      
                                                                                                                                                                                                                                   
    WARNING: commands are run roughly in order, but of course successive                                                                                                                                                           
    commands may be run at the same time.                                                                                                                                                                                          
    """
    print "Execute %s commands (using %s threads)"%(len(command_list), min(len(command_list),nthreads))
    from processing import Pool
    p = Pool(nthreads)
    for r in p.imap(apply_pair, command_list):
        if r:
            print "Parallel build failed with status %s."%r
            sys.exit(1)
```




---

archive/issue_comments_052849.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-26T15:29:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52849",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_052850.json:
```json
{
    "body": "According to:  http://www.python.org/dev/peps/pep-0371/ there was a renaming from processing to multiprocessing. There may be other changes to the api as well.\n\nAdam",
    "created_at": "2010-01-26T15:40:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52850",
    "user": "https://github.com/maxthemouse"
}
```

According to:  http://www.python.org/dev/peps/pep-0371/ there was a renaming from processing to multiprocessing. There may be other changes to the api as well.

Adam



---

archive/issue_comments_052851.json:
```json
{
    "body": "First, we need a patch to the sage library changing any remaining imports of \"processing\" to \"multiprocessing\"; this involves changes to parallel/multiprocessing.py, plus perhaps changing the name of that file (so that in parallel/decorate.py, a line like `import multiprocessing` means import parallel/multiprocessing.py, while in parallel/multiprocessing.py, a line like `from multiprocessing import Pool` means to import the Python multiprocessing module).\n\nThe file SAGE_ROOT/devel/sage/setup.py also imports from the processing module, so that needs to be changed.\n\nAlso, as awebb suggests, the api seems to have changed: when I make these changes and run doctests on sage/parallel/, I get errors like\n\n```\nAttributeError: 'Pool' object has no attribute 'imapUnordered'\n```\n\n\nAfter making the appropriate changes, perhaps we should test everything by moving the pyprocessing files out of SAGE_ROOT/local/lib/python/site-packages/ to make sure they're not being loaded?",
    "created_at": "2010-01-26T19:37:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52851",
    "user": "https://github.com/jhpalmieri"
}
```

First, we need a patch to the sage library changing any remaining imports of "processing" to "multiprocessing"; this involves changes to parallel/multiprocessing.py, plus perhaps changing the name of that file (so that in parallel/decorate.py, a line like `import multiprocessing` means import parallel/multiprocessing.py, while in parallel/multiprocessing.py, a line like `from multiprocessing import Pool` means to import the Python multiprocessing module).

The file SAGE_ROOT/devel/sage/setup.py also imports from the processing module, so that needs to be changed.

Also, as awebb suggests, the api seems to have changed: when I make these changes and run doctests on sage/parallel/, I get errors like

```
AttributeError: 'Pool' object has no attribute 'imapUnordered'
```


After making the appropriate changes, perhaps we should test everything by moving the pyprocessing files out of SAGE_ROOT/local/lib/python/site-packages/ to make sure they're not being loaded?



---

archive/issue_comments_052852.json:
```json
{
    "body": "Oh, sage-ptest also imports `processing`.",
    "created_at": "2010-01-26T19:38:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52852",
    "user": "https://github.com/jhpalmieri"
}
```

Oh, sage-ptest also imports `processing`.



---

archive/issue_comments_052853.json:
```json
{
    "body": "patch for scripts repository",
    "created_at": "2010-01-26T19:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52853",
    "user": "https://github.com/jhpalmieri"
}
```

patch for scripts repository



---

archive/issue_comments_052854.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-26T19:57:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52854",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_052855.json:
```json
{
    "body": "Attachment [trac_6503-scripts.patch](tarball://root/attachments/some-uuid/ticket6503/trac_6503-scripts.patch) by @jhpalmieri created at 2010-01-26 19:57:35\n\nHere are two patches, one for the scripts repo and one for the main repo.  Note that one patch removes the file \"parallel/multiprocessing.py\" (actually renaming it to \"multiprocessing_sage.py\" plus the requisite changes to import statements).  When I tried to run Sage after applying this patch, I still had copies of multiprocessing.py lying around which I had to delete by hand (this won't be a problem from a build from scratch, but upgrading could problematic): I had to delete the files\n\n```\nSAGE_ROOT/devel/sage/build/lib.macosx-10.6-i386-2.6/sage/parallel/multiprocessing.py\nSAGE_ROOT/local/lib/python/site-packages/sage/parallel/multiprocessing.py\n```\n\n(Without deleting these files, commands like `import multiprocessing` in parallel/multiprocessing_sage.py imported the old Sage file `multiprocessing.py` instead of the Python module `multiprocessing`.)\n\nI haven't run a full test suite yet, but \"sage -tp 2 SAGE_ROOT/devel/sage/sage/parallel/\" passes all tests for me.",
    "created_at": "2010-01-26T19:57:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52855",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_6503-scripts.patch](tarball://root/attachments/some-uuid/ticket6503/trac_6503-scripts.patch) by @jhpalmieri created at 2010-01-26 19:57:35

Here are two patches, one for the scripts repo and one for the main repo.  Note that one patch removes the file "parallel/multiprocessing.py" (actually renaming it to "multiprocessing_sage.py" plus the requisite changes to import statements).  When I tried to run Sage after applying this patch, I still had copies of multiprocessing.py lying around which I had to delete by hand (this won't be a problem from a build from scratch, but upgrading could problematic): I had to delete the files

```
SAGE_ROOT/devel/sage/build/lib.macosx-10.6-i386-2.6/sage/parallel/multiprocessing.py
SAGE_ROOT/local/lib/python/site-packages/sage/parallel/multiprocessing.py
```

(Without deleting these files, commands like `import multiprocessing` in parallel/multiprocessing_sage.py imported the old Sage file `multiprocessing.py` instead of the Python module `multiprocessing`.)

I haven't run a full test suite yet, but "sage -tp 2 SAGE_ROOT/devel/sage/sage/parallel/" passes all tests for me.



---

archive/issue_comments_052856.json:
```json
{
    "body": "Here's another version of the patch; this one also patches SAGE_ROOT/devel/sage/spkg-install to try to delete the bad files.  I don't know if I did this right, though; please review.",
    "created_at": "2010-01-30T02:29:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52856",
    "user": "https://github.com/jhpalmieri"
}
```

Here's another version of the patch; this one also patches SAGE_ROOT/devel/sage/spkg-install to try to delete the bad files.  I don't know if I did this right, though; please review.



---

archive/issue_comments_052857.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-31T17:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52857",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_052858.json:
```json
{
    "body": "Here are the steps I took:\n\n1. Applied [trac_6503-scripts.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6503/trac_6503-scripts.patch) to the scripts repository.\n2. Applied [trac_6503-sage.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6503/trac_6503-sage.patch) to the Sage library.\n3. Removed `pyprocessing-0.52.p0.spkg` from the standard spkg repository.\n4. Removed the following lines from `spkg/install`:\n {{{\nPYPROCESSING=`$newest pyprocessing`\nexport PYPROCESSING\n }}}\n1. Changed the following line in `spkg/standard/deps`\n {{{\n      $(INST)/$(ZNPOLY) $(INST)/$(POLYTOPES_DB) $(INST)/$(PYPROCESSING) $(INST)/$(GHMM) \\\n }}}\n to this line\n {{{\n      $(INST)/$(ZNPOLY) $(INST)/$(POLYTOPES_DB) $(INST)/$(GHMM) \\\n }}}\n Removed the lines:\n {{{\n$(INST)/$(PYPROCESSING): $(BASE) $(INST)/$(PYTHON)\n        $(SAGE_SPKG) $(PYPROCESSING) 2>&1\n }}}\n Removed the line:\n {{{\n                  $(INST)/$(PYPROCESSING) \\\n }}}\n \nThe above steps were implemented against Sage 4.3.2.alpha0. Afterwards, I packaged up this version of Sage but with pyprocessing removed as per the above instructions. I then built this version of Sage from source, but received the following error:\n\n```\nbuilding 'sage.ext.interpreters.wrapper_el' extension\nTraceback (most recent call last):\n  File \"setup.py\", line 920, in <module>\n    include_dirs = include_dirs)\n  File \"/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/distutils/core.py\", line 152, in setup\n    dist.run_commands()\n  File \"/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/distutils/dist.py\", line 975, in run_commands\n    self.run_command(cmd)\n  File \"/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/distutils/dist.py\", line 995, in run_command\n    cmd_obj.run()\n  File \"/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/distutils/command/install.py\", line 577, in run\n    self.run_command('build')\n  File \"/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/distutils/cmd.py\", line 333, in run_command\n    self.distribution.run_command(command)\n  File \"/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/distutils/dist.py\", line 995, in run_command\n    cmd_obj.run()\n  File \"/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/distutils/command/build.py\", line 134, in run\n    self.run_command(cmd_name)\n  File \"/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/distutils/cmd.py\", line 333, in run_command\n    self.distribution.run_command(command)\n  File \"/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/distutils/dist.py\", line 995, in run_command\n    cmd_obj.run()\n  File \"/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/distutils/command/build_ext.py\", line 340, in run\n    self.build_extensions()\n  File \"setup.py\", line 323, in build_extensions\n    from processing import Pool\nImportError: No module named processing\nsage: There was an error installing modified sage library code.\n```\n\nI also note that the file `devel/sage-main/setup.py` has these lines:\n\n```\n            # If there were any extensions that needed to be                    \n            # rebuilt, dispatch them using pyprocessing.                        \n            if extensions_to_compile:\n               from processing import Pool\n               p = Pool(min(ncpus, len(extensions_to_compile)))\n```\n\nfrom line 320. It uses the pyprocessing spkg, when in fact this spkg has been removed as per the proposal of this ticket. Perhaps this could be a reason for the above build error I received. A fix is to change the above lines to use multiprocessing instead of processing. I'm investigating this approach, in addition to John's patches.",
    "created_at": "2010-01-31T17:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52858",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Here are the steps I took:

1. Applied [trac_6503-scripts.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6503/trac_6503-scripts.patch) to the scripts repository.
2. Applied [trac_6503-sage.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6503/trac_6503-sage.patch) to the Sage library.
3. Removed `pyprocessing-0.52.p0.spkg` from the standard spkg repository.
4. Removed the following lines from `spkg/install`:
 {{{
PYPROCESSING=`$newest pyprocessing`
export PYPROCESSING
 }}}
1. Changed the following line in `spkg/standard/deps`
 {{{
      $(INST)/$(ZNPOLY) $(INST)/$(POLYTOPES_DB) $(INST)/$(PYPROCESSING) $(INST)/$(GHMM) \
 }}}
 to this line
 {{{
      $(INST)/$(ZNPOLY) $(INST)/$(POLYTOPES_DB) $(INST)/$(GHMM) \
 }}}
 Removed the lines:
 {{{
$(INST)/$(PYPROCESSING): $(BASE) $(INST)/$(PYTHON)
        $(SAGE_SPKG) $(PYPROCESSING) 2>&1
 }}}
 Removed the line:
 {{{
                  $(INST)/$(PYPROCESSING) \
 }}}
 
The above steps were implemented against Sage 4.3.2.alpha0. Afterwards, I packaged up this version of Sage but with pyprocessing removed as per the above instructions. I then built this version of Sage from source, but received the following error:

```
building 'sage.ext.interpreters.wrapper_el' extension
Traceback (most recent call last):
  File "setup.py", line 920, in <module>
    include_dirs = include_dirs)
  File "/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/distutils/core.py", line 152, in setup
    dist.run_commands()
  File "/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/distutils/dist.py", line 975, in run_commands
    self.run_command(cmd)
  File "/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/distutils/dist.py", line 995, in run_command
    cmd_obj.run()
  File "/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/distutils/command/install.py", line 577, in run
    self.run_command('build')
  File "/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/distutils/cmd.py", line 333, in run_command
    self.distribution.run_command(command)
  File "/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/distutils/dist.py", line 995, in run_command
    cmd_obj.run()
  File "/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/distutils/command/build.py", line 134, in run
    self.run_command(cmd_name)
  File "/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/distutils/cmd.py", line 333, in run_command
    self.distribution.run_command(command)
  File "/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/distutils/dist.py", line 995, in run_command
    cmd_obj.run()
  File "/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/distutils/command/build_ext.py", line 340, in run
    self.build_extensions()
  File "setup.py", line 323, in build_extensions
    from processing import Pool
ImportError: No module named processing
sage: There was an error installing modified sage library code.
```

I also note that the file `devel/sage-main/setup.py` has these lines:

```
            # If there were any extensions that needed to be                    
            # rebuilt, dispatch them using pyprocessing.                        
            if extensions_to_compile:
               from processing import Pool
               p = Pool(min(ncpus, len(extensions_to_compile)))
```

from line 320. It uses the pyprocessing spkg, when in fact this spkg has been removed as per the proposal of this ticket. Perhaps this could be a reason for the above build error I received. A fix is to change the above lines to use multiprocessing instead of processing. I'm investigating this approach, in addition to John's patches.



---

archive/issue_comments_052859.json:
```json
{
    "body": "In the file `devel/sage-main/setup.py`, changing the following lines\n\n```\n            # If there were any extensions that needed to be                    \n            # rebuilt, dispatch them using pyprocessing.                        \n            if extensions_to_compile:\n               from processing import Pool\n               p = Pool(min(ncpus, len(extensions_to_compile)))\n```\n\nto these\n\n```\n            # If there were any extensions that needed to be                    \n            # rebuilt, dispatch them using pyprocessing.                        \n            if extensions_to_compile:\n               from multiprocessing import Pool\n               p = Pool(min(ncpus, len(extensions_to_compile)))\n```\n\nresults in the build process hanging at\n\n```\nbuilding 'sage.ext.interpreters.wrapper_el' extension\nException in thread Thread-3:\nTraceback (most recent call last):\n  File \"/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/threading.py\", line 525, in __bootstrap_inner\n    self.run()\n  File \"/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/threading.py\", line 477, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/multiprocessing/pool.py\", line 225, in _handle_tasks\n    put(task)\nPicklingError: Can't pickle <type 'instancemethod'>: attribute lookup __builtin__.instancemethod failed\n```\n",
    "created_at": "2010-01-31T19:13:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52859",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

In the file `devel/sage-main/setup.py`, changing the following lines

```
            # If there were any extensions that needed to be                    
            # rebuilt, dispatch them using pyprocessing.                        
            if extensions_to_compile:
               from processing import Pool
               p = Pool(min(ncpus, len(extensions_to_compile)))
```

to these

```
            # If there were any extensions that needed to be                    
            # rebuilt, dispatch them using pyprocessing.                        
            if extensions_to_compile:
               from multiprocessing import Pool
               p = Pool(min(ncpus, len(extensions_to_compile)))
```

results in the build process hanging at

```
building 'sage.ext.interpreters.wrapper_el' extension
Exception in thread Thread-3:
Traceback (most recent call last):
  File "/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/threading.py", line 525, in __bootstrap_inner
    self.run()
  File "/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/threading.py", line 477, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/dev/shm/mvngu/sandbox/sage-4.3.2.alpha0-8115/local/lib/python/multiprocessing/pool.py", line 225, in _handle_tasks
    put(task)
PicklingError: Can't pickle <type 'instancemethod'>: attribute lookup __builtin__.instancemethod failed
```




---

archive/issue_comments_052860.json:
```json
{
    "body": "It is interesting that doing a single-threaded build on Solaris, pyprocessing failed on Solaris after applying the patch at \n\nhttp://bugs.python.org/issue1759169 \n\nHowever, after touching \n\n\n```\n$ touch spkg/installed/pyprocessing-0.52.p0\n```\n\n\nso the Sage library built without problems on Solaris 10 (SPARC)\n\nCould it be the fact a parallel build was performed that caused the problems observed? \n\nDave",
    "created_at": "2010-02-25T15:53:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52860",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

It is interesting that doing a single-threaded build on Solaris, pyprocessing failed on Solaris after applying the patch at 

http://bugs.python.org/issue1759169 

However, after touching 


```
$ touch spkg/installed/pyprocessing-0.52.p0
```


so the Sage library built without problems on Solaris 10 (SPARC)

Could it be the fact a parallel build was performed that caused the problems observed? 

Dave



---

archive/issue_comments_052861.json:
```json
{
    "body": "For the record, I'm attaching a new version of the patch which deals with the reference to processing in setup.py -- the one that I missed in the first patch.  I don't know why mvngu's build process failed with this patch.  I may try to build it myself if I have time, but if anyone else wants to give it a try, please go ahead.",
    "created_at": "2010-02-26T15:58:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52861",
    "user": "https://github.com/jhpalmieri"
}
```

For the record, I'm attaching a new version of the patch which deals with the reference to processing in setup.py -- the one that I missed in the first patch.  I don't know why mvngu's build process failed with this patch.  I may try to build it myself if I have time, but if anyone else wants to give it a try, please go ahead.



---

archive/issue_comments_052862.json:
```json
{
    "body": "patch for Sage library",
    "created_at": "2010-02-26T15:58:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52862",
    "user": "https://github.com/jhpalmieri"
}
```

patch for Sage library



---

archive/issue_comments_052863.json:
```json
{
    "body": "Attachment [trac_6503-sage.patch](tarball://root/attachments/some-uuid/ticket6503/trac_6503-sage.patch) by @jhpalmieri created at 2010-02-26 20:32:11\n\nOkay, I took a copy of Sage, applied the attached patches and made Minh's suggested changes to install and deps, then ran `sage -sdist`.  I took the resulting tar file and tried to build it.  With MAKE defined as \"make -j2\", I ran into the same issue that Minh did.  At that point I redefined MAKE to be \"make\", and the build finished.  I'm running doctests now, but everything looks good.  In particular, `sage/sage/parallel` passes doctests.",
    "created_at": "2010-02-26T20:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52863",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_6503-sage.patch](tarball://root/attachments/some-uuid/ticket6503/trac_6503-sage.patch) by @jhpalmieri created at 2010-02-26 20:32:11

Okay, I took a copy of Sage, applied the attached patches and made Minh's suggested changes to install and deps, then ran `sage -sdist`.  I took the resulting tar file and tried to build it.  With MAKE defined as "make -j2", I ran into the same issue that Minh did.  At that point I redefined MAKE to be "make", and the build finished.  I'm running doctests now, but everything looks good.  In particular, `sage/sage/parallel` passes doctests.



---

archive/issue_comments_052864.json:
```json
{
    "body": "Note also that #8191, which already has positive review and I believe will be in the next release, needs changes to spkg/install and spkg/standard/deps. These need to be coordinated with patches. \n\nI'd love to try your fixes, but I'm not sure how to apply a patch like this to the Sage library. Perhaps if you could give me an idiots buide to how to do this with Mercurial, I'll try it. \n\nDave",
    "created_at": "2010-02-26T23:58:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52864",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Note also that #8191, which already has positive review and I believe will be in the next release, needs changes to spkg/install and spkg/standard/deps. These need to be coordinated with patches. 

I'd love to try your fixes, but I'm not sure how to apply a patch like this to the Sage library. Perhaps if you could give me an idiots buide to how to do this with Mercurial, I'll try it. 

Dave



---

archive/issue_comments_052865.json:
```json
{
    "body": "The simplest way to see the bug that Minh reported is as follows:\n\n- apply trac_6503-sage.patch\n- export MAKE='make -j2'  (to do a parallel build)\n- touch a cython file in the Sage library\n- sage -b\n\nYou should get the pickling error he described above.",
    "created_at": "2010-02-27T00:03:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52865",
    "user": "https://github.com/jhpalmieri"
}
```

The simplest way to see the bug that Minh reported is as follows:

- apply trac_6503-sage.patch
- export MAKE='make -j2'  (to do a parallel build)
- touch a cython file in the Sage library
- sage -b

You should get the pickling error he described above.



---

archive/issue_comments_052866.json:
```json
{
    "body": "Replying to [comment:14 drkirkby]:\n> Note also that #8191, which already has positive review and I believe will be in the next release, needs changes to spkg/install and spkg/standard/deps. These need to be coordinated with patches. \n> \n> I'd love to try your fixes, but I'm not sure how to apply a patch like this to the Sage library. Perhaps if you could give me an idiots buide to how to do this with Mercurial, I'll try it. \n\nIn my opinion, Mercurial queues are the easiest way to do these things.  Have a look at the quick startup guide at:\n\nhttp://wiki.sagemath.org/MercurialQueues",
    "created_at": "2010-02-27T04:14:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52866",
    "user": "https://github.com/aghitza"
}
```

Replying to [comment:14 drkirkby]:
> Note also that #8191, which already has positive review and I believe will be in the next release, needs changes to spkg/install and spkg/standard/deps. These need to be coordinated with patches. 
> 
> I'd love to try your fixes, but I'm not sure how to apply a patch like this to the Sage library. Perhaps if you could give me an idiots buide to how to do this with Mercurial, I'll try it. 

In my opinion, Mercurial queues are the easiest way to do these things.  Have a look at the quick startup guide at:

http://wiki.sagemath.org/MercurialQueues



---

archive/issue_comments_052867.json:
```json
{
    "body": "Attachment [trac_6503-fix.patch](tarball://root/attachments/some-uuid/ticket6503/trac_6503-fix.patch) by @mwhansen created at 2010-02-27 20:12:36",
    "created_at": "2010-02-27T20:12:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52867",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_6503-fix.patch](tarball://root/attachments/some-uuid/ticket6503/trac_6503-fix.patch) by @mwhansen created at 2010-02-27 20:12:36



---

archive/issue_comments_052868.json:
```json
{
    "body": "I've added a patch on top of trac_6503-sage.patch which fixes the issue with pickling the instancemethods when building the Sage library in parallel with multiprocessing.",
    "created_at": "2010-02-27T20:13:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52868",
    "user": "https://github.com/mwhansen"
}
```

I've added a patch on top of trac_6503-sage.patch which fixes the issue with pickling the instancemethods when building the Sage library in parallel with multiprocessing.



---

archive/issue_comments_052869.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-27T20:13:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52869",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_052870.json:
```json
{
    "body": "mhansen's patch works for me.  Since I wrote the original patch, I can't give the whole thing a positive review.  I'll positively review mhansen's patch, though, and mvngu's instructions [above](http://trac.sagemath.org/sage_trac/ticket/6503#comment:9), items 3-5 in particular (patching spkg/install and spkg/standard/deps, and removing pyprocessing...spkg).\n\nI'm attaching complete versions of the modified versions of install and deps, for completeness.",
    "created_at": "2010-03-01T23:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52870",
    "user": "https://github.com/jhpalmieri"
}
```

mhansen's patch works for me.  Since I wrote the original patch, I can't give the whole thing a positive review.  I'll positively review mhansen's patch, though, and mvngu's instructions [above](http://trac.sagemath.org/sage_trac/ticket/6503#comment:9), items 3-5 in particular (patching spkg/install and spkg/standard/deps, and removing pyprocessing...spkg).

I'm attaching complete versions of the modified versions of install and deps, for completeness.



---

archive/issue_comments_052871.json:
```json
{
    "body": "The file \"install\" here needs to be rebased on top of that at #8191. The latter adds the new iconv spkg. In doing so, it modifies \"install\". Simiarly, the file \"deps\" on the current ticket needs to be rebased on top of that at #8191.",
    "created_at": "2010-03-02T19:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52871",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The file "install" here needs to be rebased on top of that at #8191. The latter adds the new iconv spkg. In doing so, it modifies "install". Simiarly, the file "deps" on the current ticket needs to be rebased on top of that at #8191.



---

archive/issue_comments_052872.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-02T19:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52872",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_052873.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-02T20:13:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52873",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_052874.json:
```json
{
    "body": "Given that neither #8191 nor this ticket has a positive review, I'm not sure why this one in particular needs rebasing.  But here you go.",
    "created_at": "2010-03-02T20:13:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52874",
    "user": "https://github.com/jhpalmieri"
}
```

Given that neither #8191 nor this ticket has a positive review, I'm not sure why this one in particular needs rebasing.  But here you go.



---

archive/issue_comments_052875.json:
```json
{
    "body": "rebased against #8191",
    "created_at": "2010-03-02T20:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52875",
    "user": "https://github.com/jhpalmieri"
}
```

rebased against #8191



---

archive/issue_comments_052876.json:
```json
{
    "body": "Attachment [install](tarball://root/attachments/some-uuid/ticket6503/install) by @jhpalmieri created at 2010-03-02 20:14:39\n\nrebased against #8191",
    "created_at": "2010-03-02T20:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52876",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [install](tarball://root/attachments/some-uuid/ticket6503/install) by @jhpalmieri created at 2010-03-02 20:14:39

rebased against #8191



---

archive/issue_comments_052877.json:
```json
{
    "body": "rebased against #8191",
    "created_at": "2010-03-02T20:14:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52877",
    "user": "https://github.com/jhpalmieri"
}
```

rebased against #8191



---

archive/issue_comments_052878.json:
```json
{
    "body": "Attachment [deps](tarball://root/attachments/some-uuid/ticket6503/deps) by @jhpalmieri created at 2010-03-02 20:14:58",
    "created_at": "2010-03-02T20:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52878",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [deps](tarball://root/attachments/some-uuid/ticket6503/deps) by @jhpalmieri created at 2010-03-02 20:14:58



---

archive/issue_comments_052879.json:
```json
{
    "body": "Attachment [install.diff](tarball://root/attachments/some-uuid/ticket6503/install.diff) by @jhpalmieri created at 2010-03-02 20:15:06",
    "created_at": "2010-03-02T20:15:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52879",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [install.diff](tarball://root/attachments/some-uuid/ticket6503/install.diff) by @jhpalmieri created at 2010-03-02 20:15:06



---

archive/issue_comments_052880.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-03T01:42:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52880",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_052881.json:
```json
{
    "body": "Hurray! Parallel build works and parallel doctesting works also. I often use the following little script to parallel build and doctest after the build is done:\n\n```sh\n#!/bin/sh\nexport DOT_SAGE=/dev/shm/mvngu/dot_sage/<x.y.z>\nexport MAKE='make -j6'\nmake\nmake ptestlong\n```\n\nThis script first requires that I edit the following line in `makefile`\n\n```\nNUM_THREADS=0 # 0 interpreted as min(8, multiprocessing.cpu_count())\n```\n\nto result in \n\n```\nNUM_THREADS=8 # 0 interpreted as min(8, multiprocessing.cpu_count())\n```\n\nI also attempted parallel doctest with\n\n```\n./sage -tp 12 -long devel/sage-main/\n```\n\nAs far as the parallel compilation and parallel doctesting of Sage is concerned, they went OK without pyprocessing. Now is the time to remove pyprocessing and instead use the Python library module `multiprocessing`. A big thank you to John and Mike for the hard work!",
    "created_at": "2010-03-03T01:42:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52881",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Hurray! Parallel build works and parallel doctesting works also. I often use the following little script to parallel build and doctest after the build is done:

```sh
#!/bin/sh
export DOT_SAGE=/dev/shm/mvngu/dot_sage/<x.y.z>
export MAKE='make -j6'
make
make ptestlong
```

This script first requires that I edit the following line in `makefile`

```
NUM_THREADS=0 # 0 interpreted as min(8, multiprocessing.cpu_count())
```

to result in 

```
NUM_THREADS=8 # 0 interpreted as min(8, multiprocessing.cpu_count())
```

I also attempted parallel doctest with

```
./sage -tp 12 -long devel/sage-main/
```

As far as the parallel compilation and parallel doctesting of Sage is concerned, they went OK without pyprocessing. Now is the time to remove pyprocessing and instead use the Python library module `multiprocessing`. A big thank you to John and Mike for the hard work!



---

archive/issue_comments_052882.json:
```json
{
    "body": "Merged in this order:\n\n1. Removed `SAGE_ROOT/spkg/standard/pyprocessing-0.52.p0.spkg`.\n2. Replaced the file `SAGE_ROOT/spkg/install` with [install](http://trac.sagemath.org/sage_trac/attachment/ticket/6503/install).\n3. Replaced the file `SAGE_ROOT/spkg/standard/deps` with [deps](http://trac.sagemath.org/sage_trac/attachment/ticket/6503/deps).\n4. Merged [trac_6503-scripts.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6503/trac_6503-scripts.patch) in the scripts repository.\n5. Merged [trac_6503-sage.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6503/trac_6503-sage.patch) in the Sage library.\n6. Merged [trac_6503-fix.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6503/trac_6503-fix.patch) in the Sage library.",
    "created_at": "2010-03-03T01:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52882",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged in this order:

1. Removed `SAGE_ROOT/spkg/standard/pyprocessing-0.52.p0.spkg`.
2. Replaced the file `SAGE_ROOT/spkg/install` with [install](http://trac.sagemath.org/sage_trac/attachment/ticket/6503/install).
3. Replaced the file `SAGE_ROOT/spkg/standard/deps` with [deps](http://trac.sagemath.org/sage_trac/attachment/ticket/6503/deps).
4. Merged [trac_6503-scripts.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6503/trac_6503-scripts.patch) in the scripts repository.
5. Merged [trac_6503-sage.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6503/trac_6503-sage.patch) in the Sage library.
6. Merged [trac_6503-fix.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6503/trac_6503-fix.patch) in the Sage library.



---

archive/issue_comments_052883.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-03T01:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6503#issuecomment-52883",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
