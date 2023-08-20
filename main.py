# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 09:22:23 2023

@author: Danny Huang
"""
import os

from docx import Document

import translate as t


source_folder = r"C:\Python\Scripts\Translate\1_source"
output_folder = r"C:\Python\Scripts\Translate\2_output"
file_path = ""
file_out_path = ""



# Loop through source files

for file in os.listdir(source_folder):
    file_path = source_folder + "\\" + file
    print(file_path)
    # open the first file for translation
    document = Document(file_path)
    
    # deal with text inside paragraphs
    for p in document.paragraphs:
        if p.text.isdigit():    # make sure numbers are not translated into english
            pass
        else:
            p.text = t.translate_text(p.text)
        
    # deal with text inside tables
    for table in document.tables:
        for r in table.rows:
            for c in r.cells:
                for p in c.paragraphs:
                    if p.text.isdigit():
                        pass
                    else:
                        p.text = t.translate_text(p.text)
    
    file_out_path = os.path.join(output_folder, t.translate_text(file)) # ensure file name is also translated
    document.save(file_out_path)


print("Translation successfully completed.")