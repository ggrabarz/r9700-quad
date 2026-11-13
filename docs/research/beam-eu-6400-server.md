# DDR5-6400 RDIMMs that run from JEDEC SPD @ 1.1 V on the H14SSL-N/NT — EU retail

Fetch date: 2026-11-13. Board constraint: H14SSL-N/NT BIOS is JEDEC-only (no EXPO/XMP, no voltage/timing menu; "Memory Target Speed" lists Auto/3600/4000/4400/4800/5200). A module qualifies only if its SPD defaults to DDR5-6400 at 1.1 V.

**Verdict:** cheapest qualifying 12-module buy with confirmed EU stock today is 12× Samsung M321R4GA3EB2-CCP at Tonitrus (€29,994); the cheaper 3× Kingston KF576RH40RBK4-128 route (≈€17,700, 12×32 GB) is listed at Proshop.pl but its stock/lead time could not be verified.

## What I checked

- Kingston Server Premier datasheets (kingston.com/datasheets/<PART>.pdf) for KSM64R52BD4-64MD/MH/HA (64 GB 2Rx4) and KSM64R52BD8-32MD/MH/HA (32 GB 2Rx8): all state "SPD is programmed to JEDEC standard latency DDR5-6400 timing of 52-52-52 at 1.1V" → PASS.
- Kingston FURY Renegade Pro datasheets KF572RH38RB-16/32 and KF576RH40RB-16/32: "The SPDs are programmed to JEDEC standard latency DDR5-6400 timing of 52-52-52 at 1.1V" → PASS (7200/7600 kits run 6400 from SPD). KF564R32RBE states SPD = JEDEC DDR5-4800 → FAILS (6400 only via EXPO/1.4 V).
- Samsung M321R8GA0EB2-CCP (64 GB 2Rx4) and M321R4GA3EB2-CCP (32 GB 2Rx8): server RDIMMs, 6400 MT/s, 1.1 V, CL52; no EXPO/XMP profile → JEDEC (official Samsung SPD sentence not found; third-party reference only → marked UNVERIFIED).
- Supermicro QVL part MEM-DR564MC-ER64 maps to Samsung M321R8GA0PB2-CCP (64 GB 2Rx4 6400) — PASS but out of stock / price on request at Tonitrus.
- SK hynix HMCG94AHBRA480N (64 GB 2Rx4 6400, 1.1 V) → JEDEC server part, but no EU retail listing found (US distributors only).
- Micron MTC40F2046S1RC64BH1 (64 GB 2Rx4) → 6400 MT/s, CL52, 1.1 V, JEDEC (Micron page does not print an SPD sentence → UNVERIFIED). Micron 32 GB 6400 parts (MTC20F2085S1RC64BH1/BD2, MTC20F1045S1RC64BD2) → JEDEC but no EU retail listing found.
- EU shops checked: Tonitrus, ibfusion, Proshop.pl (blocked at fetch time, price from earlier successful fetch), Galaxus/Heizhals/idealo (blocked).

## Results (qualifying, EU-buyable)

