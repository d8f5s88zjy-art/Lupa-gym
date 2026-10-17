# GYM KLUB Nitra (Lipa Gym)

Web pre **GYM KLUB Fitness & Bodybuilding**, Výstavná 6 (Lipa Centrum), 949 01 Nitra-Chrenová. Čisté HTML, CSS a JavaScript, bez build kroku a bez externých závislostí. Beží na GitHub Pages, nasadenie robí `.github/workflows/pages.yml` pri každom pushi do `main`. Pri presune na vlastnú doménu v `index.html` upraviť `canonical`, `og:url` a `og:image` (miesto je označené komentárom `DEPLOY STEP`).

## Kde sa čo upravuje

- **Otváracie hodiny, rozvrh lekcií a sviatky:** `index.html`, skript hneď za úvodom (`GK.HOURS`, `GK.TIMETABLE`, `GK.HOLIDAYS`). Stav „Otvorené do …“ sa počíta podľa času v Bratislave.
- **Kontakty a odkazy** (telefón, e-mail, mapa, Instagram, Facebook): `assets/app.js`, objekt `GYM`.
- **Tréneri:** sekcia `#treneri` v `index.html`, fotky v `assets/img/tim/` (`meno.jpg/.webp/.avif` 480 × 600 a `meno-320.*`). Počet vo filtri sa prepočíta sám.
- **Cenník, recenzie, otázky:** priamo v `index.html`.

## Štruktúra stránky

Úvod s fotografiou z prevádzky, výber „Čo je o vás?“, pás s ponukou, prečo GYM KLUB, funkčná zóna, prechádzka priestorom (11 záberov) a ďalšie zábery s lightboxom, tréningy a lekcie s ukážkou zápasenia, blok Mastro Defence System s ukážkami a kurzom Ladydefence, tréneri s filtrom, rozvrh, cenník a prvá návšteva, recenzie, otázky a kontakt s mapou.

## Súbory

- `assets/style.css` – štýly, tmavá paleta s limetkovým akcentom
- `assets/app.js` – údaje o prevádzke, rozvrh, filter trénerov, lightbox, videá, mapa načítaná až pri posune, animácie, schema.org
- `assets/depth.js` – priestorový efekt fotiek na počítači (WebGL, hĺbkové mapy v `assets/img/d/`); na telefóne, slabých zariadeniach a pri obmedzení pohybu sa nepoužije
- `assets/img/f/` – fotografie prevádzky vo formátoch AVIF, WebP a JPG v niekoľkých veľkostiach
- `assets/img/tim/` – portréty trénerov, `assets/img/mds-logo-*` – logo Mastro Defence System, `logo-gymklub.png`
- `assets/video/` – ukážky z tréningov (MP4 a WebM s náhľadom)
- `assets/fonts/` – písma hostované lokálne (licencia OFL)

## Zdroj údajov

Fakty pochádzajú z oficiálneho webu **gymklub.sk** a od majiteľa prevádzky. Fotografie a videá sú výlučne z prevádzky GYM KLUB.

## Marketing

`.claude/skills/ai-marketing-tim/` – postup pre Claude na reklamy, príspevky, odpovede záujemcom a ranný súhrn (podľa videa „AI Social Media Team“). Fakty, cenník, rozvrh a prvých 10 návrhov reklám sú v `references/gym-klub.md`. Na web sa nenasadzuje.

`.claude/skills/youtube-shorts/` – tvorba YouTube Shorts a TikTokov: vzorec scenára z virálnych videí, rozbor videí, hotové scenáre pre GYM KLUB a skript `scripts/make_short.py`, ktorý z fotiek, videí a titulkov zloží video 1080 × 1920 (len ffmpeg).
