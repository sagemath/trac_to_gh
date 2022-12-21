# Issue 1166: 2D terminal output is inconsistent and corrupted

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2007-11-13 22:44:08

Assignee: was


```
sage: f = (exp(x)-1)/(exp(x/2)+1)
sage: g = exp(x/2)-1
sage: print f(10.0), g(10.0)
                               147.4131591025766                               \
 147.4131591025766
sage: print 1, 2
1 2
sage: print f(10), g(10)
                                     10
                                    e   - 1
                                   --------
                                     5
                                    e  + 1                                     \
  5
                                     e  - 1
```


The output of f(10.0), g(10.0) [with many spaces] seems inconsistent with that of 1, 2 [no spaces]. With f(10), g(10) the exponent 5 of g(10) wraps around the terminal line, and is thus
not properly aligned with e - 1. (all this in a 80-column xterm)


---

Comment by mabshoff created at 2007-12-18 23:17:37

It looks like a newline at the end of the multi line expression of f(10) would fix the issue:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.9, Release Date: 2007-12-16                         |
| Type notebook() for the GUI, and license() for information.        |
sage: f = (exp(x)-1)/(exp(x/2)+1)
sage: g = exp(x/2)-1
sage: print f(10.0), g(10.0)
                               147.4131591025766                                147.4131591025766
sage: print 1, 2
1 2
sage: print f(10), g(10)
                                     10
                                    e   - 1
                                   --------
                                     5
                                    e  + 1                                       5
                                     e  - 1
sage: print f(10)
                                     10
                                    e   - 1
                                   --------
                                     5
                                    e  + 1
sage: print g(10)
                                      5
                                     e  - 1
sage:
```


Cheers,

Michael


---

Attachment


---

Comment by zimmerma created at 2008-01-21 15:11:58

[this is my first review, thus please take with care]

I get with this patch applied in 2.10:

```
sage: f=(exp(x)-1)/(exp(x/2)+1)
sage: g=exp(x/2)-1
sage: print f(10.0), g(10.0)

                               147.4131591025766 
                               147.4131591025766
sage: print 1, 2
1 2
sage: print f(10), g(10)

                                     10
                                    e   - 1
                                   --------
                                     5
                                    e  + 1 
                                      5
                                     e  - 1
```

The output is much better, but I would expect:

```
sage: print f(10.0), g(10.0)

                   147.4131591025766, 147.4131591025766
```

or

```
sage: print f(10.0), g(10.0)
147.4131591025766 147.4131591025766
```

However, since this is an improvement, I give a positive review.


---

Comment by mabshoff created at 2008-01-21 22:57:13

The potential solution to the adding an extra newlines in situations like

```
sage: print f(10.0), g(10.0)
147.4131591025766 147.4131591025766
```

might be that we need to check if the string returned from `f(10.0` contains a newline in which case we need to add the extra newline to separate the the two multiline outputs. If that is doable please open another ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-21 22:58:49

Merged in Sage 2.10.1.alpha1


---

Comment by mabshoff created at 2008-01-21 22:58:49

Resolution: fixed
