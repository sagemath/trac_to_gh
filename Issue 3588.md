# Issue 3588: Divison may involve lengthy calculations

Issue created by migration from https://trac.sagemath.org/ticket/3588

Original creator: robertwb

Original creation time: 2008-07-07 20:23:11

Assignee: robertwb


```
sage: p = random_prime(2^1000, proof=False)

sage: r = Integers(p)(2)

sage: time 1/r
CPU times: user 8.33 s, sys: 0.04 s, total: 8.37 s
Wall time: 8.38 s
 3499526081536621642679042248089160305431650460015592790597504050874839449753564641181241694531732168529968232075793871659087004627036430097798051425534663680136477216778245568521334956231031996455409743133009480089945324001250066901998383114487031466512725971538453941363837544198631115493811447198845
```


The generic fraction_field() call does primality testing here, takes too long. 


---

Comment by robertwb created at 2008-07-07 21:06:12

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2008-07-11 17:50:22

This is 3.0.5 material, too.

Cheers,

Michael


---

Comment by was created at 2008-07-11 18:04:04

Resolution: fixed


---

Comment by was created at 2008-07-11 18:47:18

Changing status from closed to reopened.


---

Comment by was created at 2008-07-11 18:47:18

A doctest failed in infinity.py.  I've posted a quick fix here.  Robert could easily have a better fix, so this is reopened.


---

Comment by was created at 2008-07-11 18:47:18

Resolution changed from fixed to 


---

Attachment


---

Comment by cremona created at 2008-08-24 17:16:33

Are these patches still needed?  In 3.1.1:


```
sage: p = random_prime(2^1000, proof=False)
sage: r = Integers(p)(2)                   
sage: time 1/r
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
4182378068297747496347619509094946589859242110649682753826323779912818104926185222329257414498084527466823768975174201208996376519370243477775194265315260528263826200480626844830896267031936271294686269384932307195051185481109989133791723199020928430708397791147367704717745601696690836602407579616974
sage: %timeit 1/r
100000 loops, best of 3: 5.21 µs per loop
sage: %timeit 1/Integers(p)(2)
100000 loops, best of 3: 16.8 µs per loop
```



---

Comment by mabshoff created at 2008-08-24 17:33:38

This patch was merged in Sage 3.0.6, so I am closing it. The issue it caused to appear was related to weak references and Cython. Thanks for finding this John.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-24 17:33:38

Resolution: fixed
