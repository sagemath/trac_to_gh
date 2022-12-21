# Issue 9879: Segfault in PyNaC 0.2.0.p4

Issue created by migration from Trac.

Original creator: jpflori

Original creation time: 2010-09-09 09:01:09

Assignee: burcin

CC:  kcrisman zimmerma

Keywords: pynac

Here is a short example found by Burcin and reproducing the bug:

b = [var('b_%s'%i) for i in range(4)]

precomp = (2^b_2 + 2)*(2^b_1 + 2^(-b_1) + 2<sup>b_1*2</sup>b_0 - 2<sup>b_1*2</sup>(-b_0)
- 2<sup>(-b_1)*2</sup>b_0 - 2<sup>(-b_1)*2</sup>(-b_0) + 2^b_0 + 2^(-b_0) - 9) + (2^b_1 +
2^(-b_1) + 2<sup>b_1*2</sup>b_0 - 2<sup>b_1*2</sup>(-b_0) - 2<sup>(-b_1)*2</sup>b_0 -
2<sup>(-b_1)*2</sup>(-b_0) + 2^b_0 + 2^(-b_0) - 9)/2^b_2

repl_dict = {b_0: b_0, b_3: b_1, b_2: b_3, b_1: b_2}
P = precomp.substitute(repl_dict)
P.expand() 

This is already being discussed here:
http://groups.google.com/group/sage-support/browse_thread/thread/7c85f02c76012722


---

Comment by jpflori created at 2010-09-29 14:10:17

The bug happened because of the comparison functions which are used in a call to std::sort.

I have finally looked at the comparison functions and exchanging :


```
cmpval = seq[0].coeff.compare(other.exponent);
```

by


```
cmpval = -seq[0].coeff.compare(other.exponent);
```

in mul::compare_pow (mul.cpp:1265) seems to prevent the above bug from happening.

It seems to fit better with the change made by William Stein in power::compare_same_type (power.cpp:951).

However it doesn't mean the problem is completely solved...

I'll try to take a deeper look at the comparison functions at some point.

I tested the above fix with pynac 0.2.1.


---

Attachment

Burcin original patch


---

Comment by jpflori created at 2010-10-11 14:52:10

Patch to apply on top of the other one


---

Attachment

We've been working on a patch to fix the issue.

Original discussion is here:

http://groups.google.com/group/pynac-devel/browse_thread/thread/a36020bf9208bf08/abdf6671ef0b926a#abdf6671ef0b926a

Burcin produced a patch restoring GiNaC original order for internal use and using the new ones only for printing ; thus fixing the bug.

I then worked on top of it to get a more consistent order.

