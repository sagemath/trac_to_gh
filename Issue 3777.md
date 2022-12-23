# Issue 3777: notebook -- issue parsing out <script> tags

Issue created by migration from https://trac.sagemath.org/ticket/3777

Original creator: was

Original creation time: 2008-08-05 21:30:45

Assignee: boothby

This input to the notebook results in pain:


```
html('<script>alert("</script>");</script>')
```


This should only be looked at after #3735 is applied.  Then look at this code in 
cell.py

```
        if ncols == 0:
            while True:
                i = t.lower().find('<script>')
                if i == -1: break
                j = t[i:].lower().find('</script>')
                if j == -1: break
                t = t[:i] + t[i+j+len('</script>'):]
                
```

and also `function eval_script_tags(text)` in js.py.



---

Comment by was created at 2008-08-05 21:30:55

Changing priority from major to minor.


---

Comment by jason created at 2009-01-21 07:43:53

It looks like the problem here is that we don't have a full HTML/Javascript parser built in to cell.py?


---

Attachment

Sample failure of </script> tags.


---

Comment by acleone created at 2010-01-19 06:56:23

Changing status from new to needs_review.


---

Comment by acleone created at 2010-01-19 06:56:23

Apparently this is invalid javascript.

foo.html shows that firefox gives the same behavior.


---

Comment by acleone created at 2010-01-19 06:57:02

Resolution: invalid
