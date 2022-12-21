# Issue 8828: Lower height bound for elliptic curves

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-04-30 06:44:34

Assignee: cremona

CC:  pbruin

Implements Cremona and and Samir Siksek's algorithm for computing lower bounds on canonical heights, with Nook's extensions to number fields. 


---

Attachment


---

Comment by robertwb created at 2010-04-30 06:47:33

It works fine, but is still missing documentation and doctests.


---

Comment by robertwb created at 2010-04-30 06:47:33

Changing status from new to needs_work.


---

Comment by robertwb created at 2010-04-30 06:51:51

Depends on #8535 and #8818 at least.


---

Comment by cremona created at 2014-01-02 12:17:07

I am about to convert this patch to a new git branch based on the 6.1 develop branch, in an attempt to revive the code and get it finished.  Note that this is a prerequisite for the related #8829.


---

Comment by cremona created at 2014-01-02 13:22:59

New commits:


---

Comment by cremona created at 2014-01-02 13:26:54

Here is a commit which make essentially the same changes as the patch.  I omitted some low-level stuff which seems to have been included anyway in the intervening 4 years.  I changed the QQ.residue_field() function to be even more like the number field version.


---

Comment by git created at 2014-01-03 11:45:19

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by cremona created at 2014-01-03 11:49:40

The two commits up to 307891b implement the original patch with one small additional rebasing edit.  This now passes all tests, but that is not saying a lot since there are very few doctests in the new code.

My next job: add docstrings and doctests.


---

Comment by robertwb created at 2014-03-02 10:08:28

I started adding doctests. 
----
New commits:


---

Comment by cremona created at 2014-03-02 20:06:40

Robert, I spent some time on this a mnth or two ago (how do you find out when a branch was last modified?) and I'm sure some of what I did will be useful -- certain, in fact, since at least one doctest revealed a bug.

What is the best way of sharing my branch with you?  There are 2 or 3 commits on top of 6.1.beta2.


---

Comment by robertwb created at 2014-03-06 22:02:05

I merged your branch into mine, so you should be able to merge that in easily with whatever future work you do.


---

Comment by cremona created at 2014-03-06 22:26:24

Replying to [comment:16 robertwb]:
> I merged your branch into mine, so you should be able to merge that in easily with whatever future work you do.

Git is not clever enough for you to lift by last commit off my own computer though.   I had one more commit with a lot of stuff.  I made a patch from it and put it in boxen:/home/cremona/8828.patch, and it might be worth looking at.


---

Comment by robertwb created at 2014-03-06 22:42:38

Fair point :). You should be able to do 


```
./sage --dev pull --ticket 8828
./sage --dev push --ticket 8828
```


to pull these changes in and then push your changes out. This might involve a merge, but it shouldn't conflict. Alternatively, you could publish your repo somewhere (e.g. on github or even boxen) and I could merge it in.


---

Comment by cremona created at 2014-03-07 09:50:59

Replying to [comment:18 robertwb]:
> Fair point :). You should be able to do 
> 
> {{{
> ./sage --dev pull --ticket 8828
> ./sage --dev push --ticket 8828
> }}}
> 
> to pull these changes in and then push your changes out. This might involve a merge, but it shouldn't conflict. Alternatively, you could publish your repo somewhere (e.g. on github or even boxen) and I could merge it in. 

OK, but I don't have time to do that right now as I'm leaving for a conference tomorrow and have a lot to do before that...


---

Comment by cremona created at 2014-03-07 14:52:42

New commits:


---

Comment by cremona created at 2014-03-07 14:54:33

The automatic merge worked fine: the two new commits are my work + the merge commit.  This gives us a new basis for further work (adding doctests etc): I will not touch this again for 10 days or so at least!


---

Comment by pbruin created at 2014-03-27 17:05:52

This branch looks suspicious: according to the "diffstat" that appears when clicking on the branch name, it deletes three entire files (`rings/number_field/morphism.pyx`, `rings/rational_field.py`, `schemes/elliptic_curves/ell_local_data.py`).  Is this a Git (merge) accident?


---

Comment by cremona created at 2014-03-27 17:18:32

Replying to [comment:22 pbruin]:
> This branch looks suspicious: according to the "diffstat" that appears when clicking on the branch name, it deletes three entire files (`rings/number_field/morphism.pyx`, `rings/rational_field.py`, `schemes/elliptic_curves/ell_local_data.py`).  Is this a Git (merge) accident?

That is not what I see when I click on the brnaches, either the merge I did (756d0ee) or the "work in progress" commit b2bc066.


---

Comment by pbruin created at 2014-03-27 17:28:10

It only occurs when you look at the whole branch, i.e. when you click on `u/cremona/ticket/8828` in the "Branch:" field.  I now tried to fetch the branch with `git fetch trac u/cremona/ticket/8828` and the output of `git diff develop...FETCH_HEAD` does not show anything like this, just normal changes.  Also merging with `develop` seems to work fine.  So it actually looks like a glitch in Trac's git plugin.


---

