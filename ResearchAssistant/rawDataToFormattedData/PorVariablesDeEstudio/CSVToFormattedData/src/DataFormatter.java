import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class DataFormatter {

	public static void main(String[] args) throws IOException {
		BufferedWriter bw=new BufferedWriter(new FileWriter("rawData.txt"));
		for (int i = 0; i < 27; i++) {
			BufferedReader br=new BufferedReader(new FileReader("..\\CSVFILES\\"+i+".csv"));
			for (int j = 0; j < 22; j++) {
				String[] numbers=br.readLine().split(";");
				for(int k=0;k<7;k++) {
					bw.write(numbers[k]+" ");					
				}
			}
		
			bw.write("\n");
			br.close();
		}
		bw.close();
	}

}
