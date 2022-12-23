# Issue 1891: remove workaround when Pari > 2.3.3 is released

archive/issues_001891.json:
```json
{
    "body": "Assignee: craigcitro\n\nTo fix trac #1083, I added a workaround due to a bug in Pari. The code is fixed in their svn version, but it's unlikely that we'll see a new release terribly soon. However, when one comes along, someone should go to sage/rings/number_field/number_field.py and undo the following patch:\n\n-        g = self.__rnf.rnfeltabstorel(pari(f))\n+        if self.__K.degree() == 1:\n+            g = -1*self.__rnf[0][0]*f[1] + f[0]\n+        else:\n+            g = self.__rnf.rnfeltabstorel(pari(f))\n\nOr, if whoever is updating the pari spkg sends me an email, I'll take care of this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1891\n\n",
    "created_at": "2008-01-23T11:25:28Z",
    "labels": [
        "packages: standard",
        "trivial",
        "enhancement"
    ],
    "title": "remove workaround when Pari > 2.3.3 is released",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1891",
    "user": "craigcitro"
}
```
Assignee: craigcitro

To fix trac #1083, I added a workaround due to a bug in Pari. The code is fixed in their svn version, but it's unlikely that we'll see a new release terribly soon. However, when one comes along, someone should go to sage/rings/number_field/number_field.py and undo the following patch:

-        g = self.__rnf.rnfeltabstorel(pari(f))
+        if self.__K.degree() == 1:
+            g = -1*self.__rnf[0][0]*f[1] + f[0]
+        else:
+            g = self.__rnf.rnfeltabstorel(pari(f))

Or, if whoever is updating the pari spkg sends me an email, I'll take care of this.

Issue created by migration from https://trac.sagemath.org/ticket/1891





---

archive/issue_comments_011976.json:
```json
{
    "body": "Is this already fixed?  According to\n\n```sh\n$ grep rnfeltabstorel `find -name \\*.py\\*`\n./libs/pari/gen.pyx:    def rnfeltabstorel(self, x):\n./rings/number_field/number_field_rel.py:        poly_xy = self.pari_rnf().rnfeltabstorel( self(element)._pari_() )\n./rings/number_field/maps.py:        g = self.__rnf.rnfeltabstorel(pari(f))\n```\n\nBut I don't see nearby code similar to that in the description.  However, I'm definitely not an expert.",
    "created_at": "2010-02-02T05:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1891#issuecomment-11976",
    "user": "mpatel"
}
```

Is this already fixed?  According to

```sh
$ grep rnfeltabstorel `find -name \*.py\*`
./libs/pari/gen.pyx:    def rnfeltabstorel(self, x):
./rings/number_field/number_field_rel.py:        poly_xy = self.pari_rnf().rnfeltabstorel( self(element)._pari_() )
./rings/number_field/maps.py:        g = self.__rnf.rnfeltabstorel(pari(f))
```

But I don't see nearby code similar to that in the description.  However, I'm definitely not an expert.



---

archive/issue_comments_011977.json:
```json
{
    "body": "Well, the workaround is for the case where the degree of the relative number field is one, and it's definitely still present -- several of us fought with that code just a few weeks ago. So I think we still need this ticket.",
    "created_at": "2010-02-02T18:46:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1891#issuecomment-11977",
    "user": "craigcitro"
}
```

Well, the workaround is for the case where the degree of the relative number field is one, and it's definitely still present -- several of us fought with that code just a few weeks ago. So I think we still need this ticket.



---

archive/issue_comments_011978.json:
```json
{
    "body": "Oops!  I apologize.  Time for me to read a book...",
    "created_at": "2010-02-02T20:58:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1891#issuecomment-11978",
    "user": "mpatel"
}
```

Oops!  I apologize.  Time for me to read a book...



---

archive/issue_comments_011979.json:
```json
{
    "body": "Is this still valid?\n\n\n```\nsage: gp.version()\n((2, 3, 5), 'GP/PARI CALCULATOR Version 2.3.5 (released)')\n```\n",
    "created_at": "2010-06-24T15:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1891#issuecomment-11979",
    "user": "lftabera"
}
```

Is this still valid?


```
sage: gp.version()
((2, 3, 5), 'GP/PARI CALCULATOR Version 2.3.5 (released)')
```




---

archive/issue_comments_011980.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-06-25T04:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1891#issuecomment-11980",
    "user": "craigcitro"
}
```

Resolution: wontfix



---

archive/issue_comments_011981.json:
```json
{
    "body": "Well, I don't think this ticket is valid anymore -- but not because Pari fixed the issue. Does anyone know if this works in Pari unstable (2.4.x)?",
    "created_at": "2010-06-25T04:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1891#issuecomment-11981",
    "user": "craigcitro"
}
```

Well, I don't think this ticket is valid anymore -- but not because Pari fixed the issue. Does anyone know if this works in Pari unstable (2.4.x)?