Comment by cremona created at 2014-03-27 20:03:07

Replying to [comment:24 pbruin]:
> It only occurs when you look at the whole branch, i.e. when you click on `u/cremona/ticket/8828` in the "Branch:" field.  I now tried to fetch the branch with `git fetch trac u/cremona/ticket/8828` and the output of `git diff develop...FETCH_HEAD` does not show anything like this, just normal changes.  Also merging with `develop` seems to work fine.  So it actually looks like a glitch in Trac's git plugin.

That is a relief -- though I still have that branch on my own computer and presumably if and when I check it out again I will see a file with the changes I made.


---

Comment by git created at 2014-03-31 16:14:24

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by cremona created at 2014-03-31 16:16:03

The previous commit is simply merging the current develop branch (at commit 9db8c5c, tag 6.2.beta5) into my branch, which I now intend to resume work on.


---

Comment by git created at 2014-04-03 12:28:58

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by cremona created at 2014-04-03 12:42:44

I have finished workin on height.py,  adding a large amount of documentation and examples.  There were some bugs revealed by this, which have been fixed.  One was in the function `non_neg_region` and was a simple slip, I forget the details.  The second was due to wrong normalisation of period lattice basis (for real embeddings):  L.basis() gives w1, w2 with w1 real, while L.normalised_basis() gives w1,w2 with w2 minimal and tau=w1/w2 in the fundamental region.  To avoid this catching people out in future I added a method tau() to the period lattice class.  The effect here is that in some of the tests the error is now better than it was;  but also the test results (for fk and wp) are different since they work with respect to the normalised lattice [1,tau] and so are different when the correct value of tau is used!

I added more examples from the papers cited, and also give more specific references to those papers throughout, especially the paper [TT] by Nook (Thotsaphon Thonjungthug);  the theory here was developed by himself with me and Samir Siksek while Nook was our PhD student.

It seems to be four years since Robert Bradshaw implemented this (Nook himself implemented it too, in Magma) so it seem rather unreasonable to ask him to look at it again.  Peter Bruin would be a good person, since his own recent paper improves Nook's results (and makes some of this redundant perhaps?)

I will set this to "needs review" as soon as I have added a couple of missing doctests in the file `period_lattice_region.pyx` to bring the two files up to 100%.


---

Comment by git created at 2014-04-03 13:06:08

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by cremona created at 2014-04-03 13:06:47

Done!  Please review...


---

Comment by cremona created at 2014-04-03 13:06:47

Changing status from needs_work to needs_review.


---

Comment by pbruin created at 2014-04-04 21:41:16

I'm now reading the code and documentation.  Apart from a number of small spelling/typographical things (for which I'll just make a reviewer patch), there are a few functions of which the documentation is missing:
- `EllipticCurve_number_field.height_function()`
- the functions `frame_data()` and `unframe_data()` in `period_lattice_region.pyx`
By the way, I don't think my paper of last year makes any of this redundant.  My method is almost certainly slower (I don't know by how much; it is only implemented as a PARI script and I did not make a lot of effort to make it fast, but I doubt it can beat the algorithms in this patch).  Which method is most suitable probably depends a lot on the curve.


---

Comment by pbruin created at 2014-04-06 15:30:09

I just found out about #13125, which implements a `RealSet` class representing finite unions of real intervals and points.  Would it make sense to use this (and extend it where necessary) instead of the `UnionOfIntervals` introduced in this ticket?


---

Comment by cremona created at 2014-04-06 16:10:57

