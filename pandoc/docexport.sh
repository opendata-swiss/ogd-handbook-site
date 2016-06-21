echo "Converting to ODT & DOCX formats"
DIR="$( pwd )/pandoc"
mkdir -p $2/export
cd $2/de/handbook
for f in $(find $1 -name '*.md'); do
  echo ${f##*/}
  pandoc --data-dir=$DIR $f -o $2/export/${f##*/}.odt
  pandoc -f odt -t docx -o $2/export/${f##*/}.docx $2/export/${f##*/}.odt
done;
