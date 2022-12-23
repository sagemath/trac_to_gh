# Issue 8380: Implement an interface to GAP3

Issue created by migration from https://trac.sagemath.org/ticket/8380

Original creator: saliola

Original creation time: 2010-02-26 17:20:39

Assignee: Franco Saliola

CC:  sage-combinat joyner slabbe jmichel@math.jussieu.fr

Keywords: gap3, chevie, specht, gap, sage-combinat

It would be great to have an interface to GAP3 so that one can use GAP3 packages that have not been ported to GAP4. Of particular interest are the packages (sage-devel occasionally receives questions about integrating these packages):

 * CHEVIE: Finite reflection groups and their root systems, braid groups, Iwahori-Hecke algebras, and Kazhdan-Lusztig polynomials. 
 * Specht: Specht: Decomposition matrices for the Hecke algebras of type A.

For a list of other GAP3 packages, check out [http://www.gap-system.org/Gap3/Packages3/packages.html](http://www.gap-system.org/Gap3/Packages3/packages.html).

To be clear, I am not suggesting distributing GAP3 with Sage. This would be just an to GAP3.


---

Comment by saliola created at 2010-02-26 17:35:56

Here are two patches. Make sure you apply the correct patch for you version of Sage.

Of course, you need to have GAP3 installed in order to use GAP3, and all doctests are marked optional.

The interface behaves very much like the GAP4 interface: tab completion works, one can access the GAP3 help documentation, etc.

Notes for the reviewer:

 1. To run the GAP3 doctests:
    {{{
    sage -testall -only-optional=gap3
    }}}

 1. I refactored the GAP4 interface code; basically, I separated the `Gap` class into two new classes `Gap_generic` and `GapElement_generic`.

 1. I've tested that the patches apply cleanly and all doctests pass on the following systems:

   a. sage.math
   a. Ubuntu 9.10, amd 64


---

Comment by saliola created at 2010-02-26 23:41:37

IGNORE THIS PATCH


---

Attachment

This updated patch catches GAP3's syntax error messages.

The interface seems pretty robust now, so its ready for review. Please try it out.


---

Attachment

Patch for Sage version 4.3.2 only.


---

Attachment

Patch for Sage version 4.3.3 only.


---

Attachment

Documentation


---

Comment by saliola created at 2010-03-02 03:10:39

Changing status from new to needs_review.


---

Comment by saliola created at 2010-03-02 03:10:39

If you're a GAP3 user interested in trying the new interface, then you can follow the instructions below to patch your version of Sage. These instructions are just a summary of the procedure described at: [http://www.sagemath.org/doc/developer/walk_through.html#reviewing-a-patch](http://www.sagemath.org/doc/developer/walk_through.html#reviewing-a-patch). (Alternatively, your can just install all the sage-combinat patches using the command `"sage -combinat install"`, which includes the GAP3 interface patch.)

 1. First, create a branch of your Sage library (you can later switch between the main branch and the new gap3 branch with the commands `"sage -b main"` and `"sage -b gap3"`):
   {{{
sage -clone gap3
}}}

 2. Next, start Sage and run one of the following commands, depending on the version of Sage you have installed.

 * For sage-4.3.2:

```
sage: hg_sage.apply("http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8380/gap3_interface_v4.3.2.patch")
```


 * For sage-4.3.3:

```
sage: hg_sage.apply("http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8380/gap3_interface_v4.3.3.patch")
```


 3. Finally, exist Sage and run the following command.

```
sage -br
```


You should be up and running now.

I've also generated the documentation and posted it as a PDF file. You can find it in the "Attachments" section.


---

Comment by saliola created at 2010-03-02 03:23:04

Nicolas Thiery has posted some code on the sage-combinat patch server that uses this interface to construct Coxeter groups using the GAP3 package CHEVIE. Here is a link to his code: [http://combinat.sagemath.org/hgwebdir.cgi/patches/file/e800cdb481fb/trac_8359-coxeter-groups-permutation-nt.patch#l1](http://combinat.sagemath.org/hgwebdir.cgi/patches/file/e800cdb481fb/trac_8359-coxeter-groups-permutation-nt.patch#l1)


---

Comment by slabbe created at 2010-03-02 14:45:40

I tested it on my sage-4.3.3 running mac OS X 10.5.8. I had already the gap3 together with the chevie package. With the patch applied, I obtain All test passed! with the command `sage -t -long`. I also obtain All test passed with the command `sage -testall -only-optional=gap3`. The documentation builds without warning and is very complete.

Before giving a positive review, I would like one person used with interface code to take a look at the patch.

Good work Franco!


---

Comment by nthiery created at 2010-04-02 14:43:36

Hi!

With Jean Michel, I just made an experimental spkg for gap3 + chevie + all other gap3 packages not available on gap4: 

    http://sage.math.washington.edu/home/nthiery/gap3-jm0.spkg

Please test and report! Then we will submit this for submission in experimental/optional


---

Comment by nthiery created at 2010-04-06 21:46:08

Replying to [comment:7 nthiery]:

> Hi! With Jean Michel, I just made an experimental spkg for gap3 + chevie + all other gap3 packages not available on gap4:  Please test and report! Then we will submit this for submission in experimental/optional

Updated package rebased on gap3-jm1 from http://www.math.jussieu.fr/~jmichel/gap3/ :

  http://sage.math.washington.edu/home/nthiery/gap3-jm1.spkg


---

Comment by bascorp created at 2010-04-27 12:55:23

[бесплатно картинки на рабочий](http://rapidshare.in.ua/)


---

Attachment

doctest output


---

Comment by burcin created at 2010-05-04 21:20:04

I tested attachment:gap3_interface_v4.3.3.patch on Sage-4.4.1 with gap3 installed using [Frank Luebeck's distribution](http://www.math.rwth-aachen.de:8001/~Frank.Luebeck/gap/GAP3/index.html). The patch applies cleanly, but there are many doctest failures. This could be due to the fact that optional packages like chevie are not included in this distribution of GAP3.

Here is my review for the patch:
 * There is no doctest for the change in `sage/interfaces/expect.py`
 * The method `load_package()` in `sage/interfaces/gap.py` doesn't have a doctest. I understand that this is copied as is from the old version, but if there is any package that is included by default in the GAP4 distribution (or one which we include in our package), we should add a test.
 * In `sage/interfaces/gap3.py`
  * Is the bug in the pexpect interface mentioned around line 42 reported on trac? Can you mention the ticket number in that comment. Is this specific to the GAP interface?
  * does the GAP3 banner depend on the specific package installed?
  * There are some doctests that depend on chevie, (`RequirePackage('"chevie"')` and `load_package("chevie")`), these should be optional.
  * The docstring for `GAP3Record.__getattr__` ends with " :: " then an empty line. There are many places where there is an empty line at the end of the docstring, or right after.


The optional package for gap3 in comment:9 looks good in general. Maybe the fact that it's binary only can be made more obvious, for example by adding a `bin` to the package name. 

BTW, it's not possible to install the version of GAP3 downloaded from the main web site (http://www.gap-system.org/Gap3/Download3/download.html) easily. I suggest moving the link to Frank Luebeck's distribution to the first place, and putting this option last.


---

Comment by burcin created at 2010-05-04 21:20:04

Changing status from needs_review to needs_work.


---

Comment by saliola created at 2010-05-05 14:59:01

Replying to [comment:11 burcin]:
> I tested attachment:gap3_interface_v4.3.3.patch on Sage-4.4.1 with gap3 installed using [Frank Luebeck's distribution](http://www.math.rwth-aachen.de:8001/~Frank.Luebeck/gap/GAP3/index.html). The patch applies cleanly, but there are many doctest failures. This could be due to the fact that optional packages like chevie are not included in this distribution of GAP3.

I downloaded Frank Luebeck's distribution and compiled it, but it is not working well on my machine:

```
gap>  SymmetricGroup(5);
Gasman: last bag of type +12 and size     16 has overwritten the free bag.
```

As a result, I am getting several doctest errors. I wonder if this is the problem you are having: can you at least check that the above command works on your machine? I'll remark that Luebeck's distribution also includes a binary, and all the doctests but one (the banner) pass if I use that binary.


---

Comment by burcin created at 2010-05-05 15:46:28

Replying to [comment:12 saliola]:
> I downloaded Frank Luebeck's distribution and compiled it, but it is not working well on my machine:
 {{{
 gap>  SymmetricGroup(5);
 Gasman: last bag of type +12 and size     16 has overwritten the free bag.
 }}}

You're right, I get the same error. Sorry for the noise.

Using the binary, I get only one doctest failure:


```
**********************************************************************
File "/home/burcin/sage/sage-4.4.1.alpha2-patched/devel/sage-t/sage/interfaces/gap3.py", line 169:
    sage: gap3.RequirePackage('"chevie"')              #optional - gap3
Expected:
    Welcome  to  the  CHEVIE  package, ...
Got:
    WELCOME  to  the  CHEVIE  package,  Version 3  (Dec  1996)
    <BLANKLINE>
          Meinolf Geck,  Frank Luebeck,   Gerhard Hiss, 
          Gunter Malle,  Jean Michel, and Goetz Pfeiffer,
              Lehrstuhl D fuer Mathematik, RWTH Aachen,
              IWR der Universitaet Heidelberg,
              University of St. Andrews and
              Universite Paris VII
    <BLANKLINE>
       This replaces the former weyl package. For first help type
    <BLANKLINE>
              ?CHEVIE Version 3 -- a short introduction
**********************************************************************
```



---

Comment by mrobado created at 2010-05-06 14:10:23

I managed to make an spkg that compiles on 64bits machines. See ticket #8906


---

Comment by saliola created at 2010-05-12 03:07:10

first apply gap3_interface_v4.3.3.patch, then this


---

Comment by saliola created at 2010-05-12 03:12:54

Changing status from needs_work to needs_review.


---

Attachment

I've uploaded my changes in a separate patch to ease the review. Apply the patches in this order:

 * attachment:gap3_interface_v4.3.3.patch
 * attachment:gap3_interface_patch2.patch


Replying to [comment:11 burcin]:

> Here is my review for the patch:
>  * There is no doctest for the change in `sage/interfaces/expect.py`

The problem here was that a variable name could be overwritten; before the
patch:

```
sage: x = gap(3)
sage: gap.clear(x.name())
sage: gap.clear(x.name())
sage: x = gap(3); x
3
sage: y = gap(4); y
4
sage: x # this should be 3!
4
```

This is now corrected, and I added the above as a doctest.

>  * The method `load_package()` in `sage/interfaces/gap.py` doesn't have a doctest. I understand that this is copied as is from the old version, but if there is any package that is included by default in the GAP4 distribution (or one which we include in our package), we should add a test.

Neither Sage nor Gap seem to distribute any packages (see the
`$SAGE_ROOT/local/lib/gap-4.4.12/pkg` directory). I did, however,
add a test that at least tests that it raises an appropriate exception.

>  * In `sage/interfaces/gap3.py`
>   * Is the bug in the pexpect interface mentioned around line 42 reported on trac? Can you mention the ticket number in that comment. Is this specific to the GAP interface?

Yes, it is #8471. I added the ticket number to the comment, and
cross-referenced that ticket to this one.

It is not specific to the GAP interface. It is an issue with any
`Expect` instance. See #8471 for details.

>   * does the GAP3 banner depend on the specific package installed?

It shouldn't since the software is so old. Note that when the banners are
printed in the documentation, it is only for illustration purposes. Those
commands are not tested because each spawns a console (which would require
user input to quit).

>   * There are some doctests that depend on chevie, (`RequirePackage('"chevie"')` and `load_package("chevie")`), these should be optional.

I've marked them as `#optional - gap3chevie` instead of just
`#optional - gap3`.

>   * The docstring for `GAP3Record.__getattr__` ends with " :: " then an empty line. There are many places where there is an empty line at the end of the docstring, or right after.

Corrected.

> The optional package for gap3 in comment:9 looks good in general. Maybe the fact that it's binary only can be made more obvious, for example by adding a `bin` to the package name. 

The discussion surrounding spkgs should be moved to #8906, which proposes
a source gap3 spkg instead.

> BTW, it's not possible to install the version of GAP3 downloaded from the main web site (http://www.gap-system.org/Gap3/Download3/download.html) easily. I suggest moving the link to Frank Luebeck's distribution to the first place, and putting this option last.

Done. I listed ticket #8906 as the first option (it should be changed when
that ticket is resolved).


---

Comment by saliola created at 2010-05-12 03:15:15

Replying to [comment:15 saliola]:
> 
> I've uploaded my changes in a separate patch to ease the review. Apply the patches in this order:
> 
>  * attachment:gap3_interface_v4.3.3.patch
>  * attachment:gap3_interface_patch2.patch

Ignore that the patch name says 4.3.3; it should apply cleanly against recent versions of Sage.


---

Attachment

Franco's patch2 with a minor change


---

Comment by burcin created at 2010-05-22 09:09:45

It seems the doctest framework doesn't like starting output lines with an ellipsis. The test for ` gap3.RequirePackage('"chevie"')` was failing for me saying that it didn't expect any output, so I changed the output to add `W` as the first character. attachment:trac_8380-gap3_interface_patch2.take2.patch is the same as Franco's second patch apart from this minor change.

I'm changing this to positive review.

Patches to be applied:
 * attachment:gap3_interface_v4.3.3.patch
 * attachment:trac_8380-gap3_interface_patch2.take2.patch


---

Comment by burcin created at 2010-05-22 09:09:45

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-05 22:48:15

Changing status from positive_review to needs_work.


---

Comment by mhansen created at 2010-06-05 22:48:15

I get the following failure


```

sage -t  "devel/sage/sage/interfaces/expect.py"
**********************************************************************
File "/virtual/scratch/mhansen/release/4.4.4/alpha0/sage-4.4.4.alpha0/devel/sage/sage/interfaces/expect.py", line 1213:
    sage: x
Expected:
    3
Got:
    4
**********************************************************************
```



---

Comment by saliola created at 2010-06-07 18:26:00

Replying to [comment:18 mhansen]:
> I get the following failure

Very bizarre; this passes in a sage session (but it fails while doctesting):

```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: x = gap(3); x
3
sage: gap.clear(x.name())
sage: gap.clear(x.name())
sage: x = gap(3); x
3
sage: y = gap(4); y
4
sage: x
3
sage: 
```



---

Attachment


---

Comment by saliola created at 2010-06-08 03:25:31

Changing status from needs_work to needs_review.


---

Comment by saliola created at 2010-06-08 03:25:31

The bit of code in `expect.py` I changed was meant to fix what I thought was a small bug. Unfortunately, it seems this bug runs deeper than I originally thought (I still haven't completely tracked down the problem), so instead I created a new ticket to track this particular issue: #9183. (Fixing this bug is independent of the gap3 interface code.)

I have attached another patch that reverts the changes to `expect.py`.

Patches to be applied:

    * attachment:gap3_interface_v4.3.3.patch
    * attachment:trac_8380-gap3_interface_patch2.take2.patch
    * attachment:trac_8380-revert_changes_to_expect.patch


---

Comment by saliola created at 2010-06-08 03:28:49

The first two patches above have already been positively reviewed, so just the last patch above needs to be dealt with.


---

Comment by burcin created at 2010-06-08 08:12:58

Changing status from needs_review to positive_review.


---

Comment by burcin created at 2010-06-08 08:12:58

I agree that the expect bug shouldn't hold this patch back. I'm changing this to a positive review.

It would be great if this can be merged for the next release. AFAIK, the upcoming combinat meeting will have some CHEVIE developers.


---

Comment by mhansen created at 2010-06-09 02:23:31

Resolution: fixed
