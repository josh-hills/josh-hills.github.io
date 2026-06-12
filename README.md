# Personal Website

Minimalist static personal site for Josh Hills.

## Structure

- `index.html` — single-page content (header, about, icon links, publications)
- `style.css` — design system (warm light + dark theme toggle, mobile responsive)
- `assets/cv.pdf` — resume
- `assets/profile.jpg` — portrait shown beside the about text
  (**currently a generated placeholder — replace with a real headshot**,
  ~180×220 or any portrait ratio)
- `assets/figures/` — publication thumbnails
- `assets/og.png` — social/link preview image

The visual design mirrors
[hrdkbhatnagar.github.io](https://hrdkbhatnagar.github.io/) (Newsreader /
Instrument Serif / Manrope, warm palette, dashed dividers, left-aligned
publication thumbnails), rebuilt as a dependency-free static page.

## Local preview

Open `index.html` directly in a browser, or serve it:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Deploy to GitHub Pages

For a user site at `https://josh-hills.github.io`, the repository **must** be
named `josh-hills.github.io`:

```bash
git init
git add .
git commit -m "Initial personal website"
git branch -M main
git remote add origin https://github.com/josh-hills/josh-hills.github.io.git
git push -u origin main
```

Then in the repo: **Settings → Pages → Build and deployment → Source: Deploy
from a branch → `main` / `root`**. The site goes live within a minute or two.

## Updating content

Edit the text in `index.html`. Publications live in the
`<section class="publications">` block — copy an existing `<article class="pub">`
to add a new entry. Replace `assets/cv.pdf` to update the resume.

## SEO

The site is built to help Google recognize "Josh Hills" as a distinct entity:

- **Structured data** (`Person` JSON-LD in `index.html`) with a `sameAs` array
  linking GitHub, Google Scholar, and LinkedIn. This is the strongest signal for
  consolidating your online profiles into one knowledge entity.
- **Meta tags**: descriptive `<title>`, meta description, canonical URL.
- **Open Graph / Twitter cards** + `assets/og.png` for rich link previews.
- `robots.txt` and `sitemap.xml`.

After the site is live, do these (they materially speed up ranking):

1. **Google Search Console** (https://search.google.com/search-console): add
   `https://josh-hills.github.io/` as a property, verify ownership, submit
   `sitemap.xml`, and use "URL Inspection → Request Indexing" on the homepage.
2. **Bing Webmaster Tools**: same process for Bing.
3. **Backlinks (most impactful off-page factor)**: add the URL to your LinkedIn
   "Contact info / Website", GitHub profile, Google Scholar homepage field, and
   any paper author pages or lab pages. Consistent links from those high-authority
   profiles back to this site reinforce the entity connection.
4. Keep the name spelled consistently ("Josh Hills") across all profiles.

### To regenerate the OG image

```bash
python3 scripts/make_og.py   # see commit history; uses Pillow
```
