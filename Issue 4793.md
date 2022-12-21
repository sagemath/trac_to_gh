# Issue 4793: Update lcalc to the new upstream 1.2

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-12-14 07:45:09

Assignee: mabshoff

CC:  cremona ylchapuy drkirkby

As the summary says. This should be done at the same time as the update to the latest stable pari.

Cheers,

Michael


---

Comment by mvngu created at 2009-10-01 06:19:01

See ticket #5396 for upgrading lcalc to version 1.23


---

Comment by rishi created at 2010-03-17 19:37:30

I am attaching a spkg for lcalc.

http://sage.math.washington.edu/home/rishikesh/lcalc/lcalc-1.23.spkg

This spkg is result of last last few discussion in #5396


---

Comment by rishi created at 2010-03-17 19:37:30

Changing status from new to needs_review.


---

Comment by rishi created at 2010-03-17 19:47:27

I split the spkg  from lcalc wrapper. The discussion on spkg was becoming longer and digressing from the wrapper itself.


---

Comment by rishi created at 2010-03-17 19:54:32

Changing assignee from mabshoff to rishi.


---

Comment by robertwb created at 2010-03-24 18:13:00

All the headers should be copied to a subdir of local/include (given they might clash with others).


---

Comment by robertwb created at 2010-03-24 18:13:12

Changing status from needs_review to needs_work.


---

Comment by robertwb created at 2010-03-24 18:14:54

Also has issues on OS X 


```
dyld: lazy symbol binding failed: Symbol not found: ___gmpn_lshift
  Referenced from: /Users/robertwb/sage/sage-4.0/local/lib//libpari-gmp.dylib
  Expected in: flat namespace
```


when running tests in sage/lfunctions/lcalc.py


---

Comment by rishi created at 2010-03-25 04:18:50

Changing status from needs_work to needs_review.


---

Comment by rishi created at 2010-03-25 04:18:50

This spkg has been tested on OSX, linux and Solaris. The header files are now installed in $SAGE_LOCAL/include/lcalc

http://sage.math.washington.edu/home/rishikesh/lcalc/lcalc-1.23.spkg


---

Comment by drkirkby created at 2010-03-26 00:20:32

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-03-26 00:20:32

