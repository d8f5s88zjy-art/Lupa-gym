# GYM KLUB Nitra

Web pre **GYM KLUB Fitness & Bodybuilding**, Výstavná 6 (Lipa Centrum), 949 01 Nitra-Chrenová.
Čisté HTML, CSS a JavaScript bez build kroku. Zverejnený na GitHub Pages: https://d8f5s88zjy-art.github.io/Lupa-gym/
(nasadenie robí `.github/workflows/pages.yml` pri každom pushi do `main`).

- `index.html` – celá stránka; otváracie hodiny, rozvrh lekcií a sviatky sú v skripte hneď za úvodom (`window.GK`)
- `assets/app.js` – kontakty prevádzky (`GYM`), rozvrh, tréneri, filmový pás, galéria, štruktúrované dáta
- `assets/depth.js` – priestorové fotky (hĺbkové mapy v `assets/img/d`)
- `assets/style.css`, `assets/fonts.css`, `assets/fonts/` – vzhľad a písma
- `assets/img/f` – fotky prevádzky (avif, webp, jpg), `assets/img/tim` – tréneri

Fakty (ceny, hodiny, rozvrh, tréneri, recenzie) pochádzajú z gymklub.sk. Víkendové hodiny sú na gymklub.sk uvedené
rozdielne, preto web pri víkende a sviatkoch vždy píše „overte telefonicky“.
Zdroj vývoja: repozitár head-spa-30, priečinok `lipa-gym`.
