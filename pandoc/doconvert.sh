convert_to_docx()
{
  for f in $(find . -name '*.odt'); do
    echo ${f%.*}
    unoconv -f docx -o "${f%.*}.docx" "${f%.*}.odt"
  done;
}

if ! hash unoconv 2>/dev/null; then
  echo "Please install unoconv"
elif ! hash libreoffice 2>/dev/null; then
  echo "Please install LibreOffice"
else
  echo "-------------------------------------"
  echo "Converting to Microsoft (DOCX) format"
  echo "-------------------------------------"
  cd $2/export/
  convert_to_docx

  echo "-------------------------------------"
  echo "All done!"
fi
