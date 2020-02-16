import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class DataFormatterPerformance {

	public static void main(String[] args) throws IOException {
		BufferedWriter bw=new BufferedWriter(new FileWriter("formattedDataPerformance.txt"));
		String pathCSV="C:\\Users\\asus\\Documents\\GitHub\\HealthCentersClusterAnalysis\\"
				+ "ResearchAssistant\\rawDataToFormattedData\\PorCentrosDeSalud\\"
				+ "CSVFILEANALISISDESEMPENIO.csv";
		BufferedReader br=new BufferedReader(new FileReader(pathCSV));
		String[][][] theWholeData=new String[25][22][7];
		for (int i = 0; i < 25; i++) {
			br.readLine();br.readLine();br.readLine();br.readLine();//trash
			String tableName=br.readLine().replaceAll(";+","");
			br.readLine();//trash
			for (int j = 0; j <22; j++) {
				String[] data=br.readLine().split(";+");
				for (int k = 3; k < 10; k++) {
					theWholeData[i][j][k-3]=data[k];
				}
			}
		}
		for (int j = 0; j < 22; j++) {
			for (int i = 0; i < 25; i++) {
				for (int k = 0; k < 7; k++) {
					String s=theWholeData[i][j][k];
					bw.write(s+" ");
				}
			}
			bw.write("\n");
		}
		br.close();
		bw.close();
	}
}
