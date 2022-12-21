# Issue 7648: notebook: issue with indentation of first line being wrong

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-10 01:19:32

Assignee: was


```
On 11/27/2009 05:47 AM, Minh Nguyen wrote:
> On Fri, Nov 27, 2009 at 9:10 PM, Yotam Avital <> wrote:
>> for i in range (1,5):
>>     print '%6s %6s %6s'%(i, i^2, i^3)

I think *part* of the problem could be line 294 of sagenb.interfaces.expect:

       s = s.strip().rstrip(self._prompt)


Replacing this with

       s = s.rstrip(self._prompt)

appears to restore the expected spacing.  But quitting and reopening the
worksheet puts

1      1      1
    2      4      8
    3      9     27
    4     16     64

in the output cell.  I think the problem here is line 910 (or so) of
sagenb.notebook.cell:

           out = '///\n' + out.strip()


Replacing this with

           out = '///\n' + out.strip('\n')

seems to solve this problem.  It also makes the text representation of
the worksheet more compact.

Note: I haven't tested these changes extensively.
```



---

Attachment

Make the changes in the ticket description.  sagenb repo.


---

Comment by mpatel created at 2009-12-10 03:13:45

Changing status from new to needs_review.


---

Comment by mpatel created at 2009-12-10 03:13:45

The Se tests pass.  Unfortunately, `sage -t sagenb/notebook` yields several

```
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
```

Please see #7650.


---

Comment by mpatel created at 2010-01-15 23:03:44

The patch for #7663 (and #7924) clashes with [attachment:trac_7648-missing_indent.patch this one].  Reconciling them should be easy.


---

Comment by timdumol created at 2010-01-17 18:26:37

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-01-17 18:26:37

Good job.


---

Comment by timdumol created at 2010-01-19 03:27:58

Resolution: fixed
