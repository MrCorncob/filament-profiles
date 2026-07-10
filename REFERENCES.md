# References

## `.bbsflmt` bundle format

A `.bbsflmt` file is a standard zip archive produced by Bambu Studio's filament config export. Structure observed across every bundle in this repo:

```
<bundle>.bbsflmt
├── bundle_structure.json
└── <Vendor>/
    └── <filament name> @<printer model> 0.4 nozzle.json   (one per compatible printer)
```

The internal `<Vendor>/` folder name matches the bundle's `filament_vendor` value (`TINMORRY` for every bundle in this repo today) -- it's independent of this repo's own on-disk `<Vendor>/<Printer>/` folder layout, which just happens to reuse the same vendor name.

`bundle_structure.json` fields:

| Field | Description |
|---|---|
| `bundle_id` | Internal id, format `<numeric-id>_<filament name>_<unix timestamp>` |
| `bundle_type` | Always `"filament config bundle"` in this repo |
| `filament_name` | Display name of the filament |
| `filament_vendor` | Array mapping vendor name (e.g. `TINMORRY`) to the relative path(s) of the profile JSON(s) inside the archive |
| `version` | Bambu Studio version the bundle was exported from |

Each per-printer profile JSON follows Bambu Studio's standard filament settings schema (the same keys used in Bambu Studio's built-in system filament profiles), including `filament_type`, `compatible_printers`, temperature/cooling/flow/retraction parameters, etc.

## Full profile inventory

