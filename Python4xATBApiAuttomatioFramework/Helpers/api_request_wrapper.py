import json




def getreq(url,auth):
    getreposnse = requests.get(url=url,auth=auth)
    return getreposnse.json()

def postreq(url,auth,header,payload,in_json):

    postresponse = requests.post(url=url,auth=auth,headers=header,json=payload)
    if in_json is True:
        return postresponse.json()
    else:
        return postresponse

def putreq(url,auth,header,payload,in_json):
    putresponse = requests.post(url=url, auth=auth, headers=header, json=payload)
    if in_json is True:
        return putresponse.json()
    else:
        return putresponse

def patchreq(url,auth,header,payload,in_json):
    patchreponse = requests.post(url=url, auth=auth, headers=header, json=payload)
    if in_json is True:
        return patchreponse.json()
    else:
        return patchreponse


def deletereq(url,header,in_json):
    deletereponse =  requests.delete(url=url,headers=header)
    if in_json is True:
        return deletereponse.json()
    else:
        return deletereponse
