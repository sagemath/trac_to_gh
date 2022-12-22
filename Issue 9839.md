# Issue 9839: link-editor thinks ECL library contains non-pic code on *all* 64-bit Solaris/OpenSolaris releases

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-08-30 12:11:30

Assignee: drkirkby

As noted at #9099, Maxima fails to build properly on OpenSolaris x64. The ticket then went onto discuss specific doctest failures on 32-bit Solaris n x86. 

However, the reason Maxima was not working on OpenSolaris is totally unrelated and  *much* wider. It has nothing to do with Maxima, but is almost certainly an issue with ECL. 

Hence it seemed wise to open a ticket specific for this. 

The problem is that the link-editor thinks the ecl shared library contains text relocations, which is why there was an error like 



```
ld.so.1: ecl: fatal: relocation error: R_AMD64_PC32: file /export/home/drkirkby/sage-4.4.2/local/lib//libecl.so: symbol main: value 0x22800097de04 does not fit
```


There's a command given on this Sun blog

http://blogs.sun.com/rie/entry/my_relocations_don_t_fit

which will show libraries with this problem. 

 == OpenSolaris on x64 ==

I built the latest ECL snapshot outside of Sage, and run the suggested command on the ECL library. Note, this a different version of ECL built at a later date. 


```
drkirkby`@`hawk:/tmp/ecl$ ./configure 
drkirkby`@`hawk:/tmp/ecl$ make
```


then the all important: 


```
drkirkby`@`hawk:/tmp/ecl$ elfdump -d ./build/libecl.so |  fgrep TEXTREL
      [23]  TEXTREL           0
      [31]  FLAGS             0x4                 [ TEXTREL ]

```

which indicates a problem - there should be no output from that. 

It's also suggested to compile with some debugging information:


```
$ export LD_OPTIONS=-Dreloc,detail 
$ unset MAKE
$ make
```


A full log is attached of that.


---

Attachment

Build log on OpenSolaris, when using debugging options to show text relocations.


---

Comment by drkirkby created at 2010-09-16 10:03:41

It should be noted this problem exists on every combination of Solaris/OpenSolaris system tested

 * 32-bit Solaris 10 on SPARC
 * 64-bit Solaris 10 on SPARC
 * 32-bit Solaris 10 on x86
 * 64-bit Solaris 10 on x86
 * 32-bit OpenSolaris on x86
 * 64-bit OpenSolaris on x86

However, on 32-bit builds, the text relocation issues are not actually causing any problems, so we can live with that. On 64-bit builds, it completely screws things up. 

Similar issues with text relocation has been observed with: 

 * Cliquer - solved with a change of compiler flags (#9871)
 * PolyBoRi - solved in the latest upstream release (#9872)
 * R - unsolved (#9040)

So it's only R and ECL which have this problem outstanding. 

Dave


---

Comment by drkirkby created at 2010-11-09 09:18:28

This has ben fixed upstream, and is the result of using a GCC extension (computed gotos), which don't seem to work properly on Solaris. As yet, I am unaware what the fix is, though I've been told its been fixed. 

Dave


---

Comment by drkirkby created at 2011-04-02 12:30:46

This problem was fixed by #10766, so can be closed as fixed in sage-4.7.alpha1


---

Comment by jdemeyer created at 2011-04-05 15:55:34

Resolution: duplicate