Maybe in future, but it would delay this (and the dependent tickets such as #8289), and the code here is tested.  I would say we should put in a reference to a new ticket to consider doing that in future.  But this is partly laziness, and not being familiar with the code at #13125.


---

Comment by pbruin created at 2014-04-06 18:32:33

Replying to [comment:34 cremona]:
> Maybe in future, but it would delay this (and the dependent tickets such as #8289), and the code here is tested.  I would say we should put in a reference to a new ticket to consider doing that in future.
OK, this is now #16063.


---

Comment by pbruin created at 2014-04-08 10:02:10

A question about the new method `RationalField.places()`: is there a reason why the `prec` argument is handled differently than in `NumberField_absolute.places()`?  Here is a table of which fields are used for the embedding depending on `prec`:

```
prec      RationalField    NumberField
------------------------------------------
None      RR/CC            RIF/CIF
Infinity  not accepted     AA/QQbar
53        RDF/CDF          RDF/CDF
other     RealField(prec)  RealField(prec)
```



---

Comment by cremona created at 2014-04-08 21:26:41

No reason.  If you are making some reviewer changes, please could you make this consistent?  Thanks.


---

Comment by pbruin created at 2014-04-09 11:53:26

Could you please check if you agree with the changes in the new branch (which is based on yours)?  Here is a summary of the changes:

- The first commit ("reviewer patch") consists mostly of formatting changes, spelling fixes and Python style issues.  It also adds the new files to the reference manual.  Because of this I had to change one of the references [TT] to [T].  I also changed [Cremona2010] to [CT] to be more consistent.

- The documentation of the existing method `NumberField_absolute.places()` is wrong; in fact it never returns an embedding into `RIF` or `CIF`, it just uses these to determine the required precision if `prec=None`.  I have not changed the documentation; it could be done in an additional commit here or in a new ticket.  For the new method `RationalField.places()`, I just added the `prec=Infinity` option.

- For consistency, `RDF` is now used instead for all bounds (there were two places where `RR` was used).

- The two coefficients of the Laurent series of the Weierstrass p-function that are needed can be obtained more easily as suitable multiples of the usual modular forms _c_<sub>4</sub> and _c_<sub>6</sub>.

- Added documentation for the functions mentioned in comment:32.

All tests pass, so if you are happy with the changes you can set this to positive review.


---

Comment by cremona created at 2014-04-09 20:31:45

Thanks -- I will look at your patches carefully when I am back next week.


---

Comment by cremona created at 2014-05-31 13:53:40

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2014-05-31 13:53:40

Peter, I am very sorry it took me so long to look at your reviewer's patches.  You should have reminded me!  I have looked at them and approve.  I do not know why the coloured blob at the top is not green (it looks red to me but I am not good on colours).


---

Comment by pbruin created at 2014-05-31 14:10:18

Replying to [comment:41 cremona]:
> Peter, I am very sorry it took me so long to look at your reviewer's patches.  You should have reminded me!  I have looked at them and approve.
Thank you!
> I do not know why the coloured blob at the top is not green (it looks red to me but I am not good on colours).
It is indeed red; this is because the blob shows the patchbot result for the latest stable release (6.2) instead of the latest development version, and the patchbot failed to build with 6.2, for reasons unrelated to this ticket.  Clicking on the blob will give you the result of all patchbot runs; the latest patchbot build (with 6.3.beta2) succeeded and passed tests.


---

Comment by cremona created at 2014-05-31 14:15:34

Replying to [comment:42 pbruin]:
> Replying to [comment:41 cremona]:
> > Peter, I am very sorry it took me so long to look at your reviewer's patches.  You should have reminded me!  I have looked at them and approve.
> Thank you!
> > I do not know why the coloured blob at the top is not green (it looks red to me but I am not good on colours).
> It is indeed red; this is because the blob shows the patchbot result for the latest stable release (6.2) instead of the latest development version, and the patchbot failed to build with 6.2, for reasons unrelated to this ticket.  Clicking on the blob will give you the result of all patchbot runs; the latest patchbot build (with 6.3.beta2) succeeded and passed tests.
Yes, I saw that green one.  It makes the blob on the ticket itself rather misleading!


---

Comment by vbraun created at 2014-06-02 12:46:01

PDF docs don't build


---

Comment by vbraun created at 2014-06-02 12:46:01

Changing status from positive_review to needs_work.


---

Comment by cremona created at 2014-06-02 18:31:16

Replying to [comment:44 vbraun]:
> PDF docs don't build

Please be more specific.  I don't know how to build the pdf docs for just the files created here, and a complete build (which I did do) produced such vast output that I cannot look for anything relevant in it.


---

Comment by vbraun created at 2014-06-02 20:22:54


```
grep -A 3 "Emergency stop" logs/docpdf.log
```



---

Comment by cremona created at 2014-06-03 07:58:15

Replying to [comment:46 vbraun]:
> {{{
> grep -A 3 "Emergency stop" logs/docpdf.log
> }}}

This shows nothing, even after several rounds of make doc-clean and make doc-pdf etc.
The log shows that the build quits after

```
OSError: [combinat ] /home/jec/sage/src/doc/en/reference/combinat/algebra.rst:4: WARNING: toctree contains reference to nonexisting document u'sage/combinat/free_module'
```

which has nothing to do with this ticket!


---

Comment by vbraun created at 2014-06-03 11:01:30

Does `sage -sync-build` fix it? If not: `make distclean && make`.


---

Comment by git created at 2014-06-03 12:06:07

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by pbruin created at 2014-06-03 12:08:33

Changing status from needs_work to positive_review.


---

Comment by pbruin created at 2014-06-03 12:08:33

I tried `make doc-pdf` and it TeX complained about being `\eps` being an undefined control sequence.  I changed it to `\epsilon`; hopefully that was the only problem.


---

Comment by pbruin created at 2014-06-03 14:31:50

Replying to [comment:50 pbruin]:
> I tried `make doc-pdf` and it TeX complained about being `\eps` being an undefined control sequence.  I changed it to `\epsilon`; hopefully that was the only problem.
Actually it wasn't, there is also a `\time` that should be a `\times`, patch coming soon.


---

Comment by pbruin created at 2014-06-03 14:31:50

Changing status from positive_review to needs_work.


---

Comment by git created at 2014-06-03 15:23:09

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by pbruin created at 2014-06-03 15:24:47

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2014-06-04 10:42:23

Resolution: fixed


---

Comment by jdemeyer created at 2014-10-02 09:31:58

Please see #17088 for a follow-up.
