# Flask-API
Projeto desenvolvido com o framework Flask da linguagem Python, criando uma API utilizando MYSQL para o armazenamento dos dados.

No diretório API do projeto foi criado uma API REST mas utilizando dicionário para armazenamento dos dados. Na qual o Cliente recebe como parâmetros o ID, Nome, Email, CPF.

![image](https://user-images.githubusercontent.com/106355267/203422743-96eba2a1-6752-45c3-a31d-9a8784d0bc1e.png)

Os métodos criados foram:

GET trazendo todos os resultados da API

![image](https://user-images.githubusercontent.com/106355267/203422962-404f3a92-40f1-4589-ac8d-cc5e4e8c8744.png)

GET retornando apenas um Cliente com base no ID repassado

![image](https://user-images.githubusercontent.com/106355267/203423160-55fd18e6-3e02-4609-8bca-209d3216b8d4.png)

POST para cadastrar um novo cliente

![image](https://user-images.githubusercontent.com/106355267/203423212-f6cd0317-7662-4a6a-8311-f617514a6c06.png)

PUT para realizar alteração nos dados do cliente com base no ID repassado

![image](https://user-images.githubusercontent.com/106355267/203423309-8f1e9af0-7473-436c-aef7-2710bf45e1b9.png)

DELETE para excluir o cadastro do cliente

![image](https://user-images.githubusercontent.com/106355267/203423410-765d2fe6-a07e-42b3-8756-01c19ba72634.png)

No diretório API_MYSQL foi criado uma API, mas ao invés de utilizar um dicionário, foi utilizado o MYSQL para armazenamento e interação dos dados. 

No MYSQL foi criado um database Store e uma TABLE customers

![image](https://user-images.githubusercontent.com/106355267/203424030-4d3332c4-984b-43c3-a1ac-51c0a48f0aae.png)

A partir desse banco de dados foi utilizado as Query do MYSQL para a criação do métodos da API.


