import json
from pprint import pprint

from flask import Flask,request
import subprocess

import config
app = Flask(__name__)


@app.route('/SigingService', methods=['GET', 'POST'])
def Sigining():
    if request.method == 'POST':
        #remote=request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        #return(remote)
        # get json invoice from erp
        invoiceToSign = request.get_json()
        with open('SourceDocumentJson.json', 'w', encoding='utf8' ) as fout:
            json.dump(invoiceToSign,fout,ensure_ascii=False)
        subprocess.run(["SubmitInvoices.bat"])

        with open('FullSignedDocument.json', 'r', encoding='utf8') as output:
           data=output.read()

    return format(data)

       # 3-
#


#return hello
if __name__ == '__main__':
      # app.config.from_pyfile('config.py')
      app.run(host="0.0.0.0",port="8080",debug="true",threaded=True)