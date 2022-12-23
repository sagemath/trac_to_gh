# Issue 5513: Enhanced support for number field unit groups

Issue created by migration from https://trac.sagemath.org/ticket/5513

Original creator: cremona

Original creation time: 2009-03-13 22:02:06

Assignee: was

CC:  davidloeffler

Keywords: number field unit group

The attached patch (based on 3.4) implements a new class UnitGroup for the unit group of a number field.  As before, the units are computed using the pari library, but now it is easier (for example) to obtain all generators of the unit group.  Also, I have added a wrapping for the pari function bnfisunit() which implements a discrete log function to express any unit in terms of the generators.

As well as all the documented code and examples in unit_group.py there are added functions in number_field.py.


---

Attachment


---

Comment by fwclarke created at 2009-03-16 14:34:25

This seems to work fine, with some exceptions for relative number fields.  
For example, with my current favourite extension,

```
PQ.<X> = QQ[]
F.<a, b> = NumberField([X^2 - 2, X^2 - 3])
PF.<Y> = F[]
K.<c> = F.extension(Y^2 - (1 + a)*(a + b)*a*b)
K.unit_group()
```

fails.

But the cause lies beyond this patch.  There are many problems with the
existing code for relative number fields, some addressed in my patch in
#5508, others to follow soon in a revised patch.

In this case the culprit is the use of `pari_bnf` in the line `pK = K.pari_bnf(proof)` 
at line 145 of `unit_group.py`.  For in `pari_bnf`,
the lines

```
if self.polynomial().denominator() != 1:
    raise TypeError, "Unable to coerce number field defined by ..."
}}}  
exclude extensions like `K`.  The solution is, of course, to use 
`self.absolute_polynomial()`; this change could be included 
in the patch.

So my review is positive, subject to some small changes listed below,
with the expectation that forthcoming changes to other functions will make
the code work for all (sufficiently small) relative number fields.

## Minor points

   * Three times:
      "but we do use if it is already known"
      should surely be
      "but we do use it if it is already known"

   * In `zeta`,
      {{{
              z = self.primitive_root_of_unity() ** (N//n)`
      }}}
     would be more consistently written as
     {{{
              z = K.primitive_root_of_unity() ** (N//n)`
     }}}


   * In `roots_of_unity` 
      {{{
              n = z.multiplicative_order()
      }}}
     would surely be better as
     {{{
              n = self.zeta_order()
     }}}

## Further remark

While we're working on units, one thing that should be fixed is the 
following:
{{{
sage: K.<b> = NumberField([x^2 - 3])
sage: K.zeta(5)
Traceback (most recent call last)
...
ArithmeticError: There are no roots of unity of order 5 in this unit group
}}}
compared to
{{{
sage: C.<z> = CyclotomicField(20)
sage: C.zeta(7)
Traceback (most recent call last)
...
ValueError: n (=7) does not divide order of generator
}}}
There seems to be no reason why the error type should be different, and I 
found an example where a function failed for cyclotomic fields because of 
this disparity.


---

Comment by cremona created at 2009-03-16 14:49:15

Thanks a lot Francis!  I will sort out those things and upload a new patch shortly.  John


---

Comment by cremona created at 2009-03-16 15:35:01

REPLACES the earlier patch


---

Attachment

Apply after the earlier patch


---

Attachment

I have fixed all the issues raised in the review in the new patch trac_5513.patch.  I added a doctest in unit_group.py to show that the relative example now works.  I tested all in sage/rings/number_field.

Apologies for the confusion:  I thought that my new patch (called trac_5513.patch) replaced the origianl one because I was using mercurial queues, but (as usual) I was wrong.  You need to apply the original units.patch and then the new one (trac_5513.patch) which appear twice on trac, once with the worng message and once with the right one.  I hope that is clear.


---

Comment by fwclarke created at 2009-03-16 20:08:52

A couple more things: 
   * two more replacements of `defining_polynomial` by `absolute_polynomial` are needed.

   * units can have norm -1.

With the third patch everything works.


---

Comment by fwclarke created at 2009-03-16 20:11:13

apply after the other two


---

Attachment

Replying to [comment:5 fwclarke]:
> A couple more things: 
>    * two more replacements of `defining_polynomial` by `absolute_polynomial` are needed.
> 
>    * units can have norm -1.
> 
> With the third patch everything works.

Thanks a lot -- for what it's worth, I am (more than) happy with the third patch, also a little red-faced about the norms!


---

Comment by cremona created at 2009-03-16 20:42:27

Replying to [comment:6 cremona]:
> Replying to [comment:5 fwclarke]:
> > A couple more things: 
> >    * two more replacements of `defining_polynomial` by `absolute_polynomial` are needed.
> > 
> >    * units can have norm -1.
> > 
> > With the third patch everything works.
> 
> Thanks a lot -- for what it's worth, I am (more than) happy with the third patch, also a little red-faced about the norms!

PS Francis, if yo ufancied looking at #5518 too you can have the satisfaction of adding .norm() in a similar place.  It's a lot simpler and shorter than this one.


---

Comment by mabshoff created at 2009-03-25 09:28:00

This patch set no longer applies after merging #5508.

Francis: Can you rebase this patch set? Once it is rebased the positive review should be reinstated provided the changes are minimal, otherwise we should have another review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-25 09:29:02

Ooops, I guess John should do the rebase here :)

