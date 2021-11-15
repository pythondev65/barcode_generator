function Validate() {
  var country = document.getElementById("country");
  var state = document.getElementById("state");
  var gender = document.getElementById("gender");

  if (country.value == "") {
    alert("Please select country");
    return false;
  }
  else if (state.value == "") {
    alert("Please select state");
    return false;
  }
  else if (gender.value == "") {
    alert("Please select gender");
    return false;
  }

  return true;
}
