import frappe
import requests
import json
import datetime

# frappe.msgprint(str(data))


@frappe.whitelist(allow_guest=True)
def fetchMultiSearch(query):
    apiHost = frappe.db.get_single_value('Live Score Details', 'api_host')
    apiKey = frappe.db.get_single_value('Live Score Details', 'api_key')
    apiUrl = frappe.db.get_single_value('Live Score Details', 'api_url')

    # Series
    url = apiUrl + "/search/multi-search?locale=en_INT&query=" + query
    payload = {}
    headers = {
        "X-RapidAPI-Key": apiKey,
        "X-RapidAPI-Host": apiHost
    }
    response = requests.request(
        "GET", url, headers=headers, data=payload)
    if (response.status_code == 200):
        return response.json()
    else:
        frappe.msgprint('No Records Found')


@frappe.whitelist(allow_guest=True)
def fetchRankings():
    apiHost = frappe.db.get_single_value('Live Score Details', 'api_host')
    apiKey = frappe.db.get_single_value('Live Score Details', 'api_key')
    apiUrl = frappe.db.get_single_value('Live Score Details', 'api_url')

    # Series
    url = apiUrl + "/rankings/list?locale=en_INT&sport_id=13"
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'X-RapidAPI-Key': apiKey,
        'X-RapidAPI-Host': apiHost
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if (response.status_code == 200):
        data = response.json()
        frappe.msgprint(str(data))
        docType = "Flash Rankings"
        for item in data['DATA']:
            isExit = frappe.db.exists(
                docType, {"sport_id": item['ID']})
            if (isExit):
                frappe.db.set_value(docType, isExit, {
                    'sport_id': item['ID'],
                    "title": item['NAME'],
                })
            else:
                addData = frappe.new_doc(docType)
                addData.sport_id = item['ID']
                addData.title = item['NAME']
                addData.insert()
        frappe.msgprint('Sports are Updated Successfully')
    else:
        frappe.msgprint('No Records Found')


@frappe.whitelist(allow_guest=True)
def fetchRankingDetails(rankingId):
    apiHost = frappe.db.get_single_value('Live Score Details', 'api_host')
    apiKey = frappe.db.get_single_value('Live Score Details', 'api_key')
    apiUrl = frappe.db.get_single_value('Live Score Details', 'api_url')

    # Series
    url = apiUrl + "/rankings/data?locale=en_INT&ranking_id=" + rankingId
    payload = {}
    headers = {
        "X-RapidAPI-Key": apiKey,
        "X-RapidAPI-Host": apiHost
    }
    response = requests.request(
        "GET", url, headers=headers, data=payload)
    if (response.status_code == 200):
        return response.json()
    else:
        frappe.msgprint('No Records Found')


@frappe.whitelist(allow_guest=True)
def fetchSports():
    apiHost = frappe.db.get_single_value('Live Score Details', 'api_host')
    apiKey = frappe.db.get_single_value('Live Score Details', 'api_key')
    apiUrl = frappe.db.get_single_value('Live Score Details', 'api_url')

    # Series
    url = apiUrl + "/sports/list?locale=en_INT&timezone=-4"
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'X-RapidAPI-Key': apiKey,
        'X-RapidAPI-Host': apiHost
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if (response.status_code == 200):
        data = response.json()
        # frappe.msgprint(str(data))
        docType = "Flash Sports"
        for item in data['DATA']:
            isExit = frappe.db.exists(
                docType, {"sport_id": item['ID']})
            if (isExit):
                frappe.db.set_value(docType, isExit, {
                    'sport_id': item['ID'],
                    "title": item['NAME'],
                })
            else:
                addData = frappe.new_doc(docType)
                addData.sport_id = item['ID']
                addData.title = item['NAME']
                addData.insert()
        frappe.msgprint('Sports are Updated Successfully')
    else:
        frappe.msgprint('No Records Found')


@frappe.whitelist(allow_guest=True)
def fetchSportsEventsCount():
    apiHost = frappe.db.get_single_value('Live Score Details', 'api_host')
    apiKey = frappe.db.get_single_value('Live Score Details', 'api_key')
    apiUrl = frappe.db.get_single_value('Live Score Details', 'api_url')

    # Series
    url = apiUrl + "/sports/events-count?locale=en_INT&timezone=-4"
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'X-RapidAPI-Key': apiKey,
        'X-RapidAPI-Host': apiHost
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if (response.status_code == 200):
        data = response.json()
        docType = "Flash Sports"
        for item in data['DATA']['SPORTS']:
            isExit = frappe.db.exists(
                docType, {"sport_id": item['SPORT_ID']})
            if (isExit):
                frappe.db.set_value(docType, isExit, {
                    'sport_id': item['SPORT_ID'],
                    "events_count": item['EVENTS_COUNT'],
                    "events_count_live": item['EVENTS_COUNT_LIVE'],
                    "is_popular": item['IS_POPULAR'],
                    "sport_name": item['SPORT_NAME'],
                })
            else:
                addData = frappe.new_doc(docType)
                addData.sport_id = item['SPORT_ID']
                addData.events_count = item['EVENTS_COUNT']
                addData.events_count_live = item['EVENTS_COUNT_LIVE']
                addData.is_popular = item['IS_POPULAR']
                addData.sport_name = item['SPORT_NAME']
                addData.insert()
        frappe.msgprint('Events Counts are Updated Successfully')
    else:
        frappe.msgprint('No Records Found')


