# Issue 9511: Suggestion to upgrade givaro 3.3.1 and 3.3.2 [with patch]

Issue created by migration from https://trac.sagemath.org/ticket/9511

Original creator: pcpa

Original creation time: 2010-07-15 19:51:16

Assignee: cpernet

CC:  zimmerma jpflori

In the Mandriva sagemath package I use the attached patch. It did work with sagemath 4.4 and givaro 3.3.1, and still works with sagemath 4.4.4 and givaro 3.3.2.


---

Comment by cpernet created at 2010-07-15 19:58:25

I'm currently working on the upgrade to givaro-3.3.3rc0 together with linbox-1.1.7, since this later version of linbox required very recent changes in givaro (only in 3.3.3rc0).


---

Comment by malb created at 2011-08-23 02:24:53

Changing status from new to needs_review.


---

Comment by malb created at 2011-08-23 04:44:00

Note this upgrade won't work unless LinBox is upgraded as well.


---

Comment by fbissey created at 2011-08-23 04:47:23

Replying to [comment:6 malb]:
> Note this upgrade won't work unless LinBox is upgraded as well.
I was going to say that, not to mention we need a givaro-3.3.xx spkg too.


---

Comment by fbissey created at 2011-08-23 04:48:19

spkg that I missed in the description somehow. linbox in a new ticket?


---

Comment by malb created at 2011-08-23 04:56:39

Yep, I opened #11718 for that but I just accidentally killed the last three hours of pretty boring & tedious work trying to compile 1.1.7. So it'll take a while until I upload an SPKG there.


---

Comment by malb created at 2011-08-23 18:27:00

*Status update:*

We get errors like this


```
/sage-4.7.1/local/include/givaro/givzpz16table1.inl:424: error: ‘UINT32_MAX’ was not declared in this scope
```


on _sage.math_ unless we explicitly pass `-D__STDC_LIMIT_MACROS` in `spkg-install`. This works but is weird because Givaro does set `__STDC_LIMIT_MACROS` before it includes `<stdint.h>`. Also, I do not have this problem my local machine (running 64-bit Debian/GNU Linux)


---

Comment by malb created at 2011-08-23 18:27:00

Changing status from needs_review to needs_work.


---

Comment by leif created at 2012-04-22 01:41:30

Just for the record:

There's a Givaro 3.2.13.rc1.p4 spkg with a couple of fixes at #12761 (currently still needing review).


---

Comment by malb created at 2012-06-06 19:10:03

I am feeling ambitious today (Brice from the LinBox team is in shouting distance) so I decided to give this update business another try. Givaro 3.6.0 is the easy part so here it is.


---

Comment by malb created at 2012-06-18 09:02:45

Changing status from needs_work to needs_review.


---

Comment by malb created at 2012-06-18 09:02:45

Updated so that the number theory doctest in the "French book" is deterministic.


---

Comment by vbraun created at 2012-06-18 11:08:14

The permissions of `spkg-install` and `SPKG.txt` should be fixed to make Jeroen happy ;-)


---

Comment by malb created at 2012-06-18 11:22:33

Fixed to 755 and 644 respectively.


---

Comment by vbraun created at 2012-06-18 11:30:48

Patch doesn't apply on top of the m4ri update (#12840, #12841).

Also, `Set([r for r in R])` should be just `Set(R)` or (even better in case there are duplicate elements) `sorted(R)`


---

Comment by malb created at 2012-06-18 12:11:38

Replying to [comment:20 vbraun]:
> Patch doesn't apply on top of the m4ri update (#12840, #12841).

That's weird, I have it applied here:


```
$ hg qap                                                                                                                        [r16883 mq:5/5 sage-linbox.patch -  1:09PM]
trac_12840_m4ri_new_version.patch
trac_12841_m4rie_new_version.patch
trac_9511_givaro_3_6_x.patch
matrix_modn_dense_no_linbox.patch
sage-linbox.patch
```

 
> Also, `Set([r for r in R])` should be just `Set(R)` or (even better in case there are duplicate elements) `sorted(R)` 

I just copied what Paul Zimmermann suggested as a fix for the book. Paul is CCed, so if he agrees, I'll change the doctest accordingly.


---

Comment by vbraun created at 2012-06-18 12:44:53

Where does the line 

```
              depends = [SAGE_INC + 'givaro/givconfig.h']), 
```

in your `module_list.py` come from? Its not in sage-5.1.beta3.

Also (and perhaps related), #11718 is no longer a dependency for this ticket right?


---

Comment by malb created at 2012-06-18 13:06:20

