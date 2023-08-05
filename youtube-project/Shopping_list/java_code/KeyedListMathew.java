/**
 * 
 * @author Daniel Mathew <br>
 * 
 * this is the class definition for KeyedListMathew<br>
 * this class contains fuctions of the list including clear,add,remove ect.<br>
 * 
*/
public class KeyedListMathew 
{
	/**
     * 	instance variable for the ItemMathew items
    */
private NodeMathew myHead;


/**
 * full constructor for the KeyedlistMathew class
 * 
 * @param newSize the new size for the list
 * 
*/
public KeyedListMathew(int newSize)
{
myHead = null;
}//KeyedListMathew

/**
 * this is a getter method for the getHead
 * 
 * @return this returns a NodeMathew
*/
public NodeMathew getHead()
{
return myHead;
}//getHead

/**
 * this void method allows the user to clear the list.
*/
public void setHead(NodeMathew newHead)
{
myHead = newHead;
}//setHead

/**
 * this void method allows the user to clear the list.
*/
public void clear() 
{
myHead = null;
}//clear

/**
 * this method allows the user to add a song to the item list up to ten items
 * 
 * @param product this is the product for the song
 * @return this returns a boolean which tells if the item was added or not
*/
public boolean add(ItemMathew product)
{
boolean success = false;
boolean found = false;
NodeMathew curr = myHead;
NodeMathew prev = null;
NodeMathew newGuy = null;

newGuy = new NodeMathew(product);

	while ((curr != null) && (!found))
	{
		if (product.getName().compareToIgnoreCase(curr.getData().getName()) == 0)
			found = true;
		else
		{
			prev = curr;
			curr = curr.getNext();
		}//else
	}//while
	
	if (!found) 
	{
		newGuy.setNext(curr);

		if (prev == null) 
		{
			myHead = newGuy;
			success = true;
		}//if
		else 
		{
			prev.setNext(newGuy);
			success = true;
		}//else	
	}//if
	
return success;
}//add


/**
 * this method allows the user to remove a song to the list
 * 
 * @param keyValue this is the target value
 * @return  this returns a boolean which tells if the song was removed or not
*/
public boolean remove(String keyValue)
{
boolean found = false;    
NodeMathew curr = myHead;
NodeMathew prev = null;

    while ((curr != null) && (!found))
        if (curr.getData().getName().equalsIgnoreCase(keyValue))
            found = true;
        else
        {
            prev = curr;
            curr = curr.getNext();
        }//else
    
    if (found)
    {
        if (prev == null)
            myHead = curr.getNext();
        else
            prev.setNext(curr.getNext());
    }//if
    
    return found;
}//remove

/**
 * this method allows the user to retrieve a item 
 * 
 * @param keyValue this is the target value
 * @return  this returns a itemMathew
*/
public ItemMathew retreive(String keyValue)
{
ItemMathew value = null;
NodeMathew curr = myHead;

while(curr != null)
{
if(curr.getData().getName().equalsIgnoreCase(keyValue))
	value = curr.getData();
	curr = curr.getNext();
}//while

return value;
}//retreive

/**
 * this method allows the user to see if the list is empty
 * 
 * @return this returns a boolean which tells if it is empty or not
*/
public boolean isEmpty()
{
return(myHead == null);
}//isEmpty

/**
 * this method allows the user to see if the list is full
 * 
 * @return this returns a boolean which tells if it is full or not
*/
public boolean isFull()
{
return false;
}//isFull

/**
 * this void method allows the user to print the list
*/
public void print()
{
NodeMathew curr = myHead;
int count = 1;
	
	while(curr != null)
	{
	System.out.println("Item" + count + curr.getData());
	curr = curr.getNext();
		count++;
    }//while
}// print

/**
 * this method allows the user to get the count of items
 * 
 * @return  this returns an int of the sum of items
*/
public int getCount()
{
NodeMathew curr = myHead;
int count = 0;

	while(curr != null)
	{
		count += curr.getData().getQuantity();
	}//while

return count;
}//getCount

/**
 * this method allows the user to calculate the total of the items
 * 
 * @return  this returns a double of the total cost
*/
public double calcTotal()
{
double total = 0;
NodeMathew curr = myHead;

while(curr != null)
{
	total += (curr.getData().getPrice() * curr.getData().getQuantity());
	curr = curr.getNext();
}//while

System.out.println("The sum is: " + total);

return total;
}//calcTotal

}//KeyedListMathew
