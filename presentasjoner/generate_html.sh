mkdir -p html/Del2
jupyter nbconvert --to html *.ipynb Del2/*.ipynb
mv *.html html
mv Del2/*.html html/Del2
