# Issue 7618: notebook -- make it easy to configure keyboard shortcuts

archive/issues_007618.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @fchapoton\n\n\n```\nTom:\n>> It's really easy to configure the keyboard shortcuts -- perhaps that\n>> should be an entry in the settings page?\n\nWilliam:\n> Yes, definitely.  Could you post some remarks in an email about how\n> you think adding keyboard shortcut configuration should be\n> implemented... and probably I'll implement it as a result.\n\nTom Boothby:\nWell, right now there's some functionality to statically change the\nkeyboard shortcuts through config.py.  IIRC, there's a global\ndictionary of keyboard shortcuts which establishes a mapping\n\n'name' -> [(modifier1, key1), (modifier2, key2), ... ]\n\nand when the user requests the main javascript file, this is compiled\ninto javascript.\n\nI think that it'd be easy to implement this for users -- from their\nsettings page, they could override the server's config.py.  If the\nuser had a dictionary  similar to the above, that would be loaded\nafter the global config.  This would give the user an opportunity to\nadd or override shortcuts.\n\n\nFor example, say the global configuration results in\n\nShortcuts = { 'eval' : [('shift', 'enter')], 'break cell':\n[('ctrl','semicolon')]}\n\nBut, the user also wants shift-tab to break cells.  So, they go to the\nshortcuts settings page, scroll down to the \"break cell\", and add that\nentry.  Now, their settings would contain (for example... I have no\nidea how the settings are implemented)\n\nuser.settings['shortcuts'] = {'break cell' : [('ctrl','semicolon'),\n('shift','tab')]}\n\nNote that they haven't modified 'eval', so that doesn't get put into\ntheir settings.  This way the user's settings dictionary is spliced\ninto the global settings when we render the javascript (so new\nfeatures will work without the user manually adding them).\n\nNote that the input handler (I think) always returns once it's\nidentified a shortcut as having been pressed, so we don't need to\ncheck if a particular shortcut is unique.  Otherwise, it could be\ngreat fun to map everything to a master \"do everything always\" key.\nMaybe an unmodified spacebar.\n\nI think that the actual input form for this should be pretty\nself-explanatory -- but I can describe what I'm thinking for that too,\nif you want.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7618\n\n",
    "created_at": "2009-12-08T07:10:06Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook -- make it easy to configure keyboard shortcuts",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7618",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @fchapoton


```
Tom:
>> It's really easy to configure the keyboard shortcuts -- perhaps that
>> should be an entry in the settings page?

William:
> Yes, definitely.  Could you post some remarks in an email about how
> you think adding keyboard shortcut configuration should be
> implemented... and probably I'll implement it as a result.

Tom Boothby:
Well, right now there's some functionality to statically change the
keyboard shortcuts through config.py.  IIRC, there's a global
dictionary of keyboard shortcuts which establishes a mapping

'name' -> [(modifier1, key1), (modifier2, key2), ... ]

and when the user requests the main javascript file, this is compiled
into javascript.

I think that it'd be easy to implement this for users -- from their
settings page, they could override the server's config.py.  If the
user had a dictionary  similar to the above, that would be loaded
after the global config.  This would give the user an opportunity to
add or override shortcuts.


For example, say the global configuration results in

Shortcuts = { 'eval' : [('shift', 'enter')], 'break cell':
[('ctrl','semicolon')]}

But, the user also wants shift-tab to break cells.  So, they go to the
shortcuts settings page, scroll down to the "break cell", and add that
entry.  Now, their settings would contain (for example... I have no
idea how the settings are implemented)

user.settings['shortcuts'] = {'break cell' : [('ctrl','semicolon'),
('shift','tab')]}

Note that they haven't modified 'eval', so that doesn't get put into
their settings.  This way the user's settings dictionary is spliced
into the global settings when we render the javascript (so new
features will work without the user manually adding them).

Note that the input handler (I think) always returns once it's
identified a shortcut as having been pressed, so we don't need to
check if a particular shortcut is unique.  Otherwise, it could be
great fun to map everything to a master "do everything always" key.
Maybe an unmodified spacebar.

I think that the actual input form for this should be pretty
self-explanatory -- but I can describe what I'm thinking for that too,
if you want.
```


Issue created by migration from https://trac.sagemath.org/ticket/7618





---

archive/issue_comments_064990.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7618#issuecomment-64990",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064991.json:
```json
{
    "body": "Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7618#issuecomment-64991",
    "user": "https://github.com/mkoeppe"
}
```

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.



---

archive/issue_comments_064992.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-08-25T09:31:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7618#issuecomment-64992",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064993.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-08-29T15:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7618#issuecomment-64993",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
