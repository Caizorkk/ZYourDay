# Zork Organiza — V3 Profissional

Site estático e responsivo para **GitHub Pages**, com organização de rotinas, ideias, notas, documentos, planilhas, calendário, investimentos e área mista. Não exige Python para funcionar hospedado. Python é usado **somente para montar o `index.html` autocontido**, se você editar os arquivos-fonte.

## Atualizar o seu repositório GitHub Pages

1. Abra o site atual e vá em **Configurações → Baixar backup** para guardar seus dados antes da atualização.
2. No GitHub, no repositório que publica seu site (exemplo `Caizorkk/Zork`), **substitua apenas o arquivo `index.html` na raiz** pelo `index.html` desta versão. Confirme o commit.
3. Depois que o GitHub Pages publicar, pressione **Ctrl+F5** (no celular, abra em uma aba anônima para verificar se o cache foi atualizado).
4. Se você já configurou o login no Firebase, **não substitua seu `config.js`**. O `index.html` carrega esse arquivo separadamente.

Se for criar um repositório do zero, envie o conteúdo deste ZIP para a raiz do repositório, sem colocá-lo dentro de outra pasta. Vá em **Settings → Pages → Deploy from a branch → main → / (root)**.

## Alterações desta versão

- **Logo Zork separada da foto:** a marca do menu é sempre um `Z` branco com brilho neon, ajustando a cor do brilho aos quatro temas; a imagem de perfil nunca muda a marca.
- **Favicon fixo:** a aba do navegador usa **somente a logo Z neon**. Trocar seu nome, inicial ou foto não muda a logo da aba.
- **Nome localizado:** `Zork Organiza` em português/espanhol, `Zork Organize` em inglês. O nome base **Zork** não muda.
- **Cabeçalho limpo:** no topo da página, aparece só `Início`, `Home` ou `Inicio` — ou o nome da seção atual — sem `Zork /`.
- **Avatar correto:** foto pessoal redimensionada ou primeira inicial do display name. Na ausência de nome e foto, aparece um contorno de usuário. O avatar no topo é redondo.
- **Banner simplificado:** nova mensagem com tipografia marcante, fundo com gradiente e **sem o ícone de perfil ou estrela gigante à direita**.
- **Estrelas removidas:** os ícones decorativos de estrela do cabeçalho, telas vazias e notas foram eliminados. O comando para fixar notas agora usa o ícone de alfinete.
- **Correção de inicialização:** restauradas duas funções perdidas na versão anterior (`profileName` e `processAvatar`) que impediam o funcionamento correto de páginas e avatares.
- Mantidos idiomas PT/EN/ES, fuso e data do dispositivo, temas, animações, salvamento local, login/sincronização opcional e as ferramentas já existentes.

## Editar o código

- `index-source.html` — HTML inicial
- `styles.css` — tema, layout e animações
- `js/app.js` — telas, traduções e interações
- `js/store.js` — persistência no navegador / Firebase
- `js/math.js` — fórmulas e simuladores
- `assets/favicon.svg` — logo padrão na aba
- `assets/pix-qr.png` — QR da doação
- `config.js` — parâmetros públicos do Firebase (não insira senhas/secretos)
- `firebase.rules` — regras de acesso; **é necessário publicá-las no Firestore**
- `build.py` — gera a versão autocontida `index.html` executando `python build.py`

Se editar apenas `js/app.js` ou `styles.css`, **reexecute `python build.py`** antes de publicar o `index.html`. O conteúdo do site publicado fica embutido no `index.html` gerado.

## Segurança e limitações

O GitHub Pages não hospeda backend Python. Sem login, dados são salvos somente no navegador (pode perder tudo se os dados forem apagados). Faça backups JSON regularmente. Para autenticação Google, login por e-mail e sincronização entre dispositivos, configure Firebase Authentication + Firestore e suas regras de acesso; esta versão **não substitui essa configuração**. Teste as regras com duas contas.

Os módulos Word/Excel são versões web simplificadas; simuladores de investimento não recebem dados oficiais em tempo real. O código Pix pode expor o nome do recebedor no app de quem paga.

## Validação

Testado em Chromium local com HTML autocontido: inicialização sem erro, 12 menus, PT/EN/ES, datas, nome e inicial de perfil, upload de foto, favicon independente do perfil, tarefas, menu mobile e ausência de transbordamento horizontal em tela de 390 px. Não houve integração com um Firebase real nos testes.
