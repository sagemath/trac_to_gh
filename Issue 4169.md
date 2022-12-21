# Issue 4169: [with spkg and patch, needs review] zn_poly 0.9 and hypellfrob 2.1.1

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2008-09-22 19:02:41

Assignee: mabshoff

CC:  tabbott

Update to `zn_poly` version 0.9.

Also included is a minor patch for hypellfrob (this is necessary since hypellfrob was using `zn_poly` internals in a naughty way --- bad design on my part, and now fixed).

You need to install the spkg first, then apply the hypellfrob patch and force a rebuild (touch {{{devel/sage/sage/schemes/hyperelliptic_curves/hypellfrob.pyx if necessary).


---

Attachment


---

Comment by malb created at 2008-09-22 19:41:29

Hi David, I can review this ticket. One somehow related question: Would it make sense to use znpoly for `GF(p)['x']` and `IntegersModRing(n)['x']` ?


---

Comment by dmharvey created at 2008-09-22 21:04:03

Thanks malb.

Probably not a good idea to use it as the backend yet. I'm working on it, and that's my eventual goal, but whereas multiplication and middle product are pretty good, division support is still poor.


---

Comment by mabshoff created at 2008-09-22 23:36:58

Hi David,

did you valgrind this or will I have to do it? :)

Cheers,

Michael


---

Comment by dmharvey created at 2008-09-22 23:42:34

I valgrinded (valground?) "make check" on sage.math, but not the full "test all" and not from within sage. There was a single leak of 2500 bytes, which is in GMP's mpn_random2 function, which is not used outside the test suite.


---

Comment by malb created at 2008-09-24 11:21:27

The SPKG installs cleanly and looks good (hg status, SPKG.txt). Patch applies cleanly against 3.1.2 (I'm not on any alpha yet). `sage -tp2 sage/schemes` passes.


---

Comment by mabshoff created at 2008-09-26 08:51:33

A couple remarks:

 * Please do not attach spkgs to trac, instead link them from some webspace.
 * The version patches by Tim break on every BSD and Solaris where we do not use the GNU ld per default. We now work around this by linking gld to ld, but this is *not* a long term solution. Sage in general does not benefit from versioned libraries, indeed they case a bunch of problems when linking extensions, due to the links the archives get larger and on top of that it makes the memory address space on Cygwin even more scare, so I intend to remove every one of those version patches in the future. Those patches should be moved into the Debian packaging directory or alternatively you should provide a makefile target for not versioned libraries.
 * My OSX 64 bit fixes are not in the spkg since this one was based on 0.8.p1, not p2. Please make sure that in the future you case new spkgs on the latest one in Sage. I have fixed the OSX 64 bit missing bits in 0.9.p0 and for now left the versioned library code in makemakefile.py. I intend to remove that code in the future or add a *BSD/Solaris makefile target. Using versioned libraries should be optional.
 * Feel free to add the minimal patch that adds 64 bit OSX support to your repo. If LDFLAGS was actually used when linking on OSX we do not need a separate target like

```
+print "libzn_poly.dylib64: $(LIBOBJS)"
+print "\t$(CC) -m64 -single_module -fPIC -dynamiclib -o libzn_poly.dylib $(LIBOBJS) $(LIBS)"
+print
```


But it is late, so I will take the easy way out instead of fixing the problem the right way :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-26 09:00:14

David,

an updated spkg can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha2/zn_poly-0.9.p0.spkg

It contains the 64 bit OSX fixes and some small fixes to spkg-install. Please make sure to base your next spkg on this one ;)

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-26 09:01:35

Resolution: fixed


---

Comment by mabshoff created at 2008-09-26 09:01:35

Merged in Sage 3.1.3.alpha2


---

Comment by dmharvey created at 2008-09-26 12:18:26

Replying to [comment:7 mabshoff]:
>  * The version patches by Tim break on every BSD and Solaris 

I don't really understand the issues here, and I see malb has just opened a thread on sage-devel, so I'll leave this to the experts to thrash out, and I'll be sure to follow their recommendations in future :-)

>  * My OSX 64 bit fixes are not in the spkg since this one was based on 0.8.p1, not p2. Please make sure that in the future you case new spkgs on the latest one in Sage.

Oops, sorry about that.

david
