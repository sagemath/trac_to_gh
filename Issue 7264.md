# Issue 7264: segfault while substituting powers of exp

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2009-10-22 08:25:50

Assignee: burcin


```
On Wed, 21 Oct 2009 19:49:58 -0700 (PDT)
Ichnich <warmbau`@`web.de> wrote:

> Hi,
> 
> something does not work anymore in my notebook (with version 4.1.2
> ubuntu 64bit):
>
> var('a,b,c,I')
> model(I)=a*I+b
> model_exp = exp(I)**a*(b)
> sol1_l={b: 5.0, a: 1.1}
> model_sol1_l(I)=model_exp.subs(sol1_l)
> 
> The notebook hangs-up. It's critical on the parameter a, if you change
> it to 1.0 it's o.k.
```


I can reproduce this:


```
sage: var('a,b,c,I')
(a, b, c, I)
sage: model_exp = exp(I)**a*(b)
sage: sol1_l={b: 5.0, a: 1.1}
sage: model_exp.subs(sol1_l)
/home/burcin/sage/sage-4.1.2/local/bin/sage-sage: line 203: 23916
Segmentation fault      sage-ipython "$`@`" -i
```


The cause might be #6948.


---

Comment by jason created at 2009-11-04 17:23:58

In 4.2:


```
sage: var('a,b,c,I')
(a, b, c, I)
sage: model_exp=exp(I)**a*(b)
sage: sol1_l={b: 5.0, a: 1.1}
sage: model_exp.subs(sol1_l)
/home/grout/sage/local/bin/sage-sage: line 203: 23853 Segmentation fault      sage-ipython "$`@`" -i
```


Since 4.2 has #6948 merged in, I guess that was not the cause.


---

Comment by burcin created at 2009-11-22 17:58:18

Changing status from new to needs_review.


---

Comment by burcin created at 2009-11-22 17:58:18

This was indeed caused by the changes to pynac from #6948. I forgot to adjust
automatic simplification of pynac `mul` objects to the new exp power rule. 

This is fixed in the new pynac package here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.10.spkg

attachment:trac_7264-exp_power_segfault.patch adds doctests for the fix.

Note that the new pynac version also contains fixes for #7508 and #7406. Tests should be run with the patches from those tickets also applied in this order:

 * #7508
 * #7264 (this ticket)
 * #7406

This ticket now depends on #7490 and #7508.


---

Comment by burcin created at 2009-11-22 17:58:18

Changing keywords from "" to "pynac".


---

Attachment

add doctests


---

Comment by kcrisman created at 2009-12-04 17:12:29

I would like to review this, but installing Pynac 0.1.10 caused an error (not in sage -i, but with sage -br after that):

```
error: command 'gcc' failed with exit status 1
sage: There was an error installing modified sage library code.
```

What is the base version of Sage for this ticket (e.g., 4.3)?


---

Comment by burcin created at 2009-12-04 21:51:20

Hi Karl-Dieter,

Did you have #7490 applied to your tree?

That patch was merged in 4.3.alpha1, so you can also try updating to the latest alpha.

Thank you for your time.


---

Comment by kcrisman created at 2009-12-05 13:52:42

This needs work, because somehow the following test with the new spkg causes a segfault (Mac OSX 10.5, Intel):

```
sage: exp(x)^I*exp(z)^(2.5)


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```

However, everything else behaves properly, so if this can be fixed, all three tickets will have positive review.  These are important fixes, so thanks for the work!


---

Comment by kcrisman created at 2009-12-05 13:52:42

Changing status from needs_review to needs_work.


---

Comment by burcin created at 2009-12-05 22:11:32

Can you post a backtrace? I can't reproduce the problem and I have no clue what might be going wrong.

To get a backtrace, you need to run Sage under gdb as the error message says. When it crashes, type `bt`, then copy and paste the output here.

Starting from a clean install, and making sure there is nothing else to effect this test could also help.


---

Comment by kcrisman created at 2009-12-06 02:16:38

This was a fresh build of 4.3.alpha1.  Only issue was that I had to hg -add several files to be able to add patches, and revert the two png files Minh has mentioned on sage-devel.  But I don't see how that would have affected things.

