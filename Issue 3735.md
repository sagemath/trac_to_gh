# Issue 3735: Interact - header Javascript code executes on update

Issue created by migration from https://trac.sagemath.org/ticket/3735

Original creator: itolkov

Original creation time: 2008-07-28 18:53:48

Assignee: boothby

Here is an illustration (requires #3636):


```
@interact
def _(t=text_control("n = <span id='n'>0</span>\
        <script>n=parseInt($('#n').text()); $('#n').text(1+n);</script>"),
    l=["Increment"]
): pass
```


Pressing "Increment" increments n, which implies that the line of Javascript code _in the header_ is executed. 


---

Attachment


---

Comment by was created at 2008-08-05 21:32:58

And, as an added bonus we also fix another bug!  Namely, if you put e.g., 


```
html("alert('hi')")
```


in a cell and hit shift-enter, then hi pops up in an alert ONCE, but if you
then refresh the page, "hi" pops up in an alert twice.   Now it only happens once
in both cases.

Code written by William Stein and Igor Tolkov


---

Comment by itolkov created at 2008-08-07 05:32:45

Positive review.

There is still a bug, namely, if one tries

```
html("<script>alert('</script>');</script>")
```

and the same for html tags. However, this defect existed before.


---

Comment by mabshoff created at 2008-08-09 23:23:20

Merged in Sage 3.1.alpha1


---

Comment by mabshoff created at 2008-08-09 23:23:20

Resolution: fixed
