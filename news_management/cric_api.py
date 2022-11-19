import frappe
import requests
import json
import datetime

# frappe.msgprint(str(data))


# Series
@frappe.whitelist(allow_guest=True)
def fetchSeries():
    apiHost = frappe.db.get_single_value('Cric Credentials', 'api_host')
    apiKey = frappe.db.get_single_value('Cric Credentials', 'api_key')
    apiUrl = frappe.db.get_single_value('Cric Credentials', 'api_url')

    # # Series
    types = ['international', 'league', 'domestic', 'women']
    for type in types:
        urlTournaments = apiUrl + "/series/v1/" + type
        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'X-RapidAPI-Key': apiKey,
            'X-RapidAPI-Host': apiHost
        }
        response = requests.request(
            "GET", urlTournaments, headers=headers, data=payload)
        if (response.status_code == 200):
            data = response.json()
            docType = "Cric Series"
            for seriesItem in data['seriesMapProto']:
                for item in seriesItem['series']:
                    isExit = frappe.db.exists(
                        docType, {"title": str(item['id'])})
                    startdt = datetime.datetime.fromtimestamp(
                        int(item['startDt'])/1000)
                    enddt = datetime.datetime.fromtimestamp(
                        int(item['endDt'])/1000)
                    if (isExit):
                        frappe.db.set_value(docType, isExit, {
                            "title": item['id'],
                            "type": type,
                            'date': seriesItem['date'],
                            'series_name': item['name'],
                            'startdt': startdt,
                            'enddt': enddt,
                            'status': 'open',
                        })
                    else:
                        addData = frappe.new_doc(docType)
                        addData.title = str(item['id'])
                        addData.type = type
                        addData.date = seriesItem['date']
                        addData.series_name = item['name']
                        addData.startdt = startdt
                        addData.enddt = enddt
                        addData.status = 'open'
                        addData.insert()
    frappe.msgprint('Series are Updated Successfully')
    fetchSchedule()


# Series Archives
def fetchSeriesArchives(value):
    apiHost = frappe.db.get_single_value('Cric Credentials', 'api_host')
    apiKey = frappe.db.get_single_value('Cric Credentials', 'api_key')
    apiUrl = frappe.db.get_single_value('Cric Credentials', 'api_url')

    today = datetime.date.today()
    year = today.year
    findYear = value if value else year

    # Series Archives
    types = ['international', 'league', 'domestic', 'women']
    for type in types:
        urlTournaments = apiUrl + "/series/v1/archives/" + \
            type + '?year=' + findYear
        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'X-RapidAPI-Key': apiKey,
            'X-RapidAPI-Host': apiHost
        }
        response = requests.request(
            "GET", urlTournaments, headers=headers, data=payload)
        if (response.status_code == 200):
            data = response.json()
            docType = "Cric Series"
            for seriesItem in data['seriesMapProto']:
                for item in seriesItem['series']:
                    isExit = frappe.db.exists(
                        docType, {"title": str(item['id'])})
                    startdt = datetime.datetime.fromtimestamp(
                        int(item['startDt'])/1000)
                    enddt = datetime.datetime.fromtimestamp(
                        int(item['endDt'])/1000)
                    if (isExit):
                        frappe.db.set_value(docType, isExit, {
                            "title": item['id'],
                            "type": type,
                            'date': seriesItem['date'],
                            'series_name': item['name'],
                            'startdt': startdt,
                            'enddt': enddt,
                            'status': 'archives',
                        })
                    else:
                        addData = frappe.new_doc(docType)
                        addData.title = str(item['id'])
                        addData.type = type
                        addData.date = seriesItem['date']
                        addData.series_name = item['name']
                        addData.startdt = startdt
                        addData.enddt = enddt
                        addData.status = 'archives'
                        addData.insert()
    return frappe.db.get_list('Cric Series', filters={
        'date': findYear}, fields=['name', 'type', 'series_name', 'startdt', 'date'])


