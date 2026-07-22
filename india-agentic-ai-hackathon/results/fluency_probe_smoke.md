# Language fluency probe

- started_utc: 20260721T031058Z
- languages_config: `/home/sidharth/Desktop/nvidia-hack/india-agentic-ai-hackathon/configs/synthetic-data/languages.yaml`
- language_count: 2
- models: `sarvam-105b`
- prompt: 5–6 fluent lines per language (clinic / mild fever)

---

## `hi` — Hindi (Devanagari) · model `sarvam-105b`

- elapsed_s: 1.3
- status: OK
- script_purity: PASS
- script_purity_detail: ok

```text
कल से हल्का बुखार लग रहा था।
आज सुबह उठते ही शरीर में दर्द होने लगा।
मैंने पास के ही क्लीनिक में जाने का फैसला किया।
डॉक्टर ने मुझे चेक किया और कुछ दवाएं दे दीं।
अब थोड़ा आराम महसूस हो रहा है।
उम्मीद है कल तक मैं ठीक हो जाऊँगा।
```

## `ta` — Tamil (Tamil) · model `sarvam-105b`

- elapsed_s: 0.9
- status: OK
- script_purity: PASS
- script_purity_detail: ok

```text
நேற்று இரவு எனக்கு லேசான காய்ச்சல் வந்தது.
காலையில் எழுந்து பார்த்தபோது உடல் சூடு இருந்தது.
மருத்துவமனைக்குச் சென்று பார்த்தேன்.
மருத்துவர் மருந்து கொடுத்தார்.
இப்போது உடல் கொஞ்சம் சரியாக இருக்கிறது.
```

---

# Summary

- ok: 2
- errors: 0
- script_purity_pass: 2
- script_purity_fail: 0
- output: `results/fluency_probe_smoke.md`
