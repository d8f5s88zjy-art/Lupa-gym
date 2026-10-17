---
name: ai-marketing-tim
description: AI marketingový tím pre GYM KLUB Nitra (a podobné lokálne prevádzky) – výskum reklám konkurencie, texty a videá reklám, príspevky na sociálne siete, zachytenie záujemcov z komentárov, rezervácie do kalendára a ranný súhrn. Použi, keď používateľ chce reklamy, kampaň, príspevky na Instagram/TikTok/Facebook, viac zákazníkov, marketingový plán alebo „AI tím na sociálne siete“.
---

# AI marketingový tím

Postup podľa videa @restructureai „I Built an AI Social Media Team That Runs Your Entire Marketing“
(https://vm.tiktok.com/ZN8SX2bt9/), upravený na nástroje, ktoré má táto relácia naozaj k dispozícii,
a na slovenské pravidlá. Údaje o prevádzke a hotové návrhy sú v `references/gym-klub.md`.

## Tri pravidlá, ktoré sa neporušujú

1. **Nič nejde von bez schválenia.** Každá reklama, príspevok, e-mail zákazníkovi aj publikovanie na
   TikTok sa najprv ukáže majiteľovi a čaká na „áno“. Povolenie „na všetko“ platí na prípravu, nie na
   zverejnenie konkrétneho kusu, ktorý ešte nevidel.
2. **Rozpočet je strop.** Pred každou platenou akciou (generovanie videa, reklamy) zisti cenu
   (`ads_studio_quote`, `balance`, `max_credits`) a nikdy neprekroč sumu, ktorú majiteľ určil.
3. **Len skutočné fakty a súhlas.** Ceny, hodiny a ponuka iba z `references/gym-klub.md` alebo z
   `index.html`. Žiadne vymyslené recenzie ani „zľava končí dnes“, ak to nie je pravda. Telefonovať
   alebo písať človeku smieš len vtedy, keď na to dal výslovný súhlas (GDPR); bez súhlasu iba odpoveď
   tam, kde sa pýtal.

## Moduly

### 1. Výskum (čo funguje u konkurencie)
- Cez WebSearch nájdi fitká v Nitre a okolí (napr. Chrenová, Klokočina, centrum) a ich verejné
  reklamy v Meta Ad Library (`facebook.com/ads/library`, krajina SK).
- Reklama, ktorá beží **týždne**, pravdepodobne zarába – z nej si zapíš háčik (prvá veta / prvé 2 s),
  ponuku, formát (video, foto, karusel) a výzvu.
- Výstup: tabuľka 5–10 víťazných vzorov + čo z toho prevziať pre GYM KLUB (bez kopírovania textov).

### 2. Tvorba reklám
- Texty: z víťazných vzorov napíš 20 variantov (rôzne háčiky pre rôzne publiká – začiatočník,
  bojové športy, ženy/sebaobrana, dôchodcovia, študenti). Šablóna a prvých 10 je v referencii.
- Videá a obrázky (Higgsfield, nástroje `mcp__Samuel_Pavelka__*`):
  - fotky prevádzky sú v `assets/img/f/` a videá v `assets/video/` – nahraj ich cez `media_upload`
    → `media_confirm`, nie vymyslené zábery,
  - reklamy z produktu/miesta: `show_marketing_studio_v2` alebo `ads_studio_*` (najprv `ads_studio_quote`),
  - krátke video z fotky: `generate_video` (pri nejasnosti `models_explore` s `action: "recommend"`),
  - hlas: `generate_audio` (rôzny hlas pre rôzne reklamy), hodnotenie pred spustením: `virality_predictor`.
- Ukáž majiteľovi všetko naraz v jednom prehľade (môže byť Artifact s náhľadmi) a nechaj ho vybrať.

### 3. Spustenie a optimalizácia
- TikTok: `tiktok_accounts` → `tiktok_prepare_publish` → po schválení publikovanie → `tiktok_publish_status`.
- Meta (Instagram/Facebook) reklamy: **nie sú pripojené** – priprav balík (texty, videá, cieľenie:
  Nitra + 10 km, 16–55 r., záujmy fitness/bojové športy) a návod na Ads Manager krok za krokom.
- Test 48 hodín na 3–5 variantoch s rovnakým denným rozpočtom, potom rozpočet presunúť na
  1–2 najlepšie podľa ceny za kontakt (nie podľa lajkov). Celkovo nikdy nad týždenný limit.

### 4. Záujemcovia z komentárov a správ
- Čítanie komentárov a DM na Instagrame/Facebooku/TikToku **nie je pripojené**. Kým nebude, priprav
  majiteľovi hotové odpovede na časté otázky (cena, hodiny, parkovanie, treba sa objednať?, prvá
  návšteva, MMA/Krav Maga/MDS rozvrh) – sú v referencii.
- Označ za „kupujúceho“ každého, kto sa pýta na cenu, permanentku, termín alebo „môžem prísť dnes?“.
  Odpoveď vždy končí jednou výzvou: príďte (adresa + hodiny) alebo zavolajte +421 944 800 394.

### 5. Predaj a rezervácie
- Termíny (prvý tréning s trénerom, kurz Ladydefence, Krav Maga) zapisuj do Google Calendar
  (`mcp__Google_Calendar__suggest_time` → `create_event`) až po potvrdení majiteľom.
- E-maily záujemcom: `mcp__Gmail__create_draft` – koncept, nie `send_message`, kým ho majiteľ neschváli.
- Automatické hovory (ElevenLabs agent z videa) tu nie sú. Namiesto toho: pripomienka majiteľovi
  „zavolaj späť do hodiny“ – rýchlosť odpovede je to, čo vo videu predáva.

### 6. Ranný súhrn
- Naplánovaná úloha (`create_trigger`, ráno v Europe/Bratislava, nie presne o celej) pripraví súhrn na
  jednu stranu: čo beží, koľko to stálo, koľko kontaktov/rezervácií, čo čaká na schválenie, 1 odporúčanie.
- Zdroje, ktoré sú pripojené: Gmail (dopyty na info@gymklub.sk), Google Calendar (rezervácie),
  TikTok (`tiktok_publish_status`). Čo pripojené nie je, v súhrne povedz rovno („Meta dáta: zadať ručne“).

## Postup, keď používateľ povie „sprav kampaň“

1. Spýtaj sa len na to, čo nevieš: týždenný rozpočet a cieľ (noví členovia, MMA, Ladydefence…).
2. Modul 1 → modul 2 (texty zadarmo hneď, platené videá až po potvrdení ceny).
3. Prehľad na schválenie → modul 3.
4. Ponúkni ranný súhrn (modul 6), ak ešte nebeží.

## Čo chýba na plnú automatizáciu ako vo videu

Meta Ads API, čítanie komentárov/DM (Instagram, Facebook, TikTok), hlasový agent na hovory
(ElevenLabs alebo podobný) a CRM na kontakty. Kým nie sú pripojené, tieto kroky robí majiteľ
s pripravenými podkladmi – nikdy ich nepredstieraj ako hotové.
