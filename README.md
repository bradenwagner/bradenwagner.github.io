# Braden Wagner

Personal academic website for Braden Wagner, a Ph.D. student in Economics at the University of Virginia.

The site is published at [bradenwagner.github.io](https://bradenwagner.github.io).

## Content

- `_pages/about.md` — homepage and contact information
- `_pages/research.md` — research interests and work
- `_pages/cv.md` — concise web CV
- `files/braden-wagner-cv.pdf` — downloadable PDF CV
- `_config.yml` — site identity, links, and metadata
- `_data/navigation.yml` — header navigation

## Editing the site

- Edit the large homepage introduction, cards, button labels, destinations, and contact text in `_pages/about.md`.
- Edit the header link names, order, and destinations in `_data/navigation.yml`.
- Edit the profile photo, email, department, and social links in the `author` section of `_config.yml`. Leave a value blank to hide that link.
- Edit the body of the Research and CV pages in their corresponding files under `_pages/`.
- Edit the custom colors, cards, buttons, spacing, and typography near the bottom of `assets/css/main.scss`.

Internal links use paths such as `/research/`. External links use a complete address such as `https://example.com`. Link text is the text between the opening and closing `<a>` tags in HTML, or the text in square brackets in Markdown.

### Updating the PDF CV

Replace `files/braden-wagner-cv.pdf` with the new PDF, keeping the same filename so every download link on the site continues to work.

## Local development

Install Ruby and Bundler, then run:

```sh
bundle install
bundle exec jekyll serve
```

The site is based on the [Academic Pages](https://academicpages.github.io/) Jekyll theme and is published through GitHub Pages from the `master` branch.