Cheers,

Michael


---

Comment by cremona created at 2009-03-28 16:31:16

Replaces all above, reabsed to 3.4 + sage-5508.3.patch


---

Attachment

I have attached a single patch which replaces all previous ones and is rebased on 3.4 + sage-5508.3.patch, as requested.


---

Comment by fwclarke created at 2009-03-29 19:58:14

Looks fine to me.  Positive review.


---

Comment by cremona created at 2009-03-30 09:02:42

Alternaitve, rebased to 3.4 + #550 + #5159


---

Attachment

Thanks, Francis.   For ease of merging I have also provided another rebased patch which applies to 3.4 + sage-5508.3.patch + the patches at #5159 since I hope/expect that one to be merged shortly and now the whole lot are compatible.


---

Comment by mabshoff created at 2009-03-31 07:47:18

[CCing David]

I am waiting to see if #5159 will have all its issues fixed in the next 12 to 24 hours, otherwise I will merge the rebased patch that only depends on 3.4 + #5508.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-31 08:06:23

units_rebase.patch by itself does not apply for me to 3.4.1.alpha0 (which includes #5508), so I am waiting on #5159 to go in before trying again. Does this patch depend on anything else?

Cheers,

Michael


---

Comment by cremona created at 2009-03-31 08:11:32

Replying to [comment:14 mabshoff]:
> units_rebase.patch by itself does not apply for me to 3.4.1.alpha0 (which includes #5508), so I am waiting on #5159 to go in before trying again. Does this patch depend on anything else?

It shouldn't do, but I did not have a working 3.4.1.alpha0 until late yesterday.  I'll look into that right now, as well as #5159.

> 
> Cheers,
> 
> Michael


---

Comment by cremona created at 2009-03-31 08:43:00

I cloned a freshly built 3.4.1.alpha0 and (using hg_sage.apply()) successfully applied units_rebase.patch to it.  No warnings.  No problems with sage -br.   BUT then doing sage -t on sage/rings/number_field threw up a large number of very weird errors I have never seen before:  example:

```

sage -t  "local/sage-3.4.1.alpha0/devel/sage-5513a/sage/rings/number_field/number_field.py"
  File "./number_field.py", line 18
    from local/sage-3.4.1.alpha0/devel/sage-5513a/sage/rings/number_field/number_field import *
              ^
SyntaxError: invalid syntax

         [0.4 s]
exit code: 1024

```


What is that about?   Something seems to have inserts forward slashes into a python file instead of dots.


---

Comment by davidloeffler created at 2009-03-31 08:46:52

I've been seeing this too: there's been some changes in the doctesting mechanism in 3.4.1.alpha0 that seem to have broken it almost completely.


---

Comment by mabshoff created at 2009-03-31 09:12:12

Replying to [comment:17 davidloeffler]:
> I've been seeing this too: there's been some changes in the doctesting mechanism in 3.4.1.alpha0 that seem to have broken it almost completely. 

I cannot reproduce this - but I did not try to apply this patch set. What I tried:

 * use -tp
 * use -t from inside the Sage tree
 * use -t from outside the Sage tree

Can someone give me exact instructions on how to reproduce this?

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-31 09:13:31

Can you try reverting #2129 and see if the problem goes away? That seem to be the only patch I would suspect here to cause trouble.

Cheers,

Michael


---

Comment by davidloeffler created at 2009-03-31 09:44:05

I have posted in sage-devel about this. The problem comes up when you use sage -t from within the sage tree.


---

Comment by mabshoff created at 2009-03-31 09:56:12

Using units_rebased2.patch there are a bunch of probably 32 vs. 64 bit doctest failures:

```
sage -t -long devel/sage/sage/rings/number_field/unit_group.py
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc0/devel/sage-main/sage/rings/number_field/unit_group.py", line 11:
    sage: UK.gens()
Expected:
    [1/12*a^3 - 1/6*a, 1/24*a^3 + 1/4*a^2 - 1/12*a - 1]
Got:
    [1/12*a^3 - 1/6*a, 1/24*a^3 - 7/12*a - 1/2]
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc0/devel/sage-main/sage/rings/number_field/unit_group.py", line 31:
    sage: UK.fundamental_units()
Expected:
    [1/24*a^3 + 1/4*a^2 - 1/12*a - 1]
Got:
    [1/24*a^3 - 7/12*a - 1/2]
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc0/devel/sage-main/sage/rings/number_field/unit_group.py", line 43:
    sage: u = UK.exp([13,10]); u
Expected:
    -41/8*a^3 - 55/4*a^2 + 41/4*a + 55
Got:
    41/8*a^3 + 55/4*a^2 - 41/4*a - 55
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc0/devel/sage-main/sage/rings/number_field/unit_group.py", line 64:
    sage: UL.gens()
Expected:
    [-b^3*a - b^3, -b^3*a + b, (-b^3 - b^2 - b)*a - b - 1, (-b^3 - 1)*a - b^2 + b - 1]
Got:
    [-b^3*a - b^3, -b^3*a + b, a - b^3 + 1, (-b^2 - b)*a - b^3 - b^2 + 1]
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc0/devel/sage-main/sage/rings/number_field/unit_group.py", line 374:
    sage: U.torsion_generator()
Expected:
    -1/4*a^3 - 1/4*a + 1/2
Got:
    1/4*a^3 + 1/4*a + 1/2
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc0/devel/sage-main/sage/rings/number_field/unit_group.py", line 164:
    sage: UK.gens()
Expected:
    [-z^11, z^5 + z^3, z^6 + z^5, z^9 + z^7 + z^5, z^9 + z^5 + z^4 + 1, z^5 + z]
Got:
    [-z^3, z^5 + z^3, z^6 + z^5, z^9 + z^7 + z^5, z^9 + z^5 + z^4 + 1, z^5 + z]
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc0/devel/sage-main/sage/rings/number_field/unit_group.py", line 303:
    sage: UK.gen(0)
Expected:
    -z^11
Got:
    -z^3
**********************************************************************
4 items had failures:
   4 of  35 in __main__.example_0
   1 of   6 in __main__.example_12
   1 of  12 in __main__.example_2
   1 of  11 in __main__.example_8
***Test Failed*** 7 failures.
For whitespace errors, see the file /scratch/mabshoff/sage-3.4.1.rc0/tmp/.doctest_unit_group.py
	 [2.0 s]
```


Cheers,

Michael


---

Comment by cremona created at 2009-03-31 09:59:51

replace previous


---

Attachment

ok -- see newest patch (units_rebased3.patch, to replace units_rebased2.patch).

I took the lazy way out and added #random to all the outputs which return actual units.  It may be a 32/64 issue, but not just that since when testing this patch on one machine I kept on getting different generating units out of pari.  I seem to remember that there is a way to "reset" pari in doctests  to avoid this random-ness.

Mathematically this is not so unreasonable since any f.g. abelian group will lots (infinitely many) sets of generators and there is no way to pick one canonically.  (William and I thought about this for elliptic curve generators and came up against an unsolved problem which prevents this being possible even in principle!).


---

Comment by cremona created at 2009-04-02 09:42:22

Replying to [comment:22 cremona]:
> ok -- see newest patch (units_rebased3.patch, to replace units_rebased2.patch).
> 
> I took the lazy way out and added #random to all the outputs which return actual units.  It may be a 32/64 issue, but not just that since when testing this patch on one machine I kept on getting different generating units out of pari.  I seem to remember that there is a way to "reset" pari in doctests  to avoid this random-ness.
> 
> Mathematically this is not so unreasonable since any f.g. abelian group will lots (infinitely many) sets of generators and there is no way to pick one canonically.  (William and I thought about this for elliptic curve generators and came up against an unsolved problem which prevents this being possible even in principle!).

Michael,

since all I did here was to add #random to the problem tests, does this need more review or could it be merged now?


---

Comment by mabshoff created at 2009-04-03 00:43:54

John,

William has given his "thumbs up" to this patch and the latest changes, so let's make this a positive review. This patch also passes doctests with my current 3.4.1.rc0 merge tree.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-03 00:45:04

Resolution: fixed


---

Comment by mabshoff created at 2009-04-03 00:45:04

Merged units_rebased3.patch in Sage 3.4.1.rc0.

Cheers,

Michael
