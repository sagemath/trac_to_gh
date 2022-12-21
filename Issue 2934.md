# Issue 2934: doctesting files outside of sage repo is completely broken!!

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-15 16:49:11

Assignee: failure


```


On Tue, Apr 15, 2008 at 9:11 AM, Jason Bandlow <jbandlow`@`gmail.com> wrote:
> 
>  Hello all,
>  
>  Regarding doctesting, I'd like to work with the following setup:
>  1. Create a file work.sage (or work.py) somewhere in my home directory.
>  2. Start a notebook session, and attach work.sage.
>  3. Use the notebook for generating and staring at data, while using a
>  text editor to modify my code.
>  4. Periodically run: $ sage -t work.sage      to make sure that I
>  haven't completely fouled things up.
>  
>  Step 4 seems not to work (on Sage 2.11 on Ubuntu).  For example,
>  I created the following file, foo.py, in my ~/.sage directory:
>  
>  def foo(x):
>     r"""
>     Shows how doctests don't work.
>  
>     EXAMPLES:
>         sage: 2+2
>         5
>         sage: foo(3)
>         4
>     """
>     print(x)
>  
>  And then
>  $ sage -t --verbose ~/.sage/foo.py
>  
>  ----------------------------------------------------------------------
>  All tests passed!
>  Total time for all tests: 0.0 seconds
>  
>  $ sage -coverage ~/.sage/foo.py
>  ----------------------------------------------------------------------
>  foo.py
>  SCORE foo.py: 100% (1 of 1)
>  ----------------------------------------------------------------------
>  
>  
>  Can someone explain to me what's going on here?

Somebody (I don't want to name names; maybe it is me?) has completely
broken doctesting of user files, evidently.   There has
been a lot of changes made to the doctesting system
recently, and I don't know which thing caused the
above very serious problems.    Even doctesting a pure
.py file is broken!

teragon:.sage was$ more foo.py 
def foo(x):
   r"""
   Shows how doctests don't work.

   EXAMPLES:
       sage: 2+2
       5
       sage: foo(3)
       4
   """
   print(x)

teragon:.sage was$ sage -t foo.py
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 0.0 seconds


 -- William
```



---

Comment by mhansen created at 2008-04-15 17:43:12

I can only reproduce this when the .py file is in a directory starting with a "."


---

Comment by was created at 2008-04-15 19:31:32

mhansen -- you're right, this problem only occurs when the filename is in a directory starting with a .dot.  E.g., in my test above I was in $HOME/.sage.


---

Comment by was created at 2008-04-20 17:18:16

apply this to the hg_scripts repo.


---

Attachment

The attached patch scripts-2934.patch enables doctesting in hidden directories.  This used to be disabled since we kept lots of temp data in ./doctest -- but now we don't do to some nice changes
made by Timothy Abbot.


---

Comment by mhansen created at 2008-04-21 02:33:21

Looks good to me and fixes the problem.


---

Comment by mabshoff created at 2008-04-21 02:51:15

Resolution: fixed


---

Comment by mabshoff created at 2008-04-21 02:51:15

Merged in Sage 3.0.rc1
