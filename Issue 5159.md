# Issue 5159: Add functionality to Galois groups

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2009-02-02 17:51:14

Assignee: davidloeffler

Keywords: galois groups, number theory

It would be nice to unify Sage's two ways of handling Galois groups: as abstract transitive groups, and as sets of explicit automorphisms with no group structure. This can be done by using Pari's galoisinit, galoispoltoperm and galoisapply functions.




---

Comment by davidloeffler created at 2009-02-02 18:00:12

The above patch should do the job for absolute fields: it creates a new GaloisGroup class, which has very little resemblance to the old one, and derives from PermutationGroup_generic. The init script calls Pari's galoisinit. Elements are stored as GaloisGroupElement objects, which are basically permutations, but with the addition of a cached method that returns the image of a generator of that permutation under the corresponding automorphism. 

I've also added toy implementations of decomposition and ramification groups and the Artin symbol for prime ideals in number fields; I'm sure there are faster algorithms to calculate these rather than using the definitions directly as I've done, but I am a strong believer in toy implementations.

At present this is all only for absolute fields, because Pari has no direct support for Galois groups of relative extensions. Relative fields could also be implemented, at least when the corresponding absolute field is Galois over QQ, by calculating the Galois group of the absolute extension and checking which automorphisms fix the intermediate field; but I haven't done this.


---

Comment by davidloeffler created at 2009-02-02 18:00:12

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-02-06 23:04:17

3.4 is for ReST tickets only.

Cheers,

Michael


---

Comment by cremona created at 2009-03-16 21:03:17

This looks like great work which will be extremely useful, but needs to be rebased on 3.4  (i.e. change the docstrings in number_field.py into ReST style) before it can be tested.

At the same time, I think you can safely replace the old galois_group.py with the new one instead of leaving there and adding _new to your name.

I'll do a proper review when rebased, as so far as have just read the patch.


---

Comment by davidloeffler created at 2009-03-17 18:47:27

patch against 3.4 with patch for #5508 applied


---

Attachment

I've rebased it to a patch based on (3.4 + the patch for #5508).

This version actually adds quite a bit that wasn't in the previous version: based on the debate on sage-nt, I've made it return the Galois group of the splitting field when the given field isn't Galois, and also added a method fixed_field for subgroups of Galois groups based on Pari's "galoisfixedfield".

In an ideal world, when given a non-Galois field, it would return the Galois group of the Galois closure of the given field, but represented as permutations of the roots of the defining polynomial of the original field. I couldn't work out an easy way of doing this which wouldn't be horribly slow in general, so elements are represented as permutations of the Galois conjugates of some single element generating the Galois closure.

I've also ReSTified class_group.py and number_field_ideal.py (the latter because I was editing it anyway, and the former because it was easy to do); and deprecated galois_group and is_galois for relative fields in favour of explicitly relative and absolute variants.


---

Comment by cremona created at 2009-03-17 21:56:59

I'm not sure whether I did something stupid here but in a fresh clone of 3.4 I applied sage-5508.2.patch from #5508 and then tried to apply the new galois.patch form here, but it does not apply properly:

```
sage: hg_sage.apply("galois.patch")
cd "/home/john/sage-3.4/devel/sage" && hg status
cd "/home/john/sage-3.4/devel/sage" && hg status
cd "/home/john/sage-3.4/devel/sage" && hg import   "/home/john/galois.patch"
applying /home/john/galois.patch
patching file sage/rings/number_field/number_field.py
Hunk #3 FAILED at 2536
Hunk #4 FAILED at 2555
Hunk #5 FAILED at 4147
Hunk #6 FAILED at 4160
4 out of 6 hunks FAILED -- saving rejects to file sage/rings/number_field/number_field.py.rej
abort: patch failed to apply
```


Did I misunderstand something?  John


---

Comment by davidloeffler created at 2009-03-17 22:56:58

Weird. I was using the first version of the #5508 patch, not the second, but that shouldn't make a huge difference. I will look at it in the morning.


---

Comment by cremona created at 2009-03-18 08:37:47

