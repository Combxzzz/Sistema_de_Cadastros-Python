# 📌 Sistema de Cadastro em Python (TXT)

Projeto simples em Python que simula um **mini CRUD**, utilizando arquivos `.txt` para armazenamento de dados.  
O sistema permite **criar, listar e validar usuários**, com foco em **boas práticas, organização de código e validação de entrada**.

---

## 🛠️ Funcionalidades

✔ Verificação automática do arquivo de dados  
✔ Criação do arquivo caso não exista  
✔ Cadastro de usuários com validação  
✔ Prevenção de usuários duplicados  
✔ Listagem dos usuários cadastrados  
✔ Interface em menu no terminal  
✔ Organização em módulos  

---

## 📂 Estrutura do Projeto

```text
Sistema_de_Cadastro/
│
├── Interface/
│   └── __init__.py     # Menu e interação com o usuário
│
├── Seguranca/
│   └── __init__.py     # Verificação e criação do arquivo
│
├── Servicos/
│   └── __init__.py     # Regras de negócio (cadastro, listagem)
│
├── Dados.txt           # Arquivo onde os dados são armazenados
│
└── main.py             # Ponto de entrada do sistema

