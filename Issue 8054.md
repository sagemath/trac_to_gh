# Issue 8054: roots(algorithm='numpy') does not work in arbitrary precision

Issue created by migration from https://trac.sagemath.org/ticket/8054

Original creator: zimmerma

Original creation time: 2010-01-25 12:08:01

Assignee: jkantor

CC:  rbeezer

Consider the following example:

```
sage: R.<x> = PolynomialRing(ComplexField(3322))
sage: p=x^4+54*x^2+154
sage: z=p.roots(algorithm='pari')
sage: e=p-mul([x-z[i][0] for i in range(4)])
sage: n(max(abs(e.coeffs()[i]) for i in range(0,e.degree()+1)))
6.08883742371831e-999
```

This is ok. Compare now with:

```
sage: R.<x> = PolynomialRing(ComplexField(3322))
sage: p=x^4+54*x^2+154
sage: z=p.roots(algorithm='numpy')
sage: e=p-mul([x-z[i][0] for i in range(4)])
sage: n(max(abs(e.coeffs()[i]) for i in range(0,e.degree()+1)))
6.06533797844328e-14
```

Clearly the precision given by numpy is only 14 digits, not 1000
digits as expected.


---

Comment by jason created at 2010-01-25 13:28:59

Numpy does not do arbitrary precision things.  So I suppose we should just document this.


---

Comment by zimmerma created at 2010-02-05 20:25:33

> Numpy does not do arbitrary precision things. So I suppose we should just document this. 

still not done in 4.3.1.


---

Comment by mhansen created at 2010-08-26 19:02:59

Changing status from new to needs_review.


---

Attachment


---

Comment by zimmerma created at 2010-08-30 13:56:28

Mike, the warning message is just printed once, i.e., if one calls roots(algorithm='numpy') twice,
it is not printed the second time. Is it wanted?

Paul


---

Comment by zimmerma created at 2010-08-30 14:19:55

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2010-08-30 14:19:55

All test pass (with Sage 4.4.4). Thus I give a positive review.


---

Comment by mpatel created at 2010-09-18 07:49:10

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-09-18 07:49:10

Could someone rebase the patch against 4.6.alpha1 when it's released (soon) and restore the positive review?


---

Comment by jason created at 2010-09-18 12:34:46

If someone is rebasing it, they might also correct a typo:

Note that one should not use NumPy when wanting high precicion -> precision


---

Comment by zimmerma created at 2010-09-18 19:59:26

by the way, is there a documentation somewhere explaining how to rebase a patch?

Paul


---

Comment by mpatel created at 2010-09-18 22:11:53

Replying to [comment:8 zimmerma]:
> by the way, is there a documentation somewhere explaining how to rebase a patch?

One way is to use [Mercurial queues](http://wiki.sagemath.org/MercurialQueues):

```sh
$ cd SAGE_ROOT/devel/sage
$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8054/trac_8054.patch
adding trac_8054.patch to series file
$ hg qpush
applying trac_8054.patch
patching file sage/rings/polynomial/polynomial_element.pyx
Hunk #2 FAILED at 4256
1 out of 4 hunks FAILED -- saving rejects to file sage/rings/polynomial/polynomial_element.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8054.patch
```

The file `polynomial_element.pyx.rej` is a diff of the changes that Mercurial was unable to apply.  Editing `polynomial_element.pyx` by hand to incorporate the leftover changes and then doing

```sh
$ hg qrefresh
$ hg export qtip > /path/to/trac_8054.2.patch
$ hg qpop
$ hg qdelete trac_8054.patch
```

should write out an updated patch and restore the original state of the repository.  If you choose not to delete the patch from the queue, e.g., for doctesting, then for convenience you can use

```sh
$ hg qrename trac_8054.2.patch
```

to rename it in the queue.  After this, `hg qseries`, `hg qapplied`, and `hg qunapplied` will use the updated name (until you `qdelete` the patch).

There's more on using queues in the [Developer's Guide](http://www.sagemath.org/doc/developer/walk_through.html#being-more-efficient-mercurial-queues), but as far as I can tell, there's no mention of rebasing patches.  Let us know if you have questions.


---

Comment by zimmerma created at 2010-09-19 08:17:05

Replying to [comment:9 mpatel]:

thank you. I will try when 4.6.alpha1 is available. Do you know when?

Paul


---

Comment by mpatel created at 2010-09-19 08:25:40

Replying to [comment:10 zimmerma]:
> Replying to [comment:9 mpatel]:
> thank you. I will try when 4.6.alpha1 is available. Do you know when?

No problem.  I hope I haven't made any mistakes!

I very recently [announced 4.6.alpha1 on sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/1a01378099b9d5e).

I've cc'd Rob Beezer about [comment:8 rebasing patches].


---

Attachment

original patch rebased on 4.6.alpha1


---

Comment by zimmerma created at 2010-09-19 18:58:01

Changing status from needs_work to positive_review.


---

Comment by zimmerma created at 2010-09-19 18:58:01

Replying to [comment:6 mpatel]:
> Could someone rebase the patch against 4.6.alpha1 when it's released (soon) and restore the positive review? 

done.

Paul


---

Comment by rbeezer created at 2010-09-19 19:32:51

I'll try to send Paul some rebase instructions that he might look over and then and maybe grow those into something for the Developer's Guide.

Rob


---

Comment by mpatel created at 2010-09-19 21:24:43

The rebased patch applies cleanly to 4.6.alpha1.  But testing just the changed file, I get

```
sage -t -long "devel/sage-main/sage/rings/polynomial/polynomial_element.pyx"
**********************************************************************
Error: TAB character found.

         [13.2 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage-main/sage/rings/polynomial/polynomial_element.pyx"
Total time for all tests: 13.2 seconds
```

There's a stray tab in this line

```diff
+       ``algorithm='numpy'`` with high-precision types.)                       
```

(in the patch).


---

Comment by mpatel created at 2010-09-19 21:27:15

Replying to [comment:13 rbeezer]:
> I'll try to send Paul some rebase instructions that he might look over and then and maybe grow those into something for the Developer's Guide.

Thanks, Rob.  I wasn't sure whether this is in the Guide.  I should reread it in full, soon.


---

Attachment


---

Comment by zimmerma created at 2010-09-20 07:50:48

sorry, I've replaced the tab. Apply only the last patch.

Paul


---

Comment by mpatel created at 2010-09-28 09:11:15

Resolution: fixed


---

Comment by mpatel created at 2010-10-04 22:00:16

Replying to [comment:9 mpatel]:
> Replying to [comment:8 zimmerma]:
> > by the way, is there a documentation somewhere explaining how to rebase a patch?
> 
> One way is to use [Mercurial queues](http://wiki.sagemath.org/MercurialQueues):

Another possible way:

```sh
$ hg import --no-commit filename.patch
```

which just updates the working directory.  Then you can check the .rej file, make changes, re-commit, and export anew.
