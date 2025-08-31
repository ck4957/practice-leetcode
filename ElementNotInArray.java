import java.util.Arrays;
public class ElementNotInArray {
	public int nextElement(int[] arr, int K) {
		Arrays.sort(arr);
		int i=0; 
		int j=i+1;
		int maxElement = 0;
		while(j < arr.length && arr[i] < K) {
			i++; j++;
		}
		maxElement = j == arr.length ? 0 : arr[i];	
		while(j < arr.length) {
			if(arr[j]-arr[i] <= 1) {
				i++; j++;
			}
			else{
				return arr[i]+1;
			}
		}
		return maxElement == 0 ? -1 : arr[j-1]+1;

	}
	public static void main(String[] args) {
		ElementNotInArray elementNotInArray = new ElementNotInArray();
		//int[] array = new int[] {2,5,7,9,20,20,21,22,23,24,24,24,24,25,30};
		//int[] array = new int[] {2,4,6,8,10,20};
		int[] array = new int[] {1,4,5,2,7};
		//int[] array = new int[] {1,1,1,1,1,1,1,1,1,1,1};
		int K=4;
		int nextGreatestElementNotInArray = elementNotInArray.nextElement(array,K);
		System.out.println("nextGreatestElementNotInArray: " + nextGreatestElementNotInArray);
		
	}
}