# proxy-http


Servidor Proxy HTTP

Para a disciplina de Segurança e Auditoria de Sistemas

Prof. Mauro Fonseca - UTFPR - DAINF

http://dainf.ct.utfpr.edu.br/%7Emaurofonseca/doku.php?id=cursos:if68e:proxy

----

Os servidores proxy são usados tanto para fins legais e ilegais. Na empresa, um servidor proxy é usado para facilitar a segurança, serviços de controle ou de cache administrativos, entre outros fins. Em um contexto de computação pessoal, servidores proxy são usados para ativar a privacidade do usuário e navegação anônima. Os servidores proxy pode também ser utilizado para a finalidade contrária: monitorizar o tráfego e prejudicar a privacidade do usuário .

Para o usuário, o servidor proxy é invisível; todos as requisições para a Internet e respostas parece ser diretamente com o servidor Internet. (O proxy não é realmente invisível, normalmente seu endereço IP tem de ser especificado como uma opção de configuração para o navegador ou outro programa de protocolo.)

Este trabalho tem a finalidade de trazer o conhecimento do mecanismo de funcionamento do proxy.

O trabalho deve:

    Usar Sockets TCP
        Cliente e Servidor
    Receber requisições HTTP do Cliente
        Colocar no browser o servidor proxy como endereço onde roda o proxy
    Enviar as requisições para o servidor
    Receber as resposta do servidor e repassar para o cliente
    Caso o nome do objeto requisitado contenha a palavra “monitorando” deve ser devolvido uma Pagina HTML com a mensagem “Acesso não autorizado!”
    apresentar no proxy as informações:
        endereço IP do cliente e do servidor de cada requisição
        Código da resposta (Ex: 200 OK)

    Este trabalho deverá ser defendido para o professor nas aulas definidas para este propósito para validar a nota.
    Requisições HTTP


