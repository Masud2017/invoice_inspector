
 
  const EventChanger = ()=> {
    document.getElementById("place_holder").innerHTML = "Your envent is changed successfully";

}

const include = ()=> {

  xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("place_holder").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", 'header.html', true);
  xhttp.send();
  
}