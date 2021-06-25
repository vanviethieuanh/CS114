"""
🇻🇳 VIETNAM FIREWILD API
~~~~~~~~~~~~

This module implements the Firewild API.
Data from http://firewatchvn.kiemlam.org.vn provide by
VIETNAM ADMINISTRATION OF FORESTRY (TỔNG CỤC LÂM NGHIỆP VIỆT NAM)
http://tongcuclamnghiep.gov.vn/

Data from this module is specify in Vietnam only.

:copyright: (c) 2021 Văn Viết Hiếu Anh
:license: MIT License, see LICENSE for more details.
"""

from requests import get

def GetAllProvinces():
    """Return all provinces with code of that province

    Returns:
        array: each invidual is a dict contain "ma" which is province code
            and "ten" is the name of that province
    """
    url = 'http://firewatchvn.kiemlam.org.vn/fwdata/hanhchinh/0/0'

    res = get(url)
    return res.json()

def GetDistricts(provinceCode):
    """Return all district from code of province

    Returns:
        array: each invidual is a dict contain "ma" which is district code
            and "ten" is the name of that district
    """
    url = f'http://firewatchvn.kiemlam.org.vn/fwdata/hanhchinh/{provinceCode}/0'

    res = get(url)
    return res.json()


def GetWards(provinceCode,districtCode):
    """Return all wards from code of district

    Args:
        array: each invidual is a dict contain "ma" which is ward code
            and "ten" is the name of that ward
    """
    url = f'http://firewatchvn.kiemlam.org.vn/fwdata/hanhchinh/{provinceCode}/{districtCode}'

    res = get(url)
    return res.json()

def GetAllFireWild(date,provinceCode,districtCode,wardCode=0):
    """Return all FireWild from provide district

    Args:
        date (str): date string dd/mm/yyyy
        provinceCode (int): 
        districtCode (int): 
        wardCode (int, optional): Defaults to 0.

    Returns:
        array: array of firewild record include
            date, province, district, ward, long(x), lat(y)
    """
    formatedDate = date.replace('/','!')
    url = f'http://firewatchvn.kiemlam.org.vn/fwdata/search/diaphuong/{provinceCode}/{districtCode}/{wardCode}/{formatedDate}/{formatedDate}/1/100'

    res = get(url)
    wards = res.json()

    records = []
    for ward in wards:
        for firewild in ward['hp']:
            records.append({
                'date':date,
                'province':provinceCode,
                'district':districtCode,
                'ward':ward['xa'] if not wardCode else wardCode, # if provide ward code return with it
                'x':firewild['x'],
                'y':firewild['y']
            })

    return records

def WildFireStat(date, provinceCode=0):
    """Return records of stat firewild of a date, if null return []

    Args:
        date (str): dd/mm/yyyy

    Returns:
        array: return an array of record, each individual contain province and distric code
            and firewild count
    """
    formatedDate = date.replace('/','!')
    url = f'http://firewatchvn.kiemlam.org.vn/fwdata/search/diaphuong/{provinceCode}/0/0/{formatedDate}/{formatedDate}/1/100'

    res = get(url)
    json = res.json()

    records = []
    if json:
        for province in json:
            for district in province['huyens']:
                records.append({
                    'province':province['code'],
                    'district':district['code'],
                    'firewildCount':district['sdc']
                })

    return records