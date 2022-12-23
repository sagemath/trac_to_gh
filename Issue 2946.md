# Issue 2946: bug in jordan_form

Issue created by migration from https://trac.sagemath.org/ticket/2946

Original creator: mhampton

Original creation time: 2008-04-17 21:27:33

Assignee: was

Keywords: jordan_form, matrix

Matrices with 0 eigenvalues crash jordan_form.  1x1 matrices do not seem affected, so the simplest example is:


```
j1 = matrix(ZZ,2,2,[[0,0],[0,0]])
j1.jordan_form()
```


The following code might be of some use in testing this; the function tough_nut(n) produces a highly degenerate nilpotent n by n matrix:


```
def uprand(i,j, max_i = 1):
    if i > j: return 0
    if i == j: return 1
    return Integer(randint(0,max_i))
def superd(i,j, odds = .75):
    if j - i == 1: 
        temp = random()
        if temp < odds: return 1
        else: return 0
    return 0
def tough_nut(m_size, odds = .75):
    t1 = matrix(ZZ,m_size,m_size,[[uprand(i, j, max_i = 4) for j in range(m_size)] for i in range(m_size)])
    t2 = matrix(ZZ,m_size,m_size,[[uprand(i, j, max_i = 4) for j in range(m_size)] for i in range(m_size)])
    t2 = t2.transpose()
    pre_j = matrix(ZZ,m_size,m_size,[[superd(i,j, odds = odds) for j in range(m_size)] for i in range(m_size)])
    mystery_mat = t1*t2*pre_j*t2.inverse()*t1.inverse()
    return mystery_mat
```


At first I thought this was only caused by nilpotents, but it affects many matrices with a zero eigenvalue.  Maybe it is more pervasive than that.


---

Comment by wjp created at 2008-04-17 21:49:47

The current `jordan_form` computes the number of Jordan blocks of size 1 at eigenvalue x of a matrix A as `rank(A) - rank(A - x)`. This should be `dim(ker(A-x)) = size(A) - rank(A - x)`.

The attached patch fixes this.


---

Attachment


---

Comment by mhansen created at 2008-04-18 00:20:06

Looks good to me.


---

Comment by mabshoff created at 2008-04-18 06:15:39

Resolution: fixed


---

Comment by mabshoff created at 2008-04-18 06:15:39

Merged in Sage 3.0.alpha6


---

Comment by mabshoff created at 2008-04-18 06:19:30

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-04-18 06:19:30

There are rejection problems [with or without #2947 applied]:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha6/devel/sage$ patch -p1 < trac_2947_block_matrix_empty.patch
patching file sage/matrix/constructor.py
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha6/devel/sage$ patch -p1 < trac_2946_noninvertible_jordan_form.patch
patching file sage/matrix/matrix2.pyx
Hunk #1 succeeded at 3591 (offset 59 lines).
Hunk #2 FAILED at 3601.
Hunk #3 FAILED at 3630.
2 out of 3 hunks FAILED -- saving rejects to file sage/matrix/matrix2.pyx.rej
```

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-18 06:19:30

Changing status from closed to reopened.


---

Attachment


---

Comment by mabshoff created at 2008-04-18 06:49:56

Resolution: fixed


---

Comment by mabshoff created at 2008-04-18 06:49:56

Merged 2946.patch in Sage 3.0.alpha6


---

Comment by jason created at 2008-04-18 11:50:45

Thanks for catching and fixing this!  Sorry I forgot about poor ol' zero as an eigenvalue when I wrote the original code and doctests; my bad.
