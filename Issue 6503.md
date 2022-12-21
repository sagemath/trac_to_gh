# Issue 6503: remove the pyprocessing spkg from sage, then sort out any fallout that results

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-07-09 19:01:10

Assignee: mabshoff

CC:  mhansen

In sage-4.1 we ship pyprocessing-0.52.p0.spkg, however a newer better version of that same code is standard in Python-2.6.x, which we also ship.  So we need to remove pyprocessing, do a clean build/test cycle, and see what problems arise, then sort them out. 

Be sure to test "sage -tp", which isn't tested by the test suite unless you do "make ptest".


---

Comment by was created at 2010-01-26 05:13:55

Changing status from new to needs_review.


---

Comment by was created at 2010-01-26 05:13:55

Changing priority from major to blocker.


---

Comment by was created at 2010-01-26 05:13:55

Just delete the spkg and delete the relevant lines in spkg/standard/deps.  That should be it.


---

Comment by was created at 2010-01-26 05:14:06

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-26 15:29:52

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

Comment by mvngu created at 2010-01-26 15:29:52

Changing status from positive_review to needs_work.


---

Comment by awebb created at 2010-01-26 15:40:23

According to:  http://www.python.org/dev/peps/pep-0371/ there was a renaming from processing to multiprocessing. There may be other changes to the api as well.

Adam


---

Comment by jhpalmieri created at 2010-01-26 19:37:18

First, we need a patch to the sage library changing any remaining imports of "processing" to "multiprocessing"; this involves changes to parallel/multiprocessing.py, plus perhaps changing the name of that file (so that in parallel/decorate.py, a line like `import multiprocessing` means import parallel/multiprocessing.py, while in parallel/multiprocessing.py, a line like `from multiprocessing import Pool` means to import the Python multiprocessing module).

The file SAGE_ROOT/devel/sage/setup.py also imports from the processing module, so that needs to be changed.

Also, as awebb suggests, the api seems to have changed: when I make these changes and run doctests on sage/parallel/, I get errors like

```
AttributeError: 'Pool' object has no attribute 'imapUnordered'
```


After making the appropriate changes, perhaps we should test everything by moving the pyprocessing files out of SAGE_ROOT/local/lib/python/site-packages/ to make sure they're not being loaded?


---

Comment by jhpalmieri created at 2010-01-26 19:38:49

Oh, sage-ptest also imports `processing`.


---

Comment by jhpalmieri created at 2010-01-26 19:51:51

patch for scripts repository


---

Comment by jhpalmieri created at 2010-01-26 19:57:35

Changing status from needs_work to needs_review.


---

Attachment

