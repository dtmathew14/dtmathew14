/**
 * 
 * @author Daniel Mathew <br>
 * 
 * this is the class definition for ItemMathew<br>
 * this class contains setters,getters, and private instance variablesst<br>
 * 
*/
import java.text.*;

public class ItemMathew 
{
/**
* instance variable for the item name
*/
private String myName;

/**
 * instance variable for the item quantity
*/
private int myQuantity;

/**
 * instance variable for the item price
*/
private double myPrice;

/**
 * full constructor for the SongMathew class
 * 
 * @param newName the new name for the item
 * @param newQuantity the new quantity for the item
 * @param newPrice the new price for the item
 * 
*/

public ItemMathew(String newName, int newQuantity, double newPrice)
{
    myName = newName;
    myQuantity = newQuantity;
    myPrice = newPrice;
}//SongMathew

/**
 * setter method for the item name
 * 
 * @param newName the new name for the item
*/
public void setName(String newName) 
{
    myName = newName;
}//setName

/**
 * setter method for the item quantity
 * 
 * @param newQuantity the new quantity for the item
*/
public void setQuantity(int newQuantity) 
{
    myQuantity = newQuantity;
}//setRuntime

/**
 * setter method for the item price
 * 
 * @param newPrice the new price for the item
*/
public void setPrice(double newPrice) 
{
    myPrice = newPrice;
}//setPrice

/**
 * getter method for the item name
 * 
 * @return the current value of the item name
*/
public String getName() 
{
    return myName;
}//getName

/**
 * getter method for the item quantity
 * 
 * @return the current value of the item quantity
*/
public int getQuantity() 
{
    return myQuantity;
}//getRuntime

/**
 * getter method for the item price
 * 
 * @return the current value of the item price
*/
public double getPrice() 
{
    return myPrice;
}//getPrice

/**
 * toString method for the item price
 * 
 * @return prints out a string of the item info
*/
public String toString()
{
	DecimalFormat moneystyle = new DecimalFormat("0.00"); 
	
	String ans = "\nName: " + getName() + "\n";
	ans += "Quantity: " + getQuantity() + "\n";
	ans += "Price: $" + moneystyle.format(getPrice()); 
	return ans;	
}//toString

}//ItemMathew