Replying to [comment:7 davidloeffler]:
> Weird. I was using the first version of the #5508 patch, not the second, but that shouldn't make a huge difference. I will look at it in the morning.


```
john`@`ubuntu%diff /home/john/sage-5508.2.patch /home/john/sage-5508.patch 
1679c1679
< +            a
---
> +            sage: a
```



---

Attachment

replaces previous patch -- apply after sage-5508.2.patch


---

Comment by davidloeffler created at 2009-03-18 09:03:46

Here's a new patch. On my machine I've checked that it applies happily on a clean clone of 3.4 with sage-5508.2.patch on top. Let me know if this works for you too.


---

Attachment


---

Comment by cremona created at 2009-03-18 10:02:33

Good news: this patch applies fine on top of sage-5508.2.patch.

I am very happy with this patch which provides a significant new set of functions and capabilities.  I did have two trivial doctest failures, in two files, nothing serious:

```
sage -t  "local/sage-3.4/devel/sage-5159/sage/rings/number_field//number_field.py"
**********************************************************************
File "/home/masgaj/local/sage-3.4/devel/sage-5159/sage/rings/number_field/number_field.py", line 3067:
    sage: G = k.galois_group(names='c'); G
Expected:
    Galois group of Number Field in b with defining polynomial x^3 - x + 1
Got:
    Galois group of Galois closure in c of Number Field in b with defining polynomial x^3 - x + 1

  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.
*********************************************************************
```


and


```
sage -t  "local/sage-3.4/devel/sage-5159/sage/rings/number_field//galois_group.py"
**********************************************************************
File "/home/masgaj/local/sage-3.4/devel/sage-5159/sage/rings/number_field/galois_group.py", line 479:
    sage: from sage.rings.number_field.galois_group_new import GaloisGroup_subgroup
Exception raised:
    Traceback (most recent call last):
      File "/home/masgaj/local/sage-3.4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/masgaj/local/sage-3.4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/masgaj/local/sage-3.4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[2]>", line 1, in <module>
        from sage.rings.number_field.galois_group_new import GaloisGroup_subgroup###line 479:
    sage: from sage.rings.number_field.galois_group_new import GaloisGroup_subgroup
    ImportError: No module named galois_group_new
*******************************************************************
```


I have put up a small patch which fixes these, so it can have a positive review.


---

Comment by mabshoff created at 2009-03-25 09:08:14

The latest patch on top of #5508 causes a number of doctest failures:

```
	sage -t -long devel/sage/doc/en/bordeaux_2008/nf_galois_groups.rst # 3 doctests failed
	sage -t -long devel/sage/sage/structure/sage_object.pyx # 1 doctests failed
	sage -t -long devel/sage/sage/rings/number_field/galois_group.py # 2 doctests failed
	sage -t -long devel/sage/doc/en/tutorial/tour_numtheory.rst # 1 doctests failed
	sage -t -long devel/sage/doc/fr/tutorial/tour_numtheory.rst # 1 doctests failed
```


Cheers,

Michael


---

Attachment

apply over 5508-3.patch and previous TWO patches.


---

Comment by davidloeffler created at 2009-03-25 11:16:34

I've done a new patch which fixes the above five doctest failures. The only difficulty was the pickle jar failure, which I've circumvented by renaming the classes GaloisGroup_v1 and GaloisGroup_v2, and aliasing GaloisGroup to GaloisGroup_v1; as the name GaloisGroup isn't imported into the global namespace anyway -- one constructs the objects using the galois_group method of number field objects -- this has no visible effect for the user, and unpickling now works fine.

In the process I spotted that the doctest failure that necessitated the final patch at #5508 seems to be machine-dependent, presumably a 32-bit / 64-bit thing. So the new patch adjusts that doctest to allow two different answers for 32-bit and 64-bit in the usual way; and I also put in a doctest in the __call__ method of number field relative orders to confirm that #4193 is fixed. 

David


---

Comment by davidloeffler created at 2009-03-27 11:38:19

Michael: what is the next step with this one? Given that the new patch changes nothing that the user sees, can it just be merged, or is a new review needed for the new patch? 

