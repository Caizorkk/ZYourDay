"""Gera index.html autocontido para GitHub Pages usando somente Python 3.
Execute: python build.py  (na pasta do projeto)
O site funciona em HTML/CSS/JavaScript. Python é usado só para empacotar.
"""
from pathlib import Path
import re,base64
ROOT=Path(__file__).resolve().parent
html=(ROOT/'index-source.html').read_text(encoding='utf-8')
css=(ROOT/'styles.css').read_text(encoding='utf-8')
math=(ROOT/'js/math.js').read_text(encoding='utf-8')
store=(ROOT/'js/store.js').read_text(encoding='utf-8')
app=(ROOT/'js/app.js').read_text(encoding='utf-8')
exports=re.findall(r'export (?:async function|function|const) (\w+)',store)
math=re.sub(r'\bexport\s+(?=(?:function|const)\b)','',math)
store=re.sub(r'\bexport\s+(?=(?:async\s+)?(?:function|const)\b)','',store)
app=app.replace("import * as db from './store.js';\n",'').replace("import {compute,cellValue,colName,money,forecast,annualRate,csvEscape,parseCSV} from './math.js';\n",'')
assert not re.search(r'^\s*import ',app,re.M),'Remova imports que não são compatíveis com o pacote autocontido.'
js='\n;(function(){\n"use strict";\n'+math+'\n'+store+'\nconst db={'+','.join(exports)+'};\n'+app+'\n})();\n'
assert '</script' not in js.lower(),'Código JS contém tag de fechamento e não pode ser embutido.'
assert '<link rel="stylesheet" href="styles.css" />' in html
assert '<script type="module" src="js/app.js"></script>' in html
html=html.replace('<link rel="stylesheet" href="styles.css" />','<style>\n'+css+'\n</style>')
html=html.replace('<script type="module" src="js/app.js"></script>','<script>\n'+js+'\n</script>')
for file,mime in [('assets/favicon.svg','image/svg+xml'),('assets/pix-qr.png','image/png')]:
 data=base64.b64encode((ROOT/file).read_bytes()).decode()
 html=html.replace('href="'+file+'"','href="data:'+mime+';base64,'+data+'"').replace('src="'+file+'"','src="data:'+mime+';base64,'+data+'"')
html=html.replace('<nav id="nav" aria-label="Navegação principal"></nav>','<nav id="nav" aria-label="Navegação principal">Carregando…</nav>')
html=html.replace('<main id="main" tabindex="-1"></main>','<main id="main" tabindex="-1"><div class="panel"><h2>Carregando Zork Organiza…</h2></div></main>')
(ROOT/'index.html').write_text(html,encoding='utf-8')
print('index.html gerado com sucesso (',len(html),'caracteres).')
