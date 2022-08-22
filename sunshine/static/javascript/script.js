
const cities = document.querySelectorAll(".city-name");
const icons = document.querySelectorAll(".city-icon");
const temps = document.querySelectorAll(".city-temp");
const temperature = document.getElementById("main-temp");

// Change cities
for (let i = 0; i < cities.length; i++) {
  cities[i].addEventListener("click", function() {
    changeCity();
    async function changeCity() {
      let newCity = prompt("Find yourself a new location!", cities[i].innerHTML);
      let response = await fetch(`http://api.weatherapi.com/v1/current.json?key=${KEY}&q=${newCity}&aqi=no`);
      let data = await response.json();
      
      if (i == 0) {
        const dateTime = data["location"]["localtime"];
        const rawMonth = dateTime.slice(5,7);
        const month = allMonths[rawMonth];
        const rawDay = dateTime.slice(8, 10);
        const hour = dateTime.slice(11, 16);

        document.getElementById("home-date").innerHTML =  month + " " + rawDay;
        document.getElementById("home-time").innerHTML = hour;
      };

      let icon = data["current"]["condition"]["icon"];
      let temp = data["current"]["temp_c"];

      if (temperature.value == 'celsius') {
        temp = data["current"]["temp_c"];
      } else {
        temp = data["current"]["temp_f"];
      }

      cities[i].innerHTML = newCity.toUpperCase();
      temps[i].innerHTML = Math.round(temp) + "°";
      icons[i].src = icon;

    };
  });
}

// Call for detailed analysis of 4 main cities listed on home page
for (let x = 0; x < icons.length; x++) {
  icons[x].addEventListener("click", function() {
    document.getElementById("search-field").value = cities[x].innerHTML;
    document.forms[0].submit();
  });
}

// Change temperature from Celsius to Fahrenheits and vice versa
temperature.addEventListener("click", function() {
    
  if (temperature.value == "celsius") {
    temperature.value = "fahrenheit";
    temperature.innerHTML = "F°";

    for (temp of temps) {
      temp.innerHTML = Math.round((parseInt(temp.innerHTML) * (9/5)) + 32) + "°";
    }
  } else {
    temperature.value = "celsius";
    temperature.innerHTML = "C°";

    for (temp of temps) {
      temp.innerHTML = Math.round((parseInt(temp.innerHTML) - 32) * 5/9) + "°";
    }
  }

});
