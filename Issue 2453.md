# Issue 2453: linbox related segfaults in modular/modsym/space.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-03-10 07:55:32

Assignee: cpernet

Valgrind reports the following issue:

```
==21267== Invalid read of size 8
==21267==    at 0x17232034: LinBox::Modular<double>::assign(double&, double const&) const (modular-double.h:213)
==21267==    by 0x17233B74: void LinBox::FFLAS::fcopy<LinBox::Modular<double> >(LinBox::Modular<double> const&, unsigned long, LinBox::Modular<double>::Element*, unsigned long, LinBox::Modular<double>::Element const*, unsigned long) (fflas_fcopy.inl:20)
==21267==    by 0x1736B09F: std::list<LinBox::GivPolynomial<double, std::allocator<double> >, std::allocator<LinBox::GivPolynomial<double, std::allocator<double> > > >& LinBox::FFPACK::CharpolyArithProg<LinBox::Modular<double>, LinBox::GivPolynomial<double, std::allocator<double> > >(LinBox::Modular<double> const&, std::list<LinBox::GivPolynomial<double, std::allocator<double> >, std::allocator<LinBox::GivPolynomial<double, std::allocator<double> > > >&, unsigned long, LinBox::Modular<double>::Element*, unsigned long, unsigned long) (ffpack_frobenius.inl:98)
==21267==    by 0x1736BB3D: std::list<LinBox::GivPolynomial<double, std::allocator<double> >, std::allocator<LinBox::GivPolynomial<double, std::allocator<double> > > >& LinBox::FFPACK::CharpolyArithProg<LinBox::Modular<double>, LinBox::GivPolynomial<double, std::allocator<double> > >(LinBox::Modular<double> const&, std::list<LinBox::GivPolynomial<double, std::allocator<double> >, std::allocator<LinBox::GivPolynomial<double, std::allocator<double> > > >&, unsigned long, LinBox::Modular<double>::Element*, unsigned long, unsigned long) (ffpack_frobenius.inl:187)
==21267==    by 0x17370508: std::list<LinBox::GivPolynomial<double, std::allocator<double> >, std::allocator<LinBox::GivPolynomial<double, std::allocator<double> > > >& LinBox::FFPACK::CharPoly<LinBox::Modular<double>, LinBox::GivPolynomial<double, std::allocator<double> > >(LinBox::Modular<double> const&, std::list<LinBox::GivPolynomial<double, std::allocator<double> >, std::allocator<LinBox::GivPolynomial<double, std::allocator<double> > > >&, unsigned long, LinBox::Modular<double>::Element*, unsigned long, LinBox::FFPACK::FFPACK_CHARPOLY_TAG) (ffpack_charpoly.inl:56)
==21267==    by 0x173706B8: LinBox::BlasMatrixDomainCharpoly<LinBox::Modular<double>, std::list<LinBox::GivPolynomial<double, std::allocator<double> >, std::allocator<LinBox::GivPolynomial<double, std::allocator<double> > > >, LinBox::BlasMatrix<double> >::operator()(LinBox::Modular<double> const&, std::list<LinBox::GivPolynomial<double, std::allocator<double> >, std::allocator<LinBox::GivPolynomial<double, std::allocator<double> > > >&, LinBox::BlasMatrix<double> const&) const (blas-domain.inl:1105)
==21267==    by 0x17370775: LinBox::GivPolynomial<double, std::allocator<double> >& LinBox::BlasMatrixDomain<LinBox::Modular<double> >::charpoly<LinBox::GivPolynomial<double, std::allocator<double> >, LinBox::BlasMatrix<double> >(LinBox::GivPolynomial<double, std::allocator<double> >&, LinBox::BlasMatrix<double> const&) const (blas-domain.h:445)
==21267==    by 0x173709D4: LinBox::GivPolynomial<double, std::allocator<double> >& LinBox::charpoly<LinBox::GivPolynomial<double, std::allocator<double> >, LinBox::DenseMatrix<LinBox::Modular<double> > >(LinBox::GivPolynomial<double, std::allocator<double> >&, LinBox::DenseMatrix<LinBox::Modular<double> > const&, LinBox::RingCategories::ModularTag const&, LinBox::BlasEliminationTraits const&) (charpoly.h:159)
==21267==    by 0x17370FF9: LinBox::GivPolynomial<double, std::allocator<double> >& LinBox::charpoly<LinBox::GivPolynomial<double, std::allocator<double> >, LinBox::Modular<double>, LinBox::RingCategories::ModularTag>(LinBox::GivPolynomial<double, std::allocator<double> >&, LinBox::DenseMatrix<LinBox::Modular<double> > const&, LinBox::RingCategories::ModularTag const&, LinBox::HybridSpecifier const&) (charpoly.h:126)
==21267==    by 0x1737102D: LinBox::GivPolynomial<double, std::allocator<double> >& LinBox::charpoly<LinBox::DenseMatrix<LinBox::Modular<double> >, LinBox::GivPolynomial<double, std::allocator<double> >, LinBox::HybridSpecifier>(LinBox::GivPolynomial<double, std::allocator<double> >&, LinBox::DenseMatrix<LinBox::Modular<double> > const&, LinBox::HybridSpecifier const&) (charpoly.h:80)
==21267==    by 0x17371059: LinBox::GivPolynomial<double, std::allocator<double> >& LinBox::charpoly<LinBox::DenseMatrix<LinBox::Modular<double> >, LinBox::GivPolynomial<double, std::allocator<double> > >(LinBox::GivPolynomial<double, std::allocator<double> >&, LinBox::DenseMatrix<LinBox::Modular<double> > const&) (charpoly.h:93)
==21267==    by 0x1722BF73: linbox_modn_dense_minpoly (linbox_wrap.cpp:126)
==21267==  Address 0x1b459450 is 8 bytes before a block of size 240 alloc'd
==21267==    at 0x4A1C2C7: operator new[](unsigned long) (vg_replace_malloc.c:274)
==21267==    by 0x1736A906: std::list<LinBox::GivPolynomial<double, std::allocator<double> >, std::allocator<LinBox::GivPolynomial<double, std::allocator<double> > > >& LinBox::FFPACK::CharpolyArithProg<LinBox::Modular<double>, LinBox::GivPolynomial<double, std::allocator<double> > >(LinBox::Modular<double> const&, std::list<LinBox::GivPolynomial<double, std::allocator<double> >, std::allocator<LinBox::GivPolynomial<double, std::allocator<double> > > >&, unsigned long, LinBox::Modular<double>::Element*, unsigned long, unsigned long) (ffpack_frobenius.inl:35)
==21267==    by 0x1736BB3D: std::list<LinBox::GivPolynomial<double, std::allocator<double> >, std::allocator<LinBox::GivPolynomial<double, std::allocator<double> > > >& LinBox::FFPACK::CharpolyArithProg<LinBox::Modular<double>, LinBox::GivPolynomial<double, std::allocator<double> > >(LinBox::Modular<double> const&, std::list<LinBox::GivPolynomial<double, std::allocator<double> >, std::allocator<LinBox::GivPolynomial<double, std::allocator<double> > > >&, unsigned long, LinBox::Modular<double>::Element*, unsigned long, unsigned long) (ffpack_frobenius.inl:187)
==21267==    by 0x17370508: std::list<LinBox::GivPolynomial<double, std::allocator<double> >, std::allocator<LinBox::GivPolynomial<double, std::allocator<double> > > >& LinBox::FFPACK::CharPoly<LinBox::Modular<double>, LinBox::GivPolynomial<double, std::allocator<double> > >(LinBox::Modular<double> const&, std::list<LinBox::GivPolynomial<double, std::allocator<double> >, std::allocator<LinBox::GivPolynomial<double, std::allocator<double> > > >&, unsigned long, LinBox::Modular<double>::Element*, unsigned long, LinBox::FFPACK::FFPACK_CHARPOLY_TAG) (ffpack_charpoly.inl:56)
==21267==    by 0x173706B8: LinBox::BlasMatrixDomainCharpoly<LinBox::Modular<double>, std::list<LinBox::GivPolynomial<double, std::allocator<double> >, std::allocator<LinBox::GivPolynomial<double, std::allocator<double> > > >, LinBox::BlasMatrix<double> >::operator()(LinBox::Modular<double> const&, std::list<LinBox::GivPolynomial<double, std::allocator<double> >, std::allocator<LinBox::GivPolynomial<double, std::allocator<double> > > >&, LinBox::BlasMatrix<double> const&) const (blas-domain.inl:1105)
==21267==    by 0x17370775: LinBox::GivPolynomial<double, std::allocator<double> >& LinBox::BlasMatrixDomain<LinBox::Modular<double> >::charpoly<LinBox::GivPolynomial<double, std::allocator<double> >, LinBox::BlasMatrix<double> >(LinBox::GivPolynomial<double, std::allocator<double> >&, LinBox::BlasMatrix<double> const&) const (blas-domain.h:445)
==21267==    by 0x173709D4: LinBox::GivPolynomial<double, std::allocator<double> >& LinBox::charpoly<LinBox::GivPolynomial<double, std::allocator<double> >, LinBox::DenseMatrix<LinBox::Modular<double> > >(LinBox::GivPolynomial<double, std::allocator<double> >&, LinBox::DenseMatrix<LinBox::Modular<double> > const&, LinBox::RingCategories::ModularTag const&, LinBox::BlasEliminationTraits const&) (charpoly.h:159)
==21267==    by 0x17370FF9: LinBox::GivPolynomial<double, std::allocator<double> >& LinBox::charpoly<LinBox::GivPolynomial<double, std::allocator<double> >, LinBox::Modular<double>, LinBox::RingCategories::ModularTag>(LinBox::GivPolynomial<double, std::allocator<double> >&, LinBox::DenseMatrix<LinBox::Modular<double> > const&, LinBox::RingCategories::ModularTag const&, LinBox::HybridSpecifier const&) (charpoly.h:126)
==21267==    by 0x1737102D: LinBox::GivPolynomial<double, std::allocator<double> >& LinBox::charpoly<LinBox::DenseMatrix<LinBox::Modular<double> >, LinBox::GivPolynomial<double, std::allocator<double> >, LinBox::HybridSpecifier>(LinBox::GivPolynomial<double, std::allocator<double> >&, LinBox::DenseMatrix<LinBox::Modular<double> > const&, LinBox::HybridSpecifier const&) (charpoly.h:80)
==21267==    by 0x17371059: LinBox::GivPolynomial<double, std::allocator<double> >& LinBox::charpoly<LinBox::DenseMatrix<LinBox::Modular<double> >, LinBox::GivPolynomial<double, std::allocator<double> > >(LinBox::GivPolynomial<double, std::allocator<double> >&, LinBox::DenseMatrix<LinBox::Modular<double> > const&) (charpoly.h:93)
==21267==    by 0x1722BF73: linbox_modn_dense_minpoly (linbox_wrap.cpp:126)
==21267==    by 0x16FAB007: __pyx_pf_4sage_4libs_6linbox_6linbox_17Linbox_modn_dense__poly(_object*, _object*) (linbox.cpp:1496)
```


