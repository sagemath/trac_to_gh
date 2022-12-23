# Issue 2399: allow utf8 characters in the notebook cells

Issue created by migration from https://trac.sagemath.org/ticket/2399

Original creator: jason

Original creation time: 2008-03-05 22:38:15

Assignee: boothby

CC:  burcin

From sage-support:


```
When I was writing some other code this came out; finally decided to report it.  Do the following
in an online SAGE notebook:

1+1

We get two.  Now run the following:

# Limaçon
1+1

Get:

Exception (click to the left for traceback):
...
SyntaxError: Non-ASCII character '\xe7' in file /home/server2/sage_notebook/worksheets/dino/9/code/3.py on line 4, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/server2/sage_notebook/worksheets/dino/9/code/3.py", line 4
SyntaxError: Non-ASCII character '\xe7' in file /home/server2/sage_notebook/worksheets/dino/9/code/3.py on line 4, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details

---

Sacre bleu!  It's in a comment!  Looking at the error & the web site it may be a Python thing & untouchable.
But can we get around this?  Shouldn't our French friends (and countless others) be able to use SAGE?

Dean
```




---

Attachment


---

Comment by was created at 2008-03-05 22:57:14

Looks safe to me, and it's the right fix to make.  I say apply.


---

Comment by burcin created at 2008-03-06 08:48:54

Why is this only a problem in the notebook? When I try to paste the above code in the CLI, I get the following, which I think is much worse:

```
sage: for i in range(10):
....:     # Limaçon
WARNING: 
********
You or a %run:ed script called sys.stdin.close() or sys.stdout.close()!
Exiting IPython!
```


A possible way to fix this might be to make utf8 the default encoding for python, by applying the patch provided in comment:ticket:1663:2. I will try this later today.


---

Comment by burcin created at 2008-03-06 14:48:44

Changing the default encoding of python does not affect the crash in the CLI. 

Some more information: 

With this test code:

```
for i in range(5):
    #some commentç
    print i
```


These work:
 - python shells (both built by sage, and those installed on the system)
 - IPython 0.7.2 installed on my Debian etch workstation
 - IPython 0.6.15 installed on my Gentoo laptop


IPython 0.8.1 from Sage-2.10.2 crashes on my workstation with message from comment:2.

IPython 0.8.1 from Sage-2.8.12 gives the following traceback on my laptop:


```
In [1]: for i in range(5):
   ...:     #some commentç
---------------------------------------------------------------------------
<type 'exceptions.UnicodeEncodeError'>    Traceback (most recent call last)

/home/burcin/work/sage/sage-test/local/lib/python2.5/site-packages/IPython/iplib.py in raw_input(self, prompt, continue_prompt)
   2043                         newhist = self.input_hist_raw[-1].rstrip()
   2044                         self.readline.remove_history_item(histlen-1)
-> 2045                         self.readline.replace_history_item(histlen-2,newhist)
   2046                     except AttributeError:
   2047                         pass # re{move,place}_history_item are new in 2.4.

<type 'exceptions.UnicodeEncodeError'>: 'ascii' codec can't encode character u'\xe7' in position 36: ordinal not in range(128)
```



---

Comment by jason created at 2008-03-07 05:39:44

First, I think the patch ought to be applied because it addresses the notebook issue.  Maybe a new issue ought to be created for the command line issue.

More data points:

ipython on 32-bit ubuntu 7.10 also gives the same error message as sage when given the above string.


```
jason@littleone:~$ ipython
Python 2.5.1 (r251:54863, Oct  5 2007, 13:36:32) 
Type "copyright", "credits" or "license" for more information.

IPython 0.8.1 -- An enhanced Interactive Python.
?       -> Introduction to IPython's features.
%magic  -> Information about IPython's 'magic' % functions.
help    -> Python's own help system.
object? -> Details about 'object'. ?object also works, ?? prints more.

In [1]: for i in range(10):
   ...:      # Limaçon
---------------------------------------------------------------------------
<type 'exceptions.UnicodeEncodeError'>    Traceback (most recent call last)

/var/lib/python-support/python2.5/IPython/iplib.py in raw_input(self, prompt, continue_prompt)
   2040                         newhist = self.input_hist_raw[-1].rstrip()
   2041                         self.readline.remove_history_item(histlen-1)
-> 2042                         self.readline.replace_history_item(histlen-2,newhist)
   2043                     except AttributeError:
   2044                         pass # re{move,place}_history_item are new in 2.4.

<type 'exceptions.UnicodeEncodeError'>: 'ascii' codec can't encode character u'\xe7' in position 27: ordinal not in range(128)
   ...: 
```


and 


```
jason@littleone:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.2, Release Date: 2008-02-22                      |
| Type notebook() for the GUI, and license() for information.        |
sage: for i in range(10):
....:     # Limaçon
---------------------------------------------------------------------------
<type 'exceptions.UnicodeEncodeError'>    Traceback (most recent call last)

/home/jason/sage/local/lib/python2.5/site-packages/IPython/iplib.py in raw_input(self, prompt, continue_prompt)
   2043                         newhist = self.input_hist_raw[-1].rstrip()
   2044                         self.readline.remove_history_item(histlen-1)
-> 2045                         self.readline.replace_history_item(histlen-2,newhist)
   2046                     except AttributeError:
   2047                         pass # re{move,place}_history_item are new in 2.4.                

<type 'exceptions.UnicodeEncodeError'>: 'ascii' codec can't encode character u'\xe7' in position 30: ordinal not in range(128)
....:     
KeyboardInterrupt
sage: 
Exiting SAGE (CPU time 0m1.16s, Wall time 0m14.02s).
```



---

Comment by mabshoff created at 2008-03-07 05:56:34

Merged in Sage 2.10.3.rc3. Please open another ticket for the UTF-8 issue with the commandline since this ticket about the notebook has been addressed.


---

Comment by mabshoff created at 2008-03-07 05:56:34

Resolution: fixed