# Schedule
def fetchSchedule():
    apiHost = frappe.db.get_single_value('Cric Credentials', 'api_host')
    apiKey = frappe.db.get_single_value('Cric Credentials', 'api_key')
    apiUrl = frappe.db.get_single_value('Cric Credentials', 'api_url')

    # Schedule
    types = ['international', 'league', 'domestic', 'women']
    for type in types:
        urlTournaments = apiUrl + "/schedule/v1/" + type
        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'X-RapidAPI-Key': apiKey,
            'X-RapidAPI-Host': apiHost
        }
        response = requests.request(
            "GET", urlTournaments, headers=headers, data=payload)
        if (response.status_code == 200):
            data = response.json()
            docType = "Cric Series"
            for schedule in data['matchScheduleMap']:
                if 'scheduleAdWrapper' in schedule:
                    seriesItem = schedule['scheduleAdWrapper']
                    for item in seriesItem['matchScheduleList']:
                        isExit = frappe.db.exists(
                            docType, {"title": str(item['seriesId'])})
                        # Update Match
                        updateMatch(item['matchInfo'], '')
                        if (isExit):
                            frappe.db.set_value(docType, isExit, {
                                "title": item['seriesId'],
                                "type": type,
                                'date': seriesItem['date'],
                                'series_name': item['seriesName'],
                                'status': 'open',
                                'home_country': item['seriesHomeCountry'],
                            })
                        else:
                            addData = frappe.new_doc(docType)
                            addData.title = str(item['seriesId'])
                            addData.type = type
                            addData.date = seriesItem['date']
                            addData.series_name = item['seriesName']
                            addData.status = 'open'
                            addData.home_country = item['seriesHomeCountry']
                            addData.insert()
    frappe.msgprint('Schedule are Updated Successfully')


# Matches
@frappe.whitelist(allow_guest=True)
def fetchMatches():
    apiHost = frappe.db.get_single_value('Cric Credentials', 'api_host')
    apiKey = frappe.db.get_single_value('Cric Credentials', 'api_key')
    apiUrl = frappe.db.get_single_value('Cric Credentials', 'api_url')

    # Matches
    types = ['live', 'recent', 'upcoming']
    for type in types:
        urlTournaments = apiUrl + "/matches/v1/" + type
        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'X-RapidAPI-Key': apiKey,
            'X-RapidAPI-Host': apiHost
        }
        response = requests.request(
            "GET", urlTournaments, headers=headers, data=payload)
        if (response.status_code == 200):
            data = response.json()
            docType = "Cric Series"
            for matches in data['typeMatches']:
                seriesItem = matches['seriesMatches']
                for series in seriesItem:
                    if 'seriesAdWrapper' in series:
                        item = series['seriesAdWrapper']
                        isExit = frappe.db.exists(
                            docType, {"title": str(item['seriesId'])})
                        if (isExit) is None:
                            addData = frappe.new_doc(docType)
                            addData.title = str(item['seriesId'])
                            addData.type = (matches['matchType']).lower()
                            addData.series_name = item['seriesName']
                            addData.insert()
                updateMatch(item['matches'], type)
    frappe.msgprint('Matches are Updated Successfully')


# Teams
@frappe.whitelist(allow_guest=True)
def fetchTeams():
    apiHost = frappe.db.get_single_value('Cric Credentials', 'api_host')
    apiKey = frappe.db.get_single_value('Cric Credentials', 'api_key')
    apiUrl = frappe.db.get_single_value('Cric Credentials', 'api_url')

    # Teams
    types = ['international', 'league', 'domestic', 'women']
    for type in types:
        urlTournaments = apiUrl + "/teams/v1/" + type
        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'X-RapidAPI-Key': apiKey,
            'X-RapidAPI-Host': apiHost
        }
        response = requests.request(
            "GET", urlTournaments, headers=headers, data=payload)
        if (response.status_code == 200):
            data = response.json()
            docType = "Cric Teams"
            for item in data['list']:
                if 'teamId' in item:
                    isExit = frappe.db.exists(
                        docType, {"title": str(item['teamId'])})
                    if (isExit):
                        frappe.db.set_value(docType, isExit, {
                            "title": item['teamId'],
                            'team_name': item['teamName'],
                            'team_sname': item['teamSName'],
                            'image_id': item['imageId'],
                            "type": type,
                            'country_name': item['countryName'] if ('countryName' in item) else '',
                        })
                    else:
                        addData = frappe.new_doc(docType)
                        addData.title = str(item['teamId'])
                        addData.team_name = item['teamName']
                        addData.team_sname = item['teamSName']
                        addData.image_id = item['imageId']
                        addData.type = type
                        addData.country_name = item['countryName'] if (
                            'countryName' in item) else ''
                        addData.insert()
    frappe.msgprint('Teams are Updated Successfully')


