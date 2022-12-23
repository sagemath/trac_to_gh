# Issue 4926: convert sage.schemes.* docstrings to Sphinx

Issue created by migration from https://trac.sagemath.org/ticket/4926

Original creator: mhansen

Original creation time: 2009-01-01 22:55:55

Assignee: tba




---

Comment by mhansen created at 2009-01-02 02:38:33

Patch at http://sage.math.washington.edu/home/mhansen/trac_4926.patch


---

Comment by cremona created at 2009-01-03 17:18:56

Review (from reading the html output):

Schemes section

   * base_extend(): missing newline before EXAMPLES
   * projective_embedding(): bad indentation for second INPUT block
   * affine_patch() has a comma at the start of a line
   * projective_embedding(): bad indentation for second INPUT block (again)

Elliptic and Plane Curves section

   * typo in arithmetic_genus():  "normalization"
   * division_polynomial(): bad indentation in the (rather long) explanation of input parameter two_torsion_multiplicity; some math-mode missing here too.

[I noticed that the functions are sorted into alphabetical order, with upper case before lower case.  Can we make it case-insensitive?  For example, S_integral_points() comes right near the top.]

   * typo in heegner_index: "currently"
   * modular_degree(): in one place algorithm 'ec' is mentioned instead of 'sympow'.
   * regulator_of_points: bad indentation of INPUT
   * tamagawa_exponent(): bad math translation of $C_2\times C_2$.
   * group_law (in formal_group):  missing subscript tage on t1, t2;  bad exponent "prec". same in mult_by_n() and possibly elsewhere.
   * frobenius_expansion_by_series(): the 2nd and 3rd large displays are merged.  I think "where" should be on a separate line in between.
   * "p-adic functions from ell_rational_field.py, moved here to reduce" is a sill name.  I suggest renameing to simply "p-adic functions", perhaps with "miscellaneous".

Hyperelliptic curve section:

   * At bottom of section "Conductor and Reduction Types for Genus 2 Curves": the reference to the paper of Liu looks all wrong.


---

Comment by cremona created at 2009-01-03 17:23:47

I forgot to say:  patch applies ok to 3.2.3.final.  I have not tried editing the source to fix the things I found, since I don't know how to check the result.


---

Attachment


---

Comment by mhansen created at 2009-01-11 04:44:14

I've posted a patch which addresses these changes.


---

Comment by cremona created at 2009-01-13 21:55:00

Looks good now.  Pass!


---

Attachment


---

Comment by mabshoff created at 2009-02-24 18:56:10

Resolution: fixed


---

Comment by mabshoff created at 2009-02-24 18:56:10

Merged in Sage 3.4.alpha0.

Cheers,

Michael