Hi,
there are a few problems with spkg-install, which don't reflect how Sage is currently being built. 

 * You said on #5396 "One more thing- I've also cleaned up my makefile a bit, and, in the source, got rid of depreciated headers and unused variables." Did you notice that your Makefile is being overwritten, by the following line:
  {{{
  cp ../../patches/Makefile.sage Makefile
  }}}
  Are those changes appropriate? But looking at your own Makefile, I see still see options to  suppress warnings messages. 
    * -Wa,-W is designed to suppress warnings from the assembler, which fails if the Sun assembler is used. (That's why I had to re-write part of your makefile before). 
    * -Wno-deprecate is designed to suppress warnings about depreciated headers. 

A few more things. 

 * Don't bother checking for SAGE_FORTRAN_LIB, as it is tested in the 'prereq' script. 
 * Don't bother checking for SAGE_FORTRAN, as again prereq takes care of that. 
 * Don't bother checking if the GNU and Sun compilers are mixed - that is taken care of elsewhere. 
 * The line:
  {{{
   echo "Building a 32-bit version of lcalc"
  }}}

   is incorrect, as some systems build 64-bit by default, and so the lack of a -m64 flag does not imply a 32-bit build. 
 * The line:
  {{{
  if [ "x$SAGE64" = "xyes" ] || [ "x$SAGE64" = "x1" ]  ; then
  }}}
can be simplified to 
  {{{
  if [ "x$SAGE64" = xyes ] ; then
  }}}

as SAGE64 can only be unset, set to 'yes' or set to 'no' - any other combination is not permitted. 
 
Are there any self-tests of this package? If so, it should have a spkg-check too, but of course, if there are no self-tests, then that is inappropriate. 

Dave


---

Comment by rishi created at 2010-03-26 15:48:50

Replying to [comment:12 drkirkby]:
> Hi,
> there are a few problems with spkg-install, which don't reflect how Sage is currently being built. 
> 
>  * You said on #5396 "One more thing- I've also cleaned up my makefile a bit, and, in the source, got rid of depreciated headers and unused variables." Did you notice that your Makefile is being overwritten, by the following line:
>   {{{
>   cp ../../patches/Makefile.sage Makefile
>   }}}
>   Are those changes appropriate? But looking at your own Makefile, I see still see options to  suppress warnings messages. 
>     * -Wa,-W is designed to suppress warnings from the assembler, which fails if the Sun assembler is used. (That's why I had to re-write part of your makefile before). 
>     * -Wno-deprecate is designed to suppress warnings about depreciated headers. 


Please see what the package does. I have not made any changes to original Makefile, only to Makefile.sage

> 
> A few more things. 
> 

I took the old spkg-install and added what I needed. I did not change what ever happened else where, so the person who changed those should have changed this prereq in lcalc spkg. This includes everything below. I am changing status to needs review.

>  * Don't bother checking for SAGE_FORTRAN_LIB, as it is tested in the 'prereq' script. 
>  * Don't bother checking for SAGE_FORTRAN, as again prereq takes care of that. 
>  * Don't bother checking if the GNU and Sun compilers are mixed - that is taken care of elsewhere. 
>  * The line:
>   {{{
>    echo "Building a 32-bit version of lcalc"
>   }}}
> 
>    is incorrect, as some systems build 64-bit by default, and so the lack of a -m64 flag does not imply a 32-bit build. 
>  * The line:
>   {{{
>   if [ "x$SAGE64" = "xyes" ] || [ "x$SAGE64" = "x1" ]  ; then
>   }}}
> can be simplified to 
>   {{{
>   if [ "x$SAGE64" = xyes ] ; then
>   }}}
> 
> as SAGE64 can only be unset, set to 'yes' or set to 'no' - any other combination is not permitted. 
>  
> Are there any self-tests of this package? If so, it should have a spkg-check too, but of course, if there are no self-tests, then that is inappropriate. 
> 
> Dave 
> 
>


---

Comment by rishi created at 2010-03-26 15:48:50

Changing status from needs_work to needs_review.


---

Comment by was created at 2010-03-26 16:26:12

Hi David,

The command "hg annotate" is helpful in clarifying the above issues.   Let me give you a tutorial about how that command works. Doing 

```
hg annotate spkg-install |grep FORTRAN
```

yields that changeset 22 added all the FORTRAN stuff you're complaining about:

```
changeset:   22:c7e7606b574d
user:        David Kirkby <david.kirkby`@`onetel.net>
date:        Tue Sep 15 07:41:31 2009 -0700
summary:     trac #6609: don't pass GNU flags directly to the Sun assembler
```


You also state you added this in the SPKG.txt:

```
### lcalc-20080205.p3 (David kirkby, 15th September, 2009)
 * A general tidy-up/improvement in many ways, including:
...
 * Check that the C, C++ and Fortran compilers are not a mix of Sun and GNU
```


Your comment about

```
    * The line:

         echo "Building a 32-bit version of lcalc"

        is incorrect, as some systems build 64-bit by default, and so the lack of a -m64 flag does not imply a 32-bit build.

```

is also a complaint about code that you added in patch 22.

So you are currently complaining about and rejecting Rishi's spkg based entirely on problems that you introduced in the spkg. 

Thus I don't think all (any?) of your complaints are valid. 

I'll work with Rishi and Mike Hansen today to get this spkg in.  Since you clearly don't like many of the changes you introduced in changeset 22, I encourage you to create a new trac ticket to remove those changes from say the next version of lcalc.  Then Rishi (who should be the official package maintainer -- Rishi: you may add yourself as such in SPKG.txt) can make those changes.

 -- William


---

Comment by was created at 2010-03-26 18:23:26

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-04-28 19:29:50

I merged this in as lcalc-20100428-1.23.spkg , since using lcalc-1.23.spkg would break the version number ordering and upgrade system.


---

Comment by was created at 2010-04-28 19:29:50

Resolution: fixed
