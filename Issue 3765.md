# Issue 3765: make it so "sage -br" does the cythonization in parallel using pyprocessing

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-08-03 18:26:24

Assignee: was

This would be just a few lines of code to implement and would make doing "sage -br" much faster. 


---

Comment by was created at 2008-08-03 21:15:15

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

Comment by gfurnish created at 2008-08-03 22:22:42

Wasn't this the point of pbuild?


---

Comment by mhansen created at 2008-08-04 09:17:39

I tried this out, and it worked perfectly.  A few comments:

1) Don't we already have a function for CPU detection that execute_list_of_commands should use?

2) There are no doctests for any of the new functions.


---

Comment by was created at 2008-08-05 05:08:38

> I tried this out, and it worked perfectly. A few comments:

> 1) Don't we already have a function for CPU detection that execute_list_of_commands should use?

I copied those 4 lines of code into setup.py, since this is a chicken and egg problem.  You can't call sage library code from setup.py, since setup.py is run to install the sage library.   It's only about four lines of code anyways.

> 2) There are no doctests for any of the new functions.

Unfortunately it is impossible to doctest setup.py since the act of importing setup.py would cause the distutils stuff to get run.    Also setup.py isn't part of the sage library, so it's functions aren't available elsewhere.

That said, it might make sense to separate as much code as possible out of setup.py into a separate module that is not part of the sage library.  I think such refactoring should be in another ticket though.


---

Comment by mhansen created at 2008-08-05 09:51:13

Comments seem reasonable to me.  Positive review


---

Comment by mabshoff created at 2008-08-06 00:21:15

Should we not check some env variable (SAGE_THREADS ?) before just assuming we want to use all CPUs simultaneously? Imagine two or three people on sage.math building in parallel ...

Cheers,

Michael


---

Comment by mhansen created at 2008-08-06 19:48:27

Checking SAGE_THREADS seems like a good idea especially if that environment variable is used elsewhere.  What would a good default for it be? 2?  Would a user have to edit sage-env if they wanted to say always use 4 threads on their machine?


---

Comment by mabshoff created at 2008-08-08 22:43:27

We need to make the Sage library depend on PyProcessing since otherwise this will blow up for a fresh build.

Cheers,

Michael


---

Comment by malb created at 2008-09-07 13:11:00

What's the status of it? It has a positive review but the comments read like "needs work"


---

Comment by mabshoff created at 2008-09-07 14:25:14

Replying to [comment:10 malb]:
> What's the status of it? It has a positive review but the comments read like "needs work"

Yes, it does. That is the reason it has not been merged yet :)

Cheers,

Michael


---

Comment by was created at 2008-09-22 04:54:16


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

Attachment


---

Comment by was created at 2008-10-23 20:48:13

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

Comment by was created at 2008-10-23 20:49:37

this is rebased against sage-3.2.alpha0 and uses an environment variable MAKE


---

Attachment

Looks good to me. I will fix deps so that the Sage libraru depends on pyprocessing.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-27 02:11:11

Merged in Sage 3.2.alpha1


---

Comment by mabshoff created at 2008-10-27 02:11:11

Resolution: fixed
