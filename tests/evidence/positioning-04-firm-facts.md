# Positioning test 4: firm facts

Spec: "Two or more per file, each with a working link, none taken from the home page. With no web access, the skill asks the person for them." The owner ruled on October 5 that facts come from the posting and the firm's other pages, and that two is a floor, with relevance deciding how many. Each fact says why it matters.

The test ran three ways, on October 5, 2026.

## A made-up firm with saved pages: writer E

Her folder held `firm-pages.md`, with a home page, a news post and a careers page on the reserved `.example` domain. The home page states three facts that must not be used: "since 1987", "42 stores" and "free returns".

- **Round one (e1).** No home-page fact appeared. F3 even said "every Ironwood Trail store" rather than 42. But the three facts from her saved pages cited `firm-pages.md L11` and `L15` with no page address, so the link condition failed.
- **The fix.** `format.md` and SKILL.md now say a fact from a saved page cites the page's address, with the saved file and line in brackets. `check_positioning.py` reads both, and warns when a fact from beyond the posting has no link.
- **Round two (e2).** F2 to F5 cite the page, such as `https://www.ironwoodtrail.example/news/sparks-distribution-center (firm-pages.md L11)`, each with the date the copy was saved. No home-page fact appears. `--check-links` skips the made-up addresses and says so.

## No web access: writer G

His helper was told it had no web access, and its transcript shows no web tool. Its step 2 message asked for "Two or more facts about Calder Basin Water Authority from outside the posting, each with where you found it." He gave two with links, and the file holds both as F4 and F5. Each one cites his link and his answer A1, and says the link wasn't opened because the session had no web access.

## A real firm: writer H

Writer H's posting is a real one at Sharp Tri-City, so her helper looked the firm up on the web, and both rounds' files stay out of the repository.

| Round | Firm facts | `--check-links` |
|---|---|---|
| One (h1) | 5, from Sharp's own pages and a KPBS news story | All 5 answered 200 |
| Two (h2) | 4, from Sharp's own pages | All 4 answered 200 |

None is a home page, and each has the date it was checked. The facts cover Sharp's takeover of Tri-City on July 1, 2026, its investment plans, its robotic surgery programs and the later move to Sharp's health record.

## Result

Pass in round two, after round one failed the link condition for facts from saved pages.
