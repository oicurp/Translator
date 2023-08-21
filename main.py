# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 09:22:23 2023

@author: Danny Huang
"""
import os

from docx import Document

#import translate as t # 通用领域的翻译模块，根据需要选择。
import fieldtranslate as t # 医疗领域的翻译模块，建议分析方法选择本模块。


source_folder = r"C:\Python\Scripts\Translate\1_source"
output_folder = r"C:\Python\Scripts\Translate\2_output"
file_path = ""
file_out_path = ""
file_name_english = ""



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
        elif p.text.replace('.', '', 1).isdigit():
            pass
        #elif p.text.isalnum():
         #   pass
            
        else:
            p.text = t.translate_text(p.text)
        
    # deal with text inside tables
    for table in document.tables:
        for r in table.rows:
            for c in r.cells:
                for p in c.paragraphs:
                    if p.text.isdigit(): # need more control here, e.g., digit, float, or alphabet, do not translate.
                        pass
                    elif p.text.replace('.', '', 1).isdigit():
                        pass
                   # elif p.text.isalnum():
                    #    pass
                    else:
                        p.text = t.translate_text(p.text)
    
    file_name_english = t.translate_text(file)
    file_name_english = file_name_english.replace('. docx','.docx') # fixing file extension
    file_out_path = os.path.join(output_folder, file_name_english) # ensure file name is also translated
    document.save(file_out_path)


print("---------------------------------------")
print("Translation successfully completed.")