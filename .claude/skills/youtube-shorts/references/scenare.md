# Scenáre, šablóny a strih

## Lokálny strih – `scripts/make_short.py` (zadarmo, overené)

```bash
python3 -I .claude/skills/youtube-shorts/scripts/make_short.py \
  --out short.mp4 --captions titulky.txt [--audio hlas.mp3] [--sec 2.5] \
  assets/img/f/recepcia-1-1080.jpg assets/video/zapasenie.mp4 ...
```

- Výstup: 1080×1920, 30 fps, H.264 + AAC, `faststart` – priamo na YouTube Shorts aj TikTok.
- Fotky dostanú pomalý nájazd/odjazd kamery, videá sa orežú na 9:16.
- Titulky (`titulky.txt`): `začiatok|koniec|text`, `*slovo*` = limetkové zvýraznenie (farba GYM KLUB).
  Ukážka: `examples/gymklub-6eur.txt` (15 s, 6 záberov, ~20 s renderu).
- S hlasom: najprv vyrob hlas, zisti dĺžku (`ffprobe -show_entries format=duration`), nastav časy
  titulkov podľa viet a `--sec` = dĺžka / počet záberov.
- Kontrola: vytiahni pár snímok (`ffmpeg -ss 4 -i short.mp4 -frames:v 1 f.jpg`) a pozri si ich –
  či sa zábery menia a titulky sú čitateľné a v strede.

## Šablóna scenára (vyplň)

```
NÁZOV (≤100 znakov): <kľúčové slovo> – <sľub>
DĹŽKA: <30–60 s>  ZÁBERY: <počet>

0–2 s   HÁČIK:        <odvážne tvrdenie / výsledok>           text na obrazovke: <2–4 slová>
2–6 s   DÔVERA:       <číslo – čas, cena, počet>
6–10 s  POISTKA:      <zadarmo / bez objednávania / bez rizika>
10–45 s KROKY 1–4:    <rovnaký rytmus vety, každý krok = výsledok>
45–50 s VRCHOL:       <súčet alebo kontrast>
50–55 s VÝZVA:        <ulož si / odoberaj / príď> (jedna)

POPIS: <1–2 vety> #shorts #<téma> #<miesto>
```

## Hotové scenáre – GYM KLUB Nitra

Fakty len z `index.html` (ceny a rozvrh overiť pred každým natáčaním).

### 1. „Stačí prísť. Vstup 6 €.“ (15 s, bez hlasu, len titulky + hudba z knižnice)
Hotové titulky: `examples/gymklub-6eur.txt`. Zábery: recepcia → hlavná sála → stroje → zápasenie (video)
→ funkčná zóna → terasa. Výzva v popise: „Výstavná 6, Lipa Centrum. Príďte dnes.“

### 2. „Prvýkrát vo fitku? Takto to u nás prebieha.“ (~35 s, hlas)
- 0–2: „Bojíte sa ísť prvýkrát do fitka? Nemusíte.“
- 2–6: „V GYM KLUBE v Nitre sa nič neobjednáva. Vstup 6 eur.“
- 6–10: „Pri prvej návšteve len 3 eurá za klubovú kartičku.“
- 10–28: „Krok jedna: prídete kedykoľvek od šiestej do deviatej. Krok dva: zaplatíte hotovosťou alebo
  kartou, MultiSport ukážete. Krok tri: tréner vám nastaví techniku aj plán.“
- 28–32: „Žiadne zmluvy, žiadne pózovanie pred zrkadlom.“
- 32–35: „Ulož si to a príď tento týždeň. Výstavná 6, Lipa Centrum.“

### 3. „Sebaobrana v Nitre – 3 tréningy, ktoré nepoznáš“ (~40 s)
Krav Maga (Po a Pi 17:00, Slavo Juro) · Mastro Defence System (Po a St 17:00–20:00, Tomáš Židek) ·
MMA, Jiu Jitsu, Luta Livre (Ut a Št 17:00, So 13:00, Michal Šášik). Zábery: `assets/video/mds.mp4`,
`zapasenie.mp4`, `ladydefence.mp4`. Výzva: „Ktorý by si skúsil? Napíš do komentára.“
Pred zverejnením: súhlas ľudí, ktorí sú vo videách.

### 4. „Permanentka sa oplatí od 3 tréningov týždenne“ (~25 s, čísla na obrazovke)
6 € × 3 × 4,3 týždňa ≈ 77 € vs. permanentka 50 €. Študent 42 €, dôchodca 35 €.
Výzva: „Pošli to kamošovi, s ktorým chceš začať.“

## Hotový scenár – AI nástroje (vzor z videa o ECC, po slovensky)

„Tento plugin z teba spraví celý programátorský tím. Zadarmo.“ (~50 s)
- 0–3: „Jeden vývojár dal na GitHub zadarmo celý programátorský tím.“
- 3–8: „Volá sa ECC – 71 agentov a 311 skillov pre Claude Code, Cursor aj Codex.“ (čísla overiť v deň natáčania)
- 8–16: „Inštalácia za 30 sekúnd: lomka plugin marketplace add, potom lomka plugin install ecc.“
  (na obrazovke presne: `/plugin marketplace add https://github.com/affaan-m/ECC` a `/plugin install ecc@ecc`)
- 16–40: „Povieš *plan* – navrhne architektúru. Povieš *build* – napíše kód. Povieš *secure* – zaútočí
  na vlastnú aplikáciu. Povieš *test* – nepustí ťa, kým nemáš 80 % pokrytie.“
- 40–46: „Celý tím, nula eur.“
- 46–50: „Ulož si to a odoberaj pre ďalšie AI nastavenia.“
Zábery: nahrávka obrazovky (inštalácia + výstup) – tú musí natočiť používateľ alebo sa vyrobí
v termináli a nahrá; AI generované „hackerské“ zábery len ako B-roll.
