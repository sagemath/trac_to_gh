# Issue 9507: if spkg-install is a Python script, first check that SAGE_LOCAL/bin/python exists.

Issue created by migration from https://trac.sagemath.org/ticket/9507

Original creator: was

Original creation time: 2010-07-15 13:14:03

Assignee: GeorgSWeber

See trac #9368. 


---

Comment by drkirkby created at 2010-07-15 22:24:54

How do you check if Python exists in a Python script? I would have thought the code to check Python exists would have relied on Python existing - a catch 22. Of course, if you happen to have a system wide Python, then you could use that to check for $SAGE_LOCAL/bin/python. But that's going to be far from reliable, since: 
 * A system may have no Python
 * A system Python may be too old. 
 * A system Python may not work properly, which is what appears to have happened in your sage_fortran setup. 

But I guess it is more reliable than no test at all, but I can't think of a 100% sure-fire way of doing this. One could make all spkg-install's /bin/sh scripts, and use that to check for Python before calling a Python script. But that's a lot of messing around, and one probably more likely to introduce a bug than detect one. 

Dave


---

Comment by was created at 2010-07-15 23:45:41

Changing status from new to needs_review.


---

Comment by was created at 2010-07-15 23:45:41

It was easier to just post the solution than...


---

Comment by drkirkby created at 2010-07-16 00:33:19

Neat, I like it. 

Would it not be worth checking *all* files in the top-level directory, rather than just spkg-install? Several packages have both bash scripts and python scripts in them. I don't know of any packages that have spkg-install which is a bash script, and also a python script, but it would not surprise me if one or two existed.

spkg-install in ATLAS is a small python script, which then calls a large bash script. What's to stop there being any packages with it the other way around, where a bash script calls a python script? 

Dave


---

Comment by rlm created at 2010-07-16 08:22:18

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-07-16 08:22:18

Looks good! I tried forcing Fortran to build before Python in 4.5.rc1, and got the following with this patch applied:


```
fortran-20100629/src/g95/g95_x86_osx.tar.bz2
Finished extraction
****************************************************
Host system
uname -a:
Linux geom 2.6.24-24-server #1 SMP Tue Aug 18 16:51:43 UTC 2009 x86_64 GNU/Linux
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --enable-languages=c,c++,fortran,objc,obj-c++,treelang --prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --enable-nls --with-gxx-include-dir=/usr/include/c++/4.2 --program-suffix=-4.2 --enable-clocale=gnu --enable-libstdcxx-debug --enable-objc-gc --enable-mpfr --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
Thread model: posix
gcc version 4.2.4 (Ubuntu 4.2.4-1ubuntu4)
****************************************************
The spkg-install script depends on Python, but Python is not
yet installed.  If this is a standard package, you should
properly update the /scratch/rlmill/test/sage-4.5.rc1/spkg/standard/deps script.
```



---

Comment by leif created at 2010-07-16 13:08:21

To avoid confusion to users, we should perhaps clarify in the error message that *_Sage's* Python_ is not yet installed. (Otherwise I expect reports like _"I have a Python installed, but..."_.)

The comment should read `# if not, ...` rather than `# if so, ...` (or `check if ...` should be negated).

I'd prefer `[ -x $SAGE_LOCAL/bin/python]`. Hope this never gets a script (ending up in the scripts repo) that tries to call the binary located elsewhere. On the other hand, we could do just this (making it a bash script), and test for presence of the binary in that script. The advantage would be that `env python` would always find Sage's one (no matter if the binary is already installed), of course assuming `sage-env` has been sourced. But this would also introduce another stage of indirection...


---

Comment by leif created at 2010-07-16 13:23:36

P.S.: In general, I think it's a bad idea to make Sage packages depend on Python despite the upstream package not depending on it. I.e., IMHO Python install scripts should only be used if the package depends on Python anyway.


---

Comment by leif created at 2010-07-16 13:47:41

Yet another one:

Perhaps in addition to a slightly modified version of William's patch, put that as `$SAGE_LOCAL/bin/python` into the scripts repo:

```sh
#!/usr/bin/env bash

echo python $@ ":"

echo "Error: Sage's Python has not yet been installed!"
echo "       This is most probably due to incorrect dependencies in the Makefiles."
echo "Please report this to ..."

exit 1
```

and let the Python spkg just overwrite it with the binary. (This avoids unnecessary indirection.)


---

Comment by leif created at 2010-07-16 19:46:02

Unless this ticket gets immediately merged, please also consider [this bug](http://trac.sagemath.org/sage_trac/ticket/9281#comment:15) in `sage-spkg`, which is trivially fixed but not directly related to this ticket, so I'm not sure if I should upload a patch for that _here_.

-Leif


---

Comment by was created at 2010-07-17 12:58:18

Replying to [comment:7 leif]:
> Yet another one:
> 
> Perhaps in addition to a slightly modified version of William's patch, put that 
> as `$SAGE_LOCAL/bin/python` into the scripts repo:

I definitely do not like this idea.  Though it seems good at first, it's really bad. 

  (1) it's hackish

  (2) It means that once python is installed, the scripts repository is always confused/corrupted/etc.   In particular, it would completely break "sage -upgrade", since the scripts repo is upgraded via `hg pull`.


---

Comment by was created at 2010-07-17 13:08:05

new version with better error message, as Lief suggested.


---

Attachment


---

Comment by rlm created at 2010-07-19 11:20:34

Resolution: fixed
