#! bin bash

echo 'Copiando o arquivo de configuração da AeC'
cp /home/ejabberd.yml /usr/local/etc/ejabberd/ && \

echo '>>>>>>>>>>>>>>>>>>>>>>>>> Inicializando o servidor ejabberd... '
ejabberdctl start && \

echo '>>>>>>>>>>>>>>>>>>>>>>>>> Aguardando o servidor subir'
sleep 10 && \

echo '>>>>>>>>>>>>>>>>>>>>>>>>> Criando o usuario administrador...'
ejabberdctl register admin aec 123123 && \

echo '>>>>>>>>>>>>>>>>>>>>>>>>> Parando o servidor o ejabberd... '
ejabberdctl stop && \

echo '>>>>>>>>>>>>>>>>>>>>>>>>> Aguardando o servidor subir'
sleep 5 && \

echo '>>>>>>>>>>>>>>>>>>>>>>>>> Subindo o servidor ejabberd'
ejabberdctl foreground