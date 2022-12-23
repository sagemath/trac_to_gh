# Issue 5753: [with patch and package, needs review] update to pynac 0.1.4

Issue created by migration from https://trac.sagemath.org/ticket/5753

Original creator: burcin

Original creation time: 2009-04-11 15:50:38

Assignee: burcin

CC:  wstein mhansen ncalexan

Pynac 0.1.4 is out! :)

Changes from 0.1.3 are:
 * Add support for arithmetic with infinity.
 * Use python repr function for printing numeric objects.
 * Print paranthesis in latex mode with \left and \right.
 * Call python for latex names of symbols.
 * Support calling user specified python functions to print function instances.
 * Call python for printing function and fderivative.


Attached patches corresponding to the above changes should be applied to the Sage library. Patches below depend on #5546 and #5737, in particular trac_5546-2-pynac_derivative.patch and trac_5737-02-real_imag.patch.



---

Attachment

arithmetic with infinity


---

Attachment

fix coercion of complex i


---

Comment by burcin created at 2009-04-11 15:52:59

fix doctests for printing changes


---

Attachment

fix printing of latex parenthesis


---

Comment by burcin created at 2009-04-11 15:54:16

call python for latex representation of symbols


---

Attachment

allow custom printing methods in symbolic functions, move printing of function and fderivative to python


---

Comment by burcin created at 2009-04-11 15:56:35

The package is here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.4.spkg

Sorry for the spam.


---

Comment by mabshoff created at 2009-05-20 23:45:57

The positive review is due to Mike Hansen's review at #5777.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-20 23:46:09

Resolution: fixed


---

Comment by mabshoff created at 2009-05-20 23:46:09

Merged in Sage 4.0.rc0.

Cheers,

Michael
