# Issue 9591: Upgrade genus2reduction to pari 2.4.3

Issue created by migration from https://trac.sagemath.org/ticket/9591

Original creator: jdemeyer

Original creation time: 2010-07-24 11:56:21

Assignee: tbd

After upgrading PARI/GP to version 2.4.3 (#9343), genus2reduction no longer compiles properly.


---

Comment by jdemeyer created at 2010-07-24 12:18:18

New version which works with PARI 2.4.3: [http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p7.spkg](http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p7.spkg)

All I had to do was to rename some functions (digging in earlier versions of PARI to see what the undefined functions meant).


---

Comment by fbissey created at 2010-07-24 18:41:19

out of curiosity what did you replace "gi" with? 

I had a hard figuring that one out when I tried to fix this myself.


---

Comment by jdemeyer created at 2010-07-24 22:28:05

Replying to [comment:2 fbissey]:
> out of curiosity what did you replace "gi" with? 

> I had a hard figuring that one out when I tried to fix this myself. 

gi should be replaced by gen_I().


---

Comment by mpatel created at 2010-08-13 01:45:52

We may need to coordinate this ticket with #9738, which is about a segfault caused by `SAGE_LOCAL/bin/genus2reduction`.


---

Comment by mpatel created at 2010-08-13 10:31:24

By the way, would it be worth it to rewrite `genus2reduction.c` in Cython and include it in the Sage library?


---

Comment by jdemeyer created at 2010-08-13 22:41:04

Replying to [comment:7 mpatel]:
> By the way, would it be worth it to rewrite `genus2reduction.c` in Cython and include it in the Sage library?

I guess it makes sense to include it in the sage library since it's just 1 file.  But I don't think it is very important.


---

Comment by jdemeyer created at 2010-08-14 20:40:29

I merged my patch from #9738. New spkg at [http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p8.spkg](http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p8.spkg)


---

Comment by jdemeyer created at 2010-08-14 20:40:29

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-08-14 22:38:51

If I'm not mistaken, it should be .p7, .p8, as the one version in sage-4.5.3.alpha0 is a .p6. 

But this fails to build on OpenSolaris 32-bit, despite the previous version working fine. 


```
drkirkby@hawk:~/32/sage-4.5.3.alpha0$ ./sage -i http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p8.spkg
Installing http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p8.spkg
Calling sage-spkg on http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p8.spkg
Warning: Attempted to overwrite SAGE_ROOT environment variable
genus2reduction-0.3.p8
Machine:
SunOS hawk 5.11 snv_134 i86pc i386 i86pc
Deleting directories from past builds of previous/current versions of genus2reduction-0.3.p8
Extracting package /export/home/drkirkby/32/sage-4.5.3.alpha0/spkg/optional/genus2reduction-0.3.p8.spkg ...
-rw-r--r--   1 drkirkby staff      53471 Aug 14 23:35 /export/home/drkirkby/32/sage-4.5.3.alpha0/spkg/optional/genus2reduction-0.3.p8.spkg
genus2reduction-0.3.p8/
genus2reduction-0.3.p8/.hg/
genus2reduction-0.3.p8/.hg/requires
genus2reduction-0.3.p8/.hg/store/
genus2reduction-0.3.p8/.hg/store/data/
genus2reduction-0.3.p8/.hg/store/data/src/
genus2reduction-0.3.p8/.hg/store/data/src/genus2reduction.c.i
genus2reduction-0.3.p8/.hg/store/data/.hgignore.i
genus2reduction-0.3.p8/.hg/store/data/dist/
genus2reduction-0.3.p8/.hg/store/data/dist/debian/
genus2reduction-0.3.p8/.hg/store/data/dist/debian/rules.i
genus2reduction-0.3.p8/.hg/store/data/dist/debian/control.i
genus2reduction-0.3.p8/.hg/store/data/dist/debian/compat.i
genus2reduction-0.3.p8/.hg/store/data/dist/debian/copyright.i
genus2reduction-0.3.p8/.hg/store/data/dist/debian/patches/
genus2reduction-0.3.p8/.hg/store/data/dist/debian/patches/series.i
genus2reduction-0.3.p8/.hg/store/data/dist/debian/patches/makefile.patch.i
genus2reduction-0.3.p8/.hg/store/data/dist/debian/control.in.i
genus2reduction-0.3.p8/.hg/store/data/dist/debian/changelog.i
genus2reduction-0.3.p8/.hg/store/data/spkg-install.i
genus2reduction-0.3.p8/.hg/store/data/_s_p_k_g.txt.i
genus2reduction-0.3.p8/.hg/store/undo
genus2reduction-0.3.p8/.hg/store/00manifest.i
genus2reduction-0.3.p8/.hg/store/00changelog.i
genus2reduction-0.3.p8/.hg/undo.dirstate
genus2reduction-0.3.p8/.hg/dirstate
genus2reduction-0.3.p8/.hg/00changelog.i
genus2reduction-0.3.p8/.hg/branch
genus2reduction-0.3.p8/.hg/undo.branch
genus2reduction-0.3.p8/src/
genus2reduction-0.3.p8/src/.pc/
genus2reduction-0.3.p8/src/.pc/.version
genus2reduction-0.3.p8/src/TODO
genus2reduction-0.3.p8/src/README
genus2reduction-0.3.p8/src/THANKS
genus2reduction-0.3.p8/src/genus2reduction.c
genus2reduction-0.3.p8/src/gpl-email.txt
genus2reduction-0.3.p8/src/SAGE.txt
genus2reduction-0.3.p8/src/RELEASE.NOTES
genus2reduction-0.3.p8/src/WARNING
genus2reduction-0.3.p8/src/INSTALL
genus2reduction-0.3.p8/src/CHANGES
genus2reduction-0.3.p8/src/COPYING
genus2reduction-0.3.p8/dist/
genus2reduction-0.3.p8/dist/debian/
genus2reduction-0.3.p8/dist/debian/control
genus2reduction-0.3.p8/dist/debian/rules
genus2reduction-0.3.p8/dist/debian/changelog
genus2reduction-0.3.p8/dist/debian/compat
genus2reduction-0.3.p8/dist/debian/control.in
genus2reduction-0.3.p8/dist/debian/patches/
genus2reduction-0.3.p8/dist/debian/patches/makefile.patch
genus2reduction-0.3.p8/dist/debian/patches/series
genus2reduction-0.3.p8/dist/debian/copyright
genus2reduction-0.3.p8/.hgignore
genus2reduction-0.3.p8/SPKG.txt
genus2reduction-0.3.p8/spkg-install
Finished extraction
****************************************************
Host system
uname -a:
SunOS hawk 5.11 snv_134 i86pc i386 i86pc
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/local/gcc-4.5.0/libexec/gcc/i386-pc-solaris2.10/4.5.0/lto-wrapper
Target: i386-pc-solaris2.10
Configured with: ../gcc-4.5.0/configure --prefix=/usr/local/gcc-4.5.0 --build=i386-pc-solaris2.10 --enable-languages=c,c++,fortran --with-gmp=/usr/local/gcc-4.5.0 --with-mpfr=/usr/local/gcc-4.5.0 --disable-nls --enable-checking=release --enable-werror=no --enable-multilib -with-system-zlib --enable-bootstrap --with-gnu-as --with-as=/usr/local/binutils-2.20/bin/as --without-gnu-ld --with-ld=/usr/ccs/bin/ld
Thread model: posix
gcc version 4.5.0 (GCC) 
****************************************************
Compiling genus2reduction.c
genus2reduction.c:32:1: error: expected identifier or '(' before 'long'
genus2reduction.c:32:1: error: expected ')' before '>' token
genus2reduction.c:39:1: error: expected identifier or '(' before 'long'
genus2reduction.c:39:1: error: expected ')' before '>' token
genus2reduction.c: In function 'main':
genus2reduction.c:494:27: error: called object 'pol_1' is not a function
genus2reduction.c:545:24: error: called object 'pol_1' is not a function
genus2reduction.c:618:37: error: called object 'pol_x' is not a function
genus2reduction.c:618:55: error: called object 'pol_x' is not a function
genus2reduction.c:676:46: error: called object 'pol_x' is not a function
genus2reduction.c:692:46: error: called object 'pol_x' is not a function
genus2reduction.c:741:44: error: called object 'pol_x' is not a function
genus2reduction.c:770:42: error: called object 'pol_x' is not a function
genus2reduction.c: In function 'factorpadicnonun':
genus2reduction.c:1685:37: error: subscripted value is neither array nor pointer
genus2reduction.c:1694:58: error: called object 'pol_x' is not a function
genus2reduction.c:1695:54: error: called object 'pol_x' is not a function
genus2reduction.c:1695:7: warning: passing argument 1 of 'gsubst' makes pointer from integer without a cast
/export/home/drkirkby/32/sage-4.5.3.alpha0/local/include/pari/paridecl.h:1138:9: note: expected 'GEN' but argument is of type 'int'
genus2reduction.c: In function 'polymini':
genus2reduction.c:1719:28: error: called object 'pol_x' is not a function
genus2reduction.c:1719:59: error: called object 'pol_x' is not a function
genus2reduction.c:1734:46: error: called object 'pol_x' is not a function
genus2reduction.c:1753:33: error: called object 'pol_x' is not a function
genus2reduction.c:1762:34: error: called object 'pol_x' is not a function
genus2reduction.c:1774:42: error: called object 'pol_x' is not a function
genus2reduction.c:1783:31: error: called object 'pol_x' is not a function
genus2reduction.c:1789:47: error: called object 'pol_x' is not a function
genus2reduction.c: In function 'discpart':
genus2reduction.c:1836:13: error: called object 'pol_1' is not a function
genus2reduction.c: In function 'polyminizi':
genus2reduction.c:1874:3: warning: passing argument 2 of 'gadd' makes pointer from integer without a cast
/export/home/drkirkby/32/sage-4.5.3.alpha0/local/include/pari/paridecl.h:1014:9: note: expected 'GEN' but argument is of type 'int'
genus2reduction.c:1877:32: error: called object 'pol_x' is not a function
genus2reduction.c:1882:46: error: called object 'pol_x' is not a function
genus2reduction.c:1900:38: error: called object 'pol_x' is not a function
genus2reduction.c: In function 'polyminizi2':
genus2reduction.c:1956:39: error: called object 'pol_x' is not a function
genus2reduction.c:1959:68: warning: assignment makes pointer from integer without a cast
genus2reduction.c:1969:32: error: called object 'pol_x' is not a function
genus2reduction.c:1974:46: error: called object 'pol_x' is not a function
genus2reduction.c: In function 'zi2mod':
genus2reduction.c:2018:3: warning: passing argument 2 of 'gmul' makes pointer from integer without a cast
/export/home/drkirkby/32/sage-4.5.3.alpha0/local/include/pari/paridecl.h:1018:9: note: expected 'GEN' but argument is of type 'int'
Error building genus2reduction

real	0m0.069s
user	0m0.052s
sys	0m0.014s
sage: An error occurred while installing genus2reduction-0.3.p8
```



---

Comment by drkirkby created at 2010-08-14 22:38:51

Changing status from needs_review to needs_work.


---

Comment by fbissey created at 2010-08-15 00:24:26

I had that when making the ebuild for gentoo earlier. You are not compiling it
against pari-2.4.xx - that's what the problem is.


---

Comment by drkirkby created at 2010-08-15 02:22:02

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-08-15 02:22:02

Replying to [comment:12 fbissey]:
> I had that when making the ebuild for gentoo earlier. You are not compiling it
> against pari-2.4.xx - that's what the problem is.

Yes, sorry, my mistake. 

I've stuck it back to "needs review". I dn't feel able to review it, but after installing the pari package, this installs cleanly. 

*I've only tested on OpenSolaris x64 as a 32-bit binary* - so I have not tested on Solaris SPARC (e.g. t2)

Dave


---

Comment by jdemeyer created at 2010-08-15 06:47:11

Replying to [comment:11 drkirkby]:
> If I'm not mistaken, it should be .p7, .p8, as the one version in sage-4.5.3.alpha0 is a .p6. 

Well, there has been a .p7 on this ticket for a while, even if it was never actually distributed by Sage.  In my opinion it makes sense to call this .p8 then.


---

Comment by fbissey created at 2010-08-15 07:20:19

Replying to [comment:14 jdemeyer]:
> Replying to [comment:11 drkirkby]:
> > If I'm not mistaken, it should be .p7, .p8, as the one version in sage-4.5.3.alpha0 is a .p6. 
> 
> Well, there has been a .p7 on this ticket for a while, even if it was never actually distributed by Sage.  In my opinion it makes sense to call this .p8 then.

I think Dave is right strictly speaking, but having .p8 means an easier time for people working on the pari issue to upgrade it. And now that I have updated my own package (after I had created a .p7 less than 12 hours beforehand) for Gentoo I'd like it to stay at that number - if possible.


---

Comment by mpatel created at 2010-08-19 11:13:49

Changing priority from major to blocker.


---

Attachment

Complete spkg patch (for reference)


---

Comment by mpatel created at 2010-08-31 00:39:49

I can give a positive review to the "EOF" part of [attachment:ticket:9738:9738_genus2reduction_init_opts.patch Jeroen's patch] from #9738.  With the prerequisites given at [NewPARI](http://wiki.sagemath.org/NewPARI), I get no dumped cores on bsd, redhawk, sage, and t2.math.

Unfortunately, I'm not qualified to review the rest of the patch, since I'm not familiar with the mathematics or PARI's API.


---

Comment by mpatel created at 2010-08-31 00:50:01

Replying to [comment:18 mpatel]:
> I can give a positive review to the "EOF" part of [attachment:ticket:9738:9738_genus2reduction_init_opts.patch Jeroen's patch] from #9738.  With the prerequisites given at [NewPARI](http://wiki.sagemath.org/NewPARI), I get no dumped cores on bsd, redhawk, sage, and t2.math.

Specifically, I get no dumped cores from running `genus2reduction` and testing `sage/interfaces/genus2reduction.py`.  There are still unrelated cores stemming probably from the doctesting system (cf. [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/0239f712a39fce4a/ba4e7b77e4de1b10?#ba4e7b77e4de1b10), #9739).


---

Comment by fbissey created at 2010-08-31 02:27:47

While I wouldn't claim to be a pari specialist, I had a look at updating genus2reduction myself. I didn't fell confident about giving a positive review because I don't understand the "EOF" part but I am willing to give a positive review to the rest.


---

Comment by mpatel created at 2010-09-02 10:22:26

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-09-03 23:15:39

The `dist/` directory should be removed (see #5903).

Then I can revert it to "positive review"... :)


---

Comment by leif created at 2010-09-03 23:15:39

Changing status from positive_review to needs_work.


---

Attachment

Remove `dist/`.  spkg patch.  Apply on top of "complete" patch.


---

Comment by mpatel created at 2010-09-04 07:24:42

I've a put an updated package at

 http://sage.math.washington.edu/home/mpatel/trac/9591/genus2reduction-0.3.p8.spkg


---

Comment by mpatel created at 2010-09-04 07:24:42

Changing status from needs_work to needs_review.


---

Comment by leif created at 2010-09-04 09:17:25

Ok, I've really looked at the new spkg. ;-)

The changelog in `SPKG.txt` cites #9738 for the removal, but never mind. (The commit message is correct.)

Reverting to *"positive review"*.

Mitesh, could you update the link on the NewPARI wiki page?


---

Comment by leif created at 2010-09-04 09:17:25

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-04 09:22:45

Replying to [comment:24 leif]:
> Mitesh, could you update the link on the NewPARI wiki page?

Done.


---

Attachment

New complete patch including trac_9591-g2red_remove_dist.patch


---

Comment by mpatel created at 2010-09-10 10:39:31

Resolution: fixed