# Update Match
def updateMatch(data, type):
    docType = "Cric Matches"
    for item in data:
        matchScore = {}
        if 'matchInfo' in item:
            if 'matchScore' in item:
                matchScore = item['matchScore']
            item = item['matchInfo']
        isExit = frappe.db.exists(
            docType, {"title": str(item['matchId'])})
        startdt = datetime.datetime.fromtimestamp(int(item['startDate'])/1000)
        enddt = datetime.datetime.fromtimestamp(int(item['endDate'])/1000)
        if (isExit):
            frappe.db.set_value(docType, isExit, {
                "title": item['matchId'],
                "series": item['seriesId'],
                'match_desc': item['matchDesc'],
                'match_format': item['matchFormat'],
                'startdt': startdt,
                'enddt': enddt,
                'team1': item['team1']['teamId'],
                'team2': item['team2']['teamId'],
                'venue': json.dumps(item['venueInfo']),
                'sub_satus': type if type else '',
                'state': item['state'] if ('state' in item) else '',
                'result': item['status'] if ('status' in item) else '',
                'score': json.dumps(matchScore),
            })
        else:
            addData = frappe.new_doc(docType)
            addData.title = str(item['matchId'])
            addData.series = str(item['seriesId'])
            addData.match_desc = item['matchDesc']
            addData.match_format = item['matchFormat']
            addData.startdt = startdt
            addData.enddt = enddt
            addData.team1 = str(item['team1']['teamId'])
            addData.team2 = str(item['team2']['teamId'])
            addData.venue = json.dumps(item['venueInfo'])
            addData.sub_satus = type if type else '',
            addData.state = item['state'] if ('state' in item) else ''
            addData.result = item['status'] if ('status' in item) else ''
            addData.score = json.dumps(matchScore)
            addData.insert()


# Expose API

# Match By Series
def updateMatchBySeries(serieId):
    apiHost = frappe.db.get_single_value('Cric Credentials', 'api_host')
    apiKey = frappe.db.get_single_value('Cric Credentials', 'api_key')
    apiUrl = frappe.db.get_single_value('Cric Credentials', 'api_url')

    # Matches
    urlMatches = apiUrl + "/series/v1/" + serieId
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'X-RapidAPI-Key': apiKey,
        'X-RapidAPI-Host': apiHost
    }
    response = requests.request(
        "GET", urlMatches, headers=headers, data=payload)
    if (response.status_code == 200):
        data = response.json()
        for item in data['matchDetails']:
            if 'matchDetailsMap' in item:
                updateMatch(item['matchDetailsMap']['match'], '')
        return frappe.db.get_list('Cric Matches', filters={"series": serieId}, fields=[
            'name', 'type', 'series', 'startdt', 'date', 'team1', 'team2', 'venue',  'sub_satus', 'result', 'score', 'match_desc'])


# Single Photos
def fetchSinglePhotos(imageId):
    apiHost = frappe.db.get_single_value('Cric Credentials', 'api_host')
    apiKey = frappe.db.get_single_value('Cric Credentials', 'api_key')
    apiUrl = frappe.db.get_single_value('Cric Credentials', 'api_url')

    # Photos
    urlPhotos = apiUrl + "/img/v1/i1/c" + imageId + "/i.jpg"
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'X-RapidAPI-Key': apiKey,
        'X-RapidAPI-Host': apiHost
    }
    # response = requests.request(
    #     "GET", urlPhotos, headers=headers, data=payload)
    # if (response.status_code == 200):
    # addData = frappe.new_doc('Cric Photos')
    # addData.file = 'test'
    # addData.is_private = 0
    # addData.folder = 'Home'
    # addData.doctype = 'Cric Photos'
    # addData.file_name = "c" + imageId
    # addData.insert()
    # frappe.msgprint(str(response))
    return frappe.db.get_list('Cric Photos', filters={'name': imageId}, fields=['name', 'image_url'])


