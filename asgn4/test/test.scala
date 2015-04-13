class Point(val xc: Int, val yc: Int) 
{
   val x: Int = xc;
   val y: Int = yc;
   def move(dx: Int, dy: Int):Unit = 
   {
      x = x + dx;
      y = y + dy;
   }
}
object test 
{
   var a:Int=10;
   var asc:String="Hello";
   def main(args: Array[String]):String = 
   {
      val loc:Point = new Point(10, 20);

      // Move to a new location
      loc.move(10, 10);
      return "Hello"+"World";
   }
}