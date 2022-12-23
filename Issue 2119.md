# Issue 2119: matlab matrix conversion issue

Issue created by migration from https://trac.sagemath.org/ticket/2119

Original creator: mabshoff

Original creation time: 2008-02-08 19:45:40

Assignee: cwitty

Reported by Kate:

```
a0 = matlab('eye(50)')
sage: a1 = matrix(ZZ,a0)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/mabshoff/<ipython console> in <module>()

/home/was/s/local/lib/python2.5/site-packages/sage/matrix/constructor.py in matrix(arg0, arg1, arg2, arg3, sparse)
    287     
    288     if hasattr(arg1, '_matrix_'):
--> 289         return arg1._matrix_(arg0)
    290 
    291     if arg0 is None:

/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/matlab.py in _matrix_(self, R)
    283         M = MatrixSpace(R, nrows, ncols)
    284         v = sum([[x for x in w.split()] for w in v], [])
--> 285         return M(v)
    286 
    287     def set(self, i, j, x):

/home/was/s/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py in __call__(self, entries, coerce, copy, rows)
    352             return self(entries.matrix(), copy=False)
    353 
--> 354         return self.matrix(entries, copy=copy, coerce=coerce, rows=rows)
    355 
    356     def change_ring(self, R):

/home/was/s/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py in matrix(self, x, coerce, copy, rows)
    965                 x = new_x
    966             
--> 967         return self.__matrix_class(self, entries=x, copy=copy, coerce=coerce) 
    968      
    969     def matrix_space(self, nrows=None, ncols=None, sparse=False):

/home/mabshoff/matrix_integer_dense.pyx in sage.matrix.matrix_integer_dense.Matrix_integer_dense.__init__()

<type 'exceptions.TypeError'>: entries has the wrong length
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-02-08 20:09:00

Moreover there is also the following issue reported in the same thread:

```
a00 = str(mathlab('mat2str(eye(50))'))
a01 = a00.replace(' ',',').replace(';','],[')
a02 = '[' + a01 = ']'
a03 = eval(a02)
a1 = matrix(zz,a03)
a2 = matlab.sage2matlab_matrix_string(a1)
a3 = 'm1 = ' + a2
matlab.eval(a3)     # crashes
# Q: caused by "maxread=100" and/or "eval_using_file_cutoff=100"
# in devel/sage-main/build/sage/interfaces/matlab.py ?
```


Cheers,

Michael


---

Comment by mhansen created at 2008-09-04 00:50:39

Changing assignee from cwitty to mhansen.


---

Comment by mhansen created at 2008-09-04 00:50:39

Changing status from new to assigned.


---

Comment by mhansen created at 2008-09-04 00:50:39

The original bug is caused by things like 'Columns', '27', 'through', '39' appearing in the entries.


---

Comment by mhansen created at 2010-01-17 05:44:19

Changing status from new to needs_review.


---

Comment by rossk created at 2010-02-12 15:29:53

Tried this on 2 platforms. First example is fixed by the patch i.e.

```
b0 = matlab('eye(50)')
b1 = matrix(ZZ,b0)
}}} 
but the second example (note that 3 minor typos have been removed) is still broken but shouldnt be (i.e. the displaying/printing of variable a3 shows that a3 is a valid matlab expression). Is the reference to the \x07 character mean "BELL" (a 'ding' made by PCs)? Note that if the following code uses eye(5) it works but with eye(6) it crashes with that x07 error.
{{{
sage: a00 = str(matlab('mat2str(eye(6))'))
sage: a01 = a00.replace(' ',',').replace(';','],[')
sage: a02 = '[' + a01 + ']'
sage: a03 = eval(a02)
sage: a1 = matrix(ZZ,a03)
sage: a2 = matlab.sage2matlab_matrix_string(a1)
sage: a3 = 'm1 = ' + a2
sage: matlab.eval(a3)    
'\x07??? source("/home/rossk/.sage//temp/sage.math.washington.edu/31533//interface//tmp31533");\n           |\nError: The input character is not valid in MATLAB statements or expressions.\n'
sage: a3
'm1 = [1, 0, 0, 0, 0, 0; 0, 1, 0, 0, 0, 0; 0, 0, 1, 0, 0, 0; 0, 0, 0, 1, 0, 0; 0, 0, 0, 0, 1, 0; 0, 0, 0, 0, 0, 1]'
}}}


---

Comment by rossk created at 2010-02-12 15:29:53

Changing keywords from "" to "matlab conversion".


---

Comment by rossk created at 2010-02-12 15:29:53

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by mhansen created at 2010-07-11 00:44:58

I've posted a new patch which fixes the issue above.


---

Comment by mhansen created at 2010-07-11 00:44:58

Changing status from needs_work to needs_review.


---

Comment by rossk created at 2010-07-13 02:08:38

Mike

Looks good. The patch fixes the \x07 issue and the matrices that crashed because they ran over multiple pages (if anything else is discovered with the matlab interface, it should go into a new ticket). Positive review.


---

Comment by rossk created at 2010-07-13 02:08:38

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-22 07:28:53

Resolution: fixed


---

Comment by mpatel created at 2010-07-27 07:19:44

Please see #9608 for docbuild warnings that may stem from this ticket.
