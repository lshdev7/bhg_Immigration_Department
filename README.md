# bhg_Immigration_Department
백현화랑 특별행정구 정부 출입경사무처(이민국) 홈페이지

Website of the Immigration Department of the Baekhyeon Hwarang Special Administrative Region, in English,
Korean, Traditional Chinese and Simplified Chinese. The government one-stop portal (GovBHG,
https://github.com/lshdev7/BHG) links here for travel documents, identity cards and immigration e-services.

The layout follows the Hong Kong Immigration Department website and its e-service start page; all code,
artwork and wording are original.

## Contents

| Path | Purpose |
|---|---|
| `en/` `ko/` `zh-hant/` `zh-hans/` | Generated site per language |
| `services/travel-documents/apply-passport/` | Application for passport (Before / Applying / After tabs) |
| `services/travel-documents/{photo,fees,faq,kiosk,docid,reentry,seaman}/` | Travel document information |
| `eservices/passport-application/` | Online passport application (start page + 8 steps) |
| `eservices/travel-document-booking/`, `eservices/idcard-booking/` | Appointment booking (5 steps, change / cancel) |
| `eservices/travel-document-status/`, `eservices/application-status/` | Status enquiries |
| `tools/build.py` | Generator; content in `tools/data_*.py` |

## Build

```sh
python3 tools/build.py
```

Static HTML/CSS/JS (Python 3.6+). Served by GitHub Pages from the `main` branch root.
