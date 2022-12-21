# Issue 3448: Preparser handles (ellipses in) triple quotes incorrectly

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-06-17 15:39:08

Assignee: was

CC:  robertwb


```
sage: s = """G0 [14..26,6][:6242]
....: G1 [14..26,6][6242:12484]
....: G2 [14..26,6][12484:18726]
....: G3 [14..26,6][18726:24968]
....: G4 [14..26,6][24968:31210]
....: G5 [14..26,6][31210:]
....: """
sage: s.split('\n')

['G0 (ellipsis_range(14,Ellipsis,26,6))[:6242]',
 'G1 (ellipsis_range(14,Ellipsis,26,6))[6242:12484]',
 'G2 (ellipsis_range(14,Ellipsis,26,6))[12484:18726]',
 'G3 (ellipsis_range(14,Ellipsis,26,6))[18726:24968]',
 'G4 (ellipsis_range(14,Ellipsis,26,6))[24968:31210]',
 'G5 (ellipsis_range(14,Ellipsis,26,6))[31210:]',
 '']  
```



---

Comment by mabshoff created at 2008-10-07 17:34:33

I don't think RobertWB is aware of the problem, so let's CC him.

Cheers,

Michael


---

Comment by mhansen created at 2010-02-02 22:57:03

Resolution: invalid


---

Comment by mhansen created at 2010-02-02 22:57:03

I'm going to mark this as invalid now since the code for the preparser has been reworked:


```
sage: s = """G0 [14..26,6][:6242]
....: G1 [14..26,6][6242:12484]
....: G2 [14..26,6][12484:18726]
....: G3 [14..26,6][18726:24968]
....: G4 [14..26,6][24968:31210]
....: G5 [14..26,6][31210:]
....: """
sage: s.split('\n')
['G0 [14..26,6][:6242]', 'G1 [14..26,6][6242:12484]', 'G2 [14..26,6][12484:18726]', 'G3 [14..26,6][18726:24968]', 'G4 [14..26,6][24968:31210]', 'G5 [14..26,6][31210:]', '']
```

