# Issue 2399: allow utf8 characters in the notebook cells

archive/issues_002399.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @burcin\n\nFrom sage-support:\n\n\n```\nWhen I was writing some other code this came out; finally decided to report it.  Do the following\nin an online SAGE notebook:\n\n1+1\n\nWe get two.  Now run the following:\n\n# Lima\u00e7on\n1+1\n\nGet:\n\nException (click to the left for traceback):\n...\nSyntaxError: Non-ASCII character '\\xe7' in file /home/server2/sage_notebook/worksheets/dino/9/code/3.py on line 4, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details\n\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/home/server2/sage_notebook/worksheets/dino/9/code/3.py\", line 4\nSyntaxError: Non-ASCII character '\\xe7' in file /home/server2/sage_notebook/worksheets/dino/9/code/3.py on line 4, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details\n\n---\n\nSacre bleu!  It's in a comment!  Looking at the error & the web site it may be a Python thing & untouchable.\nBut can we get around this?  Shouldn't our French friends (and countless others) be able to use SAGE?\n\nDean\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2399\n\n",
    "created_at": "2008-03-05T22:38:15Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "allow utf8 characters in the notebook cells",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2399",
    "user": "https://github.com/jasongrout"
}
```
Assignee: boothby

CC:  @burcin

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



Issue created by migration from https://trac.sagemath.org/ticket/2399





---

archive/issue_comments_016158.json:
```json
{
    "body": "Attachment [utf8.patch](tarball://root/attachments/some-uuid/ticket2399/utf8.patch) by @jasongrout created at 2008-03-05 22:48:21",
    "created_at": "2008-03-05T22:48:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2399#issuecomment-16158",
    "user": "https://github.com/jasongrout"
}
```

