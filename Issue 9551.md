# Issue 9551: Sage can try to write outside $SAGE_ROOT - potentially screwing a system up

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-07-19 16:06:29

Assignee: GeorgSWeber

CC:  alexanderdreyer leif

As reported here:

http://groups.google.co.uk/group/sage-devel/browse_thread/thread/60d384d785d9f034/9cdf5d6fbecf23d0?lnk=gst&q=write+kirkby#9cdf5d6fbecf23d0

Sage tried to write /usr/lib/python2.4/site-packages/ on t2.math.washinton.edu'. (Solaris ships with Python 2.4.4 in 2.4.4). 

This was on the 4.5.alpha0 build, though I'm not aware of any one else raising this issue, so it's quite possible nothing has been done to fix the bug in the latest build (4.5 as I write). 

Since I'm not stupid enough to build Sage as root, this was not a problem, and just resulted in a failed build. But I'm well aware many people do build Sage as root, in which case this could be very serious. (I guess one could argue they got what they deserved). 

Another ticket I created (#9209) shows that Sage can fail to build if a user has a local installation of python, but if one makes that installation unreadable, so Sage will build. 

Another, possibly relevant ticket is #9536

I personally do not have the python skills to sort this out, but I do believe it is potentially a serious problem, as a user can mess up their system by writing to system directories. 

```
copying rpy/rinterface/tests/test_SexpVector.py ->
build/lib.solaris-2.10-sun4v-2.4/rpy2/rinterface/tests
copying rpy/rinterface/tests/test_SexpEnvironment.py ->
build/lib.solaris-2.10-sun4v-2.4/rpy2/rinterface/tests
copying rpy/rinterface/tests/__init__.py ->
build/lib.solaris-2.10-sun4v-2.4/rpy2/rinterface/tests
copying rpy/rinterface/tests/test_SexpClosure.py ->
build/lib.solaris-2.10-sun4v-2.4/rpy2/rinterface/tests
copying rpy/rinterface/tests/test_EmbeddedR.py ->
build/lib.solaris-2.10-sun4v-2.4/rpy2/rinterface/tests
copying rpy/rinterface/tests/test_SexpVectorNumeric.py ->
build/lib.solaris-2.10-sun4v-2.4/rpy2/rinterface/tests
running build_ext
building 'rpy2.rinterface.rinterface' extension
creating build/temp.solaris-2.10-sun4v-2.4
creating build/temp.solaris-2.10-sun4v-2.4/rpy
creating build/temp.solaris-2.10-sun4v-2.4/rpy/rinterface
/usr/lib/python2.4/pycc -DNDEBUG
-I/rootpool2/local/kirkby/sage-4.5.alpha0/local/include
-L/rootpool2/local/kirkby/sage-4.5.alpha0/local/lib/ -O2 -g -m64
-I/rootpool2/local/kirkby/sage-4.5.alpha0/local/include -DR_INTERFACE_PTRS=1
-DCSTACK_DEFNS=1 -DRIF_HAS_RSIGHAND=1
-I/rootpool2/local/kirkby/sage-4.5.alpha0/local/lib/R/include -Irpy/rinterface
-I/usr/include/python2.4 -c rpy/rinterface/array.c -o
build/temp.solaris-2.10-sun4v-2.4/rpy/rinterface/array.o
/usr/lib/python2.4/pycc -DNDEBUG
-I/rootpool2/local/kirkby/sage-4.5.alpha0/local/include
-L/rootpool2/local/kirkby/sage-4.5.alpha0/local/lib/ -O2 -g -m64
-I/rootpool2/local/kirkby/sage-4.5.alpha0/local/include -DR_INTERFACE_PTRS=1
-DCSTACK_DEFNS=1 -DRIF_HAS_RSIGHAND=1
-I/rootpool2/local/kirkby/sage-4.5.alpha0/local/lib/R/include -Irpy/rinterface
-I/usr/include/python2.4 -c rpy/rinterface/r_utils.c -o
build/temp.solaris-2.10-sun4v-2.4/rpy/rinterface/r_utils.o
/usr/lib/python2.4/pycc -DNDEBUG
-I/rootpool2/local/kirkby/sage-4.5.alpha0/local/include
-L/rootpool2/local/kirkby/sage-4.5.alpha0/local/lib/ -O2 -g -m64
-I/rootpool2/local/kirkby/sage-4.5.alpha0/local/include -DR_INTERFACE_PTRS=1
-DCSTACK_DEFNS=1 -DRIF_HAS_RSIGHAND=1
-I/rootpool2/local/kirkby/sage-4.5.alpha0/local/lib/R/include -Irpy/rinterface
-I/usr/include/python2.4 -c rpy/rinterface/rinterface.c -o
build/temp.solaris-2.10-sun4v-2.4/rpy/rinterface/rinterface.o
/usr/lib/python2.4/pycc -G -L/rootpool2/local/kirkby/sage-4.5.alpha0/local/lib/
-m64 -I/rootpool2/local/kirkby/sage-4.5.alpha0/local/include
-L/rootpool2/local/kirkby/sage-4.5.alpha0/local/lib/ -O2 -g -m64
-I/rootpool2/local/kirkby/sage-4.5.alpha0/local/include
build/temp.solaris-2.10-sun4v-2.4/rpy/rinterface/array.o
build/temp.solaris-2.10-sun4v-2.4/rpy/rinterface/r_utils.o
build/temp.solaris-2.10-sun4v-2.4/rpy/rinterface/rinterface.o
-L/rootpool2/local/kirkby/sage-4.5.alpha0/local/lib/R/lib
-L/rootpool2/local/kirkby/sage-4.5.alpha0/local/lib/R/modules
-R/rootpool2/local/kirkby/sage-4.5.alpha0/local/lib/R/lib
-R/rootpool2/local/kirkby/sage-4.5.alpha0/local/lib/R/modules -lR -o
build/lib.solaris-2.10-sun4v-2.4/rpy2/rinterface/rinterface.so
-L/rootpool2/local/kirkby/sage-4.5.alpha0/local/lib/R//lib -lR -llapack -lblas
running install_lib
creating /usr/lib/python2.4/site-packages/rpy2
error: could not create '/usr/lib/python2.4/site-packages/rpy2': Permission denied
Error building RPY -- Python interface to R. 
```



---

Comment by AlexanderDreyer created at 2010-07-19 21:34:19

To be better save than sorry, the `spkg-install` script of rpy should call `python setup.py --prefix=$SAGE_HOME` etc.


---

Comment by ecurry created at 2011-06-16 00:00:09

It might be useful if the README.TXT file (eg. at http://boxen.math.washington.edu/sage/src/README.txt) included a warning against building Sage as root, such as the install guide (http://www.sagemath.org/doc/installation/source.html#steps-to-install-from-source - Step 7) has, at least until this ticket gets fixed.

-Eva


Replying to [ticket:9551 drkirkby]:
> As reported here:
> 
> http://groups.google.co.uk/group/sage-devel/browse_thread/thread/60d384d785d9f034/9cdf5d6fbecf23d0?lnk=gst&q=write+kirkby#9cdf5d6fbecf23d0
> 
> Sage tried to write `/usr/lib/python2.4/site-packages/` on _t2.math.washington.edu_. A larger section of the error is shown further down the ticket, but the most critical line is:
> 
> {{{
> error: could not create '/usr/lib/python2.4/site-packages/rpy2': Permission denied
> }}}
> 
> Recent(ish) version of Solaris 10 include Python 2.4.4 in `/usr/bin`, with libraries in `/lib/python2.4/`, which is where the Sage build tried to write. 
> 
> This was on the 4.5.alpha0 build, though I'm not aware of any one else raising this issue, so it's quite possible nothing has been done to fix the bug in the latest build (4.5 as I write). 
> 
> Since I'm not stupid enough to build Sage as root, this was not a problem, and just resulted in a failed build. But I'm well aware many people do build Sage as root, in which case this could be very serious. (I guess one could argue they got what they deserved).


---

Comment by jdemeyer created at 2013-12-19 12:01:15

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-12-19 12:01:15

I have never seen this error recently, so I guess it is fixed.


---

Comment by jdemeyer created at 2013-12-19 12:01:19

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2013-12-20 15:59:02

Resolution: fixed
