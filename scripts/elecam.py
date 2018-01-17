import requests

data = {
    "cbocouncil": 10,
    "cboChoix": 1,
    "txtNic": "121212122121212"
}
response = requests.post("http://file.elecam.cm/fnat/index.php", data)\

print response, response.text

data = {
    "cboReg": 2,
    "cboDep": 7,
    "cboCom": 37,
    "cboCtre": 1570,
    "cbojour": 17,
    "cboMois": 9,
    "cboAnnee": 1914,
    "txtNameSearch": "Essomba Alain"
}
