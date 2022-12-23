# Issue 5412: bug in edit and set_edit_template

Issue created by migration from https://trac.sagemath.org/ticket/5412

Original creator: was

Original creation time: 2009-03-01 16:10:04

Assignee: cwitty

Check this out:

```
sage: edit(0)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/Users/wstein/.sage/temp/h70_33_89_223.paws.uga.edu/13827/_Users_wstein__sage_init_sage_0.py in <module>()

/Users/wstein/build/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/misc/edit_module.pyc in edit(obj, editor, bg)
    243          set_editor(base,opts=opts)
    244       except (ValueError, KeyError, IndexError):
--> 245          raise ValueError, "Use set_edit_template(<template_string>) to set a default"
    246       
    247    if not(edit_template):

ValueError: Use set_edit_template(<template_string>) to set a default
sage: set_edit_template('e')
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/Users/wstein/.sage/temp/h70_33_89_223.paws.uga.edu/13827/_Users_wstein__sage_init_sage_0.py in <module>()

NameError: name 'set_edit_template' is not defined
```


Either the error message should be changed or set_edit_template should be imported at the top level.


---

Attachment


---

Comment by mabshoff created at 2009-03-02 05:20:39

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-03-02 05:20:39

Changing assignee from cwitty to mabshoff.


---

Comment by was created at 2009-03-02 05:21:43

good!! thanks!!!1


---

Comment by mabshoff created at 2009-03-02 05:22:00

Resolution: fixed


---

Comment by mabshoff created at 2009-03-02 05:22:00

Merged in Sage 3.4.rc0.

Cheers,

Michael
