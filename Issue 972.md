# Issue 972: SAGE 2.8.8.1 blows up building cddlib if libgmp is in /usr/local/lib

Issue created by migration from https://trac.sagemath.org/ticket/972

Original creator: justin

Original creation time: 2007-10-23 04:57:34

Assignee: was

I encountered this on Mac OS X (10.4.10), on a dual Quad Xeon system.  The build of cddlib-094b blows up here:

The build of cddlib-094b blows chunks, with this complaint:

g++  -I /SandBox/Justin/sb/sage-2.8.8.1/local/include   -L/usr/local/lib -o scdd_gmp  simplecdd.o ../lib-src-gmp/libcddgmp.a -lgmp

because of a separately-built libgmp there.

The error produces this complaint:
/usr/bin/ld: Undefined symbols:
___gmpq_add
___gmpq_clear
___gmpq_cmp
___gmpq_div
___gmpq_init
___gmpq_mul
___gmpq_set
___gmpq_sub
___gmpq_get_d
___gmpq_set_den
___gmpq_set_num
___gmpq_set_si
___gmpq_set_ui
___gmpz_clear
___gmpz_init
___gmpz_set_si
___gmpz_set_ui
___gmpq_canonicalize
___gmpq_get_den
___gmpq_get_num
___gmpz_cmp_ui
___gmpz_init_set_str
___gmpz_out_str
___gmpz_set


---

Comment by mabshoff created at 2007-11-30 08:57:31

Resolution: fixed


---

Comment by mabshoff created at 2007-11-30 08:57:31

This was fixed in 2.8.14 by an updated cddlib.spkg.

Cheers,

Michal
