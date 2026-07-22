# Stage 1 — Persona Sampling Audit

- timestamp_utc: `2026-07-21T07:25:28.386032+00:00`
- dataset: `nvidia/Nemotron-Personas-India` split=`en_IN`
- seed: `101`
- rows_scanned: **90910** / max `250000`
- personas_selected: **5**
- docs_per_persona: `1`
- expected_documents_downstream: **5**

## By language

| code | name | script | selected | matched_during_scan |
|------|------|--------|----------|---------------------|
| hi | Hindi | Devanagari | 1 | 38165 |
| bn | Bengali | Bengali | 1 | 7719 |
| ta | Tamil | Tamil | 1 | 5918 |
| sd | Sindhi | Arabic | 1 | 205 |
| mai | Maithili | Devanagari | 1 | 867 |

## Demographics (selected)

- sex: `{'Female': 3, 'Male': 2}`
- zone: `{'Rural': 3, 'Urban': 2}`
- age: min=`19` max=`56` mean=`34.4`
- state_top20: `{'West Bengal': 1, 'Delhi': 1, 'Bihar': 1, 'Gujarat': 1, 'Tamil Nadu': 1}`
- occupation_top20: `{'No Occupation / Retired / Homemaker': 2, 'Market-Oriented Crop and Animal Producers, Other': 1, 'Professional Nurses, Other': 1, 'Telemarketing Sales Person': 1}`
- persona_source_shard: `{'en_IN-00000-of-00011.parquet': 5}`

## Observed first_language in scan (all values)

- Hindi: 38165
- Bengali: 7719
- Telugu: 6729
- Tamil: 5918
- Marathi: 5184
- Gujarati: 4419
- Urdu: 3739
- Kannada: 3474
- Malayalam: 3106
- Odia: 2967
- Punjabi: 2740
- Assamese: 1178
- Maithili: 867
- Bhili / Bhilodi: 713
- Santali: 520
- Kashmiri: 431
- Nepali: 230
- Sindhi: 205
- Konkani: 203
- Gondi: 192
- Dogri: 188
- Tulu: 184
- Kurukh / Oraon: 152
- Khandeshi: 133
- Manipuri: 128
- Ho: 111
- Bodo: 110
- Khasi: 90
- Mundari: 76
- Tripuri: 70
- Garo: 66
- Halabi: 56
- Korku: 54
- Lushai / Mizo: 53
- Kui: 51
- Miri / Mishing: 48
- Munda: 44
- Koya: 35
- Karbi / Mikir: 34
- Bhotia: 29
- Nissi / Dafla: 24
- Konyak: 24
- Savara: 23
- Mao: 20
- Kharia: 19
- Khond / Kondh: 19
- Malto: 18
- Thado: 18
- Ao: 18
- Kisan: 16
- Lotha: 16
- Tangkhul: 15
- English: 14
- Kolami: 13
- Dimasa: 12
- Tibetan: 12
- Adi: 11
- Angami: 11
- Rabha: 9
- Lahnda: 9
- Coorgi / Kodagu: 8
- Chakru / Chokri: 8
- Yimchungre: 7
- Kinnauri: 7
- Sangtam: 7
- Hmar: 6
- Kuki: 6
- Koda / Kora: 5
- Wancho: 5
- Khiemnungan: 5
- Zemi: 5
- Kabui: 5
- Liangmei: 5
- Zeliang: 5
- Phom: 4
- Anal: 4
- Jatapu: 4
- Zou: 4
- Mogh: 4
- Konda: 4
- Parji: 4
- Paite: 4
- Mishmi: 4
- Khezha: 4
- Koch: 4
- Rengma: 3
- Tangsa: 3
- Chang: 3
- Lakher: 3
- Nicobarese: 3
- Pochury: 3
- Pawi: 3
- Maram: 3
- Bishnupuriya: 2
- Halam: 2
- Sanskrit: 2
- Arabic / Arbi: 2
- Vaiphei: 2
- Deori: 2
- Afghani / Kabuli / Pashto: 2
- Gadaba: 1
- Sherpa: 1
- Lalung: 1
- Monpa: 1
- Limbu: 1
- Nocte: 1
- Tamang: 1
- Sema: 1
- Lepcha: 1
- Rai: 1
- Shina: 1
- Ladakhi: 1