# Series List
@frappe.whitelist(allow_guest=True)
def getSeriesList(query):

    # Check Data
    series = frappe.db.get_list('Cric Series', filters={'status': 'open'}, order_by='startdt asc', fields=[
        'name', 'type', 'series_name', 'startdt', 'date'])
    return series


# Series Archives List
@frappe.whitelist(allow_guest=True)
def getSeriesArchivesList(query):

    # Check Data
    archives = frappe.db.get_list('Cric Series', filters={
                                  'date': query, 'status': 'archives'}, order_by='startdt asc', fields=['name', 'type', 'series_name', 'startdt', 'date'])
    if (len(archives) > 0):
        return archives
    else:
        data = fetchSeriesArchives(str(query))
        return data


# Teams List
@frappe.whitelist(allow_guest=True)
def getTeamsList():
    teams = frappe.db.get_list('Cric Teams', filters={}, fields=[
        'name', 'type', 'team_name', 'image_id', 'team_image', 'country_name'])
    finalTeams = []
    for item in teams:
        # Check Image
        if (item['team_image']) is None:
            item['team_image'] = 'aa'
            frappe.msgprint(str(item['team_image']))
            # newImage = fetchSinglePhotos(item['image_id'])
            # item['team_image'] = (newImage[0]['image_url']) if newImage else ''
        finalTeams.append(item)
    return finalTeams


# Matches By Day List
@frappe.whitelist(allow_guest=True)
def getMatchesByDay(query):

    # Check Data
    series = frappe.db.get_list('Cric Series', filters={
                                'status': 'open'}, fields=['name', 'date', 'type', 'series_name'])
    teams = frappe.db.get_list(
        'Cric Teams', filters={}, fields=['name', 'team_name'])
    matches = frappe.db.get_list('Cric Matches', filters={"startdt": ['>=', query]}, order_by='startdt asc', fields=[
                                 'name', 'series', 'startdt',  'team1', 'team2', 'venue', 'match_desc'])
    for match in matches:
        # Team1
        filterTeam1 = filter(
            lambda item: item["name"] == match['team1'], teams)
        newTeam1 = list(filterTeam1)
        if (len(newTeam1) > 0):
            match['team1'] = newTeam1[0]['team_name']

        # Team2
        filterTeam2 = filter(
            lambda item: item["name"] == match['team2'], teams)
        newTeam2 = list(filterTeam2)
        if (len(newTeam2) > 0):
            match['team2'] = newTeam2[0]['team_name']

        # Serie
        filterSerie = filter(
            lambda item: item["name"] == match['series'], series)
        newSerie = list(filterSerie)
        if (len(newSerie) > 0):
            match['series_name'] = newSerie[0]['series_name']
            match['series_type'] = newSerie[0]['type']
            match['series_date'] = newSerie[0]['date']
    return matches


# Matches By Filter List
@frappe.whitelist(allow_guest=True)
def getMatchesByFilter(query):

    # Check Data
    series = frappe.db.get_list('Cric Series', filters={
                                'status': 'open'}, fields=['name', 'date', 'type', 'series_name'])
    teams = frappe.db.get_list(
        'Cric Teams', filters={}, fields=['name', 'team_name', 'team_sname'])
    matches = frappe.db.get_list('Cric Matches', filters={"sub_satus": query}, order_by='startdt asc', fields=[
                                 'name', 'series', 'startdt',  'team1', 'team2', 'venue',  'sub_satus', 'result', 'score', 'match_desc'])
    for match in matches:
        # Team1
        filterTeam1 = filter(
            lambda item: item["name"] == match['team1'], teams)
        newTeam1 = list(filterTeam1)
        if (len(newTeam1) > 0):
            match['team1'] = newTeam1[0]['team_name']
            match['team1s'] = newTeam1[0]['team_sname']

        # Team2
        filterTeam2 = filter(
            lambda item: item["name"] == match['team2'], teams)
        newTeam2 = list(filterTeam2)
        if (len(newTeam2) > 0):
            match['team2'] = newTeam2[0]['team_name']
            match['team2s'] = newTeam2[0]['team_sname']

        # Serie
        filterSerie = filter(
            lambda item: item["name"] == match['series'], series)
        newSerie = list(filterSerie)
        if (len(newSerie) > 0):
            match['series_name'] = newSerie[0]['series_name']
            match['series_type'] = newSerie[0]['type']
            match['series_date'] = newSerie[0]['date']
    return matches


