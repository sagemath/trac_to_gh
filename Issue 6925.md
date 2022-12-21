# Issue 6925: Fast way of calculating cuspidal subgroup of J0(N)

Issue created by migration from Trac.

Original creator: syazdani

Original creation time: 2009-09-11 23:49:01

Assignee: tbd

CC:  pbruin

Keywords: cuspidal subgroup, modular abelian variety

This is the first implementation of Ligozat's method of calculating the rational cuspidal subgroup of J_0(N). This is done by doing linear algebra in d(N)*d(N) matrices, which seems considerably faster than the modular symbol methods.

This code is functional at this point. The problems with it are
a) __cmp__ is not called.
b) Hecke operators aren't defined yet.
c) can't coerce specific degree zero cuspidal divisors in our group.


---

Attachment

This patch touches abvar.py and cuspidal_subgroup.py


---

Attachment

rebased against 5969


---

Comment by AlexGhitza created at 2009-11-15 13:05:35

Changing component from algebra to modular forms.


---

Comment by AlexGhitza created at 2009-11-15 13:06:09

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-02-22 00:05:18

Changing status from needs_review to needs_info.


---

Comment by drkirkby created at 2010-02-22 00:05:18

Has this been checked on Solaris? Or OS X? It's not clear what it has been tested on. 

There's general information about building on Solaris at

 http://wiki.sagemath.org/solaris

Information specifically for 't2' at

 http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2

Both the source (4.3.0.1 is the latest to build on Solaris) and a binary which will run on any SPARC can be found at http://www.sagemath.org/download-source.html

Dave


---

Comment by was created at 2010-03-29 04:33:15

Changing status from needs_info to needs_review.


---

Comment by was created at 2010-05-06 01:59:33

Changing status from needs_review to needs_work.


---

Comment by was created at 2010-05-06 01:59:33

Hi Soroosh,

1. Can you look into the following doctest failures (against sage-4.4.1, say, where your code applies fine)?

```

sage -t  devel/sage/sage/modular/abvar/cuspidal_subgroup.py
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py", line 432:
    sage: C._compute_lambda()
Expected nothing
Got:
    [15/8 -3/8|-5/8  1/8]
    [-3/8 15/8| 1/8 -5/8]
    [---------+---------]
    [-5/8  1/8|15/8 -3/8]
    [ 1/8 -5/8|-3/8 15/8]
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py", line 442:
    sage: C._compute_lambda()
Expected nothing
Got:
    [    1  -1/5     0]
    [ -1/4 13/10  -1/4]
    [    0  -1/5     1]
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py", line 475:
    sage: C._compute_P_d_integral()
Expected nothing
Got:
    Free module of degree 3 and rank 3 over Integer Ring
    Echelon basis matrix:
    [1 0 0]
    [0 4 0]
    [0 0 1]
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py", line 498:
    sage: C._compute_parity_module()
Expected nothing
Got:
    Free module of degree 3 and rank 3 over Integer Ring
    Echelon basis matrix:
    [1 0 0]
    [0 2 0]
    [0 0 1]
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py", line 508:
    sage: C._compute_parity_module()
Expected nothing
Got:
    Free module of degree 4 and rank 4 over Integer Ring
    Echelon basis matrix:
    [1 0 0 0]
    [0 1 1 1]
    [0 0 2 0]
    [0 0 0 2]
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py", line 547:
    sage: C.V0()
Expected nothing
Got:
    Free module of degree 4 and rank 3 over Integer Ring
    Echelon basis matrix:
    [ 1  0  0 -1]
    [ 0  1  0 -1]
    [ 0  0  1 -1]
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py", line 557:
    sage: C.V0()
Expected nothing
Got:
    Free module of degree 3 and rank 2 over Integer Ring
    Echelon basis matrix:
    [ 1  0 -1]
    [ 0  4 -4]
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py", line 590:
    sage: C.Vprincipal()
Expected nothing
Got:
    Free module of degree 3 and rank 2 over Integer Ring
    Echelon basis matrix:
    [ 1  0 -1]
    [ 0  4 -4]
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py", line 599:
    sage: C.Vprincipal()
Expected nothing
Got:
    Free module of degree 4 and rank 3 over Integer Ring
    Echelon basis matrix:
    [ 1  1  3 -5]
    [ 0  2  0 -2]
    [ 0  0  4 -4]
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py", line 654:
    sage: C.gens()
Expected:
    [-P15+P5, -P15+P3]
Got:
    [-P15 + P5, -P15 + P3]
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/sage-4.4.1/devel/sage-main/sage/modular/abvar/cuspidal_subgroup.py", line 703:
    sage: C.0
Expected:
    [-P15 + P5, -P15 + P3]
    sgae: (C.0).additive_order()
    2
Got:
    -P15 + P5
**********************************************************************
7 items had failures:
   2 of   8 in __main__.example_13
   1 of   5 in __main__.example_14
   2 of   8 in __main__.example_15
   2 of   8 in __main__.example_16
   2 of   8 in __main__.example_17
   1 of   5 in __main__.example_19
   1 of   5 in __main__.example_22
***Test Failed*** 11 failures.
For whitespace errors, see the file /scratch/wstein/sage//tmp/.doctest_cuspidal_subgroup.py
         [6.4 s]

```