You can test them using pynac 0.2.1 from [#9901](http://trac.sagemath.org/sage_trac/search/opensearch?q=ticket%3A9901) ("cd spkg/standard/pynac-0.2.1/src/" then "hg import" both patches and build/install, you should "./sage -b" if upgrading from a previous version of pynac).

I don't consider that version as definitve, but would like to get some feedback on the order used for printing.

I don't use everything pynac provides so it is more than probable that some expression are not correctly printed now.

Do not hesitate to report it.


---

Comment by jpflori created at 2010-11-15 11:01:04

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-11-18 16:11:14

#10282 almost certainly is the same thing.


---

Comment by kcrisman created at 2010-11-18 16:18:04

Fixing this probably will close #9632 - just putting that here for the record.


---

Comment by vbraun created at 2010-11-24 01:20:48

Apply `trac_9880_revert_marking_random_from_trac_10187.patch` to re-enable doctests that fail on OSX/PPC.


---

Comment by kcrisman created at 2010-11-24 03:39:11

(Just OS X, not any particular architecture, I think.)


---

Attachment

Re-enable doctests that fail on PPC due to this issue (updated)


---

Comment by kcrisman created at 2011-01-13 16:08:17

> I don't use everything pynac provides so it is more than probable that some expression are not correctly printed now.
> 
> Do not hesitate to report it.

I'd like to test this at some point, but have two problems. 

 - There is too much C++ for me to review it properly, unless a lot of it really is just reverting.  Is there an easy way to figure out what is actual new code, and what is going back to something more-or-less Ginac?

 - I am not sure exactly what sort of expressions would not be properly printed.  Can you give any kind of example of what sort of bad behavior to look for with testing (perhaps randomized)?


---

Comment by jpflori created at 2011-01-13 16:34:56

I guess there are two main parts in this ticket, I did not have a look for a long time, so all this should be taken carefully :

- Burcin patch which (more or less) revert the internal ordering in Pynac to the original one in Ginac and create new methods to use a different order for printing. We could maybe only apply the part reverting the internal order to Ginac original one to get the bug solved and close this ticket.

- However, it is not a solution to use Ginac order for printing because it is quite random and unpredictable, it depends on variable order creation among others. That's the reason for the different order for printing (and getting operands and so on). It was not quite coherent, whence my patch to make it a little better. We could merge that in a second ticket. By the way, the order implemented right now should be more or less degrevlex.

- With that new framework, we could also quite easily allow the use of different orders for manipulating (ie printing, getting operands...) symbolic expressions in Sage (Burcin already mentionned that somewhere on the Web IIRC).

- I think there is still work to do regarding expressions manipulation (see #9989)

- I don't really have an idea of what could get misprinted with Burcin+my patch applied. You could try multivariate polynomials to check it follows degrevlex, then such expressions times exponentials and let me know what you feel.



---

Comment by vbraun created at 2011-01-13 16:36:11

I could review the c++ but the code in the ticket seems to work for me. If it segfaults for you, how about including a full sage session with a stack backtrace at the very least?


---

Comment by jpflori created at 2011-01-13 16:47:42

There is all you are asking for in the original discussion linked in the ticket description.

Maybe something changed since then, the ticket is quite old.


---

Comment by jpflori created at 2011-01-13 17:15:34

As far as I'm concerned, it still segfaults with the Sage 4.6 package for 32-bit Ubuntu provided on sagemath.org, as well as on a 64 bit Sage 4.6 that I built myself.

I did not test it any 4.6.1 alpha or rc yet.


---

Comment by jpflori created at 2011-01-14 07:31:44

I finally got Sage 4.6.1 final built from scratch, and:

 * indeed the specific instance of the bug mentionned here is no longer present
 * however, it does not mean that the bug is solved because:
   * nothing changed in pynac (IIRC)
   * the problem in the ordering used by pynac (which caused the bug when called within std::sort) are still present, I'll post a problematic expression asap

By the way, the problem of different ordering on different architecture should still be present (10187#!comment:39). 



---

Comment by jpflori created at 2011-01-14 09:36:42

Ok, here is a kind of strange example for the problems of ordering still hapenning with Sage 4.6.1:


```
sage: b_0,b_1,b_2=var('b_0,b_1,b_2')
sage: f = 1/27*b_2^2/(2^b_2)^2 + 1/27*b_1^2/(2^b_1)^2 + 1/27*b_0^2/(2^b_0)^2 + 1/27*b_2/(2^b_2)^2 - 2/81/(2^b_2)^2 + 1/27*b_1/(2^b_1)^2 + 8/243/(2^b_2)^2 - 1/81*b_0/(2^b_0)^2 - 1/27*b_1^2/((2^b_2)^2*(2^b_1)^2) - 1/27*b_0^2/((2^b_2)^2*(2^b_0)^2) - 20/243/(2^b_1)^2 + 1/9/2^b_0 + 4/81*b_0/(2^b_0)^2 - 8/243/(2^b_2)^2 - 2/9/(2^b_2*2^b_1) - 2/9/(2^b_2*2^b_0) + 8/243/(2^b_1)^2 - 1/9/2^b_0 + 2/9/(2^b_2*2^b_1) + 2/9/(2^b_2*2^b_0) - 2/27*b_1*b_2/((2^b_2)^2*(2^b_1)^2) - 1/27*b_2^2/((2^b_2)^2*(2^b_1)^2) - 2/27*b_0*b_2/((2^b_2)^2*(2^b_0)^2) - 1/27*b_2^2/((2^b_2)^2*(2^b_0)^2) + 2/81/(2^b_1)^2 - 1/27*b_0^2/((2^b_1)^2*(2^b_0)^2) - 2/27*b_0*b_1/((2^b_1)^2*(2^b_0)^2) - 1/27*b_1^2/((2^b_1)^2*(2^b_0)^2) - 2/81/(2^b_0)^2 + 5/27*b_1/((2^b_2)^2*(2^b_1)^2) + 5/27*b_2/((2^b_2)^2*(2^b_1)^2) + 5/27*b_0/((2^b_2)^2*(2^b_0)^2) + 5/27*b_2/((2^b_2)^2*(2^b_0)^2) + 5/27*b_0/((2^b_1)^2*(2^b_0)^2) + 5/27*b_1/((2^b_1)^2*(2^b_0)^2) - 4/81/((2^b_2)^2*(2^b_1)^2) + 1/27*b_0^2/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) + 2/27*b_0*b_1/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) + 2/27*b_0*b_2/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) + 1/27*b_1^2/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) + 2/27*b_1*b_2/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) + 1/27*b_2^2/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) - 4/81/((2^b_2)^2*(2^b_0)^2) - 4/81/((2^b_1)^2*(2^b_0)^2) - 11/27*b_0/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) - 11/27*b_1/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) - 11/27*b_2/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) + 64/81/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) + 35/81
sage: f
1/27*b_2^2/(2^b_2)^2 + 1/27*b_1^2/(2^b_1)^2 + 1/27*b_0^2/(2^b_0)^2 + 1/27*b_2/(2^b_2)^2 + 1/27*b_1/(2^b_1)^2 - 8/243/(2^b_2)^2 + 2/9/(2^b_2*2^b_1) + 2/9/(2^b_2*2^b_0) - 2/27*b_1*b_2/((2^b_2)^2*(2^b_1)^2) - 1/27*b_2^2/((2^b_2)^2*(2^b_1)^2) - 2/27*b_0*b_2/((2^b_2)^2*(2^b_0)^2) - 1/27*b_2^2/((2^b_2)^2*(2^b_0)^2) + 14/243/(2^b_1)^2 + 1/27*b_0/(2^b_0)^2 + 2/243/(2^b_2)^2 - 2/9/(2^b_2*2^b_1) - 2/9/(2^b_2*2^b_0) - 1/27*b_1^2/((2^b_2)^2*(2^b_1)^2) - 1/27*b_0^2/((2^b_2)^2*(2^b_0)^2) - 20/243/(2^b_1)^2 - 1/27*b_0^2/((2^b_1)^2*(2^b_0)^2) - 2/27*b_0*b_1/((2^b_1)^2*(2^b_0)^2) - 1/27*b_1^2/((2^b_1)^2*(2^b_0)^2) - 2/81/(2^b_0)^2 + 5/27*b_1/((2^b_2)^2*(2^b_1)^2) + 5/27*b_2/((2^b_2)^2*(2^b_1)^2) + 5/27*b_0/((2^b_2)^2*(2^b_0)^2) + 5/27*b_2/((2^b_2)^2*(2^b_0)^2) + 5/27*b_0/((2^b_1)^2*(2^b_0)^2) + 5/27*b_1/((2^b_1)^2*(2^b_0)^2) - 4/81/((2^b_2)^2*(2^b_1)^2) + 1/27*b_0^2/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) + 2/27*b_0*b_1/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) + 2/27*b_0*b_2/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) + 1/27*b_1^2/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) + 2/27*b_1*b_2/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) + 1/27*b_2^2/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) - 4/81/((2^b_2)^2*(2^b_0)^2) - 4/81/((2^b_1)^2*(2^b_0)^2) - 11/27*b_0/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) - 11/27*b_1/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) - 11/27*b_2/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) + 64/81/((2^b_2)^2*(2^b_1)^2*(2^b_0)^2) + 35/81


```

The expression for f should get (a little bit) simplified.

For example, there are different summands where the only symbolic expressions used are (2!<sup>b_2)!</sup>-2 and they should get automatically gathered when pynac creates the object.

In fact calling expand() method on f gives you the right expression, but if things were working correctly you should not have to do this.


---

Comment by gagern created at 2011-01-20 08:10:21

Can someone experiencing this bug please provide a gdb backtrace? There is a (small) possibility that this issue here might be related to [an issue](https://github.com/cschwan/sage-on-gentoo/issues/issue/40/#issue/40/comment/679235) I encounter with sage on Gentoo Linux (with segfault in PyNaC as well), and I'd like to know for sure whether the error occurs inside the function `__cxxabiv1::__cxa_allocate_exception` or not.


---

Comment by jpflori created at 2011-01-20 10:51:02

The detailed description of the segfault mentionned here is available in the discussion mentionned in the ticket description.

I'll put it here so that everybody finds it:

 * the segfault happens in a call to std::sort() in a call to compare() because the ordering used by pynac is not a strict weak ordering. so it is kind of random. and I think youre bug is completely unrelated.
 * the piece of code in the ticket description do not produce the segfault anymore since sage 4.6.1 (still present in 4.6.0), however the order was not changed, so it could still happen with other pieces of code, so here is a backtrace produce with a previous version of sage: 

!#0  GiNaC::power::compare (this=0x449be20, other=...) at !power.cpp:899 
 !#1  0x00007fffd7a9cc18 in void 
 std::!__unguarded_linear_insert<!__gnu_cxx::!__normal_iterator<GiNaC::expair*, 
 std::vector<GiNaC::expair, std::allocator<GiNaC::expair> > >, 
 GiNaC::expair, 
 GiNaC::expair_rest_is_less>(!__gnu_cxx::!__normal_iterator<GiNaC::expair*, 
 std::vector<GiNaC::expair, std::allocator<GiNaC::expair> > >, 
 GiNaC::expair, GiNaC::expair_rest_is_less) () 
    from /home/jp/boulot/thèse/sage/sage-4.5.2/local/lib/ 
 libpynac-0.2.so.0 
 !#2  0x00007fffd7a9cefa in void 
 std::!__final_insertion_sort<!__gnu_cxx::!__normal_iterator<GiNaC::expair*, 
 std::vector<GiNaC::expair, std::allocator<GiNaC::expair> > >, 
 GiNaC::expair_rest_is_less>(!__gnu_cxx::!__normal_iterator<GiNaC::expair*, 
 std::vector<GiNaC::expair, std::allocator<GiNaC::expair> > >, 
 !__gnu_cxx::!__normal_iterator<GiNaC::expair*, 
 std::vector<GiNaC::expair, std::allocator<GiNaC::expair> > >, 
 GiNaC::expair_rest_is_less) () from /home/jp/boulot/thèse/sage/ 
 sage-4.5.2/local/lib/libpynac-0.2.so.0 
 !#3  0x00007fffd7a95657 in 
 sort<!__gnu_cxx::!__normal_iterator<GiNaC::expair*, 
 std::vector<GiNaC::expair, std::allocator<GiNaC::expair> > >, 
 GiNaC::expair_rest_is_less> (this=<value optimized out>) at /usr/ 
 include/c++/4.4/bits/!stl_algo.h:5260 
 !#4  GiNaC::expairseq::canonicalize (this=<value optimized out>) at 
 !expairseq.cpp:1177 
 !#5  0x00007fffd7a994a4 in GiNaC::expairseq::construct_from_epvector 
 (this=0x44a5070, v=<value optimized out>, 
     do_index_renaming=<value optimized out>) at !expairseq.cpp:1055 
 !#6  0x00007fffd7a58685 in GiNaC::add::add (this=0x44a5070, vp=..., 
 oc=<value optimized out>) at !add.cpp:100 
 !#7  0x00007fffd7a5871f in GiNaC::add::expand (this=0x449eb80, 
 options=<value optimized out>) at !add.cpp:669 
 !#8  0x00007fffd7a9231d in GiNaC::ex::expand (this=<value optimized 
 out>, options=3620337048) at !ex.cpp:78 
 !#9  0x00007fffd773e386 in 
 !__pyx_pf_4sage_8symbolic_10expression_10Expression_expand 
 (!__pyx_v_self=<value optimized out>, 
     !__pyx_args=0x601160, !__pyx_kwds=0x0) at sage/symbolic/ 
 !expression.cpp:13604 
 !#10 0x00007ffff7b107ca in call_function (f=0x44a4580, throwflag=<value 
 optimized out>) at Python/!ceval.c:3706 
 !#11 PyEval_EvalFrameEx (f=0x44a4580, throwflag=<value optimized out>) 
 at Python/!ceval.c:2389 
 !#12 0x00007ffff7b124ad in PyEval_EvalCodeEx (co=0x79c4c0, 
 globals=<value optimized out>, locals=<value optimized out>, 
 args=0x0, 
     argcount=<value optimized out>, kws=0x0, kwcount=0, defs=0x0, 
 defcount=0, closure=0x0) at Python/!ceval.c:2968 
 !#13 0x00007ffff7b12582 in PyEval_EvalCode (co=0x449be20, 
 globals=0x1135200007879, locals=0x7fffd7c9f598) at Python/!ceval.c:522 
 !#14 0x00007ffff7b3014c in run_mod ( 
 . 
 . 
 . 


