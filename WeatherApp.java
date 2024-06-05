import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class WeatherApp {

    // Replace with your own API key from OpenWeatherMap
    private static final String API_KEY = "YOUR_API_KEY";

    public static void main(String[] args) {
        String city = "London"; // Replace with the desired city name

        try {
            String weatherData = getWeatherData(city);
            System.out.println(weatherData);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static String getWeatherData(String city) throws Exception {
        String apiUrl = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY;

        URL url = new URL(apiUrl);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();

        BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
        StringBuilder result = new StringBuilder();
        String line;

        while ((line = reader.readLine()) != null) {
            result.append(line);
        }

        reader.close();
        return result.toString();
    }
}