Replying to [comment:22 vbraun]:
> Where does the line 
> {{{
>               depends = [SAGE_INC + 'givaro/givconfig.h']), 
> }}}
> in your `module_list.py` come from? Its not in sage-5.1.beta3.

It's from 

http://trac.sagemath.org/sage_trac/attachment/ticket/12761/12761_givaro_depends.patch

which was merged in 5.0.1.rc1.
> Also (and perhaps related), #11718 is no longer a dependency for this ticket right?

Right, fixed that.


---

Comment by vbraun created at 2012-06-18 13:19:52

Why is #12883 a dependency? Its the other way round, this ticket is a dependency for #12883 or not?


---

Comment by malb created at 2012-06-18 13:24:42

Both tickets depend on each other, you cannot have one without the other.  Givaro upgrade implies LinBox upgrade and LinBox upgrade implies Givaro upgrade. Perhaps it would be cleaner to merge them?


---

Comment by vbraun created at 2012-06-18 13:29:59

Lets leave it at the current state but in general its probably best to avoid cyclic dependencies....


---

Comment by zimmerma created at 2012-06-18 13:46:35

Replying to [comment:20 vbraun]:
> Also, `Set([r for r in R])` should be just `Set(R)` or (even better in case there are duplicate elements) `sorted(R)` 

I prefer to leave `Set([r for r in R])` which is more explicit (in my opinion) and to make
the changes minimal in the book. There are no duplicate elements here (in a finite field).

Paul


---

Comment by vbraun created at 2012-06-18 14:37:04

The identity list comprehension doesn't add anything to the understanding here. Why not

```
Set([ s for s in [r for r in R]))
```

to make it really really explicit? :-P  

If anything, this teaches bad habits. The only valid argument imho is that nobody is going to actually look into the sage.tests directory to learn how to use Sage. So I don't really care here but I would never let this stand in a doctest that is visible in the manual.


---

Comment by vbraun created at 2012-06-21 15:19:32

I'm getting testing failures on sage-5.1.beta5 (this worked fine on beta3, but the `cholesky()` method is new in beta5):

```
[vbraun@volker-desktop matrix]$ sage -t sage/matrix/matrix2.pyx
sage -t  "devel/sage-main/sage/matrix/matrix2.pyx"          
**********************************************************************
File "/home/vbraun/opt/sage-5.1.beta5/devel/sage-main/sage/matrix/matrix2.pyx", line 9813:
    sage: L
Expected:
    [            3             0             0]
    [    4*a^2 + 1             1             0]
    [      3*a + 2 a^2 + 2*a + 3             3]
Got:
    [            2             0             0]
    [      a^2 + 4             1             0]
    [      2*a + 3 a^2 + 2*a + 3             2]
**********************************************************************
1 items had failures:
   1 of  65 in __main__.example_105
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/vbraun/.sage//tmp/matrix2_12014.py
	 [12.8 s]
```



---

Comment by vbraun created at 2012-06-22 12:14:40

Compiles fine, but one failure with the testsuite on mark/skynet (SPARC solaris)

```
/bin/bash ../libtool --tag=CXX   --mode=link g++ -O0 -Wall -g -DNDEBUG -UGIVARO_DEBUG -UDEBUG -I/home/vbraun/opt/mark/sage-5.1.beta3/local//include  -fPIC -I"/home/vbraun/opt/mark/sage-5.1.beta3/local/include" -static   -o te
st-trunc test-trunc.o  -L../src -L../src/.libs -lgivaro -L/home/vbraun/opt/mark/sage-5.1.beta3/local//lib -lgmpxx -lgmp -L/home/vbraun/opt/mark/sage-5.1.beta3/local//lib -lgmpxx -lgmp
libtool: link: g++ -O0 -Wall -g -DNDEBUG -UGIVARO_DEBUG -UDEBUG -I/home/vbraun/opt/mark/sage-5.1.beta3/local//include -fPIC -I/home/vbraun/opt/mark/sage-5.1.beta3/local/include -o test-trunc test-trunc.o  -L../src -L../src/.l
ibs /home/vbraun/opt/mark/sage-5.1.beta3/spkg/build/givaro-3.7.0/src/src/.libs/libgivaro.a -L/home/vbraun/opt/mark/sage-5.1.beta3/local//lib /home/vbraun/opt/mark/sage-5.1.beta3/local/lib/libgmpxx.so /home/vbraun/opt/mark/sag
e-5.1.beta3/local/lib/libstdc++.so -lm /home/vbraun/opt/mark/sage-5.1.beta3/local/lib/libgmp.so -Wl,-R -Wl,/home/vbraun/opt/mark/sage-5.1.beta3/local/lib -Wl,-R -Wl,/home/vbraun/opt/mark/sage-5.1.beta3/local/lib
ld: warning: file /home/vbraun/opt/mark/sage-5.1.beta3/local//lib/libstdc++.so: linked to /home/vbraun/opt/mark/sage-5.1.beta3/local/lib/libstdc++.so: attempted multiple inclusion of file
g++ -DHAVE_CONFIG_H -I. -I..  -I..  -I/home/vbraun/opt/mark/sage-5.1.beta3/local//include -I../src/kernel/system -I../src/kernel/memory -I../src/kernel/zpz -I../src/kernel/integer -I../src/kernel -I../src/library/poly1 -I../s
rc/kernel/bstruct -I../src/library/tools  -O0 -Wall -g -DNDEBUG -UGIVARO_DEBUG -UDEBUG -I/home/vbraun/opt/mark/sage-5.1.beta3/local//include  -fPIC -I"/home/vbraun/opt/mark/sage-5.1.beta3/local/include" -c -o test-crt.o test-
crt.C
```