David


---

Comment by mabshoff created at 2009-03-27 16:01:07

Replying to [comment:15 davidloeffler]:
> Michael: what is the next step with this one? Given that the new patch changes nothing that the user sees, can it just be merged, or is a new review needed for the new patch? 
> 
> David
> 

It would still be nice if someone did a quick re-review of the last two patches.

Cheers,

Michael


---

Comment by cremona created at 2009-03-29 17:48:51

I can confirm that the patches apply ok as described, based on 3.4.  I have not yet tried on 3.4.1, or tested whether my rebased patch for #5513 will still work, but will do that.

I have relabelled this "positive review" although on of the new patches -- the very trivial one -- was mine.


---

Comment by davidloeffler created at 2009-03-29 17:59:30

I have just checked that it applies cleanly to 3.4.1.alpha0, and sage -testall passes.


---

Comment by cremona created at 2009-03-30 11:00:37

Oops:  on a 64-bit machine I get this:

```
jec`@`host-57-44:~/sage-3.4/devel/sage-5159$ sage -t sage/rings/number_field/galois_group.py
sage -t  "devel/sage-5159/sage/rings/number_field/galois_group.py"
**********************************************************************
File "/home/jec/sage-3.4/devel/sage-5159/sage/rings/number_field/galois_group.py", line 343:
    sage: G.decomposition_group(P^2)
Expected:
    Traceback (most recent call last):
    ...
    ValueError: Fractional ideal (1/984*a^7 - 71/1968*a^5 + 29/984*a^3 + 527/328*a) is not prime
Got:
    Traceback (most recent call last):
      File "/home/jec/sage-3.4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jec/sage-3.4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jec/sage-3.4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_18[6]>", line 1, in <module>
        G.decomposition_group(P**Integer(2))###line 343:
    sage: G.decomposition_group(P^2)
      File "/home/jec/sage-3.4/local/lib/python2.5/site-packages/sage/rings/number_field/galois_group.py", line 357, in decomposition_group
        raise ValueError, "%s is not prime" % P
    ValueError: Fractional ideal (-1/492*a^7 + 101/1968*a^5 - 115/328*a^3 + 1717/984*a) is not prime
**********************************************************************
File "/home/jec/sage-3.4/devel/sage-5159/sage/rings/number_field/galois_group.py", line 445:
    sage: G.artin_symbol(K.primes_above(2)[0])
Expected:
    Traceback (most recent call last):
    ...
    ValueError: Fractional ideal (-1/8364*b^7 + 1/492*b^6 - 11/16728*b^5 - 101/1968*b^4 + 209/2788*b^3 + 115/328*b^2 - 3139/8364*b + 251/984) is ramified
Got:
    Traceback (most recent call last):
      File "/home/jec/sage-3.4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jec/sage-3.4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jec/sage-3.4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_22[7]>", line 1, in <module>
        G.artin_symbol(K.primes_above(Integer(2))[Integer(0)])###line 445:
    sage: G.artin_symbol(K.primes_above(2)[0])
      File "/home/jec/sage-3.4/local/lib/python2.5/site-packages/sage/rings/number_field/galois_group.py", line 463, in artin_symbol
        if len(t) > 1: raise ValueError, "%s is ramified" % P
    ValueError: Fractional ideal (43/33456*b^7 + 7/1968*b^6 - 809/33456*b^5 - 35/656*b^4 + 367/2788*b^3 + 61/492*b^2 - 4651/16728*b + 757/984) is ramified
**********************************************************************
2 items had failures:
   1 of   8 in __main__.example_18
   1 of   8 in __main__.example_22
```


I think you cannot rely on pari giveing you the primes in a specific order:

```
sage: P = K.primes_above(17)[0]
sage: P
Fractional ideal (1/492*a^7 - 101/1968*a^5 + 115/328*a^3 - 733/984*a)
sage: P^2
Fractional ideal (-1/492*a^7 + 101/1968*a^5 - 115/328*a^3 + 1717/984*a)
sage: Q = K.primes_above(17)[1]
sage: Q^2
Fractional ideal (-5/2788*a^7 + 587/11152*a^5 - 2791/5576*a^3 + 13915/5576*a)
```