I have more valgrind output from various other linbox 1.1.5.rc2 debug sessions, but I will post those on linbox-use soonish.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-10 15:06:02

Make sure to use the latest linbox.spkg from #2458 as a base.

Cheers,

Michael


---

Comment by was created at 2008-03-11 16:35:25

Make a file with just this doctest in it:

```
"""                                                                                                  
    sage: ModularSymbols(1,16,0,GF(5)).simple_factors()                                              
    [Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 3 for Gamma_0(1) \
of weight 16 with sign 0 over Finite Field of size 5,                                                
    Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 3 for Gamma_0(1) o\
f weight 16 with sign 0 over Finite Field of size 5,                                                 
    Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 3 for Gamma_0(1) o\
f weight 16 with sign 0 over Finite Field of size 5]                                                 
"""
```


This is already enough to segfault!


---

Comment by was created at 2008-03-11 16:52:58

If I disable linbox charpoly in matrix_modn_dense then all is well and this segfault completely goes away.  Thus plan to fix this bug:

0. Release sage with linbox charpoly/minpoly not the default.

1. put some sort of trace in charpoly to find out exactly which matrix is segfaulting linbox.  I.e., exactly which charpolys get computed in matrix_modn_dense when this sage command is run: `ModularSymbols(1,16,0,GF(5)).simple_factors()`
Answer, the matrix `a = matrix(GF(5),2,[1, 0, 0, 1,])` and almost any
other matrix crash it!
Indeed, directly from the command line we have:

