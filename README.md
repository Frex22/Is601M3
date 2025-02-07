# Is601M3
for improved calculator


#issues faced in pushing git repo and solutions

aakash32@Aakash:~/IS601/Is601M3$ git push origin main
error: src refspec main does not match any
error: failed to push some refs to 'github.com:Frex22/Is601M3.git'

the problem is Igot two branches main and master both I might have made some mistakes while git init or not set main as my default branch name in local the solution was

git branch -m master main  # Rename local master to main
git fetch origin  # Fetch latest remote changes.

git branch --set-upstream-to=origin/main main  # Set upstream to track main
git push -u origin main  # Push main branch to GitHub


aakash32@Aakash:~/IS601/Is601M3$ git push -u origin main
To github.com:Frex22/Is601M3.git
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'github.com:Frex22/Is601M3.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. If you want to integrate the remote changes,
hint: use 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

Solution

git pull origin main --rebase  # Fetch and reapply your commits on top
git push origin main  # Push after successful rebase

set testing tools
pip install pytest pylint-pytest
pip install pytest-cov
pip freeze > requirements.txt
