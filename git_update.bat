echo Iniciando o processo de atualização do GIT
cd c:\
cd projetos

echo Atualizando API Auth
cd api_facilitame_auth
git checkout master
git pull
cd ..
echo Atualização concluída

echo Atualizando API BackOffice
cd api_facilitame_backoffice
git checkout master
git pull
cd ..
echo Atualização concluída

echo Atualizando API Cliente
cd api_facilitame_cliente
git checkout master
git pull
cd ..
echo Atualização concluída

echo Atualizando Postgre
cd banco_facilitame_postgre
git checkout master
git fetch
cd ..
echo Atualização concluída

echo Atualizando Frontend Cadastro
cd frontend_facilitame_cadastro
git checkout master
git fetch
cd ..
echo Atualização concluída

echo Atualizando Frontend Cliente
cd frontend_facilitame_cliente
git checkout master
git fetch
cd ..
echo Atualização concluída

echo Atualizando Site
cd site_facilitame
git checkout master
git fetch
cd ..
echo Atualização concluída
pause