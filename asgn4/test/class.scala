
class Point(val xc: Int, val yc: Int) 
{

  var x: Int = xc;
  var y: Int = yc;
  def move(dx: Int, dy: Int) : Unit =
  {
    x = x + dx;
    y = y + dy;
  }
  //override def toString(): String = "(" + x + ", " + y + ")";
}


object Classes 
{
  def main(args: Array[String]) : Unit =  
  {
     // var (pt:Point)=(new Point(2,3));
      var pt:Point = new Point(1, 2) ;
    //println(pt)
    pt.move(10, 10);
    //println(pt)
  }
}