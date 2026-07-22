# Stage 1 — Persona Sampling Audit

- timestamp_utc: `2026-07-21T14:01:32.605718+00:00`
- dataset: `nvidia/Nemotron-Personas-India` split=`en_IN`
- seed: `2027`
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

- sex: `{'Male': 23, 'Female': 23}`
- zone: `{'Urban': 18, 'Rural': 28}`
- age: min=`18` max=`80` mean=`39.04347826086956`
- state_top20: `{'Karnataka': 6, 'West Bengal': 5, 'Maharashtra': 5, 'Jammu & Kashmir': 4, 'Bihar': 4, 'Assam': 3, 'Gujarat': 3, 'Kerala': 2, 'Manipur': 2, 'Odisha': 2, 'Punjab': 2, 'Rajasthan': 2, 'Andhra Pradesh': 1, 'Madhya Pradesh': 1, 'Uttar Pradesh': 1, 'Jharkhand': 1, 'Tamil Nadu': 1, 'Telangana': 1}`
- occupation_top20: `{'No Occupation / Retired / Homemaker': 17, 'Working Proprietor, Wholesale Trade': 1, 'Senior Secondary and Secondary School Teacher, Commerce': 1, 'Packer, Hand': 1, 'Labeller': 1, 'Gatherer, Medicinal Herbs': 1, 'Darner': 1, 'Tailors and Dress Makers, Other': 1, 'Poultry Farm Worker, General': 1, 'Transport Equipment Operators and Drivers, Other': 1, 'Stall and Market Salespersons, Other': 1, 'Cardtenter, Cotton': 1, 'Handwork Teacher': 1, 'Driver, Bus': 1, 'Sales Supervisor, Wholesale Trade': 1, 'Hand Embroiderer, Kamdani': 1, 'Labourer, Other': 1, 'Sports Goods Maker, Wood': 1, 'Sewer, Hand': 1, 'House Keeper (Domestic)': 1}`
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
