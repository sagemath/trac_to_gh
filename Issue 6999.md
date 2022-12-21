# Issue 6999: [with patch, needs review] doctest failures on 32-bit systems due to #4948 patches

Issue created by migration from Trac.

Original creator: flawrence

Original creation time: 2009-09-23 04:00:14

Assignee: flawrence

Some doctests added in the patches for #4948 fail on 32-bit systems:

```
sage -t -long "devel/sage/sage/interfaces/expect.py" 
********************************************************************** 
File "/space/wstein/farm/sage-4.1.2.alpha2/devel/sage/sage/interfaces/expect.py" , 
line 1599: 
    sage: gp(10.^80)._sage_repr() 
Expected nothing 
Got: 
    '1.000000000000000000000000000e80' 
********************************************************************** 
1 items had failures: 
   1 of   3 in __main__.example_45 
***Test Failed*** 1 failures. 
For whitespace errors, see the file 
/space/wstein/farm/sage-4.1.2.alpha2/tmp/.doctest_expect.py 
         [17.4 s] 
sage -t -long "devel/sage/sage/interfaces/all.py" 
         [0.1 s] 
sage -t -long "devel/sage/sage/interfaces/rubik.py" 
         [37.8 s] 
sage -t -long "devel/sage/sage/interfaces/gp.py" 
********************************************************************** 
File "/space/wstein/farm/sage-4.1.2.alpha2/devel/sage/sage/interfaces/gp.py", 
line 567: 
    sage: repr(gp(10.^80)).replace(gp._exponent_symbol(), 'e') 
Expected nothing 
Got: 
    '1.000000000000000000000000000e80' 
********************************************************************** 
1 items had failures: 
   1 of   4 in __main__.example_26 
***Test Failed*** 1 failures. 
For whitespace errors, see the file 
/space/wstein/farm/sage-4.1.2.alpha2/tmp/.doctest_gp.py 
         [3.5 s] 
---------------------------------------------------------------------- 
```




---

Attachment

Works ok for me on 32 bit. So positive review.

Jaap


---

Comment by mvngu created at 2009-09-24 07:18:40

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 09:59:43

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
