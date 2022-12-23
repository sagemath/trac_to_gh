# Issue 7886: [with patch, needs work] Implement conjugacy classes

Issue created by migration from https://trac.sagemath.org/ticket/7886

Original creator: jlopez

Original creation time: 2010-01-09 21:49:27

Assignee: joyner

CC:  wdj jdemeyer jlopez

GAP has several functions concerning conjugacy classes of groups. It would be nice to have a way to access such functions from Sage.


---

Comment by jlopez created at 2010-01-09 21:50:35

Implementation of a python class for conjugacy classes, wrapping some GAP functions and some native python methods.


---

Attachment

Conjugacy classes code


---

Comment by jlopez created at 2011-12-06 18:04:05

Changing status from new to needs_review.


---

Comment by jlopez created at 2011-12-06 18:04:05

Patch submitted. All tests pass on my machine (OX-X 10.6.8) with the exception of the ConjugacyClass Testsuite, which fails testing equality. I have no idea how the testsuite works, so could use some help here.


---

Comment by jlopez created at 2011-12-06 18:05:48

For the patchbot:

Apply trac_7886_conjugacy_classes.patch


---

Comment by jlopez created at 2011-12-06 18:56:17

Oops! Forgot to add the new module to the patch, here it is!


---

Comment by jlopez created at 2011-12-06 18:56:55

Apply trac_7886_conjugacy_classes_module.patch, trac_7886_conjugacy_classes.patch


---

Comment by jlopez created at 2011-12-07 16:45:21

conjugacy_classes.py module with passing Testsuite


---

Attachment

Updated the conjugacy_classes.py module with the fixed _cmp_ method so that the testsuite passes. All test pass on my machine, so ready for review.


---

Comment by wdj created at 2011-12-09 14:37:05

The code looks fine to me. I tested it on a 10.6.8 mac under sage-4.8.a3 and on a Ubuntu 10.04 (Lucid Lynx) machine under sage-4.8.a1.

There was a discussion of cached methods in sage-devel, but I'm not sure how that relates to this ticket, so I'm giving this a positive review. Maybe changes, if any, from that thread can go in a separate ticket.


---

Comment by wdj created at 2011-12-09 14:37:05

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-12-11 10:31:06

In the file `sage/groups/perm_gps/permgroup.py`, you use Unicode but the encoding has not been declared to be utf-8.

