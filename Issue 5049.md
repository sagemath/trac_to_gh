# Issue 5049: show(mathematica('2/3')) doesn't work

archive/issues_005049.json:
```json
{
    "body": "Assignee: was\n\nIf you do\n\n```\nshow(mathematica('2/3'))\n```\n\n\nin the notebook, you get no output.  Since latex(mathematica(...)) works great, this is stupid. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5049\n\n",
    "created_at": "2009-01-21T12:07:18Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "show(mathematica('2/3')) doesn't work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5049",
    "user": "was"
}
```
Assignee: was

If you do

```
show(mathematica('2/3'))
```


in the notebook, you get no output.  Since latex(mathematica(...)) works great, this is stupid. 

Issue created by migration from https://trac.sagemath.org/ticket/5049





---

archive/issue_comments_038477.json:
```json
{
    "body": "This is because the show method is written to deal only with images:\n\n\n```\n    def show(self, filename=None, ImageSize=600):\n        \"\"\"\n        Show a mathematica plot in the Sage notebook.\n\n        EXAMPLES:\n            sage: P = mathematica('Plot[Sin[x],{x,-2Pi,4Pi}]')   # optional - mathematica\n            sage: show(P)                                        # optional - mathematica\n            sage: P.show(ImageSize=800)                          # optional - mathematica\n        \"\"\"\n        P = self._check_valid()\n        if filename is None:\n            filename = graphics_filename()\n        orig_dir = P.eval('Directory[]').strip()\n        P.chdir(os.path.abspath(\".\"))\n        s = 'Export[\"%s\", %s, ImageSize->%s]'%(filename, self.name(), ImageSize)\n        P.eval(s)\n        P.chdir(orig_dir)\n```\n",
    "created_at": "2009-01-21T18:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5049#issuecomment-38477",
    "user": "mhansen"
}
```

This is because the show method is written to deal only with images:


```
    def show(self, filename=None, ImageSize=600):
        """
        Show a mathematica plot in the Sage notebook.

        EXAMPLES:
            sage: P = mathematica('Plot[Sin[x],{x,-2Pi,4Pi}]')   # optional - mathematica
            sage: show(P)                                        # optional - mathematica
            sage: P.show(ImageSize=800)                          # optional - mathematica
        """
        P = self._check_valid()
        if filename is None:
            filename = graphics_filename()
        orig_dir = P.eval('Directory[]').strip()
        P.chdir(os.path.abspath("."))
        s = 'Export["%s", %s, ImageSize->%s]'%(filename, self.name(), ImageSize)
        P.eval(s)
        P.chdir(orig_dir)
```




---

archive/issue_comments_038478.json:
```json
{
    "body": "This was fixed by #5916.",
    "created_at": "2009-06-05T01:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5049#issuecomment-38478",
    "user": "mhansen"
}
```

This was fixed by #5916.



---

archive/issue_comments_038479.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-05T01:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5049#issuecomment-38479",
    "user": "mhansen"
}
```

Resolution: fixed
