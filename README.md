# ETax-Signature
## Steps to install Etax-Signature on Windows Server
1. Install [Python](https://www.python.org/)
2. Install [Flask](https://flask.palletsprojects.com/en/2.0.x/)
        $ pip install flask
3. Chnage this file [SubmitInvoices.bat](https://github.com/FrontLineEG/ETax-Signature/blob/main/SubmitInvoices.bat) to fit yours.
4. Run this file [sub-serv.bat](https://github.com/FrontLineEG/ETax-Signature/blob/main/SubmitInvoices.bat) via cmd and make sure routers fit your structure.
5. Then it should working right. if you find an error about do not found python <br />so please check this file [pyvenv.cfg](https://github.com/FrontLineEG/ETax-Signature/blob/main/venv/pyvenv.cfg) then change home and version to fit yours
6. If you find this below error. so u have to change the port or make it available via network man.
7.      [WinError 10013] An attempt was made to access a socket in a way forbidden by its access permissions
- USB Names be "Egypt Trust Sealing CA" or "MCDR 2019"
- Get Python Path Command $ python -c "import sys; print(sys.executable)"
