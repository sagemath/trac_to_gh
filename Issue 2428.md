# Issue 2428: Sage CLI crashes on unicode input

archive/issues_002428.json:
```json
{
    "body": "Assignee: was\n\nKeywords: ipython\n\nThe CLI crashes (at least on some platforms) on unicode input.\n\nOn Debian etch workstation:\n\n```\nsage: #bur\u00e7in\nWARNING: \n********\nYou or a %run:ed script called sys.stdin.close() or sys.stdout.close()!\nExiting IPython!\n```\n\nOn my Gentoo laptop the example above works, but this doesn't:\n\n```\nsage: for i in range(10):\n....:      #bur\u00e7in\n---------------------------------------------------------------------------\n<type 'exceptions.UnicodeEncodeError'>    Traceback (most recent call last)\n\n/home/burcin/work/sage/sage-test/local/lib/python2.5/site-packages/IPython/iplib.py in raw_input(self, prompt, continue_prompt)\n   2043                         newhist = self.input_hist_raw[-1].rstrip()\n   2044                         self.readline.remove_history_item(histlen-1)\n-> 2045                         self.readline.replace_history_item(histlen-2,newhist)\n   2046                     except AttributeError:\n   2047                         pass # re{move,place}_history_item are new in 2.4.                \n\n<type 'exceptions.UnicodeEncodeError'>: 'ascii' codec can't encode character u'\\xe7' in position 25: ordinal not in range(128)\n....: \n```\n\n\nSee also comments in ticket:2399 and http://ipython.scipy.org/ipython/ipython/ticket/156\n\nIssue created by migration from https://trac.sagemath.org/ticket/2428\n\n",
    "created_at": "2008-03-08T14:02:14Z",
    "labels": [
        "user interface",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "Sage CLI crashes on unicode input",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2428",
    "user": "burcin"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/2428





---

archive/issue_comments_016434.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-22T21:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2428#issuecomment-16434",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016435.json:
```json
{
    "body": "This works now due to malb's fix #2593:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.11.alpha0, Release Date: 2008-03-20                 |\n| Type notebook() for the GUI, and license() for information.        |\nsage: #bur\u00e7in\nsage:\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-03-22T21:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2428#issuecomment-16435",
    "user": "mabshoff"
}
```

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