```
sage: for _ in xrange(10^3): a = matrix(GF(5),2,2,[1,0,0,1]).charpoly(algorithm='linbox')
....: 
/home/was/build/sage-2.10.3.rc3/local/bin/sage-sage: line 214: 25825 Segmentation fault      sage-ipython "$`@`" -c "$SAGE_STARTUP_COMMAND;"
```



2. Fix bug in linbox.

3. Re-eanble linbox charpoly/minpoly in Sage

4. Release.


---

Comment by was created at 2008-03-11 16:56:02

Here's a stack trace got using "sage -gdb":

```
sage: for _ in xrange(10^4): a = matrix(GF(5),2,2,[1, 0, 0,1]).charpoly(algorithm='linbox')
....: 

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 47346684858208 (LWP 2759)]
0x00002b0fc30ebd24 in mpn_sb_get_str ()
   from /home/was/build/sage-2.10.3.rc3/local/lib/libgmp.so.3
(gdb) bt
#0  0x00002b0fc30ebd24 in mpn_sb_get_str ()
   from /home/was/build/sage-2.10.3.rc3/local/lib/libgmp.so.3
#1  0x00002b0fc30ec199 in __gmpn_get_str ()
   from /home/was/build/sage-2.10.3.rc3/local/lib/libgmp.so.3
#2  0x00002b0fc30d4328 in __gmpz_get_str ()
   from /home/was/build/sage-2.10.3.rc3/local/lib/libgmp.so.3
#3  0x00002b0fd2ce4b04 in Integer::print (this=0x7fffe8549ae0, o=`@`0x2b0fd2cb8a00)
    at gmp++_int_io.C:37
#4  0x00002b0fd2b0248b in operator<< (o=`@`0x2b0fd2cb8a00, a=`@`0x7fffe8549ae0)
    at /home/was/build/sage-2.10.3.rc3/local/include/gmp++/gmp++_int.inl:311
#5  0x00002b0fd2b3c375 in ModularRandIter (this=0x7fffe8549ad0, F=`@`0x7fffe8d47470, 
    size=`@`0x7fffe8549b80, seed=`@`0x7fffe8549b70)
    at /home/was/build/sage-2.10.3.rc3/local/include/linbox/randiter/modular.h:94
#6  0x00002b0fd2b419ca in LinBox::FFPACK::CharpolyArithProg<LinBox::Modular<double>, LinBox::GivPolynomial<double, std::allocator<double> > > (F=`@`0x7fffe8d47470, 
    frobeniusForm=`@`0x7fffe8549f60, N=1, A=0x233cf60, lda=1, c=30)
    at /home/was/build/sage-2.10.3.rc3/local/include/linbox/ffpack/ffpack_frobenius.inl:44
#7  0x00002b0fd2b42b2e in LinBox::FFPACK::CharpolyArithProg<LinBox::Modular<double>, LinBox::GivPolynomial<double, std::allocator<double> > > (F=`@`0x7fffe8d47470, 
    frobeniusForm=`@`0x7fffe854a3a0, N=1, A=0x233cac0, lda=1, c=30)
    at /home/was/build/sage-2.10.3.rc3/local/include/linbox/ffpack/ffpack_frobenius.inl:1---Type ---Typ-----Type <r---Type <return> -----------Type <return> to continue, or q <return> to quit---
87
#8  0x00002b0fd2b42b2e in LinBox::FFPACK::CharpolyArithProg<LinBox::Modular<double>, LinBox::GivPolynomial<double, std::allocator<double> > > (F=`@`0x7fffe8d47470, 
    frobeniusForm=`@`0x7fffe854a7e0, N=1, A=0x233c620, lda=1, c=30)
    at /home/was/build/sage-2.10.3.rc3/local/include/linbox/ffpack/ffpack_frobenius.inl:187
#9  0x00002b0fd2b42b2e in LinBox::FFPACK::CharpolyArithProg<LinBox::Modular<double>, LinBox::GivPolynomial<double, std::allocator<double> > > (F=`@`0x7fffe8d47470, 
    frobeniusForm=`@`0x7fffe854ac20, N=1, A=0x233c180, lda=1, c=30)
    at /home/was/build/sage-2.10.3.rc3/local/include/linbox/ffpack/ffpack_frobenius.inl:187
#10 0x00002b0fd2b42b2e in LinBox::FFPACK::CharpolyArithProg<LinBox::Modular<double>, LinBox::GivPolynomial<double, std::allocator<double> > > (F=`@`0x7fffe8d47470, 
    frobeniusForm=`@`0x7fffe854b060, N=1, A=0x233bce0, lda=1, c=30)
    at /home/was/build/sage-2.10.3.rc3/local/include/linbox/ffpack/ffpack_frobenius.inl:187
#11 0x00002b0fd2b42b2e in LinBox::FFPACK::CharpolyArithProg<LinBox::Modular<double>, LinBox::GivPolynomial<double, std::allocator<double> > > (F=`@`0x7fffe8d47470, 
    frobeniusForm=`@`0x7fffe854b4a0, N=1, A=0x233b840, lda=1, c=30)
    at /home/was/build/sage-2.10.3.rc3/local/include/linbox/ffpack/ffpack_frobenius.inl:187
... etc. all the same.
```


