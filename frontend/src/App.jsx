import { useState } from "react";
import "./App.css";

function App() {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState(null);
  const [error, setError] = useState("");

  async function getWeather() {
    setError("");
    setWeather(null);

    if (!city.trim()) {
      setError("Please enter a city name");
      return;
    }

    const res = await fetch(
      `https://myweatherapp-a5k5.onrender.com/weather/${city}`
    );

    const data = await res.json();
    console.log(data);

    if (!res.ok) {
      setError(data.error || "Something went wrong");
      return;
    }

    setWeather(data);
}

  return (
    <div className="app">
      <div className="card">
        <h1>Weather App</h1>

        <input
          type="text"
          placeholder="Enter city"
          value={city}
          onChange={(e) => setCity(e.target.value)}
        />

        <button onClick={getWeather}>Get Weather</button>
        {error && <p className="error">{error}</p>}


        {weather && (
          <div className="weather">

            <h2>{weather.city}</h2>
            <h1>{weather.emoji}</h1>
            <h3>{weather.temp}°C</h3>
            <p>{weather.description}</p>
            
            
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
