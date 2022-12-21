# Issue 6119: implement taylor series without maxima

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-05-22 02:38:25

Assignee: burcin

CC:  kcrisman rws

Ginac has series about zero, it should be easy to shift to get the series about any point.


---

Comment by burcin created at 2011-06-29 13:38:10

From comment:6:ticket:9555:

> The taylor() method is cruft left over from pre-pynac symbolics. We should deprecate it in favor of the series() method. It's perfectly acceptable to give Puiseux series as a result of a call to .series(). I expect this to be done in #6119, where we add an algorithm= option to .series(). The default behavior can be to call pynac and fall back to maxima if that returns an error.

In short, we should change this ticket to cover this transition. Series expansions in Pynac need more work to match what maxima does. That should be tracked on the pynac issue tracker:

https://bitbucket.org/burcin/pynac/issues


---

Comment by kcrisman created at 2011-06-29 13:40:44

As I say in #9555, I think that changing the `.taylor()` method so that it calls a suitably Taylor-only version of the `.series()` method is preferable, especially since the global name `taylor()` should really be kept.


---

Comment by kcrisman created at 2014-12-06 20:27:19

See also http://sourceforge.net/p/maxima/bugs/2850/ where this comes up again.


---

Comment by kcrisman created at 2014-12-08 14:15:38

> As I say in #9555, I think that changing the `.taylor()` method so that it calls a suitably Taylor-only version of the `.series()` method is preferable, especially since the global name `taylor()` should really be kept.
And I'm quoted at [this SO comment](http://stackoverflow.com/questions/27288164/non-integral-exponent-for-taylor-expansion-using-sage/27297471) though I still have to think more about how we should solve this.


---

Comment by kcrisman created at 2017-01-18 14:42:44

Is this deprecating or simply replacing?  Sorry for being confused.
----
New commits:


---

Comment by rws created at 2017-01-18 14:46:50

Too fast. The deprecation part is upcoming. The Maxima replacement depends on a bugfix in upcoming pynac-0.7.4 for one doctest fail.


---

Comment by rws created at 2017-01-18 14:48:56

Replying to [comment:3 kcrisman]:
> As I say in #9555, I think that changing the `.taylor()` method so that it calls a suitably Taylor-only version of the `.series()` method is preferable, especially since the global name `taylor()` should really be kept.

Just rereading. So maybe we already have finished the ticket? If so, please review.


---

Comment by kcrisman created at 2017-01-18 15:36:37

Nah, I think it is better to do _some_ form of deprecation warning rather than a totally silent change, though I think that keeping taylor as giving taylor only would be plausible too.


---

Comment by rws created at 2017-01-18 15:51:23

Maxima is still faster than GiNaC in the cases with irrational coefficients so we will have to use GiNaC/Pynac for both `series` and `taylor` only in the rational case.
