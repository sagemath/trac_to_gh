# Issue 8094: shortcuts for matrix transpose, complex conjugate, ...

Issue created by migration from https://trac.sagemath.org/ticket/8094

Original creator: schilly

Original creation time: 2010-01-27 13:00:23

Assignee: was

CC:  robertwb rbeezer

The aim is to enhance `/sage/matrix/matrix*.pyx` files with a `__getattr__` mechanism to call `self.transpose()` and others more quickly. The attribute lookup mechanism provides a shortcut like `self.T` that is resolved to `self.transpose()`. 
Shortcuts should be similar to other environments like `numpy`.

Additionally, `__setattr__` and `__delattr__` have to be implemented to avoid modification and deletion of these attributes.

Notes: [python data model](http://docs.python.org/reference/datamodel.html#customizing-attribute-access).


---

Comment by schilly created at 2010-01-27 15:39:41

Changing status from new to needs_work.


---

Comment by schilly created at 2010-01-27 15:39:41

This first patch adds .T for all kinds of matrices in matrix_dense.pyx and some docstrings.


---

Comment by schilly created at 2010-01-27 18:09:15

`.T` has more tests and I think it works for all of them now.

attachment *.2.patch should be deleted or ignored.


---

Comment by jason created at 2010-01-28 06:42:01

I deleted the .2.patch.


---

Comment by jason created at 2010-01-28 06:44:53

Since these are cython files, why don't you use the Cython property functionality to implement this?

http://docs.cython.org/docs/extension_types.html#properties

Robert, is there an efficiency gain or some reason why one would prefer the Cython property statement to what is in this patch?


---

Comment by schilly created at 2010-01-28 09:37:04

I thought that properties don't work in cython files, but yesterday I tried them (the decorator didn't work, but just the statement is fine) and they do. Thank's for the reference! I'll use them. The advantage is that then you have these shortcuts in autocomplete. It's also better to define them once and for all in matrix2.pyx - I think that's the best place?


---

Comment by schilly created at 2010-03-22 17:40:28

doin' it the cython way


---

Attachment


---

Comment by jason created at 2010-12-18 19:57:03

schilly: is this patch still needs_work, or should it be needs_review now?


---

Comment by schilly created at 2010-12-18 20:00:37

jason: as far as i remember, the problem was that it was interfering with another matrix property (i.e. a doctest was failing and I didn't really understand why). so, the idea as it is coded works, but it's not ready for review.


---

Comment by jason created at 2010-12-18 20:04:58

I see one doctest in matrix2.pyx failing, but that's because the expected output was wrong (it's the test for M.H in the conjugate() method).


---

Comment by schilly created at 2010-12-18 20:08:21

ah well, time has passed since i looked into it, but it was a doctest failure somewhere else. probably just another one that has to be modified ... or it isn't an issue any more ;)


---

Comment by jason created at 2010-12-18 20:12:18

I'm uploading a reviewer patch and giving a positive review momentarily :).


---

Comment by schilly created at 2010-12-18 20:16:54

woohoo \o/


---

Comment by jason created at 2010-12-18 20:22:44

apply on top of previous patches


---

Attachment

Okay, maybe my changes should be reviewed (since they fix some of the doc issues).  

