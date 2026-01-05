---
name: Translation / Sync PR
about: Use this template for PRs created by the upstream sync to request translations and deployment of `zh-tw` branch

---

## Summary

Automated sync from upstream/master. Please review changed files and translate content into Traditional Chinese (zh-TW) as appropriate.

## Checklist

- [ ] Confirm that AIP front-matter (id, permalink, state, created, etc.) is preserved
- [ ] Translate all updated `.md` content into `zh-TW` and commit to `zh-tw` branch
- [ ] Verify relative links and permalinks work after translation
- [ ] Run site build locally (`./serve.sh`) and verify the translated pages render correctly
- [ ] Run Prettier / formatting for Markdown
- [ ] Add `translation-in-progress` label when starting and `translation-done` when finished

## Notes for translators

- Keep code blocks and example requests unchanged (translate only comments and human-facing text)
- Prefer consistent terminology; follow existing translations for previously translated AIPs
- If the change is trivial (typo, small wording) consider applying the patch directly to `zh-tw`

