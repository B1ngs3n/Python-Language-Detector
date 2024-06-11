def get_language_name_by_id(id):
    match id.upper():
        case "AB":
            return "Abkhazian (AB)"
        case "AA":
            return "Afar (AA)"
        case "AF":
            return "Afrikaans (AF)"
        case "AK":
            return "Akan (AK)"
        case "SQ":
            return "Albanian (SQ)"
        case "AM":
            return "Amharic (AM)"
        case "AR":
            return "Arabic (AR)"
        case "AN":
            return "Aragonese (AN)"
        case "HY":
            return "Armenian (HY)"
        case "AS":
            return "Assamese (AS)"
        case "AV":
            return "Avaric (AV)"
        case "AE":
            return "Avestan (AE)"
        case "AY":
            return "Aymara (AY)"
        case "AZ":
            return "Azerbaijani (AZ)"
        case "BM":
            return "Bambara (BM)"
        case "BA":
            return "Bashkir (BA)"
        case "EU":
            return "Basque (EU)"
        case "BE":
            return "Belarusian (BE)"
        case "BN":
            return "Bengali (BN)"
        case "BI":
            return "Bislama (BI)"
        case "BS":
            return "Bosnian (BS)"
        case "BR":
            return "Breton (BR)"
        case "BG":
            return "Bulgarian (BG)"
        case "MY":
            return "Burmese (MY)"
        case "CA":
            return "Catalan, Valencian (CA)"
        case "CH":
            return "Chamorro (CH)"
        case "CE":
            return "Chechen (CE)"
        case "NY":
            return "Chichewa, Chewa, Nyanja (NY)"
        case "ZH":
            return "Chinese (ZH)"
        case "CU":
            return "Church Slavonic, Old Slavonic, Old Church Slavonic (CU)"
        case "CV":
            return "Chuvash (CV)"
        case "KW":
            return "Cornish (KW)"
        case "CO":
            return "Corsican (CO)"
        case "CR":
            return "Cree (CR)"
        case "HR":
            return "Croatian (HR)"
        case "CS":
            return "Czech (CS)"
        case "DA":
            return "Danish (DA)"
        case "DV":
            return "Divehi, Dhivehi, Maldivian (DV)"
        case "NL":
            return "Dutch, Flemish (NL)"
        case "DZ":
            return "Dzongkha (DZ)"
        case "EN":
            return "English (EN)"
        case "EO":
            return "Esperanto (EO)"
        case "ET":
            return "Estonian (ET)"
        case "EE":
            return "Ewe (EE)"
        case "FO":
            return "Faroese (FO)"
        case "FJ":
            return "Fijian (FJ)"
        case "FI":
            return "Finnish (FI)"
        case "FR":
            return "French (FR)"
        case "FY":
            return "Western Frisian (FY)"
        case "FF":
            return "Fulah (FF)"
        case "GD":
            return "Gaelic, Scottish Gaelic (GD)"
        case "GL":
            return "Galician (GL)"
        case "LG":
            return "Ganda (LG)"
        case "KA":
            return "Georgian (KA)"
        case "DE":
            return "German (DE)"
        case "EL":
            return "Greek, Modern (EL)"
        case "KL":
            return "Kalaallisut, Greenlandic (KL)"
        case "GN":
            return "Guarani (GN)"
        case "GU":
            return "Gujarati (GU)"
        case "HT":
            return "Haitian, Haitian Creole (HT)"
        case "HA":
            return "Hausa (HA)"
        case "HE":
            return "Hebrew (HE)"
        case "HZ":
            return "Herero (HZ)"
        case "HI":
            return "Hindi (HI)"
        case "HO":
            return "Hiri Motu (HO)"
        case "HU":
            return "Hungarian (HU)"
        case "IS":
            return "Icelandic (IS)"
        case "IO":
            return "Ido (IO)"
        case "IG":
            return "Igbo (IG)"
        case "ID":
            return "Indonesian (ID)"
        case "IA":
            return "Interlingua (IA)"
        case "IE":
            return "Interlingue, Occidental (IE)"
        case "IU":
            return "Inuktitut (IU)"
        case "IK":
            return "Inupiaq (IK)"
        case "GA":
            return "Irish (GA)"
        case "IT":
            return "Italian (IT)"
        case "JA":
            return "Japanese (JA)"
        case "JV":
            return "Javanese (JV)"
        case "KN":
            return "Kannada (KN)"
        case "KR":
            return "Kanuri (KR)"
        case "KS":
            return "Kashmiri (KS)"
        case "KK":
            return "Kazakh (KK)"
        case "KM":
            return "Central Khmer (KM)"
        case "KI":
            return "Kikuyu, Gikuyu (KI)"
        case "RW":
            return "Kinyarwanda (RW)"
        case "KY":
            return "Kirghiz, Kyrgyz (KY)"
        case "KV":
            return "Komi (KV)"
        case "KG":
            return "Kongo (KG)"
        case "KO":
            return "Korean (KO)"
        case "KJ":
            return "Kuanyama, Kwanyama (KJ)"
        case "KU":
            return "Kurdish (KU)"
        case "LO":
            return "Lao (LO)"
        case "LA":
            return "Latin (LA)"
        case "LV":
            return "Latvian (LV)"
        case "LI":
            return "Limburgan, Limburger, Limburgish (LI)"
        case "LN":
            return "Lingala (LN)"
        case "LT":
            return "Lithuanian (LT)"
        case "LU":
            return "Luba-Katanga (LU)"
        case "LB":
            return "Luxembourgish, Letzeburgesch (LB)"
        case "MK":
            return "Macedonian (MK)"
        case "MG":
            return "Malagasy (MG)"
        case "MS":
            return "Malay (MS)"
        case "ML":
            return "Malayalam (ML)"
        case "MT":
            return "Maltese (MT)"
        case "GV":
            return "Manx (GV)"
        case "MI":
            return "Maori (MI)"
        case "MR":
            return "Marathi (MR)"
        case "MH":
            return "Marshallese (MH)"
        case "MN":
            return "Mongolian (MN)"
        case "NA":
            return "Nauru (NA)"
        case "NV":
            return "Navajo, Navaho (NV)"
        case "ND":
            return "North Ndebele (ND)"
        case "NR":
            return "South Ndebele (NR)"
        case "NG":
            return "Ndonga (NG)"
        case "NE":
            return "Nepali (NE)"
        case "NO":
            return "Norwegian (NO)"
        case "NB":
            return "Norwegian Bokmål (NB)"
        case "NN":
            return "Norwegian Nynorsk (NN)"
        case "II":
            return "Sichuan Yi, Nuosu (II)"
        case "OC":
            return "Occitan (OC)"
        case "OJ":
            return "Ojibwa (OJ)"
        case "OR":
            return "Oriya (OR)"
        case "OM":
            return "Oromo (OM)"
        case "OS":
            return "Ossetian, Ossetic (OS)"
        case "PI":
            return "Pali (PI)"
        case "PS":
            return "Pashto, Pushto (PS)"
        case "FA":
            return "Persian (FA)"
        case "PL":
            return "Polish (PL)"
        case "PT":
            return "Portuguese (PT)"
        case "PA":
            return "Punjabi, Panjabi (PA)"
        case "QU":
            return "Quechua (QU)"
        case "RO":
            return "Romanian, Moldavian, Moldovan (RO)"
        case "RM":
            return "Romansh (RM)"
        case "RN":
            return "Rundi (RN)"
        case "RU":
            return "Russian (RU)"
        case "SE":
            return "Northern Sami (SE)"
        case "SM":
            return "Samoan (SM)"
        case "SG":
            return "Sango (SG)"
        case "SA":
            return "Sanskrit (SA)"
        case "SC":
            return "Sardinian (SC)"
        case "SR":
            return "Serbian (SR)"
        case "SN":
            return "Shona (SN)"
        case "SD":
            return "Sindhi (SD)"
        case "SI":
            return "Sinhala, Sinhalese (SI)"
        case "SK":
            return "Slovak (SK)"
        case "SL":
            return "Slovenian (SL)"
        case "SO":
            return "Somali (SO)"
        case "ST":
            return "Southern Sotho (ST)"
        case "ES":
            return "Spanish, Castilian (ES)"
        case "SU":
            return "Sundanese (SU)"
        case "SW":
            return "Swahili (SW)"
        case "SS":
            return "Swati (SS)"
        case "SV":
            return "Swedish (SV)"
        case "TL":
            return "Tagalog (TL)"
        case "TY":
            return "Tahitian (TY)"
        case "TG":
            return "Tajik (TG)"
        case "TA":
            return "Tamil (TA)"
        case "TT":
            return "Tatar (TT)"
        case "TE":
            return "Telugu (TE)"
        case "TH":
            return "Thai (TH)"
        case "BO":
            return "Tibetan (BO)"
        case "TI":
            return "Tigrinya (TI)"
        case "TO":
            return "Tonga (Tonga Islands) (TO)"
        case "TS":
            return "Tsonga (TS)"
        case "TN":
            return "Tswana (TN)"
        case "TR":
            return "Turkish (TR)"
        case "TK":
            return "Turkmen (TK)"
        case "TW":
            return "Twi (TW)"
        case "UG":
            return "Uighur, Uyghur (UG)"
        case "UK":
            return "Ukrainian (UK)"
        case "UR":
            return "Urdu (UR)"
        case "UZ":
            return "Uzbek (UZ)"
        case "VE":
            return "Venda (VE)"
        case "VI":
            return "Vietnamese (VI)"
        case "VO":
            return "Volapük (VO)"
        case "WA":
            return "Walloon (WA)"
        case "CY":
            return "Welsh (CY)"
        case "WO":
            return "Wolof (WO)"
        case "XH":
            return "Xhosa (XH)"
        case "YI":
            return "Yiddish (YI)"
        case "YO":
            return "Yoruba (YO)"
        case "ZA":
            return "Zhuang, Chuang (ZA)"
        case "ZU":
            return "Zulu (ZU)"
        case _:
            return "Unknown language code"