Maybe an infinite loop!?!


---

Comment by was created at 2008-03-11 17:00:52

Trying with bigger matrices I get this from linbox:


```
sage: time for _ in xrange(10^2): a = random_matrix(GF(5),100).charpoly(algorithm='linbox')
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL C != 0
FAIL C != 0
FAIL C != 0
FAIL C != 0
FAIL C != 0
FAIL C != 0
FAIL C != 0
FAIL C != 0
FAIL C != 0
FAIL C != 0
FAIL C != 0
FAIL C != 0
```


AND -- interestingly, Sage's own implementation of charpoly isn't that
much slower than linbox's...

```
sage: a = random_matrix(GF(5),400)
sage: time f = a.charpoly(algorithm='generic')
CPU times: user 3.98 s, sys: 0.00 s, total: 3.98 s
Wall time: 3.98
sage: time f = a.charpoly(algorithm='linbox')
FAIL itere dependant intercale
FAIL itere dependant intercale
FAIL itere dependant intercale
CPU times: user 1.39 s, sys: 0.02 s, total: 1.42 s
Wall time: 1.42
```



---

Comment by wjp created at 2008-03-11 19:31:39

If the call to `LUdivine` in `FFPACK::CharpolyArithProg` in `ffpack_frobenius.inl` returns 0, that will cause both this valgrind warning and the infinite loop.

