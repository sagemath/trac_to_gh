# Issue 9519: scipy does not exit if there are build failures, but spkg-install looks OK

Issue created by migration from https://trac.sagemath.org/ticket/9519

Original creator: drkirkby

Original creation time: 2010-07-16 22:43:58

Assignee: GeorgSWeber

CC:  leif mpatel mvngu jhpalmieri dimpase

Building Sage 4.5 on a Sun Blade 2000, with dual UltraSPARC III+ processors in 64-bit mode, the build process produces some obvious *error* messages. These are not warnings, but errors. 


```
gcc _configtest.o -L/export/home/drkirkby/64/sage-4.5/local/lib -lf77blas -lcblas -latlas -o _configtest
ld: fatal: file _configtest.o: wrong ELF class: ELFCLASS64
ld: fatal: File processing errors. No output written to _configtest
collect2: ld returned 1 exit status
ld: fatal: file _configtest.o: wrong ELF class: ELFCLASS64
ld: fatal: File processing errors. No output written to _configtest
collect2: ld returned 1 exit status
failure.
removing: _configtest.c _configtest.o
Status: 255
Output:
```


`wrong ELF class:` messages mean an attempt what made to link a mixture of 32-bit and 64-bit object files. 

But the build process still goes on to report that scipy has installed OK. 


```
real    22m34.927s
user    20m23.356s
sys     1m5.603s
Successfully installed scipy-0.7.p5
```


What is odd, is that `spkg-install` looks to be OK to me. 


```
python setup.py build
if [ $? -ne 0 ]; then
    echo "Error building scipy."
    exit 1
fi

# Intall
python setup.py install
if [ $? -ne 0 ]; then
    echo "Error installing scipy."
    exit 1
fi
```


The problem is *not* like the cephes package, or several others, where the return code of _make_ is not checked.  

At this point, I've not no idea if this is an upstream bug, or a Sage bug. 

Anyone got any ideas? 

Dave


---

Comment by mpatel created at 2010-07-17 00:08:24

Could you give a link to the full log for scipy?


---

Comment by leif created at 2010-07-17 00:09:46

Well, `_configtest` sounds rather harmless...

Are you sure the finally produced(?) scipy is really broken?


---

Comment by drkirkby created at 2010-07-17 00:23:34

Replying to [comment:2 mpatel]:
> Could you give a link to the full log for scipy?
Sure. Will attach to the ticket. Since its fairly large, I have compressed it. 

I think there is a problem with the build of ATLAS, as that shows a `wrong ELF class:` message. Since scipy links to ATLAS, that is probably the problem. But I don't think that is an excuse for the scipy build to continue, though Leif thinks it's harmless. 

Dave


---

Attachment

Compressed version of sage-4.5/spkg/logs/scipy-0.7.p5.log


---

Comment by mpatel created at 2010-07-17 00:28:47

If enough parts of Sage run, you could try running the test suite, e.g.,

```sh
$ ./sage -sh
sage subshell$ easy_install nose
sage subshell$ exit
$ ./sage -python -c "import scipy; scipy.test()"
```

[Here's the output](http://sage.math.washington.edu/home/mpatel/trac/9519/scipy_nosetest.log) on sage.math with 4.5.

I suppose we could optionally (if the user/developer desires) install nose automatically.


---

Comment by drkirkby created at 2010-07-17 00:32:21

Replying to [comment:3 leif]:
> Well, `_configtest` sounds rather harmless...
> 
> Are you sure the finally produced(?) scipy is really broken?

I'm not certain. I thought ATLAS was broken, but I think I have remade the broken library. How can I test just scipy? The 64-bit SPARC port is not 100% ok. I can't run the doctests, as it segfaults, but Sage does semi-work. I can do computations with it. So `sage -t foobar` might work

Dave


---

Comment by drkirkby created at 2010-07-17 00:48:57

Replying to [comment:5 mpatel]:
> If enough parts of Sage run, you could try running the test suite, e.g.,
> {{{
> #!sh
> $ ./sage -sh
> sage subshell$ easy_install nose
> sage subshell$ exit
> $ ./sage -python -c "import scipy; scipy.test()"
> }}}
> [Here's the output](http://sage.math.washington.edu/home/mpatel/trac/9519/scipy_nosetest.log) on sage.math with 4.5.
> 
> I suppose we could optionally (if the user/developer desires) install nose automatically.

I've never come across 'nose' - my python skills are next to zero. I will attach a log. As you can see, it finally fails with a core dump, but perhaps has some useful information before it dumps core.

BTW, I've removed the static atlas libs, leaving only the shared ones. That might be a cause of a problem. I can't understand the need for both. If yyou look in the ATLAS package, you can see about 3 dynamic libraries will be missing. Two are not built, and one is deleted. I built them all and deleted no dynamic ones - only the static. 


Dave


---

Attachment

Output from: ./sage -python -c "import scipy; scipy.test()" > scipy.test.log  2>&1


---

Comment by mkoeppe created at 2020-08-30 20:27:15

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-08-30 20:27:15

outdated, should be closed


---

Comment by dimpase created at 2020-08-30 21:03:58

Changing status from needs_review to positive_review.


---

Comment by dimpase created at 2020-08-30 21:03:58

ok


---

Comment by chapoton created at 2020-09-21 16:41:51

Resolution: invalid
