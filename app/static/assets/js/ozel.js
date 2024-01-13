function purchaseTickets(selectedLocation) {
    console.log("Selected Location:", selectedLocation);

    var form = document.createElement("form");
    form.setAttribute("method", "POST");
    form.setAttribute("action", "/tickets_filtered");

    var locationInput = document.createElement("input");
    locationInput.setAttribute("type", "hidden");
    locationInput.setAttribute("name", "location");
    locationInput.setAttribute("value", selectedLocation);

    form.appendChild(locationInput);
    
    document.body.appendChild(form);

    form.submit();
}