And valgrind output also: 
 ==27910== Invalid read of size 8 
 ==27910==    at 0x282C4BF1: void 
 std::!__unguarded_linear_insert<!__gnu_cxx::!__normal_iterator<GiNaC::expair*, 
 std::vector<GiNaC::expair, std::allocator<GiNaC::expair> > >, 
 GiNaC::expair, 
 GiNaC::expair_rest_is_less>(!__gnu_cxx::!__normal_iterator<GiNaC::expair*, 
 std::vector<GiNaC::expair, std::allocator<GiNaC::expair> > >, 
 GiNaC::expair, GiNaC::expair_rest_is_less) (!ptr.h:99) 
 ==27910==    by 0x282C4EF9: void 
 std::!__final_insertion_sort<!__gnu_cxx::!__normal_iterator<GiNaC::expair*, 
 std::vector<GiNaC::expair, std::allocator<GiNaC::expair> > >, 
 GiNaC::expair_rest_is_less>(!__gnu_cxx::!__normal_iterator<GiNaC::expair*, 
 std::vector<GiNaC::expair, std::allocator<GiNaC::expair> > >, 
 !__gnu_cxx::!__normal_iterator<GiNaC::expair*, 
 std::vector<GiNaC::expair, std::allocator<GiNaC::expair> > >, 
 GiNaC::expair_rest_is_less) (!stl_algo.h:2161) 
 ==27910==    by 0x282BD656: GiNaC::expairseq::canonicalize() 
 (!stl_algo.h:5260) 
 ==27910==    by 0x282C14A3: 
 GiNaC::expairseq::construct_from_epvector(std::vector<GiNaC::expair, 
 std::allocator<GiNaC::expair> > const&, bool) (!expairseq.cpp:1055) 
 ==27910==    by 0x28280684: 
 GiNaC::add::add(std::auto_ptr<std::vector<GiNaC::expair, 
 std::allocator<GiNaC::expair> > >, GiNaC::ex const&) (!add.cpp:100) 
 ==27910==    by 0x2828071E: GiNaC::add::expand(unsigned int) const 
 (!add.cpp:669) 
 ==27910==    by 0x282BA31C: GiNaC::ex::expand(unsigned int) const 
 (!ex.cpp:78) 
 ==27910==    by 0x28811385: 
 !__pyx_pf_4sage_8symbolic_10expression_10Expression_expand(_object*, 
 _object*, _object*) (!expression.cpp:13604) 
 ==27910==    by 0x4F137C9: PyEval_EvalFrameEx (!ceval.c:3706) 
 ==27910==    by 0x4F154AC: PyEval_EvalCodeEx (!ceval.c:2968) 
 ==27910==    by 0x4F15581: PyEval_EvalCode (!ceval.c:522) 
 ==27910==    by 0x4F3314B: PyRun_StringFlags (!pythonrun.c:1335) 
 ==27910==    by 0x4F122DD: PyEval_EvalFrameEx (!ceval.c:4437) 
 ==27910==    by 0x4F154AC: PyEval_EvalCodeEx (!ceval.c:2968) 
 ==27910==    by 0x4E9BDDE: function_call (!funcobject.c:524) 
 ==27910==    by 0x4E6FAA2: PyObject_Call (!abstract.c:2492) 
 ==27910==    by 0xD7E0981: 
 !__pyx_pf_4sage_9structure_11sage_object_load (!sage_object.c:7304) 
 ==27910==    by 0x4F137C9: PyEval_EvalFrameEx (!ceval.c:3706) 
 ==27910==    by 0x4F154AC: PyEval_EvalCodeEx (!ceval.c:2968) 
 ==27910==    by 0x4F15581: PyEval_EvalCode (!ceval.c:522) 
 ==27910==    by 0x4F14853: PyEval_EvalFrameEx (!ceval.c:4401) 
 ==27910==    by 0x4F154AC: PyEval_EvalCodeEx (!ceval.c:2968) 
 ==27910==    by 0x4F13844: PyEval_EvalFrameEx (!ceval.c:3802) 
 ==27910==    by 0x4F154AC: PyEval_EvalCodeEx (!ceval.c:2968) 
 ==27910==    by 0x4F13844: PyEval_EvalFrameEx (!ceval.c:3802) 
 ==27910==  Address 0x97e4280 is 16 bytes before a block of size 416 
 alloc'd 
 ==27910==    at 0x4C24CCC: operator new(unsigned long) 
 (!vg_replace_malloc.c:220) 
 ==27910==    by 0x28286727: std::vector<GiNaC::expair, 
 std::allocator<GiNaC::expair> >::reserve(unsigned long) 
 (!new_allocator.h:89) 
 ==27910==    by 0x282C0D4A: 
 GiNaC::expairseq::make_flat(std::vector<GiNaC::expair, 
 std::allocator<GiNaC::expair> > const&, bool) (!expairseq.cpp:1138) 
 ==27910==    by 0x282C149B: 
 GiNaC::expairseq::construct_from_epvector(std::vector<GiNaC::expair, 
 std::allocator<GiNaC::expair> > const&, bool) (!expairseq.cpp:1051) 
 ==27910==    by 0x28280684: 
 GiNaC::add::add(std::auto_ptr<std::vector<GiNaC::expair, 
 std::allocator<GiNaC::expair> > >, GiNaC::ex const&) (!add.cpp:100) 
 ==27910==    by 0x2828071E: GiNaC::add::expand(unsigned int) const 
 (!add.cpp:669) 
 ==27910==    by 0x282BA31C: GiNaC::ex::expand(unsigned int) const 
 (!ex.cpp:78) 
 ==27910==    by 0x28811385: 
 !__pyx_pf_4sage_8symbolic_10expression_10Expression_expand(_object*, 
 _object*, _object*) (!expression.cpp:13604) 
 ==27910==    by 0x4F137C9: PyEval_EvalFrameEx (!ceval.c:3706) 
 ==27910==    by 0x4F154AC: PyEval_EvalCodeEx (!ceval.c:2968) 
 ==27910==    by 0x4F15581: PyEval_EvalCode (!ceval.c:522) 
 ==27910==    by 0x4F3314B: PyRun_StringFlags (!pythonrun.c:1335) 
 ==27910==    by 0x4F122DD: PyEval_EvalFrameEx (!ceval.c:4437) 
 ==27910==    by 0x4F154AC: PyEval_EvalCodeEx (!ceval.c:2968) 
 ==27910==    by 0x4E9BDDE: function_call (!funcobject.c:524) 
 ==27910==    by 0x4E6FAA2: PyObject_Call (!abstract.c:2492) 
 ==27910==    by 0xD7E0981: 
 !__pyx_pf_4sage_9structure_11sage_object_load (!sage_object.c:7304) 
 ==27910==    by 0x4F137C9: PyEval_EvalFrameEx (!ceval.c:3706) 
 ==27910==    by 0x4F154AC: PyEval_EvalCodeEx (!ceval.c:2968) 
 ==27910==    by 0x4F15581: PyEval_EvalCode (!ceval.c:522) 
 ==27910==    by 0x4F14853: PyEval_EvalFrameEx (!ceval.c:4401) 
 ==27910==    by 0x4F154AC: PyEval_EvalCodeEx (!ceval.c:2968) 
 ==27910==    by 0x4F13844: PyEval_EvalFrameEx (!ceval.c:3802) 
 ==27910==    by 0x4F154AC: PyEval_EvalCodeEx (!ceval.c:2968) 
 ==27910==    by 0x4F13844: PyEval_EvalFrameEx (!ceval.c:3802)


