# Issue 7618: notebook -- make it easy to configure keyboard shortcuts

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-08 07:10:06

Assignee: was

CC:  chapoton


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



---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by dimpase created at 2020-08-25 09:31:41

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-08-29 15:27:58

Resolution: invalid
