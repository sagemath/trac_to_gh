# Issue 2329: [with patch, needs review] add interface to Pari's rnfisnorm

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-02-27 09:03:44

Assignee: was

CC:  ncalexan mstreng jdemeyer

This patch adds support to solve norm equations via Pari. 

Quick summary: given an element `x` of any number field (even `QQ`), `x.is_norm(L)` will return `False` if `x` is not a norm from `L`, and if `x` is a norm from `L`, will return an element of `L` whose norm is `x`. 

According to the Pari documentation, these functions depend on GRH when `L/K` is not known to be Galois, and work independent of any such hypothesis otherwise (at least, that's what I got from reading the Pari manual). 

The data used by Pari to compute whether or not an element is a norm can be computed once for each extension `L/K`. The function `pari_rnfnorm_data` computes exactly this, and its result can be passed to `is_norm` to avoid recomputing it each time in the case that `K != QQ`. If `K` is `QQ`, there is no need to save any such data -- the only data needed is that of `K.pari_bnf()`, which is used instead, and is already cached by `K`.


---

Attachment


---

Comment by ncalexan created at 2008-02-27 19:41:51

I have some questions.

There seems to be two things in this patch: changes to pari/gen, and access to stuff to do with norms.  Is the latter independent of the former?  I'd be a lot happier with the latter if that's true, because I'm not expert in the Pari interface.

Also, what relation does this have to "elements_of_norm"?  There needs to be some unification, I think.  Also, having is_norm() not always return a boolean is not good, IMO.  I say is_norm -> Boolean and element_of_norm raises an exception if is_norm is not True.

I will gladly referee and have cc'ed myself.


---

Comment by craigcitro created at 2008-02-27 21:49:41

Changing assignee from was to craigcitro.


---

Comment by craigcitro created at 2008-02-27 21:49:41

Changing status from new to assigned.


---

Comment by ncalexan created at 2008-03-31 23:45:38

Craig, what's the status on this patch?  I need it as we speak :)  Are you interested in completing this or should I implement the changes I think are necessary and kick it back to you for refereeing?


---

Comment by craigcitro created at 2008-04-01 00:19:36

Nick, I'd be more than happy to have you finish this guy off. I think all the code is there, it just needs to be cleaned up and unified here and there. I just haven't had time to get back to it since you posted the referee report -- but if you want to clean this up, I'll review it for you lickety-split.


---

Comment by craigcitro created at 2008-04-05 23:41:38

Added a second patch that addresses all of the above issues.


---

Attachment


---

Attachment

The last patch separates out very useful fixes to the pari/gen.pyx that should be applied now.

The remainder of the functionality requires some more substantial changes and is a work in progress.


---

Comment by craigcitro created at 2008-06-20 04:30:06

Changing keywords from "" to "editor_craigcitro".


---

Comment by mabshoff created at 2008-09-27 22:34:29

This has been sitting around forever. Any movement here?

Cheers,

Michael


---

Comment by davidloeffler created at 2009-07-20 19:55:45

Changing component from number theory to number fields.


---

Comment by mstreng created at 2010-07-10 13:10:29

Same question as mabshoff 22 months ago...


---

Comment by mstreng created at 2010-08-17 14:04:06

Changing priority from minor to major.


---

Comment by mstreng created at 2010-08-17 14:04:06

As nobody replied here any more, I attacked the ticket myself by changing Craig's patch.

I've addressed Nick's concerns and replaced the documentation to reflect better what is in the Pari documentation (which weakens some claims considerably unfortunately).

x.is_norm() now decides whether an element x is a norm (proven output), while x.rnfisnorm() gives exactly the output that Pari's rnfisnorm would give.

The output of is_norm is True or False. With element=True, it also gives an element of norm x (or None if it doesn't exist). The function element_of_norm is removed, to avoid confusion with elements_of_norm.


---

Attachment

apply only this latest file


---

Comment by mstreng created at 2010-08-18 14:12:12

Ready for review, volunteer needed!

The only doctest that failed fails without the patch as well:

```
K.<a> = QuadraticField(-5)
K.selmer_group([K.ideal(2, -a+1), K.ideal(3, a+1), K.ideal(a)], 3)
[2, a + 1, a]
```

The documentation says it should be `[2, a+1, -a]`


---

Comment by mstreng created at 2010-08-18 14:12:12

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2010-09-23 09:47:13

Patch applies fine under 4.6.alpha1 but fails to compile:

```
Error converting Pyrex file to C:
------------------------------------------------------------
...
        return self.new_gen(thueinit(self.g, flag, prec))


    def rnfisnorminit(self, polrel, flag=2):
        _sig_on
        return self.new_gen(rnfisnorminit(self.g, (<gen>polrel).g, flag))
                                        ^
------------------------------------------------------------

/storage/masiao/sage-4.6.alpha1/devel/sage-hacking/sage/libs/pari/gen.pyx:7160:41: undeclared name not builtin: rnfisnorminit
```

Adding 

```
    GEN     rnfisnorminit(GEN T, GEN relpol, int galois)
```

to `sage/libs/pari/decl.pxi` fixes that issue, but this reveals another failure:

```
sage/libs/pari/gen.c: In function ‘__pyx_pf_4sage_4libs_4pari_3gen_3gen_bnfisnorm’:
sage/libs/pari/gen.c:24097: error: too many arguments to function ‘bnfisnorm’
```

This seems to be because the "prec" argument to "bnfisnorm" has been removed, but taking out the extra argument, it *still* doesn't work:

```
sage -t  number_field_element.pyx
**********************************************************************
File "/storage/masiao/sage-4.6.alpha1/devel/sage-hacking/sage/rings/number_field/number_field_element.pyx", line 971:
    sage: (beta/2).is_norm(L)
Exception raised:
    Traceback (most recent call last):
      File "/storage/masiao/sage-4.6.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/storage/masiao/sage-4.6.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/storage/masiao/sage-4.6.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_28[5]>", line 1, in <module>
        (beta/Integer(2)).is_norm(L)###line 971:
    sage: (beta/2).is_norm(L)
      File "number_field_element.pyx", line 999, in sage.rings.number_field.number_field_element.NumberFieldElement.is_norm (sage/rings/number_field/number_field_element.cpp:8726)
        return self.is_norm(L, element = True, proof = proof)[0]
      File "number_field_element.pyx", line 1017, in sage.rings.number_field.number_field_element.NumberFieldElement.is_norm (sage/rings/number_field/number_field_element.cpp:9083)
        a, b = self.rnfisnorm(L, certify = proof)
      File "number_field_element.pyx", line 1108, in sage.rings.number_field.number_field_element.NumberFieldElement.rnfisnorm (sage/rings/number_field/number_field_element.cpp:9820)
        x, q = self._pari_('y').rnfisnorm(rnf_data)
      File "gen.pyx", line 9470, in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:45353)
    PariError:  (5)
**********************************************************************
```

At that point I gave up. Sorry. That's "needs work".

David


---

Comment by davidloeffler created at 2010-09-23 09:47:13

Changing status from needs_review to needs_work.


---

Comment by mstreng created at 2010-11-03 10:01:01

If anyone wants to fix this, go ahead. It worked just fine on my 4.5.something, so I guess a solution can be found by looking at the differences between the pari interfaces of 4.5 and 4.6.


---

Comment by fwclarke created at 2010-11-04 08:38:43

Replying to [comment:15 davidloeffler]:

> ..., it *still* doesn't work:

```
sage -t  number_field_element.pyx 
********************************************************************** 
File "/storage/masiao/sage-4.6.alpha1/devel/sage-hacking/sage/rings/number_field/number_field_element.pyx", line 971:
    sage: (beta/2).is_norm(L)
Exception raised:
    Traceback (most recent call last):
... 
File "gen.pyx", line 9470, in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:45353) 
PariError:  (5) 
********************************************************************** 
```

> At that point I gave up. Sorry. That's "needs work".

Looks like a Pari bug.  This is what the doctest asks Pari to do (with the equivalent of beta.is_norm(L) first):


```
trousseau-bash% sage-4.6/sage -gp
                   GP/PARI CALCULATOR Version 2.4.3 (development svn-12577:12605)
                    i386 running darwin (x86-64/GMP-4.2.1 kernel) 64-bit version
...
parisize = 8000000, primelimit = 500509
? bnf = bnfinit(y^3 + 5);
? p = x^2 + x + Mod(y, y^3 + 5);
? T = rnfisnorminit(bnf, p);
? rnfisnorm(T, Mod(y, y^3 + 5))
%4 = [Mod(x, x^2 + x + Mod(y, y^3 + 5)), 1]
? rnfisnorm(T, Mod(y/2, y^3 + 5))
  ***   at top-level: rnfisnorm(T,Mod(y/2,
  ***                 ^--------------------
  *** rnfisnorm: zero argument in factorint.
  ***   Break loop: type 'break' to go back to GP
break> break
```

But previously, it worked alright:


```
trousseau-bash% sage-4.5.3/sage -gp
                            GP/PARI CALCULATOR Version 2.3.5 (released)
                    i386 running darwin (x86-64/GMP-4.2.1 kernel) 64-bit version
...
parisize = 8000000, primelimit = 500000
? bnf = bnfinit(y^3 + 5);
? p = x^2 + x + Mod(y, y^3 + 5);
? T = rnfisnorminit(bnf, p);
? rnfisnorm(T, Mod(y, y^3 + 5))
%4 = [Mod(-x, x^2 + x + Mod(y, y^3 + 5)), 1]
? rnfisnorm(T, Mod(y/2, y^3 + 5))
%5 = [Mod(Mod(-1/2, y^3 + 5)*x, x^2 + x + Mod(y, y^3 + 5)), 2]
? 
```

Note also that the two versions give a different result at %4.


---

Comment by mstreng created at 2010-12-02 12:56:54

Hi Francis,
Did you report this bug to pari?
Marco


---

Comment by fwclarke created at 2010-12-02 13:42:52

Replying to [comment:18 mstreng]:

> Did you report this bug to pari? Marco

No, I didn't.  But I have done now.


---

Comment by mstreng created at 2010-12-02 15:48:04

The bug with non-integral elements in rnfisnorm was reported to pari by fwclarke, and I wrote a simple workaround for the time it takes a pari-fix to reach sage.

Turns out there is another problem:

```
sage: K.<a> = NumberField(x^2 + x + 1) 
sage: Q.<X> = K[] 
sage: L.<b> = NumberField(X^3 + a) 
sage: K.pari_rnfnorm_data(L)
PariError: incorrect type (11)
```


Again caused by something that works fine in pari 2.3.4 and is broken in pari 2.4.3 (alpha)

```
gp > bnf = bnfinit(y^2+y+1);
gp > polrel = Mod(1, y^2 + y + 1)*x^3 + Mod(y, y^2 + y + 1);
gp > rnfisnorminit(bnf, polrel)
  ***   at top-level: rnfisnorminit(bnf,po
  ***                 ^--------------------
  *** rnfisnorminit: incorrect type in RgX_RgXQ_eval.
  ***   Break loop: type 'break' to go back to GP
```


Ideas anyone?


---

Comment by mstreng created at 2010-12-02 22:24:11

I've added a new file that seems to work after the pari upgrade, including workarounds for 2 new pari bugs. I'll do some additional testing before I make it "needs review" again.

The bugs have been reported to pari [http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1143](http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1143) and [http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1144](http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1144)


---

Attachment

apply only this latest file (works on sage 4.6.1.alpha2)


---

Comment by mstreng created at 2010-12-03 15:31:03

Changing status from needs_work to needs_review.


---

Comment by mstreng created at 2010-12-03 15:31:03

All tests pass again.


---

Comment by mstreng created at 2010-12-06 10:59:01

For the Buildbot's sake:

Apply trac_2329_rnfisnorm3.patch


---

Comment by jdemeyer created at 2010-12-06 13:13:41

Can you justify why you use `<gen>` instead of the `t0GEN()` mechanism in `gen.pyx`?  Even if `<gen>` happens to work, using `t0GEN()` is safer because it will prevent the `GEN` from being garbage collected.


---

Comment by mstreng created at 2010-12-06 14:16:56

Replying to [comment:26 jdemeyer]

No I can't, I didn't write that part.


---

Comment by fwclarke created at 2010-12-07 08:38:17

There remain several problems for relative extensions.  In particular, the function `sage.rings.number_field.number_field_rel.NumberField_relative.is_galois_relative` cannot be relied on at present (4.6.1.alpha3):


```
sage: K.<w> = NumberField(x^2 + x + 1)
sage: L.<a> = K.extension(x^3 - 2)
sage: L.is_galois_relative()
False
```

But


```
sage: L.is_galois_absolute()
True
```

and indeed


```
sage: len([g for g in End(L) if g(w) == w]) == L.relative_degree()
True
```

I will post a patch for this in the next couple of days, and suggest other changes to improve the behaviour of `is_norm` with relative extensions.


---

Attachment

apply only this latest file (works on sage 4.6.1.alpha2)


---

Comment by mstreng created at 2010-12-08 14:01:39

Here's a new file that addresses Jeroen's "<gen>" issue.

I don't think #9390, which Francis mentions, should stop anyone from reviewing the patch here at #2329. There must be more functionality of sage that assumes is_galois_relative to be correct, this is just one more of them, and Francis says #9390 will be fixed soon anyway. No fix of #9390 will conflict with #2329.

As for "changes to improve behaviour of is_norm". I'm not sure what you're aiming at, but if you want, you can make these changes yourself, in this ticket or a future ticket. That would be a lot more efficient.

So it is still "needs review" at the moment.


---

Comment by jdemeyer created at 2010-12-09 08:49:05

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2010-12-09 08:49:05

Planning to make a reviewer patch, focusing on the PARI interface.


---

Comment by jdemeyer created at 2010-12-09 08:50:17

Also: it might be better to wait make this ticket depend on #10430 (so we don't need the workaround).


---

Comment by jdemeyer created at 2010-12-10 12:57:40

Macro, I recommend you to take a look at my new PARI spkg at #10430, you can download it from [http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.alpha.p1.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.alpha.p1.spkg).
Could you please check whether this fixes the issues you had?  If this works, you should remove the workarounds for these bugs.


---

Comment by fwclarke created at 2010-12-10 15:11:20

Replying to [comment:29 mstreng]:

> ... I don't think #9390, which Francis mentions, should stop anyone from reviewing the patch here at #2329. There must be more functionality of sage that assumes is_galois_relative to be correct, this is just one more of them, and Francis says #9390 will be fixed soon anyway.

Actually `is_galois_relative` doesn't seem to be used anywhere else.

But anyway I have now added a (very short) patch to #9390.


---

Comment by jdemeyer created at 2010-12-11 13:56:52

New spkg at #10430: [http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.alpha.p2.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.alpha.p2.spkg)


---

Comment by fwclarke created at 2010-12-27 11:37:23

Changing status from needs_work to needs_review.


---

Comment by fwclarke created at 2010-12-27 11:37:23

The patch `trac_2329_rnfisnorm4.patch` is a modified version of `trac_2329_rnfisnorm3.patch`, designed to be applied after

 1. #10430's http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.alpha.p2.spkg;
 1. #9390's `trac_9390-3rd_replacement.patch`.

The following changes have been made:

 1. The workarounds to deal with the pari bugs have been removed.
 1. The doctests to `sage.rings.number_field.number_field_element.is_norm` involving non-Galois extensions have been changed.  The first such example was in fact a Galois extension (isomorphic to `CyclotomicField(9)`), which without the patch to #9390 was asserted to be Galois by `is_galois_relative`.
 1. A minor change to `pari_rnfnorm_data` in `number_field.py` (replacing `defining_polynomial` by `absolute_polynomial`) and more significant changes to `rnfisnorm` in `number_field_element.pyx` to allow this function to work with extensions L/K where K itself is a relative extension.  These are the changes I was referring to [comment:28 above]. Doctests have been added to illustrate this functionality.
 1. Several spaces have been removed in order to comply more closely with the style conventions given in the Developer's Guide, in particular: "Don't use spaces around the '=' sign when used to indicate a keyword argument or a default parameter value".

This all seems to work with 4.6.1.alpha3.


---

Comment by fwclarke created at 2010-12-27 11:38:20

apply only this latest file (works on sage 4.6.1.alpha3)


---

Attachment

Replying to [comment:37 fwclarke]:

> ... This all seems to work with 4.6.1.alpha3.

And with 4.6.1.rc0.


---

Comment by jdemeyer created at 2011-01-23 14:23:29

Changing keywords from "editor_craigcitro" to "editor_craigcitro pari".


---

Comment by jdemeyer created at 2011-01-23 14:23:29

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2011-01-23 14:23:29

Making some changes...


---

Comment by jdemeyer created at 2011-01-23 18:13:22

I moved the PARI part of this patch to #10677, so this patch now depends on #10677.


---

Attachment

Apply only this, rebased to sage-4.6.2.alpha1 + #10677


---

Attachment

Apply only this, rebased to sage-4.6.2.alpha1 + #10677


---

Comment by jdemeyer created at 2011-01-23 20:12:07

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2011-02-10 16:27:09

For me, this ticket gets positive review.  However, somebody needs to review my reviewer patch.


---

Comment by davidloeffler created at 2011-02-10 16:59:19

This line worries me slightly:

```
2613	        Kbnf = self.pari_bnf(certify=certify).nf_subst("'y") 
```


Is that supposed to be `("y")` or `("'y'")` perhaps?


---

Comment by jdemeyer created at 2011-02-11 08:23:00

Apply on top of previous patch


---

Attachment

Replying to [comment:45 davidloeffler]:
> Is that supposed to be `("y")` or `("'y'")` perhaps?

No, `'y` is correct.  I have added some comments to that code in the patch.

Basically, the `'y` syntax is PARI's way of refering to a _variable_ (as opposed to the _value_ of a variable).  See the following `gp` session:


```
gp> y = 42
%1 = 42
gp> y
%2 = 42
gp> 'y
%3 = y
gp> subst(x^3, x, y)
%4 = 74088
gp> subst(x^3, x, 'y)
%5 = y^3
```



---

Comment by jdemeyer created at 2011-02-11 08:31:27

Let me also clarify that, even though I uploaded [attachment:trac_2329_rnfisnorm5.patch], I only rebased the existing patch and moved parts of it to #10677.  So I believe that I am allowed to review that patch.  Only [attachment:2329_reviewer.patch] still needs review.


---

Comment by davidloeffler created at 2011-02-11 14:09:28

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2011-02-11 14:09:28

Thanks for the very clear explanation. The two patches apply and compile fine, and all doctests pass.


---

Comment by jdemeyer created at 2011-03-04 10:14:09

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-03-04 10:15:07

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2011-03-04 10:15:07

I have a new patch to change the Selmer group test, since the signs can change randomly.  Needs review.


---

Comment by jdemeyer created at 2011-03-04 12:46:56

Changing priority from major to blocker.


---

Comment by fbissey created at 2011-03-05 05:15:40

Probably related, I got this on x86 with 4.7.alpha2

```
sage -t -long  -force_lib devel/sage-main/sage/rings/rational.pyx
**********************************************************************
File  
"/storage/strogdon/gentoo/usr/share/sage/devel/sage-main/sage/rings/rational.pyx",  
line 1222:
     sage: (1/5).is_norm(QuadraticField(5/4, 'a'), element=True)
Expected:
     (True, -1/5*a + 1/2)
Got:
     (True, 1/5*a - 1/2)
```

The log is from a friend of mine who has it as well on x86 but it doesn't show up on his amd64 hardware. I cannot test on amd64 or OSX at the present time.


---

Comment by jdemeyer created at 2011-03-07 19:18:09

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2011-03-07 19:18:09

Replying to [comment:52 fbissey]:
> Probably related, I got this on x86 with 4.7.alpha2

Good to know this.  But keep in mind that sage-4.7.alpha2 has not been released (not even sage-4.7.alpha0).  In the future it would be better to test released versions with patches applied instead of unreleased versions.

I will test this patch on a 32-bit system and see what needs to be fixed.


---

Attachment

Additional patch


---

Comment by jdemeyer created at 2011-03-11 12:54:13

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2011-03-11 22:53:28

I can confirm that the doctest now passes on a 32-bit build of sage-4.7.alpha1 on OpenSolaris 06/2009 (Intel Xeon chip)


```
sage -t -long -force_lib "devel/sage/sage/rings/number_field/number_field.py"
	 [48.8 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 48.8 seconds
```


Prior to adding the 3 patches to sage-4.7.alpha1, I got. 


```
File "/export/home/drkirkby/sage-4.7.alpha1/devel/sage-main/sage/rings/number_field/number_field.py", line 3035:
    sage: K.selmer_group([K.ideal(2, -a+1), K.ideal(3, a+1), K.ideal(a)], 3)
Expected:
    [2, a + 1, a]
Got:
    [2, a + 1, -a] 
```



I don't know enough about the maths to understand what the patch does, so whilst it appears to fix the problems I see in sage-4.7.alpha1, I don't feel I should give this a positive review - it needs a mathematician to check it too. 

Dave


---

Comment by jdemeyer created at 2011-03-12 09:52:25

David, could you please test both _with_ and _without_ `-long`.


---

Comment by drkirkby created at 2011-03-14 06:52:54

Replying to [comment:57 jdemeyer]:
> David, could you please test both _with_ and _without_ `-long`.
With the patch applied, it is taking about 22 seconds _without_ -long, and 46 seconds _with_ -long. 

If the patch is not applied, it fails _with_ or _without_ -long.


---

Comment by davidloeffler created at 2011-03-14 14:23:30

> it needs a mathematician to check it too. 

Looks OK to me.


---

Comment by davidloeffler created at 2011-03-14 14:23:30

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-03-17 19:23:55

Resolution: fixed
