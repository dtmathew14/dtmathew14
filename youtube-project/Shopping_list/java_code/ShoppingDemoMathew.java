/**
*
* @author Daniel Mathew <br>
* 
* Prog9Mathew<br>
* Due Date and Time: 04/06/23 before 10:30 a.m.<br>
*
* Purpose: This program uses a menu which you can input values for a <br>
*	song item list.<br>
*
*Input: menu buttons, item information <br>
*
*Output: details about items/itemlist, add/del/total/clear etc.<br>
*
*Certification of Authenticity:<br>
*I certify that this lab is entirely my own work but i discussed it with kyle. <br>
*/

import java.io.*;
import java.util.*;


public class ShoppingDemoMathew {

	static Scanner keyboard = new Scanner (System.in);
	
	public static void main(String[] args) 
	{		
		char choice = 'z';		
		String itemName="";
		int itemQuantity = 0;
		double itemPrice =0;

		KeyedListMathew itemList = new KeyedListMathew(0);
		ItemMathew newItem = null;
		boolean added = false;
		boolean deleted = false;
		ItemMathew item = null;
		
		String fileName = null;
		int numValues =0;
		int i = 0;
		
		System.out.println("Welcome to the Prog10 linkedlist project.");
		
		System.out.println("Enter a file name: ");
		fileName = keyboard.next();
		
		File inputFile = new File(fileName);
		
		try (Scanner input = new Scanner (inputFile))
		{
			numValues = input.nextInt();
			
			for(i=0; i< numValues; i++ )
			{
			itemName = input.next();      
		    itemQuantity = input.nextInt();
		    itemPrice = input.nextDouble();
		    
		    newItem = new ItemMathew(itemName,itemQuantity, itemPrice);
		    added = itemList.add(newItem);		
			}//for 
		input.close();
		}//try
		
		catch(FileNotFoundException ex)
		{
		System.out.println("Failed to find file: " + inputFile.getAbsolutePath());
		}//catch
		
		catch(InputMismatchException ex)
		{
		System.out.println("Type mismatch for the number I just tried to read.");
		System.out.println(ex.getMessage ( ));
		}//catch
		
		catch (NumberFormatException ex)
		{
		System.out.println("Failed to convert String text into an integer value.");
		System.out.println(ex. getMessage());
		}//catch
		
		catch(NullPointerException ex)
		{
		System.out.println("Null pointer exception.");
		System.out.println(ex.getMessage ());
		}//catch
		
		catch(Exception ex)
		{
		System.out.println("Something went wrong"); 
		ex.printStackTrace();
		}//catch
		
		do
		{
		System.out.println("\nMENU");
		System.out.println("1: Add an item to the list");
		System.out.println("2: Delete an item from the list");
		System.out.println("3: Print each item in the list");
		System.out.println("4: Search for a user-specified item in the list");
		System.out.println("5: Count the total number of items in the list");
		System.out.println("6: Total the cost of the items in the list");
		System.out.println("7: Determine whether the list is empty");
		System.out.println("8: Determine whether the list is full");
		System.out.println("9: Clear the list");
		System.out.println("0: Quit");

		System.out.print("Enter your choice: ");
		choice = keyboard.next().toUpperCase().charAt(0);

		switch (choice) 
		{
		case '1':
		    System.out.print("Add Item Name: ");
		    itemName = keyboard.next();    
		    		    		    
		    do 
			{
		    	System.out.print("Add Item Quantity: ");
		    	itemQuantity = keyboard.nextInt();
			}//do
			while(itemQuantity <= 0);		    

		    do 
			{
				System.out.print("Add Item Price: ");
			    itemPrice = keyboard.nextDouble();
			}//do
			while(itemPrice <= 0);
		    
		    newItem = new ItemMathew(itemName,itemQuantity, itemPrice);
		    added = itemList.add(newItem);
		    if (added == true)
		    	System.out.print("Added");
		    else System.out.print("Not added");
		    break;
		case '2':
			System.out.print("Delete Item Name: ");
		    itemName = keyboard.next();    
		    deleted = itemList.remove(itemName);
		    
		    if (deleted == true)
		    	System.out.print("deleted");
		    else System.out.print("Not There");
			break;
		case '3':		
			if(itemList.isEmpty() == true)
				System.out.print("The list is empty");
			itemList.print();// what if empty
			break;
		case '4':	
			System.out.print("Search for an item: ");
		    itemName = keyboard.next();    
		     item = itemList.retreive(itemName);
		 if (item != null) 
		 {
		     System.out.println("Item found: " + item.getName());
		     System.out.println("Quantity: " + item.getQuantity());
		     System.out.printf("Price: $%.2f", item.getPrice());
		 }//if
		 else System.out.println("Item not found.");
		    break;
		case '5':		
			System.out.print("The item total is " + itemList.getCount());
			break;
		case '6':
			System.out.printf("The item total price is %.2f", itemList.calcTotal());	
			break;
		case '7':
			if(itemList.isEmpty() == true)
				System.out.print("The list is empty");
			else System.out.print("the list is not empty");
			break;
		case '8':
			if(itemList.isFull() == true)
				System.out.print("The list is full");
			else System.out.print("the list is not full");
			break;
		case '9':			
			itemList.clear();
			System.out.print("The list has been cleared");
			break;
		case '0':
			System.out.println("Goodbye! Thanks for running this program.");
			break;
		default:
			System.out.println("Invalid choice. Try again.");
		}//switch

		}//do
		while (choice != 0);

	keyboard.close();
	
	}//main

}//prog9Mathew

