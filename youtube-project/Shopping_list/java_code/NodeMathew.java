/**
 * 
 * @author Daniel Mathew <br>
 * 
 * this is the class definition for NodeMathew<br>
 * this class contains functions of the linked list<br>
 * 
*/
public class NodeMathew 
{
	/**
     * 	instance variable for the NodeMathew data
    */
private ItemMathew myData;

/**
 * 	instance variable for the NodeMathew next
*/
private NodeMathew myNext;

/**
 * null constructor for the NodeMathew class
 * 
*/
public NodeMathew()
{
myData = null;
myNext = null;
}//NodeMathew

/**
 * full constructor for the ItemMathew class
 * 
 * @param newData is the new object from itemMathew
 * 
*/
public NodeMathew(ItemMathew newData)
{
myData = newData;
myNext = null;
}//NodeMathew

/**
 * this is a void method for setData
*/
public void setData(ItemMathew newData)
{
myData = newData;
}

/**
 * this is a void method for setNext
*/
public void setNext(NodeMathew newNext)
{
myNext = newNext;
}

/**
 * this is a getter method for the data
 * 
 * @return this returns a NodeMathew
*/
public ItemMathew getData()
{
return myData;
}

/**
 * this is a getter method for the next in the list
 * 
 * @return this returns a NodeMathew
*/
public NodeMathew getNext()
{
return myNext;
}

}//NodeMathew


