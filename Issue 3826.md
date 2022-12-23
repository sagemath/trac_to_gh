# Issue 3826: Empty string in interact prints \x00

Issue created by migration from https://trac.sagemath.org/ticket/3826

Original creator: slabbe

Original creation time: 2008-08-12 23:23:21

Assignee: boothby

CC:  saliola

Keywords: interact empty string

In the notebook of sage 3.0.6: 

Write


```
@interact
def f(a=input_box(default='aaa',type=str,label='Your name :')):
    print a
    print [1,2,3,a]
```


Then, delete 'aaa' from the box. Press enter and the list prints like this :


```
[1, 2, 3, '\x00']
```


while should be :


```
[1, 2, 3, '']
```




---

Comment by mabshoff created at 2008-08-13 00:01:39

Changing assignee from boothby to itolkov.


---

Comment by mabshoff created at 2008-08-13 00:01:39

Changing component from notebook to interact.


---

Comment by mabshoff created at 2008-08-13 00:01:39

Reassigning the component to "interact" since I just created it.

Cheers,

Michael


---

Attachment


```
javascript: encode64("")
```

AA==


```
sage.server.notebook.interact.standard_b64decode("AA==")
```

'\x00'

My patch adds a check in the interact() function. However, encode64() and decode64() seem to be buggy. In particular, they are not inverses. For example,

```
javascript: encode64(decode64(""))
```

AAAA


---

Attachment


---

Comment by cwitty created at 2008-08-23 18:24:03

Rather than working around the bug, it seems better to just fix the bug.  My patch changes encode64 and decode64 to match the Python behavior (which I believe to be the correct behavior), where the empty string encodes/decodes to the empty string.


---

Comment by itolkov created at 2008-08-27 01:09:02

Seems to be working in the example above, as well as in my example.

+1


---

Comment by mabshoff created at 2008-08-27 01:15:47

Merged in Sage 3.1.2.alpha1


---

Comment by mabshoff created at 2008-08-27 01:15:47

Resolution: fixed


---

Comment by mabshoff created at 2008-08-27 01:16:18

PS: I merged *only* Carl's patch, i.e. trac3826-javascript-base64.patch
