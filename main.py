import chardet

from pathlib import Path

from chardet.universaldetector import UniversalDetector

detector = UniversalDetector()

import os
if __name__ == "__main__":
    working_directory = "."
    for (root,dirs,files) in os.walk(working_directory, topdown=True):
        # for name in dirs:
        #     print(os.path.join(root, name))
        for name in files:
            includes = ['.sql', '.cs', 'js', 'xml', 'css', 'csv', 'txt', 'config', 'cshtml','datasource','ps1','xaml']

            file_path = Path(os.path.join(root, name))

            if file_path.suffix in includes:
                detector.reset()
                for line in open(file_path, 'rb'):
                    detector.feed(line)
                    if detector.done: break
                detector.close()
                current_encoding = detector.result.get('encoding')

                # open file with current encoding
                with open(file_path, 'r', encoding=current_encoding) as f:
                    text = f.read()

                # save file
                # temp_file = file_path.joinpath(file_path.parent, file_path.stem+'_utf8'+file_path.suffix)
                with open(file_path, 'w', encoding='UTF-8') as f:
                    f.write(text)