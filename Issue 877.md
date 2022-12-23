# Issue 877: "sage -coverage" should not care about functions which are local to other functions/methods

Issue created by migration from https://trac.sagemath.org/ticket/877

Original creator: cwitty

Original creation time: 2007-10-13 13:47:23

Assignee: tba

Currently, if you have something like:

```
def foo():
    def bar():
        pass
    pass
```

then "sage -coverage" will complain that bar() has no docstring or doctests.  However, such functions cannot be (directly) doctested, so that warning is invalid.  In my opinion, bar() should not be required to have a docstring either.


---

Comment by mhansen created at 2008-04-04 20:26:48

To get around this, I took my local function/method and made it a regular one.  I then used functools.partial to use it.   This allowed my function to be tested like every other one.  In the few cases where I had to do this, I ended up liking the functools version better.


---

Comment by zimmerma created at 2009-02-10 07:17:18

#4323 is a duplicate of that ticket.


---

Comment by jhpalmieri created at 2009-07-24 23:53:28

Changing assignee from tba to jhpalmieri.


---

Comment by jhpalmieri created at 2009-07-24 23:53:28

Changing status from new to assigned.


---

Comment by jhpalmieri created at 2009-07-24 23:53:28

Here is a patch for this.  With sage-4.1.1.alpha0, it increases overall coverage from 77.9% to 78.5%.

To test: I know that the files steenrod_algebra_element.py and structure/factorization.py have such nested functions, so try 'sage -coverage' on these files, before and after patching.


---

Attachment

apply to scripts repository


---

Comment by jhpalmieri created at 2009-07-24 23:59:47

(Maybe it only goes from 78.0% to 78.5%.)


---

Comment by was created at 2009-07-25 00:06:48

Looks good to me:

BEFORE:

```
< Overall weighted coverage score:  77.8%
< Total number of functions:  22395
```

AFTER

```
> Overall weighted coverage score:  78.3%
> Total number of functions:  22207
```


The code looks fine and it works fine, so far as I can tell.


---

Comment by schilly created at 2009-07-25 12:21:49

quick note just from looking at the patch: i makes more sense to move the re.compile statement *before* the `while True:` loop. It's purpose is to speed up the regex searches and shouldn't be compiled in every loop! just exchange line 20 and 21 in the merged file.


---

Comment by jhpalmieri created at 2009-07-25 14:59:21

use this version instead


---

Attachment

trac_877-scripts-coverage2.patch interchanges the lines that schilly mentions.  It also moves another re.compile statement earlier.  It also stores the list of nested functions in the list "closures", for possible future use.


---

Comment by mvngu created at 2009-07-25 19:59:44

This is what I observe regarding John's patch. In Sage 4.1 without the patch `trac_877-scripts-coverage2.patch`, we have 

```
Overall weighted coverage score:  77.8%
Total number of functions:  22398
```

Applying that patch to Sage 4.1:

```
Overall weighted coverage score:  78.3%
Total number of functions:  22210
```

If I understand John's patch correctly, it doesn't count functions which are local to other functions/methods. This accounts for the reduced number of total functions after applying the patch. Moving on to Sage 4.1.1.alpha0 without the patch:

```
Overall weighted coverage score:  78.0%
Total number of functions:  22497
```

And with the patch:

```
Overall weighted coverage score:  78.5%
Total number of functions:  22308
```

Here is the coverage after applying the patch to my merge tree:

```
Overall weighted coverage score:  78.6%
Total number of functions:  22317
```



Merged `trac_877-scripts-coverage2.patch` in the scripts repository.


---

Comment by mvngu created at 2009-07-25 19:59:44

Resolution: fixed
