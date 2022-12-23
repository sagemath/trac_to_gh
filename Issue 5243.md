# Issue 5243: [with patch, needs review] non decreasing parking functions

Issue created by migration from https://trac.sagemath.org/ticket/5243

Original creator: hivert

Original creation time: 2009-02-12 13:45:37

Assignee: mhansen

CC:  sage-combinat ddrake

Keywords: parking functions / Dyck words

This patch implement the combinatorial classes of non decreassing parking function with the usual methods (counting/listing/!__contains!__/iterating)... It also implements bijections from and to Dyck words.


---

Comment by hivert created at 2009-02-12 18:39:43

Changing assignee from mhansen to nthiery.


---

Comment by hivert created at 2009-02-12 18:39:43

Nicolas is rewiewing it rigth there. I currently taking case of its remark.


---

Comment by hivert created at 2009-02-13 16:25:46

I modified my patch according to Nicolas remarks. I took the occasion to adapt this patch to the design change of patch #5255.


---

Comment by hivert created at 2009-03-01 18:23:39

Changing assignee from nthiery to hivert.


---

Comment by hivert created at 2009-03-01 18:23:39

Changing status from new to assigned.


---

Comment by hivert created at 2009-04-05 16:51:16

The patch is now rebased an finalized. Ready for review. 

Florent


---

Comment by hivert created at 2009-04-05 16:52:20

Rebased patch


---

Attachment


---

Comment by ddrake created at 2009-04-16 08:40:24

Florent, I'm working on reviewing this, and I already see a bunch of things in the docstrings that I'd like changed -- these range from grammar and usage changes to different formatting suggestions. Would you like me to list all the changes, and have you edit the patch, or should I upload a "referee patch" that changes the bits I'd like changed?

BTW, I can already say that you've got some lovely ASCII art in your docstrings!


---

Comment by hivert created at 2009-04-17 13:09:35

Hi Dan, 

Thank you for reviewing this one. It is not a very important one for the sage community, but it was my first submitted ticket and I'll be glad seeing it merged.
It will be a test-case for a future (vaporware ? :-) bijection infrastructure. 

If it's not too much work for you I'd rather you upload a referee patch, unless you have big changes. If they are a bunch on typos and presentation change, my experience is that it's not that much more work creating a new patch than explaining by trac or e-mail what you want to do. Is it ok with you ? When you say "usage changes" is this English usage and or sage usage ?

> BTW, I can already say that you've got some lovely ASCII art in your docstrings!

A picture is always clearer than a long explanation :)

Cheers,

Florent


---

Comment by ddrake created at 2009-05-06 04:08:01

I am working on reviewing this, and I have a couple questions and one larger concern. First, some questions. I'm just curious about these things:

  * what does the ``@`classmethod` decorator do?
  * why does the `keys` method return the domain of the function? It seems strange to have a `keys` method for something list-based, and not dictionary-based.

Here are my concerns:
  * Your code does not check to see if it gets a list of positive integers, so you can do `NonDecreasingParkingFunction[[0, .1, pi/3, sqrt(2)])`, yikes! Do we want to require lists of positive integers?
  * In `is_a()`, you have:

```
   for i in range(len(x)-1):
        if x[i] > x[i+1] or x[i] > i+1:
            return False
```

    Instead of iterating over indices and doing a list lookup every time, would it be faster to use Python's `enumerate` in something like this?

```
   prev = 1
   for i, elt in enumerate(x):
       if prev > elt or elt > i+1:
           return False
       prev = elt
```

    That would also let you finish the function with `return True`, since the `enumerate` loop would check the final element.

  * Right now when you give the `NonDecreasingParkingFunction` constructor a bad list, I see a strange error message:

```
sage: NonDecreasingParkingFunction([1,1,4])
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (5, 0))

---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

/home/drake/.sage/temp/klee/10186/_home_drake__sage_init_sage_0.py in <module>()

/var/tmp/sage-3.4.2/local/lib/python2.5/site-packages/sage/combinat/non_decreasing_parking_function.pyc in __init__(self, lst)
    383             [1, 1, 2, 2, 5, 6]
    384         """
--> 385         assert(is_a(lst))
    386         CombinatorialObject.__init__(self, lst)
    387         

AssertionError: 
```

  * Also, related to `is_a`: the `assert` statement should give the user some idea of what has gone wrong. I suggest changing the assert line (line 409) to `assert is_a(lst), 'list is not a non-decreasing parking function.'`. Also note that `assert` is a statement, not a function -- just like `print` before Python 3.0.
  * My biggest concern is with the getitem stuff. You are effectively shifting the list indices by 1, which really bothers me. Perhaps other people don't feel this way, and perhaps this is the best decision, but whenever I am thinking of something as a list, I _really_ want the indices to be zero-based, since that's what the rest of Sage/Python does. Right now, we have:

```
sage: f = NonDecreasingParkingFunction([1,1,2,3])
sage: f[2]
1
sage: f[3]
2
```

    When I use square brackets, I'm thinking "list index", and I really want it zero-based. Perhaps we should make these objects callable, so we can treat them like functions? I would not mind having `f(2)` be 1 and `f(3)` be 2, since the round parentheses indicate a function call, and indeed the above object f is a function that sends 3 to 2.

I'm marking this "needs work" because of the list index issue. I have a patch which fixes a bunch of tiny docstring bits which I'll upload once we have the rest of this sorted out.


---

Comment by ddrake created at 2009-05-06 04:26:00

I uploaded my documentation fixes patch, since there's no reason to keep it secret; it only fixes docstring bits (mostly it changes "non decreasing" to "non-decreasing" :) except in three places:

  * changes two "`assert(foo)`" statements to "`assert foo, 'what went wrong'`"
  * changes the `is_a()` function as I described above. If the consensus is that we should keep it the way it was, I have no problem removing this change from my patch.


---

Attachment


---

Attachment


---

Comment by mhansen created at 2009-09-26 04:19:23

Dan's changes look good to me, and I've added a patch which switches the behavior of __getitem__.  I think with these, it can go in.  Dan, do you want to sign off on the rest?


---

Comment by ddrake created at 2009-09-28 02:46:07

Looks good to me. Positive review. I think this will have to wait for 4.1.3, since 4.1.2 is now in feature freeze.


---

Comment by mhansen created at 2009-10-15 07:26:07

Merged all 3 patches.


---

Comment by mhansen created at 2009-10-15 07:26:07

Resolution: fixed