---

Comment by vbraun created at 2011-02-28 14:47:22

Replying to [comment:17 jpflori]:
>  * the segfault happens in a call to std::sort() in a call to compare() because the ordering used by pynac is not a strict weak ordering. so it is kind of random.

`std::sort` with anything but a strict weak ordering is a receipe for disaster. It is expected to crash, and it does in the example. So you are saying that we must never use GiNaC internal order for sorting.

I take it that `expair_is_greater_degrevlex` does implement a strict weak ordering, so it is safe to use with `std::sort`?

Is the patch in this ticket still relevant or has this been fixed elsewhere?


---

Comment by jpflori created at 2011-02-28 17:22:19

The problem is not the GiNaC original internal order (even if http://www.ginac.de/reference/structGiNaC_1_1expair__rest__is__less.html states it is not a SWO... at least using it makes the bug disappear and inconsistencies in automatic simplifications disappear; if it does not work, i guess it should be fixed by GiNaC team) but the modification of that order used in pynac (and so in Sage).

AFAIK the two patches here are still necessary, the segfault disappeared (!?!) but i still get some problems with automatic simplification as shown in http://trac.sagemath.org/sage_trac/ticket/9880#comment:15.

- the first patch (by Burcin) reverts the original GiNaC ordering for internal use (e.g. to be used in call to std::sort) in pynac and use the modified order only for printing (it should also be uesd at some point for operands access and so on).

- the second one (by me) should be applied on top of the first one and tries to polish the order used for printing so that is looks more like degrevlex.

It should not be much more difficult to implement other orders for printing (and operands access).


---

Comment by vbraun created at 2011-02-28 17:41:16

I have a suspicion that gcc's `std::sort` implementation changed which hides the bug. But just because its hidden doesn't mean that its still there. I'm currently trying to install some old versions to test.


---

Comment by vbraun created at 2011-03-01 13:19:47

I don't understand  the GiNaC documentation that you referred to (http://www.ginac.de/reference/structGiNaC_1_1expair__rest__is__less.html). They state it is not a SWO, and their example is that neither 3*x<2*x nor 2*x<3*x. But thats perfectly fine in a SWO, you can have incomparable elements. The only constraint on incomparable elements is transitivity, that is, if A and B are incomparable and B and C are incomparable then A and C are also incomparable. Do you understand why its not a SWO?


---

Comment by burcin created at 2011-03-01 13:27:58

#10833 was a duplicate of this. Here is the example from that ticket:

```
phi(x) = x^2 + c
def iterkate(n):
    pol = x
    for i in range(1,n):
        pol = phi(pol)
    return pol
g = expand(iterkate(7))
```



---

Comment by jpflori created at 2011-03-01 13:32:38

Replying to [comment:21 vbraun]:

> I don't understand  the GiNaC documentation that you referred to (http://www.ginac.de/reference/structGiNaC_1_1expair__rest__is__less.html). They state it is not a SWO, and their example is that neither 3*x<2*x nor 2*x<3*x. But thats perfectly fine in a SWO, you can have incomparable elements. The only constraint on incomparable elements is transitivity, that is, if A and B are incomparable and B and C are incomparable then A and C are also incomparable. Do you understand why its not a SWO?

I have no idea why GiNaC order is not an SWO, my point was just to link that page where the GiNaC devs state it is not one.

However I never had problems with it so far, so maybe it is a SWO and the statement in GiNaC doc is just wrong.

We should post on GiNaC mailing list to get more info on that one. Maybe Burcin knows also.

What is definitely sure is that the modified order used in pynac is not correct. Because of it the result of a call to std::sort is flawed. This can be not too harmful (e.g. automatic simplification does not occur because terms which should be adjacent in the internal structure are not) but can also lead to segfaults (even if that dramatic side effect seems to depend on something mysterious, potentially on the gcc version used as you stated).

So at least for me, using the original GiNaC order solves many problems.


---

Comment by vbraun created at 2011-03-01 13:35:00

Burcin: If you are working on pynac, can you add some private function/method that exposes the GiNaC order to Sage in addition to the Sage (printing) order? Then we can add some randomized testing to make sure that both are strict weak orders.


---

Comment by jpflori created at 2011-03-01 14:43:06

Replying to [comment:24 vbraun]:

> Burcin: If you are working on pynac, can you add some private function/method that exposes the GiNaC order to Sage in addition to the Sage (printing) order? Then we can add some randomized testing to make sure that both are strict weak orders.

Calling the _cmp_ method of an expression should give you access to pynac internal ordering (i.e. with the patched spkg, it is GiNaC original ordering; with the old one you would get the modified order currently used by pynac).

For example (with the new spkg):


```
sage: var('a b')
(a, b)
sage: x._cmp_(a)
1
sage: a._cmp_(b)
1
sage: a+b
a + b
sage: x+a
a + x

```

In GiNaC order, vars are ordered according to creation order iirc. So here we have x (automatically created) > a > b.

For printing, we use lexicographic order a > b > x and print bigger terms first.

To check it the only current way is to look at what gets printed, the internal ordering is used for everything else.

I'll try to post a minimal patch to have access to that order in sage.


---

Comment by jpflori created at 2011-03-01 16:23:02

Here you go:

 1. Install the new spkg available at http://perso.telecom-paristech.fr/~flori/pynac-0.2.1-order.spkg
 1. Apply pynac-order.patch
 1. Rebuild Sage
 1. Expession elements have now two new methods _cmp_add and _cmp_mul giving access to the order used for printing.

_cmp_add is (more or less) the function used to order elements in a sum and _cmp_mul in a product. Their behavior is not exactly the same (don't remember why, it's been a while).


---

Attachment

Access to comparison function used for printing.


---

Comment by vbraun created at 2011-03-02 10:52:15

Jean-Pierre: I think paristech.fr has some issues at the moment, can you upload it somewhere else?


---

Comment by jpflori created at 2011-03-02 11:23:17

Changing assignee from burcin to jpflori.


---

Comment by jpflori created at 2011-03-02 11:23:17

You can try accessing the same server at http://www.enst.fr/~flori/ or another one form the school at http://www.infres.enst.fr/~flori/ (same content, other server).

I've put also the package at http://viedethesarde.free.fr/sage/

You should get the file pynac-0.2.1-patched.spkg (not the -order one I deleted anyway).

It is quite the same as the one you would get by applying the patches of the ticket to pyanc-0.2.1.


---

Comment by jpflori created at 2011-03-02 11:24:24

Changing assignee from jpflori to burcin.


---

Comment by vbraun created at 2011-03-02 12:54:30

For the record, both the snippet in the ticket description and the `iterkate()` example reliably crash Sage-4.6.1 on Ubuntu-9.04. 

The updated pynac-0.2.1-patched.spkg fixes this problem, and sage no longer crashes.


---

Comment by vbraun created at 2011-03-02 14:19:47

Randomized testing of orders


---

Attachment

With the attached script I find some examples in `cmp_add` where `a<b<c<a`. This violates SWO:

```
sage: attach strict_weak_order.py
sage: test_symbolic_expression_order(10000)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/vbraun/Sage/Order/<ipython console> in <module>()

/home/vbraun/Sage/Order/strict_weak_order.py in test_symbolic_expression_order(repetitions)
    113         c = make_random_expr()
    114         assert_strict_weak_order(a, b, c, lambda x,y: x._cmp_(y))
--> 115         assert_strict_weak_order(a, b, c, lambda x,y: x._cmp_add(y))
    116         assert_strict_weak_order(a, b, c, lambda x,y: x._cmp_mul(y))
    117 

/home/vbraun/Sage/Order/strict_weak_order.py in assert_strict_weak_order(a, b, c, cmp_func)
     63             
     64     for i,j,k in Permutations([0,1,2]):   # transitivity
---> 65         if cmp[i,j] and cmp[j,k] and not cmp[i,k]: raise ValueError, msg
     66 
     67     def incomparable(i,j):

ValueError: The binary relation failed to be a strict weak order on the elements
 a = 2*v10*(v5 - 2)*v7 + (-(v8 + e)*(-v8 + pi) + v6)*(v9*e - 2) - v2 - v3 - v5 - v9
 b = -(v3*v8 - 51*v2 - 105)*(v2 + 5)*(v3 - 1) + 3*v6*v9
 c = -v1*v6*brun + v6*v9*pi + 3*(7*(v5 + 1)*v7 - 3)*(-(v3 - 1)*e + v4) - (v5 - 4)*(v9 + 8) - v3 - 3
[0 0 1]
[1 0 0]
[0 1 0]
```



---

Comment by jpflori created at 2011-03-02 14:26:22

Not sure it is related, but i found the ordering of functions is currently random for functions having the same name.

I'm currently fixing this.


---

Comment by jpflori created at 2011-03-02 18:35:07

Ok that was unrelated.

It happened because some types were not handled by the new ordering and compared type ids directly which screw things up.

I launched a big test with your program and we'll see if it has reported any problems tomorrow.


---

Comment by jpflori created at 2011-03-03 15:18:24

I uploaded a new version of the spkg that you can get at:

http://www.infres.enst.fr/~flori/pynac-0.2.1-patched.spkg

or:

http://perso.telecom-paristech.fr/~flori/pynac-0.2.1-patched.spkg

I'm still running tests using test_symbolic_expression_order but did not get new errors.


---

Comment by jpflori created at 2011-04-15 09:12:34

New version of patch, apply after burcin original one to build updated spkg


---

Comment by vbraun created at 2011-05-04 14:59:57

Changing status from needs_review to needs_work.


---

Attachment

Jean-Pierre: Are you now finished with running your tests? Can you bring the spkg into a reviewable state? At the very least it should be called pynac-0.2.1.p0.spkg and have a SPKG.txt entry.


---

Comment by burcin created at 2011-05-04 15:22:08

Please excuse my ignorance, especially since I promised to make a pynac release which includes this patch ages ago, but I have a few questions and not enough time to test this and find out the answers on my own:

 * doesn't this require a patch to the Sage library at least to fix doctests? Is the new printing order exactly the same as the old (inconsistent) one?

 * Don't we also need to modify the operand access functions (at least the one in Sage - not the .op() function of ginac) to return the operands in the sorted order, not the stored (somewhat random) order? 


BTW, Jean-Pierre, I wouldn't mind at all if you want to cut the new pynac release yourself. I can provide instructions on how to do this.


---

Comment by jpflori created at 2011-05-04 15:35:45

Replying to [comment:36 burcin]:

> * doesn't this require a patch to the Sage library at least to fix doctests? Is the new printing order exactly the same as the old (inconsistent) one?
I don't think this order and the old one will coincide and a lot of doctests will have to be fixed if we use it.
I'll try to have a look at all of this soon, I must admit I did not touch that code since my last post here.
> * Don't we also need to modify the operand access functions (at least the one in Sage - not the .op() function of ginac) to return the operands in the sorted order, not the stored (somewhat random) order?
I think you are right.
I did not test it but it should return unexpected values with the new code.
I'll include that when the new order seems consistent.
> BTW, Jean-Pierre, I wouldn't mind at all if you want to cut the new pynac release yourself. I can provide instructions on how to do this.
Please go ahead, I'll find the time to do it.

I'm currently rebuilding everything and running some tests, but IIRC the piece of code Volker provided did not raise errors anymore.
Of course there could be other inconsistencies here and there.


---

Comment by jpflori created at 2011-05-05 08:17:20

I did not get inconsistencies using Volker code yet. I'll package a candidate updated spkg today so that someone can have a look at the code update in pynac.

I'll do a proper pynac release when the code is positively reviewed and Burcin tells me how to.

Here is the list of doctests failure with the new spkg:


```
----------------------------------------------------------------------

The following tests failed:

	sage -t  -force_lib devel/sage/doc/en/constructions/polynomials.rst # 1 doctests failed
	sage -t  -force_lib devel/sage/doc/en/constructions/calculus.rst # 7 doctests failed
	sage -t  -force_lib devel/sage/doc/en/tutorial/tour_algebra.rst # 3 doctests failed
	sage -t  -force_lib devel/sage/doc/en/tutorial/introduction.rst # 2 doctests failed
	sage -t  -force_lib devel/sage/doc/en/a_tour_of_sage/index.rst # 1 doctests failed
	sage -t  -force_lib devel/sage/doc/en/bordeaux_2008/nf_introduction.rst # 1 doctests failed
	sage -t  -force_lib devel/sage/doc/fr/tutorial/tour_algebra.rst # 3 doctests failed
	sage -t  -force_lib devel/sage/doc/fr/tutorial/introduction.rst # 2 doctests failed
	sage -t  -force_lib devel/sage/doc/fr/a_tour_of_sage/index.rst # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/modules/vector_callable_symbolic_dense.py # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/modules/free_module_element.pyx # 3 doctests failed
	sage -t  -force_lib devel/sage/sage/interfaces/maxima_abstract.py # 3 doctests failed
	sage -t  -force_lib devel/sage/sage/interfaces/maxima_lib.py # 2 doctests failed
	sage -t  -force_lib devel/sage/sage/numerical/optimize.py # 2 doctests failed
	sage -t  -force_lib devel/sage/sage/tensor/differential_form_element.py # 2 doctests failed
	sage -t  -force_lib devel/sage/sage/rings/integer.pyx # 2 doctests failed
	sage -t  -force_lib devel/sage/sage/rings/qqbar.py # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/rings/power_series_ring.py # 2 doctests failed
	sage -t  -force_lib devel/sage/sage/rings/number_field/number_field_element.pyx # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/rings/polynomial/polynomial_element.pyx # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/gsl/dft.py # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/calculus/functional.py # 12 doctests failed
	sage -t  -force_lib devel/sage/sage/calculus/tests.py # 16 doctests failed
	sage -t  -force_lib devel/sage/sage/calculus/desolvers.py # 14 doctests failed
	sage -t  -force_lib devel/sage/sage/calculus/calculus.py # 19 doctests failed
	sage -t  -force_lib devel/sage/sage/calculus/test_sympy.py # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/calculus/functions.py # 3 doctests failed
	sage -t  -force_lib devel/sage/sage/calculus/wester.py # 10 doctests failed
	sage -t  -force_lib devel/sage/sage/calculus/var.pyx # 2 doctests failed
	sage -t  -force_lib devel/sage/sage/categories/classical_crystals.py # 2 doctests failed
	sage -t  -force_lib devel/sage/sage/combinat/perfect_matching.py # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/combinat/partition.py # 2 doctests failed
	sage -t  -force_lib devel/sage/sage/combinat/sf/ns_macdonald.py # 2 doctests failed
	sage -t  -force_lib devel/sage/sage/ext/fast_callable.pyx # 3 doctests failed
	sage -t  -force_lib devel/sage/sage/schemes/elliptic_curves/ell_generic.py # 2 doctests failed
	sage -t  -force_lib devel/sage/sage/stats/basic_stats.py # 7 doctests failed
	sage -t  -force_lib devel/sage/sage/functions/log.py # 2 doctests failed
	sage -t  -force_lib devel/sage/sage/functions/hyperbolic.py # 3 doctests failed
	sage -t  -force_lib devel/sage/sage/functions/special.py # 4 doctests failed
	sage -t  -force_lib devel/sage/sage/functions/orthogonal_polys.py # 4 doctests failed
	sage -t  -force_lib devel/sage/sage/functions/trig.py # 5 doctests failed
	sage -t  -force_lib devel/sage/sage/functions/wigner.py # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/functions/other.py # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/functions/piecewise.py # 12 doctests failed
	sage -t  -force_lib devel/sage/sage/matrix/matrix_symbolic_dense.pyx # 17 doctests failed
	sage -t  -force_lib devel/sage/sage/matrix/matrix2.pyx # 3 doctests failed
	sage -t  -force_lib devel/sage/sage/symbolic/function_factory.py # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/symbolic/maxima_wrapper.py # 14 doctests failed
	sage -t  -force_lib devel/sage/sage/symbolic/expression_conversions.py # 7 doctests failed
	sage -t  -force_lib devel/sage/sage/symbolic/ring.pyx # 3 doctests failed
	sage -t  -force_lib devel/sage/sage/symbolic/constants.py # 4 doctests failed
	sage -t  -force_lib devel/sage/sage/symbolic/random_tests.py # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/symbolic/relation.py # 13 doctests failed
	sage -t  -force_lib devel/sage/sage/symbolic/function.pyx # 2 doctests failed
	sage -t  -force_lib devel/sage/sage/symbolic/callable.py # 2 doctests failed
	sage -t  -force_lib devel/sage/sage/symbolic/assumptions.py # 11 doctests failed
	sage -t  -force_lib devel/sage/sage/symbolic/integration/integral.py # 9 doctests failed
	sage -t  -force_lib devel/sage/sage/symbolic/expression.pyx # 162 doctests failed
	sage -t  -force_lib devel/sage/sage/plot/plot3d/plot3d.py # 6 doctests failed
	sage -t  -force_lib devel/sage/sage/misc/preparser.py # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/misc/functional.py # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/graphs/generic_graph.py # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/misc/prandom.py # 1 doctests failed
	sage -t  -force_lib devel/sage/sage/misc/parser.pyx # 2 doctests failed
----------------------------------------------------------------------

```

I hope that all of them are trivial...

One question for Burcin: when you speak of operand access, are you thinking of #9989 or am I missing something in the current Sage code ?


---

Comment by jpflori created at 2011-05-05 09:15:57

A new spkg is available at http://perso.telecom-paristech.fr/~flori/sage/pynac-0.2.1.p0.spkg .

I just updated SPKG.txt and commited the changeset in comparison with pynac-0.2.1-patched.spkg .

The changes i pynac code from 0.2.1 are the result of applying:

 1. [trac9880_pynac_order_burcin_original.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9880/trac9880_pynac_order_burcin_original.patch)
 1. [trac_9880-pynac_order_jp_new-p2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9880/trac_9880-pynac_order_jp_new-p2.patch)

If you want to have access to the comparison functions used by the printing order (to stress pynac with Volker code [strict_weak_order.py](http://trac.sagemath.org/sage_trac/attachment/ticket/9880/strict_weak_order.py) for example) you must also apply the patch access_order.patch .


---

Comment by burcin created at 2011-05-07 14:44:59

I don't want to delay this any further, but if this is merged all patches touching anything symbolic will need to be rebased. I suggest we try to review and merge any feasible symbolics tickets for the next release. Then this gets merged for 4.8 with big warnings, since users would also need to change doctests in any private code they might have.

I can actually spare time for such an effort now. I will see what I can do with the needs review/work tickets on trac starting tomorrow.


BTW, we should also include Volker's test script. Perhaps as a part of `sage/symbolics/random_tests.py`.

Jean-Pierre: Yes, by operand access I mean the `.operands()` and the recent `.op` from #9989.


Making a pynac release is just a matter of editing `configure.ac`, setting the version number according to the comments there and running `autoreconf` afterwards. I am not sure any more if the next pynac release should contain this. This can be pynac 0.3.0, and I will put in the patches in my queue corresponding to some of the tickets waiting on trac for 0.2.2.

Note that I imported the pynac-0.2.1 repository into bitbucket:

https://bitbucket.org/burcin/pynac

I hope to use the facilities there to streamline the development process.


---

Comment by vbraun created at 2011-06-15 00:37:33

Initial patch


---

Attachment

Initial patch


---

Attachment

Initial patch


---

Comment by burcin created at 2011-06-15 03:50:52

I changed the structure of the order classes a little. New patches are available in my pynac queue:

https://bitbucket.org/burcin/pynac-patches/src

attachment:trac_9880_pynac_order.take2.patch should be applied to access these functions from Sage.


---

Comment by burcin created at 2011-06-16 19:48:23

updated JP's patch for sage library to work with the new order patches


---

Attachment


---

Attachment


---

Comment by kcrisman created at 2011-06-16 19:58:42

What remains for 'needs review' so one could review it?


---

Comment by burcin created at 2011-06-16 20:10:34

Replying to [comment:44 kcrisman]:
> What remains for 'needs review' so one could review it?

Volker has changes to pynac to fix simplification of expressions involving infinity when we can't assume anything about the internal ordering.

I am trying to fix printing of `mul` objects where we get `-` right after a parenthesis, such as `-(4*cos(x)^2 - 1)*sin(x)/(-4*cos(x)^3 + 3*cos(x))`.

It might be good to update my [attachment:trac_9880-stable_operands.patch] to make it optional to use the printing order.

Then a lot of doctests need to get fixed. We also need to document that `.find()`, `.match()` and friends will not return results in a canonical order any more and that expressions constructed with `hold =True` do not print in the order provided by the user.


---

Attachment

Initial patch


---

Comment by vbraun created at 2011-06-17 19:08:49

Patch fixes the segfault 

```
sage: x._cmp_add(1)
```



---

Attachment

Fixed commit message.


---

Comment by vbraun created at 2011-06-18 03:11:59

Initial patch


---

Attachment

The `trac_9880-fix_doctests_symbolic.patch` fixes the bulk of the doctests in `sage.symbolic.expression.pyx` and `sage.symbolic.random_tests.py`. There are a few remaining that depend on a random sign in the print output that Burcin is fixing right now.


---

Comment by vbraun created at 2011-06-21 18:24:12

tdupu on `#sagemath` reported the following on sage-4.7.1.alpha2:

```
sage: ff = 117306*x^2 + x
sage: gg = x + 7^3*x^2
sage: R.<x> = PolynomialRing(ZZ.quotient(7^6),1)
sage: ggred = R(gg)
sage: print expand(ff(x=ggred))
0*x^4 + 0*x^3
sage: print expand(ggred(x=ff))
x
```

This is also fixed in the updated pynac and now prints `x` both times.


---

Comment by burcin created at 2011-06-28 13:57:17

I updated my [pynac queue](https://bitbucket.org/burcin/pynac-patches) with a new patch that fixes the random sign Volker mentioned in comment:48. It turns out that the issue is bigger. The result printed in some cases might be wrong, since the internal structure of an `add` object is modified when `seq_sorted` is already stored. I added an assert statement in `{add,mul}::get_sorted_seq()` to test consistency. With the `minus.patch` from my queue applied, I still get crashes while testing `sage/calculus/tests.py`. So this needs more work.


---

Comment by jpflori created at 2011-06-28 14:09:20

Thanks for working on this.

I'll try to build your updated version and have a look at the crashes this week.


---

Comment by jpflori created at 2011-09-19 13:46:22

So I'm finally having a look at that.

Here are some examples producing the bug or not:


```
sage: var('t')
t
sage: (x-t)^3
(-t + x)^3
sage: (-t+x)^3
(-t + x)^3
sage: (-x+t)^3

Program received signal...
sage: (t-x)^3

Program received signal...
sage: var('z')
z
sage: (-x+z)^3
-(x - z)^3
sage: (x-z)^3
(x - z	)^3
sage: (-z+x)^3
(x - z)^3
sage: (z-x)^3
-(x - z)^3
sage: var('y')
y
sage: (y-t)^3
-(t - y)^3
sage: (t-y)^3
(t - y)^3
sage: (-y+z)^3
(-y + z)^3
sage: (y-z)^3

Program received signal ...
```



---

Comment by jpflori created at 2011-09-19 15:51:43

I guess the problem lies in line 1528 of mul.cpp.

When building the new mul object if there is a leading minus, I think it enters an infinite loop.

And isn't there a better way to check for leading minus than to emulate printing (even at the cost of duplicating some code) ?


---

Comment by burcin created at 2011-09-19 16:21:45

I updated my patch-queue with some small but important fixes to the handling of these leading minuses. Please update and try that version. There updates were sitting on my hard disk for months, so I need some time to remember the details again.

Replying to [comment:53 jpflori]:
> And isn't there a better way to check for leading minus than to emulate printing (even at the cost of duplicating some code) ?

Since the coefficient can be any Sage type, I don't think there is any way to get that information without printing. IIRC, GiNaC handles this by defining the csgn() function appropriately, but they don't support as many types and printing styles as we do.


---

Comment by jpflori created at 2011-09-19 18:00:03

I think I used all the patch from your above link.

I'll have a closer look at it.

Did you also tried the examples I gave above?


---

Comment by jpflori created at 2011-09-20 09:47:17

My bad, I thought you spoke of your previous changes...

I just recloned your repo and all the above tests now pass.


---

Comment by jpflori created at 2011-09-20 11:17:18

Just a remark: some of your patches in the queue do not have an author set (I mean inside the Mercurial header).


---

Comment by jpflori created at 2011-09-20 15:41:18

The latest version of the patch giving access to the internal printing functions, gives the operator() instead of the compare(...) functions.

I'm not sure this was intended, even if it is completely ok for the randomized testing.

Anyway the line using it is cmp(..) == 1, so going back to the previous semantic is also ok.

Hence I've provided a modified patch to do it.

I'll also reversed the arguments in _cmp_c_impl and get rid of the minus sign.

I do not see any reason for this choice, but if there was, please revert my change.


---

Attachment


---

Comment by jpflori created at 2011-09-21 09:05:41

There is a little glitch left in pynac which made SR(1) > SR(2).


---

Attachment


---

Comment by jpflori created at 2011-09-21 09:36:06

The "variable" ordering somehow got reversed at some point.

The following patch fixes that.


---

Attachment

Revert previous ordering for "variables" function


---

Comment by jpflori created at 2011-09-21 09:40:07

Apart from changes in the printing order, we now get the following error:


```
sage: print ((a+b)*(a+c)).match((w0+w1)*(w0+w2))
Expected:
    {$2: b, $0: a, $1: c}
Got:
    None
```



---

Attachment


---

Comment by burcin created at 2011-11-25 17:02:19

I've just pushed updates to my pynac patch queue that include Jean-Pierre's `numerics.patch`, a preliminary fix for `match()` and some attempts to fix the random effects of normalization of minus signs on printing. I don't expect all of these to be committed, they are work in progress.

I also uploaded a slightly changed version of Volker's doctest fix patch [attachment:trac_9880-fix_doctests_symbolic.take2.patch], and a new patch [attachment:trac_9880-fix_doctests-be.patch] fixing many more doctests which I believe to be correct.

Running the test suite on `sage/{symbolic,function}` directories after these patches shows more clearly that there is still some work to be done here. We get some random output from `.factor()`  and `.numerator()` calls (#12068), and a timeout on `sage/calculus/calculus.py` since `minpoly` doesn't terminate.


Here is my current sage patch queue in case you decide to apply the new patches:

```
trac_12068-numer_denom_ginac-fh.patch
trac_12068-denominator.patch
trac_12074-nth_root.patch
trac_9880_fix_import.patch
trac_9880_pynac_order.take2.patch
trac_9880_randomized_testing.patch
trac_9880-stable_operands.patch
trac_9880_pynac_infinities.patch
trac_9880-fix_comparison-p1.patch
trac_9880-fix_variables_ordering.patch
trac_9880-fix_doctests_symbolic.patch
trac_9880-fix_doctests-be.patch
```

I'll write to pynac-devel with more details of the remaining problems.


---

Comment by jpflori created at 2011-11-27 00:20:37

Here is a small example producing the random minus sign problem for anyone wanting to investigate it apart from Burcin and I:

```
sage -c "var('x y z'); print (-x+z)*(3*x-3*z)"
```



---

Comment by burcin created at 2012-07-10 09:28:10

This fixes #9046 as well. I attached [attachment:trac_9880-doctest_for_9046.patch] to add the example there as a doctest.

We don't need [attachment:trac_9880_pynac_infinities.patch] since that was merged in #12950, so I removed it from the patches listed in the description.

Naturally the doctest patches, the last two in the list, have bitrotted. The rest seems to apply fine, though I only tried with 5.0.beta13.


---

Attachment


---

Attachment


---

Attachment


---

Attachment

I rebased the patches to Sage 5.5.rc0, dropping doctest fixes that resulted in nontrivial conflicts on the way.

Volker's [attachment:trac_9880_fix_import.patch] is now on #13737.

My Sage patch queue contains Pynac 0.2.6 associated patches from #13262, #13609, #13587. The patches on this ticket might apply cleanly without those, I haven't tried.


---

Attachment


---

Attachment


---

Attachment

I rebased the patches to 5.9.

Here is an example where `minpoly()` does not terminate:


```
sage: var('x')
x
sage: eqn =  x^3 + sqrt(2)*x + 5 == 0
sage: a = solve(eqn, x)[0].rhs()
sage: a
-1/2*(1/18*sqrt(3)*sqrt(8*sqrt(2) + 675) - 5/2)^(1/3)*(I*sqrt(3) + 1) - 1/6*sqrt(2)*(I*sqrt(3) - 1)/(1/18*sqrt(3)*sqrt(8*sqrt(2) + 675) - 5/2)^(1/3)
sage: QQ[a]
```

or 

```
sage: a.minpoly()
```



---

Attachment


---

Attachment

I think this is finally good to be tested.

There is a new Pynac spkg (it's just for testing) and updated patches on this ticket. I'm working with vanilla 5.9. Note that this ticket now depends on #13213 for the fixes to the quadratic number field ordering.

Please test and report results.


---

Comment by jpflori created at 2013-05-10 14:24:59

Looks fine and some hand feeded examples pass!
I guess what's left to do is:
* cleanup Volker's patch (blank lines, http://...trac... -> :trac:, becasue->because, EXAMPLE[S]: -> EXAMPLE[S]::)
* merge related paches to ease readibility for reviewers (=me?),
* add some doctests using previously failing examples: from #10833, from ticket description, from comment 15 (http://trac.sagemath.org/sage_trac/ticket/9880#comment:15), maybe 52 http://trac.sagemath.org/sage_trac/ticket/9880#comment:52 and 67 http://trac.sagemath.org/sage_trac/ticket/9880#comment:67
* craft a proper spkg
* make sure it cleanly applies on 5.10.beta2 and passes all doctests
* positive review!


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Comment by burcin created at 2013-05-10 17:11:59

Changing status from needs_work to needs_review.


---

Comment by burcin created at 2013-05-10 17:11:59

I uploaded new patches that do almost everything suggested in comment:72. Remaining items are:

 * make a proper spkg
 * check all doctests

I will make a new Pynac release and upload the tarball to the web site soon. Running doctests on the whole tree now.

I'm setting this to `needs_review`. Please test and report any problems.


---

Comment by vbraun created at 2013-05-10 18:10:28

I get a bunch of doctest failures because of changed term orders, stuff like

```
File "devel/sage/sage/plot/plot3d/plot3d.py", line 418, in sage.plot.plot3d.plot3d.Spherical
Failed example:
    T.transform(radius=r, azimuth=theta, inclination=phi)
Expected:
    (r*sin(phi)*cos(theta), r*sin(phi)*sin(theta), r*cos(phi))
Got:
    (r*cos(theta)*sin(phi), r*sin(phi)*sin(theta), r*cos(phi))
```



---

Comment by jpflori created at 2013-05-13 10:51:02

Yup, Burcin only corrected the doctests in the symbolic or something like that.

Burcin, are you working on this or do you prefer that I take care of correcting the doctests?
I had a look and it really looks like ordering change only, so is harmless and trivial to change.

By the way, I'm ok with all the other patches, so this should get in once we fix the doctests!


---

Comment by burcin created at 2013-05-13 21:59:15

I only checked the `sage/symbolics` directory and a few other files, then switched to `needs_review` to see if anyone saw major problems before changing all the other doctests. Then travel and real life came in. I will only be able to look at this again Thursday afternoon. If you have time to take care of the remaining doctests, please go ahead.

BTW, we still need #13213 reviewed before this can go in.


---

Comment by jpflori created at 2013-05-16 20:33:35

I've had a quick look at the failing doctests and think there is no real problem hidden there.

The only thing which may be a little distrubing is that now we print

```
(2*x+1)*x^2
```

rather than

```
x^2*(2*x+1)
```


This should be easily fixed in pynac hopefully, but even if not I don't think it should be a blocker.

The other disturbing thing is than fractions get automatically modified when they used not to be:

```
File "devel/sage/doc/ru/tutorial/introduction.rst", line 49, in doc.ru.tutorial.introduction
Failed example:
    k = 1/(sqrt(3)*I + 3/4 + sqrt(73)*5/9); k
Expected:
    1/(I*sqrt(3) + 5/9*sqrt(73) + 3/4)
Got:
    36/(20*sqrt(73) + 36*I*sqrt(3) + 27)
```


Apart from that we also get a lot of nicer things now (in addition to bug fixes) than before.


---

Comment by zimmerma created at 2013-05-22 08:45:55

I cannot review this patch for the doctests of our book in french, since the dependency patch
#13213 does not apply to Sage 5.9 (which is the version we use in the book):

```
applying /tmp/trac_13213-quadratic_field_comparison.patch
patching file sage/schemes/elliptic_curves/ell_number_field.py
Hunk #1 FAILED at 1347
1 out of 3 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_number_field.py.rej
abort: patch failed to apply
```


Paul


---

Attachment


---

Comment by burcin created at 2013-05-23 11:13:39

I uploaded a new patch [attachment: trac_9880-fix_doctests-sage_5_10_beta2.take2.patch] to fix all doctest in the library (as opposed to the few symbolics related directories I was working with).

Now all that remains is to make a proper spkg, and someone to look over the doctest changes to see if there is anything fishy.


---

Comment by jpflori created at 2013-05-23 12:46:25

Thanks Burcin!
I was finally going to do it today, but you were faster than me.
At least I can give it a try on beta4 and check there is nothing else to fix (all other patches apply cleanly.

I'd really like other people (let's say at least one) to have a look at the new order before you finalize 3.0 (or if it's already finalized/tagged in your repo make a 3.1 or 3.0.1) in case we want to make minimal changes.
E.g. I don't reallylike the following, but do not really mind as well:
Replying to [comment:77 jpflori]:
> The only thing which may be a little distrubing is that now we print
> {{{
> (2*x+1)*x^2
> }}}
> rather than
> {{{
> x^2*(2*x+1)
> }}}
> 
> This should be easily fixed in pynac hopefully, but even if not I don't think it should be a blocker.
But it would be really better to make these changes, if we plan to make them, before merging the ticket, so that people preparing books (I'm thinking of the french book which is in the process of being published) can expect their examples to pass for a quite long amount of time (or at least not to fail in the next version of Sage).


---

Comment by burcin created at 2013-05-26 10:06:12

Replying to [comment:81 jpflori]:
> Thanks Burcin!
> I was finally going to do it today, but you were faster than me.
> At least I can give it a try on beta4 and check there is nothing else to fix (all other patches apply cleanly.
> 
> I'd really like other people (let's say at least one) to have a look at the new order before you finalize 3.0 (or if it's already finalized/tagged in your repo make a 3.1 or 3.0.1) in case we want to make minimal changes.

I agree. This is the reason I set this ticket to needs review even though it was failing tests all over the library. :)

I tagged the 0.3.0 release already, but I can easily make a 0.3.1 if necessary.

> E.g. I don't reallylike the following, but do not really mind as well:
> Replying to [comment:77 jpflori]:
> > The only thing which may be a little distrubing is that now we print
> > {{{
> > (2*x+1)*x^2
> > }}}
> > rather than
> > {{{
> > x^2*(2*x+1)
> > }}}
> > 
> > This should be easily fixed in pynac hopefully, but even if not I don't think it should be a blocker.
> But it would be really better to make these changes, if we plan to make them, before merging the ticket, so that people preparing books (I'm thinking of the french book which is in the process of being published) can expect their examples to pass for a quite long amount of time (or at least not to fail in the next version of Sage).

Feel free to submit patches to pynac with necessary changes. I don't have time to work on this any more right now, but I can spare some minutes to make a new release with simple patches.

That said, I'd really like this ticket to go in as soon as possible. It really is not fun to maintain the patch with the doctest fixes.


---

Comment by jpflori created at 2013-05-27 12:31:10

Burcin, could you reup a proper spkg? i.e. with just an additional line in SPKG.txt and an hg commit message?


---

Comment by burcin created at 2013-05-27 13:23:06

Replying to [comment:83 jpflori]:
> Burcin, could you reup a proper spkg? i.e. with just an additional line in SPKG.txt and an hg commit message?

I updated the spkg at the URL given in the description with a new one.

Many thanks for reviewing this!


---

Attachment

Updated patch to apply to 5.10.beta5 without fuzz


---

Comment by jpflori created at 2013-05-27 13:25:25

Reviewer patch, fix two doctests.


---

Attachment


---

Comment by jpflori created at 2013-05-27 13:31:29

A very little rant: could you mention the ticket number in the hg commit message as well, I know it's already in SPKG.txt but for lazy people as me it avoids to have to run two commands (if unlucky) before finding out the trac ticket number?
And I think it's not necessary to tag the spkg new version, Jeroen scripts will do it automatically.
I don't say it's a good thing, but it's the way it is now.
Nevertheless, tagging the spkg yourself shouldn't be an issue IIRC.


---

Comment by burcin created at 2013-05-27 17:47:36

It's been quite a while since the last time I made an `spkg`. New version is up at the same URL with a ticket number in the commit message, and no tags. :)

That reminds me... I need to update the pynac web site to mention the release.


---

Comment by jpflori created at 2013-05-27 19:04:15

It seems the tag was added to the last commit and you then removed it.
Anyway, I'll just repackage it properly.


---

Comment by jpflori created at 2013-05-27 19:39:16

Spkg diff, for review only.


---

Comment by jpflori created at 2013-05-27 19:40:30

Changing status from needs_review to positive_review.


---

Comment by jpflori created at 2013-05-27 19:40:30

Changing keywords from "pynac" to "pynac spkg".


---

Attachment


---

Comment by jdemeyer created at 2013-05-28 20:29:24

Please rebase to #14550.


---

Comment by jdemeyer created at 2013-05-28 20:29:24

Changing status from positive_review to needs_work.


---

Comment by burcin created at 2013-05-29 08:07:56

Changing status from needs_work to positive_review.


---

Comment by burcin created at 2013-05-29 08:07:56

Replying to [comment:91 jdemeyer]:
> Please rebase to #14550.

Done.


---

Comment by jdemeyer created at 2013-05-29 12:33:25

Please rebase to #9890 (the latest patch applies with fuzz 2).


---

Comment by jdemeyer created at 2013-05-29 12:33:25

Changing status from positive_review to needs_work.


---

Attachment

Replying to [comment:94 jdemeyer]:
> Please rebase to #9890 (the latest patch applies with fuzz 2).

Done.


---

Comment by burcin created at 2013-05-29 12:56:44

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2013-06-06 12:35:30

Resolution: fixed
