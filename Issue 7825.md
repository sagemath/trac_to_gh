# Issue 7825: pari-2.3.3.p5 compilation fails on FreeBSD/amd64

Issue created by migration from https://trac.sagemath.org/ticket/7825

Original creator: pjeremy

Original creation time: 2010-01-03 02:26:54

Assignee: pjeremy

CC:  drkirkby was craigcitro

FreeBSD refers to the x86_64 architecture under its original name of 'amd64' so use this as an alias for x86_64.  The `-fPIC' fix is needed to correct:

```
gcc  -o libpari-gmp.so.2.3.3 -shared  -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer  -Wl,-shared,-soname=libpari-gmp.so.2 mp.o mpinl.o Flx.o Qfb.o RgX.o alglin1.o alglin2.o arith1.o arith2.o base1.o base2.o base3.o base4.o base5.o bibli1.o bibli2.o buch1.o buch2.o buch3.o buch4.o galconj.o gen1.o gen2.o gen3.o ifactor1.o perm.o polarit1.o polarit2.o polarit3.o rootpol.o subcyclo.o subgroup.o trans1.o trans2.o trans3.o anal.o compat.o default.o errmsg.o es.o init.o intnum.o members.o sumiter.o aprcl.o elldata.o elliptic.o galois.o groupid.o kummer.o mpqs.o nffactor.o part.o stark.o subfield.o thue.o -lc -lm -L/home/peter/sage/sage-4.3/local/lib -lgmp 
/usr/bin/ld: mp.o: relocation R_X86_64_32S can not be used when making a shared object; recompile with -fPIC
mp.o: could not read symbols: Bad value
*** Error code 1

Stop in /home/peter/sage/sage-4.3/spkg/build/pari-2.3.3.p5/src/Ofreebsd-amd64.
```



---

Attachment


---

Comment by drkirkby created at 2010-01-03 03:28:30

Hi Peter, 

Thank you for cc'ing me. 

The fix looks like it will resolve the FreeBSD issue, but there is an obvious problem with the SPARC platform on that line, as -fPIC will be selected there too, which may not always be appropriate. 

If #7818 gets implemented, it will add a variable FPIC_FLAG which could be set once for any compiler. I don't know if you could change this so spkg-install has something like


```
FPIC_FLAG=-fPIC
```

then use $FPIC_FLAG in pari-2.3.3.p5/patches/get_dlcflags. 

That way, it should work today, and with simple removal of the one line from spkg-install, this could work with any compiler. 

Oh why was there never a standard for compiler flags! Life would be so much easier. 

Dave


---

Comment by pjeremy created at 2010-01-03 03:50:19

Reported upstream as http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1022.

Regarding Dave's comment above, get_dlcflags is part of pari and already has checks for GNU vs Sun CC.  My patch is inside a 'if test -n "$__gnuc__"' block.  If this test fails then '-KPIC' will be used on Solaris/SPARC.  I agree that #7818 represents a more general solution that would simplify get_dlcflags.


---

Comment by pjeremy created at 2010-01-03 03:50:19

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-01-03 04:01:21

That looks good to me then. 

I'll give that positive review. 

BTW, I see you have __gnuc__ underlined in your comments. I assume you meant to put !__gnuc!__ The trick to avoiding the underlining is to put exclamation marks before the occurrence of the two underscores. Hence you need to do it twice here. That used to drive me round the twist sometimes, but I finally found out how to escape things like that. It also allows one to write VirtualBox without it comping out as VirtualBox, which I find a bit annoying. 

Dave


---

Comment by drkirkby created at 2010-01-03 04:01:21

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-04 07:14:28

Resolution: fixed


---

Comment by mhansen created at 2010-01-04 07:14:28

I've made an SPKG out of this fix and merged it in 4.3.1.alpha0.  The spkg can be found at http://sage.math.washington.edu/home/mhansen/pari-2.3.3.p6.spkg


---

Comment by drkirkby created at 2010-01-05 22:04:56

I note the date in SPKG.txt was 2009 and not 2010. I'm just about to update this again, due to the SAGE64 issues (#7133), so I'll correct that then.