Doctests pass in matrix/*.py[x] with these patches applied, and Harald's code looks good, so positive review for his patch (given that my doctest patch is applied).  

Someone should verify my doctest changes are good.


---

Comment by jason created at 2010-12-18 20:25:25

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2010-12-19 19:08:45

Jason and Harald,

Thanks for putting this together.  I'd like to finish up getting this reviewed.  But two questions:

1.  It seems like there is evidence of the shortcuts in each of the associated docstrings for the methods, but maybe it isn't always obvious.  Like  `A.I` seems to be buried along with the `~` version and has no real explanation that it is a property.  I find students get very confused with method calls with empty parentheses, and a property will just add to that, so I think it would be better to have some explanation.

2.  #10471  implements `conjugate_transpose()` until we reclaim `adjoint()`.  So that would be the place to add in the shortcut.  Should we add that here since #10471 has a positive review, and maybe change the definition?

I can do the above on a reviewer patch in the next day or two if necessary.

Rob


---

Comment by rbeezer created at 2010-12-19 19:08:45

Changing status from needs_review to needs_info.


---

Attachment


---

Comment by mraum created at 2011-08-05 17:28:39

Changing status from needs_info to needs_review.


---

Comment by mraum created at 2011-08-05 17:28:39

I added a further example in the documentation of conjugate_transpose.

I am not sure whether 1. can be addressed at all. Typing m.T? I get the documentation of m. I would suggest to finish this anyway. It is a shame that this patch hasn't been merged for almost 2 years, and one doesn't need to tell students that they type m.T.


---

Attachment


---

Comment by rbeezer created at 2011-08-22 22:00:08

These are some of the earliest entries in the reference manual for `sage/matrix/matrix2.pyx`, so I think the documentation should include some examples, especially since the syntax is different (no parentheses).  However, INPUT and OUTPUT blocks feel like make-work, so I have not included that.

I can give a positive review to everything up to my latest patch.  If somebody would review my (documentation-only) changes, this could be done.

Rob


---

Comment by mraum created at 2011-08-24 08:08:11

Good idea to add this documentation. Everything works fine.


---

Comment by mraum created at 2011-08-24 08:08:11

Changing status from needs_review to positive_review.


---

Comment by jason created at 2011-08-24 13:11:17

Maybe on another ticket, but can I ask for one more enhancement on this?  Can we make the following work:


```
matrix("""
[1 2]
[3 4]
""")

(i.e., any "]" or "[" next to row delimiters are stripped).  That would mean that I could cut and paste output from Sage back into Sage to make a matrix.


---

Comment by jason created at 2011-08-24 13:12:02

Argh.   Wrong ticket; please ignore my comment!


---

Comment by rbeezer created at 2011-08-24 15:09:32

Replying to [comment:22 jason]:
> Argh.   Wrong ticket; please ignore my comment!

Whew!  ;-)


---

Comment by rbeezer created at 2011-08-25 18:58:52

Changing keywords from "" to "sd32".


---

Comment by leif created at 2011-09-12 15:18:38

Changing status from positive_review to needs_work.


---

Comment by leif created at 2011-09-12 15:18:38

[attachment:8094-shortcut-matrix-transpose.patch] is not a Mercurial changeset.

```
abort: no username supplied (see "hg help config")
```

Sorry, Harald. ;)


---

Attachment

I did some maintenance on the main patch, naming it "v2".  Has Harald's user info and is now a proper hg patch.  I hope.  

Should now be ready to go, since I did not change any code, so should not need a review.


---

Comment by rbeezer created at 2011-09-18 04:15:56

Changing status from needs_work to positive_review.


---

Comment by leif created at 2011-09-18 04:32:36

Replying to [comment:27 rbeezer]:
> I did some maintenance on the main patch, naming it "v2".  Has Harald's user info and is now a proper hg patch.  I hope.

Yep, sorry. I would have done it myself but failed to recall Harald's e-mail address that moment; then later was simply too busy to search which ticket it was...




> Should now be ready to go, since I did not change any code, so should not need a review.

Think so. Only meta data (including line numbers) differ.

As I had other trouble with the release, I think I can still include it.


---

Comment by leif created at 2011-09-18 07:01:11

Same patch rebased on (prerelease) Sage 4.7.2.alpha3 because of fuzz 2.


---

Attachment

Same patch rebased on (prerelease) Sage 4.7.2.alpha3 because of fuzz 2.


---

Comment by leif created at 2011-09-18 07:08:10

Attached rebased versions of two patches because of fuzz 2.


---

Comment by leif created at 2011-09-18 09:37:06

Resolution: fixed
