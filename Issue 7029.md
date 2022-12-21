# Issue 7029: Sun C++ compiler does not accept  pynac C++ code

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-09-27 13:35:58

Assignee: tbd

CC:  dimpase

Using

    * Solaris 10 update 7 on SPARC
    * sage-4.1.2.alpha2
    * Sun Studio 12.1
    * An updated configure script to allow the Sun compiler to be used

I found that pynac-0.1.8.p2 will not build. It appears the Sun C++ compiler simply does not like the C++ code in 


```
 /opt/xxxsunstudio12.1/bin/CC -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include/python2.6 -g -c add.cpp  -KPIC -DPIC -o .libs/add.o
"/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include/python2.6/pyconfig.h", line 1004: Warning (Anachronism): Attempt to redefine _FILE_OFFSET_BITS without using #undef.
"numeric.h", line 328: Warning: GiNaC::numeric::compare hides the virtual function GiNaC::basic::compare(const GiNaC::basic&) const.
"container.h", line 692: Error: Could not find a match for std::list<GiNaC::ex>::unique(GiNaC::ex_is_equal) needed in GiNaC::container<std::list<std::_T, std::_Allocator>>::unique_().
"matrix.h", line 108: Error: Operand for operator "++" must be an lvalue.
"matrix.h", line 108: Error: Cannot cast from int to GiNaC::matrix_init<GiNaC::ex, GiNaC::ex*>.
"symbol.h", line 108: Warning: GiNaC::symbol::evalf hides the virtual function GiNaC::basic::evalf(int, int) const.
"add.cpp", line 46: Error: Could not find a match for GiNaC::registered_class_options::print_func<GiNaC::registered_class_options::Ctx, GiNaC::registered_class_options::T, GiNaC::registered_class_options::C>(void(GiNaC::add::*)(const GiNaC::print_context&,unsigned)const) needed in<no tag>.
"add.cpp", line 46: Error: Unexpected type name "GiNaC::print_latex" encountered.
"add.cpp", line 46: Error: Unexpected type name "GiNaC::print_csrc" encountered.
"add.cpp", line 46: Error: Unexpected type name "GiNaC::print_tree" encountered.
"add.cpp", line 46: Error: Unexpected type name "GiNaC::print_python_repr" encountered.
"add.cpp", line 46: Error: Could not find a match for GiNaC::registered_class_options::print_func<GiNaC::registered_class_options::Ctx, GiNaC::registered_class_options::T, GiNaC::registered_class_options::C>(void(GiNaC::add::*)(const GiNaC::print_context&,unsigned)const) needed in<no tag>.
"add.cpp", line 46: Error: void(GiNaC::add::*)(const GiNaC::print_latex&,unsigned)const is not a structure type.
"add.cpp", line 46: Error: void(GiNaC::add::*)(const GiNaC::print_csrc&,unsigned)const is not a structure type.
"add.cpp", line 46: Error: void(GiNaC::expairseq::*)(const GiNaC::print_tree&,unsigned)const is not a structure type.
"add.cpp", line 46: Error: Cannot cast from int to GiNaC::class_info<GiNaC::registered_class_options>.
13 Error(s) and 3 Warning(s) detected.
make[4]: *** [add.lo] Error 1
make[4]: Leaving directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/pynac-0.1.8.p2/src/ginac'
make[3]: *** [all-recursive] Error 1
make[3]: Leaving directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/pynac-0.1.8.p2/src'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/pynac-0.1.8.p2/src'
Error building pynac.

real    0m39.101s
user    0m20.604s
sys     0m17.258s
sage: An error occurred while installing pynac-0.1.8.p2
```


I do not know C++ myself. 




---

Comment by mkoeppe created at 2020-07-08 16:51:35

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Outdated, should be closed


---

Comment by mjo created at 2020-07-12 20:02:11

The goal of these tickets is laudable, but:

* We need at least one user who is able to test.
* The package/OS information on this ticket is outdated beyond usefulness.
* Upstream is a better place to report portability issues these days.


---

Comment by mjo created at 2020-07-12 20:02:11

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-07-15 07:18:41

Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.


---

Comment by chapoton created at 2020-07-15 07:18:41

Resolution: invalid
