import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class DataIn {

	public static void main(String[] args) throws IOException {
		BufferedWriter bw=new BufferedWriter(new FileWriter("rawData.txt"));
		BufferedReader br=new BufferedReader(new FileReader("dataIn.txt"));
		br.readLine();//trash
		for (int i = 0; i < 22; i++) {
			String[] line=br.readLine().split(",");
			for (int j = 1; j < line.length; j++) {
				bw.write(line[j]+" ");
			}
			bw.write("\n");
		}
		bw.close();
		br.close();

	}

}
