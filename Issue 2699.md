# Issue 2699: scipy fails to build

Issue created by migration from https://trac.sagemath.org/ticket/2699

Original creator: schilly

Original creation time: 2008-03-28 14:07:06

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



---

Attachment

install.log of failed scipy build


---

Comment by mabshoff created at 2008-03-28 15:06:34

What is CC and CXX set to? This looks very fishy and is likely not the fault of Sage. Please report build issues to sage-devel and so not open ticket until it is clear if there is actually a bug in Sage.

Also:
 * please provide the complete install.log
 * do not attach compressed files to trac since those tend to cause problems

Cheers,

Michael


---

Comment by schilly created at 2008-03-28 15:14:47

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

Comment by mabshoff created at 2008-03-28 15:50:40

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

Comment by mabshoff created at 2008-03-28 16:59:03

Matplotlib also fails to build [at least the C++ bits - with the same issue, i.e. invoking "g++ gcc ...]. Even after exporting LANG=C the problem still happens. In this case  LANG is set to de_AT.UTF-8.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-12 18:53:15

Resolution: fixed


---

Comment by mabshoff created at 2008-05-12 18:53:15


```
[20:06] <mabshoff> schilly: is #2699 still an issue for you?
[20:06] <mabshoff> I have been unable to hit it on 6.06 LTS and also 8.04 LTS.
[20:06] <schilly> err ... let me see
[20:09] <schilly> mabshoff: close it, if it happens again i'll open another ticket. i think this was simply solved by the next version after 2.10. or something like that
```

