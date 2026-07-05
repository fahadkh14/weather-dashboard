import React, { useEffect, useState } from "react";
import { fetchWeather, getHistory } from "./api";
import "./App.css";

function App() {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState(null);
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // Load History
  useEffect(() => {
    loadHistory();
  }, []);

  const loadHistory = async () => {
    const data = await getHistory();
    setHistory(data);
  };

  // Search Weather
  const handleSearch = async (e) => {
    e.preventDefault();

    if (!city.trim()) {
      setError("Please enter a city name.");
      return;
    }

    try {
      setLoading(true);
      setError("");

      const data = await fetchWeather(city);

      setWeather(data);
      setCity("");

      loadHistory();

    } catch (err) {
      setError(err.message);
      setWeather(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">

      <h1>🌦 Weather Dashboard</h1>

      <form onSubmit={handleSearch} className="search-box">

        <input
          type="text"
          placeholder="Enter City Name"
          value={city}
          onChange={(e) => setCity(e.target.value)}
        />

        <button type="submit">
          Search
        </button>

      </form>

      {loading && (
        <p className="loading">Loading...</p>
      )}

      {error && (
        <p className="error">{error}</p>
      )}

      {weather && (
        <div className="weather-card">

          <h2>
            {weather.city}, {weather.country}
          </h2>

          <img
            src={`https://openweathermap.org/img/wn/${weather.icon}@2x.png`}
            alt="Weather Icon"
          />

          <h3>{weather.temperature} °C</h3>

          <p>
            <strong>Weather :</strong> {weather.weather}
          </p>

          <p>
            <strong>Description :</strong> {weather.description}
          </p>

          <p>
            <strong>Humidity :</strong> {weather.humidity}%
          </p>

          <p>
            <strong>Wind Speed :</strong> {weather.wind_speed} m/s
          </p>

        </div>
      )}

      <div className="history">

        <h2>Recent Searches</h2>

        {history.length === 0 ? (
          <p>No Search History</p>
        ) : (
          <table>

            <thead>
              <tr>
                <th>City</th>
                <th>Country</th>
                <th>Temperature</th>
                <th>Weather</th>
                <th>Date</th>
              </tr>
            </thead>

            <tbody>

              {history.map((item, index) => (

                <tr key={index}>

                  <td>{item.city}</td>

                  <td>{item.country}</td>

                  <td>{item.temperature} °C</td>

                  <td>{item.weather}</td>

                  <td>
                    {new Date(item.searched_at).toLocaleString()}
                  </td>

                </tr>

              ))}

            </tbody>

          </table>
        )}

      </div>

    </div>
  );
}

export default App;
