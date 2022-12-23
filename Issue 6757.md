# Issue 6757: libgcrypt in Sage is GPL 3

Issue created by migration from https://trac.sagemath.org/ticket/6757

Original creator: drkirkby

Original creation time: 2009-08-16 03:42:29

Assignee: somebody

Sage has libgcrypt version 1.4.3 in spkg/standard.

But:

http://directory.fsf.org/project/libgcrypt/

clearly shows:

1.4.3

    * Released: 21 Nov, 2008
    * Code Maturity: Stable
    * Source Archive: http://www.gnupg.org/download/index.en.html#lib...
    * Licenses: GPLv3
    * Interfaces: Command Line

The file SPKG.txt says:

## License

 * LGPL V2.1 or later (1.4 release)



---

Comment by wdj created at 2009-08-16 10:33:29

See also http://trac.sagemath.org/sage_trac/ticket/1627
When I download libcrypt-1.4.4 from http://www.gnupg.org/download/index.en.html#libgcrypt
the COPYING file indicates GPLv2 and the COPYING.LIB file indicates LGPLv2.1.

I don't see 1.4.3 there.


---

Comment by drkirkby created at 2009-08-16 12:29:43

The name of the .spkg file in Sage 4.1.1 is libgcrypt-1.4.3.p1.spkg I've made a libgcrypt-1.4.3.p2.spkg


```

drkirkby@smudge:[~/sage/suncc/sage-4.1.1/spkg/standard] $ ls -ld libgcrypt* 
-rw-r--r--   1 drkirkby other    2036701 Jul 31 22:45 libgcrypt-1.4.3.p1.spkg
-rw-r--r--   1 drkirkby other    2115840 Aug 16 12:34 libgcrypt-1.4.3.p2.spkg
drkirkby@smudge:[~/sage/suncc/sage-4.1.1/spkg/standard] $ pwd
/export/home/drkirkby/sage/suncc/sage-4.1.1/spkg/standard
drkirkby@smudge:[~/sage/suncc/sage-4.1.1/spkg/standard] $


```



---

Comment by drkirkby created at 2009-09-15 21:32:15

I guess we should go by the COPYING file. The website and the actual code disagree. I assume the code is more authorative. 

I suspect this should be closed in that case.


---

Comment by mvngu created at 2009-09-28 01:34:21

Resolution: invalid


---

Comment by mvngu created at 2009-09-28 01:34:21

I think the file COPYING in the source tarball is the authority here. So close this ticket as invalid.
