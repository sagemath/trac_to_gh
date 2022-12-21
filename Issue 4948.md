# Issue 4948: implement the transfer of Mathematica lists back to Sage

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-01-07 03:55:28

Assignee: cwitty

CC:  jason

Make the following work:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: slist = [1,2,3]
sage: mathematica(slist) 
{1, 2, 3}
sage: list(mathematica(slist))
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
| Sage Version 3.2.3, Release Date: 2009-01-05                       |
| Type notebook() for the GUI, and license() for information.        |
/home/mabshoff/.sage/temp/sage/11670/_home_mabshoff__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __len__(self)
   1345 
   1346     def __len__(self):
-> 1347         raise NotImplementedError
   1348 
   1349     def __reduce__(self):

NotImplementedError: 
```



---

Comment by mabshoff created at 2009-01-07 05:35:01

Jason comments:

```
These are not the right way to do this, but they seem to give results 
for right now, at least until someone fixes this:

sage: a=mathematica([1,2,3])
sage: [a[i] for i in range(1,a.Length()+1)]
[1, 2, 3]

Or

sage: a=mathematica(slist)
sage: a._Expect__sage_list
[1, 2, 3]
```


Cheers,

Michael


---

Attachment


---

Comment by flawrence created at 2009-08-22 05:36:22

The patch I just attached does a little more than the scope of this ticket - it also gets mmalist.sage() working, as well as allowing import of floats with exponents (e.g. 4.5e80) from both mathematica and GP (plus it lays the groundwork for importing nonstandard exponent notation from other programs too).


---

Comment by was created at 2009-09-14 05:39:14

Great work!   I hope you'll do more to improve the Sage /Mathematica interface.  Thanks!


---

Comment by mvngu created at 2009-09-15 19:41:11

What about doctest for this function in `sage/interfaces/expect.py`?

```
1142	    def _exponent_symbol(self): 
1143	        """ 
1144	        Return the symbol used to denote *10^ in floats, e.g 'e' in 1.5e6 
1145	        """ 
1146	        return 'e' 
```



---

Comment by flawrence created at 2009-09-17 02:08:01

a further patch adding doctest for generic _exponent_symbol()


---

Comment by flawrence created at 2009-09-17 03:43:40

Changing component from misc to interfaces.


---

Comment by flawrence created at 2009-09-17 03:43:40

Changing assignee from cwitty to was.


---

Attachment

I added the requested doctest for the generic _exponent_symbol(), a method that is meant to be overloaded by each derived class (i.e. the interface to gp, mathematica, etc).  Since this is meant to be overloaded by each of the interfaces, I didn't use any existing interface in this doctest, as when _exponent_symbol() was overloaded by that interface the doctest would become misleading.  Instead I created a fake interface so that the doctest would always call the correct version of _exponent_symbol.  It's a bit messy but it's the most stable way of doctesting the function that I could think of.

The approach could be taken to write doctests for the rest of the methods in the Expect class.


---

Comment by mvngu created at 2009-09-17 08:24:26

Merged patches in this order:

 1. `trac-4948-mathematica_lists.patch`
 1. `trac-4948-mathematica_lists 12660.patch`


---

Comment by mvngu created at 2009-09-17 08:24:26

Resolution: fixed


---

Comment by flawrence created at 2009-09-23 04:04:47

N.B. the doctests introduced by the above patches fail on 32-bit systems - see #6999.
