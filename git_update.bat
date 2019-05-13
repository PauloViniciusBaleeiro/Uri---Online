echo Iniciando o processo de atualização do GIT
cd c:\
cd projetos

cd api_facilitame_auth
git checkout master
git fetch
echo Atualização 
cd ..

cd api_facilitame_backoffice
git checkout master
git fetch
cd ..

cd api_facilitame_cliente
git checkout master
git fetch
cd ..

cd banco_facilitame_postgre
git checkout master
git fetch
cd ..

cd frontend_facilitame_cadastro
git checkout master
git fetch
cd ..

cd frontend_facilitame_cliente
git checkout master
git fetch
cd ..

cd site_facilitame
git checkout master
git fetch
cd ..