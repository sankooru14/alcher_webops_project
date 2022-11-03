const button = document.getElementById("give");


  if (navigator.geolocation){
    navigator.geolocation.getCurrentPosition(onSuccess, onError);
  }else {
    button.innerHTML = "Your browser not support";
  }


function onSuccess(position) {
  let {latitude, longitude} = position.coords;
  // console.log(latitude, longitude)

  fetch(`https://us1.locationiq.com/v1/reverse?key=pk.e3f94cdcca5b728f0aa65ab82656511e&lat=${latitude}&lon=${longitude}&format=json`)
  .then(response => response.json()).then(result => {
    let allDetails = result.address;
    let {city, state, postcode}=allDetails;
    button.innerHTML = `${city}, ${state}, ${postcode}`;
  })

}

function onError(error){
  if (error.code == 1) {//if user denied the request
    button.innerHTML = "you denied  the request";
  }
  else if (error.code == 2) {//if location is not available
    button.innerHTML = "Location not available";
  }else { //if any other error occured
    button.innerHTML = "Something went wrong";
  }

  button.setAttribute("disabled", "true");
}
