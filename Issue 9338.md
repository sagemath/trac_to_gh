# Issue 9338: upgrade PyCrypto to upstream 2.1.0

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-06-25 19:24:19

Assignee: tbd

As the subject says. The latest version also fixes the issue with ARC2 reported at http://www.securityfocus.com/bid/33674/info. Currently, the PyCrypto spkg maintains patches for this issue. Upgrading to the latest upstream version would mean we no longer need to maintain those patches in the spkg itself.


---

Comment by mvngu created at 2010-06-25 20:16:43

I'm still testing this spkg, so it's not ready for review.


---

Comment by mvngu created at 2010-06-26 10:43:07

The test results are summarized below. I only ran the spkg-check script of the PyCrypto spkg. This was tested with Sage 4.4.4. With the exception of cicero.skynet, all machines reported here are 64-bit.

 1. bsd.math: Mac OS X 10.6.4, GCC 4.2.1, Dual-Core Intel Xeon `@` 2.66 GHz
    * build: yes
    * doctest: pass
    * spkg-check: pass
 1. cicero.skynet: 32-bit Fedora 12, GCC 4.5.0, Intel(R) Pentium(R) 4 CPU `@` 2.66GHz
    * build: yes
    * doctest: one failure in `libs/mwrank/mwrank.pyx`, as reported [here](https://groups.google.com/group/sage-release/browse_thread/thread/20dcc2ac0c5b978c)
    * spkg-check: pass
 1. cleo.skynet: Red Hat Enterprise Linux Server 5.3, GCC 4.5.0, IA-64 Itanium 2 `@` 1594.000726 MHz
    * build: yes
    * doctest: pass
    * spkg-check: pass
 1. eno.skynet: Fedora 12, GCC 4.5.0, Intel(R) Xeon(R) CPU E5345 `@` 2.33GHz
    * build: yes
    * doctest: pass
    * spkg-check: pass
 1. flavius.skynet: Fedora 12, GCC 4.5.0, AMD Opteron(tm) Processor 248 `@` 2193.570 MHz
    * build: yes
    * doctest: pass
    * spkg-check: pass
 1. gcc11.fsffrance: Debian 5.0, GCC 4.3.2, Dual-Core AMD Opteron(tm) Processor 2212 `@` 2000.085 MHz
    * build: yes
    * doctest: pass
    * spkg-check: pass
 1. gcc16.fsffrance: Debian 5.0, GCC 4.3.2, Quad-Core AMD Opteron(tm) Processor 8354 `@` 2194.496 MHz
    * build: yes
    * doctest: [2 failures](https://groups.google.com/group/sage-release/browse_thread/thread/7a8a2e2af0eafde7) in `schemes/elliptic_curves/lseries_ell.py`
    * spkg-check: pass
 1. gcc100.fsffrance: Debian 5.0, GCC 4.3.2, AMD Opteron(tm) Processor 252 `@` 2600.011 MHz
    * build: yes
    * doctest: failures in `modules/free_module.py`
    * spkg-check: pass
 1. iras.skynet: SUSE Linux Enterprise Server 10 SP1, GCC 4.5.0, IA-64 `@` 1594.000683 MHz
    * build: yes
    * doctest: pass
    * spkg-check: pass
 1. lena.skynet: Fedora 12, GCC 4.5.0, AMD Phenom(tm) II X4 940 Processor `@` 3000.000 MHz
    * build: yes
    * doctest: pass
    * spkg-check: pass
 1. menas.skynet: openSUSE 11.1, GCC 4.5.0, Intel(R) Core(TM)2 Quad CPU Q6600 `@` 2.40GHz
    * build: yes
    * doctest: pass
    * spkg-check: pass
 1. rh.math: Ubuntu 10.04 LTS, GCC 4.4.3, Six-Core AMD Opteron(tm) Processor 8439 SE `@` 800.000 MHz
    * build: yes
    * doctest: pass
    * spkg-check: pass
 1. sage.math: Ubuntu 8.04.4 LTS, GCC 4.2.4, Intel(R) Xeon(R) CPU X7460 `@` 2.66GHz
    * build: yes
    * doctest: pass
    * spkg-check: pass
 1. sextus.skynet: Fedora 12, GCC 4.5.0, Intel(R) Xeon(TM) CPU `@` 3.60GHz
    * build: yes
    * doctest: pass
    * spkg-check: pass
 1. taurus.skynet: Fedora 12, GCC 4.5.0, Intel(R) Xeon(R) CPU X5570 `@` 2.93GHz
    * build: no, due to Linbox failing to build on taurus. This is a known issue. But forcing an installation of the PyCrypto spkg with "./sage -f <...>", and then running spkg-check, worked fine.
    * doctest: N/A since Sage 4.4.4 fails to build on taurus
    * spkg-check: pass


---

Comment by mvngu created at 2010-06-26 10:43:07

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-06-26 10:45:50

Changing status from needs_review to needs_info.


---

Comment by mvngu created at 2010-06-26 10:45:50

I'm still waiting for build/test results on t2.math.


---

Comment by mvngu created at 2010-06-27 10:17:03

Build fine on t2.math and `spkg-check` of PyCrypto passes. This is now ready for review.


---

Comment by mvngu created at 2010-06-27 10:17:03

Changing status from needs_info to needs_review.


---

Comment by mvngu created at 2010-06-27 18:14:23

Also build fine on Cygwin (`winxp2`) and spkg-check pass.


---

Comment by drkirkby created at 2010-07-16 21:05:41

You have clearly tested this thoroughly Minh - I wish all Sage developers were like you. 

I just tested it on two systems:

 * OpenSolaris 2009.06 on a 3.33 GHz Intel W3580 Xeon. 64-bit build. All tests in `spkg-check` pass. Since Sage crashes immediately on startup, I can't comment on doctests. 
 * Solaris 10 on a Sun Blade 2000, with two Sun UltraSPARC III+ processors. 64-bit build. All tests in `spkg-check` pass. Since Sage is unstable on 64-bit Solaris 10 on SPARC, it's pointless me running any doctests. (Sage does now just about work on 64-bit SPARC. I got it running for the first time yesterday, so needless to say, it is far from perfect). 

`hg status`

shows no problems, so positive review.

Dave


---

Comment by drkirkby created at 2010-07-16 21:05:41

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-09 09:38:15

Resolution: fixed