Attachment [utf8.patch](tarball://root/attachments/some-uuid/ticket2399/utf8.patch) by @jasongrout created at 2008-03-05 22:48:21



---

archive/issue_comments_016159.json:
```json
{
    "body": "Looks safe to me, and it's the right fix to make.  I say apply.",
    "created_at": "2008-03-05T22:57:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2399#issuecomment-16159",
    "user": "https://github.com/williamstein"
}
```

Looks safe to me, and it's the right fix to make.  I say apply.



---

archive/issue_comments_016160.json:
```json
{
    "body": "Why is this only a problem in the notebook? When I try to paste the above code in the CLI, I get the following, which I think is much worse:\n\n```\nsage: for i in range(10):\n....:     # Lima\u00e7on\nWARNING: \n********\nYou or a %run:ed script called sys.stdin.close() or sys.stdout.close()!\nExiting IPython!\n```\n\n\nA possible way to fix this might be to make utf8 the default encoding for python, by applying the patch provided in comment:ticket:1663:2. I will try this later today.",
    "created_at": "2008-03-06T08:48:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2399#issuecomment-16160",
    "user": "https://github.com/burcin"
}
```

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

archive/issue_comments_016161.json:
```json
{
    "body": "Changing the default encoding of python does not affect the crash in the CLI. \n\nSome more information: \n\nWith this test code:\n\n```\nfor i in range(5):\n    #some comment\u00e7\n    print i\n```\n\n\nThese work:\n- python shells (both built by sage, and those installed on the system)\n- IPython 0.7.2 installed on my Debian etch workstation\n- IPython 0.6.15 installed on my Gentoo laptop\n\n\nIPython 0.8.1 from Sage-2.10.2 crashes on my workstation with message from comment:2.\n\nIPython 0.8.1 from Sage-2.8.12 gives the following traceback on my laptop:\n\n\n```\nIn [1]: for i in range(5):\n   ...:     #some comment\u00e7\n---------------------------------------------------------------------------\n<type 'exceptions.UnicodeEncodeError'>    Traceback (most recent call last)\n\n/home/burcin/work/sage/sage-test/local/lib/python2.5/site-packages/IPython/iplib.py in raw_input(self, prompt, continue_prompt)\n   2043                         newhist = self.input_hist_raw[-1].rstrip()\n   2044                         self.readline.remove_history_item(histlen-1)\n-> 2045                         self.readline.replace_history_item(histlen-2,newhist)\n   2046                     except AttributeError:\n   2047                         pass # re{move,place}_history_item are new in 2.4.\n\n<type 'exceptions.UnicodeEncodeError'>: 'ascii' codec can't encode character u'\\xe7' in position 36: ordinal not in range(128)\n```\n",
    "created_at": "2008-03-06T14:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2399#issuecomment-16161",
    "user": "https://github.com/burcin"
}
```

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

archive/issue_comments_016162.json:
```json
{
    "body": "First, I think the patch ought to be applied because it addresses the notebook issue.  Maybe a new issue ought to be created for the command line issue.\n\nMore data points:\n\nipython on 32-bit ubuntu 7.10 also gives the same error message as sage when given the above string.\n\n\n```\njason@littleone:~$ ipython\nPython 2.5.1 (r251:54863, Oct  5 2007, 13:36:32) \nType \"copyright\", \"credits\" or \"license\" for more information.\n\nIPython 0.8.1 -- An enhanced Interactive Python.\n?       -> Introduction to IPython's features.\n%magic  -> Information about IPython's 'magic' % functions.\nhelp    -> Python's own help system.\nobject? -> Details about 'object'. ?object also works, ?? prints more.\n\nIn [1]: for i in range(10):\n   ...:      # Lima\u00e7on\n---------------------------------------------------------------------------\n<type 'exceptions.UnicodeEncodeError'>    Traceback (most recent call last)\n\n/var/lib/python-support/python2.5/IPython/iplib.py in raw_input(self, prompt, continue_prompt)\n   2040                         newhist = self.input_hist_raw[-1].rstrip()\n   2041                         self.readline.remove_history_item(histlen-1)\n-> 2042                         self.readline.replace_history_item(histlen-2,newhist)\n   2043                     except AttributeError:\n   2044                         pass # re{move,place}_history_item are new in 2.4.\n\n<type 'exceptions.UnicodeEncodeError'>: 'ascii' codec can't encode character u'\\xe7' in position 27: ordinal not in range(128)\n   ...: \n```\n\n\nand \n\n\n```\njason@littleone:~$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.10.2, Release Date: 2008-02-22                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: for i in range(10):\n....:     # Lima\u00e7on\n---------------------------------------------------------------------------\n<type 'exceptions.UnicodeEncodeError'>    Traceback (most recent call last)\n\n/home/jason/sage/local/lib/python2.5/site-packages/IPython/iplib.py in raw_input(self, prompt, continue_prompt)\n   2043                         newhist = self.input_hist_raw[-1].rstrip()\n   2044                         self.readline.remove_history_item(histlen-1)\n-> 2045                         self.readline.replace_history_item(histlen-2,newhist)\n   2046                     except AttributeError:\n   2047                         pass # re{move,place}_history_item are new in 2.4.                \n\n<type 'exceptions.UnicodeEncodeError'>: 'ascii' codec can't encode character u'\\xe7' in position 30: ordinal not in range(128)\n....:     \nKeyboardInterrupt\nsage: \nExiting SAGE (CPU time 0m1.16s, Wall time 0m14.02s).\n```\n",
    "created_at": "2008-03-07T05:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2399#issuecomment-16162",
    "user": "https://github.com/jasongrout"
}
```

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

archive/issue_events_005659.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-07T05:56:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2399",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2399#event-5659"
}
```



---

archive/issue_comments_016163.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc3. Please open another ticket for the UTF-8 issue with the commandline since this ticket about the notebook has been addressed.",
    "created_at": "2008-03-07T05:56:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2399#issuecomment-16163",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc3. Please open another ticket for the UTF-8 issue with the commandline since this ticket about the notebook has been addressed.



---

archive/issue_comments_016164.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-07T05:56:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2399#issuecomment-16164",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
