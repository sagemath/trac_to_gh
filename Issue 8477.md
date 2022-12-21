# Issue 8477: Force GNU make to build PALP serially

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-03-07 18:43:02

Assignee: tbd

CC:  drkirkby mvngu

PALP fails to build in parallel with GNU `make`.  Some output from `make -d` (debug):

```
    Must remake target `poly.o'.
Need a job token; we don't have children
make[2]: Entering directory `/mnt/usb1/scratch/mpatel/tmp/sage-4.3.4.alpha0-j20-par/spkg/build/palp-1.1.p2/src'
gcc -O3 -g -W -Wall -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE   -c -o poly.o poly.c
Putting child 0x00651fb0 (poly.o) PID 7703 on the chain.
    Commands of `poly.o' are being run.
    Considering target file `Coord.o'.
     File `Coord.o' does not exist.
    Must remake target `Coord.o'.
Live child 0x00651fb0 (poly.o) PID 7703 
Need a job token; we have children
Live child 0x00651fb0 (poly.o) PID 7703 
Live child 0x00651fb0 (poly.o) PID 7703 
Reaping winning child 0x00651fb0 PID 7703 
Removing child 0x00651fb0 PID 7703 from chain.
make[2]: Leaving directory `/mnt/usb1/scratch/mpatel/tmp/sage-4.3.4.alpha0-j20-par/spkg/build/palp-1.1.p2/src'
Error building PALP.
sage: An error occurred while installing palp-1.1.p2
```


It's not clear why this happens, but it breaks building spkgs in parallel (#8306).  As we've done with other packages, forcing a serial build helps.

PALP has a `Makefile` and a `GNUmakefile`.  GNU `make` prefers the latter.  It seems that `export MAKE="make"` in `spkg-install` is not enough to suppress a parallel build, but adding the special target [.NOTPARALLEL](http://www.gnu.org/software/automake/manual/make/Special-Targets.html#index-g_t_002eNOTPARALLEL-248) to `GNUmakefile` works.

Building in parallel appears to work if I replace `GNUmakefile` with `Makefile`, but the compiler and compiler flags are different.  The package does not have an [obvious] test suite.

#7071 is another PALP ticket. 


---

Comment by mpatel created at 2010-03-07 18:49:44

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-03-07 18:49:44

I've put the package at

 * http://sage.math.washington.edu/home/mpatel/trac/8477/palp-1.1.p2.spkg


---

Comment by mpatel created at 2010-03-11 03:47:28

There's a similar problem on bsd.  Simply deleting `GNUmakefile` or copying it to `Makefile` fixes it.

Maybe it'll help to fix this and #7071 together?


---

Comment by drkirkby created at 2010-03-12 12:29:19

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-03-12 12:29:19

Your changes to SPKG.txt are good, but the mention of only "GPL" did cause me to check the license. 

A look at the file src/COPYING shows only a link to the GPL, which is of course now version 3. The file does not contain the usual contents of the file COPYING. 

Looking at the history of PALP

http://hep.itp.tuwien.ac.at/~kreuzer/CY/CYpalp.html#History

I can see that version 1.1 (the latest, and the release in Sage) is dated November 2, 2006, which was before the GPL 3 existed. 

I believe SPKG.txt's license information should indicate the license is GPL2+, rather than GPL, but the reason for this needs to be given. Something along the lines of 

 * When released, GPL 2 was in force. 
 * There is a link to a web page, which now points to GPL 3, but would have pointed to GPL 2 at the time of the package was released. 
 * Therefore one can deduce the authors were happy for this to be released under GPL 2 or a later version. 

One other minor point, it would be good to remove the line:

CC=gcc

from Makefile, as that would then allow one to at least attempt to build this with any compiler. The Makefile refers to $(CC) everywhere, so since CC is set by the Sage environment, this line could be usefully removed, but I realise this is unrelated to the main part of the change, so don't bother unless you feel inclined to. 

I will need to check the changes don't break the build (I can't believe they can do any harm whatsoever, but I can't actually check them just now). But once the SPKG.txt is revised, I'll give this a positive review, subject to me checking it does not break a serial build, which will take me a minute or two. (I'll check the parallel build issues as part of the #7071). 

Perhaps you could also attach a Mercurical patch file, which makes reviewing a little easier. 

Once those changes are made, I'll check that the package builds serially. Then I'll revisit #7071, as that relies on this anyway. Hopefully this will allow #7071 to be resolved soon, as I believe that is a great enhancement, but we need to be sure it can't break anything. 

Dave


---

Comment by mpatel created at 2010-03-12 17:38:36

`mv GNUmakefile` to `Makefile`.  palp spkg patch


---

Attachment

I've updated

 * http://sage.math.washington.edu/home/mpatel/trac/8477/palp-1.1.p2.spkg

with your suggestions, except for removing `CC=gcc`.  See the attached the patch, which also has a workaround for parallel spkg builds that seems to work on sage.math and bsd (at least).  The makefiles differ by

```diff
 NEF_SRC= E_Poly.c Nefpart.c LG.c
 NEF_OBJ= $(NEF_SRC:.c=.o)
 
-CC=cc 
+CC=gcc
 
-CFLAGS=-O3 -fast
+CFLAGS=-O3 -g -W -Wall -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE
 # CFLAGS=-O3 -g                                      # add -g for GNU debugger gdb
 # CFLAGS=-Ofast -O3 -mips4 -n32                      # SGI / 32 bit
 # CFLAGS=-Ofast -O3 -mips4 -64                # SGI / 64 bit
```

Looking at the source, I think `-D_FILE_OFFSET_BITS=64` and `-D_LARGEFILE_SOURCE` are intended for 32-bit architectures.  But it appears the first definition is not used and the makefiles don't check the architecture.


---

Comment by mpatel created at 2010-03-12 17:58:02

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-03-12 18:01:25

I assume that at #7071, you'll use the Sage environment's `CC` and `CFLAGS` or set them in `spkg-install`.


---

Comment by drkirkby created at 2010-03-12 18:07:29

sage-env sets the environment variable CC to be gcc unless it is otherwise defined. 

Obviously when the package was made, the compiler as assumed to be 'cc'. Someone has then set it to gcc. The best option is to unset it in the makefile, then the Makefile will use $(CC) which Sage has set. But it is a minor issue - I will fix that at a later date. 

One of those gcc command lines look really odd - add -Wall to show all warnings, then add -W to suppress all warnings! So I'm not convinced the person that wrote that understood what they were doing! 

I'll take a look later today. I need to do a few jobs in the last remaining hours of daylight here in the UK. I can get back to the computer later today and will review this - I'm 99% sure it will be positive, but I'll convince myself first. 

dave


---

Comment by mpatel created at 2010-03-12 18:14:44

Doesn't `-W` activate extra warnings?  From the manual page for gcc 4.4.1:

```
       -Wextra
           This enables some extra warning flags that are not enabled by
           -Wall. (This option used to be called -W.  The older name is still
           supported, but the newer name is more descriptive.)
```

Anyway, whenever it's convenient is great.


---

Comment by drkirkby created at 2010-03-13 11:34:11

The revised SPKG.txt looks fine. 

This builds fine in serial mode. I've not had chance to check the much more complex #7071. That will need extensive testing I believe, but I'm convinced this part is working fine. 

Positive review.


---

Comment by drkirkby created at 2010-03-13 11:34:11

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-23 17:12:33

Merged into 4.4.alpha2.


---

Comment by jhpalmieri created at 2010-04-23 17:12:33

Resolution: fixed
