# Issue 917: [with patch] Matrix.minors

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-10-18 11:26:55

Assignee: was

The attached patch implements a method to return the list of all k-minors of a matrix A.

Let A be an m x n matrix and k an integer with 0 < k, k <= m, and
k <= n. A k x k minor of A is the determinant of a k x k matrix
obtained from A by deleting m - k rows and n - k columns.

The returned list is sorted in lexicographical row major ordering,
e.g., if A is a 3 x 3 matrix then the minors returned are with
for these rows/columns:  [ [0, 1]x[0, 1], [0, 1]x[0, 2],
[0, 1]x[1, 2], [0, 2]x[0, 1], [0, 2]x[0, 2], [0, 2]x[1, 2],
[1, 2]x[0, 1], [1, 2]x[0, 2], [1, 2]x[1, 2] ].

Note I am not sure if this method is too trivial or too specialised to be included with SAGE. I am submitting it here such that others can decide on that.


---

Comment by was created at 2007-10-21 01:15:32

Resolution: fixed


---

Attachment

This should definitely go in.