@frappe.whitelist(allow_guest=True)
def fetchEvents():
    apiHost = frappe.db.get_single_value('Live Score Details', 'api_host')
    apiKey = frappe.db.get_single_value('Live Score Details', 'api_key')
    apiUrl = frappe.db.get_single_value('Live Score Details', 'api_url')

    # Series
    url = apiUrl + "/events/list?locale=en_INT&timezone=-4&indent_days=-1&sport_id=13"
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'X-RapidAPI-Key': apiKey,
        'X-RapidAPI-Host': apiHost
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if (response.status_code == 200):
        data = response.json()
        docType = "Flash All Events"
        for tournament in data['DATA']:
            events = tournament['EVENTS']
            del tournament['EVENTS']
            for item in events:
                startTime = datetime.datetime.fromtimestamp(item['START_TIME'])
                isExit = frappe.db.exists(
                    docType, {"event_id": item['EVENT_ID']})
                if (isExit):
                    frappe.db.set_value(docType, isExit, {
                        'tournament_id': tournament['TOURNAMENT_ID'],
                        'tournament_details': json.dumps(tournament),
                        'event_id': item['EVENT_ID'],
                        'date': startTime,
                        'start_time': startTime,
                        'event_details': json.dumps(item),
                        "title": item['EVENT_ID'],
                    })
                else:
                    addData = frappe.new_doc(docType)
                    addData.tournament_id = tournament['TOURNAMENT_ID']
                    addData.tournament_details = json.dumps(tournament)
                    addData.event_id = item['EVENT_ID']
                    addData.date = startTime
                    addData.start_time = startTime
                    addData.event_details = json.dumps(item)
                    addData.title = item['EVENT_ID']
                    addData.insert()
        frappe.msgprint('Events are Updated Successfully')
    else:
        frappe.msgprint('No Records Found')


@frappe.whitelist(allow_guest=True)
def fetchEventsDetails(query):
    apiHost = frappe.db.get_single_value('Live Score Details', 'api_host')
    apiKey = frappe.db.get_single_value('Live Score Details', 'api_key')
    apiUrl = frappe.db.get_single_value('Live Score Details', 'api_url')

    url = apiUrl + "/events/data?locale=en_INT&event_id=" + query
    payload = {}
    headers = {
        "X-RapidAPI-Key": apiKey,
        "X-RapidAPI-Host": apiHost
    }
    response = requests.request(
        "GET", url, headers=headers, data=payload)
    if (response.status_code == 200):
        data = response.json()
        return data


