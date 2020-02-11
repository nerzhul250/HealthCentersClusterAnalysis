import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class DataToDataBase {

	public static void main(String[] args) throws IOException {
		BufferedWriter bw=new BufferedWriter(new FileWriter("pandaData.csv"));
		BufferedReader br1=new BufferedReader(new FileReader("C:\\Users\\asus\\Documents\\GitHub\\HealthCentersClusterAnalysis\\ResearchAssistant\\rawDataToFormattedData\\PorCentrosDeSalud\\CSVFILES\\MAPPING.txt"));
		bw.write("EVA,TD,MD,ED,NE,DA,MA,TA,HOSPITAL,ID\n");
		for (int i = 0; i < 22; i++) {
			BufferedReader br2=new BufferedReader(new FileReader("C:\\Users\\asus\\Documents\\GitHub\\HealthCentersClusterAnalysis\\ResearchAssistant\\rawDataToFormattedData\\PorCentrosDeSalud\\CSVFILES\\"+i+".csv"));
			String name=br1.readLine().split("\\s+")[0];
			br2.readLine();//trash
			for (int j = 0; j < 27; j++) {
				String[] numbers=br2.readLine().split(",+");
				for(int k=0;k<=7;k++) {
					bw.write(numbers[k]+",");	
				}
				bw.write(name+","+i+"\n");
			}
			br2.close();
		}
		bw.close();
		br1.close();
	}
}
