package randomBuiltin;

import java.util.Random;
import java.util.Arrays;

public class RandomJava {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Random rand = new Random();
		// 9 is the maximum and the 0 is our minimum
		
		int maxVal = 100;
		// int [] num = new int[maxVal];
		for (int i = 0; i <= maxVal; i ++) {
			int  n = rand.nextInt(9);
			System.out.println(n);
		}
	}
}
