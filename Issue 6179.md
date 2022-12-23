# Issue 6179: html -- doctest failure in sage-4.0.1.alpha0

Issue created by migration from https://trac.sagemath.org/ticket/6179

Original creator: was

Original creation time: 2009-06-01 14:37:18

Assignee: tbd

We have the following on 32-bit OS X Intel:


```
sage -t -long "devel/sage/sage/misc/html.py"
**********************************************************************
File "/Users/was/build/sage-4.0.1.alpha0/devel/sage/sage/misc/html.py", line 157:
    sage: html.table([(i, j, i == j) for i in [0..1] for j in [0..1]])
Expected:
    <html>
    <div class="notruncate">
    <table class="table_form">
    <tbody>
    <tr class ="row-a">
    <td><span class="math">0</span></td>
    <td><span class="math">0</span></td>
    <td><span class="math">True</span></td>
    </tr>
    <tr class ="row-b">
    <td><span class="math">0</span></td>
    <td><span class="math">1</span></td>
    <td><span class="math">False</span></td>
    </tr>
    <tr class ="row-a">
    <td><span class="math">1</span></td>
    <td><span class="math">0</span></td>
    <td><span class="math">False</span></td>
    </tr>
    <tr class ="row-b">
    <td><span class="math">1</span></td>
    <td><span class="math">1</span></td>
    <td><span class="math">True</span></td>
    </tr>  
    </tbody>
    </table>
    </div>
    </html>
Got:
    <html>
    <div class="notruncate">
    <table class="table_form">
    <tbody>
    <tr class ="row-a">
    <td><span class="math">0</span></td>
    <td><span class="math">0</span></td>
    <td><span class="math">\mbox{\rm True}</span></td>
    </tr>
    <tr class ="row-b">
    <td><span class="math">0</span></td>
    <td><span class="math">1</span></td>
    <td><span class="math">\mbox{\rm False}</span></td>
    </tr>
    <tr class ="row-a">
    <td><span class="math">1</span></td>
    <td><span class="math">0</span></td>
    <td><span class="math">\mbox{\rm False}</span></td>
    </tr>
    <tr class ="row-b">
    <td><span class="math">1</span></td>
    <td><span class="math">1</span></td>
    <td><span class="math">\mbox{\rm True}</span></td>
    </tr>
    </tbody>
    </table>
    </div>
    </html>
**********************************************************************
1 items had failures:

```



---

Comment by was created at 2009-06-04 00:08:53

NOTE: The expected values are *wrong*.  Math typesetting of bools should use \mbox{\rm ...}.


---

Comment by whuss created at 2009-06-04 08:29:39

On my 32-bit Debian with sage-4.0.1.alpha0:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: latex(True)
True
sage: latex(False)
False
```

| Sage Version 4.0.1.alpha0, Release Date: 2009-05-31                |
| Type notebook() for the GUI, and license() for information.        |
and also:


```
$ ./sage -t devel/sage/sage/misc/html.py
sage -t  "devel/sage/sage/misc/html.py"
         [1.1 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 1.1 seconds
```



---

Comment by mhansen created at 2009-06-05 21:21:49

Changing status from new to assigned.


---

Attachment

This issue is that


```
sage: isinstance(True, int)
True
sage: isinstance(True, bool)
True
sage: isinstance(1, bool)
False
```


so the output depended on the order in which items of the latex_table dict were iterated.  This is fixed by changing latex_table to a list so that bool comes first.


---

Comment by mhansen created at 2009-06-05 21:21:49

Changing assignee from tbd to mhansen.


---

Comment by jhpalmieri created at 2009-06-05 21:57:31

Here's another possible fix for the latex_table issue:

``` 
        try:
            f = latex_table[type(x)]
            return LatexExpr(f(x))
        except KeyError:
            if x is None:
                return LatexExpr("\\mbox{\\mathrm{None}}")
            return LatexExpr(str_function(str(x)))
```

Since `type(True)` returns `bool`, this looks up the right thing.  Is this approach better or worse than the one in your patch?  

The try/except approach helps to avoid accidental lookups in the table, but were those being used intentionally for anything?  For example, does `isinstance(blah, int)` return True for other classes that we care about for typesetting?  I tend to think that we should be more explicit rather than implicit (so add more entries `new-type: str` if we want more types to behave the way ints do), so I would favor the dictionary lookup approach.  I could be convinced otherwise, though.


---

Comment by mhansen created at 2009-06-05 22:03:18

I have no strong feelings on this; your patch is a tad more efficient, but none of this is really time critical. The latex_table should really only be used for builtin types though; anything else would be coupling things too much.


---

Comment by jhpalmieri created at 2009-06-05 22:19:45

I don't care about the efficiency, but I like that my patch is less ambiguous: with yours, if some unexpected type returns True for `isinstance(blah, int)`, then the latex could get screwed up.  It also depends on the ordering in the table.  My change was already in a patch ("needs work") for #6089, and in that patch it also gets used when constructing jsmath expressions.  So if you don't have a strong preference, I'll post my version of the patch here.

This includes your changes to html.py and your new doctest in latex.py, which I give a positive review to.


---

Comment by jhpalmieri created at 2009-06-05 22:20:07

apply only this patch


---

Attachment

Looks good to me.


---

Comment by mhansen created at 2009-06-06 00:09:55

Resolution: fixed


---

Comment by mhansen created at 2009-06-06 00:09:55

Merged in 4.0.1.rc3.
