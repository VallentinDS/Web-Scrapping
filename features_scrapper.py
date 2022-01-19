import pandas as pd
from http import client
from pip._vendor import requests
import json


# Request URL from first POST in Console
entity_summaries_url = "https://analyticssuitefrontend-pa.clients6.google.com/v1/linkstats:getEntityLinkSummaries?alt=json&key=AIzaSyDdi6kVan9cRBol3P7chVkITxXs_o6lXHQ"

# Request URL from the table where it shows the integrations
list_links_url = "https://analyticssuitefrontend-pa.clients6.google.com/v1/linkstats:listLinks?alt=json&key=AIzaSyDdi6kVan9cRBol3P7chVkITxXs_o6lXHQ"

# Building the Payload like it is in Chrome
entity_sumaries_payload="{\"linkParticipant\":{\"entityType\":\"DBM_ADVERTISER\"},\"linkType\":\"GA_PROPERTY_DBM_ADVERTISER_LINK\",\"includeFeatures\":true,\"accessibleParticipantsOnly\":false,\"accessTypeFilter\":{\"accessType\":\"READ_LINK_PARTICIPANT\"}}"

# information from the cURL in the 1st POST request
entity_sumaries_headers = {
  'cookie': 'CONSENT=YES+shp.gws-20210923-0-RC1.en+FX+500; OGPC=19025836-2:19026101-2:; .DDMMUI-PROFILE=en__|6804290|296613; XSRF-TOKEN=AFCo3MDcpBOl80jEqGgQX4GaerpjrgNoJQ:1641912764455; SID=GAjom7O1xC3uiHMlXZKkZ7LnB7EzYsmC8--kkt0G-6qDyb_nWzj8kQyfyctnOMYbV6Wkyg.; __Secure-1PSID=GAjom7O1xC3uiHMlXZKkZ7LnB7EzYsmC8--kkt0G-6qDyb_nSa2jGylauRVqUGel1W3bBw.; __Secure-3PSID=GAjom7O1xC3uiHMlXZKkZ7LnB7EzYsmC8--kkt0G-6qDyb_nNgtHiuc8pXsn1yYTc3OfMg.; HSID=AJ3ZMJZH5gQqE1vuV; SSID=Anwkoax17dLBAbQ0C; APISID=4NAClmhcer_8YrIm/AKgwuqmiOWjqTs9le; SAPISID=y19c0SsX0y29DkRe/AbYIgyVguaMwfphjx; __Secure-1PAPISID=y19c0SsX0y29DkRe/AbYIgyVguaMwfphjx; __Secure-3PAPISID=y19c0SsX0y29DkRe/AbYIgyVguaMwfphjx; S=billing-ui-v3=ozhuF2ayPmSNwn_CjnJSftYjMkOJ3sfD:billing-ui-v3-efe=ozhuF2ayPmSNwn_CjnJSftYjMkOJ3sfD:acx-xbid-apps-core-frontend=N_WTb97JfuKkwh5iorY-mmLcp0eLIzHsNnDlBUF4pSs:acx-xbid-shard-manager-frontend=lerqs9OX-QQx-RgTL4IRjcvyPwCMuDxffRIHVg6XJDM:acx-xbid-apps-cm-frontend=DkMejxGDSe0iP1607gMmSmj5goDrtvsERLN3waW5TWs:acx-xbid-apps-planning-frontend=AryPZyKeOcV8gSo_XUZDfzbl8-Ll5eHmYGRQrXoswXQ:contentads-xbid-ui-deals=AHXBQYlFyrNd69CTz2-EAvemxAN-AqrHMeya1Em-5e8:contentads-xbid-ui-buying=TCdivK75eKx0IvRCvkc-2uUOPPIeRrIf1XRINN7KFbo:contentads-xbid-ui-planning=-AMlm42hR1MwRWkvCrGWBoXZQrA0FSNxKa6noVP4_m8:contentads-xbid-ui-core=rebVvao3kl6V_YUveXKmy42wVNYMxKz7F0yYm7dJ86U:acx-contentads-xbid-apps-deals-frontend=1pdUPz3F-P_Ofwp_rmgQm_Uz2Atps9i4zNhmrXU84l0:sso=XOGGPk0hSM0f7t1WXsuhiXn0p5kMm7S3:maestro=hnIjEKnoDgqZoJc8hTaK2gxJ4JQCcwmrWHvP4wiaNGY; NID=511=Tqt9EjrQoXYrpwoOeu2Oxg8sRKxCHjSzHDjFlGqE6_ncwdla274TctQqEm_hf8at8Dlli39ksAjdO2V5AeJ5HiRFYozmD3ueFt4wYDq8yu_dO1jreUNKVhdlkX2UzVUifyvQDDaW_Mg2k-rIpX7o1RJpWcNzhUnEhA3hMTqXdK7iUOMMXn686UOC1xvZCws5bzbSKfmK_A3cnynhY6qrrJ5IgusU8dLdY8Nn52a0V9V9ESscvBGHcOxiFs5JGf4DJiWC9ftNKhl7AEoE_a_55SktNikGnkFyHVaj0891UarI_9NXHAVqWIJyRMVgV7yL8Zax0JT-9YfIpq1Gj0Z_Bz5yckrITNzsgk6CjBSsau54Z2ouE5eTmv0wMzkmlPi_JzMHCiQ4RwxxSSBv_0fWko6Lyg; 1P_JAR=2022-01-17-17; SIDCC=AJi4QfF4xogyH8S4V5t5m8iTUjYBXkyeWscQ_7SnQoqBNZ9bE4dRnblIpAaSB-Mw4nRTIXacnK4q; __Secure-3PSIDCC=AJi4QfESfykinuG_1HU6DE1dIxXu25trkG_LmEJv7SDqnhRP8y9d3Dt-fXOtwgoDm85i2L8VoSQs; SIDCC=AJi4QfHstasruQEaRPnOBgHoKo2OLMMO1y5E6fHg6-fSQFCogzAoUsr4MFmm2M_4DEnEomKBc_7h; __Secure-3PSIDCC=AJi4QfG6NFuX3hRyLf2SR5SvfkRfwBhog7rE1NrJVLoYDPqQYJK8esa7iCO96BAgeHqoa9LRbw7S',
  'x-requested-with': 'XMLHttpRequest',
  'x-referer': 'https://marketingplatform.google.com',
  'x-origin': 'https://marketingplatform.google.com',
  'x-clientdetails': 'appVersion=5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F97.0.4692.71%20Safari%2F537.36&platform=MacIntel&userAgent=Mozilla%2F5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F97.0.4692.71%20Safari%2F537.36',
  'x-goog-authuser': '0',
  'authorization': 'SAPISIDHASH 1642442129_56f68755b98807d2753c1c871a42910a1c0d904a',
  'authority': 'analyticssuitefrontend-pa.clients6.google.com',
  'accept': '*/*',
  'referrer': 'https://analyticssuitefrontend-pa.clients6.google.com/static/proxy.html?usegapi=1&jsh=m%3B%2F_%2Fscs%2Fapps-static%2F_%2Fjs%2Fk%3Doz.gapi.en_GB.IkrNZh70o5I.O%2Fam%3DAQ%2Fd%3D1%2Frs%3DAGLTcCNy_VZAhmmDJ6o6is-m-46hrNpheg%2Fm%3D__features__',
  'Content-Type': 'application/json'
}
# # information from the cURL in the 2nd POST requ
list_links_headers = {
  'cookie': 'CONSENT=YES+shp.gws-20210923-0-RC1.en+FX+500; OGPC=19025836-2:19026101-2:; .DDMMUI-PROFILE=en__|6804290|296613; XSRF-TOKEN=AFCo3MDcpBOl80jEqGgQX4GaerpjrgNoJQ:1641912764455; SID=GAjom7O1xC3uiHMlXZKkZ7LnB7EzYsmC8--kkt0G-6qDyb_nWzj8kQyfyctnOMYbV6Wkyg.; __Secure-1PSID=GAjom7O1xC3uiHMlXZKkZ7LnB7EzYsmC8--kkt0G-6qDyb_nSa2jGylauRVqUGel1W3bBw.; __Secure-3PSID=GAjom7O1xC3uiHMlXZKkZ7LnB7EzYsmC8--kkt0G-6qDyb_nNgtHiuc8pXsn1yYTc3OfMg.; HSID=AJ3ZMJZH5gQqE1vuV; SSID=Anwkoax17dLBAbQ0C; APISID=4NAClmhcer_8YrIm/AKgwuqmiOWjqTs9le; SAPISID=y19c0SsX0y29DkRe/AbYIgyVguaMwfphjx; __Secure-1PAPISID=y19c0SsX0y29DkRe/AbYIgyVguaMwfphjx; __Secure-3PAPISID=y19c0SsX0y29DkRe/AbYIgyVguaMwfphjx; S=billing-ui-v3=ozhuF2ayPmSNwn_CjnJSftYjMkOJ3sfD:billing-ui-v3-efe=ozhuF2ayPmSNwn_CjnJSftYjMkOJ3sfD:acx-xbid-apps-core-frontend=N_WTb97JfuKkwh5iorY-mmLcp0eLIzHsNnDlBUF4pSs:acx-xbid-shard-manager-frontend=lerqs9OX-QQx-RgTL4IRjcvyPwCMuDxffRIHVg6XJDM:acx-xbid-apps-cm-frontend=DkMejxGDSe0iP1607gMmSmj5goDrtvsERLN3waW5TWs:acx-xbid-apps-planning-frontend=AryPZyKeOcV8gSo_XUZDfzbl8-Ll5eHmYGRQrXoswXQ:contentads-xbid-ui-deals=AHXBQYlFyrNd69CTz2-EAvemxAN-AqrHMeya1Em-5e8:contentads-xbid-ui-buying=TCdivK75eKx0IvRCvkc-2uUOPPIeRrIf1XRINN7KFbo:contentads-xbid-ui-planning=-AMlm42hR1MwRWkvCrGWBoXZQrA0FSNxKa6noVP4_m8:contentads-xbid-ui-core=rebVvao3kl6V_YUveXKmy42wVNYMxKz7F0yYm7dJ86U:acx-contentads-xbid-apps-deals-frontend=1pdUPz3F-P_Ofwp_rmgQm_Uz2Atps9i4zNhmrXU84l0:sso=XOGGPk0hSM0f7t1WXsuhiXn0p5kMm7S3:maestro=hnIjEKnoDgqZoJc8hTaK2gxJ4JQCcwmrWHvP4wiaNGY; NID=511=Tqt9EjrQoXYrpwoOeu2Oxg8sRKxCHjSzHDjFlGqE6_ncwdla274TctQqEm_hf8at8Dlli39ksAjdO2V5AeJ5HiRFYozmD3ueFt4wYDq8yu_dO1jreUNKVhdlkX2UzVUifyvQDDaW_Mg2k-rIpX7o1RJpWcNzhUnEhA3hMTqXdK7iUOMMXn686UOC1xvZCws5bzbSKfmK_A3cnynhY6qrrJ5IgusU8dLdY8Nn52a0V9V9ESscvBGHcOxiFs5JGf4DJiWC9ftNKhl7AEoE_a_55SktNikGnkFyHVaj0891UarI_9NXHAVqWIJyRMVgV7yL8Zax0JT-9YfIpq1Gj0Z_Bz5yckrITNzsgk6CjBSsau54Z2ouE5eTmv0wMzkmlPi_JzMHCiQ4RwxxSSBv_0fWko6Lyg; 1P_JAR=2022-01-17-17; SIDCC=AJi4QfF4xogyH8S4V5t5m8iTUjYBXkyeWscQ_7SnQoqBNZ9bE4dRnblIpAaSB-Mw4nRTIXacnK4q; __Secure-3PSIDCC=AJi4QfESfykinuG_1HU6DE1dIxXu25trkG_LmEJv7SDqnhRP8y9d3Dt-fXOtwgoDm85i2L8VoSQs; SIDCC=AJi4QfEPEUDrv7xOvSVafs07811qFq3_Kuc_36IO6_7qaqzioHQofiBhJcyRRP3pSw5Xf_3cZhR5; __Secure-3PSIDCC=AJi4QfEYcHgySZ32wjO-8i3NglO7sP-xUtuPDPmqn0qGx5-5G-POr95lR-CVOv9YOgXLpsdnPCTi',
  'x-requested-with': 'XMLHttpRequest',
  'x-referer': 'https://marketingplatform.google.com',
  'x-origin': 'https://marketingplatform.google.com',
  'x-clientdetails': 'appVersion=5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F97.0.4692.71%20Safari%2F537.36&platform=MacIntel&userAgent=Mozilla%2F5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F97.0.4692.71%20Safari%2F537.36',
  'x-goog-authuser': '0',
  'authorization': 'SAPISIDHASH 1642442129_56f68755b98807d2753c1c871a42910a1c0d904a',
  'authority': 'analyticssuitefrontend-pa.clients6.google.com',
  'accept': '*/*',
  'referrer': 'https://analyticssuitefrontend-pa.clients6.google.com/static/proxy.html?usegapi=1&jsh=m%3B%2F_%2Fscs%2Fapps-static%2F_%2Fjs%2Fk%3Doz.gapi.en_GB.IkrNZh70o5I.O%2Fam%3DAQ%2Fd%3D1%2Frs%3DAGLTcCNy_VZAhmmDJ6o6is-m-46hrNpheg%2Fm%3D__features__',
  'Content-Type': 'application/json'
}
def get_list_links_payload(field_name):
  return json.dumps({'linkParticipantNames': ["ga/property/-", field_name], 'accessTypeFilter': {"accessType": "READ_LINK_PARTICIPANT"}})

response = requests.request("POST", entity_summaries_url, headers=entity_sumaries_headers, data=entity_sumaries_payload)
dictionary_response = response.json()
print(dictionary_response)
print("\n")
print("\n")

features_list = []

for entity in dictionary_response['entityLinkSummaries']:
    response = requests.request("POST", list_links_url, headers=list_links_headers, data=get_list_links_payload(entity['linkParticipant']['name']))
    for element in response.json()['links']:
        for participant in element['participants']:
            property_name = element["participants"][0]["displayName"]
            formated_participant = str(participant['name'].split('/').pop())
            # features = map(lambda x: x.encode('ascii'), element['allowedFeatures'])
            features = element["allowedFeatures"]
            # print(property_name, formated_participant, features)
            # print("\n")
        # print(formated_participant)
        # print(property_name, formated_participant, features)

        list_features= [property_name, formated_participant, features]
        features_list.append(list_features)


features_list_df = pd.DataFrame(features_list)

# Renaming the columns
headers = {
    0: "Property name",
     1: "DV ID",
     2: "Features Enabled"
}
features_list_df.rename(mapper= headers, axis=1, inplace=True)

# SAVING THE FILE TO CSV
features_list_df.to_csv('client_features5.csv', index=False)