See [http://www.python.org/dev/peps/pep-0263/](http://www.python.org/dev/peps/pep-0263/)


---

Comment by jdemeyer created at 2011-12-11 10:31:06

Changing status from positive_review to needs_work.


---

Comment by jlopez created at 2011-12-12 11:48:09

Fixed encoding and improvement of naive set method.


---

Comment by jlopez created at 2011-12-12 11:51:23

Changing status from needs_work to needs_review.


---

Attachment

Sorry, I thought we were using utf-8 by default. Fixed the encoding in permgroup.py and conjugacy_classes.py
Also implemented a more efficient fallback method using TransitiveIdeal.
Needs review.


---

Comment by jlopez created at 2011-12-12 12:00:01

For the patchbot:
Apply trac_7886_conjugacy_classes_module.patch, trac_7886_conjugacy_classes.patch, trac_7886_conjugacy_classes_encoding_fix.patch


---

Comment by jlopez created at 2012-02-08 09:01:34

Just a little bump. Jeroen, can you please check that the UTF encoding is working properly now? David Joyner already reviewed the math-related part of the ticket.


---

Comment by tkluck created at 2013-01-03 20:00:17

Changing status from needs_review to needs_work.


---

Comment by tkluck created at 2013-01-03 20:00:17

This has been lingering on trac for a while; thought I could review it. I tried to apply these patches to 5.5 in the given order.

The second one gives

```
applying http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7886/trac_7886_conjugacy_classes.patch
patching file sage/groups/perm_gps/permgroup.py
Hunk #1 succeeded at 95 with fuzz 2 (offset 3 lines).
Hunk #2 FAILED at 132
1 out of 3 hunks FAILED -- saving rejects to file sage/groups/perm_gps/permgroup.py.rej
abort: patch failed to apply
```


Is it possible to rebase them? I'll set this ticket to 'needs work' in the mean time.


---

Comment by jlopez created at 2013-01-31 19:53:28

I will give it a go during the weekend. Thanks for volunteering for reviewing!


---

Comment by jlopez created at 2013-02-04 19:19:59

Tests pass on my Mac Os X 10.6.8, ready for review. Apply the combined patch only.


---

Comment by jlopez created at 2013-02-04 19:19:59

Changing status from needs_work to needs_review.


---

Comment by jlopez created at 2013-02-04 19:20:37

patchbot: apply trac_7886_conjugacy_classes_combined.patch


---

Comment by tscrim created at 2013-02-19 20:06:30

Hey,

Thank you for working on this. However there are multiple docstring issues you will need to address. More specifically, you will need to change (for example)

```
EXAMPLES:
    sage: H = MatrixGroup([matrix(GF(5),2,[1,2, -1, 1]), matrix(GF(5),2, [1,1, 0,1])])
    sage: h = H(matrix(GF(5),2,[1,2, -1, 1]))
    sage: H.conjugacy_class(h)
    ...

#####

TODO:
    - Implement a non-naive fallback method for computing all the elements of
    the conjugacy class when the group is not defined in GAP, as the one in
    Butler's paper.
    - Define a sage method for gap matrices so that groups of matrices can
    use the quicker GAP algorithm rather than the naive one.

EXAMPLES::

- Conjugacy classes for groups of permutations 

    sage: G = SymmetricGroup(4) 
    ...
```

to

```
EXAMPLES::

    sage: H = MatrixGroup([matrix(GF(5),2,[1,2, -1, 1]), matrix(GF(5),2, [1,1, 0,1])])
    sage: h = H(matrix(GF(5),2,[1,2, -1, 1]))
    sage: H.conjugacy_class(h)
    ...

####


.. TODO::

    - Implement a non-naive fallback method for computing all the elements of
      the conjugacy class when the group is not defined in GAP, as the one in
      Butler's paper.
    - Define a sage method for gap matrices so that groups of matrices can
      use the quicker GAP algorithm rather than the naive one.

EXAMPLES:

Conjugacy classes for groups of permutations::

    sage: G = SymmetricGroup(4) 
    ...
```

otherwise the formatting will be incorrect (the convention is not to use bullet points for different examples). For a full description, see [the conventions page](http://www.sagemath.org/doc/developer/conventions.html:).

Also you will need to cleanup the patch's header message.

Thanks,

Travis


---

Comment by knsam created at 2013-02-20 16:12:41

Changing status from needs_review to needs_work.


---

Comment by knsam created at 2013-02-20 16:12:41

This patch needs to address referee's comments. I am changing this to `needs_work` in the meanwhile.


---

Comment by jlopez created at 2013-02-20 21:59:00

Thanks for looking at my patch! I have a complicated work situation during the week, but will fix the docstring style and rebase again over sage 5.7 on Friday or Saturday.

Not sure what you mean about the patch header message. Do you mean the Spanish characters in my name? That is automatically added by my hg configuration, but it seems that trac does not support UTF-8; I added the appropriate encoding to the python files, but don't know how to do it for the patch (and don't feel inclined to change my name either). If it is about the cruft that came from patch folding, I will take care of that as well.

Cheers,
J


---

Comment by tscrim created at 2013-02-21 15:42:14

Hey Javier,

Replying to [comment:20 jlopez]:
> Thanks for looking at my patch! I have a complicated work situation during the week, but will fix the docstring style and rebase again over sage 5.7 on Friday or Saturday.

Thank you! There's not a huge rush, just ping back when it's done and I'll give it a look-over.

> Not sure what you mean about the patch header message. Do you mean the Spanish characters in my name? That is automatically added by my hg configuration, but it seems that trac does not support UTF-8; I added the appropriate encoding to the python files, but don't know how to do it for the patch (and don't feel inclined to change my name either). If it is about the cruft that came from patch folding, I will take care of that as well.

If you look at the beginning of the patch, you have the following:

```
# HG changeset patch
# User Javier LÃ³pez PeÃ±a <vengoroso@gmail.com>
# Date 1360004753 0
# Node ID 2782ba59f14a8dafdb44e05a67972e5a9d4db0cf
# Parent  fa8decac55338225dc33568ad600c261fc777b4c
* * *
Trac 7886: Conjugacy classes
* * *
Trac 7886: Created module for conjugacy classes of finite groups.
Added wrappers for GAP functions and naive fallback method.
* * *
Trac 7886: Conjugacy classes
```

