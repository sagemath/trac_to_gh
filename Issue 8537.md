# Issue 8537: Update Open MPI package to latest - Sage version is 3 years old!

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-03-14 21:53:51

Assignee: tbd

Sage has an Open MPI optional package, which uses version 1.1.4 of Open MPI. This was released on Jan 30, 2007, so is more than 3 years old. It fails to build on Solaris - see #8522.

The optional package is very different to most other Sage packages, which shows its age. 

 * No SPKG.txt
 * No Mercurial repository
 * Sources sit in top-level directory, not in a 'src' subdirectory. 

I'll create a package based on the latest version of Open MPI, which is version 1.4.1, which was released 15th January 2010.


---

Comment by was created at 2010-03-14 23:13:46

Resolution: duplicate


---

Comment by was created at 2010-03-14 23:13:46

This is a dup of #8455, as a search for "update mpi" in trac shows.


---

Comment by mhansen created at 2010-03-14 23:25:02

Actually, #8455 is for MPIR and not MPI :-)


---

Comment by mhansen created at 2010-03-14 23:25:02

Changing status from closed to new.


---

Comment by mhansen created at 2010-03-14 23:25:02

Resolution changed from duplicate to 


---

Comment by mhansen created at 2010-03-14 23:25:16

From wstein:

I think the builds options are relevant to building the optional sage spkg that depends on mpi, namely mpi4py. If somebody updates openmpi, they might make sure mpi4py also works with the new version.


---

Comment by drkirkby created at 2010-03-15 00:26:15

I've created a ticket to update mpi4py - #8538, as that is very old too. I'll try to test the two packages together. 

The old version of openmpi used these configure options:


```
./configure --prefix="$SAGE_LOCAL" --with-f90-max-array-dim=0 --disable-mpi-f77 
--disable-mpi-f90 --with-mpi-f90-size=trivial
```


I'll look as whether these are all needed, as both openmpi and mpi4py are several years old. 

Dave


---

Comment by maldun created at 2011-01-07 00:18:17

Since I need mpi4py for a seminar and the current version didn't build on our multigpu machine, I had an urge to update openmpi and mpi4py.

The new package can be found under http://code.google.com/p/spkg-upload/downloads/detail?name=openmpi-1.4.3.spkg
and is tested on ubuntu 10.04

*Remark:* Before Install one has to remove other installations of openmpi or else get troubles.
The current spkg install holds a lot of remove statements a better solution would be great.
Also one has to update mpi4py.


---

Comment by maldun created at 2011-01-07 00:18:17

Changing status from new to needs_info.


---

Attachment

current spkg install


---

Comment by vbraun created at 2011-01-10 17:59:34

Thanks for updating everything!

I think you should be using `rm -f` to delete the old versions. The current `spkg-install` will fail to install if you don't already have the old openmpi lying around.

You should always use `$MAKE` because somebody might have set `MAKE=/path/gnu-make` or so. Do you need to disable parallel make? Then set `MAKE="$MAKE -j 1"`

Does mpi4py or anything else need the fortran API? If no, why not disable it in the configure. If yes, is there any way we can make it call `sage_fortran` as the compiler?


---

Comment by maldun created at 2011-01-11 12:52:42

Changing status from needs_info to needs_review.


---

Comment by maldun created at 2011-01-11 12:52:42

Replying to [comment:8 vbraun]:
> Thanks for updating everything!
> 
> I think you should be using `rm -f` to delete the old versions. The current `spkg-install` will fail to install if you don't already have the old openmpi lying around.
> 
> You should always use `$MAKE` because somebody might have set `MAKE=/path/gnu-make` or so. Do you need to disable parallel make? Then set `MAKE="$MAKE -j 1"`
> 
> Does mpi4py or anything else need the fortran API? If no, why not disable it in the configure. If yes, is there any way we can make it call `sage_fortran` as the compiler?
> 

Thanks for all the information!

I changed everything to your advices. rm worked without -f but I added it just to be sure.
Also found an unnecessary rm statement. The fortran things were already outcommented but I removed them completely, to avoid confusion.
I upload a the new spkg-install to see the difference


---

Comment by maldun created at 2011-01-11 12:53:13

new spkg-install for reference


---

Attachment

Nice! Functionality-wise it is all good. But would you mind filling in the `SPKG.txt` according to the template in the developer manual? See

http://www.sagemath.org/doc/developer/producing_spkgs.html#the-file-spkg-txt

That'll give us a place to record future changes etc. You could also add `.*~` to the `.hgignore` so that mercurial doesn't complain about emacs backup files.

Best wishes,
Volker


---

Comment by maldun created at 2011-01-11 23:41:33

Replying to [comment:10 vbraun]:
> Nice! Functionality-wise it is all good. But would you mind filling in the `SPKG.txt` according to the template in the developer manual? See
> 
> http://www.sagemath.org/doc/developer/producing_spkgs.html#the-file-spkg-txt
> 
> That'll give us a place to record future changes etc. You could also add `.*~` to the `.hgignore` so that mercurial doesn't complain about emacs backup files.
> 
> Best wishes,
> Volker

OK something went wrong with the SPKG.txt when packing, perhaps I deleted it accidentally or something else went wrong. In addition I can't upload the new version on the spkg-upload site...

You can download the corrected version now under: http://computational-sage.googlecode.com/files/openmpi-1.4.3.spkg

I hope everything is now correct, and thanks for the hint with the .hgignore!

Cheers,
Stefan


---

Comment by vbraun created at 2011-01-11 23:56:36

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2011-01-11 23:56:36

Looks great!


---

Comment by vbraun created at 2011-01-12 02:16:31

I just tested in on Solaris and the export + set variable construct seems to be a bash-ism and not portable to other shells:

```
$ export MAKE="$MAKE -j 1"
MAKE= -j 1: is not an identifier
$ MAKE="$MAKE -j 1"
$ export MAKE
```


The best fix is to change the first line of spkg-install to 

```/usr/bin/env bash
```

Almost all spkgs use that anyways.

I've made that change to the openmpi spkg and put the result here:

http://www.stp.dias.ie/~vbraun/Sage/spkg/openmpi-1.4.3.spkg

Since thats a minor change I'll leave it as positive review.

For the record, compile still fails on Solaris (as with the previous version). This issue is tracked in #8522: Optional package openmpi-1.1.4 fails to install on Solaris 10 SPARC


---

Comment by jdemeyer created at 2011-02-06 09:58:23

Resolution: fixed
