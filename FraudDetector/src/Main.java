import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.file.*;

public class Main {

    public static void main(String[] args) throws Exception {
        System.out.println("🔄 System started. Waiting for new purchases...");

        Path path = Paths.get("C:/Users/Allan/Desktop/Fraud/simulator/new_purchase.json");
        File fraudLog = new File("C:/Users/Allan/Desktop/Fraud/simulator/fraud_detect.jsonl");

        while (true) {
            if (Files.exists(path)) {
                String jsonInput = Files.readString(path);
                Files.delete(path);

                String response = sendToAPI(jsonInput);
                System.out.println("📥 Purchase received: " + jsonInput);
                System.out.println("🔍 Prediction result: " + response);

                if (response.contains("true")) {
                    System.out.println("⚠️ FRAUD ALERT!");
                    saveFraud(fraudLog, jsonInput, response);
                } else {
                    System.out.println("✅ Normal transaction.");
                }

                System.out.println("-----------");
            }

            Thread.sleep(1000);
        }
    }

    private static String sendToAPI(String jsonInputString) {
        try {
            URL url = new URL("http://localhost:8000/predict");
            HttpURLConnection con = (HttpURLConnection) url.openConnection();
            con.setRequestMethod("POST");
            con.setRequestProperty("Content-Type", "application/json; utf-8");
            con.setDoOutput(true);

            try (OutputStream os = con.getOutputStream()) {
                byte[] input = jsonInputString.getBytes("utf-8");
                os.write(input, 0, input.length);
            }

            try (BufferedReader br = new BufferedReader(
                    new InputStreamReader(con.getInputStream(), "utf-8"))) {
                StringBuilder response = new StringBuilder();
                String line;
                while ((line = br.readLine()) != null) {
                    response.append(line.trim());
                }
                return response.toString();
            }
        } catch (IOException e) {
            return "API error: " + e.getMessage();
        }
    }

    private static void saveFraud(File file, String input, String response) {
        try (FileWriter fw = new FileWriter(file, true)) {
            fw.write("{\"input\": " + input + ", \"response\": " + response + "}\n");
        } catch (IOException e) {
            System.out.println("❌ Error saving fraud: " + e.getMessage());
        }
    }
}