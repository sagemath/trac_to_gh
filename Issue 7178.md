# Issue 7178: HP-UX  lcalc does not build. Also fails on Solaris with Sun compiler

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-10-10 09:06:02

Assignee: tbd

CC:  chapoton

Keywords: HP-UX Solaris

I think lcalc needs an overhall. Warnings were purposly ignored until I recently fixed that. It does not build with the Sun compiler - see #7056. It can't even appear to find the 'cp' command on HP-UX. 

 


```
                 from Lcommandline_values_zeros.cc:25:
../include/Lgamma.h: In function 'Complex gamma_sum(Complex, int, ttype*, int, Double, Complex, Double, Long, Complex, const char*) [with ttype = std::complex<double>]':
../include/Lvalue.h:510:   instantiated from 'Complex L_function<ttype>::value_via_gamma_sum(Complex, const char*) [with ttype = std::complex<double>]'
../include/Lvalue.h:590:   instantiated from 'Complex L_function<ttype>::value(Complex, int, const char*) [with ttype = std::complex<double>]'
$ ta(Complex, Double) [with ttype = int]':                                   <
Lcommandline_values_zeros.cc:68:   instantiated from here
../include/Lgamma.h:622: warning: unused variable 'y'
../include/Lgamma.h:622: warning: unused variable 'y2'
../include/Lgamma.h:622: warning: unused variable 'y3'
sh: ../include/Lvalue.h::  not found.
$ ue_via_gamma_sum(Complex, const char*) [with ttype = int]'                 <
../include/Lvalue.h:473: warning: control reaches end of non-void function

../include/Lvalue.h: In member function 'Complex L_function<ttype>::value_via_Riemann_sum(Complex, const char*) [with ttype = int]':
../include/Lvalue.h:473: warning: control reaches end of non-void function
In file included from ../include/L.h:520,
sh: ../include/Lvalue.h:501::  not found.
                 from ../include/Lcommandline_values_zeros.h:27,
                 from Lcommandline_values_zer$ ../include/Lvalue.h:590:   instan$ ue(Complex, int, const char*) [with ttype = int]'                          <
os.cc:25:
../include/Lfind_zeros.h: In member function 'Double L_function<ttype>::zeros_zoom_brent(Double, Double, Double, Double) sh: ../include/Lvalue.h:590::  not found.
$ Lcommandline_values_zeros.cc:57:   instantiated from here
[with ttype = double]':
../include/Lfind_zeros.h:31: warning: 'd' may be used uninitialized in this function
.sh: Lcommandline_values_zeros.cc:57::  not found.
$ ../include/Lvalue.h:37: warning: unused variable 'f2'
sh: ../include/Lvalue.h:37::  not found.
$ In file included from ../include/L.h:37,
./include/Lfind_zeros.h: In member function 'Double L_function<ttype>::zeros_zoom_brent(Double, Double, Double, Double) [with ttype = std::complex<double>]':
../include/Lfind_zeros.h:31: warning: 'd' may be used uninitialized in this function
../include/Lfind_zeros.h: In function 'Double L_function<ttype>::zeros_zoom_brent(Double, Double, Double, Double) [with ttype = int]':
../include/Lfind_zeros.h:31: warning: 'd' may be used uninitialized in this function
../include/Lfind_zeros.h: In function 'void L_function<ttype>::find_zeros_via_N(Long, bool, Double, int, const char*, const char*) [with ttype = std::complex<double>]':
../include/Lfind_zeros.h:433: warning: 'tmp2' may be used uninitialized in this function
../include/Lfind_zeros.h:433: warning: 'tL_function<ttype>::find_zeros_via_N(Long, bool, Double, int, const char*, const char*) [with ttype = double]':
../include/Lfind_zeros.h:646: warning: 'tmp3' may be used uninitialized in this function
../include/Lfind_zeros.h:433: warning: 'tmp2' may be used uninitialized in this function
Lgamma.cc: In function 'Complex erfc2(Complex)':
Lgamma.cc:158: warning: unused variable 'n'
*** Error exit code 1

Stop.
Now copying over lcalc binary
cp: cannot access lcalc: No such file or directory

real    1m49.990s
user    1m46.620s
sys     0m1.890s
sage: An error occurred while installing lcalc-20080205.p3
sh: In:  not found.
$                  from ../include/Lcommandline_values_zeros.h:27,
$                  from Lcommandline_values_zeros.cc:25:
$ lex, const char*) [with ttype = int]':                                     <
sh: ../include/Lgamma.h::  not found.
$ ue_via_gamma_sum(Complex, const char*) [with ttype = int]'                 <
sh: ../include/Lvalue.h:510::  not found.
$ ue(Complex, int, const char*) [with ttype = int]'                          <
sh: ../include/Lvalue.h:590::  not found.
$ Lcommandline_values_zeros.cc:57:   instantiated from here
sh: Lcommandline_values_zeros.cc:57::  not found.
$ ../include/Lgamma.h:622: warning: unused variable 'y'
sh: ../include/Lgamma.h:622::  not found.
$ ../include/Lgamma.h:622: warning: unused variable 'y2'
sh: ../include/Lgamma.h:622::  not found.
$ ../include/Lgamma.h:622: warning: unused variable 'y3'
sh: ../include/Lgamma.h:622::  not found.
$ In file included from ../include/L.h:519,
sh: In:  not found.
$                  from ../include/Lcommandline_values_zeros.h:27,
$                  from Lcommandline_values_zeros.cc:25:
$ ta(Complex, Double) [with ttype = double]':                                <
sh: ../include/Lvalue.h::  not found.
$ ue_via_gamma_sum(Complex, const char*) [with ttype = double]'              <
sh: ../include/Lvalue.h:501::  not found.
$ ue(Complex, int, const char*) [with ttype = double]'                       <
sh: ../include/Lvalue.h:590::  not found.
$ Lcommandline_values_zeros.cc:64:   instantiated from here
sh: Lcommandline_values_zeros.cc:64::  not found.
$ ../include/Lvalue.h:37: warning: unused variable 'f2'
sh: ../include/Lvalue.h:37::  not found.
$ In file included from ../include/L.h:37,
sh: In:  not found.
$                  from ../include/Lcommandline_values_zeros.h:27,
$                  from Lcommandline_values_zeros.cc:25:
$ lex, const char*) [with ttype = double]':                                  <
sh: ../include/Lgamma.h::  not found.
$ ue_via_gamma_sum(Complex, const char*) [with ttype = double]'              <
sh: ../include/Lvalue.h:510::  not found.
$ ue(Complex, int, const char*) [with ttype = double]'                       <
sh: ../include/Lvalue.h:590::  not found.
$ Lcommandline_values_zeros.cc:64:   instantiated from here
sh: Lcommandline_values_zeros.cc:64::  not found.
$ ../include/Lgamma.h:622: warning: unused variable 'y'
sh: ../include/Lgamma.h:622::  not found.
$ ../include/Lgamma.h:622: warning: unused variable 'y2'
sh: ../include/Lgamma.h:622::  not found.
$ ../include/Lgamma.h:622: warning: unused variable 'y3'
sh: ../include/Lgamma.h:622::  not found.
$ In file included from ../include/L.h:519,
sh: In:  not found.
$                  from ../include/Lcommandline_values_zeros.h:27,
$                  from Lcommandline_values_zeros.cc:25:
$ ta(Complex, Double) [with ttype = std::complex<double>]':                  <
sh: ../include/Lvalue.h::  not found.
$ ue_via_gamma_sum(Complex, const char*) [with ttype = std::complex<double>]'<
sh: ../include/Lvalue.h:501::  not found.
$ ue(Complex, int, const char*) [with ttype = std::complex<double>]'         <
sh: ../include/Lvalue.h:590::  not found.
$ Lcommandline_values_zeros.cc:68:   instantiated from here
sh: Lcommandline_values_zeros.cc:68::  not found.
$ ../include/Lvalue.h:37: warning: unused variable 'f2'
sh: ../include/Lvalue.h:37::  not found.
$ In file included from ../include/L.h:37,
sh: In:  not found.
$                  from ../include/Lcommandline_values_zeros.h:27,
$                  from Lcommandline_values_zeros.cc:25:
$ lex, const char*) [with ttype = std::complex<double>]':                    <
sh: ../include/Lgamma.h::  not found.
$ ue_via_gamma_sum(Complex, const char*) [with ttype = std::complex<double>]'<
sh: ../include/Lvalue.h:510::  not found.
$ ue(Complex, int, const char*) [with ttype = std::complex<double>]'         <
sh: ../include/Lvalue.h:590::  not found.
$ Lcommandline_values_zeros.cc:68:   instantiated from here
sh: Lcommandline_values_zeros.cc:68::  not found.
$ ../include/Lgamma.h:622: warning: unused variable 'y'
sh: ../include/Lgamma.h:622::  not found.
$ ../include/Lgamma.h:622: warning: unused variable 'y2'
sh: ../include/Lgamma.h:622::  not found.
$ ../include/Lgamma.h:622: warning: unused variable 'y3'
sh: ../include/Lgamma.h:622::  not found.
$ a_Riemann_sum(Complex, const char*) [with ttype = double]':                <
sh: ../include/Lvalue.h::  not found.
$ ../include/Lvalue.h:473: warning: control reaches end of non-void function
sh: ../include/Lvalue.h:473::  not found.
$ a_Riemann_sum(Complex, const char*) [with ttype = std::complex<double>]':  <
sh: ../include/Lvalue.h::  not found.
$ ../include/Lvalue.h:473: warning: control reaches end of non-void function
sh: ../include/Lvalue.h:473::  not found.
$ a_Riemann_sum(Complex, const char*) [with ttype = int]':                   <
sh: ../include/Lvalue.h::  not found.
$ ../include/Lvalue.h:473: warning: control reaches end of non-void function
sh: ../include/Lvalue.h:473::  not found.
$ In file included from ../include/L.h:520,
sh: In:  not found.
$                  from ../include/Lcommandline_values_zeros.h:27,
$                  from Lcommandline_values_zeros.cc:25:
$ s_zoom_brent(Double, Double, Double, Double) [with ttype = double]':       <
sh: ../include/Lfind_zeros.h::  not found.
$ 'd' may be used uninitialized in this function                             <
sh: ../include/Lfind_zeros.h:31::  not found.
$ ouble) [with ttype = std::complex<double>]':                               <
sh: ../include/Lfind_zeros.h::  not found.
$ 'd' may be used uninitialized in this function                             <
sh: ../include/Lfind_zeros.h:31::  not found.
$ brent(Double, Double, Double, Double) [with ttype = int]':                 <
sh: ../include/Lfind_zeros.h::  not found.
$ 'd' may be used uninitialized in this function                             <
sh: ../include/Lfind_zeros.h:31::  not found.
$ r*, const char*) [with ttype = std::complex<double>]':                     <
sh: ../include/Lfind_zeros.h::  not found.
$  'tmp2' may be used uninitialized in this function                         <
sh: ../include/Lfind_zeros.h:433::  not found.
$  'tmp3' may be used uninitialized in this function                         <
sh: ../include/Lfind_zeros.h:433::  not found.
$  'x3' may be used uninitialized in this function                           <
sh: ../include/Lfind_zeros.h:434::  not found.
$  'x3_c' may be used uninitialized in this function                         <
sh: ../include/Lfind_zeros.h:434::  not found.
$  'u3' may be used uninitialized in this function                           <
sh: ../include/Lfind_zeros.h:434::  not found.
$ a_N(Long, bool, Double, int, const char*, const char*) [with ttype = int]':<
sh: ../include/Lfind_zeros.h::  not found.
$  'tmp3' may be used uninitialized in this function                         <
sh: ../include/Lfind_zeros.h:646::  not found.
$  'tmp2' may be used uninitialized in this function                         <
sh: ../include/Lfind_zeros.h:433::  not found.
$ r*, const char*) [with ttype = double]':                                   <
sh: ../include/Lfind_zeros.h::  not found.
$  'tmp3' may be used uninitialized in this function                         <
sh: ../include/Lfind_zeros.h:646::  not found.
$  'tmp2' may be used uninitialized in this function                         <
sh: ../include/Lfind_zeros.h:433::  not found.
$ Lgamma.cc: In function 'Complex erfc2(Complex)':
sh: Lgamma.cc::  not found.
$ Lgamma.cc:158: warning: unused variable 'n'
sh: Lgamma.cc:158::  not found.
$ *** Error exit code 1
sh: 2016698240: Execute permission denied.
$
$ Stop.
sh: Stop.:  not found.
$ Now copying over lcalc binary
sh: Now:  not found.
$ cp: cannot access lcalc: No such file or directory
sh: cp::  not found.
$
$ real    1m49.990s
sh: real:  not found.
$ user    1m46.620s
sh: user:  not found.
$ sys     0m1.890s
sh: sys:  not found.
$ sage: An error occurred while installing lcalc-20080205.p3

```



---

Comment by jdemeyer created at 2015-09-08 12:45:40

Changing component from build to porting: AIX or HP-UX.


---

Comment by embray created at 2019-01-15 18:39:07

I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).


---

Comment by mkoeppe created at 2020-06-23 21:26:55

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-06-23 21:26:55

We should close this ticket as outdated.


---

Comment by chapoton created at 2020-06-24 06:27:55

Resolution: invalid
