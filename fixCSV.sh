#!/usr/bin/bash

newFile="BrowserSurveyEdited.csv"

sed 's/"Does your choice of browser make a significant difference to your online life?","Which browser(s) do you mainly use?","Why?","Which of these best suits your thoughts on internet privacy?","",""/"Significance","Browsers","Why","Privacy"/g' BrowserSurvey.csv > $newFile
sed 's/Microsoft Edge/Edge/g' $newFile > $newFile.tmp
sed 's/Googal Kröm/Chrome/g' $newFile.tmp > $newFile
sed 's/Krömiyum/Chromium/g' $newFile > $newFile.tmp
sed 's/ophra jee ecks i used back then/Opera GX/g' $newFile.tmp > $newFile
sed 's|Moz://a Fayarfax|Firefox|g' $newFile > $newFile.tmp
sed 's/BRAVE BROWSER/Brave/g' $newFile.tmp > $newFile
sed 's/Opera GX /Opera GX/g' $newFile > $newFile.tmp
sed 's/That one with the orange lion/Brave/g' $newFile.tmp > $newFile
sed 's/Maykrasaft Ej/Edge/g' $newFile > $newFile.tmp
sed 's/Maykrasaft Yinternet Explorar/IE/g' $newFile.tmp > $newFile
sed 's/Aapraa/Opera/g' $newFile > $newFile.tmp
sed 's/Veevaaldee/Vivaldi/g' $newFile.tmp > $newFile
sed 's/सेब //g' $newFile > $newFile.tmp
sed 's/opirra gxx/Opera GX/g' $newFile.tmp > $newFile
sed 's/Opera gx/Opera GX/g' $newFile > $newFile.tmp
sed 's/i use opera why does everyone hate it :(/Opera GX/g' $newFile.tmp > $newFile
sed 's/brave/Brave/g' $newFile > $newFile.tmp
sed 's/Opara JKS/Opera GX/g' $newFile.tmp > $newFile
sed 's/its a Brave Browser/Brave/g' $newFile > $newFile.tmp
sed 's/Crafter edge lol/Edge/g' $newFile.tmp > $newFile
sed 's/opera gx/Opera GX/g' $newFile > $newFile.tmp

head -n 1 BrowserSurvey.csv > BrowserSurveySpam.csv
rm $newFile

while IFS= read -r line ; do
	if echo $line | grep --quiet -iE 'funny|dad|browser |shut|bee|bing|joe|CC Cleaner|gay|mom|shit|idk|sois|nut' ; then
		echo $line >> BrowserSurveySpam.csv
	else
		echo $line >> $newFile
	fi
done < $newFile.tmp

rm $newFile.tmp
