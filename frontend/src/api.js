import axios from "axios";

// Backend API URL
const API_URL =
  process.env.REACT_APP_API_URL || "http://localhost:5000";

// Axios Instance
const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
  timeout: 10000,
});

// ===============================
// Fetch Weather by City
// ===============================
export const fetchWeather = async (city) => {
  try {
    const response = await api.get("/weather", {
      params: { city },
    });

    return response.data;
  } catch (error) {
    if (error.response) {
      throw new Error(
        error.response.data.error || "Unable to fetch weather data."
      );
    }

    throw new Error("Backend server is not responding.");
  }
};

// ===============================
// Fetch Search History
// ===============================
export const getHistory = async () => {
  try {
    const response = await api.get("/history");
    return response.data;
  } catch (error) {
    console.error(error);
    return [];
  }
};

export default api;
