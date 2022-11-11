import os
import logging
from pathlib import Path

from chardet.universaldetector import UniversalDetector

logName = os.path.splitext(os.path.basename(__file__))[0] + ".log"
logging.basicConfig(filename=logName, filemode='w',
                    format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', datefmt='%Y-%m-%d:%H:%M:%S', level=logging.INFO)

detector = UniversalDetector()

if __name__ == "__main__":
    working_directory = "E:/DELL_BACKUP/Backup_20221109/tfs/tfsPRD-Domino"
    for (root,dirs,files) in os.walk(working_directory, topdown=True):
        # for name in dirs:
        #     print(os.path.join(root, name))
        for name in files:
            includes = ['.sql', '.cs', 'js', 'xml', 'css', 'csv', 'txt', 'config', 'cshtml','datasource','ps1','xaml', 'java', 'bat','ini','jsp','md','xsd','aspx','ts','resx']

            file_path = Path(os.path.join(root, name))

            if file_path.suffix.lower() in includes:
                detector.reset()
                for line in open(file_path, 'rb'):
                    detector.feed(line)
                    if detector.done: break
                detector.close()
                current_encoding = detector.result.get('encoding')

                try:
                    # open file with current encoding
                    with open(file_path, 'r', encoding=current_encoding) as f:
                        text = f.read()

                    # save file
                    # temp_file = file_path.joinpath(file_path.parent, file_path.stem+'_utf8'+file_path.suffix)
                    with open(file_path, 'w', encoding='UTF-8') as f:
                        f.write(text)
                except UnicodeDecodeError as err:
                    logging.error(f"""UnicodeDecodeError: {err}""")