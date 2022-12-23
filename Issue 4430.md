# Issue 4430: optimize new worksheet startup

Issue created by migration from https://trac.sagemath.org/ticket/4430

Original creator: robertwb

Original creation time: 2008-11-03 17:53:13

Assignee: tbd

When one creates a new worksheet, it would be nice if the sage process started up in the background right then, rather than wait till one types the first command. Currently there is an annoying lag...



---

Comment by TimothyClemans created at 2008-11-03 20:24:45

Changing component from algebra to notebook.


---

Comment by TimothyClemans created at 2008-11-03 20:24:45

Changing assignee from tbd to boothby.


---

Attachment


---

Comment by mpatel created at 2010-01-25 16:05:52

Resolution: invalid


---

Comment by mpatel created at 2010-01-25 16:05:52

I'm closing this, since we now start a worksheet when it's first served.  From `twist.py`, around line #1514:

```python
class Worksheet(WorksheetResource, resource.Resource):
    addSlash = True

    def render(self, ctx):
        self.worksheet.sage()
        s = notebook.html(worksheet_filename = self.name,  username=self.username)
        return HTMLResponse(stream=s)
```

I've also confirmed this with a print statement in `Worksheet.sage`.

By the way, the patch here appears to be for a different ticket.
