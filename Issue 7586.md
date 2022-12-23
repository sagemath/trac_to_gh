# Issue 7586: develoers' guide: document features of attach, load, iload, ed, %ed, %edit, edit()

Issue created by migration from https://trac.sagemath.org/ticket/7586

Original creator: mvngu

Original creation time: 2009-12-02 20:33:17

Assignee: mvngu

CC:  jhpalmieri

From this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c0543314ff9c15cb) thread:

```
By the way, I discovered accidentally that from the command line (not
the notebook) if you type:

sage: ed   # or %ed or %edit

then it opens up your favorite editor (whatever is set by the $EDITOR
shell variable).  Then in the editor you can type

def FF(x):
    long definition here
    which would be really annoying
    to type on the command line

then save it -- it gets written to a temporary file -- and the code
gets executed and you have thus redefined FF.  Then later you can do

sage: ed FF

and it will let you modify your code.  This is an ipython feature, it
seems.  Should it be described somewhere in the Sage documentation?
```

The following commands should at least be documented in the Developers' Guide together with explanation on how to use them for interactive development:

 1. `load`
 1. `attach`
 1. `iload`
 1. `ed`
 1. `%ed`
 1. `%edit`
 1. `edit()`


---

Comment by ddrake created at 2009-12-02 23:18:03

Some of those commands -- the % ones -- come from IPython, right? If so, we should find where their documentation is online and link to that, along with some brief descriptions of useful commands. One that I like is `!clear` which simply clears the screen.


---

Comment by mpatel created at 2009-12-29 06:35:29

Just a quick, somewhat-related note: `attach` and `load` have been rewritten at #7514.


---

Comment by jhpalmieri created at 2011-04-19 19:04:09

See #11219 for a related ticket.  (I thought that "%edit" was useful enough for general users that it should be in the tutorial, not just the developer's guide.)
