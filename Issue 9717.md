# Issue 9717: fix variable substitution in PolyBoRi

Issue created by migration from https://trac.sagemath.org/ticket/9717

Original creator: malb

Original creation time: 2010-08-10 12:43:40

Assignee: malb

CC:  polybori alexanderdreyer leif mpatel

For some inputs our[This is the Trac macro *PolyBoRi* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#PolyBoRi-macro) wrapper throws an error while upstream computes the example just fine. The reason we fail is that some rings don't match and thus coercion goes wrong. The problem was reported by Joan Daemen who also provided an example via private communication.


---

Comment by malb created at 2010-08-10 12:45:33

Alexander Dreyer provided a fix for the issue. I've packaged this fix into an SPKG

 http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.4.p2.spkg

I've also packaged his patch for Sage into a proper mercurial patch which I'll attach in a sec.


---

Comment by malb created at 2010-08-10 12:45:33

Changing status from new to needs_work.


---

Comment by malb created at 2010-08-10 12:49:29

The attached patch + SPKG fix the original problem, however I'm getting segfaults now:


```
Program received signal SIGSEGV, Segmentation fault.
linalg_step_modified (polys=<value optimized out>, terms=<value optimized out>, 
    leads_from_strat=<value optimized out>, log=<value optimized out>, 
    optDrawMatrices=<value optimized out>, matrixPrefix=<value optimized out>)
    at groebner/src/nf.cc:2270
2270    groebner/src/nf.cc: No such file or directory.
        in groebner/src/nf.cc
Current language:  auto
The current source language is "auto; currently c++".
(gdb) bt
#0  linalg_step_modified (polys=<value optimized out>, terms=<value optimized out>, 
    leads_from_strat=<value optimized out>, log=<value optimized out>, 
    optDrawMatrices=<value optimized out>, matrixPrefix=<value optimized out>)
    at groebner/src/nf.cc:2270
#1  0x00007fffcf4f6c56 in polybori::groebner::GroebnerStrategy::faugereStepDense (
    this=<value optimized out>, orig_system=<value optimized out>) at groebner/src/nf.cc:2386
#2  0x00007fffcf3e2a0d in __pyx_pf_4sage_5rings_10polynomial_5pbori_16GroebnerStrategy_faugere_step_dense (__pyx_v_self=0x5997520, __pyx_v_v=0x12bf3500) at sage/rings/polynomial/pbori.cpp:31846
#3  0x00007ffff7b11316 in call_function (f=0x418a900, throwflag=<value optimized out>)
    at Python/ceval.c:3694

```



---

Comment by malb created at 2010-08-10 13:30:00

Ignore the SIGSEGV above, it is unrelated to this ticket but is caused by #9562. 

Alexander, can you review my SPKG + patch, i.e. that it does what you intended? I give your changes a positive review so all that's needed is some check whether I produced the SPKG correctly etc.


---

Comment by malb created at 2010-08-10 13:30:00

Changing status from needs_work to needs_review.


---

Comment by malb created at 2010-08-10 15:08:28

Use this SPKG instead (it is based on the latest PolyBoRi SPKG which the previous SPKG wasn't) 

 http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.4.p3.spkg


---

Comment by AlexanderDreyer created at 2010-08-10 21:16:00

There was some unrelated issue with the previous spkg (libm4ri was not found, because Sage's lib directory was not given to PolyBoRi)
I updated the spkg accordingly:
http://sage.math.washington.edu/home/dreyer/pb/polybori-0.6.4.p4.spkg


---

Comment by leif created at 2010-08-11 12:50:25

Changing status from needs_review to needs_work.


---

Comment by leif created at 2010-08-11 12:50:25

`SPKG.txt` has to be updated for p4.

Alexander's patch looks reasonable, though libm4ri (and the GD library) were previously found (in the second attempt)... (The only issue I'm aware of is with updating from 4.5.2 on MacOS X 10.6, which Mitesh Patel couldn't reproduce either; see #9721.)

(The change to p4 is of course unrelated to the original intent of this ticket; perhaps adapt its title, too.)


---

Comment by malb created at 2010-08-11 13:12:32

Replying to [comment:8 leif]:

> `SPKG.txt` has to be updated for p4.

I have a new SPKG which does exactly that. I'll upload it later.

> Alexander's patch looks reasonable, though libm4ri (and the GD library) were previously found (in the second attempt)... (The only issue I'm aware of is with updating from 4.5.2 on MacOS X 10.6, which Mitesh Patel couldn't reproduce either; see #9721.) (The change to p4 is of course unrelated to the original intent of this ticket; perhaps adapt its title, too.)


---

Comment by malb created at 2010-08-11 13:30:19

The new SPKG is here

 http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.4.p4.spkg

I just added an entry to SPKG.txt


---

Comment by malb created at 2010-08-11 18:03:34

PolyBoRi makes assumptions about M4RI which are not met with the newest upstream release (#9475). Thus, we should fix this here asap since the new M4RI is about to go in.


---

Comment by malb created at 2010-08-12 18:48:18

I've replaced the SPKG here 

   http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.4.p4.spkg

and the new SPKG fixes the SIGSEGV and all doctests pass.

These fixes are:

 http://bitbucket.org/brickenstein/polybori/changeset/6ef7402d935b

 http://bitbucket.org/brickenstein/polybori/changeset/b692c8181e94


---

Comment by malb created at 2010-08-12 18:48:18

Changing status from needs_work to needs_review.


---

Comment by leif created at 2010-08-13 02:30:01

Changing status from needs_review to needs_work.


---

Comment by leif created at 2010-08-13 02:30:01

`Work issues` field ( = _"Update `SPKG.txt`"_) still (or again) valid... ;-)

(Perhaps also add this ticket number, and mention the PolyBoRi upstream fixes there.)


---

Comment by malb created at 2010-08-13 08:50:15

Updated accordingly.


---

Comment by malb created at 2010-08-13 08:50:15

Changing status from needs_work to needs_review.


---

Comment by AlexanderDreyer created at 2010-08-13 09:02:04

Meanwhile, I took a look at the surrounding code also. (Just to ensure, that the patches also do the right thing in other contexts.) It's a good patch and it may fix even more issues. So I give a positive review from the mathematical point of view. (If I'm allowed to do so.) For the technical viewpoint: I'm waiting now for `sage -testall` to finish.


---

Comment by leif created at 2010-08-13 09:55:32

Passed `ptestlong` with Sage 4.5.3.alpha0 and `libm4ri-20100701.p1` from #9475 on Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4).

So I can give "positive review" from the technical side. ;-)


---

Comment by leif created at 2010-08-13 10:05:36

The updated `SPKG.txt` is ok, too. (And the upstream fixes also look reasonable btw.)


---

Comment by leif created at 2010-08-13 10:14:43

Replying to [comment:18 leif]:
> The updated `SPKG.txt` is ok, too.

... except for the date(s), but I'll assume the intention was to avoid naming Friday 13th and accept it. ;-)


---

Comment by malb created at 2010-08-13 11:59:20

So we have a positive review then?


---

Comment by leif created at 2010-08-13 12:21:40

Replying to [comment:20 malb]:
> So we have a positive review then?

Once Alexander's `testall` has finished, I think yes. :)

I'll perhaps test later on a 64-bit platform, although I don't expect any issues.


---

Comment by leif created at 2010-08-13 12:55:53

Replying to [comment:21 leif]:
> I'll perhaps test later on a 64-bit platform, although I don't expect any issues.

Passed all long tests in `sage/matrix`; currently running `make testlong`, but this will take some time since the system is already fully loaded... (Ubuntu 9.04 x86_64, Core2, gcc 4.3.3)


---

Comment by AlexanderDreyer created at 2010-08-13 14:13:02

> Once Alexander's `testall` has finished, I think yes. :)
They have successfully finished (SuSE 11.1 64 Bits). So we have the positive review now


---

Comment by AlexanderDreyer created at 2010-08-13 14:13:02

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-08-13 14:25:56

## Note to the release managers

I think this should (only) be merged together with #9475, but I'm not _that_ sure.


---

Comment by leif created at 2010-08-13 16:39:48

As expected, also passed `testlong` with Sage 4.5.3.alpha0 and #9475 on Ubuntu 9.04 x86_64 (Core2, gcc 4.3.3, native code, O2).


---

Comment by leif created at 2010-08-13 17:12:15

Ooops, I just noticed the [attached patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9717/polybori-0.6.4.p2.patch) is to the _Sage library_ (I assumed it is an _spkg_ patch). So I did *not* apply that patch in any of the tests I made, which despite that all passed...

Martin, is that patch now obsolete or do we just not test an example which would fail without it? Or is it platform-specific?

(Btw, the patch's commit message lacks a ticket number; also, a back-reference/comment in the code wouldn't be bad.)

Perhaps you could add Joan Daemen's example to the ticket.


---

Comment by malb created at 2010-08-14 12:10:18

Replying to [comment:26 leif]:

> Ooops, I just noticed the [attached patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9717/polybori-0.6.4.p2.patch) is to the _Sage library_ (I assumed it is an _spkg_ patch). So I did *not* apply that patch in any of the tests I made, which despite that all passed... Martin, is that patch now obsolete or do we just not test an example which would fail without it?

The patch is necessary, Sage will SIGSEGV in some cases otherwise. I'll try to update the patch with an example.

> Or is it platform-specific? (Btw, the patch's commit message lacks a ticket number; also, a back-reference/comment in the code wouldn't be bad.)

I'll add the ticket number.

> Perhaps you could add Joan Daemen's example to the ticket.

The problem is a bit bigger and I have no permission to publish it, sorry.


---

Comment by malb created at 2010-08-14 12:19:56

I've updated the patch with an example and this ticket's number.


---

Comment by leif created at 2010-08-14 12:47:47

Replying to [comment:28 malb]:
> I've updated the patch with an example and this ticket's number.

Ok, I'll rerun some of the tests later. Currently all machines busy with new PARI testing... ;-)

(I don't see the ticket number in the patched code though.)


---

Comment by malb created at 2010-08-14 12:51:01


```
#9717 fixing parent ring in substitute_variable() (fix due to Alexander Dreyer)
```

That's the commit message, is that alright?


---

Comment by leif created at 2010-08-14 13:02:51

And an attachment comment would be nice... ("Sage library patch - ...")

I HATE TRAC! [concurrent "editing" grrrrr...]

----

I meant putting the ticket number also into a comment *in the code*; you don't see the commit messages when looking just at source files. E.g.

```
        ... # fixes #9717
```

or in the `TESTS::` section:

```
    Substitution is (now) also allowed with different rings (cf. #9717)::
```

Something like that.


---

Comment by malb created at 2010-08-14 13:17:06

I'm not too convinced by that. This was a serious bug which just wasn't reported to far. I don't want to clutter the code with track ticket numbers. When reading the code it is relatively simple to see (I'd say) that the new code is correct, thus I'd say it doesn't need a ticket to explain why it is there. Also, the new example isn't just a test, it shows a real use case.


---

Comment by malb created at 2010-08-14 13:17:44

Sage library patch fixing an issue with substitute_variable()


---

Attachment


---

Comment by mpatel created at 2010-08-15 08:03:29

Resolution: fixed


---

Comment by mpatel created at 2010-08-17 07:10:15

How does one run PolyBoRi's test suite?  I'm curious about whether we can add an `spkg-check` file (at a new ticket).


---

Comment by AlexanderDreyer created at 2010-08-17 08:27:23

The testsuite, which is included in PolyBoRi is not up to date, we use another suite for developing internally. On the one hand, it is lange, on the other, some examples are not freely available. We'll try to deliver a suitable subset of the examples in the future.
