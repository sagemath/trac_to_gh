# Issue 7497: notebook -- bug in viewing/editing attached files

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-11-20 05:37:45

Assignee: boothby

In the notebook, click "Data --> Upload or create file...", then edit the file to contain

```
Hi </textarea> foo bar 
```


Save it and re-open it.  The foo bar is *outside* the text area!  This is because this is rendered using the data/sage/html/notebook/download_or_delete_datafile.html template with this line in it:

```
    <textarea class="edit" name="textfield" rows=17 cols=70 id="textfield">{{ text_file_content }}</textarea>
```



---

Comment by mpatel created at 2009-12-14 17:56:44

I think it's sufficient to replace `{{ text_file_content }}` with `{{ text_file_content|e }}` (cf. [this](http://jinja.pocoo.org/2/documentation/templates#html-escaping)).


---

Comment by mpatel created at 2010-01-02 01:08:17

Escape data file content placed in view/edit window.  sagenb repo.


---

Attachment


---

Comment by mpatel created at 2010-01-02 01:08:54

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-01-07 03:25:59

#7786's v8 should subsume this.  If/when that ticket merges, please close this ticket.


---

Comment by timdumol created at 2010-01-19 03:15:25

Works with sagenb-0.6.


---

Comment by timdumol created at 2010-01-19 03:15:25

Resolution: duplicate
