# Issue 1852: Configure R to use Atlas / other improvements to R package

Issue created by migration from https://trac.sagemath.org/ticket/1852

Original creator: pdenapo

Original creation time: 2008-01-19 21:39:37

Assignee: was

Currenty R in Sage is configured to use its own implementation of BLAS, it would
be better to configure it to use ATLAS (wich has better performance, I think)

A parameter --with-blas can be pased to configure, to tell it wich BLAS we 
want to use.

A comenet:
See also ticket #1721, we should avoid hardcoding the location of 
the BLAS library . If that thicket is implemented, perhaps an enviroment 
variable should be setto the BLAS library that we want to use (in sage-env?) 
(or a symlink from $SAGE_LOCAL/libblas.so to the system version)

Other questions:
- why is R configured with --with-reccomended-packages=no ?
(perhaps it would be possible to offer the recommended packages as an optional
package?)

- why is the whoule source code of R installed in $SAGE_LOCAL/lib/r ? 



---

Comment by was created at 2008-01-20 01:49:24

> Other questions: - why is R configured with --with-reccomended-packages=no ? 
> (perhaps it would be possible to offer the recommended packages as an optional package?)

Because `--with-recommended-packages=yes` takes 5 times to build as no. Simple as that.    And for the first few releases of R in Sage it makes sense to be conservative to keep breakage to a minimal.  We will revisit this... say now.

> - why is the whoule source code of R installed in $SAGE_LOCAL/lib/r ?

No clue.  I didn't know that.  It is surprising.


---

Comment by mabshoff created at 2008-01-23 07:41:50

Somebody (was?) does the following in spkg-install:

```
# For some reason make install sucks -- it doesn't copy the libraries or R bin over ??

cp lib/* "$SAGE_LOCAL"/lib/
cp bin/R "$SAGE_LOCAL"/bin/
```


Very, very odd to say the least.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-23 07:44:19

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2008-01-23 07:44:19

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2008-01-24 08:56:31

Changing component from algebraic geometry to packages.


---

Comment by mabshoff created at 2008-01-25 11:29:59

The r.spkg was a total disaster to put it nicely. It took me about sic hours to sort it all out, but two official revisions later I have:

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha2/r-2.6.1.p10.spkg

The spkg builds on Linux and OSX, passes testall and now uses ATLAS if it is provided.

Cheers,

Michael


---

Comment by was created at 2008-01-25 15:04:10

I read the new spkg-install, built this package on all our test machines, and ran this test with success on all of them:


```
was@debian32:~$ echo "import rpy; rpy.r('2+2')" | sage-2.10.1.alpha1/sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.1.alpha1, Release Date: 2008-01-21               |
| Type notebook() for the GUI, and license() for information.        |
sage: 4.0
sage: 
```


So thumbs up.


---

Comment by mabshoff created at 2008-01-25 17:28:32

Merged in Sage 2.10.1.alpha2


---

Comment by mabshoff created at 2008-01-25 17:28:32

Resolution: fixed
