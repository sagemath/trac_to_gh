# Issue 628: Make binomial(x,m) work for symbolic expressions when x-m is an integer

Issue created by migration from https://trac.sagemath.org/ticket/628

Original creator: pdenapo

Original creation time: 2007-09-09 14:57:10

Assignee: somebody

Currently binomial(x,m) works for symbolic expressions if m is integer, for example

[[[ 
sage: n=var('n')
sage: binomial(n,2)
(n - 1)*n/2 
]]]
 
but binomial (n,n-2) or binomial(n+1,n-1) does not work. 

I'm submitting a patch for making this work, by defining 

binomial(x,m) = binomial (x,x-m)

when x-m is an integer. 

This would be consistent with the way  in which maxima handles the binomial function
(see http://maxima.sourceforge.net/docs/manual/en/maxima_31.html#SEC126)

Note that the proposed rule makes sense when x is an integer. However, Sage does not have
a way to specify a domain for a symbolic variable (as for example Axiom does).


---

Attachment


---

Comment by mabshoff created at 2007-09-09 18:02:13

This seems pretty nice, it has doctests, so let's shoot for 2.8.4.2.

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-09 18:02:35

Changing assignee from somebody to was.


---

Comment by jbmohler created at 2007-09-10 12:33:48

Yes, I'll referee this patch...and comment after I'm done.


---

Comment by dmharvey created at 2007-09-10 18:39:54

I'm slightly concerned about overheads on this one. By far the most common case for binomials is integer arguments. Already PARI beats Magma on the actual hard part of the computation, e.g.


```
> time for i := 1 to 10000 do x := Binomial(500, 250); end for;  
Time: 1.550
```


```
sage: time for i in range(10000): x = binomial(500, 250)
Wall time: 0.52
```


BUT the overheads are already an issue for smaller problems:

```
> time for i := 1 to 100000 do x := Binomial(20, 13); end for; 
Time: 0.070
```


```
sage: time for i in range(100000): x = binomial(20, 13)
Wall time: 2.82
```


Perhaps this should be a new ticket, "add fast pathway for binomials of integer arguments"?


---

Comment by jbmohler created at 2007-09-10 20:32:11

I import'ed this patch and made a few tweaks to the doc-string.

* Doc-tests pass
* Speed does not suffer for the "fast path" integer case (and I can't see why it should from the changes)

The only thing that gives me cause for pause is
sage: binomial(5/2,3/2)
5/2
but that only potential complaint is that this should be undefined so I don't think this is a big issue.  You could have already done similar tricks with symbolic inputs and substitution.

dmharvey's speed comments are legit, but are not affected by this patch and are not at all unique to this function.  I'm going to write sage-devel about that.

I've attached my patches with revised doc-strings and they pass my referee inspection.

--
Joel


---

Comment by jbmohler created at 2007-09-10 20:34:09

Oops, sorry about the bad formatting:

This is the only code snippet which concerned me in the post-patch sage, but I've explained above why I don't think this matters.

```
sage: binomial(5/2,3/2)
5/2
```



---

Attachment

hg bundle including the patch file and my doc-string revisions


---

Comment by mabshoff created at 2007-09-11 05:50:42

At least some of this has been merged. See

http://www.sagemath.org/hg/sage-main/rev/8def8d03e4a2

Is there more to come or can we close this ticket?

Cheers,

Michael


---

Comment by was created at 2007-09-12 18:36:03

Resolution: fixed