2. Everwhere that you have

```
Examples::  
    sage:
```

change it to


```
EXAMPLES::  

    sage:
```

(note the newline)

3. Everywhere you have -'d lists, e.g.,

```
        691	        - `` parent`` - a subgroup of the cuspidal subgroup of  
 	692	        J0(N) 
 	693	 
 	694	        - ``element`` - an element in the quotient module of degree zero divisors of cusps 
 	695	        modulo principal divisors. 
 	696	 
 	697	        - ``check`` - bool (default: False) whether to check 
 	698	        that element is in the appropriate module 
```

change them so the second line (etc.) starts exactly two spaces in from the dash so it lines up with the previous line's text, e.g., 

```
        691	        - `` parent`` - a subgroup of the cuspidal subgroup of  
 	692	          J0(N) 
 	693	 
 	694	        - ``element`` - an element in the quotient module of degree zero divisors of cusps 
 	695	          modulo principal divisors. 
 }}}

4. Can you be more careful that the docstrings match what they are documenting, e.g., 
{{{
764	    def _sub_(self, other): 
 	765	        r""" 
 	766	        Adds two elements in the cuspidal subgroup. 
}}}
It should be "Subtract" not add. 

5. 
{{{
        827	    def __cmp__(self, other): 
 	828	        r""" 
 	829	        Checks if two elements are the same. Right now this is not called, and I'm not sure why. 
}}}

You probably need to use/call __richmp__ instead...  there is some funny rule that if you define __cmp__ you have to also define __hash__ or something. Search sage-devel about this. 

7. Change this
{{{
        495	        TESTS: 
 	496	            sage: J=J0(25) 
}}}
to
{{{
        495	        TESTS::
        496
 	497	            sage: J=J0(25) 
}}}

8. I'm not sure about the name "RationalDirectCuspidalSubgroup".  Maybe "RationalCuspidalSubgroupLigozat" or something, i.e., use "Ligozat" instead of direct?


---

Comment by chapoton created at 2013-08-02 07:24:01

for the bot:

apply 6925-rationalcuspidal.patch​


---

Comment by chapoton created at 2013-08-02 07:26:36

apply only 6925-rationalcuspidal.patch


---

Comment by chapoton created at 2013-08-02 08:10:55

here is a first cleanup patch.

There is one failing doctest that needs a mathematical check.


---

Comment by chapoton created at 2013-10-04 08:51:32

Could please someone with the required math knowledge check the unique failing doctest (see patchbot report by clicking on the round icon at the top of the page) ?


---

Comment by chapoton created at 2013-10-04 19:41:12

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2013-10-04 19:41:12

I have replaced the failing test, without checking the mathematical side..

I have also added a reference to Ligozat, hopefully the correct one ?

This should now pass all tests.


---

Comment by chapoton created at 2013-10-05 09:24:33

updated patch, to ensure 100% doctest coverage


---

Comment by syazdani created at 2013-10-07 05:50:09

changed the name to rational_cuspidal_subgroup_ligozat, and few other changes.


---

Attachment

Chapoton's fix was correct. The initial doctest was incorrect.

Also, that is the correct Ligozat reference. I added the reference to my paper as well, which is what the algorithm is based upon.

I changed the name of rational_direct_cuspidal_subgroup to rational_cuspidal_subgroup_ligozat, as it was suggested, and replaced cmp function with eq and ne functions instead.

Finally, sorry for being MIA on this ticket for so long. I think I had an incorrect filter archiving these emails automatically.


---

Comment by chapoton created at 2013-10-13 11:33:24

the addon2 patch does not apply


---

Comment by syazdani created at 2013-10-13 15:29:19

hmm... are the patches supposed to be made from a clean build, or from the previous build? I applied your patches, and then used hg_sage.export. So, three patches need to be applied in order. That might not be the correct approach though.


---

Comment by chapoton created at 2013-10-17 19:43:26

Hello,

it seems that your patch was twice the same thing. Anyway, I have folded it into a new version of trac_6925_addon1.patch

apply 6925-rationalcuspidal.patch trac_6925_addon1.patch


---

Attachment

new patch, minor details changed, should now pass the tests


---

Attachment


---

Comment by chapoton created at 2013-10-25 18:00:54

new patch, folded and rebased on 5.13.beta1

for the *patchbots*

apply trac-6925-rationalcuspidal-rebased-v1.patch


---

Comment by chapoton created at 2013-12-02 21:24:43

New commits:


---

Comment by git created at 2014-01-03 21:03:56

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by pbruin created at 2014-04-26 14:26:39

resolved merge conflicts


---

Comment by pbruin created at 2014-04-26 14:58:14

All tests pass, but I can't look at this in detail now.


---

Comment by rws created at 2014-05-07 09:58:38

patchbot failed with coverage:

```
tests/cmdline.py: 100.0% (1 of 1)
tests/
Traceback (most recent call last):
  File "/home/ralf/sage/local/bin/patchbot/patchbot.py", line 468, in test_a_ti