| Folder | File | Filament | Type | Compatible printer | Studio version | Bundle id |
|---|---|---|---|---|---|---|
| profiles/BambuStudio/TINMORRY/A1 | TINMORRY PC GF.bbsflmt* | TINMORRY PC GF | PC | Bambu Lab A1 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PC GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1 | TINMORRY PET CF GF.bbsflmt* | TINMORRY PET CF GF | PET-CF | Bambu Lab A1 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PET CF GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1 | TINMORRY PET CF.bbsflmt* | TINMORRY PET CF | PET-CF | Bambu Lab A1 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PET CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1 | TINMORRY PETG CF GF.bbsflmt* | TINMORRY PETG CF GF | PETG-CF | Bambu Lab A1 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1 | TINMORRY PETG CF PP.bbsflmt* | TINMORRY PETG CF PP | PETG | Bambu Lab A1 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF PP_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1 | TINMORRY PETG CF.bbsflmt* | TINMORRY PETG CF | PETG-CF | Bambu Lab A1 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1 | TINMORRY PETG ECO.bbsflmt* | TINMORRY PETG ECO | PETG | Bambu Lab A1 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG ECO_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1 | TINMORRY PETG GF.bbsflmt* | TINMORRY PETG GF | PETG | Bambu Lab A1 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1 | TINMORRY PETG Galaxy.bbsflmt* | TINMORRY PETG Galaxy | PETG | Bambu Lab A1 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Galaxy_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1 | TINMORRY PETG HS.bbsflmt* | TINMORRY PETG HS | PETG | Bambu Lab A1 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG HS_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1 | TINMORRY PETG Marble.bbsflmt* | TINMORRY PETG Marble | PETG | Bambu Lab A1 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Marble_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1 | TINMORRY PETG Matte.bbsflmt* | TINMORRY PETG Matte | PETG | Bambu Lab A1 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Matte_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1 | TINMORRY PETG Metallic.bbsflmt* | TINMORRY PETG Metallic | PETG | Bambu Lab A1 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Metallic_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1 | TINMORRY PETG Sparkly.bbsflmt* | TINMORRY PETG Sparkly | PETG | Bambu Lab A1 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Sparkly_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1 | TINMORRY PLA CF.bbsflmt* | TINMORRY PLA CF | PLA-CF | Bambu Lab A1 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1 | TINMORRY PLA Galaxy.bbsflmt* | TINMORRY PLA Galaxy | PLA | Bambu Lab A1 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Galaxy_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1 | TINMORRY PLA Matte.bbsflmt* | TINMORRY PLA Matte | PLA | Bambu Lab A1 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Matte_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1 | TINMORRY PLA Silk.bbsflmt* | TINMORRY PLA Silk | PLA | Bambu Lab A1 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Silk_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1 | TINMORRY PLA.bbsflmt* | TINMORRY PLA | PLA | Bambu Lab A1 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1 | TINMORRY TPU 95a.bbsflmt* | TINMORRY TPU 95a | TPU | Bambu Lab A1 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU 95a_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1 | TINMORRY TPU GF.bbsflmt* | TINMORRY TPU GF | TPU | Bambu Lab A1 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1 | TINMORRY TPU.bbsflmt* | TINMORRY TPU | TPU | Bambu Lab A1 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1mini | TINMORRY PET CF GF.bbsflmt* | TINMORRY PET CF GF | PET-CF | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PET CF GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1mini | TINMORRY PET CF.bbsflmt* | TINMORRY PET CF | PET-CF | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PET CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1mini | TINMORRY PETG CF GF.bbsflmt* | TINMORRY PETG CF GF | PETG-CF | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1mini | TINMORRY PETG CF PP.bbsflmt* | TINMORRY PETG CF PP | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF PP_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1mini | TINMORRY PETG CF.bbsflmt* | TINMORRY PETG CF | PETG-CF | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1mini | TINMORRY PETG ECO.bbsflmt* | TINMORRY PETG ECO | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG ECO_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1mini | TINMORRY PETG GF.bbsflmt* | TINMORRY PETG GF | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1mini | TINMORRY PETG Galaxy.bbsflmt* | TINMORRY PETG Galaxy | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Galaxy_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1mini | TINMORRY PETG HS.bbsflmt* | TINMORRY PETG HS | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG HS_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1mini | TINMORRY PETG Marble.bbsflmt* | TINMORRY PETG Marble | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Marble_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1mini | TINMORRY PETG Matte.bbsflmt | TINMORRY PETG Matte | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY PETG Matte_1780301588 |
| profiles/BambuStudio/TINMORRY/A1mini | TINMORRY PETG Metallic.bbsflmt* | TINMORRY PETG Metallic | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Metallic_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1mini | TINMORRY PETG Sparkly.bbsflmt* | TINMORRY PETG Sparkly | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Sparkly_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1mini | TINMORRY PLA CF.bbsflmt* | TINMORRY PLA CF | PLA-CF | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1mini | TINMORRY PLA Galaxy.bbsflmt* | TINMORRY PLA Galaxy | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Galaxy_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1mini | TINMORRY PLA Matte.bbsflmt* | TINMORRY PLA Matte | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Matte_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1mini | TINMORRY PLA Silk.bbsflmt* | TINMORRY PLA Silk | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Silk_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1mini | TINMORRY PLA.bbsflmt* | TINMORRY PLA | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A1mini | TINMORRY TPU 95A.bbsflmt | TINMORRY TPU 95A | TPU | Bambu Lab A1 mini 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY TPU 95A_1782271111 |
| profiles/BambuStudio/TINMORRY/A1mini | TINMORRY TPU GF.bbsflmt* | TINMORRY TPU GF | TPU | Bambu Lab A1 mini 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A2L | TINMORRY PET CF GF.bbsflmt* | TINMORRY PET CF GF | PET-CF | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PET CF GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A2L | TINMORRY PET CF.bbsflmt* | TINMORRY PET CF | PET-CF | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PET CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A2L | TINMORRY PETG CF GF.bbsflmt* | TINMORRY PETG CF GF | PETG-CF | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG CF GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A2L | TINMORRY PETG CF PP.bbsflmt* | TINMORRY PETG CF PP | PETG | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG CF PP_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A2L | TINMORRY PETG CF.bbsflmt* | TINMORRY PETG CF | PETG-CF | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A2L | TINMORRY PETG ECO.bbsflmt | TINMORRY PETG ECO | PETG | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG ECO_1780887719 |
| profiles/BambuStudio/TINMORRY/A2L | TINMORRY PETG GF.bbsflmt* | TINMORRY PETG GF | PETG | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A2L | TINMORRY PETG Galaxy.bbsflmt* | TINMORRY PETG Galaxy | PETG | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG Galaxy_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A2L | TINMORRY PETG HS.bbsflmt* | TINMORRY PETG HS | PETG | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG HS_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A2L | TINMORRY PETG Marble.bbsflmt* | TINMORRY PETG Marble | PETG | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG Marble_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A2L | TINMORRY PETG Matte.bbsflmt* | TINMORRY PETG Matte | PETG | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG Matte_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A2L | TINMORRY PETG Metallic.bbsflmt | TINMORRY PETG Metallic | PETG | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG Metallic_1780919570 |
| profiles/BambuStudio/TINMORRY/A2L | TINMORRY PETG Sparkly.bbsflmt* | TINMORRY PETG Sparkly | PETG | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG Sparkly_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A2L | TINMORRY PLA CF.bbsflmt* | TINMORRY PLA CF | PLA-CF | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PLA CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A2L | TINMORRY PLA Galaxy.bbsflmt* | TINMORRY PLA Galaxy | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PLA Galaxy_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A2L | TINMORRY PLA Matte.bbsflmt* | TINMORRY PLA Matte | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PLA Matte_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/A2L | TINMORRY PLA Rapid.bbsflmt | TINMORRY PLA Rapid | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PLA Rapid_1780888326 |
| profiles/BambuStudio/TINMORRY/A2L | TINMORRY PLA Silk.bbsflmt | TINMORRY PLA Silk | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PLA Silk_1781160724 |
| profiles/BambuStudio/TINMORRY/A2L | TINMORRY TPU 95A.bbsflmt | TINMORRY TPU 95A | TPU | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY TPU 95A_1780887573 |
| profiles/BambuStudio/TINMORRY/A2L | TINMORRY TPU GF.bbsflmt* | TINMORRY TPU GF | TPU | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY TPU GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY ABS.bbsflmt* | TINMORRY ABS | ABS | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ABS_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY ASA CF.bbsflmt* | TINMORRY ASA CF | ASA-CF | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ASA CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY ASA.bbsflmt* | TINMORRY ASA | ASA | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ASA_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY PC GF.bbsflmt* | TINMORRY PC GF | PC | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PC GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY PET CF GF.bbsflmt* | TINMORRY PET CF GF | PET-CF | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PET CF GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY PET CF.bbsflmt* | TINMORRY PET CF | PET-CF | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PET CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY PETG CF GF.bbsflmt* | TINMORRY PETG CF GF | PETG-CF | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY PETG CF PP.bbsflmt* | TINMORRY PETG CF PP | PETG | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF PP_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY PETG CF.bbsflmt* | TINMORRY PETG CF | PETG-CF | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY PETG ECO.bbsflmt* | TINMORRY PETG ECO | PETG | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG ECO_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY PETG GF.bbsflmt* | TINMORRY PETG GF | PETG | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY PETG Galaxy.bbsflmt* | TINMORRY PETG Galaxy | PETG | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Galaxy_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY PETG HS.bbsflmt* | TINMORRY PETG HS | PETG | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG HS_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY PETG Marble.bbsflmt* | TINMORRY PETG Marble | PETG | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Marble_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY PETG Matte.bbsflmt* | TINMORRY PETG Matte | PETG | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Matte_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY PETG Metallic.bbsflmt* | TINMORRY PETG Metallic | PETG | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Metallic_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY PETG Sparkly.bbsflmt* | TINMORRY PETG Sparkly | PETG | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Sparkly_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY PLA CF.bbsflmt | TINMORRY PLA CF | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PLA CF_1781245287 |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY PLA Galaxy.bbsflmt* | TINMORRY PLA Galaxy | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PLA Galaxy_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY PLA Matte.bbsflmt* | TINMORRY PLA Matte | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PLA Matte_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY PLA Rapid.bbsflmt | TINMORRY PLA Rapid | PLA | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY PLA Rapid_1780309015 |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY PLA Silk.bbsflmt* | TINMORRY PLA Silk | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PLA Silk_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY TPU 95a.bbsflmt* | TINMORRY TPU 95a | TPU | Bambu Lab H2C 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU 95a_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY TPU GF.bbsflmt* | TINMORRY TPU GF | TPU | Bambu Lab H2C 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2C | TINMORRY TPU.bbsflmt* | TINMORRY TPU | TPU | Bambu Lab H2C 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2D | TINMORRY ABS pro.bbsflmt | TINMORRY ABS pro | ABS | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY ABS pro_1780299462 |
| profiles/BambuStudio/TINMORRY/H2D | TINMORRY ASA CF.bbsflmt | TINMORRY ASA CF | ASA | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY ASA CF_1780303223 |
| profiles/BambuStudio/TINMORRY/H2D | TINMORRY PC GF.bbsflmt* | TINMORRY PC GF | PC | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PC GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2D | TINMORRY PET CF GF.bbsflmt* | TINMORRY PET CF GF | PET-CF | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PET CF GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2D | TINMORRY PET CF.bbsflmt* | TINMORRY PET CF | PET-CF | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PET CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2D | TINMORRY PETG CF GF.bbsflmt* | TINMORRY PETG CF GF | PETG-CF | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2D | TINMORRY PETG CF PP.bbsflmt* | TINMORRY PETG CF PP | PETG | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF PP_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2D | TINMORRY PETG CF.bbsflmt* | TINMORRY PETG CF | PETG-CF | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2D | TINMORRY PETG ECO.bbsflmt* | TINMORRY PETG ECO | PETG | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG ECO_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2D | TINMORRY PETG GF.bbsflmt* | TINMORRY PETG GF | PETG | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2D | TINMORRY PETG Galaxy.bbsflmt* | TINMORRY PETG Galaxy | PETG | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Galaxy_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2D | TINMORRY PETG HS.bbsflmt* | TINMORRY PETG HS | PETG | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG HS_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2D | TINMORRY PETG Marble.bbsflmt* | TINMORRY PETG Marble | PETG | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Marble_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2D | TINMORRY PETG Matte.bbsflmt* | TINMORRY PETG Matte | PETG | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Matte_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2D | TINMORRY PETG Metallic.bbsflmt* | TINMORRY PETG Metallic | PETG | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Metallic_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2D | TINMORRY PETG Sparkly.bbsflmt* | TINMORRY PETG Sparkly | PETG | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Sparkly_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2D | TINMORRY PLA CF.bbsflmt* | TINMORRY PLA CF | PLA-CF | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2D | TINMORRY PLA Galaxy.bbsflmt* | TINMORRY PLA Galaxy | PLA | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Galaxy_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2D | TINMORRY PLA Matte，.bbsflmt | TINMORRY PLA Matte， | PLA | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Matte，_1779697060 |
| profiles/BambuStudio/TINMORRY/H2D | TINMORRY PLA Silk.bbsflmt* | TINMORRY PLA Silk | PLA | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Silk_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2D | TINMORRY TPU 95a.bbsflmt* | TINMORRY TPU 95a | TPU | Bambu Lab H2D 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU 95a_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2D | TINMORRY TPU GF.bbsflmt* | TINMORRY TPU GF | TPU | Bambu Lab H2D 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2D | TINMORRY TPU.bbsflmt* | TINMORRY TPU | TPU | Bambu Lab H2D 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2S | TINMORRY ABS Pro.bbsflmt* | TINMORRY ABS Pro | ABS | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ABS Pro_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2S | TINMORRY ABS.bbsflmt* | TINMORRY ABS | ABS | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ABS_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2S | TINMORRY ASA CF.bbsflmt | TINMORRY ASA CF | ASA | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY ASA CF_1780304244 |
| profiles/BambuStudio/TINMORRY/H2S | TINMORRY PC GF.bbsflmt* | TINMORRY PC GF | PC | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PC GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2S | TINMORRY PET CF GF.bbsflmt* | TINMORRY PET CF GF | PET-CF | Bambu Lab H2S 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PET CF GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2S | TINMORRY PET CF.bbsflmt* | TINMORRY PET CF | PET-CF | Bambu Lab H2S 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PET CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2S | TINMORRY PETG CF.bbsflmt | TINMORRY PETG CF | PETG | Bambu Lab H2S 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG CF_1782456820 |
| profiles/BambuStudio/TINMORRY/H2S | TINMORRY PETG ECO.bbsflmt* | TINMORRY PETG ECO | PETG | Bambu Lab H2S 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG ECO_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2S | TINMORRY PETG GF.bbsflmt* | TINMORRY PETG GF | PETG | Bambu Lab H2S 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2S | TINMORRY PETG Galaxy.bbsflmt* | TINMORRY PETG Galaxy | PETG | Bambu Lab H2S 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG Galaxy_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2S | TINMORRY PETG HS.bbsflmt* | TINMORRY PETG HS | PETG | Bambu Lab H2S 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG HS_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2S | TINMORRY PETG Marble.bbsflmt* | TINMORRY PETG Marble | PETG | Bambu Lab H2S 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG Marble_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2S | TINMORRY PETG Matte.bbsflmt* | TINMORRY PETG Matte | PETG | Bambu Lab H2S 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG Matte_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2S | TINMORRY PETG Metallic.bbsflmt* | TINMORRY PETG Metallic | PETG | Bambu Lab H2S 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG Metallic_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2S | TINMORRY PETG Sparkly.bbsflmt* | TINMORRY PETG Sparkly | PETG | Bambu Lab H2S 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG Sparkly_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2S | TINMORRY PLA CF.bbsflmt* | TINMORRY PLA CF | PLA-CF | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PLA CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2S | TINMORRY PLA Galaxy.bbsflmt* | TINMORRY PLA Galaxy | PLA | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PLA Galaxy_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2S | TINMORRY PLA Matte.bbsflmt* | TINMORRY PLA Matte | PLA | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PLA Matte_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2S | TINMORRY PLA Rapid.bbsflmt | TINMORRY PLA Rapid | PLA | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY PLA Rapid_1780308480 |
| profiles/BambuStudio/TINMORRY/H2S | TINMORRY PLA Silk.bbsflmt* | TINMORRY PLA Silk | PLA | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PLA Silk_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/H2S | TINMORRY TPU 95A.bbsflmt | TINMORRY TPU 95A | TPU | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY TPU 95A_1780369052 |
| profiles/BambuStudio/TINMORRY/H2S | TINMORRY TPU GF.bbsflmt* | TINMORRY TPU GF | TPU | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY TPU GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY ABS Pro.bbsflmt* | TINMORRY ABS Pro | ABS | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ABS Pro_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY ABS.bbsflmt* | TINMORRY ABS | ABS | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ABS_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY ASA CF.bbsflmt* | TINMORRY ASA CF | ASA-CF | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ASA CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY ASA.bbsflmt* | TINMORRY ASA | ASA | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ASA_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY PC GF.bbsflmt* | TINMORRY PC GF | PC | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PC GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY PET CF GF.bbsflmt* | TINMORRY PET CF GF | PET-CF | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PET CF GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY PET CF.bbsflmt* | TINMORRY PET CF | PET-CF | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PET CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY PETG CF GF.bbsflmt* | TINMORRY PETG CF GF | PETG-CF | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY PETG CF PP.bbsflmt* | TINMORRY PETG CF PP | PETG | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF PP_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY PETG CF.bbsflmt* | TINMORRY PETG CF | PETG-CF | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY PETG ECO.bbsflmt* | TINMORRY PETG ECO | PETG | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG ECO_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY PETG GF.bbsflmt* | TINMORRY PETG GF | PETG | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY PETG Galaxy.bbsflmt* | TINMORRY PETG Galaxy | PETG | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Galaxy_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY PETG HS.bbsflmt* | TINMORRY PETG HS | PETG | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG HS_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY PETG Marble.bbsflmt* | TINMORRY PETG Marble | PETG | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Marble_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY PETG Matte.bbsflmt* | TINMORRY PETG Matte | PETG | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Matte_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY PETG Metallic.bbsflmt* | TINMORRY PETG Metallic | PETG | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Metallic_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY PETG Sparkly.bbsflmt* | TINMORRY PETG Sparkly | PETG | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Sparkly_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY PLA CF.bbsflmt* | TINMORRY PLA CF | PLA-CF | Bambu Lab P1S 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY PLA Galaxy.bbsflmt* | TINMORRY PLA Galaxy | PLA | Bambu Lab P1S 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Galaxy_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY PLA Matte.bbsflmt* | TINMORRY PLA Matte | PLA | Bambu Lab P1S 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Matte_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY PLA Silk.bbsflmt* | TINMORRY PLA Silk | PLA | Bambu Lab P1S 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Silk_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY PLA.bbsflmt* | TINMORRY PLA | PLA | Bambu Lab P1S 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY TPU 95a.bbsflmt* | TINMORRY TPU 95a | TPU | Bambu Lab P1S 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU 95a_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY TPU GF.bbsflmt* | TINMORRY TPU GF | TPU | Bambu Lab P1S 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P1S | TINMORRY TPU.bbsflmt* | TINMORRY TPU | TPU | Bambu Lab P1S 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY ABS Pro.bbsflmt | TINMORRY ABS Pro | ABS | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY ABS Pro_1780300252 |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY ASA CF.bbsflmt* | TINMORRY ASA CF | ASA-CF | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ASA CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY ASA.bbsflmt* | TINMORRY ASA | ASA | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ASA_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY PC GF.bbsflmt* | TINMORRY PC GF | PC | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PC GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY PET CF GF.bbsflmt* | TINMORRY PET CF GF | PET-CF | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PET CF GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY PET CF.bbsflmt* | TINMORRY PET CF | PET-CF | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PET CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY PETG CF GF.bbsflmt* | TINMORRY PETG CF GF | PETG-CF | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY PETG CF.bbsflmt* | TINMORRY PETG CF | PETG-CF | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY PETG ECO.bbsflmt* | TINMORRY PETG ECO | PETG | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG ECO_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY PETG GF.bbsflmt* | TINMORRY PETG GF | PETG | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY PETG Galaxy.bbsflmt* | TINMORRY PETG Galaxy | PETG | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Galaxy_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY PETG HS.bbsflmt* | TINMORRY PETG HS | PETG | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG HS_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY PETG Marble.bbsflmt* | TINMORRY PETG Marble | PETG | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Marble_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY PETG Matte.bbsflmt | TINMORRY PETG Matte | PETG | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Matte_1780387842 |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY PETG Metallic.bbsflmt* | TINMORRY PETG Metallic | PETG | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Metallic_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY PETG Sparkly.bbsflmt* | TINMORRY PETG Sparkly | PETG | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Sparkly_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY PLA CF.bbsflmt* | TINMORRY PLA CF | PLA-CF | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY PLA Galaxy.bbsflmt* | TINMORRY PLA Galaxy | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Galaxy_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY PLA Matte.bbsflmt* | TINMORRY PLA Matte | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Matte_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY PLA Silk.bbsflmt* | TINMORRY PLA Silk | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Silk_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY PLA.bbsflmt* | TINMORRY PLA | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY PP-CF `.bbsflmt | TINMORRY PP-CF ` | PP-CF | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY PP-CF `_1780312363 |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY TPU 95A.bbsflmt | TINMORRY TPU 95A | TPU | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY TPU 95A_1780368775 |
| profiles/BambuStudio/TINMORRY/P2S | TINMORRY TPU GF.bbsflmt* | TINMORRY TPU GF | TPU | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY TPU GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/X2D/0.4mm | TINMORRY ABS Pro.bbsflmt | TINMORRY ABS Pro | ABS | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ABS Pro_1777370656 |
| profiles/BambuStudio/TINMORRY/X2D/0.4mm | TINMORRY ASA CF.bbsflmt* | TINMORRY ASA CF | ASA-CF | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ASA CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/X2D/0.4mm | TINMORRY ASA basic.bbsflmt | TINMORRY ASA basic | ASA | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ASA basic_1777370656 |
| profiles/BambuStudio/TINMORRY/X2D/0.4mm | TINMORRY PA-CF.bbsflmt* | TINMORRY PA-CF | PA-CF | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PA-CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/X2D/0.4mm | TINMORRY PAHT-CF.bbsflmt* | TINMORRY PAHT-CF | PAHT-CF | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PAHT-CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/X2D/0.4mm | TINMORRY PC GF.bbsflmt* | TINMORRY PC GF | PC | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PC GF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/X2D/0.4mm | TINMORRY PET CF.bbsflmt* | TINMORRY PET CF | PET-CF | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PET CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/X2D/0.4mm | TINMORRY PETG CF.bbsflmt | TINMORRY PETG CF | PETG | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF_1777370656 |
| profiles/BambuStudio/TINMORRY/X2D/0.4mm | TINMORRY PETG ECO.bbsflmt | TINMORRY PETG ECO | PETG | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG ECO_1777370656 |
| profiles/BambuStudio/TINMORRY/X2D/0.4mm | TINMORRY PETG GF.bbsflmt | TINMORRY PETG GF | PETG | Bambu Lab P2S 0.4 nozzle + Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY PETG GF_1778039341 |
| profiles/BambuStudio/TINMORRY/X2D/0.4mm | TINMORRY PETG Galaxy.bbsflmt | TINMORRY PETG Galaxy | PETG | Bambu Lab X2D 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG Galaxy_1781058844 |
| profiles/BambuStudio/TINMORRY/X2D/0.4mm | TINMORRY PETG HS.bbsflmt* | TINMORRY PETG HS | PETG | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG HS_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/X2D/0.4mm | TINMORRY PETG Marble.bbsflmt | TINMORRY PETG Marble | PETG | Bambu Lab P2S 0.4 nozzle + Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY PETG Marble_1778039341 |
| profiles/BambuStudio/TINMORRY/X2D/0.4mm | TINMORRY PETG Matte.bbsflmt* | TINMORRY PETG Matte | PETG | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Matte_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/X2D/0.4mm | TINMORRY PETG Metallic.bbsflmt | TINMORRY PETG Metallic | PETG | Bambu Lab P2S 0.4 nozzle + Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY PETG Metallic_1778039341 |
| profiles/BambuStudio/TINMORRY/X2D/0.4mm | TINMORRY PETG Sparkly.bbsflmt | TINMORRY PETG Sparkly | PETG | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Sparkly_1777370656 |
| profiles/BambuStudio/TINMORRY/X2D/0.4mm | TINMORRY PLA CF.bbsflmt* | TINMORRY PLA CF | PLA-CF | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA CF_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/X2D/0.4mm | TINMORRY PLA Galaxy.bbsflmt* | TINMORRY PLA Galaxy | PLA | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Galaxy_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/X2D/0.4mm | TINMORRY PLA Silk.bbsflmt* | TINMORRY PLA Silk | PLA | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Silk_&lt;generated&gt; |
| profiles/BambuStudio/TINMORRY/X2D/0.4mm | TINMORRY PLA matte.bbsflmt | TINMORRY PLA matte | PLA | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA matte_1779247765 |
| profiles/BambuStudio/TINMORRY/X2D/0.4mm | TINMORRY TPU 95A.bbsflmt | TINMORRY TPU 95A | TPU | Bambu Lab P2S 0.4 nozzle + Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU 95A_1778039341 |
| profiles/BambuStudio/TINMORRY/X2D/0.4mm | TINMORRY TPU GF.bbsflmt* | TINMORRY TPU GF | TPU | Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU GF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PEBA 85A.bbsflmt* | eSUN PEBA 85A | PEBA | Bambu Lab A1 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA 85A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PEBA 90A.bbsflmt* | eSUN PEBA 90A | PEBA | Bambu Lab A1 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA 90A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PEBA LW.bbsflmt* | eSUN PEBA LW | PEBA | Bambu Lab A1 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PEBA.bbsflmt* | eSUN PEBA | PEBA | Bambu Lab A1 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PET CF.bbsflmt* | eSUN PET CF | PET-CF | Bambu Lab A1 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PET CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PETG Basic.bbsflmt* | eSUN PETG Basic | PETG | Bambu Lab A1 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Basic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PETG CF.bbsflmt* | eSUN PETG CF | PETG-CF | Bambu Lab A1 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PETG ESD.bbsflmt* | eSUN PETG ESD | PETG | Bambu Lab A1 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG ESD_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PETG HS.bbsflmt* | eSUN PETG HS | PETG | Bambu Lab A1 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PETG Luminous.bbsflmt* | eSUN PETG Luminous | PETG | Bambu Lab A1 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Luminous_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PETG Matte.bbsflmt* | eSUN PETG Matte | PETG | Bambu Lab A1 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Matte_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PETG.bbsflmt* | eSUN PETG | PETG | Bambu Lab A1 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PLA Basic.bbsflmt* | eSUN PLA Basic | PLA | Bambu Lab A1 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Basic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PLA CF.bbsflmt* | eSUN PLA CF | PLA-CF | Bambu Lab A1 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PLA Clear.bbsflmt* | eSUN PLA Clear | PLA | Bambu Lab A1 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Clear_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PLA HS.bbsflmt* | eSUN PLA HS | PLA | Bambu Lab A1 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PLA LW.bbsflmt* | eSUN PLA LW | PLA | Bambu Lab A1 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PLA Lite.bbsflmt* | eSUN PLA Lite | PLA | Bambu Lab A1 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Lite_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PLA Luminous.bbsflmt* | eSUN PLA Luminous | PLA | Bambu Lab A1 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Luminous_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PLA Magic.bbsflmt* | eSUN PLA Magic | PLA | Bambu Lab A1 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Magic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PLA Marble.bbsflmt* | eSUN PLA Marble | PLA | Bambu Lab A1 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Marble_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PLA Matte.bbsflmt* | eSUN PLA Matte | PLA | Bambu Lab A1 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Matte_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PLA Metal.bbsflmt* | eSUN PLA Metal | PLA | Bambu Lab A1 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Metal_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PLA Rock UV.bbsflmt* | eSUN PLA Rock UV | PLA | Bambu Lab A1 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Rock UV_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PLA ST.bbsflmt* | eSUN PLA ST | PLA | Bambu Lab A1 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA ST_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PLA Silk.bbsflmt* | eSUN PLA Silk | PLA | Bambu Lab A1 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Silk_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PLA Twinkle.bbsflmt* | eSUN PLA Twinkle | PLA | Bambu Lab A1 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Twinkle_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PLA Wood.bbsflmt* | eSUN PLA Wood | PLA | Bambu Lab A1 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Wood_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN PLA.bbsflmt* | eSUN PLA | PLA | Bambu Lab A1 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN TPE 83A.bbsflmt* | eSUN TPE 83A | TPE | Bambu Lab A1 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPE 83A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN TPU 64D.bbsflmt* | eSUN TPU 64D | TPU | Bambu Lab A1 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 64D_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN TPU 80A.bbsflmt* | eSUN TPU 80A | TPU | Bambu Lab A1 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 80A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN TPU 85A.bbsflmt* | eSUN TPU 85A | TPU | Bambu Lab A1 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 85A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN TPU 90A.bbsflmt* | eSUN TPU 90A | TPU | Bambu Lab A1 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 90A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN TPU 95A.bbsflmt* | eSUN TPU 95A | TPU | Bambu Lab A1 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 95A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN TPU LW.bbsflmt* | eSUN TPU LW | TPU | Bambu Lab A1 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1 | eSUN TPU.bbsflmt* | eSUN TPU | TPU | Bambu Lab A1 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PEBA 85A.bbsflmt* | eSUN PEBA 85A | PEBA | Bambu Lab A1 mini 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA 85A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PEBA 90A.bbsflmt* | eSUN PEBA 90A | PEBA | Bambu Lab A1 mini 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA 90A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PEBA LW.bbsflmt* | eSUN PEBA LW | PEBA | Bambu Lab A1 mini 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PEBA.bbsflmt* | eSUN PEBA | PEBA | Bambu Lab A1 mini 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PET CF.bbsflmt* | eSUN PET CF | PET-CF | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PET CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PETG Basic.bbsflmt* | eSUN PETG Basic | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Basic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PETG CF.bbsflmt* | eSUN PETG CF | PETG-CF | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PETG ESD.bbsflmt* | eSUN PETG ESD | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG ESD_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PETG HS.bbsflmt* | eSUN PETG HS | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PETG Luminous.bbsflmt* | eSUN PETG Luminous | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Luminous_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PETG Matte.bbsflmt* | eSUN PETG Matte | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Matte_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PETG.bbsflmt* | eSUN PETG | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PLA Basic.bbsflmt* | eSUN PLA Basic | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Basic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PLA CF.bbsflmt* | eSUN PLA CF | PLA-CF | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PLA Clear.bbsflmt* | eSUN PLA Clear | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Clear_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PLA HS.bbsflmt* | eSUN PLA HS | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PLA LW.bbsflmt* | eSUN PLA LW | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PLA Lite.bbsflmt* | eSUN PLA Lite | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Lite_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PLA Luminous.bbsflmt* | eSUN PLA Luminous | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Luminous_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PLA Magic.bbsflmt* | eSUN PLA Magic | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Magic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PLA Marble.bbsflmt* | eSUN PLA Marble | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Marble_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PLA Matte.bbsflmt* | eSUN PLA Matte | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Matte_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PLA Metal.bbsflmt* | eSUN PLA Metal | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Metal_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PLA Rock UV.bbsflmt* | eSUN PLA Rock UV | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Rock UV_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PLA ST.bbsflmt* | eSUN PLA ST | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA ST_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PLA Silk.bbsflmt* | eSUN PLA Silk | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Silk_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PLA Twinkle.bbsflmt* | eSUN PLA Twinkle | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Twinkle_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PLA Wood.bbsflmt* | eSUN PLA Wood | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Wood_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN PLA.bbsflmt* | eSUN PLA | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN TPE 83A.bbsflmt* | eSUN TPE 83A | TPE | Bambu Lab A1 mini 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPE 83A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN TPU 64D.bbsflmt* | eSUN TPU 64D | TPU | Bambu Lab A1 mini 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 64D_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN TPU 80A.bbsflmt* | eSUN TPU 80A | TPU | Bambu Lab A1 mini 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 80A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN TPU 85A.bbsflmt* | eSUN TPU 85A | TPU | Bambu Lab A1 mini 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 85A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN TPU 90A.bbsflmt* | eSUN TPU 90A | TPU | Bambu Lab A1 mini 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 90A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN TPU 95A.bbsflmt* | eSUN TPU 95A | TPU | Bambu Lab A1 mini 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 95A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN TPU LW.bbsflmt* | eSUN TPU LW | TPU | Bambu Lab A1 mini 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A1mini | eSUN TPU.bbsflmt* | eSUN TPU | TPU | Bambu Lab A1 mini 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PEBA 85A.bbsflmt* | eSUN PEBA 85A | PEBA | Bambu Lab A2L 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA 85A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PEBA 90A.bbsflmt* | eSUN PEBA 90A | PEBA | Bambu Lab A2L 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA 90A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PEBA LW.bbsflmt* | eSUN PEBA LW | PEBA | Bambu Lab A2L 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PEBA.bbsflmt* | eSUN PEBA | PEBA | Bambu Lab A2L 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PET CF.bbsflmt* | eSUN PET CF | PET-CF | Bambu Lab A2L 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PET CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PETG Basic.bbsflmt* | eSUN PETG Basic | PETG | Bambu Lab A2L 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Basic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PETG CF.bbsflmt* | eSUN PETG CF | PETG-CF | Bambu Lab A2L 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PETG ESD.bbsflmt* | eSUN PETG ESD | PETG | Bambu Lab A2L 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG ESD_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PETG HS.bbsflmt* | eSUN PETG HS | PETG | Bambu Lab A2L 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PETG Luminous.bbsflmt* | eSUN PETG Luminous | PETG | Bambu Lab A2L 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Luminous_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PETG Matte.bbsflmt* | eSUN PETG Matte | PETG | Bambu Lab A2L 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Matte_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PETG.bbsflmt* | eSUN PETG | PETG | Bambu Lab A2L 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PLA Basic.bbsflmt* | eSUN PLA Basic | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Basic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PLA CF.bbsflmt* | eSUN PLA CF | PLA-CF | Bambu Lab A2L 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PLA Clear.bbsflmt* | eSUN PLA Clear | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Clear_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PLA HS.bbsflmt* | eSUN PLA HS | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PLA LW.bbsflmt* | eSUN PLA LW | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PLA Lite.bbsflmt* | eSUN PLA Lite | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Lite_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PLA Luminous.bbsflmt* | eSUN PLA Luminous | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Luminous_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PLA Magic.bbsflmt* | eSUN PLA Magic | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Magic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PLA Marble.bbsflmt* | eSUN PLA Marble | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Marble_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PLA Matte.bbsflmt* | eSUN PLA Matte | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Matte_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PLA Metal.bbsflmt* | eSUN PLA Metal | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Metal_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PLA Rock UV.bbsflmt* | eSUN PLA Rock UV | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Rock UV_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PLA ST.bbsflmt* | eSUN PLA ST | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA ST_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PLA Silk.bbsflmt* | eSUN PLA Silk | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Silk_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PLA Twinkle.bbsflmt* | eSUN PLA Twinkle | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Twinkle_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PLA Wood.bbsflmt* | eSUN PLA Wood | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Wood_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN PLA.bbsflmt* | eSUN PLA | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN TPE 83A.bbsflmt* | eSUN TPE 83A | TPE | Bambu Lab A2L 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPE 83A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN TPU 64D.bbsflmt* | eSUN TPU 64D | TPU | Bambu Lab A2L 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 64D_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN TPU 80A.bbsflmt* | eSUN TPU 80A | TPU | Bambu Lab A2L 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 80A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN TPU 85A.bbsflmt* | eSUN TPU 85A | TPU | Bambu Lab A2L 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 85A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN TPU 90A.bbsflmt* | eSUN TPU 90A | TPU | Bambu Lab A2L 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 90A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN TPU 95A.bbsflmt* | eSUN TPU 95A | TPU | Bambu Lab A2L 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 95A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN TPU LW.bbsflmt* | eSUN TPU LW | TPU | Bambu Lab A2L 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/A2L | eSUN TPU.bbsflmt* | eSUN TPU | TPU | Bambu Lab A2L 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN ABS ESD.bbsflmt* | eSUN ABS ESD | ABS | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS ESD_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN ABS FR.bbsflmt* | eSUN ABS FR | ABS | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS FR_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN ABS HS.bbsflmt* | eSUN ABS HS | ABS | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN ABS-CF.bbsflmt* | eSUN ABS-CF | ABS-CF | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS-CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN ABS-GF.bbsflmt* | eSUN ABS-GF | ABS-GF | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS-GF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN ABS.bbsflmt* | eSUN ABS | ABS | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN ASA LW.bbsflmt* | eSUN ASA LW | ASA | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ASA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN ASA.bbsflmt* | eSUN ASA | ASA | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ASA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PA-CF.bbsflmt* | eSUN PA-CF | PA-CF | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PA-CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PA.bbsflmt* | eSUN PA | PA | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PA12-CF.bbsflmt* | eSUN PA12-CF | PA12-CF | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PA12-CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PA6-CF.bbsflmt* | eSUN PA6-CF | PA6-CF | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PA6-CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PC ESD.bbsflmt* | eSUN PC ESD | PC | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PC ESD_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PC HT.bbsflmt* | eSUN PC HT | PC | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PC HT_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PEBA 85A.bbsflmt* | eSUN PEBA 85A | PEBA | Bambu Lab H2C 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA 85A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PEBA 90A.bbsflmt* | eSUN PEBA 90A | PEBA | Bambu Lab H2C 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA 90A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PEBA LW.bbsflmt* | eSUN PEBA LW | PEBA | Bambu Lab H2C 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PEBA.bbsflmt* | eSUN PEBA | PEBA | Bambu Lab H2C 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PET CF.bbsflmt* | eSUN PET CF | PET-CF | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PET CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PETG Basic.bbsflmt* | eSUN PETG Basic | PETG | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Basic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PETG CF.bbsflmt* | eSUN PETG CF | PETG-CF | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PETG ESD.bbsflmt* | eSUN PETG ESD | PETG | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG ESD_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PETG HS.bbsflmt* | eSUN PETG HS | PETG | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PETG Luminous.bbsflmt* | eSUN PETG Luminous | PETG | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Luminous_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PETG Matte.bbsflmt* | eSUN PETG Matte | PETG | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Matte_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PETG.bbsflmt* | eSUN PETG | PETG | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PLA Basic.bbsflmt* | eSUN PLA Basic | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Basic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PLA CF.bbsflmt* | eSUN PLA CF | PLA-CF | Bambu Lab H2C 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PLA Clear.bbsflmt* | eSUN PLA Clear | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Clear_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PLA HS.bbsflmt* | eSUN PLA HS | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PLA LW.bbsflmt* | eSUN PLA LW | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PLA Lite.bbsflmt* | eSUN PLA Lite | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Lite_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PLA Luminous.bbsflmt* | eSUN PLA Luminous | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Luminous_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PLA Magic.bbsflmt* | eSUN PLA Magic | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Magic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PLA Marble.bbsflmt* | eSUN PLA Marble | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Marble_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PLA Matte.bbsflmt* | eSUN PLA Matte | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Matte_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PLA Metal.bbsflmt* | eSUN PLA Metal | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Metal_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PLA Rock UV.bbsflmt* | eSUN PLA Rock UV | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Rock UV_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PLA ST.bbsflmt* | eSUN PLA ST | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA ST_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PLA Silk.bbsflmt* | eSUN PLA Silk | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Silk_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PLA Twinkle.bbsflmt* | eSUN PLA Twinkle | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Twinkle_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PLA Wood.bbsflmt* | eSUN PLA Wood | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Wood_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN PLA.bbsflmt* | eSUN PLA | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN TPE 83A.bbsflmt* | eSUN TPE 83A | TPE | Bambu Lab H2C 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPE 83A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN TPU 64D.bbsflmt* | eSUN TPU 64D | TPU | Bambu Lab H2C 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 64D_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN TPU 80A.bbsflmt* | eSUN TPU 80A | TPU | Bambu Lab H2C 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 80A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN TPU 85A.bbsflmt* | eSUN TPU 85A | TPU | Bambu Lab H2C 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 85A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN TPU 90A.bbsflmt* | eSUN TPU 90A | TPU | Bambu Lab H2C 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 90A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN TPU 95A.bbsflmt* | eSUN TPU 95A | TPU | Bambu Lab H2C 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 95A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN TPU LW.bbsflmt* | eSUN TPU LW | TPU | Bambu Lab H2C 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2C | eSUN TPU.bbsflmt* | eSUN TPU | TPU | Bambu Lab H2C 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN ABS ESD.bbsflmt* | eSUN ABS ESD | ABS | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS ESD_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN ABS FR.bbsflmt* | eSUN ABS FR | ABS | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS FR_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN ABS HS.bbsflmt* | eSUN ABS HS | ABS | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN ABS-CF.bbsflmt* | eSUN ABS-CF | ABS-CF | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS-CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN ABS-GF.bbsflmt* | eSUN ABS-GF | ABS-GF | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS-GF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN ABS.bbsflmt* | eSUN ABS | ABS | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN ASA LW.bbsflmt* | eSUN ASA LW | ASA | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ASA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN ASA.bbsflmt* | eSUN ASA | ASA | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ASA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PA-CF.bbsflmt* | eSUN PA-CF | PA-CF | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PA-CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PA.bbsflmt* | eSUN PA | PA | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PA12-CF.bbsflmt* | eSUN PA12-CF | PA12-CF | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PA12-CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PA6-CF.bbsflmt* | eSUN PA6-CF | PA6-CF | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PA6-CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PC ESD.bbsflmt* | eSUN PC ESD | PC | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PC ESD_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PC.bbsflmt* | eSUN PC | PC | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PC_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PEBA 85A.bbsflmt* | eSUN PEBA 85A | PEBA | Bambu Lab H2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA 85A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PEBA 90A.bbsflmt* | eSUN PEBA 90A | PEBA | Bambu Lab H2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA 90A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PEBA LW.bbsflmt* | eSUN PEBA LW | PEBA | Bambu Lab H2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PEBA.bbsflmt* | eSUN PEBA | PEBA | Bambu Lab H2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PET CF.bbsflmt* | eSUN PET CF | PET-CF | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PET CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PETG Basic.bbsflmt* | eSUN PETG Basic | PETG | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Basic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PETG CF.bbsflmt* | eSUN PETG CF | PETG-CF | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PETG ESD.bbsflmt* | eSUN PETG ESD | PETG | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG ESD_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PETG HS.bbsflmt* | eSUN PETG HS | PETG | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PETG Luminous.bbsflmt* | eSUN PETG Luminous | PETG | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Luminous_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PETG Matte.bbsflmt* | eSUN PETG Matte | PETG | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Matte_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PETG.bbsflmt* | eSUN PETG | PETG | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PLA Basic.bbsflmt* | eSUN PLA Basic | PLA | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Basic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PLA CF.bbsflmt* | eSUN PLA CF | PLA-CF | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PLA Clear.bbsflmt* | eSUN PLA Clear | PLA | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Clear_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PLA HS.bbsflmt* | eSUN PLA HS | PLA | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PLA LW.bbsflmt* | eSUN PLA LW | PLA | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PLA Lite.bbsflmt* | eSUN PLA Lite | PLA | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Lite_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PLA Luminous.bbsflmt* | eSUN PLA Luminous | PLA | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Luminous_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PLA Magic.bbsflmt* | eSUN PLA Magic | PLA | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Magic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PLA Marble.bbsflmt* | eSUN PLA Marble | PLA | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Marble_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PLA Matte.bbsflmt* | eSUN PLA Matte | PLA | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Matte_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PLA Metal.bbsflmt* | eSUN PLA Metal | PLA | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Metal_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PLA Rock UV.bbsflmt* | eSUN PLA Rock UV | PLA | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Rock UV_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PLA ST.bbsflmt* | eSUN PLA ST | PLA | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA ST_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PLA Silk.bbsflmt* | eSUN PLA Silk | PLA | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Silk_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PLA Twinkle.bbsflmt* | eSUN PLA Twinkle | PLA | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Twinkle_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PLA Wood.bbsflmt* | eSUN PLA Wood | PLA | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Wood_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN PLA.bbsflmt* | eSUN PLA | PLA | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN TPE 83A.bbsflmt* | eSUN TPE 83A | TPE | Bambu Lab H2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPE 83A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN TPU 64D.bbsflmt* | eSUN TPU 64D | TPU | Bambu Lab H2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 64D_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN TPU 80A.bbsflmt* | eSUN TPU 80A | TPU | Bambu Lab H2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 80A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN TPU 85A.bbsflmt* | eSUN TPU 85A | TPU | Bambu Lab H2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 85A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN TPU 90A.bbsflmt* | eSUN TPU 90A | TPU | Bambu Lab H2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 90A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN TPU 95A.bbsflmt* | eSUN TPU 95A | TPU | Bambu Lab H2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 95A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN TPU LW.bbsflmt* | eSUN TPU LW | TPU | Bambu Lab H2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2D | eSUN TPU.bbsflmt* | eSUN TPU | TPU | Bambu Lab H2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN ABS ESD.bbsflmt* | eSUN ABS ESD | ABS | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS ESD_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN ABS FR.bbsflmt* | eSUN ABS FR | ABS | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS FR_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN ABS HS.bbsflmt* | eSUN ABS HS | ABS | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN ABS-CF.bbsflmt* | eSUN ABS-CF | ABS-CF | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS-CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN ABS-GF.bbsflmt* | eSUN ABS-GF | ABS-GF | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS-GF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN ABS.bbsflmt* | eSUN ABS | ABS | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN ASA LW.bbsflmt* | eSUN ASA LW | ASA | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ASA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN ASA.bbsflmt* | eSUN ASA | ASA | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ASA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PA-CF.bbsflmt* | eSUN PA-CF | PA-CF | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PA-CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PA.bbsflmt* | eSUN PA | PA | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PA12-CF.bbsflmt* | eSUN PA12-CF | PA12-CF | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PA12-CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PA6-CF.bbsflmt* | eSUN PA6-CF | PA6-CF | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PA6-CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PC ESD.bbsflmt* | eSUN PC ESD | PC | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PC ESD_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PC HT.bbsflmt* | eSUN PC HT | PC | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PC HT_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PEBA 85A.bbsflmt* | eSUN PEBA 85A | PEBA | Bambu Lab H2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA 85A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PEBA 90A.bbsflmt* | eSUN PEBA 90A | PEBA | Bambu Lab H2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA 90A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PEBA LW.bbsflmt* | eSUN PEBA LW | PEBA | Bambu Lab H2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PEBA.bbsflmt* | eSUN PEBA | PEBA | Bambu Lab H2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PET CF.bbsflmt* | eSUN PET CF | PET-CF | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PET CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PETG Basic.bbsflmt* | eSUN PETG Basic | PETG | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Basic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PETG CF.bbsflmt* | eSUN PETG CF | PETG-CF | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PETG ESD.bbsflmt* | eSUN PETG ESD | PETG | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG ESD_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PETG HS.bbsflmt* | eSUN PETG HS | PETG | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PETG Luminous.bbsflmt* | eSUN PETG Luminous | PETG | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Luminous_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PETG Matte.bbsflmt* | eSUN PETG Matte | PETG | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Matte_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PETG.bbsflmt* | eSUN PETG | PETG | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PLA Basic.bbsflmt* | eSUN PLA Basic | PLA | Bambu Lab H2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Basic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PLA CF.bbsflmt* | eSUN PLA CF | PLA-CF | Bambu Lab H2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PLA Clear.bbsflmt* | eSUN PLA Clear | PLA | Bambu Lab H2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Clear_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PLA HS.bbsflmt* | eSUN PLA HS | PLA | Bambu Lab H2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PLA LW.bbsflmt* | eSUN PLA LW | PLA | Bambu Lab H2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PLA Lite.bbsflmt* | eSUN PLA Lite | PLA | Bambu Lab H2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Lite_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PLA Luminous.bbsflmt* | eSUN PLA Luminous | PLA | Bambu Lab H2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Luminous_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PLA Magic.bbsflmt* | eSUN PLA Magic | PLA | Bambu Lab H2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Magic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PLA Marble.bbsflmt* | eSUN PLA Marble | PLA | Bambu Lab H2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Marble_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PLA Matte.bbsflmt* | eSUN PLA Matte | PLA | Bambu Lab H2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Matte_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PLA Metal.bbsflmt* | eSUN PLA Metal | PLA | Bambu Lab H2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Metal_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PLA Rock UV.bbsflmt* | eSUN PLA Rock UV | PLA | Bambu Lab H2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Rock UV_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PLA ST.bbsflmt* | eSUN PLA ST | PLA | Bambu Lab H2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA ST_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PLA Silk.bbsflmt* | eSUN PLA Silk | PLA | Bambu Lab H2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Silk_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PLA Twinkle.bbsflmt* | eSUN PLA Twinkle | PLA | Bambu Lab H2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Twinkle_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PLA Wood.bbsflmt* | eSUN PLA Wood | PLA | Bambu Lab H2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Wood_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN PLA.bbsflmt* | eSUN PLA | PLA | Bambu Lab H2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN TPE 83A.bbsflmt* | eSUN TPE 83A | TPE | Bambu Lab H2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPE 83A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN TPU 64D.bbsflmt* | eSUN TPU 64D | TPU | Bambu Lab H2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 64D_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN TPU 80A.bbsflmt* | eSUN TPU 80A | TPU | Bambu Lab H2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 80A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN TPU 85A.bbsflmt* | eSUN TPU 85A | TPU | Bambu Lab H2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 85A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN TPU 90A.bbsflmt* | eSUN TPU 90A | TPU | Bambu Lab H2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 90A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN TPU 95A.bbsflmt* | eSUN TPU 95A | TPU | Bambu Lab H2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 95A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN TPU LW.bbsflmt* | eSUN TPU LW | TPU | Bambu Lab H2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/H2S | eSUN TPU.bbsflmt* | eSUN TPU | TPU | Bambu Lab H2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN ABS ESD.bbsflmt* | eSUN ABS ESD | ABS | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS ESD_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN ABS FR.bbsflmt* | eSUN ABS FR | ABS | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS FR_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN ABS HS.bbsflmt* | eSUN ABS HS | ABS | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN ABS HT.bbsflmt* | eSUN ABS HT | ABS | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS HT_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN ABS.bbsflmt* | eSUN ABS | ABS | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN ASA LW.bbsflmt* | eSUN ASA LW | ASA | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ASA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN ASA.bbsflmt* | eSUN ASA | ASA | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ASA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PC ESD.bbsflmt* | eSUN PC ESD | PC | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PC ESD_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PC.bbsflmt* | eSUN PC | PC | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PC_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PEBA 85A.bbsflmt* | eSUN PEBA 85A | PEBA | Bambu Lab P1S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA 85A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PEBA 90A.bbsflmt* | eSUN PEBA 90A | PEBA | Bambu Lab P1S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA 90A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PEBA LW.bbsflmt* | eSUN PEBA LW | PEBA | Bambu Lab P1S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PEBA.bbsflmt* | eSUN PEBA | PEBA | Bambu Lab P1S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PET CF.bbsflmt* | eSUN PET CF | PET-CF | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PET CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PETG Basic.bbsflmt* | eSUN PETG Basic | PETG | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Basic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PETG CF.bbsflmt* | eSUN PETG CF | PETG-CF | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PETG ESD.bbsflmt* | eSUN PETG ESD | PETG | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG ESD_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PETG HS.bbsflmt* | eSUN PETG HS | PETG | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PETG Luminous.bbsflmt* | eSUN PETG Luminous | PETG | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Luminous_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PETG Matte.bbsflmt* | eSUN PETG Matte | PETG | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Matte_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PETG.bbsflmt* | eSUN PETG | PETG | Bambu Lab P1S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PLA Basic.bbsflmt* | eSUN PLA Basic | PLA | Bambu Lab P1S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Basic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PLA CF.bbsflmt* | eSUN PLA CF | PLA-CF | Bambu Lab P1S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PLA Clear.bbsflmt* | eSUN PLA Clear | PLA | Bambu Lab P1S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Clear_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PLA HS.bbsflmt* | eSUN PLA HS | PLA | Bambu Lab P1S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PLA LW.bbsflmt* | eSUN PLA LW | PLA | Bambu Lab P1S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PLA Lite.bbsflmt* | eSUN PLA Lite | PLA | Bambu Lab P1S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Lite_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PLA Luminous.bbsflmt* | eSUN PLA Luminous | PLA | Bambu Lab P1S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Luminous_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PLA Magic.bbsflmt* | eSUN PLA Magic | PLA | Bambu Lab P1S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Magic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PLA Marble.bbsflmt* | eSUN PLA Marble | PLA | Bambu Lab P1S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Marble_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PLA Matte.bbsflmt* | eSUN PLA Matte | PLA | Bambu Lab P1S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Matte_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PLA Metal.bbsflmt* | eSUN PLA Metal | PLA | Bambu Lab P1S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Metal_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PLA Rock UV.bbsflmt* | eSUN PLA Rock UV | PLA | Bambu Lab P1S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Rock UV_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PLA ST.bbsflmt* | eSUN PLA ST | PLA | Bambu Lab P1S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA ST_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PLA Silk.bbsflmt* | eSUN PLA Silk | PLA | Bambu Lab P1S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Silk_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PLA Twinkle.bbsflmt* | eSUN PLA Twinkle | PLA | Bambu Lab P1S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Twinkle_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PLA Wood.bbsflmt* | eSUN PLA Wood | PLA | Bambu Lab P1S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Wood_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN PLA.bbsflmt* | eSUN PLA | PLA | Bambu Lab P1S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN TPE 83A.bbsflmt* | eSUN TPE 83A | TPE | Bambu Lab P1S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPE 83A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN TPU 64D.bbsflmt* | eSUN TPU 64D | TPU | Bambu Lab P1S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 64D_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN TPU 80A.bbsflmt* | eSUN TPU 80A | TPU | Bambu Lab P1S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 80A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN TPU 85A.bbsflmt* | eSUN TPU 85A | TPU | Bambu Lab P1S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 85A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN TPU 90A.bbsflmt* | eSUN TPU 90A | TPU | Bambu Lab P1S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 90A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN TPU 95A.bbsflmt* | eSUN TPU 95A | TPU | Bambu Lab P1S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 95A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN TPU LW.bbsflmt* | eSUN TPU LW | TPU | Bambu Lab P1S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P1S | eSUN TPU.bbsflmt* | eSUN TPU | TPU | Bambu Lab P1S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN ABS ESD.bbsflmt* | eSUN ABS ESD | ABS | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS ESD_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN ABS FR.bbsflmt* | eSUN ABS FR | ABS | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS FR_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN ABS HS.bbsflmt* | eSUN ABS HS | ABS | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN ABS-CF.bbsflmt* | eSUN ABS-CF | ABS-CF | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS-CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN ABS-GF.bbsflmt* | eSUN ABS-GF | ABS-GF | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS-GF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN ABS.bbsflmt* | eSUN ABS | ABS | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN ASA LW.bbsflmt* | eSUN ASA LW | ASA | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ASA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN ASA.bbsflmt* | eSUN ASA | ASA | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ASA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PA-CF.bbsflmt* | eSUN PA-CF | PA-CF | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PA-CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PA.bbsflmt* | eSUN PA | PA | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PA12-CF.bbsflmt* | eSUN PA12-CF | PA12-CF | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PA12-CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PA6-CF.bbsflmt* | eSUN PA6-CF | PA6-CF | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PA6-CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PC ESD.bbsflmt* | eSUN PC ESD | PC | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PC ESD_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PC.bbsflmt* | eSUN PC | PC | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PC_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PEBA 85A.bbsflmt* | eSUN PEBA 85A | PEBA | Bambu Lab P2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA 85A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PEBA 90A.bbsflmt* | eSUN PEBA 90A | PEBA | Bambu Lab P2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA 90A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PEBA LW.bbsflmt* | eSUN PEBA LW | PEBA | Bambu Lab P2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PEBA.bbsflmt* | eSUN PEBA | PEBA | Bambu Lab P2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PET CF.bbsflmt* | eSUN PET CF | PET-CF | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PET CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PETG Basic.bbsflmt* | eSUN PETG Basic | PETG | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Basic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PETG CF.bbsflmt* | eSUN PETG CF | PETG-CF | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PETG ESD.bbsflmt* | eSUN PETG ESD | PETG | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG ESD_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PETG HS.bbsflmt* | eSUN PETG HS | PETG | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PETG Luminous.bbsflmt* | eSUN PETG Luminous | PETG | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Luminous_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PETG Matte.bbsflmt* | eSUN PETG Matte | PETG | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Matte_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PETG.bbsflmt* | eSUN PETG | PETG | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PLA Basic.bbsflmt* | eSUN PLA Basic | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Basic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PLA CF.bbsflmt* | eSUN PLA CF | PLA-CF | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PLA Clear.bbsflmt* | eSUN PLA Clear | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Clear_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PLA HS.bbsflmt* | eSUN PLA HS | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PLA LW.bbsflmt* | eSUN PLA LW | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PLA Lite.bbsflmt* | eSUN PLA Lite | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Lite_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PLA Luminous.bbsflmt* | eSUN PLA Luminous | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Luminous_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PLA Magic.bbsflmt* | eSUN PLA Magic | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Magic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PLA Marble.bbsflmt* | eSUN PLA Marble | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Marble_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PLA Matte.bbsflmt* | eSUN PLA Matte | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Matte_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PLA Metal.bbsflmt* | eSUN PLA Metal | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Metal_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PLA Rock UV.bbsflmt* | eSUN PLA Rock UV | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Rock UV_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PLA ST.bbsflmt* | eSUN PLA ST | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA ST_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PLA Silk.bbsflmt* | eSUN PLA Silk | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Silk_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PLA Twinkle.bbsflmt* | eSUN PLA Twinkle | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Twinkle_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PLA Wood.bbsflmt* | eSUN PLA Wood | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Wood_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN PLA.bbsflmt* | eSUN PLA | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN TPE 83A.bbsflmt* | eSUN TPE 83A | TPE | Bambu Lab P2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPE 83A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN TPU 64D.bbsflmt* | eSUN TPU 64D | TPU | Bambu Lab P2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 64D_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN TPU 80A.bbsflmt* | eSUN TPU 80A | TPU | Bambu Lab P2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 80A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN TPU 85A.bbsflmt* | eSUN TPU 85A | TPU | Bambu Lab P2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 85A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN TPU 90A.bbsflmt* | eSUN TPU 90A | TPU | Bambu Lab P2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 90A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN TPU 95A.bbsflmt* | eSUN TPU 95A | TPU | Bambu Lab P2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 95A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN TPU LW.bbsflmt* | eSUN TPU LW | TPU | Bambu Lab P2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/P2S | eSUN TPU.bbsflmt* | eSUN TPU | TPU | Bambu Lab P2S 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN ABS ESD.bbsflmt* | eSUN ABS ESD | ABS | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS ESD_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN ABS FR.bbsflmt* | eSUN ABS FR | ABS | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS FR_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN ABS HS.bbsflmt* | eSUN ABS HS | ABS | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN ABS-CF.bbsflmt* | eSUN ABS-CF | ABS-CF | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS-CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN ABS-GF.bbsflmt* | eSUN ABS-GF | ABS-GF | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS-GF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN ABS.bbsflmt* | eSUN ABS | ABS | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ABS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN ASA LW.bbsflmt* | eSUN ASA LW | ASA | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ASA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN ASA.bbsflmt* | eSUN ASA | ASA | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN ASA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PA-CF.bbsflmt* | eSUN PA-CF | PA-CF | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PA-CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PA12-CF.bbsflmt* | eSUN PA12-CF | PA12-CF | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PA12-CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PA6-CF.bbsflmt* | eSUN PA6-CF | PA6-CF | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PA6-CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PC ESD.bbsflmt* | eSUN PC ESD | PC | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PC ESD_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PC.bbsflmt* | eSUN PC | PC | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PC_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PEBA 85A.bbsflmt* | eSUN PEBA 85A | PEBA | Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA 85A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PEBA 90A.bbsflmt* | eSUN PEBA 90A | PEBA | Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA 90A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PEBA LW.bbsflmt* | eSUN PEBA LW | PEBA | Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PEBA.bbsflmt* | eSUN PEBA | PEBA | Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN PEBA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PET CF.bbsflmt* | eSUN PET CF | PET-CF | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PET CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PETG Basic.bbsflmt* | eSUN PETG Basic | PETG | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Basic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PETG CF.bbsflmt* | eSUN PETG CF | PETG-CF | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PETG ESD.bbsflmt* | eSUN PETG ESD | PETG | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG ESD_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PETG HS.bbsflmt* | eSUN PETG HS | PETG | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PETG Luminous.bbsflmt* | eSUN PETG Luminous | PETG | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Luminous_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PETG Matte.bbsflmt* | eSUN PETG Matte | PETG | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG Matte_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PETG.bbsflmt* | eSUN PETG | PETG | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_eSUN PETG_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PLA Basic.bbsflmt* | eSUN PLA Basic | PLA | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Basic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PLA CF.bbsflmt* | eSUN PLA CF | PLA-CF | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA CF_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PLA Clear.bbsflmt* | eSUN PLA Clear | PLA | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Clear_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PLA HS.bbsflmt* | eSUN PLA HS | PLA | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA HS_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PLA LW.bbsflmt* | eSUN PLA LW | PLA | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PLA Lite.bbsflmt* | eSUN PLA Lite | PLA | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Lite_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PLA Luminous.bbsflmt* | eSUN PLA Luminous | PLA | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Luminous_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PLA Magic.bbsflmt* | eSUN PLA Magic | PLA | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Magic_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PLA Marble.bbsflmt* | eSUN PLA Marble | PLA | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Marble_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PLA Matte.bbsflmt* | eSUN PLA Matte | PLA | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Matte_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PLA Metal.bbsflmt* | eSUN PLA Metal | PLA | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Metal_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PLA Rock UV.bbsflmt* | eSUN PLA Rock UV | PLA | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Rock UV_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PLA ST.bbsflmt* | eSUN PLA ST | PLA | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA ST_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PLA Silk.bbsflmt* | eSUN PLA Silk | PLA | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Silk_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PLA Twinkle.bbsflmt* | eSUN PLA Twinkle | PLA | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Twinkle_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PLA Wood.bbsflmt* | eSUN PLA Wood | PLA | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA Wood_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN PLA.bbsflmt* | eSUN PLA | PLA | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_eSUN PLA_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN TPE 83A.bbsflmt* | eSUN TPE 83A | TPE | Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPE 83A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN TPU 64D.bbsflmt* | eSUN TPU 64D | TPU | Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 64D_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN TPU 80A.bbsflmt* | eSUN TPU 80A | TPU | Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 80A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN TPU 85A.bbsflmt* | eSUN TPU 85A | TPU | Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 85A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN TPU 90A.bbsflmt* | eSUN TPU 90A | TPU | Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 90A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN TPU 95A.bbsflmt* | eSUN TPU 95A | TPU | Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU 95A_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN TPU LW.bbsflmt* | eSUN TPU LW | TPU | Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU LW_&lt;generated&gt; |
| profiles/BambuStudio/eSUN/X2D/0.4mm | eSUN TPU.bbsflmt* | eSUN TPU | TPU | Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_eSUN TPU_&lt;generated&gt; |

\* Not an original vendor export. Generated by `src/convert_old_repo_to_printer.py` from a filament type present in a vendor's registered delta source(s) (`reference-old-repo/`/`reference-bambuprinters/` for TINMORRY, `reference-esun/` for eSUN -- see External references) that had no bundle for that printer yet. Machine-level parameters (temps, per-extruder-variant behavior) come from the closest existing bundle for that same printer and vendor (or, failing that, a repo-wide canonical template, currently always a TINMORRY bundle since eSUN has none of its own yet to fall back to); material-specific tuning (flow ratio, plate temp, fan speed, max volumetric speed) comes from the delta source's own profile. Generation is gated by a machine-compatibility policy -- see "Machine compatibility gating" in CLAUDE.md -- so materials without real evidence of working on a given printer (e.g. PA-CF/PAHT-CF almost everywhere, or any ABS/ASA/PC on the open-frame A1 mini/A2L) are deliberately skipped rather than guessed. **PA-CF and PAHT-CF's X2D bundles in particular did not have nozzle/bed temperature overrides in their source profile**, so they inherited PETG CF's temperature range (245-260 C) rather than PA-CF/PAHT-CF's typically higher real-world requirement (~270-300 C) -- verify against TINMORRY's spec sheet before printing with these two. **Most eSUN bundles on 4-variant printers (H2D, H2S, P2S, X2D) only have real eSUN data for the "Direct Drive Standard" extruder variant** -- eSUN's own per-printer exports almost universally leave the "Direct Drive High Flow"/"Bowden Standard"/"Bowden High Flow" slots of `nozzle_temperature`/`filament_flow_ratio`/`filament_max_volumetric_speed` unspecified (`"nil"`), so those three variants inherit the donor TINMORRY bundle's own values instead of eSUN's -- cross-check against eSUN's official datasheet before printing an eSUN filament on anything but the Direct Drive Standard setup of these printers.

Generated by extracting and inspecting each `.bbsflmt` archive's `bundle_structure.json` and per-printer profile JSON in this repository (2026-07-02), updated after generalizing the conversion tooling to all printers (2026-07-02) and again after adding eSUN as a second vendor (2026-07-10).

## Scripts

- `src/_filament_lib.py` — shared library: the printer registry, machine-compatibility tiers/gating policy, delta-source parsing (`old_repo_entries`/`bambuprinters_entries` for TINMORRY, `esun_entries` for eSUN, combined per-vendor by `delta_entries`), template selection, bundle-merging logic, the custom-override mechanism (`load_custom_override`), and the inventory helpers (`inventory_rows`, `is_original_bundle`) used by the scripts below.
- `src/find_missing_filaments.py [--printer NAME] [--vendor {TINMORRY,eSUN}]` — compares filament types in a vendor's registered delta source(s) against what's already bundled for each printer folder and reports gaps, labeled ALLOW or SKIP per the compatibility policy.
- `src/convert_old_repo_to_printer.py [--printer NAME] [--dry-run] [--vendor {TINMORRY,eSUN}]` — generates new `.bbsflmt` bundles for the ALLOW-labeled gaps. Never modifies an existing bundle, and every generated bundle's machine template traces back to a real, originally-existing bundle for that vendor (never to another bundle generated earlier in the same run). Requires the target vendor's delta source(s) to be present locally (see External references to reclone them). Applies any matching `src/custom_overrides/<vendor>/<printer>/<filament>.json` as the final step.
- `src/gen_inventory_table.py [--check]` — regenerates the "Full profile inventory" table above from the bundles actually on disk. Run after adding/removing any bundle.
- `src/gen_readme_tables.py [--write] [--check]` — regenerates the collapsible, per-slicer, per-vendor, per-printer "Available profiles" tables (filament, Original/Derived, raw-download link) in `README.md`, `README.vi.md`, and `README.zh.md` between their `<!-- BEGIN/END GENERATED PROFILE TABLES -->` markers. Run with `--write` after adding/removing any bundle, alongside `gen_inventory_table.py`.
- `src/unzip_wrapper_zips.py [--dry-run] [--delete-zip]` — finds plain `.zip` files that wrap a `.bbsflmt` bundle inside a subfolder (rather than being a bundle themselves) and extracts the inner `.bbsflmt` directly into the printer folder.

## External references

- [Tinmorry-Bambu_BambuStudio (GitHub)](https://github.com/TINMORRY/Tinmorry-Bambu_BambuStudio) — the original repo this one is forked from.
- [Bambu Studio (GitHub)](https://github.com/bambulab/BambuStudio) — the slicer these profiles are built for; its `resources/profiles` directory documents the same filament-setting schema used inside each bundle here.
- [TINMORRY-filament-profile-for-Bambu-printers (GitHub)](https://github.com/TINMORRY/TINMORRY-filament-profile-for-Bambu-printers.git) — TINMORRY's own upstream profile repo; useful for recovering profiles that are missing or older than what's tracked here. Clone it to `reference-old-repo/` (gitignored) to run the scripts above.
- [eSUN "HS Parameters for Bambu Lab"](https://www.esun3d.com/uploads/HS-Parameters-for-Bambu-Lab-20260511.zip) — eSUN's own per-printer Bambu Studio filament/process export, hosted on esun3d.com's uploads directory (the filename is date-stamped, `20260511` in the version used to generate this repo's eSUN bundles -- check https://www.esun3d.com/ for a newer link if this one 404s). Download and unzip, then copy only the `*Filament.json` files (skip `*Process.json`, out of scope -- see module docstring) into `reference-esun/<Printer>/` (gitignored, printer subfolder names matching the zip's own: `A1`, `A1 Mini`, `H2C`, `H2D`, `H2S`, `P1S`, `P2S`, `X2D`; `P1P`/`X1`/`X1C` have no folder in this repo) to run the scripts above with `--vendor eSUN`.
- [BambuPrinters (GitHub)](https://github.com/tinmorrybinhduong/BambuPrinters) — a separate TINMORRY (Binh Duong) repo with enhanced/tweaked filament and process profiles for Bambu Lab printers; worth checking for material-specific tuning not present in `reference-old-repo/`. Clone it to `reference-bambuprinters/` (gitignored) to make it a second source for `find_missing_filaments.py`/`convert_old_repo_to_printer.py` — see `src/_filament_lib.py`'s `bambuprinters_entries()`.
