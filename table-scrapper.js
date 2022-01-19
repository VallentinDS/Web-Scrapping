// var IntegrationDetails = [{
//     property1 = {}
// }]
// i=0;
// for(i=0;i < document.querySelectorAll('mat-row').size(); i++) {
// IntegrationDetails[i]["Property Name"] = document.querySelectorAll('mat-row')[i].innerText
// }

// IntegrationDetails[0]["Advertiser"] = document.querySelector("#cdk-overlay-1 > mdx-slider-container > ic-product-pair-table > div > div > mat-table > mat-row:nth-child(2) > mat-cell.mat-cell.cdk-cell.mdx-table-cell.mdx-table-cell-action.cdk-column-entityCountText.mat-column-entityCountText.ng-star-inserted > span").innerText

// IntegrationDetails[0]["Tracking ID"] = document.querySelector("#cdk-overlay-1 > mdx-slider-container > ic-product-pair-table > div > div > mat-table > mat-row:nth-child(2) > mat-cell.mat-cell.cdk-cell.mdx-table-cell.mdx-table-cell-action.cdk-column-id.mat-column-id.ng-star-inserted > span").innerText

// IntegrationDetails[0]["Account"] = document.querySelector("#cdk-overlay-1 > mdx-slider-container > ic-product-pair-table > div > div > mat-table > mat-row:nth-child(2) > mat-cell.mat-cell.cdk-cell.mdx-table-cell.mdx-table-cell-action.cdk-column-parent.mat-column-parent.ng-star-inserted > span").innerText

// IntegrationDetails[0]["Organisation name"] = document.querySelector("#cdk-overlay-1 > mdx-slider-container > ic-product-pair-table > div > div > mat-table > mat-row:nth-child(2) > mat-cell.mat-cell.cdk-cell.mdx-table-cell.mdx-table-cell-action.cdk-column-parent.mat-column-parent.ng-star-inserted > span").innerText

// IntegrationDetails[0]["Integrations with reporting data"] = document.querySelector("#cdk-overlay-1 > mdx-slider-container > ic-product-pair-table > div > div > mat-table > mat-row:nth-child(2) > mat-cell.mat-cell.cdk-cell.mdx-table-cell.mdx-table-cell-action.ic-icon-cell.cdk-column-feature0.mat-column-feature0.ng-star-inserted > span").innerText

// IntegrationDetails[0]["Integrations with Cost Data"] = document.querySelector("#cdk-overlay-1 > mdx-slider-container > ic-product-pair-table > div > div > mat-table > mat-row:nth-child(2) > mat-cell.mat-cell.cdk-cell.mdx-table-cell.mdx-table-cell-action.ic-icon-cell.cdk-column-feature0.mat-column-feature0.ng-star-inserted > span").innerText

// IntegrationDetails[0]["Integrations with Remarketing Lists"] = document.querySelector("#cdk-overlay-1 > mdx-slider-container > ic-product-pair-table > div > div > mat-table > mat-row:nth-child(2) > mat-cell.mat-cell.cdk-cell.mdx-table-cell.mdx-table-cell-action.ic-icon-cell.cdk-column-feature2.mat-column-feature2.ng-star-inserted > span").innerText

// copy(IntegrationDetails)

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

// copy Response text first

x = // reponse text

x.links.forEach(element => {
    element.participants.forEach(participant => {
    console.log(participant.name.split('/').pop(), element.allowedFeatures);
    IntegrationDetails.push({
        participant.name.split('/').pop() : element.allowedFeatures}
    })
    });
    })

    x.links.forEach(element => {
        element.participants.forEach(participant => {
        IntegrationDetails[participant.name.split('/').pop()]=element.allowedFeatures
        });
        })


        x.links.forEach(element => {
            element.participants.forEach(participant => {
            console.log(participant.name.split('/').pop(), element.allowedFeatures)
            });
            })