cket
    res = plugin(ticket, is_git=True, baseline=baseline, **kwds)
  File "/home/ralf/git/sage-patchbot/src/plugins.py", line 152, in doctest_cont
inuation
    exclude_new(ticket, regex=r'^\s*\.\.\.\s', msg="Old-style doctest continuat
ion", **kwds)
  File "/home/ralf/git/sage-patchbot/src/plugins.py", line 143, in exclude_new
    raise ValueError(full_msg)
ValueError: Old-style doctest continuation inserted on 2 non-empty lines
```

but this may be spurious because nothing in `tests/` is changed...


---

Comment by pbruin created at 2014-05-07 16:27:29

Replying to [comment:29 rws]:
> patchbot failed
The failed plugin is `non_ascii`, because of the French accents in the author and journal of Ligozat's article.  We can ignore this, since the file has a `coding: utf-8` declaration in its first line.


---

Comment by rws created at 2014-05-27 06:03:17

Changing status from needs_review to needs_work.


---

Comment by rws created at 2014-05-27 06:03:17


```
+++ b/src/sage/modular/abvar/cuspidal_subgroup.py

`@``@` -371,6 +378,538 `@``@` def is_rational_cusp_gamma0(c, N, data):

+    .. [Ligo] GÃ©rard Ligozat, Courbes modulaires de genre 1.
+       MÃ©moires de la SociÃ©tÃ© MathÃ©matique de France, 43 (1975), p. 5-80,

Non-ascii characters inserted on 2 non-empty linesmultiple lines, _no wiki_
      white space respected
```



---

Comment by chapoton created at 2014-05-27 07:31:12

What do you mean by `needs work` ? Unicode characters are ok as soon as the utf8 encoding is specified at top of the file, which is the case here. Is there anything that really needs to be corrected ???


---

Comment by rws created at 2014-05-27 08:04:19

I usually trust what patchbot is outputting but, as this and the other patchbot bugs show, I should be more careful. Thanks.


---

Comment by rws created at 2014-05-27 08:04:19

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2015-02-16 10:12:00

I have correct the failing repr. Now there are failing doctests.
----
New commits:


---

Comment by chapoton created at 2015-02-16 10:12:00

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2015-04-17 18:17:14

could someone knowledgeable about the subject have a look at the failing doctests ?


---

Comment by git created at 2015-05-14 09:11:35

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2015-07-17 11:52:35

Changing status from needs_work to needs_info.


---

Comment by git created at 2016-01-21 20:35:39

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2016-01-21 20:36:09

**ping** ?


---

Comment by git created at 2016-07-29 18:33:58

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-04-17 08:28:40

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2017-04-17 08:29:30

Changing status from needs_info to needs_review.


---

Comment by vdelecroix created at 2017-07-13 18:06:59

Do `RationalCuspidalSubgroupLigozat` and `RationalCuspSubgroup` provide the same features? Apparently it does

```
sage: X.rational_cuspidal_subgroup_ligozat()
Finite subgroup with invariants (2, 4) over QQ of Abelian variety J0(15) of dimension 1
sage: X.rational_cuspidal_subgroup()
Finite subgroup with invariants [2, 4] over QQ of Abelian variety J0(15) of dimension 1
```

It would be much better to provide an optional argument to `rational_cuspidal_subgroup` rather than having a distinct method. This branch provides (important) implementation details but nothing mathematically relevant. Moreover, inheritance choices should be more clearly explained.

The function names `_compute_XXX` make no sense. Should just be `_XXX`.


---

Comment by vdelecroix created at 2017-07-13 18:06:59

Changing status from needs_review to needs_work.


---

Comment by klui created at 2017-07-20 00:26:41

They don't provide the same features so I think they should stay separate. For instance,

```
sage: J = J0(15)
sage: G = J.rational_cuspidal_subgroup()
sage: H = J.rational_cuspidal_subgroup_ligozat()
sage: G.intersection(J)
Finite subgroup with invariants [2, 4] over QQ of Abelian variety J0(15) of dimension 1
sage: H.intersection(J)
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
<ipython-input-16-7e6428c7da6a> in <module>()
----> 1 H.intersection(J)
 
/projects/c3e0a07c-fea5-4247-a328-e21feb6d7e5d/sage/local/lib/python2.7/site-packages/sage/modular/abvar/finite_subgroup.pyc in intersection(self, other)
    399             K = coercion_model.common_parent(self.field_of_definition(), other.field_of_definition())
    400
--> 401         L = self.lattice()
    402         if A != B:
    403             # TODO: This might be way slower than what we could do if
 
/projects/c3e0a07c-fea5-4247-a328-e21feb6d7e5d/sage/local/lib/python2.7/site-packages/sage/modular/abvar/finite_subgroup.pyc in lattice(self)
    182             [   0    3   -2   -1    2    0]
    183         """
--> 184         raise NotImplementedError
    185
    186     def _relative_basis_matrix(self):
 
NotImplementedError:
```


```
sage: G == G
True
sage: H == H
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
<ipython-input-18-bc37629c2b89> in <module>()
----> 1 H == H
 
/projects/c3e0a07c-fea5-4247-a328-e21feb6d7e5d/sage/local/lib/python2.7/site-packages/sage/modular/abvar/finite_subgroup.pyc in __cmp__(self, other)
    253         L = A.lattice() + B.lattice()
    254         # Minus sign because order gets reversed in passing to lattices.
--> 255         return -cmp(self.lattice() + L, other.lattice() + L)
    256
    257     def is_subgroup(self, other):
 
/projects/c3e0a07c-fea5-4247-a328-e21feb6d7e5d/sage/local/lib/python2.7/site-packages/sage/modular/abvar/finite_subgroup.pyc in lattice(self)
    182             [   0    3   -2   -1    2    0]
    183         """
--> 184         raise NotImplementedError
    185
    186     def _relative_basis_matrix(self):
 
NotImplementedError:
```



---

Comment by vdelecroix created at 2017-07-20 08:37:54

Replying to [comment:49 klui]:
> They don't provide the same features so I think they should stay separate. For instance,

That was not my question. Do they represent the same mathematical object? The fact that some methods are not implemented is a minor difference.


---

Comment by git created at 2017-07-20 16:53:26

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-07-20 16:57:36

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2018-05-01 14:11:38

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2018-06-27 06:10:49

Branch pushed to git repo; I updated commit sha1. New commits:
