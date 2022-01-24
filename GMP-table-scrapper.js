var IntegrationDetails = []

for(let i=0;i < document.querySelectorAll('mat-row').length; i++) {
    IntegrationDetails.push( {
        "Property Name":  document.querySelectorAll('mat-row')[i].querySelectorAll("mat-cell")[1].innerText,
        "Advertiser": document.querySelectorAll('mat-row')[i].querySelectorAll("mat-cell")[2].innerText,
        "Tracking ID" : document.querySelectorAll('mat-row')[i].querySelectorAll("mat-cell")[3].innerText,
        "Account" : document.querySelectorAll('mat-row')[i].querySelectorAll("mat-cell")[4].innerText,
        "Organisation name" : document.querySelectorAll('mat-row')[i].querySelectorAll("mat-cell")[5].innerText,
        "Int with report data" : document.querySelectorAll('mat-row')[i].querySelectorAll("mat-cell")[6].innerText,
        "Int with Cost Data" : document.querySelectorAll('mat-row')[i].querySelectorAll("mat-cell")[7].innerText,
        "Int with Remarketing Lists" : document.querySelectorAll('mat-row')[i].querySelectorAll("mat-cell")[8].innerText
    })
}

copy(IntegrationDetails)


            