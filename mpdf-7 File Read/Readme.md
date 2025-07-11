## mPDF 7.0 Local File Read 

This is a modified script which helps in reading the local files using mpdf.

mPDF is a PHP library which generates PDF files from UTF-8 encoded HTML.

We can use annotaions to embed local files in to pdf file and then extract the contents of the embedded files.

This is a modifed script of the original exploit (https://www.exploit-db.com/exploits/50995), the original exploit was only generating the bas64 enc of the file we needed, but using this script we can send the payload and extract the contents of the embedded file within the pdf.