looks good but then further down

```
PASS: test-trunc
/bin/bash: line 5: 12309 Bus Error               (core dumped) ${dir}$tst
FAIL: test-crt
PASS: test-geom
PASS: test-integer
PASS: test-conversion
PASS: test-ratrecon
=============================================
1 of 12 tests failed
Please report to Jean-Guillaume.Dumas@imag.fr
=============================================
make[3]: *** [check-TESTS] Error 1
make[3]: Leaving directory `/home/vbraun/opt/mark/sage-5.1.beta3/spkg/build/givaro-3.7.0/src/tests'
make[2]: *** [check-am] Error 2
make[2]: Leaving directory `/home/vbraun/opt/mark/sage-5.1.beta3/spkg/build/givaro-3.7.0/src/tests'
make[1]: *** [check-recursive] Error 1
make[1]: Leaving directory `/home/vbraun/opt/mark/sage-5.1.beta3/spkg/build/givaro-3.7.0/src/tests'
make: *** [check-recursive] Error 1
Error while running the Givaro testsuite ... exiting
```



---

Attachment


---

Comment by malb created at 2012-06-24 15:07:09

I rebased the patch to 5.1.beta5. In particular, this patch removes the line from `matrix2.pyx` that producses the offending output

```
sage -t  "devel/sage-main/sage/matrix/matrix2.pyx"          
**********************************************************************
File "/home/vbraun/opt/sage-5.1.beta5/devel/sage-main/sage/matrix/matrix2.pyx", line 9813:
    sage: L
Expected:
    [            3             0             0]
    [    4*a^2 + 1             1             0]
    [      3*a + 2 a^2 + 2*a + 3             3]
Got:
    [            2             0             0]
    [      a^2 + 4             1             0]
    [      2*a + 3 a^2 + 2*a + 3             2]
**********************************************************************
```

The Cholesky decomposition is not unique over finite fields and we shouldn't test for the output (which can be random depending on which square-root is chosen) but test for L*L<sup>T</sup> == A. This is done by the line after the line removed in this patch. Hence, correctness is checked. Note that I discussed this off-list Rob Beezer who is the author of the line removed in this patch.


---

Comment by malb created at 2012-06-24 15:08:29

Replying to [comment:32 vbraun]:
> {{{
> PASS: test-trunc
> /bin/bash: line 5: 12309 Bus Error               (core dumped) ${dir}$tst
> FAIL: test-crt
> }}}

Shall we set this to *needs work* then? What's our policy for stuff like this?


---

Comment by vbraun created at 2012-06-24 15:19:37

Changing status from needs_review to needs_work.


---

Comment by vbraun created at 2012-06-24 15:19:37

I talked to Jean-Guillaume and he gave me an experimental patch but it didn't help. Here is the gdb backtrace

```
-bash-3.00$ /home/vbraun/opt/mark/gdb-7.4.1/gdb/gdb test-crt
GNU gdb (GDB) 7.4.1
Copyright (C) 2012 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "sparc-sun-solaris2.10".
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>...
Reading symbols from
/home/vbraun/opt/mark/sage-5.1.beta3/spkg/build/givaro-3.7.0/src/tests/test-crt...done.
(gdb) run
Starting program:
/home/vbraun/opt/mark/sage-5.1.beta3/spkg/build/givaro-3.7.0/src/tests/test-crt
[Thread debugging using libthread_db enabled]
[New Thread 1 (LWP 1)]

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 1 (LWP 1)]
0x00029030 in Givaro::GFqDom<long>::GFqDom (this=0x7eaec, F=...)
   at /home/vbraun/opt/mark/sage-5.1.beta3/local//include/givaro/givgfq.h:100
