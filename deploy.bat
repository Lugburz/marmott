@REM First, store .git which "npm run build" will remove eventually
xcopy dist\.git dist_git\.git /i /s
@RD /S /Q dist\.git


cd dist

git add -A
git commit -m "deploy"
git push git@github.com:Lugburz/marmott.git master:gh-pages
cd ..