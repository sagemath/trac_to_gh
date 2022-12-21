# Issue 1763: implement norms for matrices

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2008-01-12 09:30:43

Assignee: was

CC:  harald.schilly@gmail.com

Add functionality to implement various types of norms on matrices; for starters, see
http://en.wikipedia.org/wiki/Matrix_norm




---

Attachment

This patch adds the most common norm used for matrices: 1,2,\inf and Frobenius (and "entry-wise norm"). 2 points:
 * I don't believe there's a general formula for the p-norm, although I hear estimations can be computed. I could be wrong though.
 * I stuck this in matrix2.pyx and arbitrarily chose to use convert anything to RDF matrices since RDF matrices actually have a SVD method (which is needed for the 2-norm). I'd like to hear people comments on that.


---

Attachment

apply after the above patch


---

Comment by AlexGhitza created at 2008-04-01 04:49:47

Hi Didier,

I have a few concerns about the patch:

 1. as it is, it only returns an RDF if p=2, and some other type depending on the coefficient of the matrix otherwise; it would be preferable to have a uniform behavior

 2. for vectors, the syntax for the inf-norm is norm(Infinity), whereas here it is norm('inf'); it would be better to be consistent about this

 3. there are a bunch of trivial typos in the docstring and comments

 4. being a number theorist, to me 'frob' is much more suggestive of Frobenius than 'fro'.

Since all of this is fairly straightforward, I went ahead and put up an add-on patch.


---

Comment by robertwb created at 2008-04-06 06:15:06

This doesn't handle matrices with negative or complex entries correctly, it should be taking absolute values in several places. 

+1 to AlexGhitza's changes though.


---

Comment by AlexGhitza created at 2008-04-09 13:49:33

apply instead of the other patches


---

Attachment

I modified the previous patches so that norm() works correctly on matrices with negative and/or complex entries.  I also added a conjugate() function for conjugating a complex matrix.

1763-replacement.patch should be applied instead of the previous patches.


---

Comment by mhansen created at 2008-04-14 22:55:27

Looks good to me.


---

Comment by mabshoff created at 2008-04-15 00:28:57

Resolution: fixed


---

Comment by mabshoff created at 2008-04-15 00:28:57

Merged in Sage 3.0.alpha5