100                     _dcharacteristic = F._dcharacteristic;
(gdb) bt
#0  0x00029030 in Givaro::GFqDom<long>::GFqDom (this=0x7eaec, F=...)
   at /home/vbraun/opt/mark/sage-5.1.beta3/local//include/givaro/givgfq.h:100
#1  0x00033c3c in Givaro::GivaroMM<Givaro::GFqDom<long> >::initone
(p=0x7eaec, V=...)
   at /home/vbraun/opt/mark/sage-5.1.beta3/local//include/givaro/givaromm.h:297
#2  0x00031110 in Givaro::GivaroMM<Givaro::GFqDom<long> >::initialize
(bloc=0x7eaec, s=15, V=...)
   at /home/vbraun/opt/mark/sage-5.1.beta3/local//include/givaro/givaromm.h:300
#3  0x000268f8 in Givaro::Array0<Givaro::GFqDom<long> >::build
(this=0xffbff890, s=15, t=...)
   at /home/vbraun/opt/mark/sage-5.1.beta3/local//include/givaro/givarray0.inl:30
#4  0x00021ad0 in Givaro::Array0<Givaro::GFqDom<long> >::Array0
(this=0xffbff890, s=15)
   at /home/vbraun/opt/mark/sage-5.1.beta3/local//include/givaro/givarray0.inl:39
