object Sum extends App 
{
  
  println(sum(list));
  println(sum2(list));
  println(sum3(list));
   
  def sum(ints:Array[String]): Int =
  { 
    println(ints);
  }
 
  def sum2(ints: Array[People]): Int = {

    def sumAccumulator(ints: Array[Int], accum: Int): Int = 
    {
      sum(accum,ints);
    }
    sumAccumulator(ints, 0);
  }

  def sum3(xs: Array[Int]): Int = {
    if (xs.isEmpty) 
      p=1;
    else 
      p=xs.head + sum3(xs.tail);
  }
   
}