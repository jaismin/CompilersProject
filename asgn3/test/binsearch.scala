
object BinarySearch {
  def binarySearch(v: Int, vs: Array[Int]): Boolean = {
    
    var p:Boolean=false;
    if (v == 0) 
    {
      p=false;
    } 
    var left: Int = 0;
    var right: Int = v - 1;
    var mid: Int = 0;
    while (left != right) 
    {
     
      mid = left + (right - left) / 2;
      if (v <= vs[mid])
      {
        right = mid;
      }
      else
      {
        left = mid + 1;
      }
        
    }
    return vs[left] == v;
  }
  def binarySearchNewIndex(v1: Int, vs1: Array[Int]): Boolean = {
    
    if (v1 == 0) { p=false;}
    var left: Int = 0;
    var right: Int = vs.length;
    var mid: Int = 0;
    while (right - left != 1) {
      
      mid = left + (right - left) / 2;
      if (v < vs[mid])
        right = mid;
      else
        left = mid;
    }
    return vs[left] == v;
  }
}
object Main {
  def main(args: Array[String]):Unit =  {
  	var arr:Array[Int] = Array(1, 2, 3);
    println(BinarySearch.binarySearch(0,arr ));
   
  }
}