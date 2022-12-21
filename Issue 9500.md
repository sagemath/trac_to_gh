# Issue 9500: implement inversion of elements in a (more) general quotient ring

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-07-14 17:08:14

Assignee: AlexGhitza

Make this work:


```

            sage: R.<x,y> = QQ[]
            sage: I = R.ideal([x^2 + 1, y^3 - 2])
            sage: S.<i,cuberoot> = R.quotient(I)
            sage: 1/(1+i)
            -1/2*i + 1/2

        Confirm via symbolic computation::
        
            sage: 1/(1+sqrt(-1))
            -1/2*I + 1/2

        Another more complicated quotient::
        
            sage: b = 1/(i+cuberoot); b
            1/5*i*cuberoot^2 - 2/5*i*cuberoot + 2/5*cuberoot^2 - 1/5*i + 1/5*cuberoot - 2/5
            sage: b*(i+cuberoot)
            1
```



---

Comment by was created at 2010-07-14 19:45:23

Relevant benchmarks: http://wiki.sagemath.org/days23.5/projects/relative_number_fields


---

Attachment


---

Comment by was created at 2010-07-14 20:30:24

#9499 needs to be finished before this can be reviewed.


---

Comment by was created at 2010-07-14 20:30:24

Changing status from new to needs_review.


---

Comment by malb created at 2010-07-14 23:04:53

Patch look good and applies cleanly to 4.4.4 +#9499 (which is required).


---

Comment by malb created at 2010-07-14 23:05:04

Changing status from needs_review to positive_review.


---

Comment by malb created at 2010-07-14 23:05:04

Doctests pass.


---

Comment by mpatel created at 2010-07-20 09:32:31

Resolution: fixed
