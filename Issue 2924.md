# Issue 2924: programming guide section on style is terrible!

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-14 22:05:11

Assignee: tba

John Palmieri pointed out that 

http://sagemath.org/doc/html/prog/node5.html

is completely wrong. In particular, it bizarrely mentions Scipy (??), and tells one to use lowercase for class names.


```
2.1 Coding Conventions
Follow the standard Python formatting rules when writing code for SciPy, as explained at http://www.python.org/doc/essays/styleguide.html. In particular,

    * Use 4 spaces for indentation levels. Do not use tabs as they can result in indentation confusion. Most editors have a feature that will insert 4 spaces when the tab key is hit. Also, many editors will automatically search/replace leading tabs with 4 spaces.

    * Use all lowercase function/class names with underscore separated words:

              def set_some_value()

      instead of:

              def setSomeValue()

      There is no differentiation between classes, functions, verbs, nouns, etc.
```



---

Attachment


---

Comment by mhansen created at 2008-04-15 00:12:38

Looks good to me.


---

Comment by mabshoff created at 2008-04-15 00:20:15

Merged in Sage 3.0.alpha5


---

Comment by mabshoff created at 2008-04-15 00:20:15

Resolution: fixed
