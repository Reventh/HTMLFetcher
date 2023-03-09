from bs4 import BeautifulSoup
import glob
import pandas as pd
import itertools as it
from itertools import cycle
with open("a_file_V3.txt", "w") as textfile:
    for filename in glob.iglob('*.html'):
        textfile.write(f"{filename}:\n")

        with open(filename) as f:
            soup = BeautifulSoup(f)

            head_title = [head for head in soup.select('.header') ]
            for head in head_title:
             textfile.write(f"{head.text}\n")
            
            head_title_copy = soup.select('.header-copy-editable')
            for head_copy in head_title_copy:
             textfile.write(f"{head_copy.text}\n")

            cta_copy = soup.select('.button-text-editable')
            for cta in cta_copy:
             textfile.write(f"{cta.text}\n")

            pod_copies = [copy for copy in soup.find_all('td', {'style':" font-family:adobe-clean, Arial, Helvetica, sans-serif; "}) ]
            for pod_copy in pod_copies:
                textfile.write(f"{pod_copy.text}\n")

            mbl_images= [img['src'] for img in soup.find_all('img', class_="mobile-image")]
            for mbl_image in mbl_images:
                textfile.write(f"{mbl_image}\n")

            links_with_text = [a['href'] for a in soup.find_all('a', href=True) if a.text]
            for link in links_with_text:
                textfile.write(f"{link}\n")