```
sage: exp(x)^I*exp(z)^(2.5)

Program received signal EXC_BAD_ACCESS, Could not access memory.
Reason: KERN_INVALID_ADDRESS at address: 0xc23d006b
0x0658315e in GiNaC::Number_T::operator/ ()
(gdb) bt
#0  0x0658315e in GiNaC::Number_T::operator/ ()
#1  0x065837bb in GiNaC::numeric::div ()
#2  0x06549c14 in GiNaC::mul::eval ()
#3  0x06499fa7 in GiNaC::ex::construct_from_basic ()
#4  0x065875f7 in GiNaC::operator* ()
#5  0x0678bbe9 in GiNaC::ptr<GiNaC::basic>::operator= () at sage/symbolic/expression.cpp:10325
#6  0x0678bbe9 in operator= [inlined] () at ptr.h:75
#7  0x0678bbe9 in __pyx_f_4sage_8symbolic_10expression_10Expression__mul_ (__pyx_v_left=0x103c710, __pyx_v_right=0x103a418, __pyx_skip_dispatch=0) at sage/symbolic/expression.cpp:10325
#8  0x01a6cc6f in __pyx_pf_4sage_9structure_7element_11RingElement___mul__ (__pyx_v_self=0x103c710, __pyx_v_right=0x103a418) at sage/structure/element.c:10134
#9  0x00007bc2 in binary_op1 ()
#10 0x0000c109 in PyNumber_Multiply ()
#11 0x000b7833 in PyEval_EvalFrameEx ()
#12 0x000bb71d in PyEval_EvalCodeEx ()
#13 0x000ba07e in PyEval_EvalFrameEx ()
#14 0x000bb71d in PyEval_EvalCodeEx ()
#15 0x000b99c6 in PyEval_EvalFrameEx ()
#16 0x000bb71d in PyEval_EvalCodeEx ()
#17 0x000b99c6 in PyEval_EvalFrameEx ()
#18 0x000ba5c9 in PyEval_EvalFrameEx ()
#19 0x000bb71d in PyEval_EvalCodeEx ()
#20 0x000b99c6 in PyEval_EvalFrameEx ()
#21 0x000bb71d in PyEval_EvalCodeEx ()
#22 0x000b99c6 in PyEval_EvalFrameEx ()
#23 0x000bb71d in PyEval_EvalCodeEx ()
#24 0x000b99c6 in PyEval_EvalFrameEx ()
#25 0x000bb71d in PyEval_EvalCodeEx ()
#26 0x000bb837 in PyEval_EvalCode ()
#27 0x000e0108 in PyRun_FileExFlags ()
#28 0x000e0ff3 in PyRun_SimpleFileExFlags ()
#29 0x000efb7e in Py_Main ()
#30 0x00001c7b in _start ()
#31 0x00001ba9 in start ()
```

By the way, I get tons of errors when running sage -gdb "could not find object file "....o" - no debug information available for "....c" though I assume that is normal.

The same type of error happens if I just do 

```
sage: exp(blah)^I*exp(z)
```

where blah can be anything.  So perhaps something is parsing weird with the I* business.

Also notice that currently I seem to have both pynac-0.1.10 and pynac-0.1.10.a0 installed, but fixing this and reinstalling pynac 0.1.10 didn't hep.  Interestingly, it has to be two different things in the exps, as exp(x)^I*exp(x) works fine, but even exp(2)^I*exp(3) doesn't.


---

Comment by burcin created at 2009-12-07 17:00:51

I uploaded a new package at the same location:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.10.spkg

Can you try again with this version?


---

Comment by kcrisman created at 2009-12-07 20:27:52

I can confirm this still happens on both sage.math and my Macintel machine.   On sage.math this was from a fresh binary; note it did have the pynac-0.1.10a0 in it, which I am wondering whether this might have something to do with it - maybe two variants of something or other?


---

Comment by burcin created at 2009-12-09 00:02:17

apply only this patch


---

Attachment

I put another version at the same place:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.10.spkg

Hopefully this is the last time. :)

Can you try again?


---

Comment by mhansen created at 2009-12-09 03:32:33

This spkg fixes things on sage.math.


---

Comment by mhansen created at 2009-12-10 03:19:49

Karl-Dieter, does this fix things on your MacIntel box?


---

Comment by kcrisman created at 2009-12-10 05:03:46

I can't check this until sometime tomorrow, sorry, I was off the grid for about 36 hours.  If you can wait with 4.3 until early tomorrow afternoon (Pacific) I should be able to check this out.  I think this should definitely get in asap, assuming it's fixed - I agree with the 'critical' priority.


---

Comment by kcrisman created at 2009-12-10 14:15:12

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2009-12-10 14:15:12

It works!  

My build is a not fresh, so the patch wouldn't apply, but I checked all the doctests by hand and they were correct (as well as my own tries), so assuming it applies on a clean build, positive review!


---

Comment by kcrisman created at 2009-12-10 14:15:22

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-10 14:22:03

Resolution: fixed
