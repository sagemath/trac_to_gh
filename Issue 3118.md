# Issue 3118: update LCM (easy-to-fix buglet)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-05-07 04:00:56

Assignee: somebody

CC:  cremona


```


On Tue, May 6, 2008 at 8:49 PM, schmmd <schmmd`@`gmail.com> wrote:
> 
>  lcm? gives the following output:
>  
>  Type:           function
>  Base Class:     <type 'function'>
>  String Form:    <function lcm at 0x879087c>
>  Namespace:      Interactive
>  File:           /home/michael/downloads/sage-3.0/local/lib/python2.5/
>  site-packages/sage/rings/arith.py
>  Definition:     lcm(a, b=None, integer=False)
>  Docstring:
>  
>         The least common multiple of a and b, or if a is a list and b
>  is
>         omitted the least common multiple of all elements of a.
>  
>         NOTE: Use integer=True to make this vastly faster if you are
>         working with lists of integers.
>  
>         INPUT:
>             a -- number
>             b -- number (optional)
>             integer -- (default: False); if True, do an integer LCM
>         or
>   *           a -- vector
>             integer -- (default: False); if True, do an integer LCM
>                 NOTE -- this is *vastly* faster than doing the generic
>  LCM
>  
>  Note the starred line.  I believe that the lcm method takes a list and
>  not a vector.  At least, I seem to get errors when I pass a vector.
>  
>  

I fully agree that this is a bug.

Incidentally I wrote the LCM function a while before I implemented vectors,
so I think when I wrote those docs "vector" and "list" were the same
thing in my mind.  

The fix should be to change the docs to replace "vector" by any itterable.
Then the LCM code should iterate over the object calling LCM 
if it doesn't have an LCM method.   

Probably similar fixes need to be made for GCD.
```



---

Attachment


---

Comment by zimmerma created at 2008-10-19 13:42:17

Both attachments fix that problem. Btw, I wonder why integer=True is not the default,
at least for integer inputs. I guess there are many calls to gcd with integers in the
Sage library without Integer=True:

```
bash-3.00$ pwd
/usr/local/sage-3.1.4/sage/devel/sage/sage
bash-3.00$ find . -type f -name "*.py" -exec grep \-iw GCD {} \; | wc -l
297
```



---

Attachment

My patch applies _instead_ of the previous two.  It implements Paul's suggested behaviour.

There's one problem left (I tested all of sage.rings and had to make one change in the multiploynomial polynomial code which actually used the integers=True flag which is now redundant).  But:

```
sage: P.<x,y,z> = ZZ[]
sage: gcd(2*(x+y),3*y)
2
```

which of course should give 1.  This leads to one doctest failure, but I cannot track it down at the moment.

I (or someone) should also doctest all the rest of Sage as there are ceratinly places where gcd/lcm are used outside of sage/rings.


---

Comment by cremona created at 2008-10-22 14:15:39

Apply after previous one


---

Attachment

The second patch does three things:

    1. After running -testall a couple of small things elsewhere needed fixing;
    2. Fixed a bug in integer.pyx introduced in 3.1.2.alpha0 (in #4286)
    3. Cleaner use of sequences as a method of coercing a list to have a coherent universe.

In view of item 2, which corrected this:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.2.alpha0, Release Date: 2008-10-20                  |
| Type notebook() for the GUI, and license() for information.        |
sage: sage.rings.integer.GCD_list([2,2,3])
2
```

and the fact that I really did do a -testall, I am hoping for a quick positive review!  I think that Paul Z is eligible to do that although the initial patches here were his.


---

Comment by zimmerma created at 2008-10-23 16:22:22

I tried to apply both patches to 3.1.4 but the 2nd one failed:

```
fleur% hg import sage-trac_3118.patch 
applying sage-trac_3118.patch
fleur% hg import sage-trac_3118-2.patch
applying sage-trac_3118-2.patch
patching file sage/rings/integer.pyx
Hunk #1 FAILED at 3595
Hunk #3 FAILED at 3649
2 out of 3 hunks FAILED -- saving rejects to file sage/rings/integer.pyx.rej
abort: patch failed to apply
```

Should I apply another patch before?


---

Comment by mabshoff created at 2008-10-23 16:24:45

Hi Paul,

this patch series requires at least #4286. It should apply fine on top of 3.2.alpha0.

Cheers,

Michael


---

Comment by GeorgSWeber created at 2008-10-23 18:16:54

Hi,

positive review for the "integer.pyx" corrections in "sage-trac_3118-2.patch", which heal two issues introduced in #4286.
(One horrible bug with a new doctest to show it is fixed now, and one for beauty: make the gcd of a list consisting of one single negative number be a positive number, so that all resulting integers of a gcd calculation are non-negative now --- as long as this holds for the underlying GMP algorithm used.)

Cheers,
gsw


---

Comment by cremona created at 2008-10-23 22:16:47

Georg is right -- I made that change so that gcd((-2,)) returns 2 and similarly for lcm.  And the patches were based on 3.2.alpha0 -- sorry Paul.


---

Comment by zimmerma created at 2008-10-24 16:06:04

I tried all the above examples which work as expected, and also did sage -t in the rings
directory. Since John already did sage -testall, I give a positive review.


---

Comment by mabshoff created at 2008-10-25 22:41:19

Resolution: fixed


---

Comment by mabshoff created at 2008-10-25 22:41:19

Merged sage-trac_3118.patch and sage-trac_3118-2.patch in Sage 3.2.alpha1
