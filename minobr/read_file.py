from docx2python import docx2python
import csv
import re
import os
import docx2txt


fieldsname = [
    "id", "file_name", "title_of_program", "provider", "text"
]
file_name = "data/Программы ПЦС 2020/1.Паспорт_программы_Ритейл_менеджмент__final_FGCjO8s.docx"
files = os.listdir("data/Программы ПЦС 2020/")
id = 0
with open("file.csv", "a", encoding="utf-8") as fw:
    writer = csv.DictWriter(fw, fieldnames=fieldsname)
    writer.writeheader()
    for file_name in files:
        try:
            doc = docx2python(f"data/Программы ПЦС 2020/{file_name}")
        except:
            print(file_name)
            continue
        id += 1
        number_of_hours = ""
        title_of_program = ""
        provider = ""
        text = ""
        for obj in doc.body:
            for included_obj in obj:
                if included_obj == []:
                    continue
                list_number = re.findall(r'\d[.]\d', included_obj[0][0])
                if list_number:
                    if list_number[0] == "1.1" and provider == "":
                        provider = included_obj[-1]
                    if list_number[0] == "2.1" and title_of_program == "":
                        title_of_program = included_obj[-1]
                #print(included_obj)
        try:
            row = {
                "id": id,
                "file_name": file_name,
                "title_of_program": title_of_program[0] if title_of_program != "" else title_of_program,
                "provider": provider[0],
                "text": docx2txt.process(f"data/Программы ПЦС 2020/{file_name}").replace("\n", " ")
            }
            writer.writerow(row)
        except:
            print(file_name)

