if hash pandoc 2>/dev/null; then
  echo "Generating OpenDocument (ODT) format files"
  DIR="$( pwd )/pandoc"
  mkdir -p $2/export
  cd $2/de/handbook
  for f in $(find $1 -name '*.md'); do
    echo ${f##*/}
    pandoc --data-dir=$DIR $f -o $2/export/${f##*/}.odt
    #pandoc -f odt -t docx -o $2/export/${f##*/}.docx $2/export/${f##*/}.odt
  done;
fi

if hash libreoffice 2>/dev/null; then
  echo "Converting to DOCX format with LibreOffice"
  cd $2/export/
  libreoffice --headless --convert-to docx *.odt
fi
