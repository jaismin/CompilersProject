class Point1(val xc: Int, val yc: Int) 
{
  var z:Array[Int] = Array(1,2,3);
  var z1:Int = 1;
  var z3:Int=z1;
  def sum(b: Int) : Int =
  {
   var a:Int=b;
   z1=4;

   for( a <- 1 until 10)
   {
   var b:Int=3;
   b=xc;

  }
  return 1;

  }
}

object HelloWorld
{
  
def main(args: Array[String]): Unit = 
{
  var (x:Point1)=(new Point1(2,3));
  var y:Int = x.z[0];
  x.z1=1;
  x.z[1]=10;
  y=x.sum(10);
  y=x.yc;


}
}