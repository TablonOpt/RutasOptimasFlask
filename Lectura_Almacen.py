# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 14:29:56 2022

@author: lumen
"""

import pandas as pd
def Lectura_geometriaAlmacen():
    """
    geometriaAlmacen={

        "IdentificadorAlmacen": "0001",

        "Dimensiones":{
            "y_inferior":"0",
            "y_superior":"76"

        },

        "780": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "20",
            "ID_Ubic": "7930",
            "SKU_PRODUCTO": "780",
            "Inventario_Existencia": "10000"
        },
        "60457": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "37",
            "ID_Ubic": "2255",
            "SKU_PRODUCTO": "60457",
            "Inventario_Existencia": "2"
        },
        "60061": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "26",
            "ID_Ubic": "2200",
            "SKU_PRODUCTO": "60061",
            "Inventario_Existencia": "35"
        },
        "60354": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "26",
            "ID_Ubic": "2200",
            "SKU_PRODUCTO": "60354",
            "Inventario_Existencia": "70"
        },
        "60175": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "27",
            "ID_Ubic": "2205",
            "SKU_PRODUCTO": "60175",
            "Inventario_Existencia": "140"
        },
        "60388": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "27",
            "ID_Ubic": "2205",
            "SKU_PRODUCTO": "60388",
            "Inventario_Existencia": "10"
        },
        "75525": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "28",
            "ID_Ubic": "2210",
            "SKU_PRODUCTO": "75525",
            "Inventario_Existencia": "303"
        },
        "75542": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "28",
            "ID_Ubic": "2210",
            "SKU_PRODUCTO": "75542",
            "Inventario_Existencia": "59"
        },
        "72918": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "29",
            "ID_Ubic": "2215",
            "SKU_PRODUCTO": "72918",
            "Inventario_Existencia": "2"
        },
        "75549": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "29",
            "ID_Ubic": "2215",
            "SKU_PRODUCTO": "75549",
            "Inventario_Existencia": "9"
        },
        "75041": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "30",
            "ID_Ubic": "2220",
            "SKU_PRODUCTO": "75041",
            "Inventario_Existencia": "544"
        },
        "75558": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "31",
            "ID_Ubic": "2225",
            "SKU_PRODUCTO": "75558",
            "Inventario_Existencia": "673"
        },
        "60341": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "32",
            "ID_Ubic": "2230",
            "SKU_PRODUCTO": "60341",
            "Inventario_Existencia": "750"
        },
        "60410": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "32",
            "ID_Ubic": "2230",
            "SKU_PRODUCTO": "60410",
            "Inventario_Existencia": "1000"
        },
        "75026": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "33",
            "ID_Ubic": "2235",
            "SKU_PRODUCTO": "75026",
            "Inventario_Existencia": "321"
        },
        "73728": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "34",
            "ID_Ubic": "2240",
            "SKU_PRODUCTO": "73728",
            "Inventario_Existencia": "1050"
        },
        "60416": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "35",
            "ID_Ubic": "2245",
            "SKU_PRODUCTO": "60416",
            "Inventario_Existencia": "1000"
        },
        "73712": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "36",
            "ID_Ubic": "2250",
            "SKU_PRODUCTO": "73712",
            "Inventario_Existencia": "100"
        },
        "73716": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "36",
            "ID_Ubic": "2250",
            "SKU_PRODUCTO": "73716",
            "Inventario_Existencia": "550"
        },
        "60182": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "38",
            "ID_Ubic": "2260",
            "SKU_PRODUCTO": "60182",
            "Inventario_Existencia": "70"
        },
        "75001": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "39",
            "ID_Ubic": "2265",
            "SKU_PRODUCTO": "75001",
            "Inventario_Existencia": "546"
        },
        "73720": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "40",
            "ID_Ubic": "2270",
            "SKU_PRODUCTO": "73720",
            "Inventario_Existencia": "1770"
        },
        "29475": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "41",
            "ID_Ubic": "2275",
            "SKU_PRODUCTO": "29475",
            "Inventario_Existencia": "268"
        },
        "60046": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "42",
            "ID_Ubic": "2280",
            "SKU_PRODUCTO": "60046",
            "Inventario_Existencia": "15"
        },
        "60163": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "42",
            "ID_Ubic": "2280",
            "SKU_PRODUCTO": "60163",
            "Inventario_Existencia": "10"
        },
        "60211": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "42",
            "ID_Ubic": "2280",
            "SKU_PRODUCTO": "60211",
            "Inventario_Existencia": "30"
        },
        "73711": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "43",
            "ID_Ubic": "2285",
            "SKU_PRODUCTO": "73711",
            "Inventario_Existencia": "500"
        },
        "72951": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "3",
            "ID_Ubic": "16485",
            "SKU_PRODUCTO": "72951",
            "Inventario_Existencia": "1490"
        },
        "60002": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "45",
            "ID_Ubic": "2295",
            "SKU_PRODUCTO": "60002",
            "Inventario_Existencia": "3750"
        },
        "60351": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "46",
            "ID_Ubic": "2300",
            "SKU_PRODUCTO": "60351",
            "Inventario_Existencia": "1000"
        },
        "60412": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "46",
            "ID_Ubic": "2300",
            "SKU_PRODUCTO": "60412",
            "Inventario_Existencia": "4500"
        },
        "60353": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "47",
            "ID_Ubic": "2305",
            "SKU_PRODUCTO": "60353",
            "Inventario_Existencia": "105"
        },
        "72964": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "48",
            "ID_Ubic": "2310",
            "SKU_PRODUCTO": "72964",
            "Inventario_Existencia": "500"
        },
        "75034": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "5",
            "ID_Ubic": "30137",
            "SKU_PRODUCTO": "75034",
            "Inventario_Existencia": "6"
        },
        "75513": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "48",
            "ID_Ubic": "2310",
            "SKU_PRODUCTO": "75513",
            "Inventario_Existencia": "36"
        },
        "60010": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "1",
            "ID_Ubic": "3515",
            "SKU_PRODUCTO": "60010",
            "Inventario_Existencia": "11000"
        },
        "60008": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "2",
            "ID_Ubic": "3520",
            "SKU_PRODUCTO": "60008",
            "Inventario_Existencia": "7500"
        },
        "60006": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "3",
            "ID_Ubic": "3525",
            "SKU_PRODUCTO": "60006",
            "Inventario_Existencia": "6500"
        },
        "60054": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "4",
            "ID_Ubic": "3530",
            "SKU_PRODUCTO": "60054",
            "Inventario_Existencia": "110"
        },
        "60001": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "5",
            "ID_Ubic": "3535",
            "SKU_PRODUCTO": "60001",
            "Inventario_Existencia": "3250"
        },
        "60036": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "6",
            "ID_Ubic": "3540",
            "SKU_PRODUCTO": "60036",
            "Inventario_Existencia": "5250"
        },
        "60007": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "7",
            "ID_Ubic": "3545",
            "SKU_PRODUCTO": "60007",
            "Inventario_Existencia": "4500"
        },
        "60009": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "8",
            "ID_Ubic": "3550",
            "SKU_PRODUCTO": "60009",
            "Inventario_Existencia": "3000"
        },
        "60016": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "9",
            "ID_Ubic": "3555",
            "SKU_PRODUCTO": "60016",
            "Inventario_Existencia": "205"
        },
        "60035": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "10",
            "ID_Ubic": "3560",
            "SKU_PRODUCTO": "60035",
            "Inventario_Existencia": "210"
        },
        "60060": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "11",
            "ID_Ubic": "3565",
            "SKU_PRODUCTO": "60060",
            "Inventario_Existencia": "260"
        },
        "60027": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "12",
            "ID_Ubic": "3570",
            "SKU_PRODUCTO": "60027",
            "Inventario_Existencia": "65"
        },
        "60019": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "13",
            "ID_Ubic": "3575",
            "SKU_PRODUCTO": "60019",
            "Inventario_Existencia": "25"
        },
        "60021": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "14",
            "ID_Ubic": "3580",
            "SKU_PRODUCTO": "60021",
            "Inventario_Existencia": "320"
        },
        "60018": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "15",
            "ID_Ubic": "3585",
            "SKU_PRODUCTO": "60018",
            "Inventario_Existencia": "285"
        },
        "60029": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "16",
            "ID_Ubic": "3590",
            "SKU_PRODUCTO": "60029",
            "Inventario_Existencia": "165"
        },
        "60025": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "17",
            "ID_Ubic": "3595",
            "SKU_PRODUCTO": "60025",
            "Inventario_Existencia": "70"
        },
        "60050": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "18",
            "ID_Ubic": "3600",
            "SKU_PRODUCTO": "60050",
            "Inventario_Existencia": "190"
        },
        "60023": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "19",
            "ID_Ubic": "3605",
            "SKU_PRODUCTO": "60023",
            "Inventario_Existencia": "230"
        },
        "60048": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "21",
            "ID_Ubic": "3615",
            "SKU_PRODUCTO": "60048",
            "Inventario_Existencia": "25"
        },
        "60047": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "22",
            "ID_Ubic": "3620",
            "SKU_PRODUCTO": "60047",
            "Inventario_Existencia": "165"
        },
        "60056": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "23",
            "ID_Ubic": "3625",
            "SKU_PRODUCTO": "60056",
            "Inventario_Existencia": "40"
        },
        "60057": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "24",
            "ID_Ubic": "3630",
            "SKU_PRODUCTO": "60057",
            "Inventario_Existencia": "10"
        },
        "14104": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "28",
            "ID_Ubic": "3650",
            "SKU_PRODUCTO": "14104",
            "Inventario_Existencia": "12000"
        },
        "9658": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "29",
            "ID_Ubic": "3655",
            "SKU_PRODUCTO": "9658",
            "Inventario_Existencia": "14300"
        },
        "72874": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "30",
            "ID_Ubic": "3660",
            "SKU_PRODUCTO": "72874",
            "Inventario_Existencia": "2760"
        },
        "70597": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "32",
            "ID_Ubic": "3670",
            "SKU_PRODUCTO": "70597",
            "Inventario_Existencia": "15000"
        },
        "4076": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "33",
            "ID_Ubic": "3675",
            "SKU_PRODUCTO": "4076",
            "Inventario_Existencia": "3250"
        },
        "203": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "34",
            "ID_Ubic": "3680",
            "SKU_PRODUCTO": "203",
            "Inventario_Existencia": "1500"
        },
        "13126": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "37",
            "ID_Ubic": "3695",
            "SKU_PRODUCTO": "13126",
            "Inventario_Existencia": "200"
        },
        "10813": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "38",
            "ID_Ubic": "3700",
            "SKU_PRODUCTO": "10813",
            "Inventario_Existencia": "27500"
        },
        "5083": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "39",
            "ID_Ubic": "3705",
            "SKU_PRODUCTO": "5083",
            "Inventario_Existencia": "12800"
        },
        "1557": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "40",
            "ID_Ubic": "3710",
            "SKU_PRODUCTO": "1557",
            "Inventario_Existencia": "550"
        },
        "4118": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "41",
            "ID_Ubic": "3715",
            "SKU_PRODUCTO": "4118",
            "Inventario_Existencia": "5600"
        },
        "18447": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "43",
            "ID_Ubic": "3725",
            "SKU_PRODUCTO": "18447",
            "Inventario_Existencia": "560"
        },
        "73517": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "44",
            "ID_Ubic": "3730",
            "SKU_PRODUCTO": "73517",
            "Inventario_Existencia": "2000"
        },
        "10812": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "46",
            "ID_Ubic": "3740",
            "SKU_PRODUCTO": "10812",
            "Inventario_Existencia": "13000"
        },
        "4350": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "47",
            "ID_Ubic": "3745",
            "SKU_PRODUCTO": "4350",
            "Inventario_Existencia": "5900"
        },
        "13128": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "48",
            "ID_Ubic": "3750",
            "SKU_PRODUCTO": "13128",
            "Inventario_Existencia": "600"
        },
        "70598": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "1",
            "ID_Ubic": "4955",
            "SKU_PRODUCTO": "70598",
            "Inventario_Existencia": "24500"
        },
        "14050": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "4",
            "ID_Ubic": "4970",
            "SKU_PRODUCTO": "14050",
            "Inventario_Existencia": "6850"
        },
        "21609": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "6",
            "ID_Ubic": "4980",
            "SKU_PRODUCTO": "21609",
            "Inventario_Existencia": "1600"
        },
        "3924": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "7",
            "ID_Ubic": "4985",
            "SKU_PRODUCTO": "3924",
            "Inventario_Existencia": "16000"
        },
        "71751": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "8",
            "ID_Ubic": "4990",
            "SKU_PRODUCTO": "71751",
            "Inventario_Existencia": "5500"
        },
        "72593": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "10",
            "ID_Ubic": "5000",
            "SKU_PRODUCTO": "72593",
            "Inventario_Existencia": "27475"
        },
        "10809": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "11",
            "ID_Ubic": "5005",
            "SKU_PRODUCTO": "10809",
            "Inventario_Existencia": "7500"
        },
        "4538": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "12",
            "ID_Ubic": "5010",
            "SKU_PRODUCTO": "4538",
            "Inventario_Existencia": "2700"
        },
        "14475": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "13",
            "ID_Ubic": "5015",
            "SKU_PRODUCTO": "14475",
            "Inventario_Existencia": "5050"
        },
        "3823": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "14",
            "ID_Ubic": "5020",
            "SKU_PRODUCTO": "3823",
            "Inventario_Existencia": "4250"
        },
        "5571": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "15",
            "ID_Ubic": "5025",
            "SKU_PRODUCTO": "5571",
            "Inventario_Existencia": "550"
        },
        "72870": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "16",
            "ID_Ubic": "5030",
            "SKU_PRODUCTO": "72870",
            "Inventario_Existencia": "8136"
        },
        "6444": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "19",
            "ID_Ubic": "5045",
            "SKU_PRODUCTO": "6444",
            "Inventario_Existencia": "6800"
        },
        "4523": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "20",
            "ID_Ubic": "5050",
            "SKU_PRODUCTO": "4523",
            "Inventario_Existencia": "1650"
        },
        "72592": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "21",
            "ID_Ubic": "5055",
            "SKU_PRODUCTO": "72592",
            "Inventario_Existencia": "39750"
        },
        "70151": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "22",
            "ID_Ubic": "5060",
            "SKU_PRODUCTO": "70151",
            "Inventario_Existencia": "475"
        },
        "9660": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "23",
            "ID_Ubic": "5065",
            "SKU_PRODUCTO": "9660",
            "Inventario_Existencia": "31700"
        },
        "72873": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "24",
            "ID_Ubic": "5070",
            "SKU_PRODUCTO": "72873",
            "Inventario_Existencia": "4026"
        },
        "18527": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "27",
            "ID_Ubic": "5085",
            "SKU_PRODUCTO": "18527",
            "Inventario_Existencia": "6000"
        },
        "3714": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "28",
            "ID_Ubic": "5090",
            "SKU_PRODUCTO": "3714",
            "Inventario_Existencia": "1650"
        },
        "6092": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "29",
            "ID_Ubic": "5095",
            "SKU_PRODUCTO": "6092",
            "Inventario_Existencia": "18800"
        },
        "10805": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "30",
            "ID_Ubic": "5100",
            "SKU_PRODUCTO": "10805",
            "Inventario_Existencia": "2500"
        },
        "473": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "31",
            "ID_Ubic": "5105",
            "SKU_PRODUCTO": "473",
            "Inventario_Existencia": "950"
        },
        "72590": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "33",
            "ID_Ubic": "5115",
            "SKU_PRODUCTO": "72590",
            "Inventario_Existencia": "21475"
        },
        "2030": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "34",
            "ID_Ubic": "5120",
            "SKU_PRODUCTO": "2030",
            "Inventario_Existencia": "6750"
        },
        "1303": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "35",
            "ID_Ubic": "5125",
            "SKU_PRODUCTO": "1303",
            "Inventario_Existencia": "5000"
        },
        "3451": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "38",
            "ID_Ubic": "5140",
            "SKU_PRODUCTO": "3451",
            "Inventario_Existencia": "4700"
        },
        "9659": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "39",
            "ID_Ubic": "5145",
            "SKU_PRODUCTO": "9659",
            "Inventario_Existencia": "12800"
        },
        "26255": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "40",
            "ID_Ubic": "5150",
            "SKU_PRODUCTO": "26255",
            "Inventario_Existencia": "40"
        },
        "1911": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "41",
            "ID_Ubic": "5155",
            "SKU_PRODUCTO": "1911",
            "Inventario_Existencia": "1750"
        },
        "1920": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "42",
            "ID_Ubic": "5160",
            "SKU_PRODUCTO": "1920",
            "Inventario_Existencia": "160"
        },
        "29985": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "43",
            "ID_Ubic": "5165",
            "SKU_PRODUCTO": "29985",
            "Inventario_Existencia": "220"
        },
        "2383": {
            "Nombre_Pasillo": "C1",
            "X": "8",
            "Y": "45",
            "ID_Ubic": "5175",
            "SKU_PRODUCTO": "2383",
            "Inventario_Existencia": "44"
        },
        "00055K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "1",
            "ID_Ubic": "6395",
            "SKU_PRODUCTO": "00055K",
            "Inventario_Existencia": "17000"
        },
        "00074K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "2",
            "ID_Ubic": "6400",
            "SKU_PRODUCTO": "00074K",
            "Inventario_Existencia": "7000"
        },
        "00092K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "3",
            "ID_Ubic": "6405",
            "SKU_PRODUCTO": "00092K",
            "Inventario_Existencia": "2500"
        },
        "00059K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "4",
            "ID_Ubic": "6410",
            "SKU_PRODUCTO": "00059K",
            "Inventario_Existencia": "5250"
        },
        "00075K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "5",
            "ID_Ubic": "6415",
            "SKU_PRODUCTO": "00075K",
            "Inventario_Existencia": "13500"
        },
        "00780K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "6",
            "ID_Ubic": "6420",
            "SKU_PRODUCTO": "00780K",
            "Inventario_Existencia": "8000"
        },
        "00052K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "8",
            "ID_Ubic": "6430",
            "SKU_PRODUCTO": "00052K",
            "Inventario_Existencia": "10500"
        },
        "00778K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "9",
            "ID_Ubic": "6435",
            "SKU_PRODUCTO": "00778K",
            "Inventario_Existencia": "8500"
        },
        "08714K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "10",
            "ID_Ubic": "6440",
            "SKU_PRODUCTO": "08714K",
            "Inventario_Existencia": "3250"
        },
        "00051K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "12",
            "ID_Ubic": "6450",
            "SKU_PRODUCTO": "00051K",
            "Inventario_Existencia": "9500"
        },
        "00040K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "13",
            "ID_Ubic": "6455",
            "SKU_PRODUCTO": "00040K",
            "Inventario_Existencia": "15500"
        },
        "00053K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "14",
            "ID_Ubic": "6460",
            "SKU_PRODUCTO": "00053K",
            "Inventario_Existencia": "4000"
        },
        "00054K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "15",
            "ID_Ubic": "6465",
            "SKU_PRODUCTO": "00054K",
            "Inventario_Existencia": "21500"
        },
        "00073K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "16",
            "ID_Ubic": "6470",
            "SKU_PRODUCTO": "00073K",
            "Inventario_Existencia": "12500"
        },
        "00044K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "17",
            "ID_Ubic": "6475",
            "SKU_PRODUCTO": "00044K",
            "Inventario_Existencia": "20500"
        },
        "00038K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "18",
            "ID_Ubic": "6480",
            "SKU_PRODUCTO": "00038K",
            "Inventario_Existencia": "15000"
        },
        "00047K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "19",
            "ID_Ubic": "6485",
            "SKU_PRODUCTO": "00047K",
            "Inventario_Existencia": "18000"
        },
        "00046K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "20",
            "ID_Ubic": "6490",
            "SKU_PRODUCTO": "00046K",
            "Inventario_Existencia": "3000"
        },
        "00039K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "21",
            "ID_Ubic": "6495",
            "SKU_PRODUCTO": "00039K",
            "Inventario_Existencia": "7000"
        },
        "00041K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "22",
            "ID_Ubic": "6500",
            "SKU_PRODUCTO": "00041K",
            "Inventario_Existencia": "15000"
        },
        "00060K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "23",
            "ID_Ubic": "6505",
            "SKU_PRODUCTO": "00060K",
            "Inventario_Existencia": "5500"
        },
        "00042K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "24",
            "ID_Ubic": "6510",
            "SKU_PRODUCTO": "00042K",
            "Inventario_Existencia": "2500"
        },
        "00058K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "27",
            "ID_Ubic": "6525",
            "SKU_PRODUCTO": "00058K",
            "Inventario_Existencia": "5250"
        },
        "00078K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "28",
            "ID_Ubic": "6530",
            "SKU_PRODUCTO": "00078K",
            "Inventario_Existencia": "3500"
        },
        "02332K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "29",
            "ID_Ubic": "6535",
            "SKU_PRODUCTO": "02332K",
            "Inventario_Existencia": "2000"
        },
        "00049K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "30",
            "ID_Ubic": "6540",
            "SKU_PRODUCTO": "00049K",
            "Inventario_Existencia": "9250"
        },
        "00048K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "31",
            "ID_Ubic": "6545",
            "SKU_PRODUCTO": "00048K",
            "Inventario_Existencia": "7750"
        },
        "05525K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "32",
            "ID_Ubic": "6550",
            "SKU_PRODUCTO": "05525K",
            "Inventario_Existencia": "3250"
        },
        "00037K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "33",
            "ID_Ubic": "6555",
            "SKU_PRODUCTO": "00037K",
            "Inventario_Existencia": "46500"
        },
        "00091K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "34",
            "ID_Ubic": "6560",
            "SKU_PRODUCTO": "00091K",
            "Inventario_Existencia": "7250"
        },
        "00086K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "35",
            "ID_Ubic": "6565",
            "SKU_PRODUCTO": "00086K",
            "Inventario_Existencia": "4000"
        },
        "00090K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "36",
            "ID_Ubic": "6570",
            "SKU_PRODUCTO": "00090K",
            "Inventario_Existencia": "9500"
        },
        "00084K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "37",
            "ID_Ubic": "6575",
            "SKU_PRODUCTO": "00084K",
            "Inventario_Existencia": "2500"
        },
        "02333K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "38",
            "ID_Ubic": "6580",
            "SKU_PRODUCTO": "02333K",
            "Inventario_Existencia": "250"
        },
        "00057K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "39",
            "ID_Ubic": "6585",
            "SKU_PRODUCTO": "00057K",
            "Inventario_Existencia": "2250"
        },
        "00043K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "40",
            "ID_Ubic": "6590",
            "SKU_PRODUCTO": "00043K",
            "Inventario_Existencia": "8000"
        },
        "10965K": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "41",
            "ID_Ubic": "6595",
            "SKU_PRODUCTO": "10965K",
            "Inventario_Existencia": "3250"
        },
        "2346": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "42",
            "ID_Ubic": "6600",
            "SKU_PRODUCTO": "2346",
            "Inventario_Existencia": "36"
        },
        "155": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "43",
            "ID_Ubic": "6605",
            "SKU_PRODUCTO": "155",
            "Inventario_Existencia": "47"
        },
        "1214": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "44",
            "ID_Ubic": "6610",
            "SKU_PRODUCTO": "1214",
            "Inventario_Existencia": "35"
        },
        "2390": {
            "Nombre_Pasillo": "C2",
            "X": "12",
            "Y": "46",
            "ID_Ubic": "6620",
            "SKU_PRODUCTO": "2390",
            "Inventario_Existencia": "12"
        },
        "4609": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "28",
            "ID_Ubic": "18050",
            "SKU_PRODUCTO": "4609",
            "Inventario_Existencia": "12"
        },
        "37": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "1",
            "ID_Ubic": "7835",
            "SKU_PRODUCTO": "37",
            "Inventario_Existencia": "15500"
        },
        "55": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "2",
            "ID_Ubic": "7840",
            "SKU_PRODUCTO": "55",
            "Inventario_Existencia": "20000"
        },
        "73": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "3",
            "ID_Ubic": "7845",
            "SKU_PRODUCTO": "73",
            "Inventario_Existencia": "12500"
        },
        "53": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "4",
            "ID_Ubic": "7850",
            "SKU_PRODUCTO": "53",
            "Inventario_Existencia": "28000"
        },
        "44": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "5",
            "ID_Ubic": "7855",
            "SKU_PRODUCTO": "44",
            "Inventario_Existencia": "43500"
        },
        "52": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "6",
            "ID_Ubic": "7860",
            "SKU_PRODUCTO": "52",
            "Inventario_Existencia": "13000"
        },
        "2332": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "7",
            "ID_Ubic": "7865",
            "SKU_PRODUCTO": "2332",
            "Inventario_Existencia": "5000"
        },
        "75": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "8",
            "ID_Ubic": "7870",
            "SKU_PRODUCTO": "75",
            "Inventario_Existencia": "7000"
        },
        "74": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "9",
            "ID_Ubic": "7875",
            "SKU_PRODUCTO": "74",
            "Inventario_Existencia": "15500"
        },
        "2331": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "10",
            "ID_Ubic": "7880",
            "SKU_PRODUCTO": "2331",
            "Inventario_Existencia": "22000"
        },
        "5525": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "11",
            "ID_Ubic": "7885",
            "SKU_PRODUCTO": "5525",
            "Inventario_Existencia": "6000"
        },
        "47": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "12",
            "ID_Ubic": "7890",
            "SKU_PRODUCTO": "47",
            "Inventario_Existencia": "20000"
        },
        "49": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "13",
            "ID_Ubic": "7895",
            "SKU_PRODUCTO": "49",
            "Inventario_Existencia": "10500"
        },
        "59": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "14",
            "ID_Ubic": "7900",
            "SKU_PRODUCTO": "59",
            "Inventario_Existencia": "6500"
        },
        "48": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "15",
            "ID_Ubic": "7905",
            "SKU_PRODUCTO": "48",
            "Inventario_Existencia": "14750"
        },
        "84": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "17",
            "ID_Ubic": "7915",
            "SKU_PRODUCTO": "84",
            "Inventario_Existencia": "6500"
        },
        "76": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "18",
            "ID_Ubic": "7920",
            "SKU_PRODUCTO": "76",
            "Inventario_Existencia": "9000"
        },
        "90": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "19",
            "ID_Ubic": "7925",
            "SKU_PRODUCTO": "90",
            "Inventario_Existencia": "750"
        },
        "58": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "21",
            "ID_Ubic": "7935",
            "SKU_PRODUCTO": "58",
            "Inventario_Existencia": "15250"
        },
        "19922": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "22",
            "ID_Ubic": "7940",
            "SKU_PRODUCTO": "19922",
            "Inventario_Existencia": "13000"
        },
        "56": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "23",
            "ID_Ubic": "7945",
            "SKU_PRODUCTO": "56",
            "Inventario_Existencia": "6750"
        },
        "81": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "24",
            "ID_Ubic": "7950",
            "SKU_PRODUCTO": "81",
            "Inventario_Existencia": "15000"
        },
        "17171": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "27",
            "ID_Ubic": "7965",
            "SKU_PRODUCTO": "17171",
            "Inventario_Existencia": "46500"
        },
        "18237": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "28",
            "ID_Ubic": "7970",
            "SKU_PRODUCTO": "18237",
            "Inventario_Existencia": "3500"
        },
        "18248": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "29",
            "ID_Ubic": "7975",
            "SKU_PRODUCTO": "18248",
            "Inventario_Existencia": "10000"
        },
        "18249": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "30",
            "ID_Ubic": "7980",
            "SKU_PRODUCTO": "18249",
            "Inventario_Existencia": "5500"
        },
        "10811": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "32",
            "ID_Ubic": "7990",
            "SKU_PRODUCTO": "10811",
            "Inventario_Existencia": "32000"
        },
        "10806": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "33",
            "ID_Ubic": "7995",
            "SKU_PRODUCTO": "10806",
            "Inventario_Existencia": "16000"
        },
        "10807": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "34",
            "ID_Ubic": "8000",
            "SKU_PRODUCTO": "10807",
            "Inventario_Existencia": "12500"
        },
        "57": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "35",
            "ID_Ubic": "8005",
            "SKU_PRODUCTO": "57",
            "Inventario_Existencia": "2250"
        },
        "14127": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "42",
            "ID_Ubic": "18120",
            "SKU_PRODUCTO": "14127",
            "Inventario_Existencia": "12000"
        },
        "14126": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "38",
            "ID_Ubic": "8020",
            "SKU_PRODUCTO": "14126",
            "Inventario_Existencia": "21500"
        },
        "42332": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "39",
            "ID_Ubic": "8025",
            "SKU_PRODUCTO": "42332",
            "Inventario_Existencia": "9500"
        },
        "42331": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "40",
            "ID_Ubic": "8030",
            "SKU_PRODUCTO": "42331",
            "Inventario_Existencia": "3000"
        },
        "80": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "41",
            "ID_Ubic": "8035",
            "SKU_PRODUCTO": "80",
            "Inventario_Existencia": "8500"
        },
        "40205": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "43",
            "ID_Ubic": "8045",
            "SKU_PRODUCTO": "40205",
            "Inventario_Existencia": "6000"
        },
        "40048": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "44",
            "ID_Ubic": "8050",
            "SKU_PRODUCTO": "40048",
            "Inventario_Existencia": "17250"
        },
        "40203": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "45",
            "ID_Ubic": "8055",
            "SKU_PRODUCTO": "40203",
            "Inventario_Existencia": "3000"
        },
        "70595": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "46",
            "ID_Ubic": "8060",
            "SKU_PRODUCTO": "70595",
            "Inventario_Existencia": "9000"
        },
        "17169": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "47",
            "ID_Ubic": "8065",
            "SKU_PRODUCTO": "17169",
            "Inventario_Existencia": "3000"
        },
        "209": {
            "Nombre_Pasillo": "D1",
            "X": "14",
            "Y": "48",
            "ID_Ubic": "8070",
            "SKU_PRODUCTO": "209",
            "Inventario_Existencia": "2500"
        },
        "40": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "40",
            "Inventario_Existencia": "500"
        },
        "42": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "2",
            "ID_Ubic": "9280",
            "SKU_PRODUCTO": "42",
            "Inventario_Existencia": "1500"
        },
        "51": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "3",
            "ID_Ubic": "9285",
            "SKU_PRODUCTO": "51",
            "Inventario_Existencia": "28000"
        },
        "38": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "4",
            "ID_Ubic": "9290",
            "SKU_PRODUCTO": "38",
            "Inventario_Existencia": "22500"
        },
        "89": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "5",
            "ID_Ubic": "9295",
            "SKU_PRODUCTO": "89",
            "Inventario_Existencia": "1500"
        },
        "54": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "6",
            "ID_Ubic": "9300",
            "SKU_PRODUCTO": "54",
            "Inventario_Existencia": "32500"
        },
        "41": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "7",
            "ID_Ubic": "9305",
            "SKU_PRODUCTO": "41",
            "Inventario_Existencia": "22500"
        },
        "92": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "8",
            "ID_Ubic": "9310",
            "SKU_PRODUCTO": "92",
            "Inventario_Existencia": "8000"
        },
        "39": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "9",
            "ID_Ubic": "9315",
            "SKU_PRODUCTO": "39",
            "Inventario_Existencia": "33500"
        },
        "2333": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "10",
            "ID_Ubic": "9320",
            "SKU_PRODUCTO": "2333",
            "Inventario_Existencia": "4750"
        },
        "91": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "11",
            "ID_Ubic": "9325",
            "SKU_PRODUCTO": "91",
            "Inventario_Existencia": "750"
        },
        "60": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "12",
            "ID_Ubic": "9330",
            "SKU_PRODUCTO": "60",
            "Inventario_Existencia": "18000"
        },
        "46": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "13",
            "ID_Ubic": "9335",
            "SKU_PRODUCTO": "46",
            "Inventario_Existencia": "7000"
        },
        "10965": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "14",
            "ID_Ubic": "9340",
            "SKU_PRODUCTO": "10965",
            "Inventario_Existencia": "17500"
        },
        "43": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "15",
            "ID_Ubic": "9345",
            "SKU_PRODUCTO": "43",
            "Inventario_Existencia": "56000"
        },
        "85": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "16",
            "ID_Ubic": "9350",
            "SKU_PRODUCTO": "85",
            "Inventario_Existencia": "10250"
        },
        "78": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "17",
            "ID_Ubic": "9355",
            "SKU_PRODUCTO": "78",
            "Inventario_Existencia": "28500"
        },
        "77": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "18",
            "ID_Ubic": "9360",
            "SKU_PRODUCTO": "77",
            "Inventario_Existencia": "6500"
        },
        "778": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "19",
            "ID_Ubic": "9365",
            "SKU_PRODUCTO": "778",
            "Inventario_Existencia": "12000"
        },
        "8714": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "20",
            "ID_Ubic": "9370",
            "SKU_PRODUCTO": "8714",
            "Inventario_Existencia": "9500"
        },
        "11840": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "21",
            "ID_Ubic": "9375",
            "SKU_PRODUCTO": "11840",
            "Inventario_Existencia": "13000"
        },
        "17170": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "22",
            "ID_Ubic": "9380",
            "SKU_PRODUCTO": "17170",
            "Inventario_Existencia": "34000"
        },
        "18238": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "23",
            "ID_Ubic": "9385",
            "SKU_PRODUCTO": "18238",
            "Inventario_Existencia": "46500"
        },
        "205": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "24",
            "ID_Ubic": "9390",
            "SKU_PRODUCTO": "205",
            "Inventario_Existencia": "13500"
        },
        "18250": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "27",
            "ID_Ubic": "9405",
            "SKU_PRODUCTO": "18250",
            "Inventario_Existencia": "14000"
        },
        "208": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "28",
            "ID_Ubic": "9410",
            "SKU_PRODUCTO": "208",
            "Inventario_Existencia": "9000"
        },
        "9767": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "29",
            "ID_Ubic": "9415",
            "SKU_PRODUCTO": "9767",
            "Inventario_Existencia": "3500"
        },
        "9444": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "30",
            "ID_Ubic": "9420",
            "SKU_PRODUCTO": "9444",
            "Inventario_Existencia": "14500"
        },
        "204": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "31",
            "ID_Ubic": "9425",
            "SKU_PRODUCTO": "204",
            "Inventario_Existencia": "6500"
        },
        "10808": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "32",
            "ID_Ubic": "9430",
            "SKU_PRODUCTO": "10808",
            "Inventario_Existencia": "24000"
        },
        "10810": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "33",
            "ID_Ubic": "9435",
            "SKU_PRODUCTO": "10810",
            "Inventario_Existencia": "22500"
        },
        "23827": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "34",
            "ID_Ubic": "9440",
            "SKU_PRODUCTO": "23827",
            "Inventario_Existencia": "1500"
        },
        "79": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "35",
            "ID_Ubic": "9445",
            "SKU_PRODUCTO": "79",
            "Inventario_Existencia": "13000"
        },
        "14128": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "36",
            "ID_Ubic": "9450",
            "SKU_PRODUCTO": "14128",
            "Inventario_Existencia": "2000"
        },
        "82": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "37",
            "ID_Ubic": "9455",
            "SKU_PRODUCTO": "82",
            "Inventario_Existencia": "1500"
        },
        "11841": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "38",
            "ID_Ubic": "9460",
            "SKU_PRODUCTO": "11841",
            "Inventario_Existencia": "9500"
        },
        "3267": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "39",
            "ID_Ubic": "9465",
            "SKU_PRODUCTO": "3267",
            "Inventario_Existencia": "3500"
        },
        "9768": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "40",
            "ID_Ubic": "9470",
            "SKU_PRODUCTO": "9768",
            "Inventario_Existencia": "35500"
        },
        "42333": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "41",
            "ID_Ubic": "9475",
            "SKU_PRODUCTO": "42333",
            "Inventario_Existencia": "3750"
        },
        "40780": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "42",
            "ID_Ubic": "9480",
            "SKU_PRODUCTO": "40780",
            "Inventario_Existencia": "6000"
        },
        "40049": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "43",
            "ID_Ubic": "9485",
            "SKU_PRODUCTO": "40049",
            "Inventario_Existencia": "12000"
        },
        "202": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "44",
            "ID_Ubic": "9490",
            "SKU_PRODUCTO": "202",
            "Inventario_Existencia": "3500"
        },
        "13127": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "46",
            "ID_Ubic": "9500",
            "SKU_PRODUCTO": "13127",
            "Inventario_Existencia": "2360"
        },
        "40201": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "47",
            "ID_Ubic": "9505",
            "SKU_PRODUCTO": "40201",
            "Inventario_Existencia": "3500"
        },
        "206": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "48",
            "ID_Ubic": "9510",
            "SKU_PRODUCTO": "206",
            "Inventario_Existencia": "7000"
        },
        "882": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "1",
            "ID_Ubic": "10715",
            "SKU_PRODUCTO": "882",
            "Inventario_Existencia": "3700"
        },
        "881": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "3",
            "ID_Ubic": "10725",
            "SKU_PRODUCTO": "881",
            "Inventario_Existencia": "4500"
        },
        "7703": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "4",
            "ID_Ubic": "10730",
            "SKU_PRODUCTO": "7703",
            "Inventario_Existencia": "13800"
        },
        "886": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "5",
            "ID_Ubic": "10735",
            "SKU_PRODUCTO": "886",
            "Inventario_Existencia": "3600"
        },
        "887": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "6",
            "ID_Ubic": "10740",
            "SKU_PRODUCTO": "887",
            "Inventario_Existencia": "4100"
        },
        "999": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "7",
            "ID_Ubic": "10745",
            "SKU_PRODUCTO": "999",
            "Inventario_Existencia": "15700"
        },
        "389": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "8",
            "ID_Ubic": "10750",
            "SKU_PRODUCTO": "389",
            "Inventario_Existencia": "3900"
        },
        "19228": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "9",
            "ID_Ubic": "10755",
            "SKU_PRODUCTO": "19228",
            "Inventario_Existencia": "10300"
        },
        "4159": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "10",
            "ID_Ubic": "10760",
            "SKU_PRODUCTO": "4159",
            "Inventario_Existencia": "2925"
        },
        "7098": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "11",
            "ID_Ubic": "10765",
            "SKU_PRODUCTO": "7098",
            "Inventario_Existencia": "12000"
        },
        "4116": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "12",
            "ID_Ubic": "10770",
            "SKU_PRODUCTO": "4116",
            "Inventario_Existencia": "12750"
        },
        "19231": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "13",
            "ID_Ubic": "10775",
            "SKU_PRODUCTO": "19231",
            "Inventario_Existencia": "600"
        },
        "993": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "14",
            "ID_Ubic": "10780",
            "SKU_PRODUCTO": "993",
            "Inventario_Existencia": "7200"
        },
        "376": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "15",
            "ID_Ubic": "10785",
            "SKU_PRODUCTO": "376",
            "Inventario_Existencia": "100"
        },
        "388": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "18",
            "ID_Ubic": "10800",
            "SKU_PRODUCTO": "388",
            "Inventario_Existencia": "1200"
        },
        "20233": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "19",
            "ID_Ubic": "10805",
            "SKU_PRODUCTO": "20233",
            "Inventario_Existencia": "4600"
        },
        "20232": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "20",
            "ID_Ubic": "10810",
            "SKU_PRODUCTO": "20232",
            "Inventario_Existencia": "4800"
        },
        "73166": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "21",
            "ID_Ubic": "10815",
            "SKU_PRODUCTO": "73166",
            "Inventario_Existencia": "4300"
        },
        "8200": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "22",
            "ID_Ubic": "10820",
            "SKU_PRODUCTO": "8200",
            "Inventario_Existencia": "1000"
        },
        "9664": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "23",
            "ID_Ubic": "10825",
            "SKU_PRODUCTO": "9664",
            "Inventario_Existencia": "6250"
        },
        "8681": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "24",
            "ID_Ubic": "10830",
            "SKU_PRODUCTO": "8681",
            "Inventario_Existencia": "2900"
        },
        "5936": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "28",
            "ID_Ubic": "10850",
            "SKU_PRODUCTO": "5936",
            "Inventario_Existencia": "1200"
        },
        "191": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "29",
            "ID_Ubic": "10855",
            "SKU_PRODUCTO": "191",
            "Inventario_Existencia": "400"
        },
        "8501": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "30",
            "ID_Ubic": "10860",
            "SKU_PRODUCTO": "8501",
            "Inventario_Existencia": "450"
        },
        "8502": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "31",
            "ID_Ubic": "10865",
            "SKU_PRODUCTO": "8502",
            "Inventario_Existencia": "550"
        },
        "5221": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "33",
            "ID_Ubic": "10875",
            "SKU_PRODUCTO": "5221",
            "Inventario_Existencia": "50"
        },
        "5429": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "34",
            "ID_Ubic": "10880",
            "SKU_PRODUCTO": "5429",
            "Inventario_Existencia": "300"
        },
        "5941": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "35",
            "ID_Ubic": "10885",
            "SKU_PRODUCTO": "5941",
            "Inventario_Existencia": "350"
        },
        "503": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "38",
            "ID_Ubic": "10900",
            "SKU_PRODUCTO": "503",
            "Inventario_Existencia": "250"
        },
        "7564": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "39",
            "ID_Ubic": "10905",
            "SKU_PRODUCTO": "7564",
            "Inventario_Existencia": "450"
        },
        "1502": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "42",
            "ID_Ubic": "10920",
            "SKU_PRODUCTO": "1502",
            "Inventario_Existencia": "1100"
        },
        "72162": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "45",
            "ID_Ubic": "10935",
            "SKU_PRODUCTO": "72162",
            "Inventario_Existencia": "2624"
        },
        "72160": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "46",
            "ID_Ubic": "10940",
            "SKU_PRODUCTO": "72160",
            "Inventario_Existencia": "2937"
        },
        "72872": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "48",
            "ID_Ubic": "10950",
            "SKU_PRODUCTO": "72872",
            "Inventario_Existencia": "2946"
        },
        "885": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "1",
            "ID_Ubic": "12155",
            "SKU_PRODUCTO": "885",
            "Inventario_Existencia": "1900"
        },
        "375": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "4",
            "ID_Ubic": "12170",
            "SKU_PRODUCTO": "375",
            "Inventario_Existencia": "7200"
        },
        "378": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "8",
            "ID_Ubic": "12190",
            "SKU_PRODUCTO": "378",
            "Inventario_Existencia": "2700"
        },
        "6409": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "12",
            "ID_Ubic": "12210",
            "SKU_PRODUCTO": "6409",
            "Inventario_Existencia": "7400"
        },
        "1003": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "13",
            "ID_Ubic": "12215",
            "SKU_PRODUCTO": "1003",
            "Inventario_Existencia": "6500"
        },
        "391": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "14",
            "ID_Ubic": "12220",
            "SKU_PRODUCTO": "391",
            "Inventario_Existencia": "2600"
        },
        "380": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "15",
            "ID_Ubic": "12225",
            "SKU_PRODUCTO": "380",
            "Inventario_Existencia": "1700"
        },
        "390": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "17",
            "ID_Ubic": "12235",
            "SKU_PRODUCTO": "390",
            "Inventario_Existencia": "800"
        },
        "4200": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "18",
            "ID_Ubic": "12240",
            "SKU_PRODUCTO": "4200",
            "Inventario_Existencia": "29400"
        },
        "379": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "19",
            "ID_Ubic": "12245",
            "SKU_PRODUCTO": "379",
            "Inventario_Existencia": "2800"
        },
        "9320": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "20",
            "ID_Ubic": "12250",
            "SKU_PRODUCTO": "9320",
            "Inventario_Existencia": "19700"
        },
        "377": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "21",
            "ID_Ubic": "12255",
            "SKU_PRODUCTO": "377",
            "Inventario_Existencia": "11900"
        },
        "73170": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "22",
            "ID_Ubic": "12260",
            "SKU_PRODUCTO": "73170",
            "Inventario_Existencia": "19300"
        },
        "8324": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "23",
            "ID_Ubic": "12265",
            "SKU_PRODUCTO": "8324",
            "Inventario_Existencia": "6800"
        },
        "5630": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "27",
            "ID_Ubic": "12285",
            "SKU_PRODUCTO": "5630",
            "Inventario_Existencia": "500"
        },
        "5579": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "5579",
            "Inventario_Existencia": "50"
        },
        "6280": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "29",
            "ID_Ubic": "12295",
            "SKU_PRODUCTO": "6280",
            "Inventario_Existencia": "150"
        },
        "3542": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "30",
            "ID_Ubic": "12300",
            "SKU_PRODUCTO": "3542",
            "Inventario_Existencia": "300"
        },
        "3859": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "31",
            "ID_Ubic": "12305",
            "SKU_PRODUCTO": "3859",
            "Inventario_Existencia": "400"
        },
        "8508": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "32",
            "ID_Ubic": "12310",
            "SKU_PRODUCTO": "8508",
            "Inventario_Existencia": "150"
        },
        "8507": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "33",
            "ID_Ubic": "12315",
            "SKU_PRODUCTO": "8507",
            "Inventario_Existencia": "50"
        },
        "8503": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "34",
            "ID_Ubic": "12320",
            "SKU_PRODUCTO": "8503",
            "Inventario_Existencia": "150"
        },
        "189": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "35",
            "ID_Ubic": "12325",
            "SKU_PRODUCTO": "189",
            "Inventario_Existencia": "1250"
        },
        "6113": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "36",
            "ID_Ubic": "12330",
            "SKU_PRODUCTO": "6113",
            "Inventario_Existencia": "6100"
        },
        "4540": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "37",
            "ID_Ubic": "12335",
            "SKU_PRODUCTO": "4540",
            "Inventario_Existencia": "1650"
        },
        "7589": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "38",
            "ID_Ubic": "12340",
            "SKU_PRODUCTO": "7589",
            "Inventario_Existencia": "1900"
        },
        "575": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "39",
            "ID_Ubic": "12345",
            "SKU_PRODUCTO": "575",
            "Inventario_Existencia": "850"
        },
        "17034": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "40",
            "ID_Ubic": "12350",
            "SKU_PRODUCTO": "17034",
            "Inventario_Existencia": "900"
        },
        "1776": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "41",
            "ID_Ubic": "12355",
            "SKU_PRODUCTO": "1776",
            "Inventario_Existencia": "370"
        },
        "1551": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "42",
            "ID_Ubic": "12360",
            "SKU_PRODUCTO": "1551",
            "Inventario_Existencia": "1150"
        },
        "1473": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "43",
            "ID_Ubic": "12365",
            "SKU_PRODUCTO": "1473",
            "Inventario_Existencia": "2400"
        },
        "72161": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "44",
            "ID_Ubic": "12370",
            "SKU_PRODUCTO": "72161",
            "Inventario_Existencia": "1536"
        },
        "72720": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "45",
            "ID_Ubic": "12375",
            "SKU_PRODUCTO": "72720",
            "Inventario_Existencia": "1344"
        },
        "72719": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "46",
            "ID_Ubic": "12380",
            "SKU_PRODUCTO": "72719",
            "Inventario_Existencia": "1361"
        },
        "72871": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "47",
            "ID_Ubic": "12385",
            "SKU_PRODUCTO": "72871",
            "Inventario_Existencia": "7386"
        },
        "18026": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "31",
            "ID_Ubic": "13745",
            "SKU_PRODUCTO": "18026",
            "Inventario_Existencia": "400"
        },
        "76722": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "9",
            "ID_Ubic": "15075",
            "SKU_PRODUCTO": "76722",
            "Inventario_Existencia": "2054"
        },
        "76712": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "4",
            "ID_Ubic": "13610",
            "SKU_PRODUCTO": "76712",
            "Inventario_Existencia": "542"
        },
        "76721": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "4",
            "ID_Ubic": "13610",
            "SKU_PRODUCTO": "76721",
            "Inventario_Existencia": "166"
        },
        "76699": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "3",
            "ID_Ubic": "13605",
            "SKU_PRODUCTO": "76699",
            "Inventario_Existencia": "387"
        },
        "76700": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "4",
            "ID_Ubic": "15050",
            "SKU_PRODUCTO": "76700",
            "Inventario_Existencia": "1500"
        },
        "76720": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "4",
            "ID_Ubic": "13610",
            "SKU_PRODUCTO": "76720",
            "Inventario_Existencia": "830"
        },
        "2373": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "30",
            "ID_Ubic": "13740",
            "SKU_PRODUCTO": "2373",
            "Inventario_Existencia": "3"
        },
        "2626": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "36",
            "ID_Ubic": "15210",
            "SKU_PRODUCTO": "2626",
            "Inventario_Existencia": "10"
        },
        "7165": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "20",
            "ID_Ubic": "13690",
            "SKU_PRODUCTO": "7165",
            "Inventario_Existencia": "20"
        },
        "27098": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "6",
            "ID_Ubic": "13620",
            "SKU_PRODUCTO": "27098",
            "Inventario_Existencia": "1"
        },
        "30080": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "6",
            "ID_Ubic": "13620",
            "SKU_PRODUCTO": "30080",
            "Inventario_Existencia": "500"
        },
        "70809": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "6",
            "ID_Ubic": "13620",
            "SKU_PRODUCTO": "70809",
            "Inventario_Existencia": "600"
        },
        "76706": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "7",
            "ID_Ubic": "13625",
            "SKU_PRODUCTO": "76706",
            "Inventario_Existencia": "489"
        },
        "76702": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "8",
            "ID_Ubic": "13630",
            "SKU_PRODUCTO": "76702",
            "Inventario_Existencia": "776"
        },
        "28290": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "32",
            "ID_Ubic": "13750",
            "SKU_PRODUCTO": "28290",
            "Inventario_Existencia": "5"
        },
        "28291": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "32",
            "ID_Ubic": "13750",
            "SKU_PRODUCTO": "28291",
            "Inventario_Existencia": "5"
        },
        "11168": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "10",
            "ID_Ubic": "13640",
            "SKU_PRODUCTO": "11168",
            "Inventario_Existencia": "110"
        },
        "73703": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "35",
            "ID_Ubic": "15205",
            "SKU_PRODUCTO": "73703",
            "Inventario_Existencia": "30"
        },
        "4967": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "11",
            "ID_Ubic": "13645",
            "SKU_PRODUCTO": "4967",
            "Inventario_Existencia": "400"
        },
        "4993": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "11",
            "ID_Ubic": "13645",
            "SKU_PRODUCTO": "4993",
            "Inventario_Existencia": "20"
        },
        "13677": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "11",
            "ID_Ubic": "13645",
            "SKU_PRODUCTO": "13677",
            "Inventario_Existencia": "250"
        },
        "15631": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "11",
            "ID_Ubic": "13645",
            "SKU_PRODUCTO": "15631",
            "Inventario_Existencia": "200"
        },
        "21310": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "11",
            "ID_Ubic": "13645",
            "SKU_PRODUCTO": "21310",
            "Inventario_Existencia": "20"
        },
        "22396": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "11",
            "ID_Ubic": "13645",
            "SKU_PRODUCTO": "22396",
            "Inventario_Existencia": "150"
        },
        "76853": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "11",
            "ID_Ubic": "13645",
            "SKU_PRODUCTO": "76853",
            "Inventario_Existencia": "10"
        },
        "2347": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "12",
            "ID_Ubic": "13650",
            "SKU_PRODUCTO": "2347",
            "Inventario_Existencia": "40"
        },
        "2921": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "41",
            "ID_Ubic": "13795",
            "SKU_PRODUCTO": "2921",
            "Inventario_Existencia": "250"
        },
        "26437": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "12",
            "ID_Ubic": "13650",
            "SKU_PRODUCTO": "26437",
            "Inventario_Existencia": "1000"
        },
        "70830": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "12",
            "ID_Ubic": "13650",
            "SKU_PRODUCTO": "70830",
            "Inventario_Existencia": "600"
        },
        "9923": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "14",
            "ID_Ubic": "13660",
            "SKU_PRODUCTO": "9923",
            "Inventario_Existencia": "1"
        },
        "27002": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "41",
            "ID_Ubic": "18115",
            "SKU_PRODUCTO": "27002",
            "Inventario_Existencia": "2"
        },
        "27003": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "14",
            "ID_Ubic": "13660",
            "SKU_PRODUCTO": "27003",
            "Inventario_Existencia": "6"
        },
        "27004": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "14",
            "ID_Ubic": "13660",
            "SKU_PRODUCTO": "27004",
            "Inventario_Existencia": "4"
        },
        "27549": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "14",
            "ID_Ubic": "13660",
            "SKU_PRODUCTO": "27549",
            "Inventario_Existencia": "1"
        },
        "27840": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "14",
            "ID_Ubic": "13660",
            "SKU_PRODUCTO": "27840",
            "Inventario_Existencia": "1"
        },
        "27882": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "14",
            "ID_Ubic": "13660",
            "SKU_PRODUCTO": "27882",
            "Inventario_Existencia": "1"
        },
        "25": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "32",
            "ID_Ubic": "13750",
            "SKU_PRODUCTO": "25",
            "Inventario_Existencia": "200"
        },
        "808": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "15",
            "ID_Ubic": "13665",
            "SKU_PRODUCTO": "808",
            "Inventario_Existencia": "50"
        },
        "2966": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "48",
            "ID_Ubic": "13830",
            "SKU_PRODUCTO": "2966",
            "Inventario_Existencia": "50"
        },
        "3540": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "15",
            "ID_Ubic": "13665",
            "SKU_PRODUCTO": "3540",
            "Inventario_Existencia": "50"
        },
        "4978": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "15",
            "ID_Ubic": "13665",
            "SKU_PRODUCTO": "4978",
            "Inventario_Existencia": "200"
        },
        "14567": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "15",
            "ID_Ubic": "13665",
            "SKU_PRODUCTO": "14567",
            "Inventario_Existencia": "50"
        },
        "17542": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "15",
            "ID_Ubic": "13665",
            "SKU_PRODUCTO": "17542",
            "Inventario_Existencia": "60"
        },
        "17609": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "15",
            "ID_Ubic": "13665",
            "SKU_PRODUCTO": "17609",
            "Inventario_Existencia": "100"
        },
        "25213": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "27",
            "ID_Ubic": "13725",
            "SKU_PRODUCTO": "25213",
            "Inventario_Existencia": "20"
        },
        "26786": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "15",
            "ID_Ubic": "13665",
            "SKU_PRODUCTO": "26786",
            "Inventario_Existencia": "40"
        },
        "27034": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "15",
            "ID_Ubic": "13665",
            "SKU_PRODUCTO": "27034",
            "Inventario_Existencia": "150"
        },
        "29346": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "15",
            "ID_Ubic": "13665",
            "SKU_PRODUCTO": "29346",
            "Inventario_Existencia": "200"
        },
        "76854": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "15",
            "ID_Ubic": "13665",
            "SKU_PRODUCTO": "76854",
            "Inventario_Existencia": "10"
        },
        "1691": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "16",
            "ID_Ubic": "13670",
            "SKU_PRODUCTO": "1691",
            "Inventario_Existencia": "1200"
        },
        "3172": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "17",
            "ID_Ubic": "13675",
            "SKU_PRODUCTO": "3172",
            "Inventario_Existencia": "1000"
        },
        "8750": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "17",
            "ID_Ubic": "13675",
            "SKU_PRODUCTO": "8750",
            "Inventario_Existencia": "500"
        },
        "16489": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "18",
            "ID_Ubic": "13680",
            "SKU_PRODUCTO": "16489",
            "Inventario_Existencia": "50"
        },
        "16548": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "18",
            "ID_Ubic": "13680",
            "SKU_PRODUCTO": "16548",
            "Inventario_Existencia": "50"
        },
        "32523": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "18",
            "ID_Ubic": "13680",
            "SKU_PRODUCTO": "32523",
            "Inventario_Existencia": "12000"
        },
        "33416": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "18",
            "ID_Ubic": "13680",
            "SKU_PRODUCTO": "33416",
            "Inventario_Existencia": "61920"
        },
        "71674": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "43",
            "ID_Ubic": "13805",
            "SKU_PRODUCTO": "71674",
            "Inventario_Existencia": "60"
        },
        "7368": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "18",
            "ID_Ubic": "15120",
            "SKU_PRODUCTO": "7368",
            "Inventario_Existencia": "1"
        },
        "14227": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "20",
            "ID_Ubic": "13690",
            "SKU_PRODUCTO": "14227",
            "Inventario_Existencia": "100"
        },
        "20831": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "41",
            "ID_Ubic": "15235",
            "SKU_PRODUCTO": "20831",
            "Inventario_Existencia": "500"
        },
        "21652": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "20",
            "ID_Ubic": "13690",
            "SKU_PRODUCTO": "21652",
            "Inventario_Existencia": "50"
        },
        "23669": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "20",
            "ID_Ubic": "13690",
            "SKU_PRODUCTO": "23669",
            "Inventario_Existencia": "1500"
        },
        "26869": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "20",
            "ID_Ubic": "13690",
            "SKU_PRODUCTO": "26869",
            "Inventario_Existencia": "40"
        },
        "70388": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "20",
            "ID_Ubic": "13690",
            "SKU_PRODUCTO": "70388",
            "Inventario_Existencia": "50"
        },
        "73183": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "41",
            "ID_Ubic": "15235",
            "SKU_PRODUCTO": "73183",
            "Inventario_Existencia": "1600"
        },
        "73297": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "20",
            "ID_Ubic": "13690",
            "SKU_PRODUCTO": "73297",
            "Inventario_Existencia": "100"
        },
        "1079": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "22",
            "ID_Ubic": "13700",
            "SKU_PRODUCTO": "1079",
            "Inventario_Existencia": "9"
        },
        "2536": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "22",
            "ID_Ubic": "13700",
            "SKU_PRODUCTO": "2536",
            "Inventario_Existencia": "12"
        },
        "16813": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "22",
            "ID_Ubic": "13700",
            "SKU_PRODUCTO": "16813",
            "Inventario_Existencia": "10"
        },
        "16842": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "22",
            "ID_Ubic": "13700",
            "SKU_PRODUCTO": "16842",
            "Inventario_Existencia": "10"
        },
        "30049": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "32",
            "ID_Ubic": "13750",
            "SKU_PRODUCTO": "30049",
            "Inventario_Existencia": "2000"
        },
        "32647": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "22",
            "ID_Ubic": "13700",
            "SKU_PRODUCTO": "32647",
            "Inventario_Existencia": "500"
        },
        "33415": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "22",
            "ID_Ubic": "13700",
            "SKU_PRODUCTO": "33415",
            "Inventario_Existencia": "1440"
        },
        "70967": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "29",
            "ID_Ubic": "13735",
            "SKU_PRODUCTO": "70967",
            "Inventario_Existencia": "310"
        },
        "849": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "23",
            "ID_Ubic": "13705",
            "SKU_PRODUCTO": "849",
            "Inventario_Existencia": "250"
        },
        "1818": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "23",
            "ID_Ubic": "13705",
            "SKU_PRODUCTO": "1818",
            "Inventario_Existencia": "2"
        },
        "6342": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "23",
            "ID_Ubic": "13705",
            "SKU_PRODUCTO": "6342",
            "Inventario_Existencia": "250"
        },
        "6514": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "23",
            "ID_Ubic": "13705",
            "SKU_PRODUCTO": "6514",
            "Inventario_Existencia": "650"
        },
        "7319": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "23",
            "ID_Ubic": "13705",
            "SKU_PRODUCTO": "7319",
            "Inventario_Existencia": "400"
        },
        "11731": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "29",
            "ID_Ubic": "15175",
            "SKU_PRODUCTO": "11731",
            "Inventario_Existencia": "5000"
        },
        "30009": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "23",
            "ID_Ubic": "13705",
            "SKU_PRODUCTO": "30009",
            "Inventario_Existencia": "3000"
        },
        "30340": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "23",
            "ID_Ubic": "13705",
            "SKU_PRODUCTO": "30340",
            "Inventario_Existencia": "750"
        },
        "73557": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "23",
            "ID_Ubic": "13705",
            "SKU_PRODUCTO": "73557",
            "Inventario_Existencia": "400"
        },
        "476": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "47",
            "ID_Ubic": "13825",
            "SKU_PRODUCTO": "476",
            "Inventario_Existencia": "500"
        },
        "640": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "24",
            "ID_Ubic": "13710",
            "SKU_PRODUCTO": "640",
            "Inventario_Existencia": "50"
        },
        "4185": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "24",
            "ID_Ubic": "13710",
            "SKU_PRODUCTO": "4185",
            "Inventario_Existencia": "700"
        },
        "34192": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "24",
            "ID_Ubic": "13710",
            "SKU_PRODUCTO": "34192",
            "Inventario_Existencia": "2000"
        },
        "366": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "27",
            "ID_Ubic": "13725",
            "SKU_PRODUCTO": "366",
            "Inventario_Existencia": "200"
        },
        "367": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "27",
            "ID_Ubic": "13725",
            "SKU_PRODUCTO": "367",
            "Inventario_Existencia": "200"
        },
        "4326": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "27",
            "ID_Ubic": "13725",
            "SKU_PRODUCTO": "4326",
            "Inventario_Existencia": "5"
        },
        "6287": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "27",
            "ID_Ubic": "13725",
            "SKU_PRODUCTO": "6287",
            "Inventario_Existencia": "50"
        },
        "24036": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "27",
            "ID_Ubic": "13725",
            "SKU_PRODUCTO": "24036",
            "Inventario_Existencia": "10"
        },
        "35841": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "27",
            "ID_Ubic": "13725",
            "SKU_PRODUCTO": "35841",
            "Inventario_Existencia": "900"
        },
        "74606": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "27",
            "ID_Ubic": "13725",
            "SKU_PRODUCTO": "74606",
            "Inventario_Existencia": "2000"
        },
        "14911": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "28",
            "ID_Ubic": "13730",
            "SKU_PRODUCTO": "14911",
            "Inventario_Existencia": "20"
        },
        "16422": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "28",
            "ID_Ubic": "13730",
            "SKU_PRODUCTO": "16422",
            "Inventario_Existencia": "10"
        },
        "74667": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "43",
            "ID_Ubic": "15245",
            "SKU_PRODUCTO": "74667",
            "Inventario_Existencia": "40"
        },
        "13345": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "29",
            "ID_Ubic": "13735",
            "SKU_PRODUCTO": "13345",
            "Inventario_Existencia": "10"
        },
        "441": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "30",
            "ID_Ubic": "13740",
            "SKU_PRODUCTO": "441",
            "Inventario_Existencia": "1600"
        },
        "19370": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "28",
            "ID_Ubic": "15170",
            "SKU_PRODUCTO": "19370",
            "Inventario_Existencia": "500"
        },
        "76177": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "30",
            "ID_Ubic": "13740",
            "SKU_PRODUCTO": "76177",
            "Inventario_Existencia": "1"
        },
        "3171": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "34",
            "ID_Ubic": "13760",
            "SKU_PRODUCTO": "3171",
            "Inventario_Existencia": "100"
        },
        "12824": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "33",
            "ID_Ubic": "15195",
            "SKU_PRODUCTO": "12824",
            "Inventario_Existencia": "1250"
        },
        "15": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "48",
            "ID_Ubic": "13830",
            "SKU_PRODUCTO": "15",
            "Inventario_Existencia": "150"
        },
        "2888": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "32",
            "ID_Ubic": "13750",
            "SKU_PRODUCTO": "2888",
            "Inventario_Existencia": "50"
        },
        "28289": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "35",
            "ID_Ubic": "13765",
            "SKU_PRODUCTO": "28289",
            "Inventario_Existencia": "32"
        },
        "71467": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "32",
            "ID_Ubic": "13750",
            "SKU_PRODUCTO": "71467",
            "Inventario_Existencia": "150"
        },
        "72287": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "32",
            "ID_Ubic": "13750",
            "SKU_PRODUCTO": "72287",
            "Inventario_Existencia": "5"
        },
        "3657": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "33",
            "ID_Ubic": "13755",
            "SKU_PRODUCTO": "3657",
            "Inventario_Existencia": "750"
        },
        "14059": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "38",
            "ID_Ubic": "15220",
            "SKU_PRODUCTO": "14059",
            "Inventario_Existencia": "200"
        },
        "14730": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "33",
            "ID_Ubic": "13755",
            "SKU_PRODUCTO": "14730",
            "Inventario_Existencia": "50"
        },
        "28793": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "33",
            "ID_Ubic": "13755",
            "SKU_PRODUCTO": "28793",
            "Inventario_Existencia": "400"
        },
        "28794": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "33",
            "ID_Ubic": "13755",
            "SKU_PRODUCTO": "28794",
            "Inventario_Existencia": "800"
        },
        "28795": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "33",
            "ID_Ubic": "13755",
            "SKU_PRODUCTO": "28795",
            "Inventario_Existencia": "800"
        },
        "28796": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "33",
            "ID_Ubic": "13755",
            "SKU_PRODUCTO": "28796",
            "Inventario_Existencia": "400"
        },
        "28797": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "33",
            "ID_Ubic": "13755",
            "SKU_PRODUCTO": "28797",
            "Inventario_Existencia": "400"
        },
        "72658": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "44",
            "ID_Ubic": "15250",
            "SKU_PRODUCTO": "72658",
            "Inventario_Existencia": "100"
        },
        "4581": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "34",
            "ID_Ubic": "13760",
            "SKU_PRODUCTO": "4581",
            "Inventario_Existencia": "500"
        },
        "13904": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "30",
            "ID_Ubic": "15180",
            "SKU_PRODUCTO": "13904",
            "Inventario_Existencia": "400"
        },
        "14244": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "34",
            "ID_Ubic": "13760",
            "SKU_PRODUCTO": "14244",
            "Inventario_Existencia": "1700"
        },
        "16586": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "34",
            "ID_Ubic": "13760",
            "SKU_PRODUCTO": "16586",
            "Inventario_Existencia": "20"
        },
        "19083": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "33",
            "ID_Ubic": "15195",
            "SKU_PRODUCTO": "19083",
            "Inventario_Existencia": "500"
        },
        "22026": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "44",
            "ID_Ubic": "15250",
            "SKU_PRODUCTO": "22026",
            "Inventario_Existencia": "800"
        },
        "2322": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "41",
            "ID_Ubic": "13795",
            "SKU_PRODUCTO": "2322",
            "Inventario_Existencia": "10"
        },
        "74618": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "35",
            "ID_Ubic": "13765",
            "SKU_PRODUCTO": "74618",
            "Inventario_Existencia": "500"
        },
        "4240": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "36",
            "ID_Ubic": "13770",
            "SKU_PRODUCTO": "4240",
            "Inventario_Existencia": "20"
        },
        "7027": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "36",
            "ID_Ubic": "13770",
            "SKU_PRODUCTO": "7027",
            "Inventario_Existencia": "150"
        },
        "18024": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "36",
            "ID_Ubic": "13770",
            "SKU_PRODUCTO": "18024",
            "Inventario_Existencia": "300"
        },
        "71507": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "36",
            "ID_Ubic": "13770",
            "SKU_PRODUCTO": "71507",
            "Inventario_Existencia": "105"
        },
        "546": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "37",
            "ID_Ubic": "13775",
            "SKU_PRODUCTO": "546",
            "Inventario_Existencia": "500"
        },
        "4878": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "37",
            "ID_Ubic": "13775",
            "SKU_PRODUCTO": "4878",
            "Inventario_Existencia": "5"
        },
        "9277": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "37",
            "ID_Ubic": "13775",
            "SKU_PRODUCTO": "9277",
            "Inventario_Existencia": "500"
        },
        "15476": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "37",
            "ID_Ubic": "13775",
            "SKU_PRODUCTO": "15476",
            "Inventario_Existencia": "1500"
        },
        "18103": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "37",
            "ID_Ubic": "13775",
            "SKU_PRODUCTO": "18103",
            "Inventario_Existencia": "500"
        },
        "19753": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "43",
            "ID_Ubic": "15245",
            "SKU_PRODUCTO": "19753",
            "Inventario_Existencia": "1200"
        },
        "25798": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "37",
            "ID_Ubic": "13775",
            "SKU_PRODUCTO": "25798",
            "Inventario_Existencia": "30"
        },
        "73570W": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "37",
            "ID_Ubic": "13775",
            "SKU_PRODUCTO": "73570W",
            "Inventario_Existencia": "800"
        },
        "73573W": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "37",
            "ID_Ubic": "13775",
            "SKU_PRODUCTO": "73573W",
            "Inventario_Existencia": "800"
        },
        "15749": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "47",
            "ID_Ubic": "13825",
            "SKU_PRODUCTO": "15749",
            "Inventario_Existencia": "120"
        },
        "16979": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "38",
            "ID_Ubic": "13780",
            "SKU_PRODUCTO": "16979",
            "Inventario_Existencia": "100"
        },
        "71675": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "38",
            "ID_Ubic": "13780",
            "SKU_PRODUCTO": "71675",
            "Inventario_Existencia": "400"
        },
        "28515": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "39",
            "ID_Ubic": "13785",
            "SKU_PRODUCTO": "28515",
            "Inventario_Existencia": "500"
        },
        "71031": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "39",
            "ID_Ubic": "13785",
            "SKU_PRODUCTO": "71031",
            "Inventario_Existencia": "2"
        },
        "74372": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "39",
            "ID_Ubic": "13785",
            "SKU_PRODUCTO": "74372",
            "Inventario_Existencia": "5"
        },
        "74600": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "39",
            "ID_Ubic": "13785",
            "SKU_PRODUCTO": "74600",
            "Inventario_Existencia": "50000"
        },
        "565": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "40",
            "ID_Ubic": "13790",
            "SKU_PRODUCTO": "565",
            "Inventario_Existencia": "500"
        },
        "18750": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "40",
            "ID_Ubic": "13790",
            "SKU_PRODUCTO": "18750",
            "Inventario_Existencia": "450"
        },
        "19409": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "40",
            "ID_Ubic": "13790",
            "SKU_PRODUCTO": "19409",
            "Inventario_Existencia": "6"
        },
        "27899": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "40",
            "ID_Ubic": "13790",
            "SKU_PRODUCTO": "27899",
            "Inventario_Existencia": "1"
        },
        "27900": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "40",
            "ID_Ubic": "13790",
            "SKU_PRODUCTO": "27900",
            "Inventario_Existencia": "1"
        },
        "32351": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "40",
            "ID_Ubic": "13790",
            "SKU_PRODUCTO": "32351",
            "Inventario_Existencia": "20"
        },
        "71300": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "40",
            "ID_Ubic": "13790",
            "SKU_PRODUCTO": "71300",
            "Inventario_Existencia": "1"
        },
        "73269": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "40",
            "ID_Ubic": "13790",
            "SKU_PRODUCTO": "73269",
            "Inventario_Existencia": "6"
        },
        "73270": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "40",
            "ID_Ubic": "13790",
            "SKU_PRODUCTO": "73270",
            "Inventario_Existencia": "6"
        },
        "587": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "41",
            "ID_Ubic": "13795",
            "SKU_PRODUCTO": "587",
            "Inventario_Existencia": "2"
        },
        "639": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "41",
            "ID_Ubic": "13795",
            "SKU_PRODUCTO": "639",
            "Inventario_Existencia": "20"
        },
        "663": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "41",
            "ID_Ubic": "13795",
            "SKU_PRODUCTO": "663",
            "Inventario_Existencia": "40"
        },
        "664": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "41",
            "ID_Ubic": "13795",
            "SKU_PRODUCTO": "664",
            "Inventario_Existencia": "10"
        },
        "894": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "41",
            "ID_Ubic": "13795",
            "SKU_PRODUCTO": "894",
            "Inventario_Existencia": "100"
        },
        "6412": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "41",
            "ID_Ubic": "13795",
            "SKU_PRODUCTO": "6412",
            "Inventario_Existencia": "800"
        },
        "11196": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "41",
            "ID_Ubic": "13795",
            "SKU_PRODUCTO": "11196",
            "Inventario_Existencia": "50"
        },
        "27716": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "41",
            "ID_Ubic": "13795",
            "SKU_PRODUCTO": "27716",
            "Inventario_Existencia": "1"
        },
        "74248": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "41",
            "ID_Ubic": "13795",
            "SKU_PRODUCTO": "74248",
            "Inventario_Existencia": "1"
        },
        "200": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "42",
            "ID_Ubic": "13800",
            "SKU_PRODUCTO": "200",
            "Inventario_Existencia": "500"
        },
        "731": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "42",
            "ID_Ubic": "13800",
            "SKU_PRODUCTO": "731",
            "Inventario_Existencia": "100"
        },
        "2249": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "42",
            "ID_Ubic": "13800",
            "SKU_PRODUCTO": "2249",
            "Inventario_Existencia": "500"
        },
        "19392": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "42",
            "ID_Ubic": "13800",
            "SKU_PRODUCTO": "19392",
            "Inventario_Existencia": "2000"
        },
        "20391": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "42",
            "ID_Ubic": "13800",
            "SKU_PRODUCTO": "20391",
            "Inventario_Existencia": "10"
        },
        "22244": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "42",
            "ID_Ubic": "13800",
            "SKU_PRODUCTO": "22244",
            "Inventario_Existencia": "100"
        },
        "33202": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "42",
            "ID_Ubic": "13800",
            "SKU_PRODUCTO": "33202",
            "Inventario_Existencia": "1200"
        },
        "33209": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "42",
            "ID_Ubic": "13800",
            "SKU_PRODUCTO": "33209",
            "Inventario_Existencia": "1200"
        },
        "73185W": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "42",
            "ID_Ubic": "13800",
            "SKU_PRODUCTO": "73185W",
            "Inventario_Existencia": "400"
        },
        "73190W": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "42",
            "ID_Ubic": "13800",
            "SKU_PRODUCTO": "73190W",
            "Inventario_Existencia": "400"
        },
        "73576W": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "42",
            "ID_Ubic": "13800",
            "SKU_PRODUCTO": "73576W",
            "Inventario_Existencia": "400"
        },
        "4771": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "43",
            "ID_Ubic": "13805",
            "SKU_PRODUCTO": "4771",
            "Inventario_Existencia": "20"
        },
        "12542": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "43",
            "ID_Ubic": "13805",
            "SKU_PRODUCTO": "12542",
            "Inventario_Existencia": "20"
        },
        "18023": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "43",
            "ID_Ubic": "13805",
            "SKU_PRODUCTO": "18023",
            "Inventario_Existencia": "200"
        },
        "19972": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "43",
            "ID_Ubic": "13805",
            "SKU_PRODUCTO": "19972",
            "Inventario_Existencia": "150"
        },
        "30174": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "32",
            "ID_Ubic": "18070",
            "SKU_PRODUCTO": "30174",
            "Inventario_Existencia": "500"
        },
        "32689": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "43",
            "ID_Ubic": "13805",
            "SKU_PRODUCTO": "32689",
            "Inventario_Existencia": "2400"
        },
        "32693": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "43",
            "ID_Ubic": "13805",
            "SKU_PRODUCTO": "32693",
            "Inventario_Existencia": "2000"
        },
        "34201": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "43",
            "ID_Ubic": "13805",
            "SKU_PRODUCTO": "34201",
            "Inventario_Existencia": "2400"
        },
        "74164": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "43",
            "ID_Ubic": "13805",
            "SKU_PRODUCTO": "74164",
            "Inventario_Existencia": "1000"
        },
        "76198": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "43",
            "ID_Ubic": "13805",
            "SKU_PRODUCTO": "76198",
            "Inventario_Existencia": "1"
        },
        "228": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "44",
            "ID_Ubic": "13810",
            "SKU_PRODUCTO": "228",
            "Inventario_Existencia": "3500"
        },
        "373": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "43",
            "ID_Ubic": "15245",
            "SKU_PRODUCTO": "373",
            "Inventario_Existencia": "500"
        },
        "3386": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "44",
            "ID_Ubic": "13810",
            "SKU_PRODUCTO": "3386",
            "Inventario_Existencia": "20"
        },
        "4117": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "44",
            "ID_Ubic": "13810",
            "SKU_PRODUCTO": "4117",
            "Inventario_Existencia": "500"
        },
        "15629": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "44",
            "ID_Ubic": "13810",
            "SKU_PRODUCTO": "15629",
            "Inventario_Existencia": "1000"
        },
        "211": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "45",
            "ID_Ubic": "13815",
            "SKU_PRODUCTO": "211",
            "Inventario_Existencia": "4000"
        },
        "17880": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "45",
            "ID_Ubic": "13815",
            "SKU_PRODUCTO": "17880",
            "Inventario_Existencia": "250"
        },
        "26268": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "47",
            "ID_Ubic": "13825",
            "SKU_PRODUCTO": "26268",
            "Inventario_Existencia": "80"
        },
        "4658": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "46",
            "ID_Ubic": "13820",
            "SKU_PRODUCTO": "4658",
            "Inventario_Existencia": "500"
        },
        "4675": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "46",
            "ID_Ubic": "13820",
            "SKU_PRODUCTO": "4675",
            "Inventario_Existencia": "50"
        },
        "4684": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "46",
            "ID_Ubic": "13820",
            "SKU_PRODUCTO": "4684",
            "Inventario_Existencia": "500"
        },
        "4686": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "46",
            "ID_Ubic": "13820",
            "SKU_PRODUCTO": "4686",
            "Inventario_Existencia": "500"
        },
        "4691": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "4691",
            "Inventario_Existencia": "1000"
        },
        "6289": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "46",
            "ID_Ubic": "13820",
            "SKU_PRODUCTO": "6289",
            "Inventario_Existencia": "100"
        },
        "7836": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "46",
            "ID_Ubic": "13820",
            "SKU_PRODUCTO": "7836",
            "Inventario_Existencia": "250"
        },
        "7840": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "46",
            "ID_Ubic": "13820",
            "SKU_PRODUCTO": "7840",
            "Inventario_Existencia": "250"
        },
        "9674": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "46",
            "ID_Ubic": "13820",
            "SKU_PRODUCTO": "9674",
            "Inventario_Existencia": "500"
        },
        "11802": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "46",
            "ID_Ubic": "13820",
            "SKU_PRODUCTO": "11802",
            "Inventario_Existencia": "500"
        },
        "16520": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "46",
            "ID_Ubic": "13820",
            "SKU_PRODUCTO": "16520",
            "Inventario_Existencia": "500"
        },
        "19754": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "46",
            "ID_Ubic": "13820",
            "SKU_PRODUCTO": "19754",
            "Inventario_Existencia": "400"
        },
        "19918": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "46",
            "ID_Ubic": "13820",
            "SKU_PRODUCTO": "19918",
            "Inventario_Existencia": "500"
        },
        "22631": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "45",
            "ID_Ubic": "15255",
            "SKU_PRODUCTO": "22631",
            "Inventario_Existencia": "400"
        },
        "2594": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "47",
            "ID_Ubic": "13825",
            "SKU_PRODUCTO": "2594",
            "Inventario_Existencia": "60"
        },
        "3432": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "47",
            "ID_Ubic": "13825",
            "SKU_PRODUCTO": "3432",
            "Inventario_Existencia": "40"
        },
        "17896": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "47",
            "ID_Ubic": "13825",
            "SKU_PRODUCTO": "17896",
            "Inventario_Existencia": "1250"
        },
        "73165W": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "47",
            "ID_Ubic": "13825",
            "SKU_PRODUCTO": "73165W",
            "Inventario_Existencia": "400"
        },
        "440": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "48",
            "ID_Ubic": "13830",
            "SKU_PRODUCTO": "440",
            "Inventario_Existencia": "600"
        },
        "5062": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "48",
            "ID_Ubic": "13830",
            "SKU_PRODUCTO": "5062",
            "Inventario_Existencia": "500"
        },
        "7937": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "48",
            "ID_Ubic": "13830",
            "SKU_PRODUCTO": "7937",
            "Inventario_Existencia": "50"
        },
        "10121": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "48",
            "ID_Ubic": "13830",
            "SKU_PRODUCTO": "10121",
            "Inventario_Existencia": "100"
        },
        "11113": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "48",
            "ID_Ubic": "13830",
            "SKU_PRODUCTO": "11113",
            "Inventario_Existencia": "1000"
        },
        "19369": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "48",
            "ID_Ubic": "13830",
            "SKU_PRODUCTO": "19369",
            "Inventario_Existencia": "1500"
        },
        "20829": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "48",
            "ID_Ubic": "13830",
            "SKU_PRODUCTO": "20829",
            "Inventario_Existencia": "20"
        },
        "22312": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "48",
            "ID_Ubic": "13830",
            "SKU_PRODUCTO": "22312",
            "Inventario_Existencia": "35"
        },
        "71062": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "34",
            "ID_Ubic": "15200",
            "SKU_PRODUCTO": "71062",
            "Inventario_Existencia": "1"
        },
        "74920": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "1",
            "ID_Ubic": "15035",
            "SKU_PRODUCTO": "74920",
            "Inventario_Existencia": "2"
        },
        "74921": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "1",
            "ID_Ubic": "15035",
            "SKU_PRODUCTO": "74921",
            "Inventario_Existencia": "2"
        },
        "74922": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "1",
            "ID_Ubic": "15035",
            "SKU_PRODUCTO": "74922",
            "Inventario_Existencia": "1"
        },
        "74923": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "1",
            "ID_Ubic": "15035",
            "SKU_PRODUCTO": "74923",
            "Inventario_Existencia": "1"
        },
        "76708": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "39",
            "ID_Ubic": "18105",
            "SKU_PRODUCTO": "76708",
            "Inventario_Existencia": "178"
        },
        "76723": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "60",
            "ID_Ubic": "107780",
            "SKU_PRODUCTO": "76723",
            "Inventario_Existencia": "1090"
        },
        "734": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "5",
            "ID_Ubic": "15055",
            "SKU_PRODUCTO": "734",
            "Inventario_Existencia": "4"
        },
        "758": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "5",
            "ID_Ubic": "15055",
            "SKU_PRODUCTO": "758",
            "Inventario_Existencia": "2"
        },
        "2813": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "5",
            "ID_Ubic": "15055",
            "SKU_PRODUCTO": "2813",
            "Inventario_Existencia": "10"
        },
        "7365": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "12",
            "ID_Ubic": "15090",
            "SKU_PRODUCTO": "7365",
            "Inventario_Existencia": "9"
        },
        "76698": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "24",
            "ID_Ubic": "15150",
            "SKU_PRODUCTO": "76698",
            "Inventario_Existencia": "489"
        },
        "5195": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "13",
            "ID_Ubic": "15095",
            "SKU_PRODUCTO": "5195",
            "Inventario_Existencia": "3"
        },
        "9175": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "13",
            "ID_Ubic": "15095",
            "SKU_PRODUCTO": "9175",
            "Inventario_Existencia": "1"
        },
        "16636": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "13",
            "ID_Ubic": "15095",
            "SKU_PRODUCTO": "16636",
            "Inventario_Existencia": "3"
        },
        "27544": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "16",
            "ID_Ubic": "15110",
            "SKU_PRODUCTO": "27544",
            "Inventario_Existencia": "2"
        },
        "73231": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "13",
            "ID_Ubic": "15095",
            "SKU_PRODUCTO": "73231",
            "Inventario_Existencia": "1"
        },
        "76711": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "47",
            "ID_Ubic": "18145",
            "SKU_PRODUCTO": "76711",
            "Inventario_Existencia": "1099"
        },
        "76724": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "59",
            "ID_Ubic": "107775",
            "SKU_PRODUCTO": "76724",
            "Inventario_Existencia": "184"
        },
        "1416": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "15",
            "ID_Ubic": "15105",
            "SKU_PRODUCTO": "1416",
            "Inventario_Existencia": "2"
        },
        "7358": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "15",
            "ID_Ubic": "15105",
            "SKU_PRODUCTO": "7358",
            "Inventario_Existencia": "4"
        },
        "29878": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "15",
            "ID_Ubic": "15105",
            "SKU_PRODUCTO": "29878",
            "Inventario_Existencia": "1"
        },
        "73507": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "15",
            "ID_Ubic": "15105",
            "SKU_PRODUCTO": "73507",
            "Inventario_Existencia": "2"
        },
        "74097": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "15",
            "ID_Ubic": "15105",
            "SKU_PRODUCTO": "74097",
            "Inventario_Existencia": "2"
        },
        "74098": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "15",
            "ID_Ubic": "15105",
            "SKU_PRODUCTO": "74098",
            "Inventario_Existencia": "2"
        },
        "74099": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "15",
            "ID_Ubic": "15105",
            "SKU_PRODUCTO": "74099",
            "Inventario_Existencia": "2"
        },
        "754": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "16",
            "ID_Ubic": "15110",
            "SKU_PRODUCTO": "754",
            "Inventario_Existencia": "3"
        },
        "756": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "16",
            "ID_Ubic": "15110",
            "SKU_PRODUCTO": "756",
            "Inventario_Existencia": "2"
        },
        "16606": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "16",
            "ID_Ubic": "15110",
            "SKU_PRODUCTO": "16606",
            "Inventario_Existencia": "3"
        },
        "16609": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "16",
            "ID_Ubic": "15110",
            "SKU_PRODUCTO": "16609",
            "Inventario_Existencia": "1"
        },
        "71999": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "36",
            "ID_Ubic": "15210",
            "SKU_PRODUCTO": "71999",
            "Inventario_Existencia": "50"
        },
        "76692": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "16",
            "ID_Ubic": "15110",
            "SKU_PRODUCTO": "76692",
            "Inventario_Existencia": "528"
        },
        "16605": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "17",
            "ID_Ubic": "15115",
            "SKU_PRODUCTO": "16605",
            "Inventario_Existencia": "5"
        },
        "22188": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "17",
            "ID_Ubic": "15115",
            "SKU_PRODUCTO": "22188",
            "Inventario_Existencia": "1"
        },
        "76194": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "17",
            "ID_Ubic": "15115",
            "SKU_PRODUCTO": "76194",
            "Inventario_Existencia": "1"
        },
        "7364": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "31",
            "ID_Ubic": "15185",
            "SKU_PRODUCTO": "7364",
            "Inventario_Existencia": "4"
        },
        "29768": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "35",
            "ID_Ubic": "18085",
            "SKU_PRODUCTO": "29768",
            "Inventario_Existencia": "4"
        },
        "76690": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "20",
            "ID_Ubic": "15130",
            "SKU_PRODUCTO": "76690",
            "Inventario_Existencia": "155"
        },
        "76696": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "57",
            "ID_Ubic": "107765",
            "SKU_PRODUCTO": "76696",
            "Inventario_Existencia": "12"
        },
        "76705": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "43",
            "ID_Ubic": "18125",
            "SKU_PRODUCTO": "76705",
            "Inventario_Existencia": "361"
        },
        "7367": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "21",
            "ID_Ubic": "15135",
            "SKU_PRODUCTO": "7367",
            "Inventario_Existencia": "7"
        },
        "10757": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "21",
            "ID_Ubic": "15135",
            "SKU_PRODUCTO": "10757",
            "Inventario_Existencia": "3"
        },
        "28815": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "21",
            "ID_Ubic": "15135",
            "SKU_PRODUCTO": "28815",
            "Inventario_Existencia": "1"
        },
        "76691": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "22",
            "ID_Ubic": "15140",
            "SKU_PRODUCTO": "76691",
            "Inventario_Existencia": "890"
        },
        "1417": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "23",
            "ID_Ubic": "15145",
            "SKU_PRODUCTO": "1417",
            "Inventario_Existencia": "1"
        },
        "1421": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "23",
            "ID_Ubic": "15145",
            "SKU_PRODUCTO": "1421",
            "Inventario_Existencia": "1"
        },
        "71377": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "23",
            "ID_Ubic": "15145",
            "SKU_PRODUCTO": "71377",
            "Inventario_Existencia": "2"
        },
        "71575": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "23",
            "ID_Ubic": "15145",
            "SKU_PRODUCTO": "71575",
            "Inventario_Existencia": "1"
        },
        "72096": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "23",
            "ID_Ubic": "15145",
            "SKU_PRODUCTO": "72096",
            "Inventario_Existencia": "2"
        },
        "6943": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "27",
            "ID_Ubic": "15165",
            "SKU_PRODUCTO": "6943",
            "Inventario_Existencia": "10"
        },
        "8377": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "27",
            "ID_Ubic": "15165",
            "SKU_PRODUCTO": "8377",
            "Inventario_Existencia": "300"
        },
        "9037": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "27",
            "ID_Ubic": "15165",
            "SKU_PRODUCTO": "9037",
            "Inventario_Existencia": "10"
        },
        "27075": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "27",
            "ID_Ubic": "15165",
            "SKU_PRODUCTO": "27075",
            "Inventario_Existencia": "10"
        },
        "4796": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "28",
            "ID_Ubic": "15170",
            "SKU_PRODUCTO": "4796",
            "Inventario_Existencia": "50"
        },
        "15235": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "28",
            "ID_Ubic": "15170",
            "SKU_PRODUCTO": "15235",
            "Inventario_Existencia": "50"
        },
        "32753": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "28",
            "ID_Ubic": "15170",
            "SKU_PRODUCTO": "32753",
            "Inventario_Existencia": "400"
        },
        "35203": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "46",
            "ID_Ubic": "15260",
            "SKU_PRODUCTO": "35203",
            "Inventario_Existencia": "60"
        },
        "2272": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "29",
            "ID_Ubic": "15175",
            "SKU_PRODUCTO": "2272",
            "Inventario_Existencia": "1"
        },
        "5281": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "29",
            "ID_Ubic": "15175",
            "SKU_PRODUCTO": "5281",
            "Inventario_Existencia": "5"
        },
        "6765": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "29",
            "ID_Ubic": "15175",
            "SKU_PRODUCTO": "6765",
            "Inventario_Existencia": "4"
        },
        "6766": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "29",
            "ID_Ubic": "15175",
            "SKU_PRODUCTO": "6766",
            "Inventario_Existencia": "4"
        },
        "16743": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "30",
            "ID_Ubic": "15180",
            "SKU_PRODUCTO": "16743",
            "Inventario_Existencia": "150"
        },
        "29840": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "29",
            "ID_Ubic": "15175",
            "SKU_PRODUCTO": "29840",
            "Inventario_Existencia": "20"
        },
        "2922": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "30",
            "ID_Ubic": "15180",
            "SKU_PRODUCTO": "2922",
            "Inventario_Existencia": "150"
        },
        "3962": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "30",
            "ID_Ubic": "15180",
            "SKU_PRODUCTO": "3962",
            "Inventario_Existencia": "50"
        },
        "4215": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "30",
            "ID_Ubic": "15180",
            "SKU_PRODUCTO": "4215",
            "Inventario_Existencia": "250"
        },
        "8735": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "42",
            "ID_Ubic": "15240",
            "SKU_PRODUCTO": "8735",
            "Inventario_Existencia": "250"
        },
        "8737": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "30",
            "ID_Ubic": "15180",
            "SKU_PRODUCTO": "8737",
            "Inventario_Existencia": "250"
        },
        "11089": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "30",
            "ID_Ubic": "15180",
            "SKU_PRODUCTO": "11089",
            "Inventario_Existencia": "50"
        },
        "13133": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "30",
            "ID_Ubic": "15180",
            "SKU_PRODUCTO": "13133",
            "Inventario_Existencia": "100"
        },
        "23806": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "30",
            "ID_Ubic": "15180",
            "SKU_PRODUCTO": "23806",
            "Inventario_Existencia": "150"
        },
        "7359": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "31",
            "ID_Ubic": "15185",
            "SKU_PRODUCTO": "7359",
            "Inventario_Existencia": "1"
        },
        "7361": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "31",
            "ID_Ubic": "15185",
            "SKU_PRODUCTO": "7361",
            "Inventario_Existencia": "3"
        },
        "15257": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "32",
            "ID_Ubic": "15190",
            "SKU_PRODUCTO": "15257",
            "Inventario_Existencia": "50"
        },
        "28285": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "32",
            "ID_Ubic": "15190",
            "SKU_PRODUCTO": "28285",
            "Inventario_Existencia": "15"
        },
        "3532": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "33",
            "ID_Ubic": "15195",
            "SKU_PRODUCTO": "3532",
            "Inventario_Existencia": "10"
        },
        "6288": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "33",
            "ID_Ubic": "15195",
            "SKU_PRODUCTO": "6288",
            "Inventario_Existencia": "150"
        },
        "72460": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "67",
            "ID_Ubic": "105880",
            "SKU_PRODUCTO": "72460",
            "Inventario_Existencia": "2"
        },
        "72461": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "53",
            "ID_Ubic": "100860",
            "SKU_PRODUCTO": "72461",
            "Inventario_Existencia": "6"
        },
        "72463": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "57",
            "ID_Ubic": "105830",
            "SKU_PRODUCTO": "72463",
            "Inventario_Existencia": "16"
        },
        "72464": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "55",
            "ID_Ubic": "100870",
            "SKU_PRODUCTO": "72464",
            "Inventario_Existencia": "12"
        },
        "72467": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "67",
            "ID_Ubic": "105880",
            "SKU_PRODUCTO": "72467",
            "Inventario_Existencia": "8"
        },
        "72849": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "67",
            "ID_Ubic": "105880",
            "SKU_PRODUCTO": "72849",
            "Inventario_Existencia": "8"
        },
        "72850": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "34",
            "ID_Ubic": "15200",
            "SKU_PRODUCTO": "72850",
            "Inventario_Existencia": "4"
        },
        "72852": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "49",
            "ID_Ubic": "100840",
            "SKU_PRODUCTO": "72852",
            "Inventario_Existencia": "36"
        },
        "73592": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "34",
            "ID_Ubic": "15200",
            "SKU_PRODUCTO": "73592",
            "Inventario_Existencia": "500"
        },
        "74473": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "34",
            "ID_Ubic": "15200",
            "SKU_PRODUCTO": "74473",
            "Inventario_Existencia": "10"
        },
        "74474": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "34",
            "ID_Ubic": "15200",
            "SKU_PRODUCTO": "74474",
            "Inventario_Existencia": "15"
        },
        "15630": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "35",
            "ID_Ubic": "15205",
            "SKU_PRODUCTO": "15630",
            "Inventario_Existencia": "500"
        },
        "16616": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "35",
            "ID_Ubic": "15205",
            "SKU_PRODUCTO": "16616",
            "Inventario_Existencia": "200"
        },
        "30082": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "35",
            "ID_Ubic": "15205",
            "SKU_PRODUCTO": "30082",
            "Inventario_Existencia": "3000"
        },
        "15688": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "15688",
            "Inventario_Existencia": "200"
        },
        "10041": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "37",
            "ID_Ubic": "15215",
            "SKU_PRODUCTO": "10041",
            "Inventario_Existencia": "500"
        },
        "10042": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "37",
            "ID_Ubic": "15215",
            "SKU_PRODUCTO": "10042",
            "Inventario_Existencia": "500"
        },
        "21211": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "37",
            "ID_Ubic": "15215",
            "SKU_PRODUCTO": "21211",
            "Inventario_Existencia": "1300"
        },
        "73678": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "37",
            "ID_Ubic": "15215",
            "SKU_PRODUCTO": "73678",
            "Inventario_Existencia": "25"
        },
        "5166": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "38",
            "ID_Ubic": "15220",
            "SKU_PRODUCTO": "5166",
            "Inventario_Existencia": "400"
        },
        "7193": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "38",
            "ID_Ubic": "15220",
            "SKU_PRODUCTO": "7193",
            "Inventario_Existencia": "2000"
        },
        "13375": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "38",
            "ID_Ubic": "15220",
            "SKU_PRODUCTO": "13375",
            "Inventario_Existencia": "30"
        },
        "17103": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "38",
            "ID_Ubic": "15220",
            "SKU_PRODUCTO": "17103",
            "Inventario_Existencia": "50"
        },
        "34108": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "38",
            "ID_Ubic": "15220",
            "SKU_PRODUCTO": "34108",
            "Inventario_Existencia": "1000"
        },
        "73178": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "38",
            "ID_Ubic": "15220",
            "SKU_PRODUCTO": "73178",
            "Inventario_Existencia": "400"
        },
        "73540": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "38",
            "ID_Ubic": "15220",
            "SKU_PRODUCTO": "73540",
            "Inventario_Existencia": "100"
        },
        "1918": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "39",
            "ID_Ubic": "15225",
            "SKU_PRODUCTO": "1918",
            "Inventario_Existencia": "1500"
        },
        "12347": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "39",
            "ID_Ubic": "15225",
            "SKU_PRODUCTO": "12347",
            "Inventario_Existencia": "1500"
        },
        "16598": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "39",
            "ID_Ubic": "15225",
            "SKU_PRODUCTO": "16598",
            "Inventario_Existencia": "50"
        },
        "20397": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "39",
            "ID_Ubic": "15225",
            "SKU_PRODUCTO": "20397",
            "Inventario_Existencia": "2"
        },
        "23858": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "39",
            "ID_Ubic": "15225",
            "SKU_PRODUCTO": "23858",
            "Inventario_Existencia": "500"
        },
        "26286": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "39",
            "ID_Ubic": "15225",
            "SKU_PRODUCTO": "26286",
            "Inventario_Existencia": "50"
        },
        "73466": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "39",
            "ID_Ubic": "15225",
            "SKU_PRODUCTO": "73466",
            "Inventario_Existencia": "150"
        },
        "657": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "40",
            "ID_Ubic": "15230",
            "SKU_PRODUCTO": "657",
            "Inventario_Existencia": "10"
        },
        "4208": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "40",
            "ID_Ubic": "15230",
            "SKU_PRODUCTO": "4208",
            "Inventario_Existencia": "1000"
        },
        "5870": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "40",
            "ID_Ubic": "15230",
            "SKU_PRODUCTO": "5870",
            "Inventario_Existencia": "36"
        },
        "29995": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "40",
            "ID_Ubic": "15230",
            "SKU_PRODUCTO": "29995",
            "Inventario_Existencia": "8000"
        },
        "210": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "41",
            "ID_Ubic": "15235",
            "SKU_PRODUCTO": "210",
            "Inventario_Existencia": "5000"
        },
        "219": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "41",
            "ID_Ubic": "15235",
            "SKU_PRODUCTO": "219",
            "Inventario_Existencia": "14500"
        },
        "357": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "41",
            "ID_Ubic": "15235",
            "SKU_PRODUCTO": "357",
            "Inventario_Existencia": "3000"
        },
        "3527": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "41",
            "ID_Ubic": "15235",
            "SKU_PRODUCTO": "3527",
            "Inventario_Existencia": "20"
        },
        "3875": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "41",
            "ID_Ubic": "15235",
            "SKU_PRODUCTO": "3875",
            "Inventario_Existencia": "800"
        },
        "7838": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "41",
            "ID_Ubic": "15235",
            "SKU_PRODUCTO": "7838",
            "Inventario_Existencia": "250"
        },
        "4521": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "42",
            "ID_Ubic": "15240",
            "SKU_PRODUCTO": "4521",
            "Inventario_Existencia": "4"
        },
        "6446": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "42",
            "ID_Ubic": "15240",
            "SKU_PRODUCTO": "6446",
            "Inventario_Existencia": "400"
        },
        "8570": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "42",
            "ID_Ubic": "15240",
            "SKU_PRODUCTO": "8570",
            "Inventario_Existencia": "250"
        },
        "8708": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "42",
            "ID_Ubic": "15240",
            "SKU_PRODUCTO": "8708",
            "Inventario_Existencia": "2"
        },
        "9436": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "42",
            "ID_Ubic": "15240",
            "SKU_PRODUCTO": "9436",
            "Inventario_Existencia": "250"
        },
        "17105": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "42",
            "ID_Ubic": "15240",
            "SKU_PRODUCTO": "17105",
            "Inventario_Existencia": "250"
        },
        "19602": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "42",
            "ID_Ubic": "15240",
            "SKU_PRODUCTO": "19602",
            "Inventario_Existencia": "6"
        },
        "20810": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "42",
            "ID_Ubic": "15240",
            "SKU_PRODUCTO": "20810",
            "Inventario_Existencia": "2"
        },
        "4194": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "43",
            "ID_Ubic": "15245",
            "SKU_PRODUCTO": "4194",
            "Inventario_Existencia": "250"
        },
        "8174": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "47",
            "ID_Ubic": "15265",
            "SKU_PRODUCTO": "8174",
            "Inventario_Existencia": "25"
        },
        "14220": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "43",
            "ID_Ubic": "15245",
            "SKU_PRODUCTO": "14220",
            "Inventario_Existencia": "200"
        },
        "18022": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "43",
            "ID_Ubic": "15245",
            "SKU_PRODUCTO": "18022",
            "Inventario_Existencia": "50"
        },
        "26965": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "43",
            "ID_Ubic": "15245",
            "SKU_PRODUCTO": "26965",
            "Inventario_Existencia": "1000"
        },
        "28166": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "43",
            "ID_Ubic": "15245",
            "SKU_PRODUCTO": "28166",
            "Inventario_Existencia": "1000"
        },
        "28830": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "43",
            "ID_Ubic": "15245",
            "SKU_PRODUCTO": "28830",
            "Inventario_Existencia": "500"
        },
        "28933": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "43",
            "ID_Ubic": "15245",
            "SKU_PRODUCTO": "28933",
            "Inventario_Existencia": "1000"
        },
        "70249": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "43",
            "ID_Ubic": "15245",
            "SKU_PRODUCTO": "70249",
            "Inventario_Existencia": "24"
        },
        "73578": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "43",
            "ID_Ubic": "15245",
            "SKU_PRODUCTO": "73578",
            "Inventario_Existencia": "400"
        },
        "159": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "44",
            "ID_Ubic": "15250",
            "SKU_PRODUCTO": "159",
            "Inventario_Existencia": "20"
        },
        "1575": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "44",
            "ID_Ubic": "15250",
            "SKU_PRODUCTO": "1575",
            "Inventario_Existencia": "50"
        },
        "4597": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "47",
            "ID_Ubic": "15265",
            "SKU_PRODUCTO": "4597",
            "Inventario_Existencia": "500"
        },
        "4625": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "47",
            "ID_Ubic": "15265",
            "SKU_PRODUCTO": "4625",
            "Inventario_Existencia": "500"
        },
        "4657": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "47",
            "ID_Ubic": "15265",
            "SKU_PRODUCTO": "4657",
            "Inventario_Existencia": "500"
        },
        "4968": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "44",
            "ID_Ubic": "15250",
            "SKU_PRODUCTO": "4968",
            "Inventario_Existencia": "50"
        },
        "9563": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "44",
            "ID_Ubic": "15250",
            "SKU_PRODUCTO": "9563",
            "Inventario_Existencia": "50"
        },
        "19099": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "44",
            "ID_Ubic": "15250",
            "SKU_PRODUCTO": "19099",
            "Inventario_Existencia": "40"
        },
        "25133": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "44",
            "ID_Ubic": "15250",
            "SKU_PRODUCTO": "25133",
            "Inventario_Existencia": "40"
        },
        "76848": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "44",
            "ID_Ubic": "15250",
            "SKU_PRODUCTO": "76848",
            "Inventario_Existencia": "5"
        },
        "76849": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "44",
            "ID_Ubic": "15250",
            "SKU_PRODUCTO": "76849",
            "Inventario_Existencia": "5"
        },
        "76850": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "44",
            "ID_Ubic": "15250",
            "SKU_PRODUCTO": "76850",
            "Inventario_Existencia": "5"
        },
        "76851": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "44",
            "ID_Ubic": "15250",
            "SKU_PRODUCTO": "76851",
            "Inventario_Existencia": "5"
        },
        "76852": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "44",
            "ID_Ubic": "15250",
            "SKU_PRODUCTO": "76852",
            "Inventario_Existencia": "5"
        },
        "3206": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "45",
            "ID_Ubic": "15255",
            "SKU_PRODUCTO": "3206",
            "Inventario_Existencia": "450"
        },
        "4112": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "45",
            "ID_Ubic": "15255",
            "SKU_PRODUCTO": "4112",
            "Inventario_Existencia": "250"
        },
        "30143": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "45",
            "ID_Ubic": "15255",
            "SKU_PRODUCTO": "30143",
            "Inventario_Existencia": "1000"
        },
        "3170": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "46",
            "ID_Ubic": "15260",
            "SKU_PRODUCTO": "3170",
            "Inventario_Existencia": "600"
        },
        "3291": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "46",
            "ID_Ubic": "15260",
            "SKU_PRODUCTO": "3291",
            "Inventario_Existencia": "1000"
        },
        "3934": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "46",
            "ID_Ubic": "15260",
            "SKU_PRODUCTO": "3934",
            "Inventario_Existencia": "100"
        },
        "16387": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "46",
            "ID_Ubic": "15260",
            "SKU_PRODUCTO": "16387",
            "Inventario_Existencia": "20"
        },
        "32750": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "47",
            "ID_Ubic": "15265",
            "SKU_PRODUCTO": "32750",
            "Inventario_Existencia": "300"
        },
        "32755": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "46",
            "ID_Ubic": "15260",
            "SKU_PRODUCTO": "32755",
            "Inventario_Existencia": "100"
        },
        "491": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "47",
            "ID_Ubic": "15265",
            "SKU_PRODUCTO": "491",
            "Inventario_Existencia": "100"
        },
        "4098": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "47",
            "ID_Ubic": "15265",
            "SKU_PRODUCTO": "4098",
            "Inventario_Existencia": "200"
        },
        "5001": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "47",
            "ID_Ubic": "15265",
            "SKU_PRODUCTO": "5001",
            "Inventario_Existencia": "260"
        },
        "10532": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "47",
            "ID_Ubic": "15265",
            "SKU_PRODUCTO": "10532",
            "Inventario_Existencia": "10"
        },
        "29843": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "47",
            "ID_Ubic": "15265",
            "SKU_PRODUCTO": "29843",
            "Inventario_Existencia": "10"
        },
        "9677": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "48",
            "ID_Ubic": "15270",
            "SKU_PRODUCTO": "9677",
            "Inventario_Existencia": "150"
        },
        "10820": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "48",
            "ID_Ubic": "15270",
            "SKU_PRODUCTO": "10820",
            "Inventario_Existencia": "250"
        },
        "16595": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "48",
            "ID_Ubic": "15270",
            "SKU_PRODUCTO": "16595",
            "Inventario_Existencia": "500"
        },
        "74597": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "48",
            "ID_Ubic": "15270",
            "SKU_PRODUCTO": "74597",
            "Inventario_Existencia": "1515"
        },
        "72950": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "1",
            "ID_Ubic": "16475",
            "SKU_PRODUCTO": "72950",
            "Inventario_Existencia": "2550"
        },
        "72959": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "4",
            "ID_Ubic": "16490",
            "SKU_PRODUCTO": "72959",
            "Inventario_Existencia": "3714"
        },
        "72956": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "5",
            "ID_Ubic": "16495",
            "SKU_PRODUCTO": "72956",
            "Inventario_Existencia": "520"
        },
        "72953": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "6",
            "ID_Ubic": "16500",
            "SKU_PRODUCTO": "72953",
            "Inventario_Existencia": "2110"
        },
        "72958": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "7",
            "ID_Ubic": "16505",
            "SKU_PRODUCTO": "72958",
            "Inventario_Existencia": "2528"
        },
        "72954": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "8",
            "ID_Ubic": "16510",
            "SKU_PRODUCTO": "72954",
            "Inventario_Existencia": "3650"
        },
        "72955": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "9",
            "ID_Ubic": "16515",
            "SKU_PRODUCTO": "72955",
            "Inventario_Existencia": "1960"
        },
        "72952": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "10",
            "ID_Ubic": "16520",
            "SKU_PRODUCTO": "72952",
            "Inventario_Existencia": "2960"
        },
        "72957": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "11",
            "ID_Ubic": "16525",
            "SKU_PRODUCTO": "72957",
            "Inventario_Existencia": "280"
        },
        "70203": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "12",
            "ID_Ubic": "16530",
            "SKU_PRODUCTO": "70203",
            "Inventario_Existencia": "393"
        },
        "70213": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "13",
            "ID_Ubic": "16535",
            "SKU_PRODUCTO": "70213",
            "Inventario_Existencia": "795"
        },
        "70212": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "14",
            "ID_Ubic": "16540",
            "SKU_PRODUCTO": "70212",
            "Inventario_Existencia": "105"
        },
        "70210": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "15",
            "ID_Ubic": "16545",
            "SKU_PRODUCTO": "70210",
            "Inventario_Existencia": "200"
        },
        "72271": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "16",
            "ID_Ubic": "16550",
            "SKU_PRODUCTO": "72271",
            "Inventario_Existencia": "80"
        },
        "70201": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "18",
            "ID_Ubic": "16560",
            "SKU_PRODUCTO": "70201",
            "Inventario_Existencia": "390"
        },
        "70206": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "19",
            "ID_Ubic": "16565",
            "SKU_PRODUCTO": "70206",
            "Inventario_Existencia": "480"
        },
        "70211": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "20",
            "ID_Ubic": "16570",
            "SKU_PRODUCTO": "70211",
            "Inventario_Existencia": "70"
        },
        "70204": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "21",
            "ID_Ubic": "16575",
            "SKU_PRODUCTO": "70204",
            "Inventario_Existencia": "860"
        },
        "70012": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "22",
            "ID_Ubic": "16580",
            "SKU_PRODUCTO": "70012",
            "Inventario_Existencia": "290"
        },
        "70208": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "23",
            "ID_Ubic": "16585",
            "SKU_PRODUCTO": "70208",
            "Inventario_Existencia": "830"
        },
        "70214": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "24",
            "ID_Ubic": "16590",
            "SKU_PRODUCTO": "70214",
            "Inventario_Existencia": "185"
        },
        "75009": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "19",
            "ID_Ubic": "18005",
            "SKU_PRODUCTO": "75009",
            "Inventario_Existencia": "15"
        },
        "75024": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "28",
            "ID_Ubic": "16610",
            "SKU_PRODUCTO": "75024",
            "Inventario_Existencia": "867"
        },
        "75567": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "29",
            "ID_Ubic": "16615",
            "SKU_PRODUCTO": "75567",
            "Inventario_Existencia": "145"
        },
        "75018": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "36",
            "ID_Ubic": "18090",
            "SKU_PRODUCTO": "75018",
            "Inventario_Existencia": "12"
        },
        "75019": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "31",
            "ID_Ubic": "16625",
            "SKU_PRODUCTO": "75019",
            "Inventario_Existencia": "4149"
        },
        "75030": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "33",
            "ID_Ubic": "16635",
            "SKU_PRODUCTO": "75030",
            "Inventario_Existencia": "1546"
        },
        "75561": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "34",
            "ID_Ubic": "16640",
            "SKU_PRODUCTO": "75561",
            "Inventario_Existencia": "51"
        },
        "75543": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "40",
            "ID_Ubic": "16670",
            "SKU_PRODUCTO": "75543",
            "Inventario_Existencia": "20"
        },
        "73172": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "36",
            "ID_Ubic": "16650",
            "SKU_PRODUCTO": "73172",
            "Inventario_Existencia": "26700"
        },
        "75509": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "37",
            "ID_Ubic": "16655",
            "SKU_PRODUCTO": "75509",
            "Inventario_Existencia": "779"
        },
        "8567": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "38",
            "ID_Ubic": "16660",
            "SKU_PRODUCTO": "8567",
            "Inventario_Existencia": "3"
        },
        "16604": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "38",
            "ID_Ubic": "16660",
            "SKU_PRODUCTO": "16604",
            "Inventario_Existencia": "1"
        },
        "71948": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "38",
            "ID_Ubic": "16660",
            "SKU_PRODUCTO": "71948",
            "Inventario_Existencia": "2"
        },
        "75565": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "18",
            "ID_Ubic": "30150",
            "SKU_PRODUCTO": "75565",
            "Inventario_Existencia": "4"
        },
        "75572": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "41",
            "ID_Ubic": "16675",
            "SKU_PRODUCTO": "75572",
            "Inventario_Existencia": "144"
        },
        "2569": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "44",
            "ID_Ubic": "18130",
            "SKU_PRODUCTO": "2569",
            "Inventario_Existencia": "3"
        },
        "2659": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "67",
            "ID_Ubic": "106557",
            "SKU_PRODUCTO": "2659",
            "Inventario_Existencia": "5"
        },
        "29766": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "44",
            "ID_Ubic": "18130",
            "SKU_PRODUCTO": "29766",
            "Inventario_Existencia": "1"
        },
        "75013": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "43",
            "ID_Ubic": "16685",
            "SKU_PRODUCTO": "75013",
            "Inventario_Existencia": "1444"
        },
        "75537": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "44",
            "ID_Ubic": "16690",
            "SKU_PRODUCTO": "75537",
            "Inventario_Existencia": "7"
        },
        "75536": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "45",
            "ID_Ubic": "16695",
            "SKU_PRODUCTO": "75536",
            "Inventario_Existencia": "142"
        },
        "75515": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "36",
            "ID_Ubic": "18090",
            "SKU_PRODUCTO": "75515",
            "Inventario_Existencia": "6"
        },
        "73395": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "1",
            "ID_Ubic": "17915",
            "SKU_PRODUCTO": "73395",
            "Inventario_Existencia": "6950"
        },
        "70262": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "2",
            "ID_Ubic": "17920",
            "SKU_PRODUCTO": "70262",
            "Inventario_Existencia": "3725"
        },
        "73766": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "3",
            "ID_Ubic": "17925",
            "SKU_PRODUCTO": "73766",
            "Inventario_Existencia": "4425"
        },
        "70265": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "4",
            "ID_Ubic": "17930",
            "SKU_PRODUCTO": "70265",
            "Inventario_Existencia": "2250"
        },
        "70261": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "5",
            "ID_Ubic": "17935",
            "SKU_PRODUCTO": "70261",
            "Inventario_Existencia": "2800"
        },
        "70260": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "6",
            "ID_Ubic": "17940",
            "SKU_PRODUCTO": "70260",
            "Inventario_Existencia": "4800"
        },
        "76603": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "42",
            "ID_Ubic": "18120",
            "SKU_PRODUCTO": "76603",
            "Inventario_Existencia": "2000"
        },
        "70267": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "8",
            "ID_Ubic": "17950",
            "SKU_PRODUCTO": "70267",
            "Inventario_Existencia": "975"
        },
        "73763": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "9",
            "ID_Ubic": "17955",
            "SKU_PRODUCTO": "73763",
            "Inventario_Existencia": "2775"
        },
        "76600": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "42",
            "ID_Ubic": "18120",
            "SKU_PRODUCTO": "76600",
            "Inventario_Existencia": "2000"
        },
        "74650": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "62",
            "ID_Ubic": "107610",
            "SKU_PRODUCTO": "74650",
            "Inventario_Existencia": "24000"
        },
        "74819": {
            "Nombre_Pasillo": "D2",
            "X": "18",
            "Y": "61",
            "ID_Ubic": "107605",
            "SKU_PRODUCTO": "74819",
            "Inventario_Existencia": "22700"
        },
        "4533": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "13",
            "ID_Ubic": "17975",
            "SKU_PRODUCTO": "4533",
            "Inventario_Existencia": "500"
        },
        "16690": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "13",
            "ID_Ubic": "17975",
            "SKU_PRODUCTO": "16690",
            "Inventario_Existencia": "250"
        },
        "73758": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "13",
            "ID_Ubic": "17975",
            "SKU_PRODUCTO": "73758",
            "Inventario_Existencia": "1000"
        },
        "72591": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "14",
            "ID_Ubic": "17980",
            "SKU_PRODUCTO": "72591",
            "Inventario_Existencia": "13250"
        },
        "71514": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "15",
            "ID_Ubic": "17985",
            "SKU_PRODUCTO": "71514",
            "Inventario_Existencia": "53"
        },
        "73586": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "22",
            "ID_Ubic": "18020",
            "SKU_PRODUCTO": "73586",
            "Inventario_Existencia": "17200"
        },
        "899": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "16",
            "ID_Ubic": "17990",
            "SKU_PRODUCTO": "899",
            "Inventario_Existencia": "400"
        },
        "2843": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "17",
            "ID_Ubic": "17995",
            "SKU_PRODUCTO": "2843",
            "Inventario_Existencia": "500"
        },
        "14497": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "17",
            "ID_Ubic": "17995",
            "SKU_PRODUCTO": "14497",
            "Inventario_Existencia": "3500"
        },
        "73664": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "18",
            "ID_Ubic": "18000",
            "SKU_PRODUCTO": "73664",
            "Inventario_Existencia": "48"
        },
        "23337": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "19",
            "ID_Ubic": "18005",
            "SKU_PRODUCTO": "23337",
            "Inventario_Existencia": "27"
        },
        "75547": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "19",
            "ID_Ubic": "18005",
            "SKU_PRODUCTO": "75547",
            "Inventario_Existencia": "12"
        },
        "21486": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "20",
            "ID_Ubic": "18010",
            "SKU_PRODUCTO": "21486",
            "Inventario_Existencia": "4000"
        },
        "29990": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "20",
            "ID_Ubic": "18010",
            "SKU_PRODUCTO": "29990",
            "Inventario_Existencia": "3300"
        },
        "73757": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "20",
            "ID_Ubic": "18010",
            "SKU_PRODUCTO": "73757",
            "Inventario_Existencia": "250"
        },
        "3450": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "24",
            "ID_Ubic": "18030",
            "SKU_PRODUCTO": "3450",
            "Inventario_Existencia": "4000"
        },
        "73735": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "2",
            "ID_Ubic": "30134",
            "SKU_PRODUCTO": "73735",
            "Inventario_Existencia": "200"
        },
        "6690": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "28",
            "ID_Ubic": "18050",
            "SKU_PRODUCTO": "6690",
            "Inventario_Existencia": "1"
        },
        "73676": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "28",
            "ID_Ubic": "18050",
            "SKU_PRODUCTO": "73676",
            "Inventario_Existencia": "22"
        },
        "2590": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "67",
            "ID_Ubic": "106557",
            "SKU_PRODUCTO": "2590",
            "Inventario_Existencia": "7"
        },
        "75573": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "31",
            "ID_Ubic": "18065",
            "SKU_PRODUCTO": "75573",
            "Inventario_Existencia": "1389"
        },
        "76602": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "31",
            "ID_Ubic": "18065",
            "SKU_PRODUCTO": "76602",
            "Inventario_Existencia": "1450"
        },
        "1": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "32",
            "ID_Ubic": "18070",
            "SKU_PRODUCTO": "1",
            "Inventario_Existencia": "1"
        },
        "732": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "32",
            "ID_Ubic": "18070",
            "SKU_PRODUCTO": "732",
            "Inventario_Existencia": "100"
        },
        "2054": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "32",
            "ID_Ubic": "18070",
            "SKU_PRODUCTO": "2054",
            "Inventario_Existencia": "15"
        },
        "2612": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "32",
            "ID_Ubic": "18070",
            "SKU_PRODUCTO": "2612",
            "Inventario_Existencia": "99"
        },
        "120320": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "32",
            "ID_Ubic": "18070",
            "SKU_PRODUCTO": "120320",
            "Inventario_Existencia": "1"
        },
        "120553": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "32",
            "ID_Ubic": "18070",
            "SKU_PRODUCTO": "120553",
            "Inventario_Existencia": "1"
        },
        "20651": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "32",
            "ID_Ubic": "18070",
            "SKU_PRODUCTO": "20651",
            "Inventario_Existencia": "110"
        },
        "22844": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "32",
            "ID_Ubic": "18070",
            "SKU_PRODUCTO": "22844",
            "Inventario_Existencia": "500"
        },
        "70841": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "32",
            "ID_Ubic": "18070",
            "SKU_PRODUCTO": "70841",
            "Inventario_Existencia": "2400"
        },
        "73308": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "32",
            "ID_Ubic": "18070",
            "SKU_PRODUCTO": "73308",
            "Inventario_Existencia": "1"
        },
        "74060": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "32",
            "ID_Ubic": "18070",
            "SKU_PRODUCTO": "74060",
            "Inventario_Existencia": "500"
        },
        "2621": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "48",
            "ID_Ubic": "18150",
            "SKU_PRODUCTO": "2621",
            "Inventario_Existencia": "10"
        },
        "1941": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "35",
            "ID_Ubic": "18085",
            "SKU_PRODUCTO": "1941",
            "Inventario_Existencia": "40"
        },
        "74378": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "35",
            "ID_Ubic": "18085",
            "SKU_PRODUCTO": "74378",
            "Inventario_Existencia": "28"
        },
        "75005": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "20",
            "ID_Ubic": "30152",
            "SKU_PRODUCTO": "75005",
            "Inventario_Existencia": "582"
        },
        "75006": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "36",
            "ID_Ubic": "18090",
            "SKU_PRODUCTO": "75006",
            "Inventario_Existencia": "12"
        },
        "75007": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "36",
            "ID_Ubic": "18090",
            "SKU_PRODUCTO": "75007",
            "Inventario_Existencia": "12"
        },
        "75016": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "36",
            "ID_Ubic": "18090",
            "SKU_PRODUCTO": "75016",
            "Inventario_Existencia": "54"
        },
        "75017": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "36",
            "ID_Ubic": "18090",
            "SKU_PRODUCTO": "75017",
            "Inventario_Existencia": "59"
        },
        "75027": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "36",
            "ID_Ubic": "18090",
            "SKU_PRODUCTO": "75027",
            "Inventario_Existencia": "6"
        },
        "75500": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "36",
            "ID_Ubic": "18090",
            "SKU_PRODUCTO": "75500",
            "Inventario_Existencia": "12"
        },
        "75512": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "36",
            "ID_Ubic": "18090",
            "SKU_PRODUCTO": "75512",
            "Inventario_Existencia": "36"
        },
        "75520": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "36",
            "ID_Ubic": "18090",
            "SKU_PRODUCTO": "75520",
            "Inventario_Existencia": "12"
        },
        "75523": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "36",
            "ID_Ubic": "18090",
            "SKU_PRODUCTO": "75523",
            "Inventario_Existencia": "6"
        },
        "75532": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "36",
            "ID_Ubic": "18090",
            "SKU_PRODUCTO": "75532",
            "Inventario_Existencia": "30"
        },
        "100600": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "40",
            "ID_Ubic": "18110",
            "SKU_PRODUCTO": "100600",
            "Inventario_Existencia": "3064"
        },
        "74518": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "38",
            "ID_Ubic": "18100",
            "SKU_PRODUCTO": "74518",
            "Inventario_Existencia": "73"
        },
        "74730": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "38",
            "ID_Ubic": "18100",
            "SKU_PRODUCTO": "74730",
            "Inventario_Existencia": "55"
        },
        "76204": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "38",
            "ID_Ubic": "18100",
            "SKU_PRODUCTO": "76204",
            "Inventario_Existencia": "70"
        },
        "27001": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "41",
            "ID_Ubic": "18115",
            "SKU_PRODUCTO": "27001",
            "Inventario_Existencia": "1"
        },
        "28636": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "41",
            "ID_Ubic": "18115",
            "SKU_PRODUCTO": "28636",
            "Inventario_Existencia": "1"
        },
        "9769": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "42",
            "ID_Ubic": "18120",
            "SKU_PRODUCTO": "9769",
            "Inventario_Existencia": "4500"
        },
        "100413": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "46",
            "ID_Ubic": "18140",
            "SKU_PRODUCTO": "100413",
            "Inventario_Existencia": "36"
        },
        "6284": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "6284",
            "Inventario_Existencia": "50"
        },
        "100700": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "100700",
            "Inventario_Existencia": "40"
        },
        "167953": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "61",
            "ID_Ubic": "102490",
            "SKU_PRODUCTO": "167953",
            "Inventario_Existencia": "1330"
        },
        "444696": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "444696",
            "Inventario_Existencia": "5"
        },
        "499719": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "52",
            "ID_Ubic": "102445",
            "SKU_PRODUCTO": "499719",
            "Inventario_Existencia": "13685"
        },
        "572214": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "572214",
            "Inventario_Existencia": "12"
        },
        "593523": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "593523",
            "Inventario_Existencia": "9"
        },
        "593530": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "593530",
            "Inventario_Existencia": "180"
        },
        "593547": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "593547",
            "Inventario_Existencia": "21"
        },
        "593554": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "593554",
            "Inventario_Existencia": "9"
        },
        "614969": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "614969",
            "Inventario_Existencia": "10"
        },
        "616857": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "616857",
            "Inventario_Existencia": "12"
        },
        "639634": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "639634",
            "Inventario_Existencia": "70"
        },
        "725481": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "725481",
            "Inventario_Existencia": "10"
        },
        "72916": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "72916",
            "Inventario_Existencia": "12"
        },
        "72917": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "72917",
            "Inventario_Existencia": "18"
        },
        "72942": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "72942",
            "Inventario_Existencia": "50"
        },
        "72945": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "72945",
            "Inventario_Existencia": "50"
        },
        "72949": {
            "Nombre_Pasillo": "B2",
            "X": "6",
            "Y": "61",
            "ID_Ubic": "106885",
            "SKU_PRODUCTO": "72949",
            "Inventario_Existencia": "2700"
        },
        "736098": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "59",
            "ID_Ubic": "102480",
            "SKU_PRODUCTO": "736098",
            "Inventario_Existencia": "956"
        },
        "73709": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "4",
            "ID_Ubic": "30136",
            "SKU_PRODUCTO": "73709",
            "Inventario_Existencia": "800"
        },
        "73713": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "73713",
            "Inventario_Existencia": "800"
        },
        "73718": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "73718",
            "Inventario_Existencia": "80"
        },
        "73727": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "70",
            "ID_Ubic": "106700",
            "SKU_PRODUCTO": "73727",
            "Inventario_Existencia": "12000"
        },
        "73730": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "73730",
            "Inventario_Existencia": "600"
        },
        "73742": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "2",
            "ID_Ubic": "30134",
            "SKU_PRODUCTO": "73742",
            "Inventario_Existencia": "675"
        },
        "73743": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "74",
            "ID_Ubic": "106720",
            "SKU_PRODUCTO": "73743",
            "Inventario_Existencia": "4000"
        },
        "74008": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "74008",
            "Inventario_Existencia": "50"
        },
        "74010": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "51",
            "ID_Ubic": "105600",
            "SKU_PRODUCTO": "74010",
            "Inventario_Existencia": "2700"
        },
        "74408": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "74408",
            "Inventario_Existencia": "10"
        },
        "74820": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "60",
            "ID_Ubic": "100200",
            "SKU_PRODUCTO": "74820",
            "Inventario_Existencia": "200"
        },
        "75008": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "75008",
            "Inventario_Existencia": "6"
        },
        "75044": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "75044",
            "Inventario_Existencia": "6"
        },
        "75050": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "75050",
            "Inventario_Existencia": "10"
        },
        "751961": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "57",
            "ID_Ubic": "102470",
            "SKU_PRODUCTO": "751961",
            "Inventario_Existencia": "5010"
        },
        "754498": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "64",
            "ID_Ubic": "102505",
            "SKU_PRODUCTO": "754498",
            "Inventario_Existencia": "1740"
        },
        "75502": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "75502",
            "Inventario_Existencia": "2"
        },
        "76162": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "76162",
            "Inventario_Existencia": "1"
        },
        "769836": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "54",
            "ID_Ubic": "102455",
            "SKU_PRODUCTO": "769836",
            "Inventario_Existencia": "3175"
        },
        "769843": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "769843",
            "Inventario_Existencia": "50"
        },
        "77000": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "72",
            "ID_Ubic": "103385",
            "SKU_PRODUCTO": "77000",
            "Inventario_Existencia": "6800"
        },
        "77001": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "77001",
            "Inventario_Existencia": "300"
        },
        "77005": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "64",
            "ID_Ubic": "103345",
            "SKU_PRODUCTO": "77005",
            "Inventario_Existencia": "2500"
        },
        "820346": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "820346",
            "Inventario_Existencia": "24"
        },
        "909416": {
            "Nombre_Pasillo": "A2",
            "X": "0",
            "Y": "1",
            "ID_Ubic": "30101",
            "SKU_PRODUCTO": "909416",
            "Inventario_Existencia": "11"
        },
        "60015": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "1",
            "ID_Ubic": "30133",
            "SKU_PRODUCTO": "60015",
            "Inventario_Existencia": "40"
        },
        "76832": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "1",
            "ID_Ubic": "30133",
            "SKU_PRODUCTO": "76832",
            "Inventario_Existencia": "2950"
        },
        "76825": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "2",
            "ID_Ubic": "30134",
            "SKU_PRODUCTO": "76825",
            "Inventario_Existencia": "300"
        },
        "73638": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "3",
            "ID_Ubic": "30135",
            "SKU_PRODUCTO": "73638",
            "Inventario_Existencia": "570"
        },
        "60185": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "4",
            "ID_Ubic": "30136",
            "SKU_PRODUCTO": "60185",
            "Inventario_Existencia": "20"
        },
        "74817": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "4",
            "ID_Ubic": "30136",
            "SKU_PRODUCTO": "74817",
            "Inventario_Existencia": "29"
        },
        "76835": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "4",
            "ID_Ubic": "30136",
            "SKU_PRODUCTO": "76835",
            "Inventario_Existencia": "200"
        },
        "70015": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "5",
            "ID_Ubic": "30137",
            "SKU_PRODUCTO": "70015",
            "Inventario_Existencia": "230"
        },
        "76826": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "5",
            "ID_Ubic": "30137",
            "SKU_PRODUCTO": "76826",
            "Inventario_Existencia": "300"
        },
        "76837": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "5",
            "ID_Ubic": "30137",
            "SKU_PRODUCTO": "76837",
            "Inventario_Existencia": "400"
        },
        "75506": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "6",
            "ID_Ubic": "30138",
            "SKU_PRODUCTO": "75506",
            "Inventario_Existencia": "858"
        },
        "73623": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "11",
            "ID_Ubic": "30143",
            "SKU_PRODUCTO": "73623",
            "Inventario_Existencia": "250"
        },
        "60065": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "8",
            "ID_Ubic": "30140",
            "SKU_PRODUCTO": "60065",
            "Inventario_Existencia": "5"
        },
        "73626": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "8",
            "ID_Ubic": "30140",
            "SKU_PRODUCTO": "73626",
            "Inventario_Existencia": "90"
        },
        "73725": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "8",
            "ID_Ubic": "30140",
            "SKU_PRODUCTO": "73725",
            "Inventario_Existencia": "300"
        },
        "73624": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "9",
            "ID_Ubic": "30141",
            "SKU_PRODUCTO": "73624",
            "Inventario_Existencia": "310"
        },
        "73632": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "10",
            "ID_Ubic": "30142",
            "SKU_PRODUCTO": "73632",
            "Inventario_Existencia": "100"
        },
        "73636": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "11",
            "ID_Ubic": "30143",
            "SKU_PRODUCTO": "73636",
            "Inventario_Existencia": "80"
        },
        "76833": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "11",
            "ID_Ubic": "30143",
            "SKU_PRODUCTO": "76833",
            "Inventario_Existencia": "800"
        },
        "70205": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "12",
            "ID_Ubic": "30144",
            "SKU_PRODUCTO": "70205",
            "Inventario_Existencia": "310"
        },
        "74652": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "14",
            "ID_Ubic": "30146",
            "SKU_PRODUCTO": "74652",
            "Inventario_Existencia": "1700"
        },
        "72943": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "15",
            "ID_Ubic": "30147",
            "SKU_PRODUCTO": "72943",
            "Inventario_Existencia": "225"
        },
        "73722": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "15",
            "ID_Ubic": "30147",
            "SKU_PRODUCTO": "73722",
            "Inventario_Existencia": "400"
        },
        "60383": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "16",
            "ID_Ubic": "30148",
            "SKU_PRODUCTO": "60383",
            "Inventario_Existencia": "340"
        },
        "60191": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "17",
            "ID_Ubic": "30149",
            "SKU_PRODUCTO": "60191",
            "Inventario_Existencia": "20"
        },
        "60194": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "17",
            "ID_Ubic": "30149",
            "SKU_PRODUCTO": "60194",
            "Inventario_Existencia": "60"
        },
        "60352": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "19",
            "ID_Ubic": "30151",
            "SKU_PRODUCTO": "60352",
            "Inventario_Existencia": "190"
        },
        "73740": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "21",
            "ID_Ubic": "30153",
            "SKU_PRODUCTO": "73740",
            "Inventario_Existencia": "100"
        },
        "73622": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "22",
            "ID_Ubic": "30154",
            "SKU_PRODUCTO": "73622",
            "Inventario_Existencia": "680"
        },
        "75516": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "22",
            "ID_Ubic": "30154",
            "SKU_PRODUCTO": "75516",
            "Inventario_Existencia": "576"
        },
        "75022": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "23",
            "ID_Ubic": "30155",
            "SKU_PRODUCTO": "75022",
            "Inventario_Existencia": "502"
        },
        "75023": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "23",
            "ID_Ubic": "30155",
            "SKU_PRODUCTO": "75023",
            "Inventario_Existencia": "390"
        },
        "3057": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "24",
            "ID_Ubic": "30156",
            "SKU_PRODUCTO": "3057",
            "Inventario_Existencia": "140"
        },
        "22665": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "24",
            "ID_Ubic": "30156",
            "SKU_PRODUCTO": "22665",
            "Inventario_Existencia": "148"
        },
        "28985": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "24",
            "ID_Ubic": "30156",
            "SKU_PRODUCTO": "28985",
            "Inventario_Existencia": "3"
        },
        "2286": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "60",
            "ID_Ubic": "100200",
            "SKU_PRODUCTO": "2286",
            "Inventario_Existencia": "40"
        },
        "499719Z": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "60",
            "ID_Ubic": "100200",
            "SKU_PRODUCTO": "499719Z",
            "Inventario_Existencia": "1"
        },
        "71720": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "60",
            "ID_Ubic": "100200",
            "SKU_PRODUCTO": "71720",
            "Inventario_Existencia": "4"
        },
        "74396": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "60",
            "ID_Ubic": "100200",
            "SKU_PRODUCTO": "74396",
            "Inventario_Existencia": "300"
        },
        "10937": {
            "Nombre_Pasillo": "F2",
            "X": "30",
            "Y": "55",
            "ID_Ubic": "100630",
            "SKU_PRODUCTO": "10937",
            "Inventario_Existencia": "4"
        },
        "72851": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "52",
            "ID_Ubic": "100855",
            "SKU_PRODUCTO": "72851",
            "Inventario_Existencia": "16"
        },
        "73502": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "67",
            "ID_Ubic": "105880",
            "SKU_PRODUCTO": "73502",
            "Inventario_Existencia": "12"
        },
        "71721": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "61",
            "ID_Ubic": "105850",
            "SKU_PRODUCTO": "71721",
            "Inventario_Existencia": "10"
        },
        "10938": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "55",
            "ID_Ubic": "100870",
            "SKU_PRODUCTO": "10938",
            "Inventario_Existencia": "4"
        },
        "17647": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "65",
            "ID_Ubic": "105870",
            "SKU_PRODUCTO": "17647",
            "Inventario_Existencia": "10"
        },
        "71727": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "55",
            "ID_Ubic": "100870",
            "SKU_PRODUCTO": "71727",
            "Inventario_Existencia": "2"
        },
        "71960": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "55",
            "ID_Ubic": "100870",
            "SKU_PRODUCTO": "71960",
            "Inventario_Existencia": "2"
        },
        "72264": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "59",
            "ID_Ubic": "105840",
            "SKU_PRODUCTO": "72264",
            "Inventario_Existencia": "10"
        },
        "72854": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "61",
            "ID_Ubic": "105850",
            "SKU_PRODUCTO": "72854",
            "Inventario_Existencia": "2"
        },
        "22447": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "49",
            "ID_Ubic": "101080",
            "SKU_PRODUCTO": "22447",
            "Inventario_Existencia": "15"
        },
        "73363": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "62",
            "ID_Ubic": "106552",
            "SKU_PRODUCTO": "73363",
            "Inventario_Existencia": "12"
        },
        "73696": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "49",
            "ID_Ubic": "101080",
            "SKU_PRODUCTO": "73696",
            "Inventario_Existencia": "6"
        },
        "73654": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "51",
            "ID_Ubic": "101090",
            "SKU_PRODUCTO": "73654",
            "Inventario_Existencia": "51"
        },
        "26279": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "53",
            "ID_Ubic": "101100",
            "SKU_PRODUCTO": "26279",
            "Inventario_Existencia": "12"
        },
        "73655": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "53",
            "ID_Ubic": "101100",
            "SKU_PRODUCTO": "73655",
            "Inventario_Existencia": "48"
        },
        "19074": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "55",
            "ID_Ubic": "101110",
            "SKU_PRODUCTO": "19074",
            "Inventario_Existencia": "69"
        },
        "18166": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "56",
            "ID_Ubic": "101115",
            "SKU_PRODUCTO": "18166",
            "Inventario_Existencia": "1"
        },
        "19180": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "56",
            "ID_Ubic": "101115",
            "SKU_PRODUCTO": "19180",
            "Inventario_Existencia": "10"
        },
        "499702": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "49",
            "ID_Ubic": "102430",
            "SKU_PRODUCTO": "499702",
            "Inventario_Existencia": "11850"
        },
        "560266": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "50",
            "ID_Ubic": "102435",
            "SKU_PRODUCTO": "560266",
            "Inventario_Existencia": "11175"
        },
        "560242": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "51",
            "ID_Ubic": "102440",
            "SKU_PRODUCTO": "560242",
            "Inventario_Existencia": "15150"
        },
        "444597": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "53",
            "ID_Ubic": "102450",
            "SKU_PRODUCTO": "444597",
            "Inventario_Existencia": "2490"
        },
        "444566": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "55",
            "ID_Ubic": "102460",
            "SKU_PRODUCTO": "444566",
            "Inventario_Existencia": "140"
        },
        "377352": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "56",
            "ID_Ubic": "102465",
            "SKU_PRODUCTO": "377352",
            "Inventario_Existencia": "1070"
        },
        "377369": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "58",
            "ID_Ubic": "102475",
            "SKU_PRODUCTO": "377369",
            "Inventario_Existencia": "2670"
        },
        "444559": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "60",
            "ID_Ubic": "102485",
            "SKU_PRODUCTO": "444559",
            "Inventario_Existencia": "2320"
        },
        "581209": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "62",
            "ID_Ubic": "102495",
            "SKU_PRODUCTO": "581209",
            "Inventario_Existencia": "2525"
        },
        "444573": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "63",
            "ID_Ubic": "102500",
            "SKU_PRODUCTO": "444573",
            "Inventario_Existencia": "40"
        },
        "70156": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "73",
            "ID_Ubic": "102550",
            "SKU_PRODUCTO": "70156",
            "Inventario_Existencia": "725"
        },
        "70155": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "74",
            "ID_Ubic": "102555",
            "SKU_PRODUCTO": "70155",
            "Inventario_Existencia": "950"
        },
        "70152": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "75",
            "ID_Ubic": "102560",
            "SKU_PRODUCTO": "70152",
            "Inventario_Existencia": "4275"
        },
        "72804": {
            "Nombre_Pasillo": "E2",
            "X": "24",
            "Y": "76",
            "ID_Ubic": "102565",
            "SKU_PRODUCTO": "72804",
            "Inventario_Existencia": "3870"
        },
        "3791": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "52",
            "ID_Ubic": "103285",
            "SKU_PRODUCTO": "3791",
            "Inventario_Existencia": "1450"
        },
        "73524": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "52",
            "ID_Ubic": "103285",
            "SKU_PRODUCTO": "73524",
            "Inventario_Existencia": "800"
        },
        "4994": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "54",
            "ID_Ubic": "103295",
            "SKU_PRODUCTO": "4994",
            "Inventario_Existencia": "150"
        },
        "73520": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "55",
            "ID_Ubic": "103300",
            "SKU_PRODUCTO": "73520",
            "Inventario_Existencia": "6000"
        },
        "15741": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "56",
            "ID_Ubic": "103305",
            "SKU_PRODUCTO": "15741",
            "Inventario_Existencia": "500"
        },
        "73523": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "56",
            "ID_Ubic": "103305",
            "SKU_PRODUCTO": "73523",
            "Inventario_Existencia": "1000"
        },
        "73525": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "57",
            "ID_Ubic": "103310",
            "SKU_PRODUCTO": "73525",
            "Inventario_Existencia": "6150"
        },
        "73522": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "58",
            "ID_Ubic": "103315",
            "SKU_PRODUCTO": "73522",
            "Inventario_Existencia": "2950"
        },
        "76144": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "59",
            "ID_Ubic": "103320",
            "SKU_PRODUCTO": "76144",
            "Inventario_Existencia": "3000"
        },
        "76142": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "60",
            "ID_Ubic": "103325",
            "SKU_PRODUCTO": "76142",
            "Inventario_Existencia": "5250"
        },
        "73631": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "61",
            "ID_Ubic": "103330",
            "SKU_PRODUCTO": "73631",
            "Inventario_Existencia": "520"
        },
        "73629": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "62",
            "ID_Ubic": "103335",
            "SKU_PRODUCTO": "73629",
            "Inventario_Existencia": "570"
        },
        "73630": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "63",
            "ID_Ubic": "103340",
            "SKU_PRODUCTO": "73630",
            "Inventario_Existencia": "540"
        },
        "77009": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "73",
            "ID_Ubic": "103390",
            "SKU_PRODUCTO": "77009",
            "Inventario_Existencia": "1000"
        },
        "77037": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "64",
            "ID_Ubic": "103345",
            "SKU_PRODUCTO": "77037",
            "Inventario_Existencia": "7500"
        },
        "77015": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "65",
            "ID_Ubic": "103350",
            "SKU_PRODUCTO": "77015",
            "Inventario_Existencia": "7500"
        },
        "77019": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "65",
            "ID_Ubic": "103350",
            "SKU_PRODUCTO": "77019",
            "Inventario_Existencia": "4500"
        },
        "77013": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "66",
            "ID_Ubic": "103355",
            "SKU_PRODUCTO": "77013",
            "Inventario_Existencia": "5900"
        },
        "77031": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "66",
            "ID_Ubic": "103355",
            "SKU_PRODUCTO": "77031",
            "Inventario_Existencia": "2700"
        },
        "77032": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "66",
            "ID_Ubic": "103355",
            "SKU_PRODUCTO": "77032",
            "Inventario_Existencia": "2800"
        },
        "77003": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "67",
            "ID_Ubic": "103360",
            "SKU_PRODUCTO": "77003",
            "Inventario_Existencia": "5400"
        },
        "77008": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "67",
            "ID_Ubic": "103360",
            "SKU_PRODUCTO": "77008",
            "Inventario_Existencia": "2200"
        },
        "77027": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "67",
            "ID_Ubic": "103360",
            "SKU_PRODUCTO": "77027",
            "Inventario_Existencia": "2800"
        },
        "77035": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "68",
            "ID_Ubic": "103365",
            "SKU_PRODUCTO": "77035",
            "Inventario_Existencia": "5700"
        },
        "77038": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "68",
            "ID_Ubic": "103365",
            "SKU_PRODUCTO": "77038",
            "Inventario_Existencia": "7500"
        },
        "77018": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "73",
            "ID_Ubic": "103390",
            "SKU_PRODUCTO": "77018",
            "Inventario_Existencia": "1000"
        },
        "77039": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "69",
            "ID_Ubic": "103370",
            "SKU_PRODUCTO": "77039",
            "Inventario_Existencia": "4500"
        },
        "77016": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "70",
            "ID_Ubic": "103375",
            "SKU_PRODUCTO": "77016",
            "Inventario_Existencia": "3900"
        },
        "77017": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "70",
            "ID_Ubic": "103375",
            "SKU_PRODUCTO": "77017",
            "Inventario_Existencia": "3900"
        },
        "77028": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "70",
            "ID_Ubic": "103375",
            "SKU_PRODUCTO": "77028",
            "Inventario_Existencia": "2800"
        },
        "77029": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "70",
            "ID_Ubic": "103375",
            "SKU_PRODUCTO": "77029",
            "Inventario_Existencia": "2800"
        },
        "77011": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "71",
            "ID_Ubic": "103380",
            "SKU_PRODUCTO": "77011",
            "Inventario_Existencia": "4900"
        },
        "77030": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "71",
            "ID_Ubic": "103380",
            "SKU_PRODUCTO": "77030",
            "Inventario_Existencia": "2800"
        },
        "77021": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "73",
            "ID_Ubic": "103390",
            "SKU_PRODUCTO": "77021",
            "Inventario_Existencia": "1000"
        },
        "77025": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "72",
            "ID_Ubic": "103385",
            "SKU_PRODUCTO": "77025",
            "Inventario_Existencia": "2800"
        },
        "77007": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "73",
            "ID_Ubic": "103390",
            "SKU_PRODUCTO": "77007",
            "Inventario_Existencia": "1000"
        },
        "77033": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "73",
            "ID_Ubic": "103390",
            "SKU_PRODUCTO": "77033",
            "Inventario_Existencia": "1000"
        },
        "77034": {
            "Nombre_Pasillo": "F1",
            "X": "26",
            "Y": "73",
            "ID_Ubic": "103390",
            "SKU_PRODUCTO": "77034",
            "Inventario_Existencia": "2000"
        },
        "74815": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "56",
            "ID_Ubic": "105625",
            "SKU_PRODUCTO": "74815",
            "Inventario_Existencia": "2700"
        },
        "71959": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "65",
            "ID_Ubic": "105870",
            "SKU_PRODUCTO": "71959",
            "Inventario_Existencia": "4"
        },
        "72856": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "61",
            "ID_Ubic": "105850",
            "SKU_PRODUCTO": "72856",
            "Inventario_Existencia": "2"
        },
        "17642": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "59",
            "ID_Ubic": "105840",
            "SKU_PRODUCTO": "17642",
            "Inventario_Existencia": "16"
        },
        "71961": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "61",
            "ID_Ubic": "105850",
            "SKU_PRODUCTO": "71961",
            "Inventario_Existencia": "8"
        },
        "73504": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "61",
            "ID_Ubic": "105850",
            "SKU_PRODUCTO": "73504",
            "Inventario_Existencia": "12"
        },
        "73501": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "63",
            "ID_Ubic": "105860",
            "SKU_PRODUCTO": "73501",
            "Inventario_Existencia": "4"
        },
        "73503": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "63",
            "ID_Ubic": "105860",
            "SKU_PRODUCTO": "73503",
            "Inventario_Existencia": "4"
        },
        "12808": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "65",
            "ID_Ubic": "105870",
            "SKU_PRODUCTO": "12808",
            "Inventario_Existencia": "6"
        },
        "71722": {
            "Nombre_Pasillo": "G1",
            "X": "32",
            "Y": "67",
            "ID_Ubic": "105880",
            "SKU_PRODUCTO": "71722",
            "Inventario_Existencia": "12"
        },
        "73194": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "60",
            "ID_Ubic": "106550",
            "SKU_PRODUCTO": "73194",
            "Inventario_Existencia": "12"
        },
        "73362": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "58",
            "ID_Ubic": "106548",
            "SKU_PRODUCTO": "73362",
            "Inventario_Existencia": "21"
        },
        "73695": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "62",
            "ID_Ubic": "106552",
            "SKU_PRODUCTO": "73695",
            "Inventario_Existencia": "20"
        },
        "72839": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "64",
            "ID_Ubic": "106554",
            "SKU_PRODUCTO": "72839",
            "Inventario_Existencia": "24"
        },
        "73364": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "64",
            "ID_Ubic": "106554",
            "SKU_PRODUCTO": "73364",
            "Inventario_Existencia": "9"
        },
        "14826": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "66",
            "ID_Ubic": "106556",
            "SKU_PRODUCTO": "14826",
            "Inventario_Existencia": "5"
        },
        "72838": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "66",
            "ID_Ubic": "106556",
            "SKU_PRODUCTO": "72838",
            "Inventario_Existencia": "9"
        },
        "73193": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "66",
            "ID_Ubic": "106556",
            "SKU_PRODUCTO": "73193",
            "Inventario_Existencia": "2"
        },
        "76169": {
            "Nombre_Pasillo": "G2",
            "X": "36",
            "Y": "66",
            "ID_Ubic": "106556",
            "SKU_PRODUCTO": "76169",
            "Inventario_Existencia": "3"
        },
        "74397": {
            "Nombre_Pasillo": "B1",
            "X": "2",
            "Y": "65",
            "ID_Ubic": "106675",
            "SKU_PRODUCTO": "74397",
            "Inventario_Existencia": "14800"
        },
        "76697": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "57",
            "ID_Ubic": "107765",
            "SKU_PRODUCTO": "76697",
            "Inventario_Existencia": "10"
        },
        "76707": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "61",
            "ID_Ubic": "107785",
            "SKU_PRODUCTO": "76707",
            "Inventario_Existencia": "1571"
        },
        "76709": {
            "Nombre_Pasillo": "E1",
            "X": "20",
            "Y": "62",
            "ID_Ubic": "107790",
            "SKU_PRODUCTO": "76709",
            "Inventario_Existencia": "812"
        }
    }
    
    """
    
    import urllib, json
    import requests
    
    # GET
    urlGET="http://myonest.com:7090/ords/onewms/almacen/layout"


    response=urllib.request.urlopen(urlGET)

    print(response)

    geometriaAlmacen=json.loads(response.read())



    print(geometriaAlmacen)
    
    

    #Una vez hecha la lectura de la geometría del almacen procederemos a castear a un CSV con el fomrato necesario

    #Hay que desanidar el contenido del json



    #Extraemos los primeros dos elementos
    #Identificador del almacen y dimensiones para poder trabajar con el resto de la infromación que tiene un formato único


    identificadorAlmacen=geometriaAlmacen["IdentificadorAlmacen"]
    geometriaAlmacen.pop("IdentificadorAlmacen", None)


    dimensionesAlmacen=geometriaAlmacen["Dimensiones"]
    geometriaAlmacen.pop("Dimensiones", None)
    
    """
    cont=0

    for i in geometriaAlmacen:
        print(i)
        print(geometriaAlmacen[i])
        print(cont)
        cont+=1
        for j in geometriaAlmacen[i]:
            #print("Segundoloop")
            print(j)
            #print(geometriaAlmacen[i][j])

    #print(geometriaAlmacen["76709"])
    
    """
    
    
    #Almacenamos la infromación en ubicaciones

    dF_raw=pd.DataFrame(geometriaAlmacen)

    dF_raw_transpose=dF_raw.transpose()

    dF_raw_ResetIndex = dF_raw_transpose.reset_index(drop=True)
    
    

    #Solamente debemos renombrar la columna NOmbre Pasillo por ID_Pasillo
    dF_raw_ResetIndex.rename(columns = {'Nombre_Pasillo':'ID_Pasillo'}, inplace = True)

    #Hecho esto solamente queda almacenar el csv en la carpeta correspondiente.
    dF_raw_ResetIndex_Sorted=dF_raw_ResetIndex.sort_values('ID_Pasillo')


    dF_raw_ResetIndex_Sorted.to_csv("Ubicaciones.csv",index=False)



    #Guardamos el entero que nos dice el identificador del almacen

    with open('identificadorAlmacen.txt', 'w') as f:
      f.write('%s' % identificadorAlmacen)

    #Guardamos el diccionario que nos da las dimensiones del almacen
    with open('dimensionesAlmacen.txt', 'w') as f:
      f.write('%s' % dimensionesAlmacen)



    print("Leyendo la geometría del almacen")
    
    
    
    return



#error  key 5764015

"""
Users\lumen\Documents\ONEST\OnestRutasOptims\VERSION_UNICAMENTE_FLASK_NOAIRFLOW\3_AppFinalFlask\OPT_Recolecc_Indiv_Y_Apilados.py", line 854, in <listcomp>
  listaUbicacionesProductosPorPedido.append([DicProducUbic[str(x)] for x in i])
  
  """

#dF_raw,dF_raw_transpose,geometriaAlmacen=Lectura_geometriaAlmacen()

#SKUList=list(dF_raw_transpose["SKU_PRODUCTO"])

#print(SKUList.index("5764015"))

