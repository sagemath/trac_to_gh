# Issue 1840: Hill cipher addition to crypto package

Issue created by migration from Trac.

Original creator: kohel

Original creation time: 2008-01-18 23:08:19

Assignee: cwitty

This adds functionality for Hill ciphers as in the following example:

sage: S = AlphabeticStrings()
sage: E = HillCryptosystem(S,7)
sage: E.random_key()

[13  1 23  4 14 15  0]
[11  4  4 12  0 23 14]
[18  4 25 13 10  7 10]
[ 9 14 13 11  1 12 10]
[13  8 10 19 24 13 24]
[ 8  7 12 12 25  2 10]
[ 2  7  1 10 13 12  5]
sage: e = E(E.random_key())
sage: e

[ 1  9  8 17 16  2 13]
[11 12 12 24 12 25  2]
[18 21 20  2 16  7 17]
[17 17  8 19 14 23 19]
[15 11 24  6  5  7  4]
[17 20 18  6 16 13 13]
[ 2 12 17  4 23  4  4]
sage: pt = S([ randint(0,25) for i in range(7*16) ])
sage: pt
QWTWCUQMBMTGDSGTHNJLBNDEXYWGJKHZGAPRFKMPGJDXDLYYGZVTXHLJIMOGKERMWCMOOJKHGCTXAOVIJCXBIGRSLVCBZAXJBCDAEHUZUGCEYCLA
sage: e(pt)
YBQWKZZLXQLKVACTPHEFPHAWYSSUKFVQJGJVGVNYWXDRYMYHXZIBOGJISSTQTOQYQPYNKIVPAQZNJDXJRNPKQUWYRRGRLGERSLXUAWAMXXGSQETD
sage: c = e.inverse()
sage: c(e(pt)) == pt
True
sage: e.key()

[ 1  9  8 17 16  2 13]
[11 12 12 24 12 25  2]
[18 21 20  2 16  7 17]
[17 17  8 19 14 23 19]
[15 11 24  6  5  7  4]
[17 20 18  6 16 13 13]
[ 2 12 17  4 23  4  4]
sage: type(e.key())
<type 'sage.matrix.matrix_modn_dense.Matrix_modn_dense'>
sage: type(e)
<class 'sage.crypto.classical_cipher.HillCipher'>
sage: A = e.key()
sage: A.det()
17


---

Attachment


---

Comment by malb created at 2008-01-20 17:56:56

Patch looks good and applies cleanly against 2.10. Only detail: It uses `__repr__` rather than `_repr_` (two instead of one underscore) but inherits from `SageObject`. All objects inheriting from `SageObject` are supposed to implement `_repr_`.


---

Attachment


---

Comment by mhansen created at 2008-01-21 05:39:54

Works for me, and I posted a second patch changing __repr__'s to _repr_.


---

Comment by mabshoff created at 2008-01-21 06:22:00

Merged in Sage 2.10.1.alpha1


---

Comment by mabshoff created at 2008-01-21 06:22:00

Resolution: fixed
