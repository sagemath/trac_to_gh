# Issue 4588: doctest -- get rid of the "feature" where docstrings with require, optional, and package all in them are automatically marked optional

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-11-23 02:44:06

Assignee: mabshoff

This "feature" that I introduced years ago is incredibly confusing.  3 people at least got very confused by this in the last 3-4 days. 

To close this ticket:
    1. remove this functionality from local/bin/sage-*test*

    2. rewrite all the files that use this by tediously marking each optional line with #optional.   This is tedious, but it is much much clearer what is going on.  

Note -- only do this *after* apply #4583, which already does some of part 2 above. 


---

Comment by was created at 2008-11-23 02:48:07

NOTE: Some people want a 

```
# start optional
...
# end optional
```

system to allow for optional blocks. 

I'm not sure.  I think I don't like this.

One way to implement this though would be in sage-doctest when parsing the docstring if start optional appears, just mark everything # optional through to where end optional appears.  I guess.


---

Attachment

Fallout after applying the patch:


```
----------------------------------------------------------------------

The following tests failed:

        sage -t  devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 1 doctests failed
        sage -t  devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py # 1 doctests failed
        sage -t  devel/sage/sage/interfaces/matlab.py # 1 doctests failed
        sage -t  devel/sage/sage/interfaces/macaulay2.py # 1 doctests failed
        sage -t  devel/sage/sage/interfaces/octave.py # 2 doctests failed
        sage -t  devel/sage/sage/interfaces/scilab.py # 5 doctests failed
        sage -t  devel/sage/sage/interfaces/lie.py # 1 doctests failed
        sage -t  devel/sage/sage/interfaces/kash.py # 100 doctests failed
        sage -t  devel/sage/sage/interfaces/maple.py # 40 doctests failed
        sage -t  devel/sage/sage/interfaces/mupad.py # 19 doctests failed
        sage -t  devel/sage/sage/interfaces/qepcad.py # 66 doctests failed
        sage -t  devel/sage/sage/combinat/designs/incidence_structures.py # 1 doctests failed
        sage -t  devel/sage/sage/databases/sloane.py # 3 doctests failed
        sage -t  devel/sage/sage/databases/jones.py # 4 doctests failed
        sage -t  devel/sage/sage/databases/stein_watkins.py # 21 doctests failed
        sage -t  devel/sage/sage/groups/perm_gps/permgroup.py # 1 doctests failed
        sage -t  devel/sage/sage/graphs/graph_database.py # 1 doctests failed
        sage -t  devel/sage/sage/coding/linear_code.py # 4 doctests failed
----------------------------------------------------------------------
Total time for all tests: 171.8 seconds
```



---

Comment by was created at 2009-01-23 09:00:42

fix fallout in the core library.


---

Attachment


---

Attachment

The attached sage patches fix all missing # optionals after applying the scripts patch (the first one -- trac_4588-scripts.patch).  I also greatly improve the use of 

```
  # optional -- name_of_package
```

while I was at it.

However, note that this revealed some bugs in David Joyner's linear_code.py stuff.  See #5067. Thus I believe this patch should receive a positive review *despite* that after applying it suddenly four doctests will fail.   I've made #5067 a blocker.


---

Attachment


---

Comment by rlm created at 2009-01-24 13:39:30

I think that this set of patches should be merged in. They all applied cleanly to alpha0 (I don't know about alpha1), and this definitely needs to be done. I think that any remaining issues which arise once this does get merged should become their own ticket.


---

Comment by mabshoff created at 2009-01-24 15:30:38

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 15:30:38

Merged in Sage 3.3.alpha2
