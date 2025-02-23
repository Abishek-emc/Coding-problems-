/*An automobile company manufactures both a two wheeler(TW) and a four wheeler(FW). A company manger wants to
make the production of both types of vehicle according to the given data below:
 1st data , Total number of vehicle (two – wheeler + four - wheeler)=v
 2nd data, Total number of wheels=w
The task is to find how many two-wheelers as well as four-wheelers need to manufacture as per the given data.
Example:
Input:
200 -> Value of V
540 -> Value of W
Output:
TW=130 FW=70
Explanation:
130 + 70=200 vehicles
(70*4) + (130*2)=540 wheels
Constraints:
 2<=W
 W%2=0
 V<W
Print “INVALID INPUT”, if inputs did not meet the constraints.*/
import java.util.Scanner;
class Demo{
    
    public static void main(String arg[]){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of vehicles : ");
        int v = sc.nextInt();
        System.out.println();
        System.out.print("Enter the number of wheels : ");
        int w = sc.nextInt();
        System.out.println();
        int totalb = 0;
        int totalc = 0;
        
        
        if(2<=w & w%2==0 & v<w){
            
            
            while (totalb+totalc != v ){
                totalc += 1;
                w = w -4;
                totalb = w/2;
                   
            }
            System.out.println(String.format("Tw = %d \nFW = %d",totalb,totalc));
        }
        else{
            System.out.println("Invalid Input");
        }
    }
}