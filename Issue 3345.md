# Issue 3345: trace no longer works in 3.0.2

Issue created by migration from Trac.

Original creator: fwclarke

Original creation time: 2008-05-31 22:01:56

Assignee: cwitty

Keywords: trace


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: trace('2 + 2')
> <string>(1)<module>()
(Pdb) s
--Return--
> <string>(1)<module>()->4
(Pdb) s
4
```

But now

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.1, Release Date: 2008-05-05                       |
| Type notebook() for the GUI, and license() for information.        |
| SAGE Version 3.0.2, Release Date: 2008-05-24                       |
| Type notebook() for the GUI, and license() for information.        |
sage: trace('2 + 2')
> <string>(1)<module>()
(Pdb) s
NameError: "name 'Integer' is not defined"
> <string>(1)<module>()
(Pdb) s
--Return--
> <string>(1)<module>()->None
(Pdb) s
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/Users/mafwc/<ipython console> in <module>()

/Users/mafwc/sage-3.0.2/local/lib/python2.5/site-packages/sage/misc/trace.py in trace(code, preparse)
     41     """
     42     code = preparser.preparse(code)
---> 43     return pdb.runeval(code)
     44 
     45     # this could also be useful; it drops

/Users/mafwc/sage-3.0.2/local/lib/python2.5/pdb.py in runeval(expression, globals, locals)
   1144 
   1145 def runeval(expression, globals=None, locals=None):
-> 1146     return Pdb().runeval(expression, globals, locals)
   1147 
   1148 def runctx(statement, globals, locals):

/Users/mafwc/sage-3.0.2/local/lib/python2.5/bdb.py in runeval(self, expr, globals, locals)
    383         try:
    384             try:
--> 385                 return eval(expr, globals, locals)
    386             except BdbQuit:
    387                 pass

/Users/mafwc/<string> in <module>()

NameError: name 'Integer' is not defined
}}} 

It seems that in 3.0.2 nothing is defined inside trace.




---

Attachment


---

Comment by mhansen created at 2008-06-10 04:07:53

I've attached a patch which grabs the interpreters namespace from IPython and passes it in as the globals to pdb.runeval.  I'm not sure why trace worked before / why it's not working now though.


---

Comment by mhansen created at 2008-06-10 04:07:53

Changing status from new to assigned.


---

Comment by mhansen created at 2008-06-10 04:07:53

Changing assignee from cwitty to mhansen.


---

Comment by fwclarke created at 2008-06-10 07:55:29

With the patch `trace('2 + 2')` works now, but strangely each instance of trace seems to start by recalling the last : 

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: fwc
sage: trace('2 + 2')
> <string>(1)<module>()
(Pdb) s
--Return--
> <string>(1)<module>()->4
(Pdb) s
4
sage: trace('2 + 2')
> <string>(1)<module>()->4
(Pdb) s
--Return--
> <string>(1)<module>()->4
(Pdb) s
4
sage: trace('3 + 3')
> <string>(1)<module>()->4
(Pdb) s
--Return--
> <string>(1)<module>()->6
(Pdb) s
6
sage: trace('3 + 3')
> <string>(1)<module>()->6
(Pdb) s
--Return--
> <string>(1)<module>()->6
(Pdb) s
6
```

| SAGE Version 3.0.2, Release Date: 2008-05-24                       |
| Type notebook() for the GUI, and license() for information.        |
And there are still some things `trace` can't do:


```
sage: trace("P.<y> = QQ[]")
------------------------------------------------------------
   File "<string>", line 1
     P = QQ['y']; (y,) = P._first_ngens(Integer(1))
       ^
SyntaxError: invalid syntax
```

But there's no problem with

```
sage: P = QQ['y']; (y,) = P._first_ngens(Integer(1))
sage: P
Univariate Polynomial Ring in y over Rational Field
sage: P == parent(y)
True
```



---

Comment by mhansen created at 2008-06-15 21:20:11

Why did this get positive review? It looks broken.


---

Comment by craigcitro created at 2008-06-20 04:58:14

Changing keywords from "trace" to "trace, editor_mhansen".


---

Attachment


---

Comment by mhansen created at 2008-07-15 21:29:49

I don't know what's going on recalling the last value produced by trace, but that seems to be something within pdb.  Trace has never worked on (and probably shouldn't) work on statements (like assignment ones) -- only on expressions.


---

Attachment

done while refereeing.


---

Comment by was created at 2008-07-21 18:20:22

While refereeing trac_3345.patch I:
   1. fix the issue with running assignments, and 
   2. added some mean serious doctests
   3. Added a proper error message when one uses trace in the notebook


---

Comment by was created at 2008-07-21 18:23:29

To apply this patch you should apply trac_3345.patch and trac_3345-part2.patch


---

Comment by mabshoff created at 2008-07-21 19:44:43

When applying the two patches William recommended I am seeing the following failure on sage.math:

```
sage -t -long devel/sage/sage/misc/trace.py    
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.6.alpha1/tmp/trace.py", line 49:
    sage: print s.before
Expected:
    /rings/arith.py(...)factor()
    ...
    ipdb> c
    2 * 5
    <BLANKLINE>
Got:
    -3.0.6.alpha1/local/lib/python2.5/site-packages/
**********************************************************************
1 items had failures:
   1 of   9 in __main__.example_1
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.6.alpha1/tmp/.doctest_trace.py
         [3.8 s]
exit code: 1024
```


Am I doing something wrong?

Cheers,

Michael


---

Attachment


---

Attachment


---

Comment by mhansen created at 2008-07-21 22:53:11

Positive review for all four trac_3345* patches.


---

Comment by mabshoff created at 2008-07-21 22:56:34

Merged trac_3345.patch, trac_3345-part2.patch, trac_3345-part3.patch and
trac_3345-part4.patch in Sage 3.0.6.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-21 22:56:34

Resolution: fixed
