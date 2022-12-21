# Issue 8645: maxima package fails to install ECL library

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2010-04-02 22:58:34

Assignee: AlexGhitza

CC:  nbruin was mvngu mpatel jdemeyer

Keywords: maxima, ecl

With the recent ECL update #8275, maxima package doesn't install the ECL library (which was added in #7287). The library is built, but put in an unexpected location. Here is the end of the log:


```
;;; Note: Invoking external command:
;;;   ranlib /home/burcin/.cache/common-lisp/ecl-10.2.1-linux-x86-64/home/burcin/sage/sage-4.3.2/spkg/build/maxima-5.20.1/src/src/libmaxima.a
;;; Note: Invoking external command:
;;;   gcc "-I/home/burcin/sage/sage-4.3.2/local/include/"  -I/home/burcin/sage/sage-4.3.2/local/include -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64  -O2  -g  -Wall  -fPIC  -Dlinux -O -w -c "/tmp/ECLINITEsuxJJ.c" -o "/tmp/ECLINITEsuxJJ.o"
;;; Note: Invoking external command:
;;;   gcc -o "/home/burcin/.cache/common-lisp/ecl-10.2.1-linux-x86-64/home/burcin/sage/sage-4.3.2/spkg/build/maxima-5.20.1/src/src/maxima.fasb" -L"/home/burcin/sage/sage-4.3.2/local/lib/" "/tmp/ECLINITEsuxJJ.o" "/home/burcin/.cache/common-lisp/ecl-10.2.1-linux-x86-64/home/burcin/sage/sage-4.3.2/spkg/build/maxima-5.20.1/src/src/libmaxima.a"   -shared  -L/home/burcin/sage/sage-4.3.2/local/lib  -L/home/burcin/sage/sage-4.3.2/local/lib  -lecl  -lgmp -lgc -ldl  -lm 
installing Maxima library as /home/burcin/sage/sage-4.3.2/local/lib/ecl//maxima.fas
cp: cannot stat `maxima.fasb': No such file or directory

