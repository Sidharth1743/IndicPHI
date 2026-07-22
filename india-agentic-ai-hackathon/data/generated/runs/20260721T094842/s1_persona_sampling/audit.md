# Stage 1 — Persona Sampling Audit

- timestamp_utc: `2026-07-21T04:18:44.635419+00:00`
- dataset: `nvidia/Nemotron-Personas-India` split=`en_IN`
- seed: `1301`
- rows_scanned: **90910** / max `250000`
- personas_selected: **23**
- docs_per_persona: `3`
- expected_documents_downstream: **69**

## By language

| code | name | script | selected | matched_during_scan |
|------|------|--------|----------|---------------------|
| as | Assamese | Bengali | 1 | 1178 |
| bn | Bengali | Bengali | 1 | 7719 |
| brx | Bodo | Devanagari | 1 | 110 |
| doi | Dogri | Devanagari | 1 | 188 |
| en | English | Latin | 1 | 14 |
| gu | Gujarati | Gujarati | 1 | 4419 |
| hi | Hindi | Devanagari | 1 | 38165 |
| kn | Kannada | Kannada | 1 | 3474 |
| ks | Kashmiri | Arabic | 1 | 431 |
| kok | Konkani | Devanagari | 1 | 203 |
| mai | Maithili | Devanagari | 1 | 867 |
| ml | Malayalam | Malayalam | 1 | 3106 |
| mni | Manipuri | Meitei | 1 | 128 |
| mr | Marathi | Devanagari | 1 | 5184 |
| ne | Nepali | Devanagari | 1 | 230 |
| or | Odia | Odia | 1 | 2967 |
| pa | Punjabi | Gurmukhi | 1 | 2740 |
| sa | Sanskrit | Devanagari | 1 | 2 |
| sat | Santali | Ol Chiki | 1 | 520 |
| sd | Sindhi | Arabic | 1 | 205 |
| ta | Tamil | Tamil | 1 | 5918 |
| te | Telugu | Telugu | 1 | 6729 |
| ur | Urdu | Arabic | 1 | 3739 |

## Demographics (selected)

- sex: `{'Male': 14, 'Female': 9}`
- zone: `{'Rural': 13, 'Urban': 10}`
- age: min=`18` max=`79` mean=`38.17391304347826`
- state_top20: `{'Odisha': 4, 'Assam': 2, 'Bihar': 2, 'Jammu & Kashmir': 2, 'Uttar Pradesh': 2, 'Andhra Pradesh': 2, 'Maharashtra': 2, 'Gujarat': 1, 'Goa': 1, 'Kerala': 1, 'Manipur': 1, 'Himachal Pradesh': 1, 'Haryana': 1, 'Tamil Nadu': 1}`
- occupation_top20: `{'No Occupation / Retired / Homemaker': 8, 'Tappers, Other': 1, 'Salesman, Retail Trade': 1, 'Salt Reclamation Worker': 1, 'Labourer, Other': 1, 'Caretaker, Burial Places and Cremation Grounds': 1, 'Steward, Hotel': 1, 'Garbage Collectors, Other': 1, 'Heavy Truck and Lorry Drivers, Other': 1, 'Fisherman, Deep Sea': 1, 'Loader and Unloader': 1, 'Market-Oriented Crop and Animal Producers, Other': 1, 'Sports Goods Maker, Wood': 1, 'Plasterer': 1, 'Stall and Market Salespersons, Other': 1, 'Tobacco Curer': 1}`
- persona_source_shard: `{'en_IN-00000-of-00011.parquet': 23}`

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
