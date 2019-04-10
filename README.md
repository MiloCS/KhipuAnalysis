# KhipuAnalysis 

This is a project that I pursued as part of an optional project for a class. 
It uses the python requests and BeautifulSoup libraries to parse a webpage to obtain 
a list of download links for files relevant to analysis, then populates a specified 
directory by downloading these files. It then uses the .xlsx files downloaded to 
generate a .txt file in the form requested by the professor.

## Using this code yourself

In order to use this code yourself, run:
```
git clone https://github.com/MiloCS/KhipuAnalysis.git 
```

In order to run the file downloader, run:
```
python collect_khipu_data.py <name of desired destination directory>
```

In order to run the table constructor, run:
```
python generate_data_table.py <name of target directory to read from>
```