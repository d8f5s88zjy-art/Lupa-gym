# GYM KLUB Nitra (Lipa Gym)

Web pre **GYM KLUB Fitness & Bodybuilding**, Výstavná 6 (Lipa Centrum), 949 01 Nitra-Chrenová. Čisté HTML, CSS a JavaScript, bez build kroku a bez externých závislostí. Beží na GitHub Pages, nasadenie robí `.github/workflows/pages.yml` pri každom pushi do `main`. Pri presune na vlastnú doménu v `index.html` upraviť `canonical`, `og:url` a `og:image` (miesto je označené komentárom `DEPLOY STEP`).

## Zdroj údajov

Všetky fakty pochádzajú z oficiálneho webu **gymklub.sk** (stav 19. 9. 2026) a zo zadania klienta. Nič nie je vymyslené:

| Údaj | Hodnota | Zdroj |
|---|---|---|
| Názov | GYM KLUB Fitness & Bodybuilding | gymklub.sk |
| Adresa | Výstavná 6 (Lipa Centrum), 949 01 Nitra, Chrenová | gymklub.sk/contact.html |
| Telefón, e-mail | +421 944 800 394, info@gymklub.sk | gymklub.sk |
| Hodiny | Po až Št 06:30 – 21:00, Pi 06:30 – 23:00, So a Ne 08:00 – 17:00 | gymklub.sk (kontakt, FAQ, harmonogram); pätička webu uvádza pre víkend 08:30 – 18:00, preto je na stránke poznámka „cez víkend overte telefonicky“ |
| Cenník | vstup 6 €, permanentka 50 €/mesiac, študentská 42 €/mesiac, 10 vstupov 50 €, 20 vstupov 80 €, študent 5 €, dôchodca 3,50 €; platba len v hotovosti; MultiSport a Upbalansea app | gymklub.sk, sekcia Cenník a FAQ |
| Rozvrh | Po Pilates 16:00 a Krav Maga 17:00, Ut a Št Bojové športy 17:00 a Zdravý chrbát 18:00, St Pilates 18:00, So Bojové športy 13:00 | gymklub.sk, časový harmonogram |
| Tréneri (10) | mená, špecializácie, fotografie, telefóny a popisy | gymklub.sk/treneri.html a stránky tréningov |
| Recenzie (4) | Nika D., Jozef K., Andrea F., Marcel Š. | gymklub.sk, sekcia Recenzie |
| Fotografie | výlučne zábery z prevádzky: 10 fotografií priestoru (aj pri tréningoch), 10 portrétov trénerov, logo | gymklub.sk |
| Sociálne siete | Instagram gymklubnitra, Facebook | gymklub.sk |

Kontakty, hodiny a rozvrh sú na jednom mieste v `assets/app.js` (`GYM`, `HOURS`, `TIMETABLE`); z nich sa vypĺňa stránka aj štruktúrované dáta (schema.org HealthClub s hodinami, cenníkom a trénermi, FAQPage).

## Štruktúra

- `index.html` – úvod (fotografia z prevádzky, zapnutie svetiel, nájazd kamery), bežiaci pás, dôvody, 6 tréningov s fotografiami, cenník (3 karty + tabuľka + podmienky), rozvrh s dňami a živým stavom otvorené, 10 trénerov s filtrom podľa disciplíny, galéria 9 fotografií s lightboxom, prvá návšteva, recenzie, otázky, kontakt s mapou, hodinami a formulárom
- `assets/style.css` – štýly, tmavá paleta s limetkovou, Bebas Neue + Manrope
- `assets/app.js` – údaje o prevádzke, živé hodiny (Bratislava), rozvrh, filter trénerov, lightbox, formulár (otvorí pripravený e-mail na info@gymklub.sk, nič neukladá), mapa načítaná až pri posune, animácie, koľajnica, zotrvačné skrolovanie, schema.org
- `assets/img/` – fotografie prevádzky (`hero`, `stojany`, `rig`, `cardio`, `ring`, `stroje`, `recepcia`, `rig2`, `tatami`, `bar`, `about`) s mobilnými variantmi `-640`, `tim/` portréty trénerov (+ `-320`), `logo-gymklub.png`; každý obrázok v JPG aj WebP
- `assets/fonts/` – Bebas Neue a Manrope lokálne

## Animácie

- **Otvorenie (zapnutie svetiel):** úvod je pri načítaní tmavý, svetlá dvakrát bliknú a zostanú svietiť, po hale prejde odlesk, kamera 12 sekúnd pomaly nabieha a nadpis vybehne po riadkoch. Preskočí sa klikom do úvodu, pri obmedzení pohybu, pri odkaze na sekciu a pri druhom načítaní v tej istej karte.
- **Skrolovacia vrstva:** obrysové kotúče a činka v pozadí plynú rôznou rýchlosťou, za nadpismi sekcií plávajú obrysové nápisy, nadpisy nabiehajú podľa skrolu, bežiaci pás sa pri rýchlom skrole nakloní, vpravo koľajnica s kotúčom a bodkami sekcií.
- **Zotrvačné skrolovanie** kolieskom na počítači (`SMOOTH_SCROLL` v `app.js`), odkazy na sekcie idú tou istou cestou, dotyk a klávesnica ostávajú natívne.
- **Telefón (odľahčený režim, `body.lite`):** na dotykových zariadeniach a do šírky 860 px nebeží pohyblivé pozadie, obrysové nápisy, paralaxa ani nájazd kamery, obrázky sa berú v menších variantoch (`*-640`, `tim/*-320`) a sekcie mimo obrazovky sa nevykresľujú (`content-visibility`). Zapnutie svetiel ostáva ako prelínanie priehľadnosti.
- **Plynulosť:** žiadne filtre na hýbucich sa prvkoch, `will-change` na vrstvách, premenná postupu len na prvkoch, ktoré ju používajú, lišta bez rozostrenia na mobile.
- Pri zapnutom **obmedzení pohybu** je všetko statické a nič sa neschováva.

## Kontakt a formulár

Hlavná akcia je „Prísť si zacvičiť“ (kontakt s hodinami, mapou a navigáciou) a „Pozrieť cenník“. Na telefóne je dole lišta Zavolať a Cenník a vstup. Formulár „Napíšte nám“ pripraví e-mail do klientovho programu, web nič neukladá ani neposiela.

## Náhľad

```
npx http-server -p 8080
```

a otvoriť `http://localhost:8080/`.