Here are two patches, one for the scripts repo and one for the main repo.  Note that one patch removes the file "parallel/multiprocessing.py" (actually renaming it to "multiprocessing_sage.py" plus the requisite changes to import statements).  When I tried to run Sage after applying this patch, I still had copies of multiprocessing.py lying around which I had to delete by hand (this won't be a problem from a build from scratch, but upgrading could problematic): I had to delete the files

```
SAGE_ROOT/devel/sage/build/lib.macosx-10.6-i386-2.6/sage/parallel/multiprocessing.py
SAGE_ROOT/local/lib/python/site-packages/sage/parallel/multiprocessing.py
```

(Without deleting these files, commands like `import multiprocessing` in parallel/multiprocessing_sage.py imported the old Sage file `multiprocessing.py` instead of the Python module `multiprocessing`.)

I haven't run a full test suite yet, but "sage -tp 2 SAGE_ROOT/devel/sage/sage/parallel/" passes all tests for me.


---

Comment by jhpalmieri created at 2010-01-30 02:29:05

Here's another version of the patch; this one also patches SAGE_ROOT/devel/sage/spkg-install to try to delete the bad files.  I don't know if I did this right, though; please review.


---

Comment by mvngu created at 2010-01-31 17:29:24

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2010-01-31 17:29:24

Here are the steps I took:

 1. Applied [trac_6503-scripts.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6503/trac_6503-scripts.patch) to the scripts repository.
 1. Applied [trac_6503-sage.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6503/trac_6503-sage.patch) to the Sage library.
 1. Removed `pyprocessing-0.52.p0.spkg` from the standard spkg repository.
 1. Removed the following lines from `spkg/install`:
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

Comment by mvngu created at 2010-01-31 19:13:19

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

Comment by drkirkby created at 2010-02-25 15:53:58

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

Comment by jhpalmieri created at 2010-02-26 15:58:08

For the record, I'm attaching a new version of the patch which deals with the reference to processing in setup.py -- the one that I missed in the first patch.  I don't know why mvngu's build process failed with this patch.  I may try to build it myself if I have time, but if anyone else wants to give it a try, please go ahead.


---

Comment by jhpalmieri created at 2010-02-26 15:58:34

patch for Sage library


---

Attachment

Okay, I took a copy of Sage, applied the attached patches and made Minh's suggested changes to install and deps, then ran `sage -sdist`.  I took the resulting tar file and tried to build it.  With MAKE defined as "make -j2", I ran into the same issue that Minh did.  At that point I redefined MAKE to be "make", and the build finished.  I'm running doctests now, but everything looks good.  In particular, `sage/sage/parallel` passes doctests.


---

Comment by drkirkby created at 2010-02-26 23:58:30

Note also that #8191, which already has positive review and I believe will be in the next release, needs changes to spkg/install and spkg/standard/deps. These need to be coordinated with patches. 

I'd love to try your fixes, but I'm not sure how to apply a patch like this to the Sage library. Perhaps if you could give me an idiots buide to how to do this with Mercurial, I'll try it. 

Dave


---

Comment by jhpalmieri created at 2010-02-27 00:03:33

The simplest way to see the bug that Minh reported is as follows:

 - apply trac_6503-sage.patch
 - export MAKE='make -j2'  (to do a parallel build)
 - touch a cython file in the Sage library
 - sage -b

You should get the pickling error he described above.


---

Comment by AlexGhitza created at 2010-02-27 04:14:15

Replying to [comment:14 drkirkby]:
> Note also that #8191, which already has positive review and I believe will be in the next release, needs changes to spkg/install and spkg/standard/deps. These need to be coordinated with patches. 
> 
> I'd love to try your fixes, but I'm not sure how to apply a patch like this to the Sage library. Perhaps if you could give me an idiots buide to how to do this with Mercurial, I'll try it. 

In my opinion, Mercurial queues are the easiest way to do these things.  Have a look at the quick startup guide at:

http://wiki.sagemath.org/MercurialQueues


---

Attachment


---

Comment by mhansen created at 2010-02-27 20:13:50

I've added a patch on top of trac_6503-sage.patch which fixes the issue with pickling the instancemethods when building the Sage library in parallel with multiprocessing.


---

Comment by mhansen created at 2010-02-27 20:13:50

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-03-01 23:52:16

mhansen's patch works for me.  Since I wrote the original patch, I can't give the whole thing a positive review.  I'll positively review mhansen's patch, though, and mvngu's instructions [above](http://trac.sagemath.org/sage_trac/ticket/6503#comment:9), items 3-5 in particular (patching spkg/install and spkg/standard/deps, and removing pyprocessing...spkg).

I'm attaching complete versions of the modified versions of install and deps, for completeness.


---

Comment by mvngu created at 2010-03-02 19:54:16

The file "install" here needs to be rebased on top of that at #8191. The latter adds the new iconv spkg. In doing so, it modifies "install". Simiarly, the file "deps" on the current ticket needs to be rebased on top of that at #8191.


---

Comment by mvngu created at 2010-03-02 19:54:16

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2010-03-02 20:13:53

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-03-02 20:13:53

Given that neither #8191 nor this ticket has a positive review, I'm not sure why this one in particular needs rebasing.  But here you go.


---

Comment by jhpalmieri created at 2010-03-02 20:14:26

rebased against #8191


---

Attachment

rebased against #8191


---

Comment by jhpalmieri created at 2010-03-02 20:14:50

rebased against #8191


---

Attachment


---

Attachment


---

Comment by mvngu created at 2010-03-03 01:42:33

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-03 01:42:33

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

Comment by mvngu created at 2010-03-03 01:58:05

Merged in this order:

 1. Removed `SAGE_ROOT/spkg/standard/pyprocessing-0.52.p0.spkg`.
 1. Replaced the file `SAGE_ROOT/spkg/install` with [install](http://trac.sagemath.org/sage_trac/attachment/ticket/6503/install).
 1. Replaced the file `SAGE_ROOT/spkg/standard/deps` with [deps](http://trac.sagemath.org/sage_trac/attachment/ticket/6503/deps).
 1. Merged [trac_6503-scripts.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6503/trac_6503-scripts.patch) in the scripts repository.
 1. Merged [trac_6503-sage.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6503/trac_6503-sage.patch) in the Sage library.
 1. Merged [trac_6503-fix.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6503/trac_6503-fix.patch) in the Sage library.


---

Comment by mvngu created at 2010-03-03 01:58:05

Resolution: fixed
