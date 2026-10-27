# Zork Organiza — V2 ajustada (base original preservada)

Esta versão foi feita **a partir do ZIP V2 original fornecido pelo criador**, sem usar a V3. Mantém os mesmos módulos, armazenamento local e integração opcional com Firebase.

**Ajustes visuais apenas:** marca discreta com Z branco e leve neon; nome Zork Organiza (PT/ES) ou Zork Organize (EN); breadcrumb mostra somente a página; banner sem avatar/estrela; foto do usuário aparece apenas nos avatares; favicon Z fixo; estrelas decorativas substituídas por ícones neutros.

**Como publicar no GitHub:** substitua o `index.html` na raiz. Se já tiver Firebase configurado, **não substitua seu `config.js`**. Faça backup JSON antes de atualizar. O `index.html` é autocontido, mas o `config.js` externo ainda precisa estar na raiz para login configurado.

---

# Zork Organiza — V2.0

Organizador web com tarefas, ideias, calculadora, anotações em cartões, editor de documentos, planilhas com fórmulas básicas, calendário, planejador de investimentos, área mista (quatro ferramentas), guia e doações por Pix.

## Instalação no GitHub Pages

### Já tem o Zork no GitHub?

1. **Faça um backup pelo próprio site** antes de trocar a versão (Configurações → Baixar backup).
2. Copie **somente `index.html`** desta versão para a **raiz** do repositório (onde está o arquivo atual).
3. Clique em **Commit changes** e aguarde o GitHub Pages publicar. Atualize usando **Ctrl + F5**.
4. **Não substitua o seu `config.js` atual**, caso já tenha configurado o Firebase. A atualização usa as mesmas chaves de armazenamento (`zork-organiza-v1`) da V1; as anotações não são excluídas pela troca do arquivo.

### Novo repositório

Envie o conteúdo deste ZIP para a raiz do repositório e, em **Settings → Pages**, selecione **Deploy from a branch → main → / (root)**. A URL seguirá o formato `https://SEU-USUARIO.github.io/NOME-DO-REPOSITORIO/`. A página de entrada precisa se chamar `index.html`.

O `index.html` da V2 já contém os estilos, códigos JavaScript e QR Pix embutidos. É suficiente para usar sem conta. `config.js` separado ativa login/sincronização quando configurado.

## Novidades da V2

- **Visual redesenhado:** dark preto e branco, roxo vibrante, fontes Outfit/Plus Jakarta Sans, cards e botões reformulados; também há tema claro, galáxia clara e galáxia noturna, combinados com visual moderno/intermediário/clássico.
- **Aparecimento com rolagem:** animações leves em cada seção ao aparecer na tela; respeita a preferência do sistema para reduzir movimento.
- **Perfil:** nome visível, ícones predefinidos ou foto JPG/PNG/WebP opcional. Sem foto ou ícone especial, o avatar mostra a **primeira letra do nome**. O ícone aparece no menu, no topo, no banner e na aba do navegador. Fotos são redimensionadas para 192×192 px antes de salvar.
- **Cadastro por e-mail:** solicita nome de exibição e oferece foto opcional. No primeiro login pelo Google, exibe convite para configurar perfil (se ainda não tiver perfil salvo).
- **Idiomas:** português, inglês e espanhol. O modo automático usa o idioma preferido do navegador e considera os fusos conhecidos do Brasil para priorizar português. A interface foi traduzida amplamente; mensagens técnicas e algumas funções podem continuar em português. É possível forçar qualquer idioma nas configurações.
- **Data e hora:** relógio atualizado na página, com o fuso horário **do próprio navegador/dispositivo**. Configuração de data regional, brasileira DD/MM/AAAA ou americana MM/DD/AAAA. Não usa GPS nem detecta a localização física com precisão: ajuste o fuso do aparelho caso esteja errado.
- **Salvar sem avisos repetitivos:** o aviso permanente “Salvo neste navegador” foi removido. O armazenamento local continua automático.

## Dados, privacidade e sincronização

- Sem login, dados e preferências ficam no `localStorage` deste navegador. Isso **não é backup confiável** caso o navegador seja apagado; exporte backups JSON periodicamente.
- Com login, se o Firebase estiver configurado, cada conta salva preferências e registros no **Firestore**. As regras de acesso devem ser publicadas no console Firebase. A foto de perfil reduzida também faz parte das preferências privadas do usuário, sincronizadas em conta (sem upload para um servidor de imagens público).
- A sincronização não é edição colaborativa de texto caractere a caractere. Alterações concorrentes sobre o mesmo registro podem sobrescrever umas às outras.
- **As versões do Word e Excel são editores web simplificados**; não implementam todos os comandos ou compatibilidade integral dos aplicativos Microsoft.
- **Simulações de investimento** usam taxas fornecidas pelo usuário; não consultam taxas oficiais em tempo real e não são promessa de rendimento.
- O QR Code Pix contém o nome do recebedor, que pode aparecer para qualquer doador. Verifique os dados do destinatário no aplicativo do banco.

## Configuração do Firebase (opcional)

1. Crie um projeto em [Firebase Console](https://console.firebase.google.com/), registre um aplicativo Web e copie o `firebaseConfig`.
2. Configure os valores públicos de `window.ZORK_FIREBASE_CONFIG` no `config.js` (arquivo da raiz).
3. Habilite Google e/ou Email/Password em **Authentication → Sign-in method**.
4. Adicione seu domínio `SEU-USUARIO.github.io` em **Authentication → Settings → Authorized domains**.
5. Crie o **Firestore Database** e publique o conteúdo de `firebase.rules` em **Firestore Database → Rules**.
6. Teste com duas contas distintas antes de disponibilizar o site a outras pessoas. Não coloque senhas, chaves privadas ou arquivos de conta de serviço no GitHub.

A configuração pública do aplicativo Web Firebase não é uma senha; as regras de acesso do Firestore são a proteção real dos dados.

## Estrutura e manutenção

```text
Zork_Organiza_V2/
├── index.html          ← pronto para hospedar (tudo embutido)
├── index-source.html   ← HTML-fonte com links para CSS/JS
├── styles.css          ← estilos editáveis
├── js/
│   ├── app.js          ← interface e interações
│   ├── store.js        ← dados locais e integração Firebase
│   └── math.js         ← cálculos e fórmulas
├── assets/
│   ├── favicon.svg
│   └── pix-qr.png
├── config.js           ← configurar Firebase se desejar
├── firebase.rules      ← publicar no console Firebase
└── build.py            ← recompila o index.html a partir das fontes
```

**Para editar código:** altere `styles.css`, `js/*.js` ou `index-source.html` e execute `python build.py`. Depois publique o `index.html` recompilado. Modificar os módulos sem gerar um novo index não afeta a versão publicada.

## Testes da V2

Em Chromium local, foram verificadas a renderização do menu (12 seções), tarefas, calendário e investimentos, troca de idioma PT/EN/ES, formato americano/brasileiro de data, nome/inicial, ícone, upload de foto, relógio em diferentes fusos brasileiros, navegação mobile e as animações ao rolar. A autenticação e sincronização **não foram testadas com um projeto Firebase real** — essas funcionalidades exigem a sua configuração.

Esta aplicação permanece hospedável de forma estática pelo GitHub Pages. Python é utilizado apenas como ferramenta de compilação (`build.py`), não como servidor de produção.
