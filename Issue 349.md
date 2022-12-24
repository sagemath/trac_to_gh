# Issue 349: Tab completion on Sage() object does not work

archive/issues_000349.json:
```json
{
    "body": "Assignee: was\n\nI get the following traceback when trying to do tab completion on a Sage object.\n\nsage: s = Sage()\nsage: s.---------------------------------------------------------------------------\n<type 'exceptions.SyntaxError'>           Traceback (most recent call last)\n\n/Users/yqiang/Software/sage/local/lib/python2.5/site-packages/IPython/completer.py in complete(self=<IPython.completer.IPCompleter instance at 0x15a88c8>, text='s.', state=0)\n    632                         self.matches = []\n    633                         for matcher in self.matchers:\n--> 634                             self.matches.extend(matcher(text))\n        self.matches.extend = <built-in method extend of list object at 0x8ff4fd0>\n        matcher = <bound method IPCompleter.python_matches of <IPython.completer.IPCompleter instance at 0x15a88c8>>\n        text = 's.'\n    635                     else:\n    636                         for matcher in self.matchers:\n\n/Users/yqiang/Software/sage/local/lib/python2.5/site-packages/IPython/completer.py in python_matches(self=<IPython.completer.IPCompleter instance at 0x15a88c8>, text='s.')\n    454         if \".\" in text:\n    455             try:\n--> 456                 matches = self.attr_matches(text)\n        matches = undefined\n        self.attr_matches = <bound method IPCompleter.attr_matches of <IPython.completer.IPCompleter instance at 0x15a88c8>>\n        text = 's.'\n    457                 if text.endswith('.') and self.omit__names:\n    458                     if self.omit__names == 1:\n\n/Users/yqiang/Software/sage/local/lib/python2.5/site-packages/IPython/completer.py in attr_matches(self=<IPython.completer.IPCompleter instance at 0x15a88c8>, text='s.')\n    223         if hasattr(object, 'trait_names'):\n    224             try:\n--> 225                 words.extend(object.trait_names())\n        words.extend = <built-in method extend of list object at 0x900ab48>\n        object.trait_names = <bound method Sage.trait_names of Sage>\n    226                 may_have_dupes = True\n    227             except TypeError:\n\n/Users/yqiang/Software/sage-2.4.1.2/local/lib/python2.5/site-packages/sage/interfaces/sage0.py in trait_names(self=Sage)\n    133 \n    134     def trait_names(self):\n--> 135         return eval(self.eval('globals().keys()'))\n        global eval = undefined\n        self.eval = <bound method Sage.eval of Sage>\n    136 \n    137     def quit(self, verbose=False):\n\n<type 'exceptions.SyntaxError'>: unexpected EOF while parsing (<string>, line 0)\n\nIssue created by migration from https://trac.sagemath.org/ticket/349\n\n",
    "created_at": "2007-04-09T14:59:55Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.2",
    "title": "Tab completion on Sage() object does not work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/349",
    "user": "yi"
}
```
Assignee: was

I get the following traceback when trying to do tab completion on a Sage object.

sage: s = Sage()
sage: s.---------------------------------------------------------------------------
<type 'exceptions.SyntaxError'>           Traceback (most recent call last)

/Users/yqiang/Software/sage/local/lib/python2.5/site-packages/IPython/completer.py in complete(self=<IPython.completer.IPCompleter instance at 0x15a88c8>, text='s.', state=0)
    632                         self.matches = []
    633                         for matcher in self.matchers:
--> 634                             self.matches.extend(matcher(text))
        self.matches.extend = <built-in method extend of list object at 0x8ff4fd0>
        matcher = <bound method IPCompleter.python_matches of <IPython.completer.IPCompleter instance at 0x15a88c8>>
        text = 's.'
    635                     else:
    636                         for matcher in self.matchers:

/Users/yqiang/Software/sage/local/lib/python2.5/site-packages/IPython/completer.py in python_matches(self=<IPython.completer.IPCompleter instance at 0x15a88c8>, text='s.')
    454         if "." in text:
    455             try:
--> 456                 matches = self.attr_matches(text)
        matches = undefined
        self.attr_matches = <bound method IPCompleter.attr_matches of <IPython.completer.IPCompleter instance at 0x15a88c8>>
        text = 's.'
    457                 if text.endswith('.') and self.omit__names:
    458                     if self.omit__names == 1:

/Users/yqiang/Software/sage/local/lib/python2.5/site-packages/IPython/completer.py in attr_matches(self=<IPython.completer.IPCompleter instance at 0x15a88c8>, text='s.')
    223         if hasattr(object, 'trait_names'):
    224             try:
--> 225                 words.extend(object.trait_names())
        words.extend = <built-in method extend of list object at 0x900ab48>
        object.trait_names = <bound method Sage.trait_names of Sage>
    226                 may_have_dupes = True
    227             except TypeError:

/Users/yqiang/Software/sage-2.4.1.2/local/lib/python2.5/site-packages/sage/interfaces/sage0.py in trait_names(self=Sage)
    133 
    134     def trait_names(self):
--> 135         return eval(self.eval('globals().keys()'))
        global eval = undefined
        self.eval = <bound method Sage.eval of Sage>
    136 
    137     def quit(self, verbose=False):

<type 'exceptions.SyntaxError'>: unexpected EOF while parsing (<string>, line 0)

Issue created by migration from https://trac.sagemath.org/ticket/349





---

archive/issue_comments_001695.json:
```json
{
    "body": "I can't replicate this anywhere, so I guess it is fixed in sage-2.8.2.",
    "created_at": "2007-08-19T02:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/349#issuecomment-1695",
    "user": "was"
}
```

I can't replicate this anywhere, so I guess it is fixed in sage-2.8.2.



---

archive/issue_comments_001696.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-19T02:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/349#issuecomment-1696",
    "user": "was"
}
```

Resolution: fixed