#5  0x0001bf04 in tmain<Givaro::GFqDom<long> > (argc=1,
argv=0xffbffb3c, generator=...) at test-crt.C:49
#6  0x00013d00 in main (argc=1, argv=0xffbffb3c) at test-crt.C:151
(gdb) l
95              {
96                      zero = F.zero;
97                      one = F.one;
98                      mOne = F.mOne;
99                      _characteristic = F._characteristic;
100                     _dcharacteristic = F._dcharacteristic;
101                     _exponent = F._exponent;
102                     _irred = F._irred;
103                     _q = F._q;
104                     _qm1 = F._qm1;
```

I think we should at least wait a bit more if he can come up with a working patch.


---

Comment by vbraun created at 2012-06-25 21:02:41

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2012-06-25 21:02:41

The alignment problem stems from the use of placement new in the Givaro array class. Since we currently do not use that in Sage, there is no reason to delay this ticket further. I've created another ticket (#13164) to deal with the SPARC failure.

Positive review.


---

Comment by vbraun created at 2012-06-26 15:56:46

Changing status from positive_review to needs_work.


---

Comment by vbraun created at 2012-06-26 15:56:46

From the spkg-install:

```
if [ -f "$SAGE_ROOT"/devel/sage/sage/rings/polynomial/multi_polynomial_ideal_libsingular.pyx ]; then
    echo "Touching extensions linked against Givaro"
    touch "$SAGE_ROOT"/devel/sage/sage/rings/finite_field_givaro.pyx
    touch "$SAGE_ROOT"/devel/sage/sage/libs/linbox/linbox.pyx
    touch "$SAGE_ROOT"/devel/sage/sage/libs/singular/singular.pyx
    touch "$SAGE_ROOT"/devel/sage/sage/matrix/matrix_mpolynomial_dense.pyx
    touch "$SAGE_ROOT"/devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx
    touch "$SAGE_ROOT"/devel/sage/sage/rings/polynomial/multi_polynomial_ideal_libsingular.pyx
fi
```

So *THIS* is the reason why `sage/rings/finite_field_givaro.pyx` magically reappears once in a while. This file has been renamed a long time ago but whenever you reinstall givaro it is recreated. Our setup stuff does take care of recompiling dependent Cython classes, so this whole section is useless. Can you take it out before we ship it?


---

Comment by malb created at 2012-06-26 16:15:41

Fixed

  https://bitbucket.org/malb/givaro-spkg/changeset/a7631e395f36

I also uploaded a new SPKG.


---

Comment by vbraun created at 2012-06-26 18:48:04

Your repository isn't public, I think. I get an error when following the link.


---

Comment by vbraun created at 2012-06-26 19:21:19

Ok looks good!


---

Comment by vbraun created at 2012-06-26 19:21:19

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2012-06-27 07:43:29

Replying to [comment:39 vbraun]:
> So *THIS* is the reason why `sage/rings/finite_field_givaro.pyx` magically reappears once in a while. This file has been renamed a long time ago but whenever you reinstall givaro it is recreated. Our setup stuff does take care of recompiling dependent Cython classes, so this whole section is useless. Can you take it out before we ship it?

This was supposed to be fixed in #12761 (merged in sage-5.0.1.rc1 and sage-5.1.beta4 and clearly mentioned in the comments and dependencies of this ticket!), so your spkg should be rebased to that.


---

Comment by jdemeyer created at 2012-06-27 07:43:29

Changing status from positive_review to needs_work.


---

Comment by malb created at 2012-06-27 10:30:03

I've merged the two SPKGs here:

  https://bitbucket.org/malb/givaro-spkg/changeset/9b0324505f18

I've also uploaded a new SPKG (MD5: `7db046ff7fcb737234e41fcb2e15f94f`).

Note that Givaro 3.7.0 is GCC 4.7. compliant (at least it compiles on my machine which has GCC 4.7).


---

Comment by vbraun created at 2012-06-27 10:56:30

What about `givtablelimits.h.patch`? Arguable we don't care about Cygwin any more but then it seems like it can't hurt either. Opinions?


---

Comment by malb created at 2012-06-27 15:23:28

TBH, I don't care either way.


---

Comment by jdemeyer created at 2012-06-27 15:26:53

Replying to [comment:46 malb]:
> TBH, I don't care either way.
Well, if you _remove_ a patch, you should have a reason for it...


---

Comment by vbraun created at 2012-06-27 15:31:48

I'm fine without the Cygwin patch, its rather ugly ihmo.


---

Comment by vbraun created at 2012-06-27 15:31:48

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2012-06-27 20:35:27

Diff between the 3.2.13.p0 (#12761) and 3.7.0 givaro spkgs. For review only.


---

Comment by jdemeyer created at 2012-06-27 20:41:41

Changing status from positive_review to needs_work.


---

Attachment

You should keep the

```
echo >&2 Error
```

instead of 

```
echo Error
```

and also the Cygwin patch and the `$SAGE_LOCAL` quoting (i.e. don't undo something from givaro-3.2.13 unless you have a reason too).


---

Comment by malb created at 2012-06-27 21:03:51

Quote and echo business fixed in:

  https://bitbucket.org/malb/givaro-spkg/changeset/d9b1505bb161

As far as I can tell Cygwin fixes are not needed any more:

  https://lists.gnu.org/archive/html/bug-gnulib/2010-03/msg00217.html


---

Comment by malb created at 2012-06-27 21:03:51

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2012-06-27 21:08:32

Looks good to me!


---

Comment by vbraun created at 2012-06-27 21:08:32

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-08-12 21:48:22

This needs to be rebased to [sage-5.3.beta1](http://boxen.math.washington.edu/home/release/sage-5.3.beta1/) (to be released very soon).


---

Comment by jdemeyer created at 2012-08-12 21:48:22

Changing status from positive_review to needs_work.


---

Comment by vbraun created at 2012-08-14 02:32:47

Rebased patch


---

Attachment

Rebased patch for sage-5.3.beta1. Just a trivial rebase in `module_list.py`.


---

Comment by vbraun created at 2012-08-14 02:33:39

Changing status from needs_work to positive_review.


---

Comment by jpflori created at 2012-08-20 22:21:20

Volker, could you tag the last hg commit here as well?


---

Comment by jhpalmieri created at 2012-08-20 22:38:15

I thought that Jeroen's scripts for Sage releases added those tags automatically, but I'm not sure.


---

Comment by vbraun created at 2012-08-21 02:38:22

I haven't made any changes to the spkg yet, so I'm not going to partake in the bikeshedding here. The Sage developer guide contains nothing about mandatory hg tagging. In fact, since we frequently make changes in response to reviews before releasing the spkg, really only the release manager can set the tag.


---

Comment by jdemeyer created at 2012-08-21 09:17:47

Replying to [comment:60 jhpalmieri]:
> I thought that Jeroen's scripts for Sage releases added those tags automatically
Indeed.


---

Comment by vbraun created at 2012-08-24 12:06:32

Superseded by #13164.


---

Comment by jhpalmieri created at 2012-08-24 15:24:37

Is the Sage library patch still necessary? If so, maybe it should be moved to #13164 and this ticket should be closed as a duplicate.


---

Comment by jpflori created at 2012-08-24 15:28:31

I did not try without it (in fact I did but without the linbox patches as well, by mistake), but with it there are no errors.


---

Comment by vbraun created at 2012-08-25 17:50:32

Superseded by #13164, close this ticket as duplicate.


---

Comment by jdemeyer created at 2012-09-05 09:38:26

Resolution: duplicate
