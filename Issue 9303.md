# Issue 9303: dumb (easy-to-fix) mistake in sage notebook js.py file

archive/issues_009303.json:
```json
{
    "body": "Assignee: jason, was\n\nReported by Ralf Hemmecke:\n\n```\nOh, it's a bug. It hit me again... :-(\n\nsagenb-0.8.p2/src/sagenb/sagenb/notebook/js.py\n\nsays\n\ntry:\n   from sage.misc.misc import SAGE_ROOT\n   from pkg_resources import Requirement, working_set\n   sagenb_path = working_set.find(Requirement.parse('sagenb')).location\n   debug_mode = SAGE_ROOT not in os.path.realpath(sagenb_path)\nexcept AttributeError, ImportError:\n   debug_mode = False\n\nBut according to what I cite below, it should rather be\n\nexcept (AttributeError, ImportError):\n\nRalf\n\nhttp://docs.python.org/tutorial/errors.html\n\nA try statement may have more than one except clause, to specify\nhandlers for different exceptions. At most one handler will be executed.\nHandlers only handle exceptions that occur in the corresponding try\nclause, not in other handlers of the same try statement. An except\nclause may name multiple exceptions as a parenthesized tuple, for example:\n\n... except (RuntimeError, TypeError, NameError):\n...     pass\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9303\n\n",
    "created_at": "2010-06-22T04:36:02Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "dumb (easy-to-fix) mistake in sage notebook js.py file",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9303",
    "user": "https://github.com/williamstein"
}
```
Assignee: jason, was

Reported by Ralf Hemmecke:

```
Oh, it's a bug. It hit me again... :-(

sagenb-0.8.p2/src/sagenb/sagenb/notebook/js.py

says

try:
   from sage.misc.misc import SAGE_ROOT
   from pkg_resources import Requirement, working_set
   sagenb_path = working_set.find(Requirement.parse('sagenb')).location
   debug_mode = SAGE_ROOT not in os.path.realpath(sagenb_path)
except AttributeError, ImportError:
   debug_mode = False

But according to what I cite below, it should rather be

except (AttributeError, ImportError):

Ralf

http://docs.python.org/tutorial/errors.html

A try statement may have more than one except clause, to specify
handlers for different exceptions. At most one handler will be executed.
Handlers only handle exceptions that occur in the corresponding try
clause, not in other handlers of the same try statement. An except
clause may name multiple exceptions as a parenthesized tuple, for example:

... except (RuntimeError, TypeError, NameError):
...     pass
```

Issue created by migration from https://trac.sagemath.org/ticket/9303





---

archive/issue_comments_087488.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-06-22T04:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9303#issuecomment-87488",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid



---

archive/issue_comments_087489.json:
```json
{
    "body": "```\nWhat happens if the bug was fixed before the track ticket was reported? :)\n\nhttp://boxen.math.washington.edu:8100/rev/65d6838cefd8\n\nOndrej\n```",
    "created_at": "2010-06-22T04:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9303#issuecomment-87489",
    "user": "https://github.com/williamstein"
}
```

```
What happens if the bug was fixed before the track ticket was reported? :)

http://boxen.math.washington.edu:8100/rev/65d6838cefd8

Ondrej
```



---

archive/issue_events_022934.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-06-22T04:57:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9303",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9303#event-22934"
}
```
