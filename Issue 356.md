# Issue 356: add a general number field sieve to SAGE

Issue created by migration from https://trac.sagemath.org/ticket/356

Original creator: was

Original creation time: 2007-04-25 14:28:27

Assignee: was

SAGE should include a usable implementation of the number field sieve, say for factoring integers with up to 140 digits in a few days (??).  

Michael points this one out, which looks like a potentially
good choice to me:

```

A while ago on this list it was asked if there were open source
implementations
of the GNFS for possible inclusion into sage. I came accros these
links

http://www.math.ttu.edu/~cmonico/software/ggnfs/

```



---

Comment by davidloeffler created at 2009-07-20 20:00:28

Changing component from number theory to factorization.


---

Comment by davidloeffler created at 2009-07-20 20:00:28

Changing assignee from was to tbd.


---

Comment by aapitzsch created at 2010-11-11 15:31:26

Instead of ggnfs one could use msieve (#5310) or both together (see http://gladman.plushost.co.uk/oldsite/computing/factoring.php)
