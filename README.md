# Wellnergie — website redesign

Static site, no framework. Everything the browser needs is inside `site/`.

```
site/
  index.html          home (hero slider + featured products)
  shop.html           all 12 products with category filters
  product/*.html      one page per product (gallery, options, description, functions, specs)
  technology.html     about.html   faq.html   testimonials.html   contact.html
  css/style.css       design tokens + all styling
  js/main.js          slider, header, mobile menu, gallery, filters, accordions
  assets/             product photos (from wellnergie.com), hero images, logo variants
build.py              generates every HTML page from the product data inside it
site_images.json      list of product image files per product (used by build.py)
```

## Editing content

- Product names, prices, descriptions, functions, specs, colours: edit `PRODUCTS` in `build.py`, then run `python3 build.py`.
- Page copy (home, technology, about, FAQ, contact, testimonials): edit the `page_*` functions in `build.py`.
- Colours / fonts / spacing: the `:root` tokens at the top of `site/css/style.css`.
- Hero slides: the `slides` list in `page_home()`; images live in `site/assets/hero/`.

## Preview locally

```bash
python3 -m http.server 8765 --directory site
```

Then open http://localhost:8765.

## Reviews and testimonials

- Video testimonials: the `TESTIMONIALS` list in `build.py` (YouTube ID, title). Thumbnails live in `site/assets/testimonials/`.
- Google reviews: the `GOOGLE_REVIEWS` list in `build.py` (name, stars, when, text), plus `GOOGLE_RATING` and `GOOGLE_COUNT`. Paste more reviews there and rebuild. Both the home slider and the Testimonials page read from it.
- Product ratings on shop cards: add `rating=5, reviews=4` to a product in `PRODUCTS` to show stars; add `compare=259` to show a strike-through price and a Sale badge.

## Notes

- "Add to cart" links to the matching product page on the existing Wix store, so checkout keeps working until the new site gets its own cart.
- The contact form opens the visitor's email client addressed to wellnergie@gmail.com. Swap it for a form service (Formspree, Netlify Forms, etc.) when hosting.
- Fonts are loaded from Google Fonts: Outfit (headlines), Roboto (body, the Colantotte font), Instrument Serif (italic accents).
- Colours: white page, very dark maroon (`--maroon` in `style.css`) for the hero, header text, headings, the technology callout and the footer.
