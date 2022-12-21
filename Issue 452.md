# Issue 452: multi_polynomial_libsingular.c doesn't compile on Solaris

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-08-19 08:03:45

Assignee: malb

the compilation fails complaining about OSTREAM:

> gcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -
> fPIC -I/extra/home/mabshoff/SAGE-build/sage-2.8/local/include/singular
> -I/extra/home/mabshoff/SAGE-build/sage-2.8/local//include -I/extra/
> home/mabshoff/SAGE-build/sage-2.8/local//include/python -I/extra/home/
> mabshoff/SAGE-build/sage-2.8/devel//sage/sage/ext -I/extra/home/
> mabshoff/SAGE-build/sage-2.8/local/include/python2.5 -c sage/rings/
> polynomial/multi_polynomial_libsingular.cpp -o build/temp.solaris-2.9-
> sun4u-2.5/sage/rings/polynomial/multi_polynomial_libsingular.o -w
> cc1plus: warning: command line option "-Wstrict-prototypes" is valid
> for Ada/C/ObjC but not for C++
> In file included from /extra/home/mabshoff/SAGE-build/sage-2.8/local/
> include/singular/factory.h:43,
>                  from /extra/home/mabshoff/SAGE-build/sage-2.8/local/
> include/singular/interrupt.h:6,
>                  from sage/rings/polynomial/
> multi_polynomial_libsingular.cpp:30:
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_array.h:38: error: 'OSTREAM' has not been declared
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_array.h:44: error: expected constructor, destructor, or type
> conversion before '&' token
> In file included from /extra/home/mabshoff/SAGE-build/sage-2.8/local/
> include/singular/factory.h:44,
>                  from /extra/home/mabshoff/SAGE-build/sage-2.8/local/
> include/singular/interrupt.h:6,
>                  from sage/rings/polynomial/
> multi_polynomial_libsingular.cpp:30:
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_factor.h:40: error: 'OSTREAM' has not been declared
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_factor.h:49: error: expected constructor, destructor, or type
> conversion before '&' token
> In file included from /extra/home/mabshoff/SAGE-build/sage-2.8/local/
> include/singular/factory.h:45,
>                  from /extra/home/mabshoff/SAGE-build/sage-2.8/local/
> include/singular/interrupt.h:6,
>                  from sage/rings/polynomial/
> multi_polynomial_libsingular.cpp:30:
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_list.h:27: error: expected constructor, destructor, or type
> conversion before '&' token
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_list.h:47: error: 'OSTREAM' has not been declared
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_list.h:78: error: 'OSTREAM' has not been declared
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_list.h:79: error: ISO C++ forbids declaration of 'OSTREAM' with
> no type
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_list.h:79: error: 'OSTREAM' is neither function nor member
> function; cannot be declared friend
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_list.h:79: error: expected ';' before '&' token
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_list.h:86: error: expected constructor, destructor, or type
> conversion before '&' token
> In file included from /extra/home/mabshoff/SAGE-build/sage-2.8/local/
> include/singular/factory.h:46,
>                  from /extra/home/mabshoff/SAGE-build/sage-2.8/local/
> include/singular/interrupt.h:6,
>                  from sage/rings/polynomial/
> multi_polynomial_libsingular.cpp:30:
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_matrix.h:27: error: expected constructor, destructor, or type
> conversion before '&' token
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_matrix.h:37: error: 'OSTREAM' has not been declared
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_matrix.h:57: error: 'OSTREAM' has not been declared
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_matrix.h:58: error: ISO C++ forbids declaration of 'OSTREAM'
> with no type
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_matrix.h:58: error: 'OSTREAM' is neither function nor member
> function; cannot be declared friend
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_matrix.h:58: error: expected ';' before '&' token
> /extra/home/mabshoff/SAGE-build/sage-2.8/local//include/templates/
> ftmpl_matrix.h:93: error: expected constructor, destructor, or type
> conversion before '&' token
> In file included from /extra/home/mabshoff/SAGE-build/sage-2.8/local/
> include/singular/tmpl_inst.h:8,
>                  from /extra/home/mabshoff/SAGE-build/sage-2.8/local/
> include/singular/interrupt.h:8,
>                  from sage/rings/polynomial/
> multi_polynomial_libsingular.cpp:30:
> /extra/home/mabshoff/SAGE-build/sage-2.8/local/include/singular/
> class.h:43: error: 'OSTREAM' has not been declared
> /extra/home/mabshoff/SAGE-build/sage-2.8/local/include/singular/
> class.h:44: error: ISO C++ forbids declaration of 'OSTREAM' with no
> type
> /extra/home/mabshoff/SAGE-build/sage-2.8/local/include/singular/
> class.h:44: error: 'OSTREAM' is neither function nor member function;
> cannot be declared friend
> /extra/home/mabshoff/SAGE-build/sage-2.8/local/include/singular/
> class.h:44: error: expected ';' before '&' token
> /extra/home/mabshoff/SAGE-build/sage-2.8/local/include/singular/
> class.h:50: error: expected `;' before '}' token
> error: command 'gcc' failed with exit status 1
> sage: There was an error installing modified sage library code.



You can build libCF with and without IO support and apparently this got mixed
up. This is why we build a stand-alone libCF/libfac after we built SINGULAR
and libSINGULAR. This way we make sure OSTREAM is known properly. Short
answer: I'll have look at it.

Martin 


---

Comment by mabshoff created at 2007-08-21 15:09:38

Fixed by Martin Albrecht in  Singular-20070819p2.

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-21 15:09:38

Resolution: fixed


---

Comment by mabshoff created at 2007-08-22 02:00:57

Resolution changed from fixed to 


---

Comment by mabshoff created at 2007-08-22 02:00:57

Changing status from closed to reopened.


---

Comment by mabshoff created at 2007-08-22 02:00:57

Unfortunately, that new package breaks compilation on OSX and/or Linux. William has revered back to some former version of the spkg, so let's reopen this and target it at 2.8.3 and hope that it will be all sorted out be by then.

Cheers,

Michael


---

Comment by was created at 2007-08-30 00:12:38

Resolution: fixed
