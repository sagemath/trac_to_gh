# Issue 4905: convert sage.coding.* docstrings to Sphinx

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-01-01 22:46:55

Assignee: tba




---

Attachment


---

Comment by wdj created at 2009-01-02 03:29:40

Will the table in sd_codes.py which the patch indicats is 


```
 	166	    n 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 B_n 1 1 1 2 2 3 4 7 9 
 	167	    16 25 55 103 261 731 
```

actually print in the docstring as


```
 	n  2 4 6 8 10 12 14 16 18 20 22 24  26  28  30 
       B_n 1 1 1 2  2  3  4  7  9 16 25 55 103 261 731 
```

?


---

Comment by mhansen created at 2009-01-02 03:35:14

Nope, thanks for catching that.  I've attached a patch which fixes that.


---

Comment by wdj created at 2009-01-02 10:37:04

Thanks. Can we read the html or pdf output somewhere or is it possible to generate it ourselves after applying the patch?


---

Comment by mhansen created at 2009-01-02 10:42:16

You can read the html output at http://sage.math.washington.edu/home/mhansen/sage-3.2.3-sage.math-only-x86_64-Linux/devel/sage/doc/output/html/en/reference/index.html  There's a few things I need to do before the patch to build the docs is ready.


---

Comment by wdj created at 2009-01-02 11:15:19

That helps a lot.

Here are some more typos:

 * In the section on assmus_mattson_designs:


```
s = |{ i | A_i^* \not= 0, 0<i\leq n-t}|
```

does not output the math correctly. Maybe 


```
$s = |\{ i\ |\ A_i^* \not= 0,\ 0<i\leq n-t\}|$
```

would be better?

Also,


```
 	771	        (1) If `Ai\not= 0` and 
 	772	        `d\leq i\leq n then Ci = { c in C | wt(c) = i}` holds a 
 	773	        simple t-design. 
	774	         
 	775	        (2) If `Ai*\not= 0` and 
 	776	        `d*\leq i\leq n-t then Ci* = { c in C* | wt(c) = i}` 
 	777	        holds a simple t-design. 
```

should maybe be (maybe add a "math::" somewhere?)


```
 	771	        (1) If `Ai\not= 0` and 
 	772	        `d\leq i\leq n` then `C_i = \{ c \in C\ |\ wt(c) = i\}` holds a 
 	773	        simple t-design. 
	774	         
 	775	        (2) If `Ai*\not= 0` and 
 	776	        `d*\leq i\leq n-t` then `C_i^* = \{ c \in C*\ |\ wt(c) = i\}` 
 	777	        holds a simple t-design. 
```

and


```
 	793	        `B = \{supp(c) | c in C_i\}` is the set of supports of the 
```

should be


```
 	793	        `B = \{supp(c)\ |\ c \in C_i\}` is the set of supports of the 
```


 * In automorphism_group_binary_code,


```
 	701	                     \{ g in S_n\ |\ g(c) \in C, \forall c\in C\},  
```

should be

```
 	701	                     \{ g \in S_n\ |\ g(c) \in C, \forall c\in C\},  
```


What else needs to be done to review this?


---

Attachment

I've updated the second patch to take care of these.


---

Comment by was created at 2009-01-03 04:44:45

This happens a few times in the diff:

```
BEFORE:
356	 	    provided 0 < delta < 1-1/q. 
AFTER: 	 
 	416	    provided 0 delta 1-1/q. 
```


Notice that the < "less than" signs are just deleted.


---

Comment by was created at 2009-01-03 04:47:06

This is worrisome:

```
BEFORE:
4	4	AUTHOR: 
5	 	    -- David Joyner (2007-05): initial version 
6	 	    --    "         (2008-02): added cyclic codes, Hamming codes 
7	 	    --    "         (2008-03): added BCH code, LinearCodeFromCheckmatrix,   
```



```
AFTER:
 	6	- David Joyner (2007-05): initial version 
 	7	 
 	8	- " (2008-02): added cyclic codes, Hamming codes 
 	9	 
 	10	- " (2008-03): added BCH code, LinearCodeFromCheckmatrix, ReedSolomonCode, WalshCode, 
 	11	  DuadicCodeEvenPair, DuadicCodeOddPair, QR codes (even and odd) 
 	12	 
```


It seems like AUTHOR: doesn't get changed to AUTHOR::.  Also, I'm worried about the -'s making a correct list, but maybe I shouldn't be.


---

Attachment

These patches look good to me. 

I've forgotten now what exactly is involved in giving this a positive review beyond just looking them over, but this looks like it should go in to me.


---

Attachment


---

Comment by mabshoff created at 2009-02-24 18:58:39

Resolution: fixed


---

Comment by mabshoff created at 2009-02-24 18:58:39

Merged in Sage 3.4.alpha0.

Cheers,

Michael