real    3m15.250s
user    2m34.586s
sys     0m19.645s
Successfully installed maxima-5.20.1
```


Note that the return value of the cp command is not checked.

The files are here:


```
burcin`@`karr ~/sage/sage-4.3.2 $ ls ~/.cache/common-lisp/ecl-10.2.1-linux-x86-64/home/burcin/sage/sage-4.3.2/spkg/build/maxima-5.20.1/src/src/
libmaxima.a  maxima.fasb  
```


Any ideas why?


---

Comment by burcin created at 2010-04-10 09:44:27

Changing assignee from AlexGhitza to tbd.


---

Comment by burcin created at 2010-04-10 09:44:27

Changing component from algebra to packages.


---

Comment by nbruin created at 2010-04-13 22:07:14

I checked and between maxima 5.19 and maxima 5.20 none of the "lisp" files have changed in src/src, so it seems very unlikely that the change in location of maxima.fasb is due to the maxima upgrade.

On the other hand, between ECL 9 and ECL 10, there seems to be a lot of activity in the ASDF module, which is responsible for the building:

http://ecls.cvs.sourceforge.net/viewvc/ecls/ecl/src/CHANGELOG?view=markup

so I can easily believe that the cause is here.

In particular, they are advertising a new option ":move-here" which allows the destination to be specified. I tried this with the presently packaged ECL 10.2.1 without luck, so perhaps upgrading ECL would be a good idea (and then hope they don't touch ASDF for a while).

On the plus side: The "fasb" file type is always recognised by ECL 10.4.2, so the ugly (and risky?) renaming should not be necessary anymore.

If after upgrading you still can't manage getting maxima.fasb in a sane location, perhaps drop Juanjo a line.


---

Comment by nbruin created at 2010-04-14 06:27:28

This may be of some help. I tried building with ECL 10.4.1. As announced in
http://groups.google.com/group/sage-devel/browse_thread/thread/e094589b2d99be8a/ab26bd29b3a8990a
we need a patch (attached there) to Maxima 5.20.1 to let it build.

The following instruction *should* do the trick

```
(require 'asdf)
(load "maxima-build.lisp")
(asdf:make-build :maxima :type :fasl :move-here ".")
```

but for me they lead to an error

```
Cannot rename the file #P"/home/nbruin/.cache/common-lisp/ecl-10.4.1-linux-x86-64/usr/local/sage/4.3.4/spkg/build/maxima-5.20.1/src/src/maxima.fasb" to #P"/usr/local/sage/4.3.4/spkg/build/maxima-5.20.1/src/src/maxima.fasb".
Explanation: Invalid cross-device link.
```

This error message indicates:
 * that ECL is trying to do exactly the right thing
 * that it's trying to do the move with a hard link, which it shouldn't try. That's a straightforward error, which will probably be fixed in ECL 10.4.2.

So my guess is that this issue should be fixable quite soon by upgrading.

Oh, and the line

```
cp maxima.fasb $ECLLIB/maxima.fas
```

should be changed to

```
cp maxima.fasb $ECLLIB || echo "Failed to build maxima.fasb"; exit 1
```

so that errors like this get caught next time and because ECL 10.4 supposedly natively recognizes .fasb files.


---

Comment by nbruin created at 2010-04-14 15:58:41

This should solve the problem:

```
mkdir ./lisp-cache
```

then in lisp:

```
(require 'asdf)
(setf asdf::*user-cache* (truename "./lisp-cache"))
(load "maxima-build.lisp")
(asdf:make-build :maxima :type :fasl :move-here ".")
```


 * this directory is guaranteed to be on the same file system
 * the cache is not accidentally on a slower (/home) file system
 * the cache gets wiped when spkg/build/maxima-5.20.1 does.
 * no interference with a possible cache that the user privately might have in ecl

So, what needs to be done is:

 * upgrade to ecl 10.4.1
 * patch Maxima to build with ecl 10.4.1
 * patch maxima's spkg-install with the above changes so that maxima.fasb gets built in the right place.


---

Comment by nbruin created at 2010-04-15 05:41:28

patch for ecl-10.4.1.spkg


---

Attachment

patch for maxima-5.20.1.p1.spkg


---

Comment by nbruin created at 2010-04-15 05:48:00

Changing status from new to needs_review.


---

Comment by nbruin created at 2010-04-15 05:48:00

Updated spkgs up at

http://sage.math.washington.edu/home/nbruin/ecl-10.4.1.spkg

http://sage.math.washington.edu/home/nbruin/maxima-5.20.1.p1.spkg

I haven't extensively tested them but at least on sage.math they seem to work and changes are small otherwise. Someone probably wants to test maxima on ecl-10.4.1 extensively (although maxima is part of the regular ecl buildfarm testsuite)

For reference, I have also attached the patches for the spkgs. _These are already applied to the above spkgs_.


---

Comment by jason created at 2010-04-20 19:32:53

The maxima package at #8731 supersedes the maxima spkg here.


---

Comment by jason created at 2010-05-13 03:24:32

Does this ECL package fix #7690?  The ecl update at #8808 claims to fix #7690.


---

Comment by jason created at 2010-05-13 04:16:44

The src/ directory in the ecl spkg on this ticket is not the same as the ECL official sources (this spkg is missing several directories, like "src/contrib/encodings" and "src/msvc".  So I think #8808's ecl spkg supersedes the ecl spkg on this ticket.

So with that, I think this ticket should be closed, as the two spkgs listed on it are superseded elsewhere.


---

Comment by mvngu created at 2010-05-13 07:28:24

Resolution: invalid


---

Comment by jason created at 2010-05-14 17:25:22

My apologies--#8808 was actually in error, and this spkg was correctly made.  I've corrected the mistake on #8951.  So really, this ticket should be closed as fixed, and #8808 should be closed as invalid.


---

Comment by mvngu created at 2010-05-14 21:32:09

Resolution changed from invalid to fixed


---

Comment by nbruin created at 2010-06-16 00:43:01

Resolution changed from fixed to 


---

Comment by nbruin created at 2010-06-16 00:43:01

This ticket was not merged in 4.4.2, so I'm reopening. The ecl spkg on #8951 supersedes the one here. However, the maxima spkg on #8731 is listed as "needs work" so declaring that the spkg there supersedes the one here is a bit premature. The only change in 

http://sage.math.washington.edu/home/nbruin/maxima-5.20.1.p1.spkg

is to the way that maxima.fasb get built, copied and its existence tested, so reviewing that should be quick.


---

Comment by nbruin created at 2010-06-16 00:43:01

Changing status from closed to new.


---

Comment by nbruin created at 2010-06-16 00:43:16

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-06-18 17:09:25

I'm just building sage-4.4.4.alpha1 on Solaris 10 SPARC and will test this as soon as that is finished. What other machines has it been tested on? 

I can't spend any more time on this just now - my wife wants me to do something which is going to take a few hours. 

I think it is sensible to upgrade the maxima in this way, but there are various small changes to ECL which could (should) be merged into the ecl update. 

Would you consider making merging these patches 

 * On #8951, the patch which removes the tmp files and has a minor (really cosmetic) changes to spkg-install. The removal of the tmp files is quite important, as it often stops builds on 't2'
 * On #8089 the patch to disable assembly code on OpenSolaris
 * On #9187 the patch to allow parallel building of .spkgs. 

I think if a new .spkg with ECL 10.4.1 is created, and the Maxima changed to work properly with that, then these should be merged. Then hopefully the maxima update can be separated. 

One of the issues I will have reviewing this is the fact I don't know lisp, but I doubt many people will so I will do my best. 

But just now I need to do other things. 

Dave


---

Comment by nbruin created at 2010-06-21 06:11:37

If #9264 gets merged then this ticked can be closed as resolved.


---

Comment by drkirkby created at 2010-06-21 09:13:52

Replying to [comment:16 nbruin]:
> If #9264 gets merged then this ticked can be closed as resolved.

Are you sure that is correct? #9264 only makes changes to ECL, not Maxima. So the revised Maxima package at  http://sage.math.washington.edu/home/nbruin/maxima-5.20.1.p1.spkg must still be merged. What does not need merging is the ECL patch attached here, as that is covered by #9264


Dave


---

Comment by nbruin created at 2010-06-21 18:00:22

Replying to [comment:17 drkirkby]:

> Are you sure that is correct? #9264 only makes changes to ECL, not Maxima.

Except for the "Important" section and the comment in the positive review. Only upgrading ECL will lead to maxima not building, so no doctests will pass. A successful merge has to include a change to maxima.

(incidentally, on #9264 it would have helped a lot if you had also run "make test" or "make ptest" after the successful build. One of the issues on #8731 was that it people were unsure whether the doctest failures were due to the ECL upgrade or the maxima upgrade. We now know it's just due to maxima 5.21 behaving differently)


---

Comment by drkirkby created at 2010-06-21 20:15:29

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-06-21 20:15:29

Replying to [comment:18 nbruin]:
> Replying to [comment:17 drkirkby]:
> 
> > Are you sure that is correct? #9264 only makes changes to ECL, not Maxima.
> 
> Except for the "Important" section and the comment in the positive review. Only upgrading ECL will lead to maxima not building, so no doctests will pass. A successful merge has to include a change to maxima.


That was my point - upgrading just ECL would not have worked. 
 
> (incidentally, on #9264 it would have helped a lot if you had also run "make test" or "make ptest" after the successful build. One of the issues on #8731 was that it people were unsure whether the doctest failures were due to the ECL upgrade or the maxima upgrade. We now know it's just due to maxima 5.21 behaving differently)

OK, point taken. 

It would be good if there was a list of doc tests associated with each package, so its possible to quickly test if changes break any tests. 

Anyway, positive review. 

 == Note to release manager ==
This ticket, and #9264 need to be merged together. Merging  #9264 without this one will cause problems. 
Dave 

Dave


---

Comment by rlm created at 2010-06-25 15:46:17

Applied http://sage.math.washington.edu/home/nbruin/maxima-5.20.1.p1.spkg


---

Comment by rlm created at 2010-06-25 15:46:17

Resolution: fixed


---

Comment by mpatel created at 2010-07-09 06:53:48

Could any of the changes here be related to the problems at #9460?


---

Comment by drkirkby created at 2010-07-09 08:51:08

Replying to [comment:21 mpatel]:
> Could any of the changes here be related to the problems at #9460?
Possibly, though I don't recall seeing reports of this against sage-4.5.alpha0, which was when this ticket was merged. 

Dave


---

Comment by rlm created at 2010-07-09 09:04:39

Replying to [comment:22 drkirkby]:
> Replying to [comment:21 mpatel]:
> > Could any of the changes here be related to the problems at #9460?
> Possibly, though I don't recall seeing reports of this against sage-4.5.alpha0, which was when this ticket was merged. 

William, AFAIK, reported those failures on the first alpha in the 4.5 series that he tested. So it is quite possible.


---

Comment by drkirkby created at 2010-07-09 09:18:48

Replying to [comment:23 rlm]:
> Replying to [comment:22 drkirkby]:
> > Replying to [comment:21 mpatel]:
> > > Could any of the changes here be related to the problems at #9460?
> > Possibly, though I don't recall seeing reports of this against sage-4.5.alpha0, which was when this ticket was merged. 
> 
> William, AFAIK, reported those failures on the first alpha in the 4.5 series that he tested. So it is quite possible.

In which case reverting this would be sensible, though it we be good if we could if we could find the circumstances in which the problem occurs - there is a note that it may occur only if Sage is built from a script. 

Dave


---

Comment by mpatel created at 2010-07-09 23:29:36

It seems that there are unchecked in changes in the spkg:

```sh
$ tar xvf sage-4.5.alpha4/spkg/standard/maxima-5.20.1.p1.spkg
$ cd maxima-5.20.1.p1
$ hg stat
? patches/defsystem.lisp
? patches/ecl-port.lisp
```



---

Comment by rlm created at 2010-07-11 19:13:57

Changing status from closed to new.


---

Comment by rlm created at 2010-07-11 19:13:57

Resolution changed from fixed to 


---

Comment by drkirkby created at 2010-09-17 00:47:44

This is marked as minor, but I've found it causes Maxima to fail to install on bsd.math, so it breaks the build. 


```
;;;   gcc -o "/Users/kirkby/sage-4.5.alpha1/spkg/build/maxima-5.20.1.p1/src/src/ECL001STjrNf.fas" -L"/Users/kirkby/sage-4.5.alpha1/local/lib/" "/Users/kirkby/sage-4.5.alpha1/spkg/build/maxima-5.20.1.p1/src/src/ECL001STjrNf.o"   -bundle  -L/Users/kirkby/sage-4.5.alpha1/local/lib -m64   -L/Users/kirkby/sage-4.5.alpha1/local/lib -m64   -lffi -lecl  -lgmp   -lm 
; loading system definition from
; /Users/kirkby/sage-4.5.alpha1/spkg/build/maxima-5.20.1.p1/src/src/maxima.asd
; into #<ASDF0 package>
;;; Loading "/Users/kirkby/sage-4.5.alpha1/spkg/build/maxima-5.20.1.p1/src/src/maxima.asd"
; registering #<SYSTEM :MAXIMA 4321128880> as MAXIMA
An error occurred during initialization:
Unknown keyword :MOVE-HERE.

installing Maxima library as /Users/kirkby/sage-4.5.alpha1/local/lib/ecl//maxima.fas
cp: cannot stat `maxima.fasb': No such file or directory
***********************************************************
Failed to install maxima.fasb as a library
***********************************************************

real	4m45.305s
user	3m35.767s
sys	0m41.909s
sage: An error occurred while installing maxima-5.20.1.p1
```


That's not a minor problem to me, if it stops Sage building.


---

Comment by drkirkby created at 2010-09-17 00:47:44

Changing priority from minor to major.


---

Comment by nbruin created at 2010-09-18 03:17:26

Replying to [comment:28 drkirkby]:

```
> Unknown keyword :MOVE-HERE.
> 
> installing Maxima library as /Users/kirkby/sage-4.5.alpha1/local/lib/ecl//maxima.fas
> cp: cannot stat `maxima.fasb': No such file or directory
> ***********************************************************
> Failed to install maxima.fasb as a library
> ***********************************************************
> 
> real	4m45.305s
> user	3m35.767s
> sys	0m41.909s
> sage: An error occurred while installing maxima-5.20.1.p1
```

The package maxima-5.20.1.p1 is designed to be built on ecl 10.4.1 or later. In order to use the :MOVE-HERE keyword, I had to upgrade to ecl 10.4.1.

I think sage is still shipping maxima-5.20.1.p0 with ecl 10.2.1, which silently fails to build maxima.fasb. Hence the original filing as "minor": a library that by default isn't used silently fails to build.


---

Comment by drkirkby created at 2010-09-18 12:18:17

Thank you, it seem whenever we need to update we need to 

 * Update maxima
 * Update ecl
 * Update the doctests

which is a bit annoying. It often does not seem possible to update ecl or maxima independently.


---

Comment by nbruin created at 2010-09-20 17:05:15

I don't think that is true. I think maxima-5.20.1.p0 will build an executable on ecl 10.4.1 and will silently fail to build maxima.fasl, just as it does on ecl 10.2.1. Furthermore, I think maxima-5.20.1 on ecl 10.2.1 produces the same output as on 10.4.1 (given that the only changes between .p0 and .p1 had to do with building a by default unused library)

The fact that doctests for maxima have to be adjusted is a good thing. A bunch of those detect error conditions that are not errors in newer versions of maxima.

But in general, you'd expect dependent packages to be - you know - dependent :-).


---

Comment by nbruin created at 2010-09-21 17:21:23

Replying to [comment:31 nbruin]:
> I don't think that is true. I think maxima-5.20.1.p0 will build an executable on ecl 10.4.1
Sorry, I take that back. That must have been before coffee. The point of ".p1" was to fix library building and detect failure of it, but in the process needed an ecl upgrade (because 10.2.1 was a snapshot of the building system in flux), which required further patches to maxima (announced and supplied by Juanjo -- Maxima is part of the ECL test suite, so he knows when Maxima/ECL breaks)


---

Comment by leif created at 2010-09-24 12:42:07

Replying to [comment:31 nbruin]:
> But in general, you'd expect dependent packages to be - you know - dependent :-).

Yes, but the current Sage build (and upgrade) process doesn't really reflect this... ;-)

(We use `make`, but `sage-spkg` usually just reports a dependent package was already installed; our current scheme lacks version requirements almost completely.)

For the _rebuild dependent packages on upgrade_ issue, there's #9896 (needs review; not limited to MacOS X). :)


---

Comment by zimmerma created at 2010-09-27 09:07:46

#9538 might depend on that ticket.

Paul


---

Comment by kcrisman created at 2010-11-18 16:25:14

#10187 should fix this.


---

Comment by kcrisman created at 2011-01-19 21:09:57

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-01-19 21:09:57

To release manager: #10187 was closed quite a while ago, and there it is confirmed that this should close this.  Thanks!


---

Comment by jdemeyer created at 2011-01-19 22:11:35

Resolution: duplicate
