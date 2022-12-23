# Issue 2428: Sage CLI crashes on unicode input

Issue created by migration from https://trac.sagemath.org/ticket/2428

Original creator: burcin

Original creation time: 2008-03-08 14:02:14

Assignee: was

Keywords: ipython

The CLI crashes (at least on some platforms) on unicode input.

On Debian etch workstation:

```
sage: #burçin
WARNING: 
********
You or a %run:ed script called sys.stdin.close() or sys.stdout.close()!
Exiting IPython!
```

On my Gentoo laptop the example above works, but this doesn't:

```
sage: for i in range(10):
....:      #burçin
---------------------------------------------------------------------------
<type 'exceptions.UnicodeEncodeError'>    Traceback (most recent call last)

/home/burcin/work/sage/sage-test/local/lib/python2.5/site-packages/IPython/iplib.py in raw_input(self, prompt, continue_prompt)
   2043                         newhist = self.input_hist_raw[-1].rstrip()
   2044                         self.readline.remove_history_item(histlen-1)
-> 2045                         self.readline.replace_history_item(histlen-2,newhist)
   2046                     except AttributeError:
   2047                         pass # re{move,place}_history_item are new in 2.4.                

<type 'exceptions.UnicodeEncodeError'>: 'ascii' codec can't encode character u'\xe7' in position 25: ordinal not in range(128)
....: 
```


See also comments in ticket:2399 and http://ipython.scipy.org/ipython/ipython/ticket/156


---

Comment by mabshoff created at 2008-03-22 21:20:50

Resolution: fixed


---

Comment by mabshoff created at 2008-03-22 21:20:50

This works now due to malb's fix #2593:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.11.alpha0, Release Date: 2008-03-20                 |
| Type notebook() for the GUI, and license() for information.        |
sage: #burçin
sage:
```


Cheers,

Michael
