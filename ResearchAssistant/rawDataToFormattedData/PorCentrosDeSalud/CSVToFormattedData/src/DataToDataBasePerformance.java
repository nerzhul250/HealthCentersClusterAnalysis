import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class DataToDataBasePerformance {

	public static void main(String[] args) throws IOException {
		BufferedWriter bw=new BufferedWriter(new FileWriter("pandaDataPerformance.csv"));
		String pathCSV="C:\\Users\\asus\\Documents\\GitHub\\HealthCentersClusterAnalysis\\"
				+ "ResearchAssistant\\rawDataToFormattedData\\PorCentrosDeSalud\\"
				+ "CSVFILEANALISISDESEMPENIO.csv";
		BufferedReader br=new BufferedReader(new FileReader(pathCSV));
		bw.write("EVA,NU,CN,AV,NE,MV,CS,SI,HOSPITAL,ID\n");
		for (int i = 0; i < 25; i++) {
			br.readLine();br.readLine();br.readLine();br.readLine();//trash
			String tableName=br.readLine().replaceAll(";+","");
			br.readLine();//trash
			for (int j = 0; j <22; j++) {
				String[] data=br.readLine().split(";+");
				bw.write(tableName+",");
				for (int k = 3; k < 10; k++) {
					bw.write(data[k]+",");
				}
				bw.write(data[1]+","+j+"\n");
			}
		}
		br.close();
		bw.close();
	}

}