@frappe.whitelist(allow_guest=True)
def fetchTournaments():
    apiHost = frappe.db.get_single_value('Live Score Details', 'api_host')
    apiKey = frappe.db.get_single_value('Live Score Details', 'api_key')
    apiUrl = frappe.db.get_single_value('Live Score Details', 'api_url')

    # Series
    url = apiUrl + "/tournaments/list?locale=en_INT&sport_id=13"
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'X-RapidAPI-Key': apiKey,
        'X-RapidAPI-Host': apiHost
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if (response.status_code == 200):
        data = response.json()
        docType = "Flash Tournaments"
        for item in data['DATA']:
            isExit = frappe.db.exists(
                docType, {"template_id": item['TEMPLATE_ID']})
            if (isExit):
                frappe.db.set_value(docType, isExit, {
                    "title": item['TEMPLATE_ID'],
                    "tournament_name": item['LEAGUE_NAME'],
                    'country_name': item['COUNTRY_NAME'],
                    'country_id': item['COUNTRY_ID'],
                    'actual_tournament_season_id': item['ACTUAL_TOURNAMENT_SEASON_ID'],
                    'group_id': item['GROUP_ID'],
                    'season_id': item['SEASON_ID'],
                    'template_id': item['TEMPLATE_ID'],
                    'stages': json.dumps(item['STAGES']),
                })
            else:
                addData = frappe.new_doc(docType)
                addData.title = item['TEMPLATE_ID']
                addData.tournament_name = item['LEAGUE_NAME']
                addData.country_name = item['COUNTRY_NAME']
                addData.country_id = item['COUNTRY_ID']
                addData.actual_tournament_season_id = item['ACTUAL_TOURNAMENT_SEASON_ID']
                addData.group_id = item['GROUP_ID']
                addData.season_id = item['SEASON_ID']
                addData.template_id = item['TEMPLATE_ID']
                addData.stages = json.dumps(item['STAGES'])
                addData.insert()
        frappe.msgprint('Events are Updated Successfully')
    else:
        frappe.msgprint('No Records Found')


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
            # Date Format
            newDay = datetime.datetime.fromisoformat(
                item['date']).strftime("%d")
            newMonth = datetime.datetime.fromisoformat(
                item['date']).strftime("%m")
            newYear = datetime.datetime.fromisoformat(
                item['date']).strftime("%Y")
            newHour = datetime.datetime.fromisoformat(
                item['date']).strftime("%H")
            newMin = datetime.datetime.fromisoformat(
                item['date']).strftime("%M")
            newSec = datetime.datetime.fromisoformat(
                item['date']).strftime("%S")
            isExit = frappe.db.exists(docType, {"id": item['id']})
            if (isExit):
                frappe.db.set_value(docType, isExit, {
                    'id': item['id'],
                    "series_id": item['series_id'],
                    "venue": item['venue'],
                    "date": datetime.datetime(
                        int(newYear), int(newMonth), int(newDay)),
                    "datetime": datetime.datetime(int(newYear), int(
                        newMonth), int(newDay), int(newHour), int(newMin), int(newSec), ),
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
                addData.date = datetime.datetime(
                    int(newYear), int(newMonth), int(newDay))
                addData.datetime = datetime.datetime(int(newYear), int(
                    newMonth), int(newDay), int(newHour), int(newMin), int(newSec), )
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
            # Date Format
            newDay = datetime.datetime.fromisoformat(
                item['date']).strftime("%d")
            newMonth = datetime.datetime.fromisoformat(
                item['date']).strftime("%m")
            newYear = datetime.datetime.fromisoformat(
                item['date']).strftime("%Y")
            newHour = datetime.datetime.fromisoformat(
                item['date']).strftime("%H")
            newMin = datetime.datetime.fromisoformat(
                item['date']).strftime("%M")
            newSec = datetime.datetime.fromisoformat(
                item['date']).strftime("%S")
            isExit = frappe.db.exists(docType, {"id": item['id']})
            if (isExit):
                frappe.db.set_value(docType, isExit, {
                    'id': item['id'],
                    "series_id": item['series_id'],
                    "venue": item['venue'],
                    "date": datetime.datetime(
                        int(newYear), int(newMonth), int(newDay)),
                    "datetime": datetime.datetime(int(newYear), int(
                        newMonth), int(newDay), int(newHour), int(newMin), int(newSec), ),
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
                addData.date = datetime.datetime(
                    int(newYear), int(newMonth), int(newDay))
                addData.datetime = datetime.datetime(int(newYear), int(
                    newMonth), int(newDay), int(newHour), int(newMin), int(newSec), )
                addData.status = item['status']
                addData.result = item['result']
                addData.match_title = item['match_title']
                addData.match_subtitle = item['match_subtitle']
                addData.home = json.dumps(item['home'])
                addData.away = json.dumps(item['away'])
                addData.insert()
        frappe.msgprint('Fixtures Updated Successfully')


@frappe.whitelist(allow_guest=True)
def getSportsData(query):
    apiHost = frappe.db.get_single_value('Live Score Details', 'api_host')
    apiKey = frappe.db.get_single_value('Live Score Details', 'api_key')
    apiUrl = frappe.db.get_single_value('Live Score Details', 'api_url')

    url = apiUrl + "/sports/" + query
    payload = {}
    headers = {
        "X-RapidAPI-Key": apiKey,
        "X-RapidAPI-Host": apiHost
    }
    response = requests.request(
        "GET", url, headers=headers, data=payload)
    if (response.status_code == 200):
        return response.json()


@frappe.whitelist(allow_guest=True)
def getEventsData(query):
    apiHost = frappe.db.get_single_value('Live Score Details', 'api_host')
    apiKey = frappe.db.get_single_value('Live Score Details', 'api_key')
    apiUrl = frappe.db.get_single_value('Live Score Details', 'api_url')

    url = apiUrl + "/events/" + query
    payload = {}
    headers = {
        "X-RapidAPI-Key": apiKey,
        "X-RapidAPI-Host": apiHost
    }
    response = requests.request(
        "GET", url, headers=headers, data=payload)
    if (response.status_code == 200):
        return response.json()


@frappe.whitelist(allow_guest=True)
def getTeamsData(query):
    apiHost = frappe.db.get_single_value('Live Score Details', 'api_host')
    apiKey = frappe.db.get_single_value('Live Score Details', 'api_key')
    apiUrl = frappe.db.get_single_value('Live Score Details', 'api_url')

    url = apiUrl + "/teams/" + query
    payload = {}
    headers = {
        "X-RapidAPI-Key": apiKey,
        "X-RapidAPI-Host": apiHost
    }
    response = requests.request(
        "GET", url, headers=headers, data=payload)
    if (response.status_code == 200):
        return response.json()


@frappe.whitelist(allow_guest=True)
def getTournamentsData(query):
    apiHost = frappe.db.get_single_value('Live Score Details', 'api_host')
    apiKey = frappe.db.get_single_value('Live Score Details', 'api_key')
    apiUrl = frappe.db.get_single_value('Live Score Details', 'api_url')

    url = apiUrl + "/tournaments/" + query
    payload = {}
    headers = {
        "X-RapidAPI-Key": apiKey,
        "X-RapidAPI-Host": apiHost
    }
    response = requests.request(
        "GET", url, headers=headers, data=payload)
    if (response.status_code == 200):
        return response.json()
