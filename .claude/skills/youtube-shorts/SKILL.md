---
name: youtube-shorts
description: Tvorba YouTube Shorts (aj TikTok a Reels) od nápadu po hotové video 9:16 – háčik, scenár podľa overenej štruktúry virálnych videí, hlas, titulky, strih cez ffmpeg alebo Higgsfield, názov, popis a kontrola pred zverejnením. Použi, keď používateľ chce short, krátke video, reel, TikTok, scenár na video, alebo pošle TikTok/Shorts odkaz, z ktorého sa treba naučiť formát.
---

# YouTube Shorts

Naučené z dvoch virálnych videí, ktoré poslal používateľ (rozbor v `references/rozbor-videi.md`).
Hotové scenáre a šablóny sú v `references/scenare.md`.

## Ako sa učiť z nového odkazu (TikTok, Shorts, Reels)

Video ako obraz nevidíš – ber z neho text a čísla:
1. `curl -sSL -A "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)" <odkaz>` → v HTML je
   `<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__">` s JSON: `desc`, `duration`, autor, `subtitleInfos`
   (URL titulkov WebVTT – stiahni anglickú alebo pôvodnú verziu). Kód skriptu drž v scratchpade, HTML
   spúšťaj cez `python3 -I`.
2. Rozpíš video do štruktúry nižšie (háčik / tvrdenie / dôkaz / kroky / vrchol / výzva) s časmi.
3. **Over fakty** (WebSearch, oficiálne README) – virálne videá často zastarajú alebo preháňajú
   (príklad: video o ECC tvrdí 64 agentov a 261 skillov, README už uvádza 71 a 311).
4. Zapíš rozbor do `references/rozbor-videi.md` a ak prinesie nový vzorec, doplň ho do tohto súboru.

## Formát

- **9:16, 1080 × 1920**, 30 alebo 60 fps, H.264 + AAC. Shorts môže mať až 3 minúty, ale cieľ je
  **30–60 s** (overené videá: 54 s a 97 s; kratšie sa lepšie dopozerajú a opakujú).
- Dôležitý obsah drž v strede – hore (~250 px) a dole (~400 px) prekrýva rozhranie YouTube.
- **Titulky natvrdo vo videu** vždy (väčšina pozerá bez zvuku): 2–4 slová naraz, veľké, s obrysom,
  zvýraznené kľúčové slovo.
- Strih každé 1–3 s (nový záber, zoom, text, B-roll). Žiadna statická scéna dlhšia ako 3 s.
- Koniec sa má plynulo napojiť na začiatok, aby sa video prehralo znova (slučka).

## Štruktúra scenára (vzorec z oboch videí)

| Čas | Časť | Čo tam patrí | Príklad z videí |
|---|---|---|---|
| 0–2 s | **Háčik** | odvážne tvrdenie alebo výsledok, ktorý divák chce | „Jeden chlap práve nahradil celý váš programátorský tím…“ |
| 2–6 s | **Dôveryhodnosť** | konkrétne číslo, čas, námaha | „200 hodín práce“, „sám za 10 mesiacov, 250 000 hviezdičiek“ |
| 6–10 s | **Poistka / zadarmo** | odstráni námietku | „zadarmo na GitHube“, „nič nejde von, kým to neschválite“ |
| 10–45 s | **Kroky** | 3–4 očíslované moduly, každý = jedna veta s výsledkom | „Povedz *plan* → … Povedz *build* → … Povedz *secure* → …“ |
| 45–50 s | **Vrchol** | najsilnejší dôsledok alebo súčet | „64 agentov, 261 skillov, všetko zadarmo.“ / „nie viac followerov, viac zákazníkov“ |
| posledné 2–3 s | **Výzva** | uložiť / sledovať / komentovať (jedna) | „Ulož si tento postup a sleduj ma pre ďalšie…“ |

Pravidlá textu:
- Hovorená reč, krátke vety, **každá veta posúva** (žiadne „ahojte, vitajte na kanáli“).
- Opakujúci sa rytmus pri krokoch („Povedz X a… Povedz Y a…“) – divák vie, čo príde, a pozerá ďalej.
- Konkrétne čísla namiesto prívlastkov („do 60 sekúnd“, nie „rýchlo“).
- Pre YouTube Shorts výzva „odoberaj“ namiesto „follow“.

## Výroba – nástroje v tejto relácii

1. **Scenár** – napíš sám podľa štruktúry; pri dĺžke počítaj ~2,5 slova za sekundu (SK).
2. **Hlas** – `mcp__Samuel_Pavelka__generate_audio` (text → reč), alebo nahrávka používateľa.
3. **Zábery**
   - vlastné fotky/videá (napr. GYM KLUB: `assets/img/f/`, `assets/video/`) – nahrať cez
     `media_upload` → `media_confirm`,
   - AI video z fotky: `generate_video` (model vyber cez `models_explore` s `action: "recommend"`),
   - hotový short z podkladov: `shorts_studio_list_presets` → `shorts_studio_create` → `shorts_studio_status`,
   - **každá platená generácia: najprv cena (`balance`, odhad/`max_credits`) a súhlas používateľa.**
4. **Strih a titulky lokálne (zadarmo)** – `ffmpeg` je nainštalovaný; recept v `references/scenare.md`.
   Alternatíva: Descript (`import_media` → `prompt_project_agent` „pridaj titulky, odstráň pauzy“ →
   `publish_project`).
5. **Kontrola** – `virality_predictor` na hotové video (háčik, udržanie pozornosti), oprav slabé miesto.
6. **Zverejnenie**
   - YouTube nie je pripojený → odovzdaj používateľovi hotové MP4 (`SendUserFile`) + názov, popis,
     hashtagy a postup nahratia (YouTube app → + → Short, alebo YouTube Studio).
   - TikTok je pripojený: `tiktok_accounts` → `tiktok_prepare_publish` → po schválení → `tiktok_publish_status`.

## Kontrola pred zverejnením

- [ ] Háčik je zrozumiteľný bez zvuku v prvej sekunde (text na obrazovke)
- [ ] Fakty a čísla overené k dnešnému dňu; ceny a hodiny len zo zdroja (pri GYM KLUB `index.html`)
- [ ] Hudba len z knižnice YouTube/TikTok alebo vlastná (inak Content ID a stlmený zvuk)
- [ ] Realistický AI obsah (AI hlas skutočnej osoby, vymyslené reálne udalosti) → pri nahrávaní
      zaškrtnúť „Altered or synthetic content“
- [ ] Nikto vo videu bez súhlasu (cvičiaci vo fitku!), žiadne cudzie logá ako vlastné
- [ ] Názov ≤ 100 znakov, kľúčové slovo na začiatku; popis 1–2 vety + 3–5 hashtagov vrátane `#shorts`
- [ ] Používateľ video videl a schválil – **nič nezverejňuj sám**
