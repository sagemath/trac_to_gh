# Issue 5837: bug in rational_diagonal_form() from QuadraticForm class

Issue created by migration from https://trac.sagemath.org/ticket/5837

Original creator: LBerlioz

Original creation time: 2009-04-20 20:12:46

Assignee: LBerlioz

CC:  tornaria

Keywords: QuadraticForm diagonal

The following returns a non-diagonal QuadraticForm:


```
sage: Q=QuadraticForm(2*A) 
sage: Q.rational_diagonal_form()
Quadratic form in 3 variables over Rational Field with coefficients:
[ -3 -32 5184 ]
[ * -81 26240 ]
[ * * -2125111 ] 
```


This method works only when the matrix has a diagonal of only ones.


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2009-04-20 22:36:34

Hi Luis, 

at this stage only blockers will be fixed in 3.4.1, so this ticket is getting bounced to 3.4.2. Since this bug produces mathematically incorrect answers this is also certainly not minor ;)

You should also attach a patch with a doctest that demonstrates that the problem has been fixed. Let me know if you have any questions. 

Gonzalo: If you find  the time can you review this?

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-20 22:36:34

Changing priority from minor to major.


---

Comment by tornaria created at 2009-04-20 22:40:16

Some issues in your patch:

 a. it's not a well formed patch (it's missing the filename to patch)
 b. some lines look badly indented, the `i=0` in the first line doesn't change the meaning, but the first `else` is paired with a `for`, not sure if that's what you actually mean.
 c. you should add a test case which shows the bug has been fixed. For instance, add something like
 {{{
        sage: Q2=QuadraticForm(ZZ,3,[ -3,2,0 , 3,-2 , 5 ])
        sage: Q2.rational_diagonal_form()
        Quadratic form in 3 variables over Rational Field with coefficients: 
        [ -3 0 0 ]
        [ * 10/3 0 ]
        [ * * 47/10 ]
}}}
 to the doctest.
 d. you are also changing the function to correctly handle quadratic forms with 0 in the diagonal. You should write a doctest for that case as well.

Personally, I'd avoid the exception and rewrite the code making an explicit test for `Q[i,i]Q=0`. This could also helps keeping the more natural `for i in range(n):` outer loop, which is easier to read than the `while i < n-1:` loop. The loop would just do a different thing depending on `Q[i,i]=0` or not. Just a suggestion, since you are writing the patch, do as you see is more convenient.


---

Comment by tornaria created at 2009-05-18 23:47:04

This issue is fixed in the doctest patch in #5954.


---

Comment by mabshoff created at 2009-05-19 00:39:26

Fixed via #5954, but credit still goes to Luiz for this ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-19 00:39:26

Resolution: fixed
