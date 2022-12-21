# Issue 4933: lots of files in sage.schemes.elliptic_curves are not included in the reference manual

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2009-01-03 17:59:06

Assignee: tba

Keywords: documentation

The following files have useful docstrings but are not included in the ref manual (judging from 3.2.3), all in sage.schemes.elliptic_curves.
   * cm.py
   * ec_database.py
   * ell_field.py
   * ell_local_data.py
   * ell_modular_symbols
   * ell_number_field
   * ell_padic_field
   * ell_point.py
   * ell_tate_curve.py
   * ell_torsion.py
   * kodaira_symbol.py
   * lseries_ell.py
   * padic_lseries.py
   * period_lattice.py
   * sha_tate.py
   * weierstrass_morphism.py


---

Comment by GeorgSWeber created at 2009-02-25 21:30:48

Hi,

the files

 * ell_modular_symbols.py
 * ell_tate_curve.py
 * padic_lseries.py
 * sha_tate.py

are not only enhanced in a vital way but also considerably cleaned up docstring- and comment-wise by #4667. The patch there is currently based against 3.3 and needs a rebase concerning two files (ell_rational_field.py, padocs.py) against 3.4 series, and there is still one doctest failure, but nevertheless I do consider #4667 worth of applying before working on this very ticket here!


---

Comment by mabshoff created at 2009-03-01 02:23:13

Better luck in 3.4.1.

Cheers,

Michael


---

Attachment


---

Comment by cremona created at 2009-04-15 16:29:29

I have attached a patch trac_4933-1.patch which does this for three files:
    * ell_number_field.py
    * ell_torsion.py
    * ell_point.py
which is a start.

The patch rewrites all the docstrings in those files and also adds them to the list of files which are processed by "sage -docbuild reference" so that they show up in the reference manual.

To review/test the patch (which was based on 3.4.1.rc2), you need to apply it and rebuild, and then (1) do  "sage -t" is usual on the files affected, and (2) do "sage -docbuild reference pdf/html/whatever" to check that the documentation looks good.


---

Attachment

Two more;  apply after previous.


---

Comment by cremona created at 2009-04-16 16:36:00

The second patch adds a couple more files (weierstrass_morphism and period_lattice).


---

Attachment

IGNORE all previous patches.  This is based on 3.4.1.rc3


---

Comment by cremona created at 2009-04-17 14:06:15

Changing keywords from "documentation" to "documentation, elliptic curves".


---

Comment by cremona created at 2009-04-17 14:06:15

The patch trac_4933-3.patch converts the following to rest/sphinx and adds them to the reference manual:
    * ell_number_field
    * ell_local_data
    * ell_torsion
    * ell_point
    * period_lattice
    * weierstrass_morphism
as well as fixing some glitches in other files (notable ell_rational_field) and adding a few doctests.

Almost all the changes are in docstrings.  To review this you'll have to build the docs (reference manual) and eyeball the output.

NB I combined more than one earlier patch into one, but failed to get "sage -hg qfold" to work, so i nthe patch there are liable to be more than one chunk for each file.


---

Comment by jhpalmieri created at 2009-04-17 14:24:14

If you're patching ell_rational_field, can you fix the doc string for mwrank?  It looks pretty garbled to me, and I don't know what it's supposed to say...


---

Comment by cremona created at 2009-04-17 14:29:43

Replying to [comment:7 jhpalmieri]:
> If you're patching ell_rational_field, can you fix the doc string for mwrank?  It looks pretty garbled to me, and I don't know what it's supposed to say...

It looks pretty clear to me, except perhaps where it explains the format of the options string.  Perhaps we should just include the output of "sage -mwrank -h":

```
mwrank command line options (can be in any order):

-h      help            prints this info and quits
-q      quiet           turns OFF banner display
-v n    verbosity       sets verbosity to n (default=1)
-o      PARI/GP output  turns ON extra PARI/GP short output (default is OFF)
-p n    precision       sets precision to n decimals (default=15)
                        (irrelevant unless compiled with multiprecision option)
-b n    quartic bound   bound on quartic point search (default=10)
-x n    n aux           number of aux primes used for sieving (default=6)
-l      list            turns ON listing of points (default ON unless v=0)
-t      trace           turns ON trace of quartic equivalence testing (debugging only)
-s      selmer_only     if set, computes Selmer rank only (default: not set)
-d      skip_2nd_descent        if set, skips the second descent for curves with 2-torsion (default: not set)
-S n    sat_bd          upper bound on saturation primes (default=100, -1 for automatic)
```



---

Comment by jhpalmieri created at 2009-04-17 15:13:55

>It looks pretty clear to me, except perhaps where it explains the format of the options string. 

Do you mean this part?
{{{ 
        -  ``options`` - string; passed when starting mwrank.
           The format is q pprecision vverbosity bhlim_q xnaux chlim_c l t o
           s d]
}}}


---

Comment by cremona created at 2009-04-17 15:14:48

Replying to [comment:9 jhpalmieri]:
> >It looks pretty clear to me, except perhaps where it explains the format of the options string. 
> 
> Do you mean this part?
> {{{ 
>         -  ``options`` - string; passed when starting mwrank.
>            The format is q pprecision vverbosity bhlim_q xnaux chlim_c l t o
>            s d]
> }}}
Yes!


---

Attachment

Replaces previous;  based on 3.4.1.rc3 + #5808 patch


---

Comment by cremona created at 2009-04-17 15:56:26

The new patch (trac_4933-3-rebase.patch) replaces the earlier one as it applies cleanly to 3.4.1.rc3 + ref-warnings.patch from #5808.  It also answers John Palmieri's request to make the docstring for mwrank() less confusing.

I think the reason that this one is smaller is that the previous one applied several patches in succession to the same files, while this one does not.  At least, I hope that is the reason.


---

Comment by jhpalmieri created at 2009-04-17 21:09:59

Code looks good, all tests pass, the reference manual looks nice. I'm attaching a referee's patch with two very small changes.


---

Comment by jhpalmieri created at 2009-04-17 21:10:30

apply on top of the other patch


---

Attachment

Replying to [comment:12 jhpalmieri]:
> Code looks good, all tests pass, the reference manual looks nice. I'm attaching a referee's patch with two very small changes.

Thanks John -- I am quite happy with your adjustments.


---

Comment by mabshoff created at 2009-04-18 01:52:45

Resolution: fixed


---

Comment by mabshoff created at 2009-04-18 01:52:45

Merged  trac_4933-3-rebase.patch and 4933-ref.patch in Sage 3.4.1.rc4.

Cheers,

Michael


---

Comment by cremona created at 2009-04-22 10:42:10

This is continued in #5851.
