# EduPay 📚💸

**EduPay** é um aplicativo Android desenvolvido com o objetivo de facilitar o controle de pagamentos estudantis, oferecendo funcionalidades modernas como acúmulo de pontos, troca por produtos, histórico de mensalidades, feedback, entre outras.

---

## 📲 Funcionalidades

- **Cadastro e Login com Firebase Authentication**
- **Tela de Pagamentos:** cadastro e consulta de mensalidades
- **Sistema de Pontos:** cada mensalidade paga gera 40 pontos
- **Troca de Pontos:** permite trocar pontos acumulados por produtos disponíveis
- **Tela de Feedback:** envio de mensagem, e-mail e avaliação por estrelas
- **Navegação entre telas com animações personalizadas**
- **Firebase Realtime Database** para gerenciamento dos dados

---

## 🛠️ Tecnologias Utilizadas

- **Android Studio** com Java (Groovy)
- **Firebase Authentication** (login/cadastro)
- **Firebase Realtime Database** (dados de usuários e pagamentos)
- **XML** para layouts personalizados
- **Animações** para navegação entre telas
- **Criptografia de senhas integrada via Firebase**

---

## 📁 Organização das Telas

| Tela | Descrição |
|------|-----------|
| `LoginActivity.java` | Login do usuário com validação Firebase |
| `CadastroActivity.java` | Cadastro com campos: nome completo, CPF, celular, data de nascimento, e-mail e senha |
| `TelaPagamentosActivity.java` | Permite cadastrar e consultar pagamentos |
| `TelaTrocaPontosActivity.java` | Lista produtos disponíveis para troca |
| `TelaFeedbackActivity.java` | Envio de feedback com avaliação em estrelas |
| `TelaEscolhaPagamentoActivity.java` | Escolha entre PIX, boleto ou cartão |
| `TelaPixActivity.java`, `TelaBoletoActivity.java`, `TelaCartaoActivity.java` | Exibição dos dados conforme método escolhido |
| `MainActivity.java` | Tela de boas-vindas e navegação principal |

---

## 🧠 Regras de Pontuação

- Cada mensalidade paga = **+40 pontos**
- Pontos acumulados podem ser trocados por produtos cadastrados no app

---

## 🔐 Segurança

- Firebase Authentication para autenticação segura
- Senhas criptografadas automaticamente via Firebase
- Regras de segurança configuradas no Firebase Realtime Database

---

## 👥 Desenvolvedores

Este projeto foi desenvolvido por alunos do curso de Análise e Desenvolvimento de Sistemas da **FATEC** – 1º semestre de 2025.

Repositório oficial: [https://github.com/2025-1-NADS3/Projeto10](https://github.com/2025-1-NADS3/Projeto10)

---

## 📌 Como Executar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/2025-1-NADS3/Projeto10.git
