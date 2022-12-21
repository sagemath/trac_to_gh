# Issue 4755: CremonaDatabase().number_of_curves() should work when the optional database isn't installed.

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-12-11 04:27:42

Assignee: cwitty


```
sage: CremonaDatabase().number_of_curves()
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)

/home/mike/.sage/temp/mike_laptop/12400/_home_mike__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/opt/sage/local/lib/python2.5/site-packages/sage/databases/cremona.pyc in number_of_curves(self, N, i)
    680         """
    681         if N == 0:
--> 682             return self['number_of_curves']
    683         C = self.allcurves(N)
    684         if i == 0:

/opt/sage/local/lib/python2.5/site-packages/sage/databases/cremona.pyc in __getitem__(self, N)
    345         if isinstance(N, str) and len(N) > 0:
    346             if N[0].isalpha():
--> 347                 return sage.databases.db.Database.__getitem__(self, N)
    348             else:
    349                 return self.elliptic_curve(N)

/opt/sage/local/lib/python2.5/site-packages/sage/databases/db.pyc in __getitem__(self, x)
    258         try:
    259             if not isinstance(x, slice):
--> 260                 return self.root[x]
    261             return [self[k] for k in range(x.start, x.stop, x.step)]
    262         except AttributeError:

KeyError: 'number_of_curves'
```



---

Comment by AlexGhitza created at 2009-01-23 08:53:05

Same issue with number_of_isogeny_classes().


---

Comment by AlexGhitza created at 2009-01-23 09:23:34

The attached patch fixes the two issues, as well as a number of smaller issues that I noticed while looking through cremona.py.


---

Attachment

Looks and works good for me. Lots of other documentation and other typo fixes too.


---

Comment by mabshoff created at 2009-01-24 19:55:15

Merged in Sage 3.3.alpha2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 19:55:15

Resolution: fixed
