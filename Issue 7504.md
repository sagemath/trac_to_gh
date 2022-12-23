# Issue 7504: Magma booleans don't evaluate correctly in boolean contexts

Issue created by migration from https://trac.sagemath.org/ticket/7504

Original creator: kedlaya

Original creation time: 2009-11-20 13:27:44

Assignee: was

Keywords: magma, boolean context

Compare the following results:

```
sage: bool(pari(False))
False
sage: bool(gap(False))
False
sage: bool(maxima(False))
False
sage: bool(maple(False))
False
sage: bool(mathematica(False))
False
sage: bool(magma(False))
True
```

This is in some sense the inverse problem to #845.


---

Comment by GeorgSWeber created at 2009-11-20 23:24:33

In "gap.py", in the "class GapElement(ExpectElement)", there is (lines 1058 ff):

```
    def bool(self):
        """
        EXAMPLES::
        
            sage: bool(gap(2))
            True
            sage: gap(0).bool()
            False
            sage: gap('false').bool()
            False
        """
        P = self._check_valid()
        return self != P(0) and repr(self) != 'false'
```

I didn't check maxima.py, ... but in magma.py, I couldn't find a counterpart in the class MagmaElement. My first attempt to add this with the obvious minor modifications failed however (so I do not post the patch):

```
sage: magma(True).bool()
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/Users/georgweber/.sage/temp/susanne_webers_computer.local/15820/_Users_georgweber__sage_init_sage_0.py in <module>()

/Users/Shared/sage/sage-4.2.1/local/lib/python2.6/site-packages/sage/interfaces/magma.pyc in bool(self)
   2111         """
   2112         P = self._check_valid()
-> 2113         return self != P(0) and repr(self) != 'false'
   2114 
   2115     def __len__(self):

/Users/Shared/sage/sage-4.2.1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__richcmp__ (sage/structure/element.c:6484)()

/Users/Shared/sage/sage-4.2.1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element._richcmp (sage/structure/element.c:6363)()

/Users/Shared/sage/sage-4.2.1/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __cmp__(self, other)
   1521         P = self.parent()
   1522         if P.eval("%s %s %s"%(self.name(), P._equality_symbol(),
-> 1523                                  other.name())) == P._true_symbol():
   1524             return 0
   1525         elif P.eval("%s %s %s"%(self.name(), P._lessthan_symbol(), other.name())) == P._true_symbol():

/Users/Shared/sage/sage-4.2.1/local/lib/python2.6/site-packages/sage/interfaces/magma.pyc in eval(self, x, strip, **kwds)
    478         ans = Expect.eval(self, x, **kwds).replace('\\\n','')
    479         if 'Runtime error' in ans or 'User error' in ans:
--> 480             raise RuntimeError, "Error evaluating Magma code.\nIN:%s\nOUT:%s"%(x, ans)
    481         return ans
    482 

RuntimeError: Error evaluating Magma code.
IN:_sage_[3] eq _sage_[6];
OUT:
>> _sage_[3] eq _sage_[6];
             ^
Runtime error in 'eq': Bad argument types
Argument types given: BoolElt, RngIntElt
```



---

Comment by GeorgSWeber created at 2009-11-20 23:32:30

Ouch, I give up after experimenting further and getting (one and the same session!):

```
sage: magma(False).bool()
False
sage: bool(magma(False))
True
```



---

Comment by mhansen created at 2009-11-21 15:27:09

` bool(f) ` calls ` f.__nonzero__() `


---

Comment by was created at 2009-11-22 22:11:25

Changing status from new to needs_review.


---

Comment by was created at 2009-11-22 22:11:25

In Magma we have:


```
> false ne 0;

>> false ne 0;
         ^
Runtime error in 'ne': Bad argument types
Argument types given: BoolElt, RngIntElt

> 1 ne 0;    
true
```


I.e., comparing false to 0 is not allowed in Magma.   So we need to add code to __nonzero__ that also tests bools.


---

Comment by kedlaya created at 2009-11-24 22:19:29

Changing status from needs_review to positive_review.


---

Attachment

This applied against 4.2, fixed the issue for me, and doesn't appear to have caused any failures of optional doctests.


---

Comment by mhansen created at 2009-11-29 05:43:36

Resolution: fixed
