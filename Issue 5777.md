# Issue 5777: [with package and patches, needs review] update to pynac 0.1.5

Issue created by migration from https://trac.sagemath.org/ticket/5777

Original creator: burcin

Original creation time: 2009-04-13 16:07:10

Assignee: burcin

CC:  wstein mhansen ncalexan robertwb

There is a new version of pynac with the following changes:

 * Change printing of pi (Pi -> pi)
 * Delay evaluation of special functions until .evalf() is called
 * Add precision parameter to .evalf()

I am opening a new ticket, since the patches require separate review.

The package is here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.5.spkg

Attached patches need to be applied to Sage, they depend on #5753.

I got an infinite loop trying to convert to `ComplexField` in the second patch, hence the additions to sage/rings/complex_field.py. Robert, am I doing something wrong here?


---

Comment by burcin created at 2009-04-13 16:07:55

fix doctests for printing changes


---

Attachment

allow setting precision for numerical approximation


---

Comment by burcin created at 2009-04-24 14:21:32

Rebased attachment:trac_5777-02-precision.patch for 3.4.1.


---

Comment by burcin created at 2009-05-05 23:12:23

add doctests for exceptions raised during hashing


---

Attachment

support pickling pynac expressions


---

Attachment

support pickling symbolic functions


---

Comment by burcin created at 2009-05-05 23:13:40

doctests for the changes in behavior of exp


---

Attachment

I put a preliminary version of the new pynac package here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.6.spkg

I haven't actually committed the version information to the pynac repository yet. I plan to wait until this gets reviewed, and see if there are any last minute changes needed.

The newly uploaded patches:

 * attachment:trac_5777-11-hash_doctests.patch
 * attachment:trac_5777-12-pickle_expression.patch
 * attachment:trac_5777-13-pickle_sfunction.patch
 * attachment:trac_5777-14-exp.patch

correspond to the changes in the new package.

The changes in pynac are:
 * Fix error handling in Number_T::hash().
 * Add support for archiving numeric and function objects.
 * Fix comparison bug in mul.
 * Fix gcc warnings about conversion of strings to char*.
 * Change exp to not prints exponents of 1.
 * Add power method to exp so that `(e<sup>x)</sup>y -> e^(x*y)`.

Note that this fixes #5944, which I consider a blocker.


---

Comment by mhansen created at 2009-05-19 01:48:20

Changing assignee from burcin to mhansen.


---

Comment by mhansen created at 2009-05-19 01:48:20

Changing status from new to assigned.


---

Comment by mhansen created at 2009-05-19 01:48:20

I have all of Burcin's changes that apply to 4.0.rc0 in symbolics_final1.patch.  These work with the pynac-0.1.6.spkg.

These get a positive review from me.  I've based the new symbolics changes on these.


---

Attachment

Merged in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-20 23:44:31

Resolution: fixed
