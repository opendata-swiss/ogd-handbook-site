convert_to_odt()
{
  cd $2/$3/handbook
  for f in $(find $1 -name '*.md'); do
    echo ${f##*/}
    pandoc --from markdown+raw_html --data-dir=$DIR $f -o $2/export/${f##*/}.odt
    #pandoc -f odt -t docx -o $2/export/${f##*/}.docx $2/export/${f##*/}.odt
  done;
}
# Going the other way:
# pandoc -s example30.docx –-no-wrap –-reference-links -t markdown -o example35.md

if ! hash pandoc 2>/dev/null; then
  echo "Please install pandoc"
else
  echo "------------------------------------------"
  echo "Generating OpenDocument (ODT) format files"
  echo "------------------------------------------"

  DIR="$( pwd )/pandoc"
  mkdir -p $2/export
  convert_to_odt $1 $2 'de'
  convert_to_odt $1 $2 'fr'
  convert_to_odt $1 $2 'en'
  convert_to_odt $1 $2 'it'

  echo "-------------------------------------"
fi
