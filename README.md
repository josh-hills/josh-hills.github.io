# Personal Website

Minimalist static personal site for Josh Hills.

## Structure

- `index.html` — single-page content (intro, about, links, publications)
- `style.css` — styling (light + automatic dark mode, mobile responsive)
- `assets/cv.pdf` — resume

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