In particular, the line right after the `# Parent ...` should be a one line summary of the patch with the ticket number (such as `Trac 7886: Conjugacy classes` which is probably what you originally had). This can get mangled when folding patches. You can change this by doing a `qrefresh -e`. I don't think the encoding for your name in the header is important.

Gracias por tu trabajo,

Travis


---

Comment by jlopez created at 2013-02-22 14:24:36

I think I fixed all the docstring formatting. Also removed some trailing whitespaces and rebased over sage 5.7. Needs review.

Patchbot apply trac_7886_conjugacy_classes_combined.patch


---

Comment by jlopez created at 2013-02-22 14:24:36

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2013-02-22 14:47:24

Hey Javier,

There are still many misformatted docstrings (did you forget to refresh the patch?) and the examples are still itemized. Also remove the `* * *` from the header. In case you are unaware, you can run `sage -docbuild reference html` (or reference/groups and/or reference/categories with #6495) to view the documentation.

Thanks,

Travis


---

Comment by jlopez created at 2013-02-22 15:28:17

Hi Travis,

refreshed, fixed the itemized examples. My docbuild refuses to work due to the presence of UTF8 characters in the docstring:

```
    reading sources... [ 75%] sage/groups/perm_gps/permgroup                        
    Sphinx error:
    'ascii' codec can't decode byte 0xc3 in position 3438: ordinal not in range(128)
```


Is there any way to tell sphinx to use the utf8 codec instead? I already included the 

```
# coding = utf-8
```

in the python file, but the docbuild seems to ignore that.


---

Comment by jlopez created at 2013-02-22 16:05:02

Docstring and whitespaces fixes, rebased for sage 5.7. Apply this patch only.


---

Attachment


---

Attachment

Hey Javier,

I've attaching a review patch which fixes up the remaining documentation and adds the files to the docbuild (I had to do some extra tweaks in the `categories/finite_groups.py` since it wasn't in the docbuild prior to this patch). If everything works and looks good to you, you go ahead and set this to positive review.

Thanks,

Travis

For patchbot:

Apply: trac_7886_conjugacy_classes_combined.patch, trac_7886-conjugacy_classes-review-ts.patch


---

Comment by jlopez created at 2013-02-23 12:26:26

Hi Travis,

your reviewer patch fails to apply for me:


```
applying trac_7886-conjugacy_classes-review-ts.patch
unable to find 'doc/en/reference/categories/index.rst' for patching
1 out of 1 hunks FAILED -- saving rejects to file doc/en/reference/categories/index.rst.rej
unable to find 'doc/en/reference/groups/index.rst' for patching
1 out of 1 hunks FAILED -- saving rejects to file doc/en/reference/groups/index.rst.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_7886-conjugacy_classes-review-ts.patch
```


Are we working over the same version of sage (I'm on 5.7), or did you apply any previous patches that changed documentation files?


---

Comment by tscrim created at 2013-02-23 13:58:29

Hey Javier,

Actually I have #6495 applied, it might be because of that. I've added it as a dependency. Try applying the patches with #6495.

Thanks,

Travis


---

Comment by jlopez created at 2013-02-23 18:02:57

Alright. WIth #6495 applied the reviewer patch applies and docs build properly. Tests pass, so I think this is good to go.
Thanks for your help with the reviewing and the docstring formatting!


---

Comment by jlopez created at 2013-02-23 18:02:57

Changing status from needs_review to positive_review.


---

Comment by jlopez created at 2013-02-23 18:04:36

Patchbot seems confused about what needs to be applied, so here it goes again:

Apply trac_7886_conjugacy_classes_combined.patch trac_7886-conjugacy_classes-review-ts.patch


---

Comment by jdemeyer created at 2013-02-28 10:32:12

Resolution: fixed


---

Comment by vbraun created at 2013-02-28 20:55:36

You shouldn't return lists from `@`cached_method functions. If somebody mutates the output list then future calls return the wrong result! Always return tuples instead of lists unless you want the output to be mutable.

Also, `ConjugacyClass` is a parent without elements; Use `SageObject` as base for classes that do not use the parent/element pattern.
