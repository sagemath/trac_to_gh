# Issue 3031: [with patch] Add zeta_function method for schemes

Issue created by migration from Trac.

Original creator: kedlaya

Original creation time: 2008-04-26 15:42:49

Assignee: wstein

CC:  kedlaya

Keywords: zeta function, schemes, finite fields

The attached patch (built against 3.0) adds a zeta_function method to the class of schemes over finite fields. It is meant to be a default procedure, to be overridden by something more sensible for particular classes of schemes (e.g., elliptic and hyperelliptic curves).

Zeta functions are currently only enabled over prime fields, but it will be trivial to fix that once coercion between nonprime finite fields is supported.


---

Attachment


---

Attachment


---

Comment by craigcitro created at 2008-04-27 00:53:30

Looks good. Added a patch with a few additional doctests, killed some long lines, and fixed one tiny tiny bug: the code was `return`ing exceptions, instead of `raise`ing them. Merge both patches.


---

Comment by mabshoff created at 2008-04-27 01:25:59

Merged both patches in Sage 3.0.1.alpha1


---

Comment by mabshoff created at 2008-04-27 01:25:59

Resolution: fixed


---

Comment by cremona created at 2008-04-27 20:25:34

I have taken a look at the code.  Some tweaking will be needed to make
it sensibly compatible with the existing code for point counting of
elliptic curves.  There, the function cardinality() takes a parameter
extension_degree with default 1, while you do a base change to get the
cardinality over extensions.  Secondly, I think having a cardinality()
method is better than calling a rational_points() functioI have taken
a look at the code.  Some tweaking will be needed to make it sensibly
compatible with the existing code for point counting of elliptic
curves.  There, the function cardinality() takes a n and then taking
the len() of the result, since there is little point in creating a
list of all the rational points at all if what one needs is their
number.


---

Comment by mabshoff created at 2008-04-28 02:32:31

As various people have pointed out there are various problems here. Hence it will be reopened and I will revert the two applied patches.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-28 02:32:31

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-04-28 02:32:31

Changing status from closed to reopened.


---

Attachment


---

Comment by craigcitro created at 2008-04-28 03:36:13

ncalexan brought up the good point that maybe some users will expect a rational function from zeta_function. After some discussion, it's been renamed to zeta_series. 

I also fixed about 10 occurrences of "the the" in sage.


---

Comment by ncalexan created at 2008-04-28 05:09:48

I prefer the name zeta_series and hope that zeta_function (Returning a rational function!) will be implemented in the near future.


---

Comment by mabshoff created at 2008-04-29 00:04:45

Remerged the previously reverted patches and merged trac-3031-pt3.patch in Sage 3.0.1.alpha1


---

Comment by mabshoff created at 2008-04-29 00:04:45

Resolution: fixed
