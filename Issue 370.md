# Issue 370: improve the documentation of show

Issue created by migration from https://trac.sagemath.org/ticket/370

Original creator: was

Original creation time: 2007-05-19 04:56:48

Assignee: was


```
> One suggestion I have arising from my problems is that the
> documentation for the show command be improved.  It is a very
> important function for most users.

Agreed -- the documentation for show now is terrible.  It doesn't
even mention that it can be used to show the typeset version of
an object!

William
```



---

Comment by mhansen created at 2008-02-27 12:37:00

What is the status of this?  Here is the current documentation when doing show?


```
        Show a graphics object x.
    
        OPTIONAL INPUT:
            filename -- (default: None) string
    
        SOME OF THESE MAY APPLY:
            dpi -- dots per inch
            figsize -- [width, height] (same for square aspect)
            axes -- (default: True)
            fontsize -- positive integer
            frame -- (default: False) draw a MATLAB-like frame around the image
    
        EXAMPLES:
            sage: show(graphs(3))
            sage: show(list(graphs(3)))

```



---

Comment by malb created at 2008-04-01 12:25:38

Resolution: fixed


---

Comment by malb created at 2008-04-01 12:25:38

Unless the request is specified, I'm all for closing it.


```
[13:19] <mabshoff> malb: what is your take on #370 ?
[13:19] <malb> it looks alright
[13:20] <mabshoff> If you also think it should be closed as fixed please do so.
```

