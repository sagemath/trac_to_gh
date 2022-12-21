# Issue 1921: add random_element to groups

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-01-25 06:09:48

Assignee: joyner

Currently, at least some of the groups G in SAGE access a random
element using G.random(). (This was borrowed from GAP's syntax.) 
The default for a ring R in SAGE seems to be R.random_element(). 
The function call should be the same in both cases, 
so for now add G.random_element() and in the future maybe deprecate
G.random().



---

Comment by was created at 2008-01-25 06:24:14

I greatly prefer random_element to random.  I think random is unclear about what it does, and of course inconsistent.  random_element is crystal clear.  I also use to use random in various places, since in Magma the command is `Random`. 

There are current 28 instances of the random function in Sage:

```
sage: search_src('def random(')
```


There are 36 instances of random_element.

```
sage: search_src('def random_element(')
```


It would make the most sense to remove all the random(...) methods and
replace them by random_element throughout.  If we make all the random(...)
methods do a 

```
    raise Deprecated
```

then I hope those really do disappear completely within 2 months (say). ??


---

Attachment

doc patch


---

Comment by AlexGhitza created at 2008-04-17 02:36:38

The attached patch renames all .random() methods to random_element() and adds a NotImplementedError deprecated message to .random().

This change messes up a doctest in the tutorial, so there is also a small doc patch for that.


---

Attachment


---

Comment by mhansen created at 2008-04-26 02:26:41

I fixed a few things up in the combinat/ directory.

Other than that, looks good to me.  Apply the last two patches.


---

Comment by mabshoff created at 2008-04-26 02:49:16

Resolution: fixed


---

Comment by mabshoff created at 2008-04-26 02:49:16

Merged 1921-doc.patch and 1921-1.patch in Sage 3.0.1.alpha0
