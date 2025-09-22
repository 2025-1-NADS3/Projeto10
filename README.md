# 🎓 FECAP - Fundação de Comércio Álvares Penteado

<p align="center">
  <a href="https://www.fecap.br/">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhZPrRa89Kma0ZZogxm0pi-tCn_TLKeHGVxywp-LXAFGR3B1DPouAJYHgKZGV0XTEf4AE&usqp=CAU" alt="FECAP">
  </a>
</p>

# 🍰 Cannoli - Gestão e Experiência Gastronômica

---

## 👨‍💻 Integrantes

- [Caua William Barbieri Brandão](https://www.linkedin.com/in/caua-william-967295247/)
- [Gabriel Orlandi Portes](https://www.linkedin.com/in/gabriel-orlandi-4b5ab22ab)
- [Karoline Lemos Avelar](https://www.linkedin.com/in/karoline-lemos-540461296)
- [Matheus Santoro Carriço Veiga](https://www.linkedin.com/in/matheus-santoro-34b7a7186)

## 👨‍🏫 Professores Orientadores

- [Aimar Martins Lopes](https://www.linkedin.com/in/aimarlopes/)
- [Eduardo Savino](https://www.linkedin.com/in/francisco-escobar/)
- [Lucy Mary](https://www.linkedin.com/in/vheltai/)
- [Edson Barbeiro](https://www.linkedin.com/in/jefferson-o-silva/)
- [Ronaldo Araujo](https://www.linkedin.com/in/jefferson-o-silva/)

---

## ✨ Funcionalidades do App

- 📲 Cadastro e login com autenticação Firebase
- 💰 Visualização de mensalidades e geração de boletos
- 🧾 Registro de pagamentos realizados
- ⭐ Acúmulo de pontos a cada mensalidade paga
- 🎁 Troca de pontos por produtos ou benefícios
- 👨‍💼 Tela administrativa para visualizar transações
- 🔐 Criptografia de senha
- 🔄 Comunicação via API com Firebase Firestore

---

## 🧠 Tecnologias Utilizadas

### 🔧 Mobile
- Android Studio (Groovy)
- Firebase Authentication
- Firebase Firestore
- Firebase Realtime Database
- Firebase Hosting (Dashboard Administrativo)
- Firebase Storage (opcional para armazenar imagens dos produtos)
- Material Design Components

### 💻 Backend
- Firebase Functions (para lógica avançada e validações)
- Firebase Cloud Firestore (como banco de dados principal)

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

Este projeto foi desenvolvido por alunos do curso de Análise e Desenvolvimento de Sistemas da **FECAP** – 3º semestre de 2025.

## 📚 Referências

- [https://firebase.google.com/docs](https://firebase.google.com/docs)
- [https://developer.android.com/docs](https://developer.android.com/docs)
- [https://material.io/components](https://material.io/components)
- [https://developer.android.com/training/data-storage/shared-preferences](https://developer.android.com/training/data-storage/shared-preferences)
- [https://developer.android.com/guide/navigation](https://developer.android.com/guide/navigation)
- [https://developer.android.com/studio](https://developer.android.com/studio)

