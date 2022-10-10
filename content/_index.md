---
TAGS:
  - TYPE/hub
  - STATUS/ok
---

![[media/waves.jpg]]

## Helpful links

- [[! Meta - Vault Guide]]
- [[! Meta - Tag Disambiguation]]

## Best Files

```dataview
table
	file.ctime as "Created",
	file.mtime as "Modified"
from #STATUS/great
sort file.mtime desc
```

## TODO

Uses Dataview to list all files tagged with `STATUS/todo` and aggregate their `TODO ::` keys.

```dataview
table
	TODO as "TODO",
	file.mtime as "Modified"
from #STATUS/todo
```