so the doctest needs to be designed to allow for that.  Perhaps define P via

```
sage: P=K.ideal(17,a^2)
sage: P
Fractional ideal (1/492*a^7 - 101/1968*a^5 + 115/328*a^3 - 733/984*a)
sage: P.is_prime()
True
```

(which may or may not be the P i your doctest).


---

Comment by davidloeffler created at 2009-03-30 12:52:36

It doesn't greatly matter which P is being used, since they are all Galois-conjugate. Thus I have put a "..." in the two doctests that failed above. I've tested it on a 64-bit machine with this fix and now all doctests in sage/rings/number_fields pass there too. Patch coming in a moment.

David


---

Comment by davidloeffler created at 2009-03-30 12:53:01

Apply over previous three patches


---

Attachment


---

Comment by mabshoff created at 2009-03-31 07:19:00

When merging

 * trac_5159_galois_new.patch
 * trac_5159_extra.patch
 * trac_5159-unpickle-fix.patch
 * trac_5159-64bit-doctest.patch

I am seeing the following doctest failure on sage.math, i.e. 64 bit Linux:

```
sage -t -long "devel/sage/doc/en/bordeaux_2008/nf_galois_groups.rst"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc0/devel/sage/doc/en/bordeaux_2008/nf_galois_groups.rst", line 44:
    sage: [G.artin_symbol(Q) for Q in K.primes_above(5)]
Expected:
    [(1,5)(2,4)(3,6), (1,3)(2,6)(4,5), (1,2)(3,4)(5,6)]
Got:
    [(1,5)(2,4)(3,6), (1,2)(3,4)(5,6), (1,3)(2,6)(4,5)]
**********************************************************************
```

I would guess that sorting the list might fix the issue.

Cheers,

Michael


---

Comment by davidloeffler created at 2009-03-31 08:36:39

Sorting the list exposed another bug, which I refuse to accept any responsibility for whatsoever: there is something funny going on in the default __cmp__ routine in sage.structure.element.Element, which meant that if x,y were GaloisGroupElements then cmp(x, y) worked but sorted([x, y]) didn't. 

I've worked around this by implementing __cmp__ directly for GaloisGroupElements. This gets the doctests in doc/en/bordeaux_2008 to pass on 32bit and 64bit.

Apologies that these things didn't get spotted earlier, but I'm working from home on a clapped out old 32-bit laptop, on which running sage -testall takes over three hours, so when I was working on this I only ran the doctests in sage/rings/number_field. That's a mistake I won't make again.

David


---

Comment by davidloeffler created at 2009-03-31 08:37:09

apply over previous four patches (!)


---

Attachment

I'll test all these in a minute....


---

Comment by cremona created at 2009-03-31 08:56:04

Replying to [comment:24 cremona]:
> I'll test all these in a minute....
unfortunately the total weirdness I came across just now in testing 5513 is still here.  It looks like I cannot test anything on 3.4.1.alpha0 without rebuilding from scratch, which unfortunately would not finish until after my free time for the day is over.  So unless mabshoff has any idea what was causing that, it will be hard for me to do anything useful for a while.


---

Comment by cremona created at 2009-03-31 09:05:10

Well the good news is that on my 64-bit build (on Bill Hart's computer) I successfully applied all 5 patches to 3.4.1.alpha0, and all tests (in sage/rings/number_field) pass, so I will give this a positive review and hope that it works for Michael too.


---

Comment by mabshoff created at 2009-03-31 09:35:38

Resolution: fixed


---

Comment by mabshoff created at 2009-03-31 09:35:38

Merged 

 * trac_5159_part_1_galois_new.patch
 * trac_5159_part_2_extra.patch
 * trac_5159_part_3-unpickle-fix.patch
 * trac_5159_part_4-64bit-doctest.patch
 * trac_5159_part_5_sort-fix.patch

in Sage 3.4.1.rc0.

Cheers,

Michael
