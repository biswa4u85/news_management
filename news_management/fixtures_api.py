import frappe
import requests
import json
import datetime


@frappe.whitelist(allow_guest=True)
def fetchDataSeries():
    apiHost = frappe.db.get_single_value('Live Score Details', 'api_host')
    apiKey = frappe.db.get_single_value('Live Score Details', 'api_key')
    apiUrl = frappe.db.get_single_value('Live Score Details', 'api_url')

    # Series
    url = apiUrl + "/series"
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'X-RapidAPI-Key': apiKey,
        'X-RapidAPI-Host': apiHost
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if (response.status_code == 200):
        data = response.json()
        docType = "Live Score Series"
        for series in data['results']:
            seriesType = series['type']
            for item in series['series']:
                # frappe.msgprint(json.dumps(item['updated_at']))
                isExit = frappe.db.exists(
                    docType, {"series_id": item['series_id']})
                if (isExit):
                    frappe.db.set_value(docType, isExit, {
                        'series_id': item['series_id'],
                        'type': seriesType,
                        "season": item['season'],
                        "series_name": item['series_name'],
                        "status": item['status'],
                        "updated_at": item['updated_at'],
                    })
                else:
                    addData = frappe.new_doc(docType)
                    addData.series_id = item['series_id']
                    addData.type = seriesType
                    addData.season = item['season']
                    addData.series_name = item['series_name']
                    addData.status = item['status']
                    addData.updated_at = item['updated_at']
                    addData.insert()
        frappe.msgprint('Series Updated Successfully')


@frappe.whitelist(allow_guest=True)
def fetchDataFixtures():
    apiHost = frappe.db.get_single_value('Live Score Details', 'api_host')
    apiKey = frappe.db.get_single_value('Live Score Details', 'api_key')
    apiUrl = frappe.db.get_single_value('Live Score Details', 'api_url')

    # Fixtures
    url = apiUrl + "/fixtures"
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'X-RapidAPI-Key': apiKey,
        'X-RapidAPI-Host': apiHost
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if (response.status_code == 200):
        data = response.json()
        docType = "Live Score Fixtures"
        for item in data['results']:
            isExit = frappe.db.exists(docType, {"id": item['id']})
            if (isExit):
                frappe.db.set_value(docType, isExit, {
                    'id': item['id'],
                    "series_id": item['series_id'],
                    "venue": item['venue'],
                    "date": item['date'],
                    "status": item['status'],
                    "result": item['result'],
                    "match_title": item['match_title'],
                    "match_subtitle": item['match_subtitle'],
                    "home": json.dumps(item['home']),
                    "away": json.dumps(item['away']),
                })
            else:
                addData = frappe.new_doc(docType)
                addData.id = item['id']
                addData.series_id = item['series_id']
                addData.venue = item['venue']
                addData.date = item['date']
                addData.status = item['status']
                addData.result = item['result']
                addData.match_title = item['match_title']
                addData.match_subtitle = item['match_subtitle']
                addData.home = json.dumps(item['home'])
                addData.away = json.dumps(item['away'])
                addData.insert()

    # Results
    url = apiUrl + "/results"
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'X-RapidAPI-Key': apiKey,
        'X-RapidAPI-Host': apiHost
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if (response.status_code == 200):
        data = response.json()
        docType = "Live Score Fixtures"
        for item in data['results']:
            isExit = frappe.db.exists(docType, {"id": item['id']})
            if (isExit):
                frappe.db.set_value(docType, isExit, {
                    'id': item['id'],
                    "series_id": item['series_id'],
                    "venue": item['venue'],
                    "date": item['date'],
                    "status": item['status'],
                    "result": item['result'],
                    "match_title": item['match_title'],
                    "match_subtitle": item['match_subtitle'],
                    "home": json.dumps(item['home']),
                    "away": json.dumps(item['away']),
                })
            else:
                addData = frappe.new_doc(docType)
                addData.id = item['id']
                addData.series_id = item['series_id']
                addData.venue = item['venue']
                addData.date = item['date']
                addData.status = item['status']
                addData.result = item['result']
                addData.match_title = item['match_title']
                addData.match_subtitle = item['match_subtitle']
                addData.home = json.dumps(item['home'])
                addData.away = json.dumps(item['away'])
                addData.insert()
        frappe.msgprint('Fixtures Updated Successfully')
