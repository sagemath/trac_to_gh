# Issue 8994: Improve convolution support

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2010-05-19 17:21:31

Assignee: burcin

Keywords: convolution, convolve, discrete, continuous

We have convolution scattered in several places, including

```
sage.rings.polynomial.convolution
sage.functions.piecewise.PiecewisePolynomial.convolution
sage.gsl.dft.IndexedSequence.convolution
```

This should be extended to make it easier to use/find and to support more arbitrary inputs, both discrete and continuous.

See [http://groups.google.com/group/sage-support/browse_thread/thread/7f90c228df9530dd](http://groups.google.com/group/sage-support/browse_thread/thread/7f90c228df9530dd) for background.


---

Comment by mkoeppe created at 2016-06-25 17:38:36

Updated description to reflect changes in new `piecewise` implementation (#14801).
Changing to "wishlist" because nobody seems to have worked on it in 6 years
