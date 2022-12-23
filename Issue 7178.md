# Issue 7178: HP-UX  lcalc does not build. Also fails on Solaris with Sun compiler

archive/issues_007178.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  chapoton\n\nKeywords: HP-UX Solaris\n\nI think lcalc needs an overhall. Warnings were purposly ignored until I recently fixed that. It does not build with the Sun compiler - see #7056. It can't even appear to find the 'cp' command on HP-UX. \n\n \n\n\n```\n                 from Lcommandline_values_zeros.cc:25:\n../include/Lgamma.h: In function 'Complex gamma_sum(Complex, int, ttype*, int, Double, Complex, Double, Long, Complex, const char*) [with ttype = std::complex<double>]':\n../include/Lvalue.h:510:   instantiated from 'Complex L_function<ttype>::value_via_gamma_sum(Complex, const char*) [with ttype = std::complex<double>]'\n../include/Lvalue.h:590:   instantiated from 'Complex L_function<ttype>::value(Complex, int, const char*) [with ttype = std::complex<double>]'\n$ ta(Complex, Double) [with ttype = int]':                                   <\nLcommandline_values_zeros.cc:68:   instantiated from here\n../include/Lgamma.h:622: warning: unused variable 'y'\n../include/Lgamma.h:622: warning: unused variable 'y2'\n../include/Lgamma.h:622: warning: unused variable 'y3'\nsh: ../include/Lvalue.h::  not found.\n$ ue_via_gamma_sum(Complex, const char*) [with ttype = int]'                 <\n../include/Lvalue.h:473: warning: control reaches end of non-void function\n\n../include/Lvalue.h: In member function 'Complex L_function<ttype>::value_via_Riemann_sum(Complex, const char*) [with ttype = int]':\n../include/Lvalue.h:473: warning: control reaches end of non-void function\nIn file included from ../include/L.h:520,\nsh: ../include/Lvalue.h:501::  not found.\n                 from ../include/Lcommandline_values_zeros.h:27,\n                 from Lcommandline_values_zer$ ../include/Lvalue.h:590:   instan$ ue(Complex, int, const char*) [with ttype = int]'                          <\nos.cc:25:\n../include/Lfind_zeros.h: In member function 'Double L_function<ttype>::zeros_zoom_brent(Double, Double, Double, Double) sh: ../include/Lvalue.h:590::  not found.\n$ Lcommandline_values_zeros.cc:57:   instantiated from here\n[with ttype = double]':\n../include/Lfind_zeros.h:31: warning: 'd' may be used uninitialized in this function\n.sh: Lcommandline_values_zeros.cc:57::  not found.\n$ ../include/Lvalue.h:37: warning: unused variable 'f2'\nsh: ../include/Lvalue.h:37::  not found.\n$ In file included from ../include/L.h:37,\n./include/Lfind_zeros.h: In member function 'Double L_function<ttype>::zeros_zoom_brent(Double, Double, Double, Double) [with ttype = std::complex<double>]':\n../include/Lfind_zeros.h:31: warning: 'd' may be used uninitialized in this function\n../include/Lfind_zeros.h: In function 'Double L_function<ttype>::zeros_zoom_brent(Double, Double, Double, Double) [with ttype = int]':\n../include/Lfind_zeros.h:31: warning: 'd' may be used uninitialized in this function\n../include/Lfind_zeros.h: In function 'void L_function<ttype>::find_zeros_via_N(Long, bool, Double, int, const char*, const char*) [with ttype = std::complex<double>]':\n../include/Lfind_zeros.h:433: warning: 'tmp2' may be used uninitialized in this function\n../include/Lfind_zeros.h:433: warning: 'tL_function<ttype>::find_zeros_via_N(Long, bool, Double, int, const char*, const char*) [with ttype = double]':\n../include/Lfind_zeros.h:646: warning: 'tmp3' may be used uninitialized in this function\n../include/Lfind_zeros.h:433: warning: 'tmp2' may be used uninitialized in this function\nLgamma.cc: In function 'Complex erfc2(Complex)':\nLgamma.cc:158: warning: unused variable 'n'\n*** Error exit code 1\n\nStop.\nNow copying over lcalc binary\ncp: cannot access lcalc: No such file or directory\n\nreal    1m49.990s\nuser    1m46.620s\nsys     0m1.890s\nsage: An error occurred while installing lcalc-20080205.p3\nsh: In:  not found.\n$                  from ../include/Lcommandline_values_zeros.h:27,\n$                  from Lcommandline_values_zeros.cc:25:\n$ lex, const char*) [with ttype = int]':                                     <\nsh: ../include/Lgamma.h::  not found.\n$ ue_via_gamma_sum(Complex, const char*) [with ttype = int]'                 <\nsh: ../include/Lvalue.h:510::  not found.\n$ ue(Complex, int, const char*) [with ttype = int]'                          <\nsh: ../include/Lvalue.h:590::  not found.\n$ Lcommandline_values_zeros.cc:57:   instantiated from here\nsh: Lcommandline_values_zeros.cc:57::  not found.\n$ ../include/Lgamma.h:622: warning: unused variable 'y'\nsh: ../include/Lgamma.h:622::  not found.\n$ ../include/Lgamma.h:622: warning: unused variable 'y2'\nsh: ../include/Lgamma.h:622::  not found.\n$ ../include/Lgamma.h:622: warning: unused variable 'y3'\nsh: ../include/Lgamma.h:622::  not found.\n$ In file included from ../include/L.h:519,\nsh: In:  not found.\n$                  from ../include/Lcommandline_values_zeros.h:27,\n$                  from Lcommandline_values_zeros.cc:25:\n$ ta(Complex, Double) [with ttype = double]':                                <\nsh: ../include/Lvalue.h::  not found.\n$ ue_via_gamma_sum(Complex, const char*) [with ttype = double]'              <\nsh: ../include/Lvalue.h:501::  not found.\n$ ue(Complex, int, const char*) [with ttype = double]'                       <\nsh: ../include/Lvalue.h:590::  not found.\n$ Lcommandline_values_zeros.cc:64:   instantiated from here\nsh: Lcommandline_values_zeros.cc:64::  not found.\n$ ../include/Lvalue.h:37: warning: unused variable 'f2'\nsh: ../include/Lvalue.h:37::  not found.\n$ In file included from ../include/L.h:37,\nsh: In:  not found.\n$                  from ../include/Lcommandline_values_zeros.h:27,\n$                  from Lcommandline_values_zeros.cc:25:\n$ lex, const char*) [with ttype = double]':                                  <\nsh: ../include/Lgamma.h::  not found.\n$ ue_via_gamma_sum(Complex, const char*) [with ttype = double]'              <\nsh: ../include/Lvalue.h:510::  not found.\n$ ue(Complex, int, const char*) [with ttype = double]'                       <\nsh: ../include/Lvalue.h:590::  not found.\n$ Lcommandline_values_zeros.cc:64:   instantiated from here\nsh: Lcommandline_values_zeros.cc:64::  not found.\n$ ../include/Lgamma.h:622: warning: unused variable 'y'\nsh: ../include/Lgamma.h:622::  not found.\n$ ../include/Lgamma.h:622: warning: unused variable 'y2'\nsh: ../include/Lgamma.h:622::  not found.\n$ ../include/Lgamma.h:622: warning: unused variable 'y3'\nsh: ../include/Lgamma.h:622::  not found.\n$ In file included from ../include/L.h:519,\nsh: In:  not found.\n$                  from ../include/Lcommandline_values_zeros.h:27,\n$                  from Lcommandline_values_zeros.cc:25:\n$ ta(Complex, Double) [with ttype = std::complex<double>]':                  <\nsh: ../include/Lvalue.h::  not found.\n$ ue_via_gamma_sum(Complex, const char*) [with ttype = std::complex<double>]'<\nsh: ../include/Lvalue.h:501::  not found.\n$ ue(Complex, int, const char*) [with ttype = std::complex<double>]'         <\nsh: ../include/Lvalue.h:590::  not found.\n$ Lcommandline_values_zeros.cc:68:   instantiated from here\nsh: Lcommandline_values_zeros.cc:68::  not found.\n$ ../include/Lvalue.h:37: warning: unused variable 'f2'\nsh: ../include/Lvalue.h:37::  not found.\n$ In file included from ../include/L.h:37,\nsh: In:  not found.\n$                  from ../include/Lcommandline_values_zeros.h:27,\n$                  from Lcommandline_values_zeros.cc:25:\n$ lex, const char*) [with ttype = std::complex<double>]':                    <\nsh: ../include/Lgamma.h::  not found.\n$ ue_via_gamma_sum(Complex, const char*) [with ttype = std::complex<double>]'<\nsh: ../include/Lvalue.h:510::  not found.\n$ ue(Complex, int, const char*) [with ttype = std::complex<double>]'         <\nsh: ../include/Lvalue.h:590::  not found.\n$ Lcommandline_values_zeros.cc:68:   instantiated from here\nsh: Lcommandline_values_zeros.cc:68::  not found.\n$ ../include/Lgamma.h:622: warning: unused variable 'y'\nsh: ../include/Lgamma.h:622::  not found.\n$ ../include/Lgamma.h:622: warning: unused variable 'y2'\nsh: ../include/Lgamma.h:622::  not found.\n$ ../include/Lgamma.h:622: warning: unused variable 'y3'\nsh: ../include/Lgamma.h:622::  not found.\n$ a_Riemann_sum(Complex, const char*) [with ttype = double]':                <\nsh: ../include/Lvalue.h::  not found.\n$ ../include/Lvalue.h:473: warning: control reaches end of non-void function\nsh: ../include/Lvalue.h:473::  not found.\n$ a_Riemann_sum(Complex, const char*) [with ttype = std::complex<double>]':  <\nsh: ../include/Lvalue.h::  not found.\n$ ../include/Lvalue.h:473: warning: control reaches end of non-void function\nsh: ../include/Lvalue.h:473::  not found.\n$ a_Riemann_sum(Complex, const char*) [with ttype = int]':                   <\nsh: ../include/Lvalue.h::  not found.\n$ ../include/Lvalue.h:473: warning: control reaches end of non-void function\nsh: ../include/Lvalue.h:473::  not found.\n$ In file included from ../include/L.h:520,\nsh: In:  not found.\n$                  from ../include/Lcommandline_values_zeros.h:27,\n$                  from Lcommandline_values_zeros.cc:25:\n$ s_zoom_brent(Double, Double, Double, Double) [with ttype = double]':       <\nsh: ../include/Lfind_zeros.h::  not found.\n$ 'd' may be used uninitialized in this function                             <\nsh: ../include/Lfind_zeros.h:31::  not found.\n$ ouble) [with ttype = std::complex<double>]':                               <\nsh: ../include/Lfind_zeros.h::  not found.\n$ 'd' may be used uninitialized in this function                             <\nsh: ../include/Lfind_zeros.h:31::  not found.\n$ brent(Double, Double, Double, Double) [with ttype = int]':                 <\nsh: ../include/Lfind_zeros.h::  not found.\n$ 'd' may be used uninitialized in this function                             <\nsh: ../include/Lfind_zeros.h:31::  not found.\n$ r*, const char*) [with ttype = std::complex<double>]':                     <\nsh: ../include/Lfind_zeros.h::  not found.\n$  'tmp2' may be used uninitialized in this function                         <\nsh: ../include/Lfind_zeros.h:433::  not found.\n$  'tmp3' may be used uninitialized in this function                         <\nsh: ../include/Lfind_zeros.h:433::  not found.\n$  'x3' may be used uninitialized in this function                           <\nsh: ../include/Lfind_zeros.h:434::  not found.\n$  'x3_c' may be used uninitialized in this function                         <\nsh: ../include/Lfind_zeros.h:434::  not found.\n$  'u3' may be used uninitialized in this function                           <\nsh: ../include/Lfind_zeros.h:434::  not found.\n$ a_N(Long, bool, Double, int, const char*, const char*) [with ttype = int]':<\nsh: ../include/Lfind_zeros.h::  not found.\n$  'tmp3' may be used uninitialized in this function                         <\nsh: ../include/Lfind_zeros.h:646::  not found.\n$  'tmp2' may be used uninitialized in this function                         <\nsh: ../include/Lfind_zeros.h:433::  not found.\n$ r*, const char*) [with ttype = double]':                                   <\nsh: ../include/Lfind_zeros.h::  not found.\n$  'tmp3' may be used uninitialized in this function                         <\nsh: ../include/Lfind_zeros.h:646::  not found.\n$  'tmp2' may be used uninitialized in this function                         <\nsh: ../include/Lfind_zeros.h:433::  not found.\n$ Lgamma.cc: In function 'Complex erfc2(Complex)':\nsh: Lgamma.cc::  not found.\n$ Lgamma.cc:158: warning: unused variable 'n'\nsh: Lgamma.cc:158::  not found.\n$ *** Error exit code 1\nsh: 2016698240: Execute permission denied.\n$\n$ Stop.\nsh: Stop.:  not found.\n$ Now copying over lcalc binary\nsh: Now:  not found.\n$ cp: cannot access lcalc: No such file or directory\nsh: cp::  not found.\n$\n$ real    1m49.990s\nsh: real:  not found.\n$ user    1m46.620s\nsh: user:  not found.\n$ sys     0m1.890s\nsh: sys:  not found.\n$ sage: An error occurred while installing lcalc-20080205.p3\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7178\n\n",
    "created_at": "2009-10-10T09:06:02Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "HP-UX  lcalc does not build. Also fails on Solaris with Sun compiler",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7178",
    "user": "drkirkby"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/7178





---

archive/issue_comments_059461.json:
```json
{
    "body": "Changing component from build to porting: AIX or HP-UX.",
    "created_at": "2015-09-08T12:45:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7178#issuecomment-59461",
    "user": "jdemeyer"
}
```

Changing component from build to porting: AIX or HP-UX.



---

archive/issue_comments_059462.json:
```json
{
    "body": "I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).",
    "created_at": "2019-01-15T18:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7178#issuecomment-59462",
    "user": "embray"
}
```

I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).



---

archive/issue_comments_059463.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7178#issuecomment-59463",
    "user": "mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059464.json:
```json
{
    "body": "We should close this ticket as outdated.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7178#issuecomment-59464",
    "user": "mkoeppe"
}
```

We should close this ticket as outdated.



---

archive/issue_comments_059465.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-06-24T06:27:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7178#issuecomment-59465",
    "user": "chapoton"
}
```

Resolution: invalid