The attached patch to `ffpack_frobenius.inl` checks for that return value explicitly, but I'm not sufficiently familiar with the used algorithm to see if this is the right thing to do. It does fix the crashes for me, in any case.


---

Attachment

I fixed the files ffpack_frobenius.inl and ffpack_charpoly.inl, to 
1. remove the verbosity when the preconditionning failed
2. default to the deterministic algorithm when the probabilistic asumption is likely to be wrong
3. changed the random generation of the block vector, so that is has rank > 0

The new linbox spkg is available at
[http://sage.math.washington.edu/home/pernet/linbox-1.1.5rc2.p5.spkg](http://sage.math.washington.edu/home/pernet/linbox-1.1.5rc2.p5.spkg)

I also attached the diff between rc2.p4 and rc2.p5


---

Attachment

diff of linbox-1.1.5rc2.p4 against 1.1.5rc2.p5


---

Comment by wjp created at 2008-03-13 20:32:07

Your patch and new spkg look good to me and testing shows it indeed fixes the crash as well as the memory errors valgrind found. A couple of minor comments:


I would still add the `if (R == 0) { throw... } ` check after the call to LUdivine even though it shouldn't be able to occur in theory now.

The `FAIL itere dependant intercale` message is still printed. This probably looks a bit scarier than it should be in a sage session.

There are some unnecessary files in the .spkg (`SPKG.txt~`, `linbox/linbox/util/commentator.h~`, and probably also the `linbox/a.out.dSYM` directory?).


---

Comment by mabshoff created at 2008-03-15 05:43:58

This ticket seems to be superseded by #2525 and should probably be closed once that ticket has been merged. I assume the patch has made it upstream into the LinBox svn repo.

Clement: can you confirm this?

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-02 00:05:18

Please note that Sage 3.0.alphaX will contain updated linbox spkgs, so this will likely need to be rebased vs. that spkg. I would also very much like to base the new linbox.spkg on clean code and clear up all the patches and other cruft from that spkg.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-04 01:10:04

Fixed since #2525 was merged in Sage 3.0.alpha0


---

Comment by mabshoff created at 2008-04-04 01:10:04

Resolution: fixed
