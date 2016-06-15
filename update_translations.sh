cd theme/translations/
pybabel extract -F babel.cfg -o messages.pot .. --omit-header
pybabel update -i messages.pot -d .
pybabel compile -d . -f
