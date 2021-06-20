from docx2python import docx2python
import docx2txt
import os
import csv

docxFilename = "data/Программы вузов для хакатона/2021.05.14. ВГТУ/Автом-ное проект-ие киберфизических систем, Системная инженерия/2019-2020_Ucheb_plan_09_03_01_A_CPh_O_NOR_FEVT_SAPR_2019_plx_Базы данных (2).docx"
doc = docx2python(f"data/Программы вузов для хакатона/2021.05.14. ВГТУ/Автом-ное проект-ие киберфизических систем, Системная инженерия/2019-2020_Ucheb_plan_09_03_01_A_CPh_O_NOR_FEVT_SAPR_2019_plx_Базы данных (2).docx")
MY_TEXT = docx2txt.process(docxFilename).replace("\n", " ")
fieldsname = [
    "id", "file_name", "direction", "title_of_program", "provider", "text"
]
universities = os.listdir("data/Программы вузов для хакатона")
id = 0
cnt = 0
with open("universities.csv", "a", encoding="utf-8") as fw:
    writer = csv.DictWriter(fw, fieldnames=fieldsname)
    writer.writeheader()
    for university in universities:
        provider = university.split()[-1]
        directions = os.listdir(f"data/Программы вузов для хакатона/{university}")
        for direction in directions:
            direction_name = direction
            try:
                files = os.listdir(f"data/Программы вузов для хакатона/{university}/{direction}")
            except NotADirectoryError:
                continue
            for file in files:
                id += 1
                if file.split(".")[-1] in ["docx", "doc"]:
                    try:
                        doc = docx2python(f"data/Программы вузов для хакатона/{university}/{direction}/{file}")
                    except KeyError:
                        continue
                    except:
                        continue
                    title_of_program = ""
                    for obj in doc.body:
                        try:
                            title_of_program = doc.body[0][14][0]
                        except IndexError:
                            continue
                        #print(doc.body)
                    docxFilename = f"data/Программы вузов для хакатона/{university}/{direction}/{file}"
                    try:
                        text = docx2txt.process(docxFilename).replace("\n", " ")
                    except KeyError:
                        continue
                    row = {
                        "id": id,
                        "file_name": file,
                        "direction": direction_name,
                        "title_of_program": title_of_program,
                        "provider": provider,
                        "text": text
                    }
                    writer.writerow(row)
                    cnt += 1
                    print(cnt)