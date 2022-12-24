# Issue 7264: segfault while substituting powers of exp

archive/issues_007264.json:
```json
{
    "body": "Assignee: burcin\n\n\n```\nOn Wed, 21 Oct 2009 19:49:58 -0700 (PDT)\nIchnich <warmbau@web.de> wrote:\n\n> Hi,\n> \n> something does not work anymore in my notebook (with version 4.1.2\n> ubuntu 64bit):\n>\n> var('a,b,c,I')\n> model(I)=a*I+b\n> model_exp = exp(I)**a*(b)\n> sol1_l={b: 5.0, a: 1.1}\n> model_sol1_l(I)=model_exp.subs(sol1_l)\n> \n> The notebook hangs-up. It's critical on the parameter a, if you change\n> it to 1.0 it's o.k.\n```\n\n\nI can reproduce this:\n\n\n```\nsage: var('a,b,c,I')\n(a, b, c, I)\nsage: model_exp = exp(I)**a*(b)\nsage: sol1_l={b: 5.0, a: 1.1}\nsage: model_exp.subs(sol1_l)\n/home/burcin/sage/sage-4.1.2/local/bin/sage-sage: line 203: 23916\nSegmentation fault      sage-ipython \"$@\" -i\n```\n\n\nThe cause might be #6948.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7264\n\n",
    "created_at": "2009-10-22T08:25:50Z",
    "labels": [
        "symbolics",
        "critical",
        "bug"
    ],
    "title": "segfault while substituting powers of exp",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7264",
    "user": "burcin"
}
```
Assignee: burcin


```
On Wed, 21 Oct 2009 19:49:58 -0700 (PDT)
Ichnich <warmbau@web.de> wrote:

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
Segmentation fault      sage-ipython "$@" -i
```


The cause might be #6948.

Issue created by migration from https://trac.sagemath.org/ticket/7264





---

archive/issue_comments_060342.json:
```json
{
    "body": "In 4.2:\n\n\n```\nsage: var('a,b,c,I')\n(a, b, c, I)\nsage: model_exp=exp(I)**a*(b)\nsage: sol1_l={b: 5.0, a: 1.1}\nsage: model_exp.subs(sol1_l)\n/home/grout/sage/local/bin/sage-sage: line 203: 23853 Segmentation fault      sage-ipython \"$@\" -i\n```\n\n\nSince 4.2 has #6948 merged in, I guess that was not the cause.",
    "created_at": "2009-11-04T17:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7264#issuecomment-60342",
    "user": "jason"
}
```

In 4.2:


```
sage: var('a,b,c,I')
(a, b, c, I)
sage: model_exp=exp(I)**a*(b)
sage: sol1_l={b: 5.0, a: 1.1}
sage: model_exp.subs(sol1_l)
/home/grout/sage/local/bin/sage-sage: line 203: 23853 Segmentation fault      sage-ipython "$@" -i
```


Since 4.2 has #6948 merged in, I guess that was not the cause.



---

archive/issue_comments_060343.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-22T17:58:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7264#issuecomment-60343",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060344.json:
```json
{
    "body": "This was indeed caused by the changes to pynac from #6948. I forgot to adjust\nautomatic simplification of pynac `mul` objects to the new exp power rule. \n\nThis is fixed in the new pynac package here:\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.10.spkg\n\nattachment:trac_7264-exp_power_segfault.patch adds doctests for the fix.\n\nNote that the new pynac version also contains fixes for #7508 and #7406. Tests should be run with the patches from those tickets also applied in this order:\n\n* #7508\n* #7264 (this ticket)\n* #7406\n\nThis ticket now depends on #7490 and #7508.",
    "created_at": "2009-11-22T17:58:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7264#issuecomment-60344",
    "user": "burcin"
}
```

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

archive/issue_comments_060345.json:
```json
{
    "body": "Changing keywords from \"\" to \"pynac\".",
    "created_at": "2009-11-22T17:58:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7264#issuecomment-60345",
    "user": "burcin"
}
```

Changing keywords from "" to "pynac".



---

archive/issue_comments_060346.json:
```json
{
    "body": "Attachment [trac_7264-exp_power_segfault.patch](tarball://root/attachments/some-uuid/ticket7264/trac_7264-exp_power_segfault.patch) by burcin created at 2009-11-22 17:58:49\n\nadd doctests",
    "created_at": "2009-11-22T17:58:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7264#issuecomment-60346",
    "user": "burcin"
}
```

Attachment [trac_7264-exp_power_segfault.patch](tarball://root/attachments/some-uuid/ticket7264/trac_7264-exp_power_segfault.patch) by burcin created at 2009-11-22 17:58:49

add doctests



---

archive/issue_comments_060347.json:
```json
{
    "body": "I would like to review this, but installing Pynac 0.1.10 caused an error (not in sage -i, but with sage -br after that):\n\n```\nerror: command 'gcc' failed with exit status 1\nsage: There was an error installing modified sage library code.\n```\n\nWhat is the base version of Sage for this ticket (e.g., 4.3)?",
    "created_at": "2009-12-04T17:12:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7264#issuecomment-60347",
    "user": "kcrisman"
}
```

I would like to review this, but installing Pynac 0.1.10 caused an error (not in sage -i, but with sage -br after that):

```
error: command 'gcc' failed with exit status 1
sage: There was an error installing modified sage library code.
```

What is the base version of Sage for this ticket (e.g., 4.3)?



---

archive/issue_comments_060348.json:
```json
{
    "body": "Hi Karl-Dieter,\n\nDid you have #7490 applied to your tree?\n\nThat patch was merged in 4.3.alpha1, so you can also try updating to the latest alpha.\n\nThank you for your time.",
    "created_at": "2009-12-04T21:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7264#issuecomment-60348",
    "user": "burcin"
}
```

Hi Karl-Dieter,

Did you have #7490 applied to your tree?

That patch was merged in 4.3.alpha1, so you can also try updating to the latest alpha.

Thank you for your time.



---

archive/issue_comments_060349.json:
```json
{
    "body": "This needs work, because somehow the following test with the new spkg causes a segfault (Mac OSX 10.5, Intel):\n\n```\nsage: exp(x)^I*exp(z)^(2.5)\n\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n```\n\nHowever, everything else behaves properly, so if this can be fixed, all three tickets will have positive review.  These are important fixes, so thanks for the work!",
    "created_at": "2009-12-05T13:52:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7264#issuecomment-60349",
    "user": "kcrisman"
}
```

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

archive/issue_comments_060350.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-05T13:52:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7264#issuecomment-60350",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060351.json:
```json
{
    "body": "Can you post a backtrace? I can't reproduce the problem and I have no clue what might be going wrong.\n\nTo get a backtrace, you need to run Sage under gdb as the error message says. When it crashes, type `bt`, then copy and paste the output here.\n\nStarting from a clean install, and making sure there is nothing else to effect this test could also help.",
    "created_at": "2009-12-05T22:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7264#issuecomment-60351",
    "user": "burcin"
}
```

Can you post a backtrace? I can't reproduce the problem and I have no clue what might be going wrong.

To get a backtrace, you need to run Sage under gdb as the error message says. When it crashes, type `bt`, then copy and paste the output here.

Starting from a clean install, and making sure there is nothing else to effect this test could also help.



---

archive/issue_comments_060352.json:
```json
{
    "body": "This was a fresh build of 4.3.alpha1.  Only issue was that I had to hg -add several files to be able to add patches, and revert the two png files Minh has mentioned on sage-devel.  But I don't see how that would have affected things.\n\n```\nsage: exp(x)^I*exp(z)^(2.5)\n\nProgram received signal EXC_BAD_ACCESS, Could not access memory.\nReason: KERN_INVALID_ADDRESS at address: 0xc23d006b\n0x0658315e in GiNaC::Number_T::operator/ ()\n(gdb) bt\n#0  0x0658315e in GiNaC::Number_T::operator/ ()\n#1  0x065837bb in GiNaC::numeric::div ()\n#2  0x06549c14 in GiNaC::mul::eval ()\n#3  0x06499fa7 in GiNaC::ex::construct_from_basic ()\n#4  0x065875f7 in GiNaC::operator* ()\n#5  0x0678bbe9 in GiNaC::ptr<GiNaC::basic>::operator= () at sage/symbolic/expression.cpp:10325\n#6  0x0678bbe9 in operator= [inlined] () at ptr.h:75\n#7  0x0678bbe9 in __pyx_f_4sage_8symbolic_10expression_10Expression__mul_ (__pyx_v_left=0x103c710, __pyx_v_right=0x103a418, __pyx_skip_dispatch=0) at sage/symbolic/expression.cpp:10325\n#8  0x01a6cc6f in __pyx_pf_4sage_9structure_7element_11RingElement___mul__ (__pyx_v_self=0x103c710, __pyx_v_right=0x103a418) at sage/structure/element.c:10134\n#9  0x00007bc2 in binary_op1 ()\n#10 0x0000c109 in PyNumber_Multiply ()\n#11 0x000b7833 in PyEval_EvalFrameEx ()\n#12 0x000bb71d in PyEval_EvalCodeEx ()\n#13 0x000ba07e in PyEval_EvalFrameEx ()\n#14 0x000bb71d in PyEval_EvalCodeEx ()\n#15 0x000b99c6 in PyEval_EvalFrameEx ()\n#16 0x000bb71d in PyEval_EvalCodeEx ()\n#17 0x000b99c6 in PyEval_EvalFrameEx ()\n#18 0x000ba5c9 in PyEval_EvalFrameEx ()\n#19 0x000bb71d in PyEval_EvalCodeEx ()\n#20 0x000b99c6 in PyEval_EvalFrameEx ()\n#21 0x000bb71d in PyEval_EvalCodeEx ()\n#22 0x000b99c6 in PyEval_EvalFrameEx ()\n#23 0x000bb71d in PyEval_EvalCodeEx ()\n#24 0x000b99c6 in PyEval_EvalFrameEx ()\n#25 0x000bb71d in PyEval_EvalCodeEx ()\n#26 0x000bb837 in PyEval_EvalCode ()\n#27 0x000e0108 in PyRun_FileExFlags ()\n#28 0x000e0ff3 in PyRun_SimpleFileExFlags ()\n#29 0x000efb7e in Py_Main ()\n#30 0x00001c7b in _start ()\n#31 0x00001ba9 in start ()\n```\n\nBy the way, I get tons of errors when running sage -gdb \"could not find object file \"....o\" - no debug information available for \"....c\" though I assume that is normal.\n\nThe same type of error happens if I just do \n\n```\nsage: exp(blah)^I*exp(z)\n```\n\nwhere blah can be anything.  So perhaps something is parsing weird with the I* business.\n\nAlso notice that currently I seem to have both pynac-0.1.10 and pynac-0.1.10.a0 installed, but fixing this and reinstalling pynac 0.1.10 didn't hep.  Interestingly, it has to be two different things in the exps, as exp(x)^I*exp(x) works fine, but even exp(2)^I*exp(3) doesn't.",
    "created_at": "2009-12-06T02:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7264#issuecomment-60352",
    "user": "kcrisman"
}
```

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

archive/issue_comments_060353.json:
```json
{
    "body": "I uploaded a new package at the same location:\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.10.spkg\n\nCan you try again with this version?",
    "created_at": "2009-12-07T17:00:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7264#issuecomment-60353",
    "user": "burcin"
}
```

I uploaded a new package at the same location:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.10.spkg

Can you try again with this version?



---

archive/issue_comments_060354.json:
```json
{
    "body": "I can confirm this still happens on both sage.math and my Macintel machine.   On sage.math this was from a fresh binary; note it did have the pynac-0.1.10a0 in it, which I am wondering whether this might have something to do with it - maybe two variants of something or other?",
    "created_at": "2009-12-07T20:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7264#issuecomment-60354",
    "user": "kcrisman"
}
```

I can confirm this still happens on both sage.math and my Macintel machine.   On sage.math this was from a fresh binary; note it did have the pynac-0.1.10a0 in it, which I am wondering whether this might have something to do with it - maybe two variants of something or other?



---

archive/issue_comments_060355.json:
```json
{
    "body": "apply only this patch",
    "created_at": "2009-12-09T00:02:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7264#issuecomment-60355",
    "user": "burcin"
}
```

apply only this patch



---

archive/issue_comments_060356.json:
```json
{
    "body": "Attachment [trac_7264-exp_power_segfault.take2.patch](tarball://root/attachments/some-uuid/ticket7264/trac_7264-exp_power_segfault.take2.patch) by burcin created at 2009-12-09 00:03:50\n\nI put another version at the same place:\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.10.spkg\n\nHopefully this is the last time. :)\n\nCan you try again?",
    "created_at": "2009-12-09T00:03:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7264#issuecomment-60356",
    "user": "burcin"
}
```

Attachment [trac_7264-exp_power_segfault.take2.patch](tarball://root/attachments/some-uuid/ticket7264/trac_7264-exp_power_segfault.take2.patch) by burcin created at 2009-12-09 00:03:50

I put another version at the same place:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.10.spkg

Hopefully this is the last time. :)

Can you try again?



---

archive/issue_comments_060357.json:
```json
{
    "body": "This spkg fixes things on sage.math.",
    "created_at": "2009-12-09T03:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7264#issuecomment-60357",
    "user": "mhansen"
}
```

This spkg fixes things on sage.math.



---

archive/issue_comments_060358.json:
```json
{
    "body": "Karl-Dieter, does this fix things on your MacIntel box?",
    "created_at": "2009-12-10T03:19:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7264#issuecomment-60358",
    "user": "mhansen"
}
```

Karl-Dieter, does this fix things on your MacIntel box?



---

archive/issue_comments_060359.json:
```json
{
    "body": "I can't check this until sometime tomorrow, sorry, I was off the grid for about 36 hours.  If you can wait with 4.3 until early tomorrow afternoon (Pacific) I should be able to check this out.  I think this should definitely get in asap, assuming it's fixed - I agree with the 'critical' priority.",
    "created_at": "2009-12-10T05:03:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7264#issuecomment-60359",
    "user": "kcrisman"
}
```

I can't check this until sometime tomorrow, sorry, I was off the grid for about 36 hours.  If you can wait with 4.3 until early tomorrow afternoon (Pacific) I should be able to check this out.  I think this should definitely get in asap, assuming it's fixed - I agree with the 'critical' priority.



---

archive/issue_comments_060360.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-10T14:15:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7264#issuecomment-60360",
    "user": "kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060361.json:
```json
{
    "body": "It works!  \n\nMy build is a not fresh, so the patch wouldn't apply, but I checked all the doctests by hand and they were correct (as well as my own tries), so assuming it applies on a clean build, positive review!",
    "created_at": "2009-12-10T14:15:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7264#issuecomment-60361",
    "user": "kcrisman"
}
```

It works!  

My build is a not fresh, so the patch wouldn't apply, but I checked all the doctests by hand and they were correct (as well as my own tries), so assuming it applies on a clean build, positive review!



---

archive/issue_comments_060362.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-10T14:15:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7264#issuecomment-60362",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060363.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-10T14:22:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7264#issuecomment-60363",
    "user": "mhansen"
}
```

Resolution: fixed
