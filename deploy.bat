@REM First, store .git which "npm run build" will remove eventually
xcopy dist\.git dist_git\.git /i /s

@REM Build as usual
nmp run build

@REM get back .git folder
xcopy dist_git\.git dist\.git /i /s

cd dist

git add -A
git commit -m "deploy"
git push -f git@github.com:Lugburz/marmott.git master:gh-pages
cd ..