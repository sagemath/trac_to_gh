# Issue 5335: [with patch, needs review] Create Sage 3.3 release notes

Issue created by migration from https://trac.sagemath.org/ticket/5335

Original creator: mabshoff

Original creation time: 2009-02-22 12:25:30

Assignee: mabshoff

CC:  mvngu

Attached is draft1 of the release notes. These need to be spell checked as well as read over to make sure there are no other problems.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-22 12:26:13

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2009-02-22 12:54:19

Two comments by wjp:

```
wjp: "Aside from the above there a very large number"
mabs: *is*
wjp: "This are false"
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-02-22 16:32:43

And Carl Witty correctly pointed out:

```
cwitty: Shouldn't the "Known issues" mention Fedora 64-bit not working?
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-02-22 16:34:12

And another issue:

```

[08:32am] mabs: re: "inline text cells"  - I took that from the ticket and I 
tend not to change the summaries in the listing so the original can be easily 
found in trac.
[08:34am] cwitty: I wasn't talking about the ticket, I was talking about this:
[08:34am] cwitty: One of the new major usability
[08:34am] cwitty: 97improvements to the notebook is the addition and integration of the
[08:34am] cwitty: 98TinyMCE editor which now allows to add inline text cells to the notebook
[08:34am] cwitty: 99via a very nice WYSIWYG editor.
```



---

Attachment


---

Attachment

Ok, put up draft 3 with a corrected description of the FC 9/10 libSingular problem.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-22 19:29:15

Resolution: fixed


---

Comment by mabshoff created at 2009-02-22 19:29:15

Merged in Sage 3.3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-22 19:29:15

Changing component from doctest to distribution.


---

Comment by mvngu created at 2009-02-23 02:32:20

patch against draft 3


---

Attachment

release note resulting from applying above patch


---

Attachment

OK, I'm very late here, but I can't resist being somewhat pedantic :-) Draft 4 of the release note fixes some typos in draft 3.
