import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class DataFormatter {

	public static void main(String[] args) throws IOException {
		BufferedWriter bw=new BufferedWriter(new FileWriter("rawData.txt"));
		for (int i = 0; i < 22; i++) {
			BufferedReader br=new BufferedReader(new FileReader("C:\\Users\\asus\\Documents\\GitHub\\HealthCentersClusterAnalysis\\ResearchAssistant\\rawDataToFormattedData\\PorCentrosDeSalud\\CSVFILES\\"+i+".csv"));
		
			br.readLine();//trash
			for (int j = 0; j < 27; j++) {
				String[] numbers=br.readLine().split(",+");
				for(int k=1;k<=7;k++) {
					bw.write(numbers[k]+" ");					
				}
			}
		
			bw.write("\n");
			br.close();
		}
		bw.close();
	}

}