| Part number | Capacity / ranks | JEDEC SPD default + voltage | EU shop | Price | Stock / lead | URL | Notes |
|---|---|---|---|---|---|---|---|
| Kingston KSM64R52BD4-64MD (also -64MH, -64HA) | 64 GB 2Rx4 | JEDEC DDR5-6400 CL52-52-52 @ 1.1 V (quote: "SPD is programmed to JEDEC standard latency DDR5-6400 timing of 52-52-52 at 1.1V") | ibfusion.com | €2,481 (VAT 0%, export) | 4 in stock | https://ibfusion.com/ram/64gb-ddr5-rdimm-ecc-6400mhz/ | Suffixes interchangeable (DRAM vendor only); specialist, price changes daily |
| Kingston KSM64R52BD8-32MH (also -32MD, -32HA) | 32 GB 2Rx8 | JEDEC DDR5-6400 CL52-52-52 @ 1.1 V (same SPD sentence) | ibfusion.com | €1,421 (VAT 0%, export) | 5 in stock | https://ibfusion.com/ram/32gb-ddr5-rdimm-ecc-6400mhz/ | Suffixes interchangeable; specialist |
| Micron MTC40F2046S1RC64BH1 | 64 GB 2Rx4 | 6400 MT/s, CL52, 1.1 V (JEDEC; Micron page has no SPD sentence → UNVERIFIED) | Tonitrus (DE) | €3,158.50 new / €3,693.50 refurbished (incl. VAT) | NEW 2 / REF 50, 3-4 workdays | https://www.tonitrus.com/MTC40F2046S1RC64BH1_1 | EU stock small for new |
| Samsung M321R8GA0EB2-CCP | 64 GB 2Rx4 | 6400 MT/s, CL52, 1.1 V (JEDEC inferred; no official SPD quote → UNVERIFIED) | Tonitrus (DE) | €3,174.50 (incl. VAT) | 50 new, 3-4 workdays | https://www.tonitrus.com/M321R8GA0EB2-CCP | Real EU shop, in stock |
| Samsung M321R4GA3EB2-CCP | 32 GB 2Rx8 | 6400 MT/s, CL52, 1.1 V (JEDEC inferred; UNVERIFIED) | Tonitrus (DE) | €2,499.50 (incl. VAT) | 50 new, 3-4 workdays | https://www.tonitrus.com/M321R4GA3EB2-CCP | Real EU shop, in stock |
| Kingston KF576RH40RBK4-128 (4× KF576RH40RB) | 4×32 GB 1Rx8 | SPD JEDEC DDR5-6400 CL52-52-52 @ 1.1 V (quote: "The SPDs are programmed to JEDEC standard latency DDR5-6400 timing of 52-52-52 at 1.1V") | Proshop.pl | 25,969 PLN/kit ≈ €5,893 (4 modules) | Not verified (page blocked at fetch) | https://www.proshop.pl/RAM/Kingston-FURY-Renegade-PRO-DDR5-7600-128GB-CL38-Quad-Channel-4-pcs-AMD-EXPO-Intel-EXPO-Czarny/3462079 | EXPO kit but JEDEC default 6400; 3 kits = 12 modules ≈ €17,700 |
| Kingston KF572RH38RBK8-256 (8× KF572RH38RB) | 8×32 GB 1Rx8 | SPD JEDEC DDR5-6400 CL52-52-52 @ 1.1 V (same SPD sentence) | Proshop.pl | 50,712 PLN/kit ≈ €11,507 (8 modules) | Not verified (page blocked at fetch) | https://www.proshop.pl/RAM/Kingston-FURY-Renegade-PRO-DDR5-7200-256GB-CL38-Octa-Channel-8-pcs-AMD-EXPO-Intel-EXPO-Czarny/3462075 | EXPO kit but JEDEC default 6400; + 1× KF576 kit = 12 modules ≈ €17,400 |

## Could not verify / blocked / not EU-buyable

- Kingston KF564R32RBE (6400 CL32): SPD = JEDEC DDR5-4800 → FAILS (6400 only via EXPO at 1.4 V); listed at Proshop.pl 32,458 PLN but does not qualify.
- Samsung M321R8GA0PB2-CCP (64 GB 2Rx4 6400): PASS but out of stock / price on request at Tonitrus (https://www.tonitrus.com/M321R8GA0PB2-CCP); Supermicro QVL part MEM-DR564MC-ER64 maps here (US: WiredZone).
- SK hynix HMCG94AHBRA480N (64 GB 2Rx4 6400, 1.1 V): PASS but no EU retail listing found (US distributors only).
- Micron MTC40F2046S1RC64BD2 (64 GB 2Rx4): PASS but only price range seen at Tonitrus (€3,693.50-3,884.50); stock not confirmed.
- Micron 32 GB 6400 parts (MTC20F2085S1RC64BH1/BD2, MTC20F1045S1RC64BD2): PASS but no EU retail listing found.
- Samsung 32 GB 6400 part M321R4GA0EB2-CCP (1Rx4): PASS but no EU listing found.
- Galaxus, Heise preisvergleich, Geizhals, idealo, Alternate, Mindfactory, Caseking, Amazon.de/pl, Morele, x-kom, komputronik: blocked or no results for the qualifying parts at fetch time.
- Manufacturer QVL/SPD verification for Samsung/Micron/SK hynix: no JEDEC SPD sentence quoted (third-party references only) → marked UNVERIFIED where applicable.
- Kingston ValueRAM KVR "6400" parts found (KVR64A52BD8-64 etc.) are CUDIMM/unbuffered, not RDIMM → excluded.