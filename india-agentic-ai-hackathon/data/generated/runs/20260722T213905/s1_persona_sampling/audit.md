# Stage 1 — Persona Sampling Audit

- timestamp_utc: `2026-07-22T16:09:07.559532+00:00`
- dataset: `nvidia/Nemotron-Personas-India` split=`en_IN`
- seed: `4042`
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

- sex: `{'Male': 16, 'Female': 7}`
- zone: `{'Rural': 16, 'Urban': 7}`
- age: min=`18` max=`68` mean=`34.391304347826086`
- state_top20: `{'Maharashtra': 3, 'Bihar': 3, 'Assam': 2, 'Jammu & Kashmir': 2, 'Nagaland': 2, 'Odisha': 2, 'West Bengal': 1, 'Gujarat': 1, 'Karnataka': 1, 'Goa': 1, 'Kerala': 1, 'Punjab': 1, 'Uttar Pradesh': 1, 'Tamil Nadu': 1, 'Andhra Pradesh': 1}`
- occupation_top20: `{'No Occupation / Retired / Homemaker': 9, 'Model, Fashion': 1, 'Telemarketing Sales Person': 1, 'Building Construction Labourers, Other': 1, 'Carpenter, Construction': 1, 'Dress Diver': 1, 'Bee-keeper': 1, 'Labourer, Other': 1, 'Manager, Poultry Farm': 1, 'Bill and Accounts Collector': 1, 'Rearer, Silkworm': 1, 'Horse Carriage Driver': 1, 'Picker (Tobacco)': 1, 'Petrol Pump Salesman': 1, 'Supervisors and Foremen and Related Trades Workers in Painting, Building Structure': 1}`
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
