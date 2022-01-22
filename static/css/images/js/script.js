function responsiveNavbar() {
    var x = document.getElementById("custom-navbar");
    if (x.className === "custom-navbar") {
      x.className += " responsive";
    } else {
      x.className = "custom-navbar";
    }
  }