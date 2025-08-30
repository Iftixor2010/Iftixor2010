// app.js

const form = document.querySelector("#change-location");
const card = document.querySelector("#card");
const details = document.querySelector("#details");
const icon = document.querySelector("#weather-icon");
const overlay = document.querySelector("#overlay");

const apiKey = "dd412ccab9257a81ba083972c53adce6"; 

// ob-havoni shahar bo‘yicha olish
async function getWeather(city) {
  const base = "https://api.openweathermap.org/data/2.5/weather";
  const query = `?q=${city}&units=metric&appid=${apiKey}`;
  const response = await fetch(base + query);
  if (!response.ok) {
    throw new Error("Shahar topilmadi");
  }
  const data = await response.json();
  return data;
}

// UI yangilash
function updateUI(data) {
  const { name, weather, main } = data;

  details.innerHTML = `
    <h5 class="mb-3">${name}</h5>
    <p class="mb-3">${weather[0].description.toUpperCase()}</p>
    <div class="display-4 mb-3">
      <span>${Math.round(main.temp)}</span>
      <span>&deg;C</span>
    </div>
  `;

  // ob-havo iconi
  const iconSrc = `https://openweathermap.org/img/wn/${weather[0].icon}@2x.png`;
  icon.setAttribute("src", iconSrc);

  card.classList.remove("d-none");
}

// formni tinglash
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const city = form.city.value.trim();

  overlay.classList.remove("d-none"); 
  getWeather(city)
    .then((data) => {
      updateUI(data);
      overlay.classList.add("d-none");
    })
    .catch((err) => {
      overlay.classList.add("d-none");
      alert(err.message);
    });
    

  form.reset();
});


