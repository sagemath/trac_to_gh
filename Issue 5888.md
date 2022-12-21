# Issue 5888: quadratic forms added a stupid/broken new function to sage for random integer.  Remove!

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-24 06:53:32

Assignee: somebody

CC:  cremona


```


On Thu, Apr 23, 2009 at 11:51 PM, Bill Hart <goodwillhart`@`googlemail.com> wrote:
> Yeah, the random_int_upto function looks broken.
> random_int_upto(2^100) is always divisible by 2^47. Not very random.


I've never heard of that function, and expected it to be something you defined.
I was surprised to find it is in Sage.

This was some weird crap that Jon Hanke just added to Sage in his big patch (bomb), evidently.

File:		/Users/wstein/build/sage-3.4.1/local/lib/python2.5/site-packages/sage/quadratic_forms/extras.py
Definition:	random_int_upto(n)
Source:
def random_int_upto(n):
    """
    Returns a random integer x satisfying 0 <= x < n.

    EXAMPLES:
        sage: x = random_int_upto(10) 
        sage: x >= 0
        True
        sage: x < 10
        True
    """
    return floor(n * random())
```



---

Comment by mabshoff created at 2009-04-24 07:04:51

Well, random() returns a python float, so *boom* for anything large. That function should get a max size check, get deprecated and use generic infrastructure. 

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-24 10:53:17

John Cremona fixes this at #5834.

Cheers,

Michael


---

Comment by jonhanke created at 2009-04-25 16:40:15

Changing status from new to assigned.


---

Comment by jonhanke created at 2009-04-25 16:40:15

Changing assignee from somebody to jonhanke.


---

Comment by mabshoff created at 2009-05-04 18:16:52

Resolution: fixed


---

Comment by mabshoff created at 2009-05-04 18:16:52

This has been fixed in Sage 4.0.alpha0 via #5834.

Cheers,

Michael
