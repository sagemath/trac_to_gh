# Issue 3434: notebook -- implementin MAX_OUTPUT handling in cell.py for interact.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-06-15 23:11:35

Assignee: boothby

Try this in the notebook

```
`@`interact
def test(a=1):
    print 2^a
```


For large a it outputs something massive and very very bad. This should not be aloud. 

To fix this:

1. Look at

```
            self.interact = input[len('%__sage_interact__')+1]
```

in cell.py
2. Factor out this code from cell.py:

```
        if 'notruncate' not in output and 'Output truncated!' not in output and \
              (len(output) > MAX_OUTPUT or output.count('\n') > MAX_OUTPUT_LINES) and \
```



---

Comment by AlexGhitza created at 2009-01-23 02:50:18

Changing type from defect to enhancement.


---

Comment by boothby created at 2020-03-29 02:04:25

Closing deprecated notebook tickets


---

Comment by boothby created at 2020-03-29 02:04:25

Resolution: invalid