# Home Matches List
@frappe.whitelist(allow_guest=True)
def getHomeMatchList(query):

    # Check Data
    series = frappe.db.get_list('Cric Series', filters={
                                'status': 'open'}, fields=['name', 'date', 'type', 'series_name'])
    teams = frappe.db.get_list(
        'Cric Teams', filters={}, fields=['name', 'team_name', 'team_image', 'team_sname'])
    today = datetime.date.today()
    matches = frappe.db.get_list('Cric Matches', filters={"startdt": ['Between',  [query['start'], query['end']]]}, order_by='startdt asc', fields=[
                                 'name',  'series', 'startdt',  'team1', 'team2', 'venue',  'sub_satus', 'result', 'score', 'match_desc'])
    for match in matches:
        # Team1
        filterTeam1 = filter(
            lambda item: item["name"] == match['team1'], teams)
        newTeam1 = list(filterTeam1)
        if (len(newTeam1) > 0):
            match['team1'] = newTeam1[0]['team_name']
            match['team1s'] = newTeam1[0]['team_sname']
            match['team1_image'] = newTeam1[0]['team_image']

        # Team2
        filterTeam2 = filter(
            lambda item: item["name"] == match['team2'], teams)
        newTeam2 = list(filterTeam2)
        if (len(newTeam2) > 0):
            match['team2'] = newTeam2[0]['team_name']
            match['team2s'] = newTeam2[0]['team_sname']
            match['team2_image'] = newTeam2[0]['team_image']

        # Serie
        filterSerie = filter(
            lambda item: item["name"] == match['series'], series)
        newSerie = list(filterSerie)
        if (len(newSerie) > 0):
            match['series_name'] = newSerie[0]['series_name']
            match['series_type'] = newSerie[0]['type']
            match['series_date'] = newSerie[0]['date']
    return matches


# Matches By Series List
@frappe.whitelist(allow_guest=True)
def getMatchesBySeries(query):

    series = frappe.db.get_list('Cric Series', filters={
        'name': query}, fields=['name', 'date', 'type', 'series_name' ,'startdt', 'enddt'])
    teams = frappe.db.get_list(
        'Cric Teams', filters={}, fields=['name', 'team_name', 'team_sname'])

    # Check Data
    matches = frappe.db.get_list('Cric Matches', filters={"series": query}, order_by='startdt asc', fields=[
                                 'name',  'series', 'startdt',  'team1', 'team2', 'venue',  'sub_satus', 'result', 'score', 'match_format', 'match_desc'])
    if (len(matches) == 0):
        matches = updateMatchBySeries(query)
    for match in matches:
        # Team1
        filterTeam1 = filter(
            lambda item: item["name"] == match['team1'], teams)
        newTeam1 = list(filterTeam1)
        if (len(newTeam1) > 0):
            match['team1'] = newTeam1[0]['team_name']
            match['team1s'] = newTeam1[0]['team_sname']

        # Team2
        filterTeam2 = filter(
            lambda item: item["name"] == match['team2'], teams)
        newTeam2 = list(filterTeam2)
        if (len(newTeam2) > 0):
            match['team2'] = newTeam2[0]['team_name']
            match['team2s'] = newTeam2[0]['team_sname']

        # Serie
        filterSerie = filter(
            lambda item: item["name"] == match['series'], series)
        newSerie = list(filterSerie)
        if (len(newSerie) > 0):
            match['series_name'] = newSerie[0]['series_name']
            match['series_type'] = newSerie[0]['type']
            match['series_date'] = newSerie[0]['date']
            match['series_start'] = newSerie[0]['startdt']
            match['series_end'] = newSerie[0]['enddt']
    return matches
