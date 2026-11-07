# Kaasasolevad sõltuvused

Veeb kasutab Pyodide 314.0.7 ametlikku distributsiooni: https://cdn.jsdelivr.net/pyodide/v314.0.7/full/ . Käituskeskkonna räside väljavõte on materjalid/PYODIDE_SHA256.json. Pydanticu ja selle sõltuvuste wheel-failide SHA-256 kontrolliti ametliku pyodide-lock.json vastu. Distributsiooni litsents on veeb/runtime/LICENSE-PYODIDE; wheel-paketid sisaldavad oma litsentsiandmeid.

Kaasas on Pydantic 2.12.5, pydantic-core 2.41.5 ja nende lukufailis loetletud sõltuvused ning micropip. openpyxl 3.1.5 ja et-xmlfile 2.0.0 wheel-failid pärinevad PyPI-st ning säilitavad oma metaandmed ja litsentsid. Kohalikud analüüsisõltuvused on requirements.txt-s.

Google Fontsist küsitakse DM Sans ja Manrope fonte; kui laadimine ei õnnestu, kasutatakse Arial/sans-serif varufonti. Mingit arveinfot fontide päringuga ei edastata. Fonte pole projektiga binaarfailidena kaasa pakitud.
