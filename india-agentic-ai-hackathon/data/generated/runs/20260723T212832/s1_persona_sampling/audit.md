# Stage 1 — Persona Sampling Audit

- timestamp_utc: `2026-07-23T15:58:35.175647+00:00`
- dataset: `nvidia/Nemotron-Personas-India` split=`en_IN`
- seed: `3031`
- rows_scanned: **90910** / max `250000`
- personas_selected: **46**
- docs_per_persona: `3`
- expected_documents_downstream: **138**

## By language

| code | name | script | selected | matched_during_scan |
|------|------|--------|----------|---------------------|
| as | Assamese | Bengali | 2 | 1178 |
| bn | Bengali | Bengali | 2 | 7719 |
| brx | Bodo | Devanagari | 2 | 110 |
| doi | Dogri | Devanagari | 2 | 188 |
| en | English | Latin | 2 | 14 |
| gu | Gujarati | Gujarati | 2 | 4419 |
| hi | Hindi | Devanagari | 2 | 38165 |
| kn | Kannada | Kannada | 2 | 3474 |
| ks | Kashmiri | Arabic | 2 | 431 |
| kok | Konkani | Devanagari | 2 | 203 |
| mai | Maithili | Devanagari | 2 | 867 |
| ml | Malayalam | Malayalam | 2 | 3106 |
| mni | Manipuri | Meitei | 2 | 128 |
| mr | Marathi | Devanagari | 2 | 5184 |
| ne | Nepali | Devanagari | 2 | 230 |
| or | Odia | Odia | 2 | 2967 |
| pa | Punjabi | Gurmukhi | 2 | 2740 |
| sa | Sanskrit | Devanagari | 2 | 2 |
| sat | Santali | Ol Chiki | 2 | 520 |
| sd | Sindhi | Arabic | 2 | 205 |
| ta | Tamil | Tamil | 2 | 5918 |
| te | Telugu | Telugu | 2 | 6729 |
| ur | Urdu | Arabic | 2 | 3739 |

## Demographics (selected)

- sex: `{'Female': 30, 'Male': 16}`
- zone: `{'Urban': 21, 'Rural': 25}`
- age: min=`18` max=`79` mean=`39.869565217391305`
- state_top20: `{'Maharashtra': 6, 'Assam': 5, 'West Bengal': 5, 'Karnataka': 5, 'Jammu & Kashmir': 4, 'Gujarat': 3, 'Odisha': 3, 'Jharkhand': 2, 'Kerala': 2, 'Manipur': 2, 'Punjab': 2, 'Tamil Nadu': 2, 'Madhya Pradesh': 1, 'Goa': 1, 'Bihar': 1, 'Rajasthan': 1, 'Uttar Pradesh': 1}`
- occupation_top20: `{'No Occupation / Retired / Homemaker': 19, 'Cultivator, General': 1, 'Screener, Mica': 1, 'Sales Supervisor, Retail Trade': 1, 'Hawker': 1, 'Police Officers, Other': 1, 'Tailors and Dress Makers, Other': 1, 'Shop Attendant': 1, 'Farm Overseer, Crop Production': 1, 'Tappers, Other': 1, 'Teacher, Infant School Pre-Primary Education Teaching Associate Professionals, Other': 1, 'Market-Oriented Crop and Animal Producers, Other': 1, 'Wood Working Machine Operatives, Other': 1, 'Caretaker, Building': 1, 'Mono Operator': 1, 'Keypunch Operator': 1, 'Supervisor, Jewellery, Engraving and Precision Metal Workers': 1, 'Labourer, Other': 1, 'Ordained Religious Workers, Other': 1, 'Operator, Call Centre': 1}`
- persona_source_shard: `{'en_IN-00000-of-00011.parquet': 46}`

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
