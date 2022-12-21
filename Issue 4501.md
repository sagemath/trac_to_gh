# Issue 4501: preparser does not know about python notation for complex numbers

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-11-12 16:57:58

Assignee: somebody


```
sage: 1j
------------------------------------------------------------
   File "<ipython console>", line 1
     Integer(1)j
               ^
SyntaxError: invalid syntax
```


but in python:


```
sage: preparser(False)
sage: 1j
1j
sage: type(1j)
<type 'complex'>
```


Note that this does work now:


```
sage: 1rj
1j
sage: 1rj == complex('j')
True
```





---

Comment by jason created at 2008-11-12 17:02:03

According to [http://docs.python.org/reference/lexical_analysis.html#id7](http://docs.python.org/reference/lexical_analysis.html#id7), python supports imaginary numbers being declared as:

imagnumber ::=  (floatnumber | intpart) ("j" | "J")


---

Comment by jason created at 2008-11-12 17:03:33


```
[10:57] <mhansen> jason-: I don't have time to make a patch now, but the following two lines around line 805 in sage/misc/preparser.py are the correct fix if we want 1j to return a <type 'complex'>:
[10:57] <mhansen>                 elif i < len(line) and line[i] == 'j':
[10:57] <mhansen>                     pass
[10:57] <jason-> I can make a quick patch
[10:57] <jason-> It needs to support "J"
[10:57] <jason-> and also work for floating numbers too
[10:58] <jason-> and then there's the issue of if we want to construct Sage complex numbers instead of python complex numbers
```



---

Comment by jason created at 2008-11-12 17:05:37

and the next line:


```
[10:58] <mhansen> Just change == "j" to in 'jJ'
```



---

Comment by robertwb created at 2008-11-12 18:26:23

I think 1j should be a Sage complex number.


---

Comment by was created at 2008-11-13 01:35:37

> I think 1j should be a Sage complex number. 

And I think it should return a Python complex number. :-)


---

Comment by robertwb created at 2008-11-13 02:21:27

Your reasoning (that the userbase for this feature is almost entirely numeric users) has convinced me.


---

Comment by robertwb created at 2009-01-24 11:42:39

Resolution: duplicate


---

Comment by robertwb created at 2009-01-24 11:42:39

See #5079
