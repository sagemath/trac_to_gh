# Issue 4126: [with patch; not ready for review] improve sage <--> magma interface for number fields

archive/issues_004126.json:
```json
{
    "body": "Assignee: was\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4126\n\n",
    "created_at": "2008-09-15T03:56:49Z",
    "labels": [
        "interfaces",
        "minor",
        "enhancement"
    ],
    "title": "[with patch; not ready for review] improve sage <--> magma interface for number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4126",
    "user": "was"
}
```
Assignee: was



Issue created by migration from https://trac.sagemath.org/ticket/4126





---

archive/issue_comments_029915.json:
```json
{
    "body": "Attachment\n\nadd sage number field --> magma number field conversion",
    "created_at": "2008-09-15T03:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4126#issuecomment-29915",
    "user": "was"
}
```

Attachment

add sage number field --> magma number field conversion



---

archive/issue_comments_029916.json:
```json
{
    "body": "Attachment\n\nThe part 3 patch that I applied does some re-architect-ing of the sage --> magma conversion system so now one can define either _magma_init_ in the very simple case when a pure string is enough or _magma_coerce_ when one wants to do arbitrarily complicated stuff but doesn't want to have to worry about caching. \n\n Caching turns out to be extremely important, e.g., coercing the same number field twice into magma without caching would result in two separate copies of that number field in Magma with no coercion maps, which would cause lots of problems for other things.  This re-architecting will surely be needed all over the place as the Magma / Sage interface gets steadily improved.\n\nIt's possible that the choices of names is not optimal.  Using _magma_coerce_ was better than anything else I could think of (e.g., _magma_not_cached_, _magma_impl_, etc.).",
    "created_at": "2008-09-19T04:40:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4126#issuecomment-29916",
    "user": "was"
}
```

Attachment

The part 3 patch that I applied does some re-architect-ing of the sage --> magma conversion system so now one can define either _magma_init_ in the very simple case when a pure string is enough or _magma_coerce_ when one wants to do arbitrarily complicated stuff but doesn't want to have to worry about caching. 

 Caching turns out to be extremely important, e.g., coercing the same number field twice into magma without caching would result in two separate copies of that number field in Magma with no coercion maps, which would cause lots of problems for other things.  This re-architecting will surely be needed all over the place as the Magma / Sage interface gets steadily improved.

It's possible that the choices of names is not optimal.  Using _magma_coerce_ was better than anything else I could think of (e.g., _magma_not_cached_, _magma_impl_, etc.).



---

archive/issue_comments_029917.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-09-19T04:55:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4126#issuecomment-29917",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_029918.json:
```json
{
    "body": "Looks good to me. This looks like it's more magma -> sage (I can't get number fields back into Sage for example), but that doesn't look like the intent of the ticket. \n\nIn terms of naming, perhaps _magma_convert_ would be another alternative (coercion happens implicitly, conversion only when explicitly asked for). The caching architecture looks fine.",
    "created_at": "2008-09-25T00:39:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4126#issuecomment-29918",
    "user": "robertwb"
}
```

Looks good to me. This looks like it's more magma -> sage (I can't get number fields back into Sage for example), but that doesn't look like the intent of the ticket. 

In terms of naming, perhaps _magma_convert_ would be another alternative (coercion happens implicitly, conversion only when explicitly asked for). The caching architecture looks fine.



---

archive/issue_comments_029919.json:
```json
{
    "body": "Replying to [comment:3 robertwb]:\n> Looks good to me. This looks like it's more magma -> sage (I can't get number fields back into Sage for example), but that doesn't look like the intent of the ticket. \n> \n> In terms of naming, perhaps _magma_convert_ would be another alternative (coercion happens implicitly, conversion only when explicitly asked for). The caching architecture looks fine. \n\nSo the rename would turn this into a positive review?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-25T00:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4126#issuecomment-29919",
    "user": "mabshoff"
}
```

Replying to [comment:3 robertwb]:
> Looks good to me. This looks like it's more magma -> sage (I can't get number fields back into Sage for example), but that doesn't look like the intent of the ticket. 
> 
> In terms of naming, perhaps _magma_convert_ would be another alternative (coercion happens implicitly, conversion only when explicitly asked for). The caching architecture looks fine. 

So the rename would turn this into a positive review?

Cheers,

Michael



---

archive/issue_comments_029920.json:
```json
{
    "body": "The comment that magma -> sage is not implemented rather than unintentionally broken, and a comment on the name change (doesn't have to change, just looks like William was looking for ideas).",
    "created_at": "2008-09-25T00:46:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4126#issuecomment-29920",
    "user": "robertwb"
}
```

The comment that magma -> sage is not implemented rather than unintentionally broken, and a comment on the name change (doesn't have to change, just looks like William was looking for ideas).



---

archive/issue_comments_029921.json:
```json
{
    "body": "Attachment\n\nrespond to referee remark",
    "created_at": "2008-09-25T18:15:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4126#issuecomment-29921",
    "user": "was"
}
```

Attachment

respond to referee remark



---

archive/issue_comments_029922.json:
```json
{
    "body": "I've posted a patch that makes the change robert suggests, which I like. \n\nAnd indeed, this was definitely not meant to be feature complete, but a first self-contained step before I do a lot more that uses the same architecture.",
    "created_at": "2008-09-25T18:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4126#issuecomment-29922",
    "user": "was"
}
```

I've posted a patch that makes the change robert suggests, which I like. 

And indeed, this was definitely not meant to be feature complete, but a first self-contained step before I do a lot more that uses the same architecture.



---

archive/issue_comments_029923.json:
```json
{
    "body": "I'm happy with the code.",
    "created_at": "2008-09-25T19:03:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4126#issuecomment-29923",
    "user": "robertwb"
}
```

I'm happy with the code.



---

archive/issue_comments_029924.json:
```json
{
    "body": "Attachment\n\nThe following two hunks\n\n```\n@@ -5300,6 +5301,14 @@\n         return NumberField_cyclotomic_v1, (self.__n, self.variable_name())\n\n     def _magma_init_(self):\n+        # TODO: I really don't like this on multiple levels.\n+        # (1) it kills a global symbol self.gen()\n+        # (2) it abuses how conversion works and throws in an extra define.\n+        # (3) a cyclo field in a funny generator wouldn't get converted to\n+        #     one with the right name via this.\n+        # (4) One should define _magma_coerce_ instead of _magma_init_\n+        #     in this case, probably.\n+        #    -- William\n         return 'CyclotomicField(%s); %s:=CyclotomicField(%s).1;'%(self.__n, self.gen(), self.__n)\n\n     def _repr_(self):\n```\n\nand\n\n```\n@@ -5306,7 +5306,7 @@\n         # (2) it abuses how conversion works and throws in an extra define.\n         # (3) a cyclo field in a funny generator wouldn't get converted to\n         #     one with the right name via this.\n-        # (4) One should define _magma_coerce_ instead of _magma_init_\n+        # (4) One should define _magma_convert_ instead of _magma_init_\n         #     in this case, probably.\n         #    -- William\n         return 'CyclotomicField(%s); %s:=CyclotomicField(%s).1;'%(self.__n, self.gen(), self.__n)\n```\n\ndid not apply cleanly against my merge tree, so I committed them manually. Patch is attached.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T05:05:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4126#issuecomment-29924",
    "user": "mabshoff"
}
```

Attachment

The following two hunks

```
@@ -5300,6 +5301,14 @@
         return NumberField_cyclotomic_v1, (self.__n, self.variable_name())

     def _magma_init_(self):
+        # TODO: I really don't like this on multiple levels.
+        # (1) it kills a global symbol self.gen()
+        # (2) it abuses how conversion works and throws in an extra define.
+        # (3) a cyclo field in a funny generator wouldn't get converted to
+        #     one with the right name via this.
+        # (4) One should define _magma_coerce_ instead of _magma_init_
+        #     in this case, probably.
+        #    -- William
         return 'CyclotomicField(%s); %s:=CyclotomicField(%s).1;'%(self.__n, self.gen(), self.__n)

     def _repr_(self):
```

and

```
@@ -5306,7 +5306,7 @@
         # (2) it abuses how conversion works and throws in an extra define.
         # (3) a cyclo field in a funny generator wouldn't get converted to
         #     one with the right name via this.
-        # (4) One should define _magma_coerce_ instead of _magma_init_
+        # (4) One should define _magma_convert_ instead of _magma_init_
         #     in this case, probably.
         #    -- William
         return 'CyclotomicField(%s); %s:=CyclotomicField(%s).1;'%(self.__n, self.gen(), self.__n)
```

did not apply cleanly against my merge tree, so I committed them manually. Patch is attached.

Cheers,

Michael



---

archive/issue_comments_029925.json:
```json
{
    "body": "Merged all five patches in Sage 3.1.3.alpha2",
    "created_at": "2008-09-26T05:06:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4126#issuecomment-29925",
    "user": "mabshoff"
}
```

Merged all five patches in Sage 3.1.3.alpha2



---

archive/issue_comments_029926.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-26T05:06:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4126#issuecomment-29926",
    "user": "mabshoff"
}
```

Resolution: fixed
